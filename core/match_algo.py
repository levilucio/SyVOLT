
import sys
from .himesis import Himesis
from .himesis_utils import standardize_name, is_RAM_attribute, to_non_RAM_attribute

class Priority(object):
    """
        Implements heuristics for the HimesisMatcher algorithm.
        Determines the order in which the candidate pairs should be computed.
        By default, the order is the index order of the nodes in igraph.
        To refine this heuristic order, you should sub-class Priority and override its methods. 
    """
    def __init__(self):
        """
            Implements heuristics for the HimesisMatcher algorithm.
            Determines the order in which the candidate pairs should be computed.
            By default, the order is the index order of the nodes in igraph.
            To refine this heuristic order, you should sub-class Priority and override its methods.
        """
        self.source_graph = None
        self.pattern_graph = None
    
    def cache_info(self, source_graph, pattern_graph):
        """
            Pre-computes any information required by the order and order_all methods
            @param source_graph: The source graph.
            @param pattern_graph: The pattern graph.
        """
        pass
    
    def order_source(self, candidate_list):
        """
            Specifies the order for the terminal sets for the source graph.
            @param candidate_list: The list of possible candidates.
        """
        return sorted(candidate_list)
    
    def order_pattern(self, candidate_list):
        """
            Specifies the order for the terminal sets for the pattern graph.
            @param candidate_list: The list of possible candidates.
        """
        return sorted(candidate_list)
    
    def order_all_source(self, candidate_list):
        """
            Specifies the order for all source nodes.
            @param candidate_list: The list of possible candidates.
        """
        return candidate_list
    
    def order_all_pattern(self, candidate_list):
        """
            Specifies the order for all pattern nodes.
            @param candidate_list: The list of possible candidates.
        """
        return candidate_list


class HimesisMatcher(object):
    """
        Represents a pattern matching algorithm for typed attributed multi-graphs.
        The pattern matching algorithm is based on VF2.
    """
    def __init__(self, source_graph, pattern_graph, pred1={}, succ1={}, pred2 = {}, succ2 = {}):
        """
            Represents a pattern matching algorithm for typed attributed multi-graphs.
            @param source_graph: The source graph.
            @param pattern_graph: The pattern graph.
            @param priority: Instance of a sub-class of the Priority class.
                            It is used to determine the order in which the candidate pairs should be computed.
            @param pred1: Pre-built dictionary of predecessors in the source graph.
            @param succ1: Pre-built dictionary of successors in the source graph.
        """

        try:
            src_eqs = source_graph["equations"]
        except KeyError:
            print("Graph has no equations array: " + source_graph.name)
            src_eqs = []

        try:
            patt_eqs = pattern_graph["equations"]
        except KeyError:
            print("Graph has no equations array: " + pattern_graph.name)
            patt_eqs = []

        try:
            patt_labels = pattern_graph.vs["MT_label__"]
        except KeyError:
            patt_labels = []

        self.src_eqs_constant = {}
        self.src_eqs_variable = []


        for eq in src_eqs:
            if eq[1][0] == "constant":
                node_num = eq[0][0]
                attr = eq[0][1]
                try:
                    self.src_eqs_constant[node_num].append((attr, eq[1][1]))
                except KeyError:
                    self.src_eqs_constant[node_num] = [(attr, eq[1][1])]
            else:
                self.src_eqs_variable.append(eq)

        self.patt_eqs_constant = {}
        self.patt_eqs_variable = []

        for eq in patt_eqs:
            if eq[1][0] == "constant":
                node_label = str(eq[0][0])
                attr = eq[0][1]
                #print("Node label: " + str(node_label))
                #print("Labels: " + str(patt_labels))

                node_num = patt_labels.index(node_label)
                try:
                    self.patt_eqs_constant[node_num].append((attr, eq[1][1]))
                except KeyError:
                    self.patt_eqs_constant[node_num] = [(attr, eq[1][1])]
            else:
                self.patt_eqs_variable.append(eq)

        # print("\n")
        # print("Src constant eqs: " + str(self.src_eqs_constant))
        # print("Src variable eqs: " + str(self.src_eqs_variable))
        # print("Patt constant eqs: " + str(self.patt_eqs_constant))
        # print("Patt variable eqs: " + str(self.patt_eqs_variable))

        self.G1 = source_graph
        self.G2 = pattern_graph
        self.pred1 = pred1
        self.succ1 = succ1

        self.G1_vcount = self.G1.vcount()
        self.G2_vcount = self.G2.vcount()

        # removed priority for speed
        #assert(isinstance(priority, Priority))
        #self.priority = priority
        #self.priority.source_graph = source_graph
        #self.priority.pattern_graph = pattern_graph

        # Set recursion limit
        self.old_recursion_limit = sys.getrecursionlimit()
        expected_max_recursion_level = self.G2_vcount
        if self.old_recursion_limit < 1.5 * expected_max_recursion_level:
            # Give some breathing room
            sys.setrecursionlimit(int(1.5 * expected_max_recursion_level))
        
        # Initialize the state
        self.initialize()
        
        # Check whether we are considering multi-graph
