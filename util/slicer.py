
from core.himesis_utils import graph_to_dot
from util.decompose_graph import decompose_graph

from core.himesis_utils import build_traceability

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

    def find_required_rules(self, graph_name, graph_list, is_contract = False, verbosity = 0):


        if self.debug:
            print("\nLooking for required rules for graph: " + graph_name)

        required_rules = []

        for layer in self.transformation:

            #don't look at the same layer that a rule is on
            rule_names = [r.name for r in layer]

            if graph_name in rule_names:
                break

            for rule in layer:

                if rule in required_rules:
                    continue

                rule_me = self.match_elements[rule.name]


                rule_me = set([rule.vs[n]["mm__"] for n in rule_me])

                for graph in graph_list:
                    verbosity = 0

                    graph_me = self.isolated_match_elements[graph.name]
                    graph_me = set([graph.vs[n]["mm__"].replace("MT_pre__", "") for n in graph_me])

                    if len(graph_me.intersection(rule_me)) > 0:
                        required_rules.append(rule)
                        continue

                    if match_links(graph, self.data[graph.name], rule, self.data[rule.name], self.superclasses_dict, verbosity=verbosity):
                        required_rules.append(rule)


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

        print("Slicing took: " + str(end_time) + " seconds")
        print("Number rules after: " + str(len(new_rules)))
        #raise Exception()

        return new_rules, new_transformation

def match_links(pattern, pattern_data, graph, source_data, superclasses_dict, verbosity=0, match_all = False):

    # if "HcopersonsSolveRefCountryFamilyParentCommunityMan" in pattern.name and "HCountry2Community" in graph.name:
    #     verbosity = 2
    #
    #     print("Pattern: " + pattern.name + " vs " + graph.name)

    for iso_match_element in pattern_data["isolated_match_elements"]:
        # print("Matching iso element: " + str(iso_match_element))
        for node in range(len(graph.vs)):
            # print("Matching on: " + str(node))
            nodes_match = match_nodes(graph, node, pattern, iso_match_element, superclasses_dict, verbosity)

            if nodes_match:
                return True

    # copy these links, as we might need to remove some
    links = [
        [pattern_data["direct_links"], source_data["direct_links"]],
        [pattern_data["backward_links"], source_data["backward_links"]],
    ]

    for patt_links, source_links in links:
        if verbosity > 1:
            print("\n===================\nPattern " + pattern.name + " nodes:")
            for patt0_n, patt1_n, patt_link_n in patt_links:
                print_link(pattern, patt0_n, patt1_n, patt_link_n)
            print("Pattern " + pattern.name + " nodes:\n===================\n")
            print("\n===================\nGraph " + graph.name + " nodes:")
            for graph_n0_n, graph_n1_n, graph_link_n in source_links:
                print_link(graph, graph_n0_n, graph_n1_n, graph_link_n)
            print("Graph " + graph.name + " nodes:\n===================\n")


        for patt0_n, patt1_n, patt_link_n in patt_links:

            for graph_n0_n, graph_n1_n, graph_link_n in source_links:


                links_match = match_nodes(graph, graph_link_n, pattern, patt_link_n, superclasses_dict)

                if not links_match:
                    #if verbosity > 1:
                    #    print("Links don't match")
                    continue

                if verbosity > 1:
                    print("\nChecking Pattern " + pattern.name + " nodes:")
                    print_link(pattern, patt0_n, patt1_n, patt_link_n)

                nodes_match_1 = match_nodes(graph, graph_n0_n, pattern, patt0_n, superclasses_dict, verbosity = verbosity)

                nodes_match_2 = match_nodes(graph, graph_n1_n, pattern, patt1_n, superclasses_dict, verbosity = verbosity)

                nodes_match_3 = match_nodes(graph, graph_n1_n, pattern, patt0_n, superclasses_dict, verbosity = verbosity)

                nodes_match_4 = match_nodes(graph, graph_n0_n, pattern, patt1_n, superclasses_dict, verbosity = verbosity)


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
                        print_link(pattern, patt0_n, patt1_n, patt_link_n)
                        print("On:")
                        print_link(graph, graph_n0_n, graph_n1_n, graph_link_n)

                    return True

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

    return False


