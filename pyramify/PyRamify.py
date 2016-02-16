#!/bin/python
import re
import sys
import os
from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from core.himesis_utils import *
from core.himesis_plus import *

import uuid

import traceback


from core.himesis import *
from itertools import combinations

from itertools import permutations

from profiler import *

'''

    1. Relaxation, which relaxes constraints on the language which are
    no longer valid for the pattern language. For instance, it should
    be possible to instantiate abstract classes in rule patterns.

    2. Augmentation, which augments metamodel elements with at-
    tributes used by the transformation engine.

    3. Modification, which modifies the data type of attributes such
    that they can express constraints on attribute values or actions
    which compute the new value of the attribute.'''
class PyRamify:

    def __init__(self, verbosity = 0, draw_svg = "True"):

        #keep track of the next label to give a graph node
        self.next_label = 0
        self.verbosity = verbosity
        self.draw_svg =(draw_svg == "True")
        self.ruleSubsumption = {}
        self.transformation_layers = []
        self.rules = {}
        self.loopingRuleSubsumption = []


    '''
     changeAttrType (M): Changes the type of attributes to 'string', which allows conditions and actions to be specified on attribute values in patterns.
     Also appends '__' to attributes starting with '__'. This is because the pLabel and pMatchSubtypes attributes (introduced in one of the next steps) need to be scoped appropriately for HOTs. 
     The first time a metamodel is ramified, each class will have a __pLabel and __pMatchSubtypes attribute.
     The next time, these attributes are renamed to ____pLabel and ____pMatchSubtypes, to allow a condition/action to be specified for the __pLabel and __pMatchSubtypes attributes which were introduced in the first RAMified metamodel.
    '''
    def changeAttrType(self, graph, make_pre = True, back_to_trace = True):

        #change mm of the graph
        try:
            if make_pre:
                graph["mm__"] = [str(Himesis.Constants.MT_PRECOND_PREFIX + graph["mm__"][0]), 'MoTifRule']
            else:
                graph["mm__"] = [str(Himesis.Constants.MT_POSTCOND_PREFIX + graph["mm__"][0]), 'MoTifRule']
        except IndexError:
            graph["mm__"] = "MM"

        # set the default constraint or action of the graph
        if make_pre:
            graph["MT_constraint__"] = get_default_constraint()
        else:
            graph["MT_action__"] = get_default_action()

        #don't change some of the attributes
        attribs_to_skip = ["GUID__", "mm__", "MT_label__", "MT_subtypes__", "MT_dirty__", "MT_subtypeMatching__"]


        #examine the nodes in order to change their attributes
        for i in range(len(graph.vs)):
            node = graph.vs[i]

            #examine each attribute
            #warning: node.attribute_names() may not
            #produce the attribute names for only this node,
            #but instead the set of all attributes for all nodes
            for attrib in node.attribute_names():

                #we ignore the attributes that are None
                #this works around the above bug
                if node[attrib] is None:
                    continue

                #skip some of the attribs
                if attrib in attribs_to_skip:
                    continue

                #skip already RAMified attribs
                #TODO: Fix for double RAMification
                if Himesis.Constants.MT_PRECOND_PREFIX in attrib:
                    continue

                if Himesis.Constants.MT_POSTCOND_PREFIX in attrib:
                    continue

                #make sure to copy the value
                val = copy.deepcopy(node[attrib])

                #delete the attrib from the node
                #(not really deletion, but will be ignored in the future)
                node[attrib] = None

                #re-add the value with the new attribute name
                if make_pre:
                    new_attrib_name = Himesis.Constants.MT_PRECOND_PREFIX + attrib
                else:
                    new_attrib_name = Himesis.Constants.MT_POSTCOND_PREFIX + attrib

                node[new_attrib_name] = val

        #go through the graph again,
        #to fix some edge cases
        for i in range(len(graph.vs)):
            node = graph.vs[i]

            for attrib in node.attribute_names():

                if node[attrib] is None:
                    continue

                #add the prefix to the mm
                #TODO: Fold this into above for loop
                if attrib == "mm__":

                    if back_to_trace:
                        if node["mm__"] == "backward_link":
                            node["mm__"] = "trace_link"

                    if make_pre:
                        node["mm__"] = Himesis.Constants.MT_PRECOND_PREFIX + node["mm__"]
                    else:
                        node["mm__"] = Himesis.Constants.MT_POSTCOND_PREFIX + node["mm__"]
                    continue

                #skip the other attribs
                if attrib in attribs_to_skip:
                    continue


                #TODO: Come up with a nice pattern for these attributes
                #Hack for Attributes         
                
                if "Attribute" in node["mm__"] and attrib == "MT_pre__name":
                    node[attrib] = "if attr_value == \"" + node[attrib] + "\":\n    return True\nreturn False\n"

                #Hack for Constants
                
                elif "Constant" in node["mm__"] and attrib == "MT_pre__name":
                    node[attrib] = "if attr_value == \"" + node[attrib] + "\":\n    return True\nreturn False\n"
                    
                elif "Constant" in node["mm__"] and attrib == "MT_pre__value":
                    node[attrib] = "if attr_value == \"" + node[attrib] + "\":\n    return True\nreturn False\n"
                    
                elif "directLink" in node["mm__"] and attrib == "MT_pre__attr1":
                    node[attrib] = "if attr_value == \"" + node[attrib] + "\":\n    return True\nreturn False\n"
                    
                elif "Constant" in node["mm__"] and attrib == "MT_post__value":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "directLink" in node["mm__"] and attrib == "MT_post__attr1":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "Attribute" in node["mm__"] and attrib == "MT_post__name":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "Constant" in node["mm__"] and attrib == "MT_post__name":
                    node[attrib] = "return '" + node[attrib] + "'"

                else:
                    #set the other values to the default match or rewrite code
                    if make_pre:
                        node[attrib] = get_default_match_code()
                    else:
                        node[attrib] = get_default_rewrite_code()

            #set some other attribs for the node
            if make_pre:
                node["MT_dirty__"] = False

        if make_pre:
            graph["superclasses_dict"] = {}

        return graph


    #RAMify this file
    def do_RAMify(self, graph, output_dir, remove_rule_nodes = True, back_to_trace = True):

        #in some cases, the 'structural' or 'rule' nodes are removed
        if remove_rule_nodes is True:
            remove_nodes = find_nodes_with_mm(graph, ["MatchModel", "ApplyModel", "paired_with", "match_contains", "apply_contains", "directLink_T"])
            print("Removing rule nodes")
            graph.delete_nodes(remove_nodes)

        #make sure this graph becomes a precondition pattern
        graph = makePreConditionPattern(graph)

        #change the attribs in this graph
        graph = self.changeAttrType(graph, back_to_trace = back_to_trace)


        #compile the output pattern for future study + use
        #throw everything in the output dir
        #graph.compile(output_dir)

        return graph

    #=========================
    #=========================

    #hacky, could be extended to better match hand-built rules
    def get_RAMified_name(self, name, partial=False):
        s = name.replace(".py", "") + "_Matcher_"
        if partial:
            s = s + "LHS"
        return s

    # create the backward patterns for this file
    def get_backward_patterns(self, rule):
        if self.verbosity >= 2:
            print("\nStarting get backward patterns")
        name = list(rule.keys())[0]
        graph = list(rule.values())[0]

        label = 0
        for i in range(len(graph.vs)):
            graph.vs[i]["MT_label__"] = str(label)
            label += 1

        return_graph = graph

        #check to see which nodes have backward links
        backwards_links = find_nodes_with_mm(graph, ["backward_link"])

        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return [{graph.name: None}, []]

        #there are backward links, so start RAMifying
        out_dir = "./patterns/"
        outfile = out_dir + self.get_RAMified_name(name) + ".py"

        graph = graph.copy()
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)


        bwPatterns = []
        bwPatterns2Rule = {}

        #The node mappings may have changed
        #So to be safe, find the backward/trace links again
        backwards_links = find_nodes_with_mm(graph, ["MT_pre__trace_link"])

        #get the ids of the structural nodes
        #structure_nodes = find_nodes_with_mm(graph, ["MT_pre__MatchModel", "MT_pre__paired_with", "MT_pre__ApplyModel", "MT_pre__match_contains", "MT_pre__apply_contains"])
        #structure_nums = [get_node_num(graph, item) for item in structure_nodes]


        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = graph.copy()
        new_graph = makePreConditionPattern(new_graph)


        # keep the nodes attached to the backward link plus the 'structural' nodes
        #that should be kept
        nodes_to_keep = []  # + new_structure


        #for each backward link found, create a matcher for the attached nodes
        i = 0
        for link in backwards_links:
            #find the nodes attached to the backwards link
            attached_nodes = look_for_attached(link, new_graph)


            # #get the nodes attached to the nodes attached to the backward link
            # attached_to_attached = []
            # for a in attached_nodes:
            #     b = self.look_for_attached(new_graph.vs[a], new_graph)
            #     attached_to_attached += b
            #
            # #start a list of nodes to keep
            # new_structure = []
            #
            # #the metamodels to keep
            # keep_mms = ["MT_pre__MatchModel", "MT_pre__paired_with", "MT_pre__ApplyModel"]
            #
            # #for all the 'structural' nodes
            # for item in structure_nums:
            #
            #     #keep the node if it is attached to a node attached to the backwards link
            #     #or the metamodel should be kept
            #     if item in attached_to_attached or new_graph.vs[item]["mm__"] in keep_mms:
            #         new_structure.append(item)


            nodes_to_keep += attached_nodes

        #get the list of nodes to remove
        #(which is all nodes that should not be kept)
        nodes_to_remove = range(len(new_graph.vs))
        nodes_to_remove = [new_graph.vs[item] for item in nodes_to_remove if item not in nodes_to_keep]

        #remove everything except for the attached nodes and the backward link
        new_graph.delete_nodes(nodes_to_remove)


        #create a new name for this backward matcher
        #replace the pattern name with the partial pattern name
        new_name = new_graph.name + "_rule_trace_checker" + str(i)
        i += 1

        #write out the file
        new_graph.name = new_name
        new_graph["name"] = new_name

        #remove equations for backward patterns
        new_graph["equations"] = []


        file_name = new_graph.compile(out_dir)

        if self.verbosity >= 2:
            print("Backward patterns compiled to: " + file_name)

        rule = load_class(out_dir + "/" + new_name)
        name = list(rule.keys())[0]
        backward_pattern = list(rule.values())[0]

        if self.draw_svg:
            graph_to_dot(new_name, backward_pattern)

        #create the Matcher
        matcher = Matcher(backward_pattern, disambig_matching = True)

        #append the new backward pattern and name mapping
        bwPatterns.append(matcher)
        #bwPatterns2Rule[matcher] = name

        return [{str(return_graph.name): matcher}, bwPatterns2Rule]

    
    def get_all_nodes(self, graph):
        node_list = []

        for n in graph.vs:

            if n["mm__"] in ["MT_pre__match_contains", "MT_pre__apply_contains", \
                             "MT_pre__paired_with",
                             "MT_pre__MatchModel", "MT_pre__ApplyModel", \
                             "MT_pre__hasAttribute_T", "MT_pre__hasAttribute_S", \
                             "MT_pre__Attribute", "MT_pre__Equation", \
                             "MT_pre__Constant", "MT_pre__Concat", \
                             "MT_pre__leftExpr", "MT_pre__rightExpr", \
                             "MT_pre__trace_link", "MT_pre__hasAttribute_S", \
                             "MT_pre__directLink_S", "MT_pre__directLink_T", \
                             "MT_pre__indirectLink_S", "MT_pre__indirectLink_T", \
                             ]:
                continue

            node_list.append(n)
            
        return node_list

    def get_all_nodes_with_equations(self, graph):

        #these are all nodes that are not part of the metamodel
        all_nodes = self.get_all_nodes(graph)


        all_nodes_w_eqs = {}
        for n in all_nodes:

            node_num = get_node_num(graph, n)

            connected_nodes = flood_find_nodes(node_num, graph, ["MT_pre__match_contains", "MT_pre__apply_contains",
                                                                "MT_pre__directLink_S", "MT_pre__directLink_T",
                                                                "MT_pre__indirectLink_S", "MT_pre__indirectLink_T",
                                                                "MT_pre__trace_link"], )

            all_nodes_w_eqs[n] = connected_nodes
        return all_nodes_w_eqs


    # Build the LHS condition for the combinators for rules that are subsumed by others.
    # If the combinator is to match outside the subsumed rule, writeOnTop is False
    # If the combinator is to match on the subsumed rule, writeOnTop is True     
    def get_LHS_combinator_match_code(self, graph, writeOnTop):
    
        match_apply_nodes = self.get_all_nodes(graph)
        
        LHS_condition_string = "from core.himesis_plus import flood_find_nodes\n"
        LHS_condition_string += "nodesToCheck = ["

        for node in match_apply_nodes:
            node_label = node["MT_label__"]
            LHS_condition_string += "'" + str(node_label) + "'" + ","
        LHS_condition_string += "]\n"
        LHS_condition_string += "setsOfpairedWithNodes = []\n"

        # check what rule the match found is connected to 
        LHS_condition_string += "for node in nodesToCheck:\n"
        #LHS_condition_string += "    print 'Node: ' + str(node)\n"
        LHS_condition_string += "    pairedWithNodes = flood_find_nodes(PreNode(node).index, graph,['directLink_S', 'directLink_T', \
'indirectLink_S', 'indirectLink_T','hasAttribute_S', 'hasAttribute_T', 'trace_link'],['paired_with'], ['paired_with'])\n"
        LHS_condition_string += "    setsOfpairedWithNodes.append(set(pairedWithNodes))\n"   
        #LHS_condition_string += "    print 'Rule nodes: ' + str(pairedWithNodes)\n"
                
        LHS_condition_string += "result = set.intersection(*setsOfpairedWithNodes)\n"
        #LHS_condition_string += "print '>>>>>> Result: ' + str(result)\n"
        # it is fully connected to the subsuming rule            
        if writeOnTop:
            LHS_condition_string += "if result == set():\n"
            LHS_condition_string += "    return False\n"
            LHS_condition_string += "else:\n"
            LHS_condition_string += "    return True"  
        # it is not fully connected to the subsuming rule              
        else:
            LHS_condition_string += "if result != set():\n"
            LHS_condition_string += "    return False\n"
            LHS_condition_string += "else:\n"
            LHS_condition_string += "    return True\n"
                         
