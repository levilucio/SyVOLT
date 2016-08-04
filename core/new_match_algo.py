
from util.decompose_graph import decompose_graph

from core.match_algo import HimesisMatcher

from core.himesis_utils import graph_to_dot

from itertools import product
import time

from profiler import *

class NewHimesisMatcher(object):


    def __init__(self, source_graph, pattern_graph, pred1 = {}, succ1 = {}, pred2 = {}, succ2 = {}, superclasses_dict = {}):
        self.debug = False
        self.print_reason_failed = False

        self.compare_to_old = False

        source_data = pred1
        patt_data = pred2

        self.pred1 = pred1
        self.pred2 = pred2

        if source_data:
            self.source_data = source_data
        else:
            self.source_data = decompose_graph(source_graph)


        if patt_data:
            self.pattern_data = patt_data
        else:
            self.pattern_data = decompose_graph(pattern_graph)

        self.succ1 = succ1
        self.succ2 = succ2

        self.source_graph = source_graph
        self.pattern_graph = pattern_graph

        self.superclasses_dict = superclasses_dict

        #not removing MT_pre__ anymore. This may cause problems
        try:
            self.source_mms = source_graph.vs["mm__"]#[mm.replace("MT_pre__", "") for mm in source_graph.vs["mm__"]]
        except KeyError:
            self.source_mms = []

        try:
            self.pattern_mms = [mm.replace("MT_pre__", "") for mm in pattern_graph.vs["mm__"]]
        except KeyError:
            self.pattern_mms = []

        #get the set of pattern attribs from the first node if it exists
        try:
            self.pattern_attribs = [attrib for attrib in self.pattern_graph.vs[0].attribute_names() if attrib.startswith("MT_pre__")]
        except IndexError:
            self.pattern_attribs = []

        # if "MM5_then_Complete" in self.pattern_graph.name and \
        #                 "HEmptyPathCondition_HState2ProcDef-0_HBasicState2ProcDef-P0_HTransition2Inst-0_HTransitionHListenBranch" in self.source_graph.name:  # "HPP3_CompleteLHS" in self.pattern_graph.name:# and \
        #
        #     #
        #     # "component" in attr1 and "componentPrototype" in attr1:# and "mother" in attr1 and "daughter" in attr1:
        #     print(self.pattern_graph.name)
        #
        #     # print("Source: " + self.source_graph.name)
        #     self.debug = True
        #     self.show_eqs = True
        #     self.compare_to_old = False
        #     graph_to_dot("z_source_" + self.source_graph.name, self.source_graph)
        #     graph_to_dot("z_pattern_" + self.pattern_graph.name, self.pattern_graph)
        #
        # else:
        #     self.debug = False
        #     self.show_eqs = False
        #     self.compare_to_old = False

        self.debug_equations = False

        self.patt_eqs_constant, self.patt_eqs_variable = self.load_equations(pattern_graph)
        self.src_eqs_constant, self.src_eqs_variable = self.load_equations(source_graph)

        self.oldMatcher = None

        self.pattern_nodes = [node for node in self.pattern_graph.vs]
        self.source_nodes = [node for node in self.source_graph.vs]

    def load_equations(self, graph):
        try:
            eqs = graph["equations"]
        except KeyError:
            print("Graph has no equations array: " + graph.name)
            eqs = []

        eqs_constant = {}
        eqs_variable = []



        if self.debug_equations:
            print("Looking at equation")
        for eq in eqs:

            if self.debug_equations:
                print(eq)
                print(eq[1])

            if eq[1][0] == "constant":
                node_num = eq[0][0]
                attr = eq[0][1]

                if attr == "pivot" or "ApplyAttribute" in attr:
                    continue

                try:
                    eqs_constant[node_num].append((attr, eq[1][1]))
                except KeyError:
                    eqs_constant[node_num] = [(attr, eq[1][1])]
            else:
                eqs_variable.append(eq)

        return eqs_constant, eqs_variable


    def has_match(self, context = {}):
        try:
            self.match_iter(context).next()
            return True
        except StopIteration:
            return False


    def match_iter(self, context = {}):
        #print(self.pattern_graph.name + " vs " + self.source_graph.name)


        # try:
        #     mms = self.source_graph.vs["mm__"]
        # except KeyError:
        #     mms = []
        #
        # try:
        #     attr1 = self.source_graph.vs["attr1"]
        # except KeyError:
        #     attr1 = []

        #print(self.pattern_graph.name + " vs " + self.source_graph.name)

        # required_mms = ["ComponentInstance", "ProvidedPort", "RequiredPort",
        #                 "StatementList", "Member", "GlobalVariableDeclaration"]
        # if "Hlayer5rule1_rule_trace_checker" in self.pattern_graph.name:
        #     #if self.source_graph.name == "Em_0R0-_0R2-_0R3-_0R6-_0R1-OVER1_0R7-OVER1_1R0-T_1R1-P_1R2-T_2R2-P_2R3-P_2R5-P_2R1-OVER0_3R0-T_3R1-OVER0.168":
        #     if "2R3" in self.source_graph.name and "2R4" in self.source_graph.name:
        #         if not self.source_graph.name == "4R0":
        #
        #             has_required = True
        #
        #             # for k, v in sorted(self.superclasses_dict.items()):
        #             #
        #             #     print(k)
        #             #     print(v)
        #
        #             for r in required_mms:
        #                 if r not in mms:
        #                     has_required = False
        #
        #             if has_required and mms.count("ComponentInstance") < 2:
        #                 has_required = False
        #
        #             if has_required:
        #                 self.print_reason_failed = True
        #                 self.debug = True
        #                 #graph_to_dot(self.source_graph.name, self.source_graph)
        #                 graph_to_dot("links_" + self.source_graph.name, self.source_graph, force_trace_links = True)





        if self.debug_equations:
            print("Pattern eqs:")
            print(self.pattern_graph["equations"])
            print("Pattern eqs (constant)")
            print(self.patt_eqs_constant)
            print("Pattern eqs (variable)")
            print(self.patt_eqs_variable)

            print("Source eqs:")
            print(self.source_graph["equations"])
            print("Source eqs (constant)")
            print(self.src_eqs_constant)
            print("Source eqs (variable)")
            print(self.src_eqs_variable)


        for mapping in self._match():
            yield mapping

    def reset_recursion_limit(self):
        pass

    #@profile
    def _match(self):

        link_matches = {}

        #failed_matches = []

        if self.debug:
            print("\nMatching pattern: " + self.pattern_graph.name)
            print("on Source Graph " + self.source_graph.name)

        for iso_match_element in self.pattern_data["isolated_match_elements"]:

            matched_element = False
            #print("Matching iso element: " + str(iso_match_element))
            for node in range(len(self.source_graph.vs)):

                #print("Matching on: " + str(node))

                nodes_match = self.match_nodes(node, iso_match_element)
                if nodes_match:
                    iso_link = (iso_match_element, None, None)
                    node_link = (node, None, None)
                    matched_element = True

                    try:
                        link_matches[iso_link].append(node_link)
                    except KeyError:
                        link_matches[iso_link] = [node_link]

            if not matched_element:
                if self.print_reason_failed:
                    print("Failed on iso element: " + str(iso_match_element))
                    #failed_matches.append(iso_match_element)
                return

        links = [
            [self.pattern_data["backward_links"], self.source_data["backward_links"]],
            [self.pattern_data["direct_links"], self.source_data["direct_links"]],
        ]

        for patt_links, source_links in links:
            # if self.debug:
            #     print("Patt Link: " + str(patt_links))
            #     print("Source Link: " + str(source_links))

            for patt_link in patt_links:
                # if self.debug:
                #     print("Patt link: " + str(patt_link))
                (patt0_n, patt1_n, patt_link_n) = patt_link

                found_match = False

                if self.debug:
                    print("\n===================Checking Pattern " + self.pattern_graph.name + " nodes:")
                    self.print_link(self.pattern_graph, patt0_n, patt1_n, patt_link_n)


                    print("\nSource Graph nodes")# + self.source_graph.name + " nodes:")
                    # for graph_n0_n, graph_n1_n, graph_link_n in self.source_data["direct_links"]:
                    #     self.print_link(self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)
                    # print("\n===================\n")#End Source Graph " + self.source_graph.name + " nodes:")

                for graph_n0_n, graph_n1_n, graph_link_n in source_links:

                    # if self.debug:
                    #     print("\nChecking Graph " + self.source_graph.name + " nodes:")
                    #     self.print_link(self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)

                    if patt_link_n is not None and graph_link_n is not None:
                        nodes_match_link = self.match_nodes(graph_link_n, patt_link_n)
                    else:
                        nodes_match_link = False

                    if not nodes_match_link:
                        # if self.debug:
                        #     print("Link doesn't match")
                        continue


                    #if nodes_match:
                    if self.match_nodes(graph_n0_n, patt0_n) and self.match_nodes(graph_n1_n, patt1_n):

                        if self.debug:
                            print("Found a link - " + str(graph_n0_n) + " " + str(graph_link_n) + " " + str(graph_n1_n))

                        found_match = True
                        patt_link = (patt0_n, patt1_n, patt_link_n)
                        source_link = (graph_n0_n, graph_n1_n, graph_link_n)

                        try:
                            link_matches[patt_link].append(source_link)
                        except KeyError:
                            link_matches[patt_link] = [source_link]

                if not found_match and len(self.pattern_data["isolated_match_elements"]) == 0:
                    if self.debug or self.print_reason_failed:
                        print("Matching failed on:")
                        self.print_link(self.pattern_graph, patt0_n, patt1_n, patt_link_n)

                        raise Exception()
                    return



        if len(link_matches) == 0:
            if self.debug:
                print("Found no matches")
                raise Exception()
            yield {}
            return



        #HACK:
        #for family transformation, directLinks are being doubled between families and members
        #remove these
        #Alg: remove duplicate matches where the first two nodes match

        #i = 0
        for k in link_matches.keys():
            new_v = []

            v = link_matches[k]

            for original_v in v:

                count = 0
                for check_v in v:

                    if original_v[0] == check_v[0] and original_v[1] == check_v[1]:
                        count += 1
                if count == 1 or len(new_v) == 0:
                    new_v.append(original_v)



        def combo_generator3(match_set, reverse_match_set, *link_matches):


            if len(link_matches) == 0:
                yield {}
            else:
                #print(len(link_matches))
                tail = link_matches[1:]
                #print(len(tail))

                key, values = link_matches[0]


                for v in values:

                    match_set_copy = match_set.copy()
                    reverse_match_set_copy = reverse_match_set.copy()

                    skip = False
                    for i in range(3):
                        if key[i] is None:
                            continue

                        try:
                            if reverse_match_set[v[i]] != key[i]:
                                #print("Target matching to different pattern")
                                skip = True
                                break
                        except KeyError:
                            pass

                        match_set_copy[key[i]] = v[i]
                        reverse_match_set_copy[v[i]] = key[i]

                    if skip:
                        continue

                    for rest in combo_generator3(match_set_copy, reverse_match_set_copy, *tail):

                        match_set_copy_copy = match_set_copy.copy()
                        match_set_copy_copy.update(rest)
                        yield match_set_copy_copy


        link_matches_list = [kv for kv in link_matches.items()]

        link_matches_list.sort(key = lambda tup: (len(tup[1]), str(tup[1])))


        for i, combo in enumerate(combo_generator3({}, {}, *link_matches_list)):
            #print(i)
            #print(combo)
            #print("New time: " + str(time.time() - start_time))
            yield combo

    def combo_generator(self, link_matches):
        for values in product(*link_matches.values()):
            #if len(set(values)) == len(values):
            yield zip(link_matches, values)


    def create_match_set(self, pm):
        match_set = {}
        reverse_match_set = {}

        for ps, ss in pm:
            for p, s in zip(ps, ss):
                if p is None or s is None:
                    continue

                try:
                    if reverse_match_set[s] != p:
                        # we already have another element binding to this one, so fail
                        if self.debug:
                            print("Another pattern element is already binding to this source element")
                            print("Source: " + str(s))
                            print("Pattern: " + str(p))
                            raise Exception()
                        return {}
                except KeyError:
                    pass

                match_set[p] = s
                reverse_match_set[s] = p

        #if self.debug:
        print("Match set:")
        print(match_set)
        return match_set

    def print_link(self, graph, n0, n1, nlink):
        if nlink is not None:
            link = graph.vs[nlink]["mm__"].replace("MT_pre__", "")
            try:
                attr_string = str(graph.vs[nlink]["MT_pre__attr1"])
                attr_string = attr_string.replace("\n", "").replace("return True", "").replace("return False", "")
            except KeyError:
                attr_string = str(graph.vs[nlink]["attr1"])

            attr_string = attr_string.replace("#","").replace("=", "").replace("This code is executed when evaluating if a node shall be matched by this rule. You can access the value of the current node's attribute value by: attr_value. You can access any attribute x of this node by: this['x']. If the constraint relies on attribute values from other nodes, use the LHS/NAC constraint instead. The given constraint must evaluate to a boolean expression.", "")

            link += " (" + attr_string + ") "

        else:
            link = "backward_link"
        print(graph.vs[n0]["mm__"].replace("MT_pre__", "") + " - " + link + " - " + graph.vs[n1]["mm__"].replace("MT_pre__", ""))



    #==============================================================

    #@profile
    def match_nodes(self, graph_node, patt_node):

        targetMM = self.pattern_mms[patt_node]

        if graph_node is not None:
            sourceMM = self.source_mms[graph_node]
        else:
            sourceMM = "backward_link"

        # if self.debug:

        if targetMM in ["trace_link", "backward_link"]:
            if sourceMM in ["trace_link", "backward_link"]:
                return True
            else:
                return False

        # if targetMM == "directLink_T" and sourceMM != "directLink_T":
        #     return False
        #
        # if targetMM == "directLink_S" and sourceMM != "directLink_S":
        #     return False

        #print("Source: " + sourceMM + " vs Target: " + targetMM)

        if sourceMM != targetMM:

            # if debug:
            #    print("Superclasses: " + str(superclasses_dict))

            # print("Superclasses: " + str(superclasses_dict))

            if sourceMM not in self.superclasses_dict or not self.superclasses_dict[sourceMM] or targetMM not in \
                    self.superclasses_dict[sourceMM]:

                # if self.debug:
                #     print("Src: " + sourceMM + " Trgt: " + targetMM + " Node mms don't match")
                return False

        are_feasible = self.are_semantically_feasible(graph_node, patt_node)
        # if self.debug:
        #     print("Src: " + sourceMM + " Trgt: " + targetMM + " Are feasible: " + str(are_feasible))
        return are_feasible

    #@profile
    def are_semantically_feasible(self, src_node_num, patt_node_num):
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

        src_node = self.source_nodes[src_node_num]
        patt_node = self.pattern_nodes[patt_node_num]


        # if self.debug_equations:
        #     print("\n")
        #     print("Src node: " + str(src_node_num))
        #     print("Src constant: " + str(self.src_eqs_constant))
        #     print("Patt node: " + str(patt_node_num))
        #     print("Patt constant: " + str(self.patt_eqs_constant))

        try:
            patt_label = patt_node["MT_label__"]
        except KeyError:
            patt_label = -1

        #HACK: Use patt node num not labels for contracts!

        if self.pattern_graph.name.endswith("LHS"):
            lookup = patt_node_num
        else:
            lookup = int(patt_label)

        try:
            patt_equations = self.patt_eqs_constant[lookup]
        except KeyError:
            patt_equations = []

        if patt_equations:
            try:
                src_equations = self.src_eqs_constant[src_node_num]
            except KeyError:
                src_equations = []
                
            for patt_eq in patt_equations:
                patt_attr = patt_eq[0]

                #skip matching pivots
                if patt_attr == "pivot" or "ApplyAttribute" in patt_attr:
                    continue

                patt_value = patt_eq[1]

                found = False
                for (src_attr, src_value) in src_equations:
                    if patt_attr == src_attr:
                        if patt_value == src_value:
                            found = True
                            break
                        else:
                            if self.debug:
                                print("Equations do not match")
                            return False

                if found:
                    continue

                try:
                    if src_node[patt_attr] != patt_value:
                        if self.debug:
                            print("Couldn't find value, found " + str(src_node[patt_attr]))
                            print("Patt eq: " + str(patt_eq))
                        return False
                except KeyError:
                    if self.debug:
                        print("Couldn't find " + patt_attr + " on node " + src_node["mm__"])
                    return False


        # Check for attributes value/constraint
        for attr in self.pattern_attribs:
            # Attribute constraints are stored as attributes in the pattern node.
            # The attribute must be prefixed by a specific keyword
            #if not attr.startswith("MT_pre__"):
            #    continue
            # If the attribute does not "in theory" exist
            # because igraph actually stores all attribute names in all nodes.
            if not patt_node[attr]:
                continue

            attr_name = attr[8:]

            # methName = self.G2.get_attr_constraint_name(patt_node.index, attr)
            methName = 'eval_%s%s' % (attr_name, patt_label)
            #
            # print("Attr name: " + attr_name)
            # print("Meth name: " + methName)
            # print("Patt node label: " + patt_node["MT_label__"])

            checkConstraint = getattr(self.pattern_graph, methName, None)

            # print("Result: " + str(checkConstraint(src_node[attr_name], src_node)))
            # The following assumes that every attribute constraint is defined on the pattern graph
            # (and not on the pattern node itself)
            # if callable(checkConstraint):
            try:
                # This is equivalent to: if not eval_attrLbl(attr_value, currNode)
                if not checkConstraint(src_node[attr_name], src_node):

                    if self.debug:
                        print("Constraint failed: " + attr_name)
                    #     print(src_node[attr_name])
                    #     print(patt_node["MT_pre__" + attr_name])
                    #     print(methName)
                    return False
            except Exception as e:
                # TODO: This should be a TransformationLanguageSpecificException
                print("Source graph: " + self.source_graph.name)
                print("Pattern graph: " + self.pattern_graph.name)
                for n in self.source_nodes:
                    try:
                        print("Type: " + str(n["type"]))
                        print("MM: " + n["mm__"])
                    except KeyError:
                        pass
                raise Exception(
                    "An error has occurred while checking the constraint of the attribute '" + attr_name + "'"
                    + " in node '" + src_node["mm__"] + "' in graph: '" + self.source_graph.name + "'", e)
                # assume the method is callable
                # else:
                #    raise Exception('The method %s was not found in the pattern graph' % methName)
        return True