#        if reduce(lambda x,y: x or y, self.G2.is_multiple()):
#            self.cache_info_multi(self.G1_nodes, self.G2_nodes)
        
        # Scan the two graphs to cache required information.
        # Typically stores the results of expensive operation on the graphs.
        # This speeds up the algorithm significantly.
        # (disabled)
        # self.cache_info()

        # Memoize the predecessor & successor information:
        # for each node store the number of neighbours and the list

        #igraph.IN = 2, igraph.OUT = 1
        if  not self.pred1:
            self.pred1 = [(len(tmp), tmp) for tmp in self.G1.get_adjlist(mode=2)]

        if not self.succ1:
            self.succ1 = [(len(tmp), tmp) for tmp in self.G1.get_adjlist(mode=1)]

        self.pred2 = pred2
        self.succ2 = succ2

        if not pred2:
            #print("No pred2 for graph: " + self.G2.name)
            self.pred2 = [(len(tmp), tmp) for tmp in self.G2.get_adjlist(mode=2)]

        if not succ2:
            self.succ2 = [(len(tmp), tmp) for tmp in self.G2.get_adjlist(mode=1)]


        self.has_super = None
        if self.G1_vcount > 0 and self.G2_vcount > 0:
            #keep track of the metamodels
            self.mm1 = self.G1.vs["mm__"]
            self.mm2 = [mm[8:] for mm in self.G2.vs["mm__"]]



            #self.patt_has_subtype = self.G2.vs['MT_subtypeMatching__']

            try:
                self.superclasses_dict = self.G2["superclasses_dict"]
            except KeyError:
                self.superclasses_dict = {}
                print("Graph " + self.G2.name + " needs to be updated. Can't find 'superclasses_dict'")

            if self.superclasses_dict:
                self.src_has_supertype = [child_mm in self.superclasses_dict for child_mm in self.mm1]
            else:
                self.src_has_supertype = [False] * self.G1_vcount



            self.superclasses_dict = self.G2["superclasses_dict"]

            #ignore an empty directory
            if self.superclasses_dict:
                self.has_super = [mm in self.superclasses_dict.keys() for mm in self.mm1]

    
    def cache_info(self):
        """
            Cache information on the nodes.
            Typically stores the results of expensive operation on the graphs.
            This speeds up the algorithm significantly.
        """
        # Cache individual nodes
        self.G1_nodes = self.G1.node_iter()
        self.G2_nodes = self.G2.node_iter()
        

        
        # Cache any further data used for the heuristic prioritization for computing the candidate pair
        # This is done when initializing the priority class
        self.priority.cache_info(self.G1, self.G2)
    
    def reset_recursion_limit(self):
        """
            Restores the recursion limit.
        """
        sys.setrecursionlimit(self.old_recursion_limit)
    
    def initialize(self):
        """
            (Re)Initializes the state of the algorithm.
        """
        #=======================================================================
        # The algorithm is based on VF2.
        # The following are the data-structures used:
        #    - M_1: the current partial mapping from G1 to G2
        #    - M_2: the current partial mapping from G2 to G1
        #    - T1_in: the in-neighbours of the nodes in M_1
        #    - T2_in: the in-neighbours of the nodes in M_2
        #    - T1_out: the out-neighbours of the nodes in M_1
        #    - T2_out: the out-neighbours of the nodes in M_2
        #=======================================================================
        
        # core_1[n] contains the index of the node m paired with n, if n is in the mapping
        self.core_1 = {}   # This is M_1
        # core_2[m] contains the index of the node n paired with m, if m is in the mapping
        self.core_2 = {}   # This is M_2
        
        # The value stored is the depth of the search tree when the node became part of the corresponding set
        # Non-zero if n is in M_1 or in T_1^{in}
        self.in_1 = {}
        # Non-zero if n is in M_1 or in T_1^{out}
        self.out_1 = {}
        # Non-zero if m is in M_2 or in T_2^{in}
        self.in_2 = {}
        # Non-zero if m is in M_2 or in T_2^{out}
        self.out_2 = {}
        # To improve the performance, we also store the following vectors
        # Non-zero if n is in M_1 or in T_1^{in} or in T_1^{out}
        self.inout_1 = {}
        # Non-zero if n is in M_2 or in T_2^{in} or in T_2^{out}
        self.inout_2 = {}
        
        # Prepare the necessary data structures required for backtracking
        self.state = self.save()#HimesisMatcherState(self)

        # Provide a convenient way to access the isomorphism mapping.
        self.mapping = self.core_2.copy()

    def are_compatibile(self, src_node, patt_node):
        """
            Verifies if a candidate pair is compatible.
            More specifically, verify degree and meta-model compatibility.
            @param src_node: The candidate from the source graph.
            @param patt_node: The candidate from the pattern graph.
        """

        # WARNING:
        # MOVED TO _MATCH FUNCTION!
        
        # First check if they are of the same type

        #if sourceNode["mm__"] == to_non_RAM_attribute(patternNode["mm__"]):
        #Assumption: patternNode["mm__"] always starts with "MT_pre__"
        #MT_pre taken off when creating self.mm2
        #if sourceNode["mm__"] == patternNode["mm__"][8:]:

        sourceMM = self.mm1[src_node]
        targetMM = self.mm2[patt_node]
        if sourceMM == targetMM:
            # Then check for the degree compatibility
            return (self.pred2[patt_node][0] <= self.pred1[src_node][0]
                    and self.succ2[patt_node][0] <= self.succ1[src_node][0])

        # Otherwise, first check for the degree compatibility
        elif not (self.pred2[patt_node][0] <= self.pred1[src_node][0]
                and self.succ2[patt_node][0] <= self.succ1[src_node][0]):
            return False


        if self.src_has_supertype[src_node]:
            return targetMM in self.superclasses_dict[sourceMM]

        #
        # # Then check sub-types compatibility
        # if self.patt_has_subtype[patt_node]:
        #     for subtype in self.G2.vs[patt_node]['MT_subtypes__']:
        #         if sourceMM == subtype[8:]:
        #             return True
        return False

    def candidate_pairs_iter(self):
        """
            Iterator over candidate pairs of nodes in G1 and G2, according to the VF2 algorithm.
            The candidate pairs have all passed the compatibility check before output.
            @return: The candidate pair (source node, pattern node)
        """

        #=======================================================================
        # Here we compute P(s) = (p1,p2) the candidate pair
        # for the current partial mapping M(s).
        #=======================================================================
        
        # First try the nodes that are in both Ti_in and Ti_out
        if len(self.inout_1) > len(self.core_1) and len(self.inout_2) > len(self.core_2):
            for patt_node in sorted(self.inout_2):
                if patt_node not in self.core_2:
                    break
            for src_node in sorted(self.inout_1):
                if src_node not in self.core_1:
                    yield src_node, patt_node
        
        # If T1_out and T2_out are both non-empty:
        # P(s) = T1_out x {min T2_out}
        elif len(self.out_1) > len(self.core_1) and len(self.out_2) > len(self.core_2):
            for patt_node in sorted(self.out_2):
                if patt_node not in self.core_2:
                    break
            for src_node in sorted(self.out_1):
                if src_node not in self.core_1:
                    yield src_node, patt_node
    
        # If T1_in and T2_in are both non-empty:
        # P(s) = T1_in x {min T2_in}
        elif len(self.in_1) > len(self.core_1) and len(self.in_2) > len(self.core_2):
            for patt_node in sorted(self.in_2):
                if patt_node not in self.core_2:
                    break
            for src_node in sorted(self.in_1):
                if src_node not in self.core_1:
                    yield src_node, patt_node
    
        # If all terminal sets are empty:
        # P(s) = (N_1 - M_1) x {min (N_2 - M_2)}
        else:
            for patt_node in range(self.G2_vcount):
                if patt_node not in self.core_2:
                    break
            for src_node in range(self.G1_vcount):
                if src_node not in self.core_1:
                    yield src_node, patt_node
    
    def are_syntactically_feasible(self, src_node, patt_node):
        """
            Determines whether the two nodes are syntactically feasible,
            i.e., it ensures that adding this candidate pair does not make it impossible to find a total mapping.
            @param src_node: The candidate from the source graph.
            @param patt_node: The candidate from the pattern graph.
            @return: True if they are syntactically feasible, False otherwise.
        """
        #=======================================================================
        # The syntactic feasibility considers the topology of the two graphs.
        # It verifies that edges directly or indirectly connected to M(s + P(s))
        # does not violate the subgraph matching conditions.
        #=======================================================================
        
        # Check for self-loops