#         print "--------------------------------------------------------------"
#         print LHS_condition_string              
#         print "--------------------------------------------------------------"
        
        return LHS_condition_string



    # create the rule combinators for this file
    def get_rule_combinators(self, rule):

        if self.verbosity >= 2:
            print("\nStarting to get rule combinators")
        name = list(rule.keys())[0]
        graph = list(rule.values())[0]


        label = 0
        for i in range(len(graph.vs)):
            graph.vs[i]["MT_label__"] = str(label)
            label += 1

        return_graph = copy_graph(graph)

        # check to see which nodes have backward links
        backwards_links = find_nodes_with_mm(graph, ["backward_link"])

        rule_has_backward_links = False

        #no backward links in file, do nothing
        if len(backwards_links) != 0:
            rule_has_backward_links = True
            #return [{graph.name: None}, []]
        
        #there are backward links, so start RAMifying
        out_dir = "./patterns/"
        outfile = out_dir + self.get_RAMified_name(name) + ".py"

        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)

        #change the graph's name
        #graph.name = self.get_RAMified_name(name)
        #graph["name"] = self.get_RAMified_name(name)

        #output the graph
        #graph.compile(out_dir)

        bwPatterns = []
        bwPatterns2Rule = {}

        #The node mappings may have changed
        #So to be safe, find the backward/trace links again
        backwards_links = find_nodes_with_mm(graph, ["MT_pre__trace_link"])

       
        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = copy_graph(graph)
        new_graph = makePreConditionPattern(new_graph)



        base_graph = copy_graph(new_graph)

 #get the ids of the structural nodes
        
        #TODO: Get rewriter graph from matcher rewriter
        
        structure_nodes = find_nodes_with_mm(return_graph, ["MT_pre__MatchModel", "MT_pre__paired_with",
                                                          "MT_pre__ApplyModel", "MT_pre__match_contains",
                                                          "MT_pre__apply_contains"])
        structure_nums = [get_node_num(return_graph, item) for item in structure_nodes]
        
        
        rewriter_graph = self.make_rewriter(return_graph)
        #self.copy_graph(return_graph)
        
        
        rewriter_graph.delete_nodes(structure_nums)


        #make the base graph
        # nodes_w_eqs = self.get_all_nodes_with_equations(base_graph)
        #
        # remove_nodes = []
        # keep_nodes = []
        # for n in nodes_w_eqs.keys():
        #
        #     #node_num = self.get_node_num(graph, n)
        #     connected = look_for_attached(n, base_graph)
        #
        #     in_match = False
        #     in_apply = False
        #     backward_link = False
        #
        #     for c in connected:
        #         if graph.vs[c]["mm__"] == "MT_pre__match_contains":
        #             in_match = True
        #             keep_nodes.append(n)
        #         elif graph.vs[c]["mm__"] == "MT_pre__apply_contains":
        #             in_apply = True
        #         elif graph.vs[c]["mm__"] == "MT_pre__trace_link":
        #             backward_link = True
        #
        #     if in_apply and not backward_link:
        #         remove_nodes += nodes_w_eqs[n]
                