def match_nodes(graph, graph_node, pattern, patt_node, superclasses_dict, verbosity = 0):

    #print("Match nodes: graph_node " + str(graph_node))
    #print("Match nodes: patt_node " + str(patt_node))


    if graph_node is not None:
        sourceMM = graph.vs[graph_node]["mm__"].replace("MT_pre__", "")
    else:
        sourceMM = "backward_link"


    if patt_node is not None:
        targetMM = pattern.vs[patt_node]["mm__"].replace("MT_pre__", "")
    else:
        targetMM = "backward_link"



    if sourceMM != targetMM:
        # HACK: For slicing, we want to reverse these
        # because of subtyping

        # temp = sourceMM
        # sourceMM = targetMM
        # targetMM = temp

        # is this a hack?
        if targetMM == "trace_link" and sourceMM == "backward_link":
            return True
        if targetMM == "backward_link" and sourceMM == "trace_link":
            return True

        #superclasses_dict = pattern["superclasses_dict"]

        #if debug:
        #    print("Superclasses: " + str(superclasses_dict))


        if verbosity > 1:
            print("Pattern MM: " + sourceMM + " vs Target MM: " + targetMM)


        #print("Superclasses: " + str(superclasses_dict))

        if sourceMM not in superclasses_dict or not superclasses_dict[sourceMM] or targetMM not in superclasses_dict[sourceMM]:
            if verbosity > 1:
                print("Not a supertype")
                print(superclasses_dict[sourceMM])
            return False

    # print("Source MM: " + sourceMM)
    # print("Target MM: " + targetMM)

    # graph_attrib = graph.vs[graph_node]["attr1"]
    #
    # try:
    #     pattern_attrib = pattern.vs[patt_node]["attr1"]
    # except KeyError:
    #     pattern_attrib = pattern.vs[patt_node]["MT_pre__attr1"]
    #
    #
    # #return graph.vs[graph_node]["attr1"]
    #
    # if graph_attrib == pattern_attrib:
    #     #print(graph_attrib)
    #     #print(pattern_attrib)
    #     return True
    #
    # if "return True" in pattern_attrib:
    #     return True
    #
    # if graph_attrib in pattern_attrib:
    #     #print(graph_attrib)
    #     #print(pattern_attrib)
    #     return True

    are_feasible = are_semantically_feasible(graph, graph_node, pattern, patt_node)
    if verbosity > 1:
        print("Are feasible: " + str(are_feasible))
    #     print("Source: " + sourceMM + " vs " + "Target: " + targetMM)
    #     print("Graph: " + graph.vs[graph_node]["attr1"])
    #     print("Patt: " + pattern.vs[patt_node]["MT_pre__attr1"])
    #
    return are_feasible


def print_link(graph, n0, n1, nlink):
    if nlink is not None:
        link = graph.vs[nlink]["mm__"].replace("MT_pre__", "")
        try:
            attr_string = str(graph.vs[nlink]["MT_pre__attr1"])
            attr_string = attr_string.replace("\n", "").replace("return True", "").replace("return False", "")
        except KeyError:
            attr_string = str(graph.vs[nlink]["attr1"])

        attr_string = attr_string.replace("#", "").replace("=", "").replace(
            "This code is executed when evaluating if a node shall be matched by this rule. You can access the value of the current node's attribute value by: attr_value. You can access any attribute x of this node by: this['x']. If the constraint relies on attribute values from other nodes, use the LHS/NAC constraint instead. The given constraint must evaluate to a boolean expression.",
            "")

        link += " (" + attr_string + ") "

    else:
        link = "backward_link"
    print(graph.vs[n0]["mm__"].replace("MT_pre__", "") + " - " + link + " - " + graph.vs[n1]["mm__"].replace("MT_pre__", ""))


