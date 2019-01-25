import ast

from enum import Enum

from core.himesis_utils import graph_to_dot


class MutationOperators(Enum):

    #ADD OPERATIONS
    ADD_CLASS = "ADD_CLASS"
    ADD_ASSOC = "ADD_ASSOC"
    ADD_BACK_LINK = "ADD_BACK_LINK"

    #DELETE OPERATIONS
    DELETE_ELEMENT = "DELETE"

    #MODIFY OPERATIONS
    RENAME_CLASS = "RENAME_CLASS"
    RENAME_ASSOC = "RENAME_ASSOC"

    #ATTRIB OPERATIONS
    DELETE_ATTRIB = "DELETE_ATTRIB"
    DELETE_EQ = "DELETE_EQ"

    CHANGE_TERM_NODE = "CHANGE_TERM_NODE"
    CHANGE_TERM_ATTRIB = "CHANGE_TERM_ATTRIB"

    CHANGE_CONCAT = "CHANGE_CONCAT"
    CHANGE_ATOM = "CHANGE_ATOM"

    # TO ADD
    #   CLASSES:
    #   Change Any/Exists type of classes
    #   Change positive/negative type of classes

    #   ASSOCIATIONS:
    #   Change positive/negative associations
    #   Change direct/indirect associations

    #   BACKWARD LINKS
    #   Change negative/positive

class Mutator:

    def __init__(self, rule_to_mutate, mutate):
        self.rule_to_mutate = rule_to_mutate
        self.mutate = ast.literal_eval(mutate)

        self.structural_classes = ["MatchModel", "ApplyModel", "paired_with",
                                   "match_contains", "apply_contains"
                                   ]
        self.link_classes = ["directLink_S", "directLink_T", "backward_link"]

        self.debug = True

    def print_rule(self, rule):
        mms = rule.vs["mm__"]
        print("Rule: " + rule.name)
        print([v["mm__"] for v in rule.vs])
        print([str(edge.source) + "-" + str(edge.target) for edge in rule.es])
        print([str(mms[edge.source]) + "-" + str(mms[edge.target]) for edge in rule.es])


    def debug_rule(self, rule, stage):

        if not self.debug:
            return

        if stage:
            stage_str = "before"
        else:
            stage_str = "after"


        self.print_rule(rule)
        graph_to_dot(rule.name + "_" + str(self.mutate[0]) + str(self.mutate[1]) + "_" + stage_str, rule)


    def mutate_rules(self, rules, transformation):

        for i, layer in enumerate(transformation):
            for j, rule in enumerate(layer):
                if self.rule_to_mutate == rule.name:

                    self.debug_rule(rule, True)
                    self.mutate_rule(rule)
                    self.debug_rule(rule, False)

                    rules[rule.name] = rule

        #raise Exception()
        return rules, transformation

    def mutate_rule(self, rule):

        print("Mutating " + rule.name + " with " + str(self.mutate))

        op = self.mutate[0]
        try:
            # call the mutation function
            getattr(self, op)(self.mutate, rule)
        except KeyError:
            raise Exception("Unknown mutation operator: " + op)


    ## OPERATIONS

    def ADD_CLASS(self, mutate, rule):
        return rule

    def ADD_ASSOC(self, mutate, rule):
        return rule

    def ADD_BACK_LINK(self, mutate, rule):
        return rule

    def DELETE_ELEMENT(self, mutate, rule):
        op, node_num = self.mutate

        assoc_nodes = []
        for edge in rule.es:
            if edge.source == node_num and rule.vs[edge.target]["mm__"] in self.link_classes + ["match_contains",
                                                                                                "apply_contains"]:
                assoc_nodes.append(edge.target)
            elif edge.target == node_num and rule.vs[edge.source]["mm__"] in self.link_classes + ["match_contains",
                                                                                                  "apply_contains"]:
                assoc_nodes.append(edge.source)

        print("Nodes to delete: " + str(node_num) + " " + str(assoc_nodes))

        rule.delete_nodes([node_num] + assoc_nodes)
        return rule

    def RENAME_CLASS(self, mutate, rule):
        op, node_num, change = self.mutate

        rule.vs[node_num]["mm__"] = change

        return rule

    def RENAME_ASSOC(self, mutate, rule):
        return rule

    def DELETE_ATTRIB(self, mutate, rule):
        return rule

    def DELETE_EQ(self, mutate, rule):
        return rule

    def CHANGE_TERM_NODE(self, mutate, rule):
        return rule

    def CHANGE_TERM_ATTRIB(self, mutate, rule):
        return rule

    def CHANGE_CONCAT(self, mutate, rule):
        return rule

    def CHANGE_ATOM(self, mutate, rule):
        return rule