#         print("Keep nodes: ")
#         for k in keep_nodes:
#             print(k["mm__"])
            
        #print("Remove nodes: ")
        #for r in remove_nodes:
            #print(r["mm__"])
            
        # for k in keep_nodes:
        #
        #     k_num = get_node_num(base_graph, k)
        #     try:
        #         remove_nodes.remove(k_num)
        #     except Exception:
        #         pass

        #base_graph["equations"] = []

        #base_graph.delete_nodes(remove_nodes)

        
        # # turn the backward links into trace links
        #
        # backwards_links2 = self.find_nodes_with_mm(rewriter_graph, ["backward_link"])
        # #print(backwards_links2)
        #
        # for node in backwards_links2:
        #      node["mm__"] = "trace_link
        
        # remove apply classes not connected to any backward link
        
        apply_nums = []
        bk_links = find_nodes_with_mm(base_graph, ["MT_pre__trace_link"])
        bk_links_nums = [get_node_num(base_graph, item) for item in bk_links]
        apply_contains_nodes = find_nodes_with_mm(base_graph, ["MT_pre__apply_contains"])
        for node in apply_contains_nodes:
            apply_node = base_graph.neighbors(node,"out")[0]
            neighbors_apply_node = base_graph.neighbors(apply_node,"out")
            if set(neighbors_apply_node).intersection(bk_links_nums) == set():
                apply_nums.append(apply_node)

        structure_nodes = find_nodes_with_mm(base_graph, ["MT_pre__MatchModel", "MT_pre__paired_with",
                                                          "MT_pre__ApplyModel", "MT_pre__match_contains",
                                                          "MT_pre__apply_contains"])
        structure_nums = [get_node_num(base_graph, item) for item in structure_nodes]
        
        link_nodes = find_nodes_with_mm(base_graph, ["MT_pre__directLink_T", "MT_pre__indirectLink_T"])
        link_nums = [get_node_num(base_graph, item) for item in link_nodes]


        base_graph.delete_nodes(structure_nums + link_nums + apply_nums)
        
        if self.draw_svg:
            graph_to_dot("base_graph_" + base_graph.name, base_graph)
        
        
        
        link_nodes = find_nodes_with_mm(base_graph, ["MT_pre__directLink_S", "MT_pre__indirectLink_S"])
        link_nums = [get_node_num(base_graph, item) for item in link_nodes]
        
        temp_input_nodes = []
        
