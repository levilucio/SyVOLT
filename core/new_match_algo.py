
from util.decompose_graph import decompose_graph, match_nodes

from core.match_algo import HimesisMatcher

from core.himesis_utils import graph_to_dot

from itertools import product
import time

from profiler import *

class NewHimesisMatcher(object):
    def __init__(self, source_graph, pattern_graph, pred1 = {}, succ1 = {}, pred2 = {}, succ2 = {}):
        self.debug = False
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

        try:
            self.source_mms = [mm.replace("MT_pre__", "") for mm in source_graph.vs["mm__"]]
        except KeyError:
            self.source_mms = []

        try:
            self.pattern_mms = [mm.replace("MT_pre__", "") for mm in pattern_graph.vs["mm__"]]
        except KeyError:
            self.pattern_mms = []

        self.pattern_attribs = [[attrib for attrib in node.attribute_names() if attrib.startswith("MT_pre__")] for node in self.pattern_graph.vs]



        self.oldMatcher = None

    def has_match(self, context = {}):
        try:
            self.match_iter(context).next()
            return True
        except StopIteration:
            return False


    def match_iter(self, context = {}):
        # print(self.pattern_graph.name + " vs " + self.source_graph.name)


        # try:
        #     mms = self.source_graph.vs["mm__"]
        # except KeyError:
        #     mms = []
        #
        # try:
        #     attr1 = self.source_graph.vs["attr1"]
        # except KeyError:
        #     attr1 = []

        # if "DaughterMother" in self.pattern_graph.name:# and "mothers" in attr1:
        #
        #
        #     #print("Source: " + self.source_graph.name)
        #     self.debug = True
        #     self.compare_to_old = True
        #     graph_to_dot("z_source_" + self.source_graph.name, self.source_graph)
        #     graph_to_dot("z_pattern_" + self.pattern_graph.name, self.pattern_graph)
        # else:
        #    self.debug = False
        #    self.compare_to_old = False


        if self.compare_to_old:

            #old_time = time.time()
            self.oldMatcher = HimesisMatcher(self.source_graph, self.pattern_graph, self.pred1, self.succ1, self.pred2, self.succ2)
            old_matches = [x for x in self.oldMatcher.match_iter()]
            #old_time = time.time() - old_time

            #new_time = time.time()
            new_matches = [x for x in self._match()]
            #new_time = time.time() - new_time

            #print("Old time: " + str(old_time) + " seconds")
            #print("New time " + str(new_time) + " seconds")

            if self.debug:
                print("Old matches: " + str(old_matches))
                print("New matches: " + str(new_matches))


            #if len(old_matches) != len(new_matches):
            if old_matches != new_matches:
                print("Matchers give different results")
                print(self.source_graph.name + " vs " + self.pattern_graph.name)




        for mapping in self._match():
            yield mapping

    def reset_recursion_limit(self):
        pass


    def _match(self):

        link_matches = {}

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
                return

        links = [
            [self.pattern_data["direct_links"], self.source_data["direct_links"]],
            [self.pattern_data["backward_links"], self.source_data["backward_links"]],
        ]

        for patt_links, source_links in links:
            if self.debug:
                print("Patt Link: " + str(patt_links))
                print("Source Link: " + str(source_links))

            for patt_link in patt_links:
                if self.debug:
                    print("Patt link: " + str(patt_link))
                (patt0_n, patt1_n, patt_link_n) = patt_link

                found_match = False

                if self.debug:
                    print("\n===================Checking Pattern " + self.pattern_graph.name + " nodes:")
                    self.print_link(self.pattern_graph, patt0_n, patt1_n, patt_link_n)


                    print("\nSource Graph " + self.source_graph.name + " nodes:")
                    # for graph_n0_n, graph_n1_n, graph_link_n in self.source_data["direct_links"]:
                    #     self.print_link(self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)
                    # print("\n===================\n")#End Source Graph " + self.source_graph.name + " nodes:")

                for source_link in source_links:
                    graph_n0_n, graph_n1_n, graph_link_n = source_link

                    if self.debug:
                        print("\nChecking Graph " + self.source_graph.name + " nodes:")
                        self.print_link(self.source_graph, graph_n0_n, graph_n1_n, graph_link_n)

                    if patt_link_n is not None and graph_link_n is not None:
                        nodes_match_link = self.match_nodes(graph_link_n, patt_link_n)
                    else:
                        nodes_match_link = False

                    if not nodes_match_link:
                        if self.debug:
                            print("Link doesn't match")
                        continue

                    nodes_match_1 = self.match_nodes(graph_n0_n, patt0_n)

                    nodes_match_2 = self.match_nodes(graph_n1_n, patt1_n)

                    nodes_match_3 = self.match_nodes(graph_n1_n, patt0_n)

                    nodes_match_4 = self.match_nodes(graph_n0_n, patt1_n)




                    nodes_match = ((nodes_match_1 and nodes_match_2) or (nodes_match_3 and nodes_match_4)) and nodes_match_link

                    if self.debug:
                        #print("Nodes match link: " + str(nodes_match_link))
                        print("Links matched: " + str(nodes_match))

                    if nodes_match:

                        found_match = True
                        pattern_link = (patt0_n, patt1_n, patt_link_n)
                        source_link = (graph_n0_n, graph_n1_n, graph_link_n)

                        #original version matched
                        if nodes_match_1 and nodes_match_2:
                            try:
                                link_matches[pattern_link].append(source_link)
                            except KeyError:
                                link_matches[pattern_link] = [source_link]

                        #matched on the reversed versions
                        if nodes_match_3 and nodes_match_4:
                            source_link = (source_link[1], source_link[0], source_link[2])

                            try:
                                link_matches[pattern_link].append(source_link)
                            except KeyError:
                                link_matches[pattern_link] = [source_link]


                if not found_match and len(self.pattern_data["isolated_match_elements"]) == 0:
                    return




        if len(link_matches) == 0:
            yield {}
            return

        if self.debug:
            print("Link matches:")
            for k in link_matches.keys():
                print(str(k) + " : " + str(link_matches[k]))

        combinations = [[(key, value) for (key, value) in zip(link_matches, values)] for values in
                        product(*link_matches.values())]

        for pm in combinations:
            if self.debug:
                print("Potential match:")
                print(pm)
            match_set = self.create_match_set(pm, combinations)

            if self.debug:
                print("Match set:")
                print(match_set)

            if match_set:


                yield match_set


    def create_match_set(self, pm, combinations):
        match_set = {}
        for pair in pm:
            (k, v) = pair

            p0, p1, p_link = k
            s0, s1, s_link = v

            for p, s in [(p0, s0), (p1, s1), (p_link, s_link)]:

                if p is None or s is None:
                    continue

                #p_label = self.pattern_graph.vs[p]["MT_label__"]

                #try:
                #    s_label = self.source_graph.vs[s]["MT_label__"]
                #except KeyError:

                if self.debug:
                    print("Setting " + str(p) + " to " + str(s))
                if p in match_set.keys() and match_set[p] != s:
                    if self.debug:
                        print("Already binding")
                        print(str(p) + " : " + str(match_set[p]))
                    if len(combinations) > 1:

                        #there is already a binding, so ignore this matching possibility
                        return {}
                    else:
                        #this matching would fail unless we allow this
                        #so this is where disambiguation is needed
                        pass
                        #
                        # print("Already a binding")
                        # print(pm)
                        # graph_to_dot("source", self.source_graph)
                        # graph_to_dot("pattern", self.pattern_graph)

                        # import sys
                        # sys.exit()

                match_set[p] = s

        if self.debug:
            print("Match set:")
            print(pm)
            print(match_set)
        return match_set

    def print_link(self, graph, n0, n1, nlink):
        if nlink is not None:
            link = graph.vs[nlink]["mm__"].replace("MT_pre__", "")
            try:
                link += " (" + str(graph.vs[nlink]["MT_pre__attr1"]) + ") "
                link = link.replace("\n", "").replace("return True", "").replace("return False", "")
            except KeyError:
                link += " (" + str(graph.vs[nlink]["attr1"]) + ") "
        else:
            link = "backward_link"
        print(graph.vs[n0]["mm__"].replace("MT_pre__", "") + " - " + link + " - " + graph.vs[n1]["mm__"].replace("MT_pre__", ""))



    #==============================================================

    #@Profiler2
    def match_nodes(self, graph_node, patt_node):
        # print("Match nodes: graph_node " + str(graph_node))
        # print("Match nodes: patt_node " + str(patt_node))
        sourceMM = self.source_mms[graph_node]
        targetMM = self.pattern_mms[patt_node]

        if sourceMM != targetMM:
            # if self.debug:
            #     print("Source: " + sourceMM)
            #     print("Target: " + targetMM)


            # is this a hack?
            if targetMM == "trace_link" and sourceMM == "backward_link":
                return True

            superclasses_dict = self.pattern_graph["superclasses_dict"]

            # if debug:
            #    print("Superclasses: " + str(superclasses_dict))





            # print("Superclasses: " + str(superclasses_dict))

            if sourceMM not in superclasses_dict or not superclasses_dict[sourceMM] or targetMM not in \
                    superclasses_dict[sourceMM]:
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

        are_feasible = self.are_semantically_feasible(graph_node, patt_node)
        if self.debug:
            print("Are feasible: " + str(are_feasible))
        return are_feasible

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

        src_node = self.source_graph.vs[src_node_num]
        patt_node = self.pattern_graph.vs[patt_node_num]

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
        for attr in self.pattern_attribs[patt_node_num]:
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
            methName = 'eval_%s%s' % (attr_name, patt_node['MT_label__'])
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
                        print(src_node[attr_name])
                        print(patt_node["MT_pre__" + attr_name])
                        print(methName)
                    return False
            except Exception as e:
                # TODO: This should be a TransformationLanguageSpecificException
                print("Source graph: " + self.source_graph.name)
                print("Pattern graph: " + self.pattern_graph.name)
                for n in graph.vs:
                    try:
                        print("Type: " + n["type"])
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