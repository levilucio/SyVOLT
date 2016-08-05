
from core.himesis_utils import graph_to_dot
from util.decompose_graph import decompose_graph

from core.himesis_utils import build_traceability
from core.new_match_algo import NewHimesisMatcher

from copy import deepcopy
class Slicer:


    def __init__(self, rules, transformation, superclasses_dict, overlapping_rules):

        self.debug = False

        self.data = {}
        self.direct_links = {}
        self.backward_links = {}
        self.match_elements = {}
        self.isolated_match_elements = {}
        self.apply_elements = {}

        self.found_links = {}
        self.found_isolated_match_elements = {}

        self.rules = rules

        for rule in self.rules:
            self.rules[rule] = build_traceability(deepcopy(self.rules[rule]))


        self.transformation = transformation

        self.superclasses_dict = superclasses_dict

        self.overlapping_rules = overlapping_rules

        for layer in transformation:
            for i, rule in enumerate(layer):

                rule_name = rule.name

                #make sure to update layer with traceability rules
                layer[i] = self.rules[rule_name]

                data = decompose_graph(self.rules[rule_name])
                self.direct_links[rule_name] = data["direct_links"]
                self.backward_links[rule_name] = data["backward_links"]
                self.match_elements[rule_name] = data["match_elements"]
                self.isolated_match_elements[rule_name] = data["isolated_match_elements"]
                self.apply_elements[rule_name] = data["apply_elements"]
                self.data[rule_name] = data

                #if self.debug:
                    #print("Drawing: " + rule.name)
                    #graph_to_dot(rule.name, rule)



        # if self.debug:
        #
        #     print("Supertype hierarchy: ")
        #     supertypes = list(self.rules.values())[0]["superclasses_dict"]
        #     defaults = ['MetaModelElement_S', 'MetaModelElement_T']
        #     for k in sorted(supertypes.keys()):
        #         v = [s for s in supertypes[k] if s not in defaults]
        #         if v:
        #             print(k + " : " + str(v))



        for layer in transformation:
            for rule in layer:

                #if "UnionMother" not in rule.name:
                #    continue

                r_rules = self.find_required_rules(rule.name, [rule])
                r_rules = sorted([r.name for r in r_rules])
                print("Rule " + rule.name + " depends on: " + str(r_rules))

        for layer in transformation:
            for rule in layer:
                self.check_for_missing_elements(rule, is_contract=False)

    def get_contract(self, contract_num, atomic, if_then):

        contract = None
        num = contract_num
        if contract_num >= 0 and contract_num < len(atomic):
            atomic = [atomic[contract_num]]
            if_then = []
            contract = atomic[0]

        num -= len(atomic)
        if contract_num >= 0 and contract_num < len(if_then):
            atomic = []
            if_then = [if_then[contract_num]]
            contract = if_then[0]

        print("Slicing for contract number " + str(contract_num) + " : " + contract[0])

        return contract, atomic, if_then




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

            data = decompose_graph(c, verbosity = 0, isolated_if_attached_backward=True)

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

        print("Number rules before: " + str(len(self.rules)))

        try:
            contract_name, contract_list = self.decompose_contract(contract)
        except KeyError:
            #this is actually a rule
            contract_name = contract.name
            contract_list = [contract]


        if self.debug:

            graph_to_dot(contract_name, contract_list[0])
            for layer in self.transformation:
                for rule in layer:
                    graph_to_dot(rule.name, rule)


        required_rules = self.find_required_rules(contract_name, contract_list, True, verbosity=0)


        rr_names = [rule.name for rule in required_rules]

        print("Required rules for contract " + contract_name + ": " + str(sorted(rr_names)))

        #this contract is a rule, so make sure it requires itself
        if contract_name in self.rules.keys():
            required_rules.append(self.rules[contract_name])

        #raise Exception("Contract Required Rules")

        for rr in required_rules:

            new_rrs = self.find_required_rules(rr.name, [rr], False, self.transformation)
            for new_rr in new_rrs:
                if new_rr not in required_rules:
                    required_rules.append(new_rr)

        rr_names = [rule.name for rule in required_rules]

        #add in the rules which might be needed for subsumption
        rrules_copy = list.copy(rr_names)
        for rr in rrules_copy:
            for key, values in self.overlapping_rules.items():
                if rr == key:
                    for val in values:
                        if val not in rr_names:
                            rr_names += values
                            #print("Adding: " + str(values))
                if rr in values and key not in rr_names:
                    rr_names.append(key)
                    #print("Adding: " + str(key))

        print("Required rules for contract " + contract_name + ":\n" + str(sorted(rr_names)))
        #raise Exception()

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

        for contract in contract_list:
            self.check_for_missing_elements(contract, is_contract = True)

        print("Slicing took: " + str(end_time) + " seconds")
        print("Number rules after: " + str(len(new_rules)))
        #raise Exception()


        #raise Exception()
        return new_rules, new_transformation


    def find_required_rules(self, pattern_name, pattern_list, is_contract = False, verbosity = 0):
        if self.debug:
            print("\nLooking for required rules for pattern: " + pattern_name)

        required_rules = []

        for layer in self.transformation:
            # don't look at the same layer that a rule is on

            if not is_contract:
                rule_names = [r.name for r in layer]

                if pattern_name in rule_names:
                    break

            for rule in layer:
                if rule in required_rules:
                    continue

                if is_contract:
                    rule_me = self.match_elements[rule.name]
                    rule_me = set([rule.vs[n]["mm__"] for n in rule_me])
                else:
                    rule_me = set()

                source_data = self.data[rule.name]
                source_mms = rule.vs["mm__"]

                for pattern in pattern_list:
                    verbosity = 0

                    pattern_data = self.data[pattern.name]
                    pattern_mms = pattern.vs["mm__"]

                    #we care about backward links for both rules and contracts,
                    #but only direct link for contracts

                    if is_contract:
                        real_backward_links = pattern_data["backward_links"]
                    else:
                        real_backward_links = [bl for bl in pattern_data["backward_links"] if pattern_mms[bl[2]] == "backward_link"]
                    real_trace_links = [tl for tl in source_data["backward_links"] if source_mms[tl[2]] == "trace_link"]

                    links = [
                        [real_backward_links, real_trace_links],
                    ]

                    if is_contract:
                        links.append([pattern_data["direct_links"], source_data["direct_links"]])

                        graph_me = self.isolated_match_elements[pattern.name]
                        graph_me = set([pattern.vs[n]["mm__"].replace("MT_pre__", "") for n in graph_me])

                        if len(graph_me.intersection(rule_me)) > 0:
                            required_rules.append(rule)
                            #continue

                    if self.match_links(links, pattern, self.data[pattern.name], rule, self.data[rule.name], self.superclasses_dict,
                                   verbosity = verbosity):
                        required_rules.append(rule)

        return list(set(required_rules))

    def match_links(self, links, pattern, pattern_data, graph, source_data, superclasses_dict, verbosity=0):

        matcher = NewHimesisMatcher(graph, pattern, pred1=source_data, pred2=pattern_data, superclasses_dict=superclasses_dict, skip_equations = True)
        # pattern_mms = pattern.vs["mm__"]
        # source_mms = graph.vs["mm__"]

        does_match = False
        for iso_match_element in pattern_data["isolated_match_elements"]:

            for node in range(len(graph.vs)):
                # print("Matching on: " + str(node))
                nodes_match = matcher.match_nodes(node, iso_match_element)

                if nodes_match:
                    if pattern.name not in self.found_isolated_match_elements.keys():
                        self.found_isolated_match_elements[pattern.name] = []
                    self.found_isolated_match_elements[pattern.name].append(iso_match_element)
                    does_match = True

        # copy these links, as we might need to remove some


        for patt_links, source_links in links:
            if verbosity > 1:
                print("\n===================\nPattern " + pattern.name + " nodes:")
                for patt0_n, patt1_n, patt_link_n in patt_links:
                    matcher.print_link(pattern, patt0_n, patt1_n, patt_link_n)
                print("Pattern " + pattern.name + " nodes:\n===================\n")
                print("\n===================\nGraph " + graph.name + " nodes:")
                for graph_n0_n, graph_n1_n, graph_link_n in source_links:
                    matcher.print_link(graph, graph_n0_n, graph_n1_n, graph_link_n)
                print("Graph " + graph.name + " nodes:\n===================\n")


            for patt0_n, patt1_n, patt_link_n in patt_links:

                for graph_n0_n, graph_n1_n, graph_link_n in source_links:
                    if pattern.vs[patt_link_n]["mm__"] in ["trace_link", "backward_link"]:
                        if graph.vs[graph_link_n]["mm__"] in ["trace_link", "backward_link"]:
                            links_match = True
                        else:
                            links_match = False
                    else:
                        links_match = matcher.match_nodes(graph_link_n, patt_link_n)

                    if not links_match:
                        #if verbosity > 1:
                        #    print("Links don't match")
                        continue

                    if verbosity > 1:
                        print("\nChecking Pattern " + pattern.name + " nodes:")
                        matcher.print_link(pattern, patt0_n, patt1_n, patt_link_n)

                    nodes_match_1 = matcher.match_nodes(graph_n0_n, patt0_n)

                    nodes_match_2 = matcher.match_nodes(graph_n1_n, patt1_n)

                    nodes_match_3 = matcher.match_nodes(graph_n1_n, patt0_n)

                    nodes_match_4 = matcher.match_nodes(graph_n0_n, patt1_n)


                    nodes_match = (nodes_match_1 and nodes_match_2) or (nodes_match_3 and nodes_match_4)

                    #if nodes_match:
                    #    print("\nNodes found!")
                    # if not nodes_match:
                    #     print("Failure matching on " + pc.vs[pc_n0_n]["mm__"] + " vs " + contract.vs[n0_n]["mm__"])

                    # if not nodes_match:
                    #     print("Failure matching on " + pc.vs[pc_n1_n]["mm__"] + " vs " + contract.vs[n1_n]["mm__"])

                    if nodes_match:
                        if verbosity > 1:
                            print("\nFound the pattern link: ")
                            matcher.print_link(pattern, patt0_n, patt1_n, patt_link_n)
                            print("On:")
                            matcher.print_link(graph, graph_n0_n, graph_n1_n, graph_link_n)

                        if pattern.name not in self.found_links.keys():
                            self.found_links[pattern.name] = []
                        self.found_links[pattern.name].append([patt0_n, patt1_n, patt_link_n])

                        does_match = True
                        #return True

                        #pc_direct_links.remove([pc_n0_n, pc_n1_n, pc_link_n])
                        #break
                    # else:
                    #     if verbosity > 1:
                    #         print("\nNot match on:")
                    #         print(graph.vs[graph_n0_n]["mm__"])
                    #         print(graph.vs[graph_n1_n]["mm__"])
                    #
                    #         if graph_link_n:
                    #             print(graph.vs[graph_link_n]["mm__"])
                    #         print()

                # if not found_match:
                #     if verbosity > 1:
                #         print("No direct link matches found")
                #         print("Couldn't find:")
                #         print(pattern.vs[patt0_n]["mm__"])
                #         print(pattern.vs[patt1_n]["mm__"])
                #         if patt_link_n:
                #             print(pattern.vs[patt_link_n]["mm__"])
                #         print()
                #     return False

        return does_match

    def check_for_missing_elements(self, graph, is_contract = False):

        original_mms = graph.vs["mm__"]
        mms = [mm.replace("MT_pre__", "") for mm in original_mms]

        direct_links = self.data[graph.name]["direct_links"]

        backward_links = self.data[graph.name]["backward_links"]

        if not is_contract:
            backward_links = [bl for bl in backward_links if bl[2] == "backward_link"]

        try:
            found_links = self.found_links[graph.name]
        except KeyError:
            found_links = []

        if is_contract:
            for dl in direct_links:
                if dl not in found_links:
                    rwe = self.print_rules_with_element(original_mms[dl[0]], verbose = False)
                    rwe2 = self.print_rules_with_element(original_mms[dl[1]], verbose = False)

                    #check to see if it is in the apply graph
                    if "directLink_T" in mms[dl[2]]:
                        if len(rwe) == 0 or len(rwe2) == 0:
                            print("Elements in direct link are missing")
                            print(mms[dl[0]] + " - " + mms[dl[2]] + " - " + mms[dl[1]])
                    else:
                        print("Error! Direct link missing!")
                        print(mms[dl[0]] + " - " + mms[dl[2]] + " - " + mms[dl[1]])
                    #print(dl)

                    #raise Exception()
                elif found_links.count(dl) < direct_links.count(dl):
                    print("Possible error in multiplicity!")
                    print(mms[dl[0]] + " " + mms[dl[2]] + " " + mms[dl[1]])



        for iso in self.isolated_match_elements[graph.name]:
            if iso not in self.found_isolated_match_elements[graph.name]:
                print("Isolated element " + str(iso) + " cannot be found!")
                print(mms[iso])
                self.print_rules_with_element(original_mms[iso])
                #raise Exception()

        for bl in backward_links:
            if bl not in found_links:
                print("Error! Backward link might be missing!")
                print(bl)
                print(mms[bl[0]] + " " + mms[bl[2]] + " " + mms[bl[1]])
                self.print_rules_with_element(original_mms[bl[0]])
                self.print_rules_with_element(original_mms[bl[1]])
            elif found_links.count(bl) < backward_links.count(bl):
                print("Possible error in multiplicity!")

    def print_rules_with_element(self, element_mm, verbose = True):
        element_mm = element_mm.replace("MT_pre__", "")

        rwe = []
        if verbose: print("\nLooking for mm: " + element_mm)
        for rule_name, rule in sorted(self.rules.items()):
            mms = rule.vs["mm__"]

            for mm in mms:
                if mm == element_mm:
                    if verbose: print("Rule " + rule_name + " contains mm: " + mm)
                    rwe.append(rule_name)
                try:
                    if element_mm in self.superclasses_dict[mm]:
                        if verbose: print("Rule " + rule_name + " contains mm: " + element_mm + " as " + mm)
                        rwe.append(rule_name)
                except KeyError:
                    pass

        rwe = list(set(rwe))
        if len(rwe) == 0:
            print("Error: MM " + str(element_mm) + " not found in any rule!!")

        return rwe