#         for array in input_nodes:
#             new_array = []
#             for node in array:
#                 node_num = self.get_node_num(base_graph, node)
        
        #input_nodes.append(link_nums)

        # nodes_w_eqs = self.get_all_nodes_with_equations(base_graph)
        #
        #
        # input_nodes = []
        # for n in nodes_w_eqs.keys():
        #
        #     #print("Node w eqs: " + str(n["mm__"]))
        #     #print(nodes_w_eqs)
        #
        #     #node_num = self.get_node_num(graph, n)
        #     connected = look_for_attached(n, base_graph)
        #     #print("Connected: " + str(connected))
        #
        #     backward_link = False
        #
        #     for c in connected:
        #         #print("Connected to: " + base_graph.vs[c]["mm__"])
        #         if base_graph.vs[c]["mm__"] == "MT_pre__trace_link":
        #             #print("Connected to backward link")
        #             backward_link = True
        #
        #     if not backward_link:
        #         temp_array = []
        #
        #         for actual_node in nodes_w_eqs[n]:
        #             temp_array.append(base_graph.vs[actual_node])
        #
        #         input_nodes.append(nodes_w_eqs[n])
        #
        #
        # output = sum([list(map(list, combinations(input_nodes, i))) for i in range(len(input_nodes) + 1)], [])

        rewrite_name = rewriter_graph.name + "_rule_combinator_rewriter"

        # levis_tiny_hack = True
        # if levis_tiny_hack and len(output) > 1:
        #     output = [output[0], output[-1]]


        # LEVI: we only need the total and the partial combinator.
        # the total combinator includes all the base graph as match and no NAC.
        # the partial combinator includes only the backward links, and has as NAC the remaining base graph.
        
        # first build the total combinator (just the base graph)        
        total_combinator_matcher = copy_graph(base_graph)
        
        # now build the partial combinator by removing everything except for the backward links
        partial_combinator_matcher = copy_graph(base_graph)

        partial_combinator_matcher["equations"] = []

        
        # remove all nodes that are not connected to backward links

        backwards_links = find_nodes_with_mm(partial_combinator_matcher, ["MT_pre__trace_link"])

        # keep the nodes attached to the backward link that should be kept
        nodes_to_keep = []


        #for each backward link found, create a matcher for the attached nodes
        i = 0
        for link in backwards_links:
            #find the nodes attached to the backwards link
            attached_nodes = look_for_attached(link,  partial_combinator_matcher)
            nodes_to_keep += attached_nodes

        #get the list of nodes to remove
        #(which is all nodes that should not be kept)
        nodes_to_remove = range(len(partial_combinator_matcher.vs))
        nodes_to_remove = [partial_combinator_matcher.vs[item] for item in nodes_to_remove if item not in nodes_to_keep]

        #remove everything except for the attached nodes and the backward link
        partial_combinator_matcher.delete_nodes(nodes_to_remove)
       
        subsuming_rules = []
        
        if name in self.rules_needing_overlap_treatment():
            subsuming_rules = self.get_subsuming_rules(name)
        
#             print "-----------------------------"
#             print "Name: " + name
#             print subsuming_rules
#             print "-----------------------------"
            
        if subsuming_rules != []  and rule_has_backward_links:
            total_combinator_matcher_copy = copy_graph(total_combinator_matcher)
            # if there are subsuming rules add an additional combinator to deal with overlapping rules 
            combinator_matchers = [partial_combinator_matcher, total_combinator_matcher, total_combinator_matcher_copy]
        elif subsuming_rules == []  and rule_has_backward_links:
            # there are no subsuming rules, thus we don't have to consider any overlapping treatment
            combinator_matchers = [partial_combinator_matcher, total_combinator_matcher]
            # there are subsuming rules but the rule has no backward links
        elif subsuming_rules != []  and not rule_has_backward_links:
            combinator_matchers = [total_combinator_matcher]
            # there are no subsuming rules and the rule has no backward links - in this case we only build the rewriter
        elif subsuming_rules == []  and not rule_has_backward_links:
            # remove all nodes in the graph
            nodes = []
            for node in total_combinator_matcher.vs:
                nodes.append(node)
            total_combinator_matcher.delete_vertices(nodes)                         
            combinator_matchers = [total_combinator_matcher]                

        for i in range(len(combinator_matchers)):
            
