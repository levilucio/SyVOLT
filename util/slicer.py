
from core.himesis_utils import graph_to_dot
from util.decompose_graph import decompose_graph, match_links

from PyRamify import PyRamify

from core.match_algo import HimesisMatcher
from core.himesis_plus import makePreConditionPattern

from copy import deepcopy
class Slicer():


    def __init__(self, rules, transformation):

        self.debug = False

        self.direct_links = {}
        self.backward_links = {}
        self.match_elements = {}
        self.isolated_match_elements = {}
        self.apply_elements = {}


        self.rules = rules
        self.transformation = transformation


        for layer in transformation:
            for rule in layer:

                rule_name = rule.name
                dls, bls, mes, imes, aes = decompose_graph(self.rules[rule_name], verbosity=0)
                self.direct_links[rule_name] = dls
                self.backward_links[rule_name] = bls
                self.match_elements[rule_name] = mes
                self.isolated_match_elements[rule_name] = imes
                self.apply_elements[rule_name] = aes


                #if self.debug:
                    #print("Drawing: " + rule.name)
                    #graph_to_dot(rule.name, rule)



        if self.debug:

            print("Supertype hierarchy: ")
            supertypes = list(self.rules.values())[0]["superclasses_dict"]
            defaults = ['MetaModelElement_S', 'MetaModelElement_T']
            for k in sorted(supertypes.keys()):
                v = [s for s in supertypes[k] if s not in defaults]
                if v:
                    print(k + " : " + str(v))



        for layer in transformation:
            for rule in layer:

                r_rules = self.find_required_rules(rule)
                r_rules = sorted([r.name for r in r_rules])
                print("Rule " + rule.name + " depends on: " + str(r_rules))




    def find_required_rules(self, graph, is_contract = False, verbosity = 0):


        if self.debug:
            print("\nLooking for required rules for graph: " + graph.name)


        try:
            supertypes = graph["superclasses_dict"]
        except KeyError:
            print("Graph: " + graph.name + " does not have a superclasses dict")
            supertypes = []




        required_rules = []

        for layer in self.transformation:

            #don't look at the same layer that a rule is on
            rule_names = [r.name for r in layer]

            if graph.name in rule_names:
                break

            for rule in layer:

                if rule in required_rules:
                    continue

                # rule_dls = self.direct_links[rule.name]
                #
                # if verbosity > 1:
                #     print("\n" + rule.name)
                #     print("Rule DLs: " + str(rule_dls))
                #     print("Match Elements: " + str(self.match_elements[rule.name]))
                #     print("Apply Elements: " + str(self.apply_elements[rule.name]))

                #HACK: temp removal of equations
                eqs = graph["equations"]
                graph["equations"] = []

                matcher = HimesisMatcher(rule, graph)
                graph["equations"] = eqs

                graph["superclasses_dict"] = rule["superclasses_dict"]

                #matcher = None

                if match_links(matcher, graph, self.direct_links[graph.name], rule, self.direct_links[rule.name], 2):
                    required_rules.append(rule)

                if match_links(matcher, graph, self.backward_links[graph.name], rule, self.backward_links[rule.name], 0):
                    required_rules.append(rule)

                # for dl in dls:
                #
                #     if dl in rule_dls:
                #         required_rules.append(rule)
                #         if self.debug:
                #             print("Add rule (dl): " + rule.name)
                #         break
                #
                #     else:
                #
                #         #check for supertype matching
                #
                #         a, b = dl
                #         for rule_dl in rule_dls:
                #             ra, rb = rule_dl
                #
                #             if a in supertypes and ra in supertypes[a] and \
                #                 b in supertypes and rb in supertypes[b]:
                #                 required_rules.append(rule)
                #
                #                 if self.debug:
                #                     print("Add rule (dl-supertypes): " + rule.name)
                #                 break


                # for backward_link in bls:
                #     a, m = backward_link
                #
                #     if self.debug:
                #         print("M: " + m + " A: " + a)
                #         print("Match Elements: " + str(self.match_elements[rule.name]))
                #         print("Apply Elements: " + str(self.apply_elements[rule.name]))
                #
                #     if m in self.match_elements[rule.name] and \
                #         a in self.apply_elements[rule.name]:
                #         required_rules.append(rule)
                #         found_bls.append(backward_link)
                #         if self.debug:
                #             print("Add rule (bl): " + rule.name)
                #     else:
                #
                #         #check for supertype matching
                #
                #         if a in supertypes and supertypes[a] in self.apply_elements[rule.name] and \
                #             m in supertypes and supertypes[m] in self.match_elements[rule.name]:
                #             required_rules.append(rule)
                #             found_bls.append(backward_link)
                #             if self.debug:
                #                 print("Add rule (bl-supertypes): " + rule.name)
                #
                #
                # isolated_elements = self.isolated_match_elements[graph.name]
                #
                # if isolated_elements:
                #
                #     isolated_added = False
                #     rule_mms = rule.vs["mm__"]
                #     #print("Rule mms: " + str(rule_mms))
                #     #print("Isolated mms: " + str(isolated_elements))
                #
                #     for isolated_mm in isolated_elements:
                #         if isolated_mm in rule_mms:
                #             required_rules.append(rule)
                #             isolated_added = True
                #             break



                # print("WARNING: HAVENT ADDED RULE YET")
                # print("Rule: " + rule.name)

                #rule_bls = self.backward_links[rule.name]

                # print("Rule BLs: " + str(rule_bls))
                #
                # print("Match Elements: " + str(self.match_elements[rule.name]))
                # print("Apply Elements: " + str(self.apply_elements[rule.name]))
                #
                # print("Contract BLs: " + str(bls))

                #print("\nRule " + rule.name + " MMS: " + str(rule_mms))

                # for mm in mms_required:
                #     if mm in rule_mms:
                #         required_rules.append(rule)
                #
                #         #print("Add rule: " + rule.name + " with mms: " + str(rule_mms))
                #         break
        # if len(found_bls) < len(bls):
        #     print("\nERROR: Could not find all backward links for graph: " + graph.name)
        #     print("Missing backward links: " + str(["M: " + m + " -> A: " + a for a,m in bls if (a,m) not in found_bls]))

        return list(set(required_rules))


    def slice_transformation(self, contract):

        contract = contract[1].complete
        contract_name = contract.name

        print("Slicing for: " + contract_name)


        dls, bls, mes, imes, aes = decompose_graph(contract, verbosity=0)
        self.direct_links[contract_name] = dls
        self.backward_links[contract_name] = bls
        self.match_elements[contract_name] = mes
        self.isolated_match_elements[contract_name] = imes
        self.apply_elements[contract_name] = aes


        if self.debug:
            #print("Direct links: " + str(self.direct_links))
            
            graph_to_dot(contract.name, contract)
            for layer in self.transformation:
                for rule in layer:
                    graph_to_dot(rule.name, rule)


        required_rules = self.find_required_rules(contract, True, verbosity=2)


        rr_names = [rule.name for rule in required_rules]

        print("Required rules for contract " + contract_name + ": " + str(sorted(rr_names)))




        #raise Exception("Contract Required Rules")

        for rr in required_rules:

            new_rrs = self.find_required_rules(rr, self.transformation)
            for new_rr in new_rrs:
                if new_rr not in required_rules:
                    required_rules.append(new_rr)

        rr_names = [rule.name for rule in required_rules]
        print("Required rules: " + str(sorted(rr_names)))


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