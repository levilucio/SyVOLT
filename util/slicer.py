
from core.himesis_utils import graph_to_dot
from util.decompose_graph import decompose_graph, match_links

from core.match_algo import HimesisMatcher
from core.himesis_plus import makePreConditionPattern

from copy import deepcopy
class Slicer():


    def __init__(self, rules, transformation, superclasses_dict, overlapping_rules):

        self.debug = False

        self.data = {}
        self.direct_links = {}
        self.backward_links = {}
        self.match_elements = {}
        self.isolated_match_elements = {}
        self.apply_elements = {}


        self.rules = rules
        self.transformation = transformation

        self.superclasses_dict = superclasses_dict

        self.overlapping_rules = overlapping_rules

        for layer in transformation:
            for rule in layer:

                rule_name = rule.name
                data = decompose_graph(self.rules[rule_name], verbosity=0, ignore_apply_dls=True)
                self.direct_links[rule_name] = data["direct_links"]
                self.backward_links[rule_name] = data["backward_links"]
                self.match_elements[rule_name] = data["match_elements"]
                self.isolated_match_elements[rule_name] = data["isolated_match_elements"]
                self.apply_elements[rule_name] = data["apply_elements"]
                self.data[rule_name] = data

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

                #if "UnionMother" not in rule.name:
                #    continue

                r_rules = self.find_required_rules(rule.name, [rule])
                r_rules = sorted([r.name for r in r_rules])
                print("Rule " + rule.name + " depends on: " + str(r_rules))




    def find_required_rules(self, graph_name, graph_list, is_contract = False, verbosity = 0):


        if self.debug:
            print("\nLooking for required rules for graph: " + graph_name)


        # try:
        #     supertypes = graph["superclasses_dict"]
        # except KeyError:
        #     print("Graph: " + graph.name + " does not have a superclasses dict")
        #     supertypes = []




        required_rules = []

        for layer in self.transformation:

            #don't look at the same layer that a rule is on
            rule_names = [r.name for r in layer]

            if graph_name in rule_names:
                break

            for rule in layer:

                if rule in required_rules:
                    continue

                #if not "FatherRule" in rule.name:
                #    continue

                # rule_dls = self.direct_links[rule.name]
                #
                # if verbosity > 1:
                #     print("\n" + rule.name)
                #     print("Rule DLs: " + str(rule_dls))
                #     print("Match Elements: " + str(self.match_elements[rule.name]))
                #     print("Apply Elements: " + str(self.apply_elements[rule.name]))


                for graph in graph_list:

                    if match_links(graph, self.data[graph.name], rule, self.data[rule.name], self.superclasses_dict, verbosity=0):
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


    def decompose_contract(self, contract):

        contract_list = contract[1].get_graph()
        contract_name = contract[1].name

        print("Slicing for: " + contract_name)

        self.direct_links[contract_name] = []
        self.backward_links[contract_name] = []
        self.match_elements[contract_name] = []
        self.isolated_match_elements[contract_name] = []
        self.apply_elements[contract_name] = []

        for c in contract_list:

            data = decompose_graph(c, verbosity = 2)

            self.direct_links[c.name] = data["direct_links"]
            self.backward_links[c.name] = data["backward_links"]
            self.match_elements[c.name] = data["match_elements"]
            self.isolated_match_elements[c.name] = data["isolated_match_elements"]
            self.apply_elements[c.name] = data["apply_elements"]

            self.data[c.name] = data

        return contract_name, contract_list


    def slice_transformation(self, contract):
        import time
        start_time = time.time()
        contract_name, contract_list = self.decompose_contract(contract)

        if self.debug:
            #print("Direct links: " + str(self.direct_links))
            
            graph_to_dot(contract.name, contract)
            for layer in self.transformation:
                for rule in layer:
                    graph_to_dot(rule.name, rule)


        required_rules = self.find_required_rules(contract_name, contract_list, True, verbosity=2)


        rr_names = [rule.name for rule in required_rules]

        print("Required rules for contract " + contract_name + ": " + str(sorted(rr_names)))

        #raise Exception("Contract Required Rules")

        for rr in required_rules:

            new_rrs = self.find_required_rules(rr.name, [rr], self.transformation)
            for new_rr in new_rrs:
                if new_rr not in required_rules:
                    required_rules.append(new_rr)

        rr_names = [rule.name for rule in required_rules]

        #add in the rules which might be needed for subsumption
        rrules_copy = list.copy(rr_names)
        for rr in rrules_copy:
            for key, values in self.overlapping_rules.items():
                if rr == key:
                    rr_names += values
                if rr in values:
                    rr_names.append(key)

        rr_names = list(set(rr_names))

        print("Required rules for contract " + contract_name + ":\n" + str(sorted(rr_names)))


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

        end_time = time.time() - start_time

        print("Slicing took: " + str(end_time) + " seconds")

        return new_rules, new_transformation