#             if len(combinator_matchers) == 3 and i < 2:
#                 combinator_matchers[i]["MT_constraint__"] = self.get_LHS_combinator_match_code(combinator_matchers[i], False)
            if len(combinator_matchers) == 3 and i == 2:
                combinator_matchers[i]["MT_constraint__"] = self.get_LHS_combinator_match_code(combinator_matchers[i], True)
            elif len(combinator_matchers) == 1 and subsuming_rules != []:
                combinator_matchers[i]["MT_constraint__"] = self.get_LHS_combinator_match_code(combinator_matchers[i], True)
                
            #create a new name for this backward matcher
            #replace the pattern name with the partial pattern name
        
            new_name = combinator_matchers[i].name + "_rule_combinator_matcher_" + str(i)
            
            combinator_matchers[i].name = new_name
            combinator_matchers[i]["name"] = new_name + "_rc_matcher"    
    
            file_name = combinator_matchers[i].compile(out_dir)
            if self.verbosity >= 2:
                print("Rule combinator matcher compiled to: " + file_name)
    
            rule = load_class(out_dir + "/" + new_name)
            
            # debug printout
            if self.draw_svg:
                graph_to_dot(combinator_matchers[i].name, combinator_matchers[i])
            
            backward_pattern = list(rule.values())[0]
            
            if i == 0 and len(combinator_matchers) != 1:
                # now build the NAC for the first combinator (just the complete base graph) 
                
                NAC_graph = copy_graph(base_graph)
                NAC_graph = makePreConditionPatternNAC(NAC_graph)
                NAC_graph.name += "_rule_combinator_NAC"
                
                NAC_graph.LHS = backward_pattern
                
                file_name = NAC_graph.compile(out_dir)
                if self.verbosity >= 2:
                    print("Nac graph compiled to: " + file_name)
                
                NAC_graph = load_class(out_dir + NAC_graph.name, [backward_pattern])
                NAC_graph = list(NAC_graph.values())[0]
                
                # debug printout
                if self.draw_svg:
                    graph_to_dot(NAC_graph.name, NAC_graph)
                       
                backward_pattern.NACs = [NAC_graph]

            #create the Matcher

            matcher = Matcher(backward_pattern, disambig_matching = True)
 
 
            #TODO: Make rewriter code simpler, and same as match pattern rewriter
 
            rewriter_graph_copy = copy_graph(rewriter_graph)

#             if combinator_matchers[i] == None: 
#                 rule = load_class("property_prover_rules/HEmptyPathCondition.py")
#                 matcherCond = rule.values()[0]
#                 matcher = Matcher(matcherCond)
#                 backward_pattern = rule.values()[0]

            rewriter_graph_copy.pre = copy_graph(backward_pattern)
            rewriter_graph_copy.name = rewrite_name + "_" + str(i)
            
            file_name = rewriter_graph_copy.compile(out_dir)
            if self.verbosity >= 2:
                print("Rewriter graph compiled to: " + file_name)
            
             
            rewriter_graph2 = load_class(out_dir + rewriter_graph_copy.name)
            rewriter_graph2 = list(rewriter_graph2.values())[0]

 
            # debug printout
            if self.draw_svg:
                graph_to_dot(rewriter_graph2.name, rewriter_graph2)
 
            rewriter_graph2.pre = copy_graph(backward_pattern)
 
#            rewriter_graph2.pre = copy_graph(backward_pattern)
 
            for n in range(len(rewriter_graph2.pre.vs)):
                node = rewriter_graph2.pre.vs[n]
                #print("mm2__: " + node["mm__"])
 
            rewriter = Rewriter(rewriter_graph2)
 
 
            #append the new backward pattern and name mapping
            bwPatterns.append([matcher, rewriter])
            #bwPatterns2Rule[matcher] = name 
            
        return {name: bwPatterns}

    def remove_structure_nodes(self, graph):
        #structure_nodes = find_nodes_with_mm(graph, ["MatchModel", "match_contains", "paired_with", "ApplyModel", "apply_contains"])
        structure_nodes = find_nodes_with_mm(graph, ["paired_with", "ApplyModel", "apply_contains"])
        graph.delete_nodes(structure_nodes)
        return graph




    def get_match_graph(self, graph):

        if self.draw_svg:
            graph_to_dot(graph.name + "_original", graph)

        apply_contain_node = find_nodes_with_mm(graph, ["apply_contains"])
#         apply_contain_node = get_node_num(graph, apply_contain_node[0])
# 
#         apply_nodes = flood_find_nodes(apply_contain_node, graph, ["ApplyModel", "backward_link", "trace_link"])
#         apply_nodes = list(set(apply_nodes))
        
        apply_nodes = []
        for node in apply_contain_node:
            node_num = get_node_num(graph, node)
            apply_nodes.extend(flood_find_nodes(node_num, graph, ["ApplyModel", "backward_link", "trace_link"]))
        apply_nodes = list(set(apply_nodes))

#         print "-----------------------------"
#         print graph.name
#         print "found: "
#         print "-----"
#         for a in apply_nodes:
#             print(graph.vs[a]["mm__"])
#         print "-----------------------------"

        backward_links = find_nodes_with_mm(graph, ["backward_link"])
        attached_apply = []
        for bl in backward_links:
            attached_apply += look_for_attached(bl, graph)

        for an in attached_apply:
            try:
                apply_nodes.remove(an)
            except ValueError:
                pass

        graph.delete_nodes(apply_nodes)
        
        graph = self.remove_structure_nodes(graph)

        return graph

    def make_rewriter(self, graph):

        rewriter = copy_graph(graph)

        #Add trace links
        match_contains = find_nodes_with_mm(graph, ["match_contains"])
        match_attached = []
        for mc in match_contains:
            match_attached += look_for_attached(mc, rewriter)
        match_attached = list(set(match_attached))

        apply_contains = find_nodes_with_mm(graph, ["apply_contains"])
        apply_attached = []
        for ac in apply_contains:
            apply_attached += look_for_attached(ac, rewriter)
        apply_attached = list(set(apply_attached))

        linked_nodes = []

        backward_links = find_nodes_with_mm(graph, ["backward_link", "trace_link"])
        for bl in backward_links:
            bl_attached = look_for_attached(bl, rewriter)
            #print("BL attached: " + str(bl_attached))

            linked_nodes.append([bl_attached[0], bl_attached[1]])

#         if rewriter.name == "HConnectPPortPrototypeHConnectRPortPrototype":        
#             for match_node in match_attached:
#                 if rewriter.vs[match_node]["mm__"] in ["MatchModel", "match_contains"]:
#                     continue   
#          
#             for apply_node in apply_attached:
#                 if rewriter.vs[apply_node]["mm__"] in ["ApplyModel", "apply_contains"]:
#                     continue   
        
        for match_node in match_attached:

            #print("Match node: " + str(rewriter.vs[match_node]["mm__"]))
            if rewriter.vs[match_node]["mm__"] in ["MatchModel", "match_contains"]:
                continue

            for apply_node in apply_attached:
                #print("Apply node: " + str(rewriter.vs[apply_node]["mm__"]))
                if rewriter.vs[apply_node]["mm__"] in ["ApplyModel", "apply_contains"]:
                    continue

                found_link = False
                for a, b in linked_nodes:

                    if a == apply_node or b == apply_node:
                        #there is already a link here
                        found_link = True
                        #print("Found the link")

                if not found_link:
