
from core.himesis_plus import look_for_attached
from core.himesis_utils import graph_to_dot
from copy import deepcopy

def decompose_graph(graph, verbosity = 0, ignore_apply_dls = False):
    #decompose graph into directLinks, backwardLinks, and isolated elements

    debug = False

    #debug = graph.name == "HUnionMotherRule_rule_combinator_matcher_1"

    if debug:
        print("\nDecomposing graph: " + graph.name)
        graph_to_dot(graph.name, graph)

    direct_links = []
    backward_links = []
    match_elements = []
    isolated_match_elements = []
    apply_elements = []


    dls = []
    bls = []


    vs = graph.vs
    try:
        mms = vs["mm__"]
    except KeyError:
        mms = []

    for i in range(len(vs)):
        v = vs[i]
        mm = mms[i]

        #print("MM: " + mm)
        if "directLink" in mm:
            dls.append(i)
        elif "trace_link" in mm or "backward_link" in mm:
            bls.append(i)
        else:
            if mm in ["MatchModel", "ApplyModel", "paired_with"]:
                continue

            neighbours = look_for_attached(i, graph)
            for n in neighbours[:1]:
                n_mm = mms[n]
                if n_mm == "match_contains":
                    match_elements.append(v)
                    break
                elif n_mm == "apply_contains":
                    apply_elements.append(v)
                    break


    for dl in dls:

        neighbours = look_for_attached(dl, graph)

        n_link = neighbours[0]
        n0_neighbours = look_for_attached(n_link, graph)
        n0_neighbours_mm = [vs[n]["mm__"] for n in n0_neighbours]

        #we don't care about direct links in the apply part
        if ignore_apply_dls and 'apply_contains' in n0_neighbours_mm:
            continue

        n0 = neighbours[0]
        n1 = neighbours[1]
        direct_links.append((n0, n1, dl))

    if debug:
        print("Direct links: ")
        for n0, n1, nlink in direct_links:
            print_link(graph, n0, n1, nlink)

    for bl in bls:

        neighbours = look_for_attached(bl, graph)
        n0 = neighbours[0]
        n1 = neighbours[1]
        backward_links.append((n0, n1, bl))

    if debug:
        print("Backward links: ")
        for n0, n1, nlink in backward_links:
            print_link(graph, n0, n1, nlink)


    #see if there are any match elements which are not in a direct link
    for mm in match_elements:
        #print("Match element: " + mm)
        found = False
        for (n1, n2, n_link) in direct_links:
            mm1 = mms[n1]
            mm2 = mms[n2]
            #print("MM2: " + mm2)
            if mm == mm1 or mm == mm2:
                found = True

        if not found:
            isolated_match_elements.append(mm)


    for me in match_elements:
        me = me.index

        for ae in apply_elements:

            ae = ae.index

            found_link = False
            for a, b, c in backward_links:
                if (a == me and b == ae) or (b == me and a == ae):
                    found_link = True

            if not found_link:
                backward_links.append((me, ae, None))

    # if debug:
    #     print("\nRule name: " + graph.name)
    #     print("Match contains: " + str(match_elements))
    #     print("Isolated match elements: " + str(isolated_match_elements))
    #     print("Apply contains: " + str(apply_elements))

    return direct_links, backward_links, match_elements, isolated_match_elements, apply_elements


