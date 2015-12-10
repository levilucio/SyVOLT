
from util.decompose_graph import decompose_graph, match_nodes

from core.match_algo import HimesisMatcher

from core.himesis_utils import graph_to_dot

from itertools import product

class NewHimesisMatcher(object):
    def __init__(self, source_graph, pattern_graph, pred1 = {}, succ1 = {}, pred2 = {}, succ2 = {}):
        self.debug = False
        self.source_graph = source_graph
        self.pattern_graph = pattern_graph

        self.source_data = {}
        self.source_data["direct_links"], self.source_data["backward_links"], \
        self.source_data["match_elements"], self.source_data["isolated_match_elements"], \
        self.source_data["apply_elements"] = decompose_graph(source_graph)

        self.pattern_data = {}
        self.pattern_data["direct_links"], self.pattern_data["backward_links"], \
        self.pattern_data["match_elements"], self.pattern_data["isolated_match_elements"], \
        self.pattern_data["apply_elements"] = decompose_graph(pattern_graph)

        self.oldMatcher = HimesisMatcher(source_graph, pattern_graph, pred1, succ1, pred2, succ2)

    def has_match(self, context = {}):
        try:
            self.match_iter(context).next()
            return True
        except StopIteration:
            return False

    def match_iter(self, context = {}):

        old_matches = [x for x in self.oldMatcher.match_iter()]
        new_matches = [x for x in self._match()]

        if self.debug:
            print("Old matches: " + str(old_matches))
            print("New matches: " + str(new_matches))

        #if len(old_matches) != len(new_matches):
        if old_matches != [{}] and old_matches != new_matches:
            print("Matchers give different results")
            print(self.source_graph.name + " vs " + self.pattern_graph.name)

            graph_to_dot("source", self.source_graph)
            graph_to_dot("pattern", self.pattern_graph)

            import sys
            sys.exit()

        for mapping in self._match():
            yield mapping

    def reset_recursion_limit(self):
        pass


    def _match(self):

        link_matches = {}

        if self.debug:
            print("\nMatching pattern: " + self.pattern_graph.name)
            print("on Source Graph " + self.source_graph.name)

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

                    nodes_match_1 = match_nodes(None, self.source_graph, graph_n0_n, self.pattern_graph, patt0_n)

                    nodes_match_2 = match_nodes(None, self.source_graph, graph_n1_n, self.pattern_graph, patt1_n)

                    nodes_match_3 = match_nodes(None, self.source_graph, graph_n1_n, self.pattern_graph, patt0_n)

                    nodes_match_4 = match_nodes(None, self.source_graph, graph_n0_n, self.pattern_graph, patt1_n)

                    nodes_match_link = True

                    if patt_link_n and graph_link_n:
                        nodes_match_link = match_nodes(None, self.source_graph, graph_link_n, self.pattern_graph, patt_link_n)
                    else:
                        nodes_match_link = False

                    nodes_match = ((nodes_match_1 and nodes_match_2) or (nodes_match_3 and nodes_match_4)) and nodes_match_link

                    if self.debug:
                        #print("Nodes match link: " + str(nodes_match_link))
                        print("Links matched: " + str(nodes_match))

                    if nodes_match:

                        found_match = True
                        pattern_link = (patt0_n, patt1_n, patt_link_n)
                        source_link = (graph_n0_n, graph_n1_n, graph_link_n)

                        #matched on the reversed versions
                        if nodes_match_3 or nodes_match_4:
                            source_link = (source_link[1], source_link[0], source_link[2])

                        try:
                            #if reversed_link not in potential_matches[pattern_link]:
                            link_matches[pattern_link].append(source_link)
                        except KeyError:
                            link_matches[pattern_link] = [source_link]


                if not found_match:
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

            match_set = self.create_match_set(pm)



            if match_set:
                # print("Match set:")
                # print(match_set)
                yield match_set


    def create_match_set(self, pm):
        match_set = {}
        for pair in pm:
            (k, v) = pair

            p0, p1, p_link = k
            s0, s1, s_link = v

            for p, s in [(p0, s0), (p1, s1), (p_link, s_link)]:

                #p_label = self.pattern_graph.vs[p]["MT_label__"]

                #try:
                #    s_label = self.source_graph.vs[s]["MT_label__"]
                #except KeyError:

                if p in match_set.keys() and match_set[p] != s:
                    #there is already a binding, so ignore this matching possibility
                    return {}

                match_set[p] = s
        return match_set

    def print_link(self, graph, n0, n1, nlink):
        if nlink:
            link = graph.vs[nlink]["mm__"].replace("MT_pre__", "")
            try:
                link += " (" + str(graph.vs[nlink]["MT_pre__attr1"]) + ") "
                link = link.replace("\n", "").replace("return True", "").replace("return False", "")
            except KeyError:
                link += " (" + str(graph.vs[nlink]["attr1"]) + ") "
        else:
            link = "backward_link"
        print(graph.vs[n0]["mm__"].replace("MT_pre__", "") + " - " + link + " - " + graph.vs[n1]["mm__"].replace("MT_pre__", ""))