#                     print("Did not find link")
#                     if rewriter.name == "HConnectPPortPrototypeHConnectRPortPrototype":
#                         print "Connecting:"
#                         print "    Apply node: " + rewriter.vs[apply_node]['mm__']
#                         print "    Match node: " + rewriter.vs[match_node]['mm__']
                    new_node = rewriter.add_node()
                    rewriter.vs[new_node]["mm__"] = "trace_link"
                    rewriter.vs[new_node]["MT_label__"] = str(new_node)
                    #print("New label: " + str(rewriter.vs[new_node]["MT_label__"]))

                    rewriter.add_edge(apply_node, new_node)
                    rewriter.add_edge(new_node, match_node)


        rewriter = self.changeAttrType(rewriter, make_pre = False, back_to_trace = True)

        rewriter = makePostConditionPattern(rewriter)

        #graph_to_dot("the_rewriter_graph_after_post_" + rewriter.name, rewriter)


        return rewriter


    def make_rewriter_with_back(self, graph):

        rewriter = copy_graph(graph)

        #Add trace links
        match_contains = find_nodes_with_mm(graph, ["match_contains"])
        match_attached = []
        for mc in match_contains:
            match_attached += look_for_attached(mc, rewriter)

        apply_contains = find_nodes_with_mm(graph, ["apply_contains"])
        apply_attached = []
        for ac in apply_contains:
            apply_attached += look_for_attached(ac, rewriter)

        linked_nodes = []

        backward_links = find_nodes_with_mm(graph, ["backward_link", "trace_link"])
        for bl in backward_links:
            bl_attached = look_for_attached(bl, rewriter)
            #print("BL attached: " + str(bl_attached))

            linked_nodes.append([bl_attached[0], bl_attached[1]])

#        for match_node in match_attached:

            #print("Match node: " + str(rewriter.vs[match_node]["mm__"]))
#             if rewriter.vs[match_node]["mm__"] in ["MatchModel", "match_contains"]:
#                 continue
# 
#             for apply_node in apply_attached:
#                 #print("Apply node: " + str(rewriter.vs[apply_node]["mm__"]))
#                 if rewriter.vs[apply_node]["mm__"] in ["ApplyModel", "apply_contains"]:
#                     continue