def match_links(matcher, pattern, pattern_dls, graph, graph_dls, verbosity=0, match_all = False):


    # print("\n=====================\nMatching links")
    # print("Pattern: " + pattern.name + " Graph: " + graph.name)
    #
    # for patt0_n, patt1_n, patt_link_n in pattern_dls:
    #
    #     print("\nPattern nodes:")
    #     if patt_link_n:
    #         link = pattern.vs[patt_link_n]["mm__"]
    #     else:
    #         link = "backward_link"
    #
    #     print(pattern.vs[patt0_n]["mm__"] + " - " + link + " - " + pattern.vs[patt1_n]["mm__"])
    #
    # for graph_n0_n, graph_n1_n, graph_link_n in graph_dls:
    #
    #
    #     print("\nGraph " + graph.name + " nodes:")
    #     if graph_link_n:
    #         link = graph.vs[graph_link_n]["mm__"]
    #     else:
    #         link = "backward_link"
    #     print(graph.vs[graph_n0_n]["mm__"] + " - " + link + " - " + graph.vs[graph_n1_n]["mm__"])

    # copy these links, as we might need to remove some
    graph_dls = deepcopy(graph_dls)

    for patt0_n, patt1_n, patt_link_n in pattern_dls:

        if verbosity > 1:
            print("\nChecking Pattern " + pattern.name + " nodes:")
            print_link(pattern, patt0_n, patt1_n, patt_link_n)


        found_match = False

        if verbosity > 1:
            print("\n===================\nGraph " + graph.name + " nodes:")
            for graph_n0_n, graph_n1_n, graph_link_n in graph_dls:
                print_link(graph, graph_n0_n, graph_n1_n, graph_link_n)
            print("\n===================\nGraph " + graph.name + " nodes:")

        graph_links = graph_dls
        for graph_n0_n, graph_n1_n, graph_link_n in graph_links:

            if verbosity > 1:
                print("\nChecking Graph " + graph.name + " nodes:")
                print_link(graph, graph_n0_n, graph_n1_n, graph_link_n)


            nodes_match_1 = match_nodes(matcher, graph, graph_n0_n, pattern, patt0_n)

            nodes_match_2 = match_nodes(matcher, graph, graph_n1_n, pattern, patt1_n)

            nodes_match_3 = match_nodes(matcher, graph, graph_n1_n, pattern, patt0_n)

            nodes_match_4 = match_nodes(matcher, graph, graph_n0_n, pattern, patt1_n)


            nodes_match = (nodes_match_1 and nodes_match_2) or (nodes_match_3 and nodes_match_4)

            #if nodes_match:
            #    print("\nNodes found!")
            # if not nodes_match:
            #     print("Failure matching on " + pc.vs[pc_n0_n]["mm__"] + " vs " + contract.vs[n0_n]["mm__"])

            # if not nodes_match:
            #     print("Failure matching on " + pc.vs[pc_n1_n]["mm__"] + " vs " + contract.vs[n1_n]["mm__"])

            if patt_link_n and graph_link_n:
                nodes_match = nodes_match and match_nodes(matcher, graph, graph_link_n, pattern, patt_link_n)


            if nodes_match:
                found_match = True


                if verbosity > 1:
                    print("\nFound the pattern link: ")
                    print_link(pattern, patt0_n, patt1_n, patt_link_n)

                if not match_all:
                    return True

                #need to check the correct number of links
                else:
                    graph_links.remove((graph_n0_n, graph_n1_n, graph_link_n))
                    break



        if not found_match and match_all:

            if verbosity > 1:
                print("Could not find pattern link: ")
                print_link(pattern, patt0_n, patt1_n, patt_link_n)
            return False

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

    #return True if all are found successfully
    #return False if we don't need all, and none were found
    return match_all


def match_nodes(matcher, graph, graph_node, pattern, patt_node, debug = False):

    #print("Match nodes: graph_node " + str(graph_node))
    #print("Match nodes: patt_node " + str(patt_node))
    sourceMM = graph.vs[graph_node]["mm__"].replace("MT_pre__", "")
    targetMM = pattern.vs[patt_node]["mm__"].replace("MT_pre__", "")



    if sourceMM != targetMM:
        # is this a hack?
        if targetMM == "trace_link" and sourceMM == "backward_link":
            return True

        superclasses_dict = pattern["superclasses_dict"]

        #if debug:
        #    print("Superclasses: " + str(superclasses_dict))





        #print("Superclasses: " + str(superclasses_dict))

        if sourceMM not in superclasses_dict or not superclasses_dict[sourceMM] or targetMM not in superclasses_dict[sourceMM]:
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
    #print("Are feasible: " + str(are_feasible))
    return are_feasible

def print_link(graph, n0, n1, nlink):
    if nlink:
        link = graph.vs[nlink]["mm__"].replace("MT_pre__", "")
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