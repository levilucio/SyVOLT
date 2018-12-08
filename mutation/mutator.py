import ast

from enum import Enum
class MutationOperators(Enum):
    RENAME_CLASS = "RENAME"
    DELETE_CLASS = "DELETE"

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

        print("Mutator")
        print(rule_to_mutate)
        print(mutate)

    def mutate_rules(self, rules, transformation):

        print(rules)
        print(transformation)

        for i, layer in enumerate(transformation):
            for j, rule in enumerate(layer):
                if self.rule_to_mutate == rule.name:
                    self.print_rule(rule)
                    self.mutate_rule(rule)
                    self.print_rule(rule)

                    rules[rule.name] = rule

        #raise Exception()
        return rules, transformation

    def mutate_rule(self, rule):
        print("Mutate")
        print(rule.name)
        print(self.mutate)

        op = self.mutate[0]

        if op == MutationOperators.RENAME_CLASS.name:
            op, node_num, change = self.mutate
            print(rule.vs[node_num])
            print(change)

            rule.vs[node_num]["mm__"] = change
        else:
            print("Unknown mutation operator: " + op)

    def print_rule(self, rule):
        for v in rule.vs:
            print(v["mm__"])