#                 found_link = False
#                 for a, b in linked_nodes:
# 
#                     if a == apply_node or b == apply_node:
#                         #there is already a link here
#                         found_link = True
#                         #print("Found the link")
# 
#                 if not found_link:
#                     #print("Did not find link")
#                     new_node = rewriter.add_node()
#                     rewriter.vs[new_node]["mm__"] = "trace_link"
#                     rewriter.vs[new_node]["MT_label__"] = str(new_node)
#                     #print("New label: " + str(rewriter.vs[new_node]["MT_label__"]))
# 
#                     rewriter.add_edge(apply_node, new_node)
#                     rewriter.add_edge(new_node, match_node)


        #graph_to_dot("the_rewriter_graph_" + rewriter.name, rewriter)

        rewriter = self.changeAttrType(rewriter, make_pre = False, back_to_trace = False)

        rewriter = makePostConditionPattern(rewriter)

        #graph_to_dot("the_rewriter_graph_after_post_" + rewriter.name, rewriter)


        return rewriter

    def get_match_pattern(self, rule):
        name = list(rule.keys())[0]
        graph = list(rule.values())[0]

        label = 0
        for i in range(len(graph.vs)):

            graph.vs[i]["MT_label__"] = str(label)
            label += 1

        rewriter = self.make_rewriter_with_back(graph)
        
        out_dir = "./patterns/"

        graph = self.get_match_graph(graph)     
        
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False, back_to_trace = False)

        graph["mm__"] = [graph["mm__"][0], 'MoTifRule']
        graph["MT_constraint__"] = get_default_constraint()



        #Remove pre_cardinality
        for i in range(len(graph.vs)):
            node = graph.vs[i]
            try:
                del(node["MT_pre__cardinality"])
            except:
                pass

            # if node["mm__"] != "MT_pre__directLink_S":
            #     node["MT_pre__associationType"] = None

        old_name = graph.name



        graph.name = old_name + "_match_pattern_matcher"
        file_name = graph.compile(out_dir)
        if self.verbosity >= 2:
            print("Match pattern matcher compiled to: " + file_name)

        if self.draw_svg:
            graph_to_dot(graph.name, graph)

        #have to reload the graph to define all the eval functions
        rule = load_class(out_dir + "/" + old_name + "_match_pattern_matcher")
        match_graph = list(rule.values())[0]


        rewriter.pre = match_graph
        rewriter.name = old_name + "_match_pattern_rewriter"
        #graph_to_dot("the_rewriter_graph" + rewriter.name, rewriter)

        file_name = rewriter.compile(out_dir)
        if self.verbosity >= 2:
            print("Match pattern rewriter compiled to: " + file_name)

        rewriter_dict = load_class(out_dir + rewriter.name)
        rewriter = list(rewriter_dict.values())[0]

        #graph_to_dot("the_rewriter_graph_after" + rewriter.name, rewriter)

        matcher = Matcher(match_graph, disambig_matching = False)

        return {name : [matcher, Rewriter(rewriter)]}

    # helper function for the user, to list all of the
    # rules in the transformation that have backward links
    def getRulesIncludingBackLinks(self, transformation, backwardPatterns):
        rulesIncludingBackLinks = []

        for layer in transformation:
            back_links = []
            for rule in layer:
                bp = backwardPatterns[rule.name]
                if bp is []:
                    continue

                #if the rule has a backwards pattern,
                #then it has backwards links
                back_links.append(rule)

            #keep the layered structure
            rulesIncludingBackLinks.append(back_links)
        return rulesIncludingBackLinks


    #================================================================================
    
    
    # check if a rule has backward links
    def rule_has_backward_links(self, rule):
        rule_object = self.rules[rule]
        backwards_links = find_nodes_with_mm(rule_object, ["backward_link"])
        if len(backwards_links) == 0:
            return False
        return True
    

    # find all the rules that subsume a given rule    
    def get_subsuming_rules(self, rule):
        foundParent = False
        subsuming_rules = []
        for ruleKey in sorted(self.ruleSubsumption.keys()):
            if rule in set(self.ruleSubsumption[ruleKey]):
                # check for loops when two rules subsume each other
                if rule not in set(subsuming_rules):
                    foundParent = True
                    subsuming_rules.append(ruleKey)
                    subsuming_rules.extend(self.get_subsuming_rules(ruleKey))
        if not foundParent:
            return []
        else:
            return subsuming_rules


    # calculate the partial order induced by rule match subsumption for all rules in the transformation.
    def calculate_rule_subsumption(self, matchRulePatterns):
             
        rulepairs = list(permutations(sorted(self.rules.keys()),2))
        
        # keep only the pairs which correspond to subsumption relations (second element subsumes the first)
        
        pairsToRemove = []
        
        for pair in rulepairs:
            p = Packet()
            p.graph = self.rules[pair[1]]
            p = matchRulePatterns[pair[0]][0].packet_in(p)

            if not matchRulePatterns[pair[0]][0].is_success:
                pairsToRemove.append(pair)
        
        rulepairs = [pair for pair in rulepairs if pair not in pairsToRemove]

        ruleChains = []
        ruleSubsumption = {}
        
        rulepairsCopy = list(rulepairs)
        rulesToRemove = []
                 
        while rulepairsCopy != []:
            
            pair = rulepairsCopy.pop(0)
            
            if (pair[1],pair[0]) in rulepairsCopy:           
                # found a loop
                
                # remove the reversed pair from the list of pairs
                rulepairsCopy.remove((pair[1],pair[0]))

                rulesToRemove.append(pair)
                rulesToRemove.append((pair[1],pair[0]))
                
                indexOfExistingChain = []
                
                for chainIndex in range(len(ruleChains)):
                    if pair[0] in ruleChains[chainIndex]:
                        # the new loop is part of a existing chains
                        indexOfExistingChain.append(chainIndex)
                    if pair[1] in ruleChains[chainIndex]:
                        # the new loop is part of a existing chains
                        indexOfExistingChain.append(chainIndex)
                        
                
                if indexOfExistingChain == []:
                    #print "going to add to the list of chains"
                    
                    # add the chain to list of chains and set the top and bottom elements
                    ruleChains.append([pair[1],pair[0]])
                    # add the new pair to the subsumption relation                        
                    ruleSubsumption[pair[1]] = [pair[0]]   
                else:
                    # gets merged with existing chain(s)
                    if len(indexOfExistingChain) == 1:
                        #print "going to add to one chain: " + str(pair)
                        # extends one chain
                        # push the new rule to the bottom of the chain                        
                        newElement = list(set([pair[0],pair[1]]) - set(ruleChains[indexOfExistingChain[0]]))[0]
                        # add the new rule at the end of the existing chain in the subsumption relation
                        ruleSubsumption[ruleChains[indexOfExistingChain[0]][len(ruleChains[indexOfExistingChain[0]])-1]] = [newElement]
                        ruleChains[indexOfExistingChain[0]].append(newElement)
                        
                    elif len(indexOfExistingChain) == 2:
                        if len(indexOfExistingChain) == 2 and indexOfExistingChain[0] == indexOfExistingChain[1]:
                            pass
                            #print "discarding link"
                        else:
                            #print "going to merge two chains"
                            # merges two existing chains
                            chain1 = list(ruleChains[indexOfExistingChain[0]])
                            chain2 = list(ruleChains[indexOfExistingChain[1]])
                            ruleChains.append(chain1.extend(chain2))
                            # add connect the end of one chain to the beginning of the other
                            lastElementOfFirstChain = chain1[len(chain1)-1]
                            firstElementOfSecondChain = chain2[0]
                            ruleSubsumption[lastElementOfFirstChain] = firstElementOfSecondChain                           
                            del ruleChains[indexOfExistingChain[0]]
                            del ruleChains[indexOfExistingChain[1]]
            
            # store the information about rules having looping subsumption relations
            self.loopingRuleSubsumption = list(ruleChains)
                                    
        remainingRulepairs = [rule for rule in rulepairs if rule not in rulesToRemove]
        
        # now add all the remaining subsumption relations (not loops) to the ruleSubsumption dictionary
        
        for pair in remainingRulepairs:         
#             print "---------------------------------------"
#             print "Pair: " + str(pair)
            canAdd = True
            # check if the subsuming rule is part of a chain and not the last element of the chain
            # only last elements of chains can have children
            for ruleChain in ruleChains:
                if pair[1] in ruleChain and pair[1] != ruleChain[len(ruleChain)-1]:
#                    print "not the last element of the chain"
                    canAdd = False
                    break
            # check if the subsumed rule is part of a chain and not the first of the chain
            # only first elements of chains can have parents
            for ruleChain in ruleChains:
                if pair[0] in ruleChain and pair[0] != ruleChain[0]:
#                    print "not the first element of the chain"
                    canAdd = False
                    break
            
            if canAdd:
                if pair[1] in ruleSubsumption.keys():
                    ruleSubsumption[pair[1]].append(pair[0])
                else:
                    ruleSubsumption[pair[1]] = [pair[0]]                              
            
        return ruleSubsumption


    # return the layer a rule occurs in
    def layer_rule_occurs_in(self, rule):
        for layerIndex in range(len(self.transformation_layers)):
            for ruleIndex in range(len(self.transformation_layers[layerIndex])):
                if rule == self.transformation_layers[layerIndex][ruleIndex].name:
                    return layerIndex
        return None
        

    # Calculate if the rules need special treatment because they overlap.
    # This happens when:
    # - Rule A is subsumed by Rule B, rule A has no backward links and Rule B appears in the same layer as rule A, or in a layer before
    # - Rule A is subsumed by rule B and both rule A and rule B have backward links and Rule A appears in the same layer as rule B
    # returns a list of pairs of rules for which combinators need to be built for
    def rules_needing_overlap_treatment(self):
        rules_needing_overlap_treatment = {}
        for rule in sorted(self.rules.keys()):
            subsuming_rules = self.get_subsuming_rules(rule)           
            
            for s_rule in subsuming_rules:
                
