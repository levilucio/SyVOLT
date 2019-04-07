from __future__ import print_function
from util.decompose_graph import decompose_graph

# from core.match_algo import HimesisMatcher
#
# from core.himesis_utils import graph_to_dot

from itertools import product

from collections import defaultdict

from profiler import *

from solver.simple_attribute_equation_evaluator import compare_constant_equations, compare_variable_equations

class NewHimesisMatcher:

    use_old_match_gen = False

    def __init__(self, source_graph, pattern_graph, pred1 = {}, succ1 = {}, pred2 = {}, succ2 = {}, superclasses_dict = {}, skip_equations = False):
        self.debug = False
        self.record_reason_failed = False
        self.failed_iso_elements = []
        self.failed_links = []
        self.failed_link_matches = []

        self.skip_equations = skip_equations

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

        self.pattern_nodes = [node for node in self.pattern_graph.vs]
        self.source_nodes = [node for node in self.source_graph.vs]

        #get the set of pattern attribs from the first node if it exists
        try:
            self.pattern_attribs = [attrib for attrib in self.pattern_nodes[0].attribute_names() if attrib.startswith("MT_pre__")]
        except IndexError:
            self.pattern_attribs = []

        from core.himesis_plus import get_default_match_code
        self.default_match_code = get_default_match_code()

        self.pattern_attribs_by_node = {}

        for i, patt_node in enumerate(self.pattern_nodes):
            self.pattern_attribs_by_node[i] = [attr[8:] for attr in self.pattern_attribs if patt_node[attr] != self.default_match_code and patt_node[attr] is not None]


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

        self.oldMatcher = None

        self.debug_equations = False

        self.is_contract = self.pattern_graph.name.endswith("LHS")

        if len(self.pattern_nodes) > 0 and "MT_label__" in self.pattern_nodes[0].attribute_names():
            self.pattern_labels = [int(l) for l in self.pattern_graph.vs["MT_label__"]]
        else:
            self.pattern_labels = [-1] * len(self.pattern_nodes)

        self.patt_eqs_constant, self.patt_eqs_variable = self.load_equations(pattern_graph)

        if self.patt_eqs_constant or self.patt_eqs_variable:
            self.src_eqs_constant, self.src_eqs_variable = self.load_equations(source_graph)
        else:
            self.src_eqs_constant = defaultdict(list)
            self.src_eqs_variable = defaultdict(list)



    def load_equations(self, graph):

        if self.skip_equations:
            return defaultdict(list), defaultdict(list)

        try:
            eqs = graph["equations"]
        except KeyError:
            print("Graph has no equations array: " + graph.name)
            eqs = []

        eqs_constant = defaultdict(list)
        eqs_variable = defaultdict(list)



        if self.debug_equations:
            print("Looking at equation")
        for eq in eqs:

            if self.debug_equations:
                print(eq)
                print(eq[1])

            if eq is None or eq[0] is None:
                continue

            node_num = eq[0][0]
            attr = eq[0][1]

            if eq[1][0] == "constant":
                if attr == "pivot" or "ApplyAttribute" in attr:
                    continue

                try:
                    eqs_constant[node_num].append((attr, eq[1][1]))
                except KeyError:
                    eqs_constant[node_num] = [(attr, eq[1][1])]
            else:
                try:
                    eqs_variable[node_num].append((attr, eq[1]))
                except KeyError:
                    eqs_variable[node_num] = [(attr, eq[1])]

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
        #                 self.record_reason_failed = True
        #                 self.debug = True
        #                 #graph_to_dot(self.source_graph.name, self.source_graph)
        #                 graph_to_dot("links_" + self.source_graph.name, self.source_graph, force_trace_links = True)

        if self.debug_equations:
            self.print_equations()

        #if len(self.superclasses_dict) == 0:
        #    raise Exception("Error: Superclasses dictionary is empty!")


        for mapping in self._match():
            yield mapping

    def print_equations(self):

        #print("Pattern eqs:")
        #print(self.pattern_graph["equations"])
        print("Pattern eqs (constant)")
        print(dict(self.patt_eqs_constant))
        print("Pattern eqs (variable)")
        print(dict(self.patt_eqs_variable))

        #print("Source eqs:")
        #print(self.source_graph["equations"])
        print("Source eqs (constant)")
        print(dict(self.src_eqs_constant))
        print("Source eqs (variable)")
        print(dict(self.src_eqs_variable))

    def reset_recursion_limit(self):
        pass

    def get_patt_node_constraints(self, patt_node_num):
        patt_label = self.pattern_labels[patt_node_num]

        # HACK: Use patt node num not labels for contracts!
        if self.is_contract:
            lookup = patt_node_num
        else:
            lookup = patt_label

        return self.patt_eqs_constant[lookup], self.patt_eqs_variable[lookup], self.pattern_attribs_by_node[patt_node_num]


    #@profile
    def _match(self):

        link_matches = {}

        patt_mms = self.pattern_mms
        #src_mms = self.source_mms

        #failed_matches = []

        if self.debug:
            print("\nMatching pattern: " + self.pattern_graph.name)
            print("on Source Graph " + self.source_graph.name)

        for iso_match_element in self.pattern_data["isolated_match_elements"]:

            matched_element = False
            #print("Matching iso element: " + str(iso_match_element))

            iso_mm = patt_mms[iso_match_element]

            patt_constraints = self.get_patt_node_constraints(iso_match_element)
            for node in range(len(self.source_graph.vs)):

                #print("Matching on: " + str(node))

                nodes_match = self.match_nodes(node, iso_match_element, iso_mm, patt_constraints)
                if nodes_match:
                    iso_link = (iso_match_element, None, None)
                    node_link = (node, None, None)
                    matched_element = True

                    try:
                        link_matches[iso_link].append(node_link)
                    except KeyError:
                        link_matches[iso_link] = [node_link]

            if not matched_element:
                if self.record_reason_failed:
                    #print("Failed on iso element: " + str(iso_match_element))
                    if iso_match_element not in self.failed_iso_elements:
                        self.failed_iso_elements.append(iso_match_element)
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

                patt_0_mm = patt_mms[patt0_n]
                patt_1_mm = patt_mms[patt1_n]
                patt_link_mm = patt_mms[patt_link_n]

                patt_link_is_not_trace_back = patt_link_mm not in ["trace_link", "backward_link"]

                patt_constraints_0 = self.get_patt_node_constraints(patt0_n)
                patt_constraints_1 = self.get_patt_node_constraints(patt1_n)
                patt_constraints_link = self.get_patt_node_constraints(patt_link_n)

                found_match = False

                if self.debug:
                    print("\n===================Checking Pattern " + self.pattern_graph.name + " nodes:")
                    self.print_link(self, self.pattern_graph, patt0_n, patt1_n, patt_link_n)


                    #print("\nSource Graph nodes")# + self.source_graph.name + " nodes:")
                    # for graph_n0_n, graph_n1_n, graph_link_n in self.source_data["direct_links"]:
                    #     self.print_link(self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)
                    # print("\n===================\n")#End Source Graph " + self.source_graph.name + " nodes:")

                for source_link in source_links:
                    #graph_n0_n, graph_n1_n, graph_link_n = source_link

                    # if self.debug:
                    #     print("\nChecking Graph " + self.source_graph.name + " nodes:")
                    #     self.print_link(self, self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)




                    #trace links and backward links will always match over each other
                    #so don't bother checking them
                    if patt_link_is_not_trace_back:
                        if not self.match_nodes(source_link[2], patt_link_n, patt_link_mm, patt_constraints_link):
                            continue

                    #if nodes_match:
                    if self.match_nodes(source_link[0], patt0_n, patt_0_mm, patt_constraints_0) and self.match_nodes(source_link[1], patt1_n, patt_1_mm, patt_constraints_1):

                        # if self.debug:
                        #     print("Found a link - " + str(graph_n0_n) + " " + str(graph_link_n) + " " + str(graph_n1_n))

                        found_match = True
                        patt_link = (patt0_n, patt1_n, patt_link_n)
                        #source_link = (graph_n0_n, graph_n1_n, graph_link_n)

                        try:
                            link_matches[patt_link].append(source_link)
                        except KeyError:
                            link_matches[patt_link] = [source_link]

                    # if self.debug:
                    #
                    #     if not self.match_nodes(graph_n0_n, patt0_n):
                    #         print("First nodes didn't match")
                    #     if not self.match_nodes(graph_n1_n, patt1_n):
                    #         print("Second nodes didn't match")
                    #
                    #     print("Pattern link:")
                    #     self.print_link(self, self.pattern_graph, patt0_n, patt1_n, patt_link_n)
                    #     print("Source link:")
                    #     self.print_link(self, self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)

                if not found_match and len(self.pattern_data["isolated_match_elements"]) == 0:
                    if self.debug or self.record_reason_failed:
                        #print("Matching failed on:")
                        #self.print_link(self, self.pattern_graph, patt0_n, patt1_n, patt_link_n)
                        if (patt0_n, patt1_n, patt_link_n) not in self.failed_links:
                            self.failed_links.append((patt0_n, patt1_n, patt_link_n))

                        #raise Exception()
                    return



        if len(link_matches) == 0:
            if self.debug:
                print("Found no matches")
                #raise Exception()
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

        num_of_combos = 0

        if self.use_old_match_gen:

            for combo in self.combo_generator(link_matches):
                ms = self.create_match_set(combo)
                if ms:
                    num_of_combos += 1
                    yield ms

        else:
            for i, combo in enumerate(combo_generator3({}, {}, *link_matches_list)):
                num_of_combos = i
                yield combo

        if num_of_combos == 0 and self.record_reason_failed:
            for key, value in link_matches_list:
                #print(str(key) + " : " + str(value))
                number = sum([1 for key2, val2 in link_matches_list if value == val2])
                if len(value) >= number:
                    continue

                # more pattern links want this link than can be satisfied
                self.failed_link_matches.append(key)

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

        if self.debug:
            print("Match set:")
            print(match_set)
        return match_set

    @staticmethod
    def print_link(self, graph, n0, n1, nlink):
        if nlink is not None:
            link = graph.vs[nlink]["mm__"].replace("MT_pre__", "")
            try:
                attr_string = str(graph.vs[nlink]["MT_pre__attr1"])
                attr_string = attr_string.replace("\n", "").replace("return True", "").replace("return False", "")
            except KeyError:
                attr_string = str(graph.vs[nlink]["attr1"])

            attr_string = attr_string.replace("#","").replace("=", "").replace("This code is executed when evaluating if a node shall be matched by this rule. You can access the value of the current node's attribute value by: attr_value. You can access any attribute x of this node by: this['x']. If the constraint relies on attribute values from other nodes, use the LHS/NAC constraint instead. The given constraint must evaluate to a boolean expression.", "")

            if attr_string != "None":
                link += " (" + attr_string + ") "

        else:
            link = "backward_link"
        print(graph.vs[n0]["mm__"].replace("MT_pre__", "") + " - " + link + " - " + graph.vs[n1]["mm__"].replace("MT_pre__", ""))

    def print_failures(self):
        print("Elements of pattern that fail on this target:")
        if len(self.failed_iso_elements) > 0:
            print("Pattern requires elements of type:")
            for iso in self.failed_iso_elements:
                print("\t" + self.pattern_mms[iso])
                self.print_equation(iso)

        if len(self.failed_links) > 0:
            print("Pattern could not find links of type:")
            for link in self.failed_links:
                n0, n1, nlink = link
                print("\t", end = "")
                NewHimesisMatcher.print_link(None, self.pattern_graph, n0, n1, nlink)
                self.print_equation(n0)
                self.print_equation(n1)

            #self.print_rules_with_link(required_rules, self.failed_links)

        if len(self.failed_link_matches) > 0:
            print("Pattern requires multiple links of these types:")
            for link in self.failed_link_matches:
                n0, n1, nlink = link
                print("\t", end = "")
                NewHimesisMatcher.print_link(None, self.pattern_graph, n0, n1, nlink)
                self.print_equation(n0)
                self.print_equation(n1)

        self.print_equations()

            #self.print_rules_with_link(required_rules, self.failed_link_matches)

    def print_rules_with_link(self, required_rules, failed_links):

        for fl in set(failed_links):
            for rr, links in required_rules.items():
                if fl in links:
                    print(rr + " contains link")

    def print_equation(self, patt_node_num):
        patt_label = self.pattern_labels[patt_node_num]
        # HACK: Use patt node num not labels for contracts!
        if self.is_contract:
            lookup = patt_node_num
        else:
            lookup = int(patt_label)

        if self.patt_eqs_constant[lookup]:
            print("Constant equation on " + self.pattern_mms[patt_node_num] + ": " + str(self.patt_eqs_constant[lookup]))

        if self.patt_eqs_variable[lookup]:
            print("Variable equation on " + self.pattern_mms[patt_node_num] + ": " + str(self.patt_eqs_variable[lookup]))

    #==============================================================

    #@profile
    def match_nodes(self, graph_node, patt_node, targetMM, patt_constraints):
        sourceMM = self.source_mms[graph_node]


        # if targetMM == "directLink_T" and sourceMM != "directLink_T":
        #     return False
        #
        # if targetMM == "directLink_S" and sourceMM != "directLink_S":
        #     return False

        #print("Source: " + sourceMM + " vs Target: " + targetMM)

        if sourceMM == targetMM or (sourceMM in self.superclasses_dict and targetMM in self.superclasses_dict[sourceMM]):
            return self.are_semantically_feasible(graph_node, patt_node, patt_constraints)

            # if debug:
            #    print("Superclasses: " + str(superclasses_dict))

            # print("Superclasses: " + str(superclasses_dict))
                # if self.debug:
                #     print("Src: " + sourceMM + " Trgt: " + targetMM + " Node mms don't match")
        return False

    #@profile
    def are_semantically_feasible(self, src_node_num, patt_node_num, patt_constraints):
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

        patt_constant_equations, patt_variable_equations, attr_constraints = patt_constraints

        if patt_constant_equations:
            src_constant_equations = self.src_eqs_constant[src_node_num]
            if not compare_constant_equations(patt_constant_equations, src_constant_equations, self.source_nodes[src_node_num]):
                return False

        if patt_variable_equations:
            src_variable_equations = self.src_eqs_variable[src_node_num]
            if not compare_variable_equations(patt_variable_equations, src_variable_equations):
                return False

        # Check for attributes value/constraint
        for attr_name in attr_constraints:
            # Attribute constraints are stored as attributes in the pattern node.
            # The attribute must be prefixed by a specific keyword
            #if not attr.startswith("MT_pre__"):
            #    continue
            # If the attribute does not "in theory" exist
            # because igraph actually stores all attribute names in all nodes.
            # if not patt_node[attr]:
            #     continue

            # if patt_node[attr] == self.default_match_code or not patt_node[attr]:
            #     continue

            # methName = self.G2.get_attr_constraint_name(patt_node.index, attr)
            methName = 'eval_{}{}'.format(attr_name, self.pattern_labels[patt_node_num])
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
                src_node = self.source_nodes[src_node_num]
                if not checkConstraint(src_node[attr_name], src_node):

                    if self.debug:
                        print("Constraint failed: " + attr_name)
                    #     print(src_node[attr_name])
                    #     print(patt_node["MT_pre__" + attr_name])
                    #     print(methName)
                    return False
            except Exception as e:
                print("Source graph: " + self.source_graph.name)
                print("Pattern graph: " + self.pattern_graph.name)
                raise Exception(
                    "An error has occurred while checking the constraint of the attribute '" + attr_name + "'"
                    + " in node '" + src_node["mm__"] + "' in graph: '" + self.source_graph.name + "'", e)
                # assume the method is callable
                # else:
                #    raise Exception('The method %s was not found in the pattern graph' % methName)
        return True


