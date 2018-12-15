import ast

from enum import Enum

from himesis_utils import graph_to_dot


class MutationOperators(Enum):
    RENAME_CLASS = "RENAME"
    DELETE_ELEMENT = "DELETE"

    #CLASSES:
    #Replace class with another class
    #Add/remove classes
    #Change Any/Exists type of classes
    #Change positive/negative type of classes

    #ASSOCIATIONS:
    #Remove/add associations
    #Change class of associations
    #Change positive/negative associations
    #Change direct/indirect associations

    #BACKWARD LINKS
    #Add/remove backward links
    #Change negative/positive

    #ATTRIBUTES
    #Add/remove attributes
    #Change match attrib
    #Change Atom value (what values?)
    #Change apply attrib
    #Change target of attribRef
    #Concat, prefer one or the other side

class Mutator:

    def __init__(self, rule_to_mutate, mutate):
        self.rule_to_mutate = rule_to_mutate
        self.mutate = ast.literal_eval(mutate)

        self.structural_classes = ["MatchModel", "ApplyModel", "paired_with",
                                   "match_contains", "apply_contains"
                                   ]
        self.link_classes = ["directLink_S", "directLink_T", "backward_link"]

    def mutate_rules(self, rules, transformation):

        for i, layer in enumerate(transformation):
            for j, rule in enumerate(layer):
                if self.rule_to_mutate == rule.name:
                    # self.print_rule(rule)
                    self.mutate_rule(rule)
                    # self.print_rule(rule)

                    rules[rule.name] = rule

        #raise Exception()
        return rules, transformation

    def mutate_rule(self, rule):

        print("Mutating " + rule.name + " with " + str(self.mutate))

        op = self.mutate[0]

        if op == MutationOperators.RENAME_CLASS.name:
            op, node_num, change = self.mutate

            rule.vs[node_num]["mm__"] = change

        elif op == MutationOperators.DELETE_ELEMENT.name:
            op, node_num = self.mutate

            assoc_nodes = []
            for edge in rule.es:
                if edge.source == node_num and rule.vs[edge.target]["mm__"] in self.link_classes:
                    assoc_nodes.append(edge.target)
                elif edge.target == node_num and rule.vs[edge.source]["mm__"] in self.link_classes:
                    assoc_nodes.append(edge.source)

            rule.delete_nodes([node_num] + assoc_nodes)

        else:
            raise Exception("Unknown mutation operator: " + op)

    def print_rule(self, rule):
        for v in rule.vs:
            print(v["mm__"])