def are_semantically_feasible(graph, src_node_num, pattern, patt_node_num):
    """
        Determines whether the two nodes are syntactically feasible,
        i.e., it ensures that adding this candidate pair does not make it impossible to find a total mapping.
        @param src_node: The candidate from the source graph.
        @param patt_node: The candidate from the pattern graph.
        @return: True if they are semantically feasible, False otherwise.
    """
    # =======================================================================
    # This feasibility check looks at the data stored in the pair of candidates.
    # It verifies that all attribute constraints are satisfied.
    # =======================================================================

    if not src_node_num or not patt_node_num:
        return True

    src_node = graph.vs[src_node_num]
    patt_node = pattern.vs[patt_node_num]

    # print("\n")
    # print("Src node: " + str(src_node_num))
    # print("Src constant: " + str(self.src_eqs_constant))
    # print("Patt node: " + str(patt_node_num))
    # print("Patt constant: " + str(self.patt_eqs_constant))

    # src_equations = []
    # if src_node_num in self.src_eqs_constant:
    #     src_equations = self.src_eqs_constant[src_node_num]
    #
    # if patt_node_num in self.patt_eqs_constant:
    #     patt_equations = self.patt_eqs_constant[patt_node_num]
    #
    #     # print("Source Eq: " + str(src_equation))
    #     # print("Pattern Eq: " + str(patt_equations))
    #
    #     for patt_eq in patt_equations:
    #         patt_attr = patt_eq[0]
    #         patt_value = patt_eq[1]
    #
    #         found = False
    #         for (src_attr, src_value) in src_equations:
    #             if patt_attr == src_attr:
    #                 if patt_value == src_value:
    #                     found = True
    #                     break
    #                 else:
    #                     # print("Equations do not match")
    #                     return False
    #
    #         if found:
    #             continue
    #
    #         try:
    #             if src_node[patt_attr] != patt_value:
    #                 # print("Couldn't find value, found " + str(src_node[patt_attr]))
    #                 # print("Patt eq: " + str(patt_eq))
    #                 return False
    #         except KeyError:
    #             # print("Couldn't find " + patt_attr + " on node " + src_node["mm__"])
    #             # the attribute does not exist on the node
    #             return False

    # Check for attributes value/constraint
    for attr in patt_node.attribute_names():
        # Attribute constraints are stored as attributes in the pattern node.
        # The attribute must be prefixed by a specific keyword
        if not attr.startswith("MT_pre__"):
            continue
        # If the attribute does not "in theory" exist
        # because igraph actually stores all attribute names in all nodes.
        elif not patt_node[attr]:
            continue

        attr_name = attr[8:]

        # methName = self.G2.get_attr_constraint_name(patt_node.index, attr)
        methName = 'eval_%s%s' % (attr_name, patt_node['MT_label__'])
        #
        # print("Attr name: " + attr_name)
        # print("Meth name: " + methName)
        # print("Patt node label: " + patt_node["MT_label__"])

        checkConstraint = getattr(pattern, methName, None)

        # print("Result: " + str(checkConstraint(src_node[attr_name], src_node)))
        # The following assumes that every attribute constraint is defined on the pattern graph
        # (and not on the pattern node itself)
        # if callable(checkConstraint):
        try:
            # This is equivalent to: if not eval_attrLbl(attr_value, currNode)
            if not checkConstraint(src_node[attr_name], src_node):
                return False
        except Exception as e:
            # TODO: This should be a TransformationLanguageSpecificException
            print("Source graph: " + graph.name)
            print("Pattern graph: " + pattern.name)
            for n in graph.vs:
                try:
                    print("Type: " + n["type"])
                    print("MM: " + n["mm__"])
                except KeyError:
                    pass
            raise Exception("An error has occurred while checking the constraint of the attribute '" + attr_name + "'"
                            + " in node '" + src_node["mm__"] + "' in graph: '" + graph.name + "'", e)
            # assume the method is callable
            # else:
            #    raise Exception('The method %s was not found in the pattern graph' % methName)
    return True