#        e1, e2 = -1, -1
#        if patt_node in self.succ2[patt_node] or patt_node in self.pred2[patt_node]:
#            if src_node in self.succ1[src_node] or src_node in self.pred1[src_node]:
#                e1 = self.G1.get_eid(src_node, src_node)
#                e2 = self.G2.get_eid(patt_node, patt_node)
#                if self.G1.count_multiple(e1) < self.G2.count_multiple(e2):
#                    return False
#            else:
#                return False
        
        # Counters for in and out edges found 
        in1 = 0
        in2 = 0
        out1 = 0
        out2 = 0
        inout1 = 0
        inout2 = 0
        
        # Checks if successors are compatible
        for successor2 in self.succ2[patt_node][1]:
            #tmp = self.G2.predecessors(successor2)
            # tmp = self.pred2[successor2][1]
            # self.pred2[successor2] = (len(tmp), tmp)
            # tmp = self.G2.successors(successor2)
            # self.succ2[successor2] = (len(tmp), tmp)
            if successor2 not in self.core_2:
                for successor1 in self.succ1[src_node][1]:
                    # tmp = self.G1.predecessors(successor1)
                    # self.pred1[successor1] = (len(tmp), tmp)
                    # tmp = self.G1.successors(successor1)
                    # self.succ1[successor1] = (len(tmp), tmp)
                    if (self.succ2[successor2][0] <= self.succ1[successor1][0]
                        and self.pred2[successor2][0] <= self.pred1[successor1][0]
                        and successor1 not in self.core_1):
                        break
                else:
                    return False
                # They are compatible, so update the counters of the pattern node
                if self.pred2[successor2][1]:
                    in2 += 1
                if self.succ2[successor2][1]:
                    out2 += 1
                if not self.pred2[successor2][1] and not self.succ2[successor2][1]:
                    inout2 += 1
            else:
                if self.core_2[successor2] not in self.succ1[src_node][1]:
                    return False
        
        # Checks if predecessors are compatible
        for predecessor2 in self.pred2[patt_node][1]:
            # tmp = self.G2.predecessors(predecessor2)
            # self.pred2[predecessor2] = (len(tmp), tmp)
            # tmp = self.G2.successors(predecessor2)
            # self.succ2[predecessor2] = (len(tmp), tmp)
            if predecessor2 not in self.core_2:
                for predecessor1 in self.pred1[src_node][1]:
                    # tmp = self.G1.predecessors(predecessor1)
                    # self.pred1[predecessor1] = (len(tmp), tmp)
                    # tmp = self.G1.successors(predecessor1)
                    # self.succ1[predecessor1] = (len(tmp), tmp)
                    if (self.pred2[predecessor2][0] <= self.pred1[predecessor1][0]
                        and self.pred2[predecessor2][0] <= self.pred1[predecessor1][0]
                        and predecessor1 not in self.core_1):
                        break
                else:
                    return False
                # They are compatible, so update the counters of the pattern node
                if self.pred2[predecessor2][1]:
                    in2 += 1
                if self.pred2[predecessor2][1]:
                    out2 += 1
                if not self.pred2[predecessor2][1] and not self.pred2[predecessor2][1]:
                    inout2 += 1
            else:
                if self.core_2[predecessor2] not in self.pred1[src_node][1]:
                    return False
        
        # Now compute the counters of the source node
        for successor1 in self.succ1[src_node][1]:
            if successor1 not in self.core_1:
                # tmp = self.G1.predecessors(successor1)
                # self.pred1[successor1] = (len(tmp), tmp)
                # tmp = self.G1.successors(successor1)
                # self.succ1[successor1] = (len(tmp), tmp)
                if self.pred1[successor1][1]:
                    in1 += 1
                if self.succ1[successor1][1]:
                    out1 += 1
                if not self.pred1[successor1][1] and not self.succ1[successor1][1]:
                    inout1 += 1
            # For induced matches
            #else:
            #    if self.core_1[successor1] not in self.succ2[patt_node]:
            #        return False
        
        # Now compute the counters of the source node
        for predecessor1 in self.pred1[src_node][1]:
            if predecessor1 not in self.core_1:
                # tmp = self.G1.predecessors(predecessor1)
                # self.pred1[predecessor1] = (len(tmp), tmp)
                # tmp = self.G1.successors(predecessor1)
                # self.succ1[predecessor1] = (len(tmp), tmp)
                if self.pred1[predecessor1][1]:
                    in1 += 1
                if self.pred1[predecessor1][1]:
                    out1 += 1
                if not self.pred1[predecessor1][1] and not self.pred1[predecessor1][1]:
                    inout1 += 1
            # For induced matches
            #else:
            #    if self.core_1[predecessor1] not in self.pred2[patt_node]:
            #        return False
        
        # Finally, verify if all counters satisfy the subgraph matching conditions
        # For induced matches
        #return in2 <= in1 and out2 <= out1 and inout2 <= inout1
        return in2 <= in1 and out2 <= out1 and (in2 + out2 + inout2) <= (in1 + out1 + inout1)
    
    def are_semantically_feasible(self, src_node_num, patt_node_num):
        """
            Determines whether the two nodes are syntactically feasible,
            i.e., it ensures that adding this candidate pair does not make it impossible to find a total mapping.
            @param src_node: The candidate from the source graph.
            @param patt_node: The candidate from the pattern graph.
            @return: True if they are semantically feasible, False otherwise.
        """
        #=======================================================================
        # This feasibility check looks at the data stored in the pair of candidates.
        # It verifies that all attribute constraints are satisfied.
        #=======================================================================
        
        src_node = self.G1.vs[src_node_num]
        patt_node = self.G2.vs[patt_node_num]

        # print("\n")
        # print("Src node: " + str(src_node_num))
        # print("Src constant: " + str(self.src_eqs_constant))
        # print("Patt node: " + str(patt_node_num))
        # print("Patt constant: " + str(self.patt_eqs_constant))

        src_equations = []
        if src_node_num in self.src_eqs_constant:
            src_equations = self.src_eqs_constant[src_node_num]

        if patt_node_num in self.patt_eqs_constant:
            patt_equations = self.patt_eqs_constant[patt_node_num]

            #print("Source Eq: " + str(src_equation))
            #print("Pattern Eq: " + str(patt_equations))

            for patt_eq in patt_equations:
                patt_attr = patt_eq[0]
                patt_value = patt_eq[1]

                found = False
                for (src_attr, src_value) in src_equations:
                    if patt_attr == src_attr:
                        if patt_value == src_value:
                            found = True
                            break
                        else:
                            #print("Equations do not match")
                            return False

                if found:
                    continue

                try:
                    if src_node[patt_attr] != patt_value:
                        #print("Couldn't find value, found " + str(src_node[patt_attr]))
                        #print("Patt eq: " + str(patt_eq))
                        return False
                except KeyError:
                    #print("Couldn't find " + patt_attr + " on node " + src_node["mm__"])
                    #the attribute does not exist on the node
                    return False

        
        # Check for attributes value/constraint
        for attr in patt_node.attribute_names():
            # Attribute constraints are stored as attributes in the pattern node.
            # The attribute must be prefixed by a specific keyword
            if not attr.startswith("MT_pre__"):
                continue
            # If the attribute does not "in theory" exist
            # because igraph actually stores all attribute names in all nodes. 
            elif patt_node[attr] == None:
                continue

            attr_name = attr[8:]
            #methName = self.G2.get_attr_constraint_name(patt_node.index, attr)
            methName = 'eval_%s%s' % (attr_name, patt_node['MT_label__'])

            checkConstraint = getattr(self.G2, methName, None)
            # The following assumes that every attribute constraint is defined on the pattern graph
            # (and not on the pattern node itself) 
            #if callable(checkConstraint):
            try:
                # This is equivalent to: if not eval_attrLbl(attr_value, currNode)
                if not checkConstraint(src_node[attr_name], src_node):
                    return False
            except Exception as e:
                #TODO: This should be a TransformationLanguageSpecificException
                print("Source graph: " + self.G1.name)
                print("Pattern graph: " + self.G2.name)
                for n in self.G1.vs:
                    try:

                        print("Type: " + n["type"])
                        print("MM: " + n["mm__"])
                    except KeyError:
                        pass
                raise Exception("An error has occurred while checking the constraint of the attribute '" + attr_name + "'"
                               + " in node '" + src_node["mm__"] + "' in graph: '" + self.G1.name + "'", e)
            #assume the method is callable
            #else:
            #    raise Exception('The method %s was not found in the pattern graph' % methName)
        return True

    #@profile
    def _match(self):
        """
            Extends the pattern matching mapping.
            This method is recursively called to determine if the pattern G2
            can be completely matched on G1.
            @return: The mapping {pattern node index : source node index}
        """
        #=======================================================================
        # It cleans up the class variables after each recursive call.
        # If a match is found, we yield the mapping.
        #=======================================================================

        # Base condition when a complete match is found
        if len(self.core_2) == self.G2_vcount:
            # Save the final mapping, otherwise garbage collection deletes it
            self.mapping = self.core_2.copy()
            yield self.mapping
        else:
            for src_node, patt_node in self.candidate_pairs_iter():
                
                # Cache the predecessors and successors of the candidate pairs on the fly 
                # self.pred1, self.succ1, self.pred2, self.succ2 = {}, {}, {}, {}
                # self.pred1[src_node] = (len(self.G1.predecessors(src_node)), self.G1.predecessors(src_node))
                # self.succ1[src_node] = (len(self.G1.successors(src_node)), self.G1.successors(src_node))
                # self.pred2[patt_node] = (len(self.G2.predecessors(patt_node)), self.G2.predecessors(patt_node))
                # self.succ2[patt_node] = (len(self.G2.successors(patt_node)), self.G2.successors(patt_node))

                # Check for the degree compatibility
                if not (self.pred2[patt_node][0] <= self.pred1[src_node][0]
                        and self.succ2[patt_node][0] <= self.succ1[src_node][0]):
                    continue

                sourceMM = self.mm1[src_node]
                targetMM = self.mm2[patt_node]
                if sourceMM != targetMM:

                    if not self.src_has_supertype[src_node] or targetMM not in self.superclasses_dict[sourceMM]:
                        continue



                #if self.are_compatibile(src_node, patt_node):
                if self.are_syntactically_feasible(src_node, patt_node):
                    if self.are_semantically_feasible(src_node, patt_node):
                        # Recursive call, adding the feasible state
                        newstate = self.save(src_node, patt_node)
                        #newstate = HimesisMatcherState(self, src_node, patt_node)
                        for mapping in self._match():
                            yield mapping

                        # restore data structures
                        self.restore(newstate)
                        #newstate.restore()
    
    def has_match(self, context={}):
        """
            Determines if the pattern graph can be matched on the source graph. 
            @param context: Optional predefined mapping {string:uuid}.
            @return: True if a match is found, False otherwise.
        """
        try:
            self.match_iter(context).next()
            return True
        except StopIteration:
            return False
    
    def match_iter(self, context={}):
        """
            Iterator over matchings of the pattern graph on the source graph.
            @param context: Optional predefined mapping {pattern node index: source node index}.
            @return: The mapping {pattern node index : source node index}.
        """
        self.initialize()
        for p in context:
            if self.are_semantically_feasible(context[p], p):
                self.save(context[p], p)
            else:
                # Additional constraints on the pivot nodes are not satisfied: no match is possible
                return
        for mapping in self._match():
            yield mapping


    def save(self, src_node=None, patt_node=None):
        """
            Internal representation of state for the HimesisMatcher class.
            @param matcher: The HimesisMatcher object.
            @param src_node: The source node of the candidate pair.
            @param src_node: The pattern node of the candidate pair.
        """

        # Initialize the last stored node pair.
        saved_src_node = None
        saved_patt_node = None
        depth = 0

        if src_node is None or patt_node is None:
            # Then we reset the class variables
            self.core_1 = {}
            self.core_2 = {}
            self.in_1 = {}
            self.in_2 = {}
            self.out_1 = {}
            self.out_2 = {}
            self.inout_1 = {}
            self.inout_2 = {}

        # Watch out! src_node == 0 should evaluate to True.
        if src_node is not None and patt_node is not None:
            # Add the node pair to the isomorphism mapping.
            self.core_1[src_node] = patt_node
            self.core_2[patt_node] = src_node

            # Store the node that was added last.
            saved_src_node = src_node
            saved_patt_node = patt_node

            # Now we must update the other four vectors.
            # We will add only if it is not in there already!
            depth = len(self.core_1)

            # First we add the new nodes...
            for vector in (self.in_1, self.out_1, self.inout_1):
                if src_node not in vector:
                    vector[src_node] = depth
            for vector in (self.in_2, self.out_2, self.inout_2):
                if patt_node not in vector:
                    vector[patt_node] = depth

            # Now we add every other node...

            # Updates for T_1^{in}
            new_nodes_in = []
            # Updates for T_1^{out}
            new_nodes_out = []
            for node in self.core_1:
                new_nodes_in += self.pred1[node][1]
                new_nodes_out += self.succ1[node][1]

            for node in set(new_nodes_in):
                if node not in self.in_1 and node not in self.core_1:
                    self.in_1[node] = depth

            for node in set(new_nodes_out):
                if node not in self.out_1 and node not in self.core_1:
                    self.out_1[node] = depth

            # Updates for T_1^{inout}
            # & returns the intersection
            for node in set(self.in_1.keys()).intersection(set(self.out_1.keys())):
                if node not in self.inout_1:
                    self.inout_1[node] = depth




            # Updates for T_2^{in}
            new_nodes_in = []
            # Updates for T_2^{out}
            new_nodes_out = []

            for node in self.core_2:
                new_nodes_in += self.pred2[node][1]
                new_nodes_out += self.succ2[node][1]

            for node in set(new_nodes_in):
                if node not in self.in_2 and node not in self.core_2:
                    self.in_2[node] = depth

            for node in set(new_nodes_out):
                if node not in self.out_2 and node not in self.core_2:
                    self.out_2[node] = depth

            # Updates for T_2^{inout}
            # & returns the intersection
            for node in set(self.in_2.keys()).intersection(set(self.out_2.keys())):
                if node not in self.inout_2:
                    self.inout_2[node] = depth

        return (saved_src_node, saved_patt_node, depth)

    def restore(self, state):
        """
            Deletes the HimesisMatcherState object and restores the class variables.
        """

        saved_src_node, saved_patt_node, depth = state

        # First we remove the node that was added from the core vectors.
        # Watch out! src_node == 0 should evaluate to True.
        if saved_src_node is not None and saved_patt_node is not None:
            del self.core_1[saved_src_node]
            del self.core_2[saved_patt_node]

        # Now we revert the other four vectors.
        # Thus, we delete all entries which have this depth level.
        for vector in (self.in_1, self.in_2, self.out_1, self.out_2, self.inout_1, self.inout_2):

            vector_keys = list(vector.keys())
            for node in vector_keys:
                if vector[node] == depth:
                    del vector[node]



