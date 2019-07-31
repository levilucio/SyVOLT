import ast

from enum import Enum

from core.himesis_utils import graph_to_dot


class MutationOperators(Enum):

    NONE = "NONE"
    # ADD OPERATIONS
    ADD_CLASS = "ADD_CLASS"
    ADD_ASSOC = "ADD_ASSOC"
    ADD_BACK_LINK = "ADD_BACK_LINK"
    ADD_EQUATION = "ADD_EQUATION"

    # DELETE OPERATIONS
    DELETE_ELEMENT = "DELETE"
    DELETE_EQUATION = "DELETE_EQUATION"

    # MODIFY OPERATIONS
    RENAME_CLASS = "RENAME_CLASS"
    RENAME_ASSOC = "RENAME_ASSOC"
    MODIFY_EQUATION = "MODIFY_EQUATION"

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

        self.debug = False

    def print_rule(self, rule):
        mms = rule.vs["mm__"]
        print("Rule: " + rule.name)
        print([v["mm__"] for v in rule.vs])
        print([str(edge.source) + "-" + str(edge.target) for edge in rule.es])
        print([str(mms[edge.source]) + "-" + str(mms[edge.target]) for edge in rule.es])

    def debug_rule(self, rule, stage):

        if not self.debug:
            return

        if MutationOperators.NONE.name in self.mutate[0]:
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

        # raise Exception()
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

    #null operator for baseline
    def NONE(self, mutate, rule):
        return rule

    def ADD_CLASS(self, mutate, rule):
        op, class_name, is_match, ma_model_index = mutate

        new_node_index = len(list(rule.vs))

        rule.add_node()
        new_node = rule.vs[new_node_index]
        new_node["mm__"] = class_name
        new_node["attr1"] = "+"

        container_node_index = len(list(rule.vs))
        rule.add_node()
        container_node = rule.vs[container_node_index]
        if is_match:
            container_node["mm__"] = "match_contains"
        else:
            container_node["mm__"] = "apply_contains"

        rule.add_edge(ma_model_index, container_node_index)
        rule.add_edge(container_node_index, new_node_index)

        return rule

    def ADD_ASSOC(self, mutate, rule):

        op, assoc_name, src, trgt, is_in_match = mutate

        if is_in_match:
            mm = "directLink_S"
        else:
            mm = "directLink_T"

        new_node_index = len(list(rule.vs))

        rule.add_node()
        new_node = rule.vs[new_node_index]
        new_node["mm__"] = mm
        new_node["attr1"] = assoc_name

        rule.add_edge(src, new_node_index)
        rule.add_edge(new_node_index, trgt)

        return rule

    def ADD_BACK_LINK(self, mutate, rule):

        new_node_index = len(list(rule.vs))

        rule.add_node()
        new_node = rule.vs[new_node_index]
        new_node["mm__"] = "backward_link"

        match_index = mutate[1]
        apply_index = mutate[2]

        rule.add_edge(apply_index, new_node_index)
        rule.add_edge(new_node_index, match_index)
        return rule

    def DELETE_ELEMENT(self, mutate, rule):

        #TODO: Delete elements in equations

        op, node_num = self.mutate

        assoc_nodes = []
        for edge in rule.es:
            if edge.source == node_num and rule.vs[edge.target]["mm__"] in self.link_classes + ["match_contains",
                                                                                                "apply_contains"]:
                assoc_nodes.append(edge.target)
            elif edge.target == node_num and rule.vs[edge.source]["mm__"] in self.link_classes + ["match_contains",
                                                                                                  "apply_contains"]:
                assoc_nodes.append(edge.source)

        rule.delete_nodes([node_num] + assoc_nodes)
        return rule

    def RENAME_CLASS(self, mutate, rule):
        op, node_num, change = self.mutate

        rule.vs[node_num]["mm__"] = change

        return rule

    def RENAME_ASSOC(self, mutate, rule):
        num = mutate[1]
        new_assoc = mutate[2]

        node = rule.vs[num]
        node["attr1"] = new_assoc
        return rule

    def DELETE_EQUATION(self, mutate, rule):
        num = mutate[1]
        del rule["equations"][num]
        return rule

    def MODIFY_EQUATION(self, mutate, rule):
        eq_num = mutate[1]
        new_eq = mutate[2]

        rule["equations"][eq_num] = new_eq
        return rule