#                 print("---------------------------------")
#                 print("Rule: " + str(rule))
# #                 print "Has backward links: " + str(self.rule_has_backward_links(rule))
# #                 print "Position: " + str(self.layer_rule_occurs_in(rule))
#                 print("Subsuming Rule: " + str(s_rule))
# #                 print "Has backward links: " + str(self.rule_has_backward_links(s_rule))
# #                 print "Position: " + str(self.layer_rule_occurs_in(s_rule))
#                 print("---------------------------------")

                try:
                    if (not self.rule_has_backward_links(rule) and not self.rule_has_backward_links(s_rule)) or\
                       (not self.rule_has_backward_links(rule) and self.rule_has_backward_links(s_rule)):
                        if self.layer_rule_occurs_in(rule) >= self.layer_rule_occurs_in(s_rule):
                            if rule in rules_needing_overlap_treatment.keys():
                                rules_needing_overlap_treatment[rule].append(s_rule)
                            else:
                                rules_needing_overlap_treatment[rule] = [s_rule]

                    elif (self.rule_has_backward_links(rule) and self.rule_has_backward_links(s_rule)):
                        if self.layer_rule_occurs_in(rule) == self.layer_rule_occurs_in(s_rule):
                            if rule in rules_needing_overlap_treatment.keys():
                                rules_needing_overlap_treatment[rule].append(s_rule)
                            else:
                                rules_needing_overlap_treatment[rule] = [s_rule]
                except Exception:
                    print("ERROR in rules_needing_overlap_treatment()")
                    tb = traceback.format_exc()
                    print(tb)
        
        return rules_needing_overlap_treatment
    
    
#     # remove loops in the subsumption relation by defining only one subsumption direction between rules that subsume each other.
#     # remove all upward subsumption relations for any but the top rule in the rules that subsume each other.
#     # remove all downward subsumption relations for any but the bottom rule in the rules that subsume each other.
#     def remove_subsumption_loops(self):                    
#         for rule1 in self.rules.keys():
#             for rule2 in self.rules.keys()

    #ramify a whole directory
    #@do_cprofile
    def ramify_directory(self, dir_name, transformation_layers):
        print("Ramifying directory: " + dir_name)
        
        self.transformation_layers = transformation_layers
        
        rules = {}
        
        backwardPatterns = {}
        backwardPatterns2Rules = {}
        backwardPatternsComplete = {}
        matchRulePatterns = {}
        ruleCombinators = {}

        for layer in transformation_layers:
            for rule in layer:

                #add the rule to the rules dict
                rule2 = load_class(dir_name + "/" + rule.name + ".py")
                rules.update(rule2)

                #reload the rule
                #this is probably not needed
                #but there were problems with aliasing and copying

                #get the backwards pattern for this rule
                rule3 = load_class(dir_name + "/" + rule.name + ".py")
                (bwPattern, bwP2Rule) = self.get_backward_patterns(rule3)
                backwardPatterns.update(bwPattern)

                if not bwP2Rule is None:
                    backwardPatterns2Rules.update(bwP2Rule)

                #fresh rule for the match pattern
                rule4 = load_class(dir_name + "/" + rule.name + ".py")
                matchRulePattern = self.get_match_pattern(rule4)
                matchRulePatterns.update(matchRulePattern)

        self.rules = rules
            
        self.ruleSubsumption = self.calculate_rule_subsumption(matchRulePatterns)
        
        rulesNeedingOverlapTreatment = self.rules_needing_overlap_treatment()
        

        #build the combinators only after calculating the dependencies between rules
        for layer in transformation_layers:
            for rule in layer:

                # fresh rule for the rule combinators
                rule5 = load_class(dir_name + "/" + rule.name + ".py")
                rule_combinator = self.get_rule_combinators(rule5)
                ruleCombinators.update(rule_combinator)
       
        
        # remove from the subsumption relation subsumption between a rule in a layer and a rule in a layer appearing before
        # TODO: this should be replaced by layer ordering to avoid tests all the time during PC construction
        try:
            for rule in self.ruleSubsumption.keys():
                rulesToDelete = []
                for subsumedRule in self.ruleSubsumption[rule]:
                    if self.layer_rule_occurs_in(rule) > self.layer_rule_occurs_in(subsumedRule) or\
                       (self.layer_rule_occurs_in(rule) < self.layer_rule_occurs_in(subsumedRule) and
                        self.rule_has_backward_links(rule) and self.rule_has_backward_links(subsumedRule)):
                        rulesToDelete.append(subsumedRule)
                self.ruleSubsumption[rule] = [r for r in self.ruleSubsumption[rule] if r not in rulesToDelete]
            # now remove empty dictionary entries
            self.ruleSubsumption = dict((k, v) for k, v in self.ruleSubsumption.items() if v)

            print("Subsumption")
            print(self.ruleSubsumption)
        except Exception as e:
            print(e)
            raise Exception("Error in subsuming rules")
            
        # remove from loopingRuleSubsumption relation rules that completeley overlap but belong to different layers, as they
        # will be treated by the total combinators. If rules belonging to more than one layer exist keep them only if two or
        # more belong to the same layer, otherwise discard

        cleanLoopingRuleSubsumption = []

        for loopingRules in self.loopingRuleSubsumption:
            loopDict = {}
            for rule in loopingRules:
                if self.layer_rule_occurs_in(rule) not in loopDict:
                    loopDict[self.layer_rule_occurs_in(rule)] = [rule]
                else:
                    loopDict[self.layer_rule_occurs_in(rule)].append(rule) 
            # keep entries that only have more than one rule
            for layer in loopDict.keys():
                if len(loopDict[layer]) > 1:
                    cleanLoopingRuleSubsumption.append(loopDict[layer])
            

        #print("Rules that need overlap treatment: " + str(rulesNeedingOverlapTreatment))
        #print("Subsumption order between rules for all layers: " + str(self.ruleSubsumption))
        #print("Rules fully overlapping with each other: " + str(cleanLoopingRuleSubsumption))

        print("\n")
        print("Finished PyRamify")
        print("==================================\n")                    

        return [rules, backwardPatterns, backwardPatterns2Rules, {}, matchRulePatterns, ruleCombinators, rulesNeedingOverlapTreatment, self.ruleSubsumption, cleanLoopingRuleSubsumption]


    #================================================================================



if __name__ == "__main__":
     #No default action
    pass