class HimesisMatcherState(object):
    """
        Internal representation of state for the HimesisMatcher class.
        
        This class is used internally by the HimesisMatcher class.  It is used
        only to store state specific data. There will be at most V(pattern graph) of
        these objects in memory at a time, due to the depth-first search
        strategy employed by the VF2 algorithm.
    """
    def __init__(self, matcher, src_node=None, patt_node=None):
        """
            Internal representation of state for the HimesisMatcher class.
            @param matcher: The HimesisMatcher object.
            @param src_node: The source node of the candidate pair.
            @param src_node: The pattern node of the candidate pair.
        """
        self.matcher = matcher

        # Initialize the last stored node pair.
        self.src_node = None
        self.patt_node = None
        self.depth = len(matcher.core_1)
      
        if src_node is None or patt_node is None:
            # Then we reset the class variables
            matcher.core_1 = {}
            matcher.core_2 = {}
            matcher.in_1 = {}
            matcher.in_2 = {}
            matcher.out_1 = {}
            matcher.out_2 = {}
            matcher.inout_1 = {}
            matcher.inout_2 = {}

        # Watch out! src_node == 0 should evaluate to True.
        if src_node is not None and patt_node is not None:
            # Add the node pair to the isomorphism mapping.
            matcher.core_1[src_node] = patt_node
            matcher.core_2[patt_node] = src_node
            
            # Store the node that was added last.
            self.src_node = src_node
            self.patt_node = patt_node
            
            # Now we must update the other four vectors.
            # We will add only if it is not in there already!
            self.depth = len(matcher.core_1)
            
            # First we add the new nodes...
            for vector in (matcher.in_1, matcher.out_1, matcher.inout_1):
                if src_node not in vector:
                    vector[src_node] = self.depth
            for vector in (matcher.in_2, matcher.out_2, matcher.inout_2):
                if patt_node not in vector:
                    vector[patt_node] = self.depth
                    
            # Now we add every other node...

            # Updates for T_1^{in}
            new_nodes_in = []
            # Updates for T_1^{out}
            new_nodes_out = []
            for node in matcher.core_1:
                new_nodes_in += matcher.pred1[node][1]
                new_nodes_out += matcher.succ1[node][1]

            for node in set(new_nodes_in):
                if node not in matcher.in_1 and node not in matcher.core_1:
                    matcher.in_1[node] = self.depth

            for node in set(new_nodes_out):
                if node not in matcher.out_1 and node not in matcher.core_1:
                    matcher.out_1[node] = self.depth
            
            # Updates for T_1^{inout}
            # & returns the intersection
            for node in set(matcher.in_1.keys()).intersection(set(matcher.out_1.keys())):
                if node not in matcher.inout_1:
                    matcher.inout_1[node] = self.depth



            
            # Updates for T_2^{in}
            new_nodes_in = []
            # Updates for T_2^{out}
            new_nodes_out = []

            for node in matcher.core_2:
                new_nodes_in += matcher.pred2[node][1]
                new_nodes_out += matcher.succ2[node][1]

            for node in set(new_nodes_in):
                if node not in matcher.in_2 and node not in matcher.core_2:
                    matcher.in_2[node] = self.depth

            for node in set(new_nodes_out):
                if node not in matcher.out_2 and node not in matcher.core_2:
                    matcher.out_2[node] = self.depth
            
            # Updates for T_2^{inout}
            # & returns the intersection
            for node in set(matcher.in_2.keys()).intersection(set(matcher.out_2.keys())):
                if node not in matcher.inout_2:
                    matcher.inout_2[node] = self.depth
    
    def restore(self):
        """
            Deletes the HimesisMatcherState object and restores the class variables.
        """
        
        # First we remove the node that was added from the core vectors.
        # Watch out! src_node == 0 should evaluate to True.
        if self.src_node is not None and self.patt_node is not None:
            del self.matcher.core_1[self.src_node]
            del self.matcher.core_2[self.patt_node]

        # Now we revert the other four vectors.        
        # Thus, we delete all entries which have this depth level.
        for vector in (self.matcher.in_1, self.matcher.in_2, self.matcher.out_1, self.matcher.out_2, self.matcher.inout_1, self.matcher.inout_2):

            vector_keys = list(vector.keys())
            for node in vector_keys:
                if vector[node] == self.depth:
                    del vector[node]


