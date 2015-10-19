
from core.himesis_utils import graph_to_dot

from util.rule_preprocessor import RulePreprocessor

class Slicer():


    def __init__(self, rules, transformation):

        self.debug = False



        self.rules = rules
        self.transformation = transformation


        self.rule_preprocessor = RulePreprocessor()

        self.rule_preprocessor.process_rules(self.rules, self.transformation)


    def slice_transformation(self, contract):

        contract = contract[1].complete

        print("Slicing for: " + contract.name)

        self.rule_preprocessor.decompose_graph(contract, verbosity=0)

        if self.debug:
            #print("Direct links: " + str(self.direct_links))
            
            graph_to_dot(contract.name, contract)
            for layer in self.transformation:
                for rule in layer:
                    graph_to_dot(rule.name, rule)


        required_rules = self.rule_preprocessor.find_required_rules(contract, True, verbosity=0)


        rr_names = [rule.name for rule in required_rules]

        if self.debug:
            print("Required rules for contract: " + str(rr_names))

        for rr in required_rules:

            new_rrs = self.rule_preprocessor.find_required_rules(rr, self.transformation)
            for new_rr in new_rrs:
                if new_rr not in required_rules:
                    required_rules.append(new_rr)

        rr_names = [rule.name for rule in required_rules]
        print("Required rules: " + str(sorted(set(rr_names))))


        new_rules = {}
        for k in self.rules.keys():
            if k in rr_names:
                new_rules[k] = self.rules[k]


        new_transformation = []
        for layer in self.transformation:
            new_layer = []
            for rule in layer:
                if rule.name in rr_names:
                    new_layer.append(rule)

            if len(new_layer) > 0:
                new_transformation.append(new_layer)



        return new_rules, new_transformation