class VF2(HimesisMatcher):
    """
        The native VF2 algorithm for subgraph isomorphism.
    """
    def __init__(self, G1, G2):
        """
            The native VF2 algorithm for subgraph isomorphism.
            @param G1: The bigger graph.
            @param G2: The smaller graph. 
        """
        HimesisMatcher.__init__(self, G1, G2)
    
    def match_iter(self):
        """
            Iterator over mappings of G2 on a subgraph of G1.
            @return: The mapping {pattern node uuid : source node uuid}.
        """
        for mapping in self.G1.get_subisomorphisms_vf2(self.G2):
            # mapping is a list for which mapping[i] is the source node index mapped to the pattern node index i
            # So we need to convert it into a dictionary  
            match = {}
            for pattern_node, src_node in enumerate(mapping):
                match[pattern_node] = src_node
            yield match


class SubgraphIsoMatcher(HimesisMatcher):
    """
        The VF2 algorithm for subgraph isomorphism as implemented in HimesisMatcher.
        Basically this is the same as HimesisMatcher but no node data is taken into consideration. 
    """
    def __init__(self, source_graph, pattern_graph, priority=Priority()):
        """
            The VF2 algorithm for subgraph isomorphism as implemented in HimesisMatcher.
            Basically this is the same as HimesisMatcher but no node data is taken into consideration. 
        """
        HimesisMatcher.__init__(self, source_graph, pattern_graph, priority)
    
    def are_compatibile(self, src_node, patt_node):
        """
            Verifies if a candidate pair is compatible.
            More specifically, verify degree compatibility.
            @param src_node: The candidate from the source graph.
            @param patt_node: The candidate from the pattern graph.
        """
        
        return (self.pred2[patt_node][0] <= self.pred1[src_node][0]
                and self.succ2[patt_node][0] <= self.succ1[src_node][0])
    
    def are_semantically_feasible(self, sourceNode, patternNode):
        """
            Since no data is considered, the graphs have no semantics.
            @param src_node: The candidate from the source graph.
            @param patt_node: The candidate from the pattern graph.
            @return: True always. 
        """
        return True


