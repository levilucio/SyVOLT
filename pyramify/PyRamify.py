#!/bin/python
import re
import sys
import os

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from core.himesis_utils import *
from core.himesis_plus import *

from pyramify.SubsumptionHandler import SubsumptionHandler

import uuid

import traceback


from core.himesis import *
from itertools import combinations


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

        self.verbosity = verbosity
        self.draw_svg =(draw_svg == "True")
        self.ruleSubsumption = {}
        self.subsumingRules = {}
        self.rulesNeedingOverlapTreatment = []
        self.transformation_layers = []
        self.rules = {}


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

        # if make_pre:
        #     graph["superclasses_dict"] = {}

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

        #no backward links in file, do nothing
        if "backward_link" not in graph.vs["mm__"]:
            return [{graph.name: None}, []]

        #there are backward links, so start RAMifying
        out_dir = "./patterns/"

        graph = graph.copy()
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)

        bwPatterns = []
        bwPatterns2Rule = {}

        #The node mappings may have changed
        #So to be safe, find the backward/trace links again
        backwards_links = find_nodes_with_mm(graph, ["MT_pre__trace_link"])

        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = graph.copy()
        new_graph = makePreConditionPattern(new_graph)


        # keep the nodes attached to the backward link
        nodes_to_keep = []


        #create a matcher for the attached nodes of all backward links
        for link in backwards_links:
            #find the nodes attached to the backwards link
            attached_nodes = look_for_attached(link, new_graph)

            nodes_to_keep += attached_nodes

        #get the list of nodes to remove
        #(which is all nodes that should not be kept)
        nodes_to_remove = range(len(new_graph.vs))
        nodes_to_remove = [new_graph.vs[item] for item in nodes_to_remove if item not in nodes_to_keep]

        #remove everything except for the attached nodes and the backward link
        new_graph.delete_nodes(nodes_to_remove)

        #create a new name for this backward matcher
        #replace the pattern name with the partial pattern name
        new_name = new_graph.name + "_rule_trace_checker"

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

        mm_list = ["MT_pre__match_contains", "MT_pre__apply_contains",
                   "MT_pre__paired_with",
                   "MT_pre__MatchModel", "MT_pre__ApplyModel",
                   "MT_pre__trace_link",
                   "MT_pre__directLink_S", "MT_pre__directLink_T",
                   "MT_pre__indirectLink_S", "MT_pre__indirectLink_T",
                   ]

        node_list = [n for n in graph.vs if n["mm__"] not in mm_list]

        return node_list

    # Build the LHS condition for the combinators for rules that are subsumed by others.
    # If the combinator is to match outside the subsumed rule, writeOnTop is False
    # If the combinator is to match on the subsumed rule, writeOnTop is True     
    def get_LHS_combinator_match_code(self, graph, writeOnTop):
    
        match_apply_nodes = self.get_all_nodes(graph)
        
        LHS_condition_string = "from core.himesis_plus import find_connected_match_node\n"
        LHS_condition_string += "nodesToCheck = ["

        for node in match_apply_nodes:
            node_label = node["MT_label__"]
            LHS_condition_string += "'" + str(node_label) + "'" + ","
        LHS_condition_string += "]\n"

        # check what rule the match found is connected to
        LHS_condition_string += "MatchNodes = [find_connected_match_node(PreNode(node).index, graph) for node in nodesToCheck]\n"

        LHS_condition_string += "result = len(set(MatchNodes)) == 1\n"
        # it is fully connected to the subsuming rule

        #LHS_condition_string += "print(MatchNodes)\n"
        #LHS_condition_string += "print('Result: ' + str(result))\n"

        LHS_condition_string += "return " + str(writeOnTop) + " and result\n"
                         
        # print("--------------------------------------------------------------")
        # print(LHS_condition_string              )
        # print(graph.name)
        # graph_to_dot("match_code_"+graph.name, graph)
        # print("--------------------------------------------------------------")


        
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
        rule_has_backward_links = False

        # no backward links in file, do nothing
        if "backward_link" in graph.vs["mm__"]:
            rule_has_backward_links = True
        
        #there are backward links, so start RAMifying
        out_dir = "./patterns/"

        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)

        bwPatterns = []
        bwPatterns2Rule = {}

        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = copy_graph(graph)
        new_graph = makePreConditionPattern(new_graph)


        base_graph = copy_graph(new_graph)

        rewriter_graph = self.make_rewriter(return_graph)


        # get the ids of the structural nodes
        structure_nodes = find_nodes_with_mm(return_graph, ["MT_pre__MatchModel", "MT_pre__paired_with",
                                                            "MT_pre__ApplyModel", "MT_pre__match_contains",
                                                            "MT_pre__apply_contains"])
        structure_nums = [item.index for item in structure_nodes]
        rewriter_graph.delete_nodes(structure_nums)

        
        # remove apply classes not connected to any backward link
        apply_nums = []
        bk_links = find_nodes_with_mm(base_graph, ["MT_pre__trace_link"])
        bk_links_nums = [item.index for item in bk_links]

        has_contains = "MT_pre__apply_contains" in base_graph.vs["mm__"]

        if has_contains:
            apply_contains_nodes = find_nodes_with_mm(base_graph, ["MT_pre__apply_contains"])
            for node in apply_contains_nodes:
                apply_node = base_graph.neighbors(node,"out")[0]
                neighbors_apply_node = base_graph.neighbors(apply_node,"out")
                if set(neighbors_apply_node).intersection(bk_links_nums) == set():
                    apply_nums.append(apply_node)
        else:
            apply_model_node = find_nodes_with_mm(base_graph, ["MT_pre__ApplyModel"])[0]
            apply_nodes = base_graph.neighbors(apply_model_node, "out")
            for node in apply_nodes:
                neighbors_apply_node = base_graph.neighbors(node, "out")
                if set(neighbors_apply_node).intersection(bk_links_nums) == set():
                    apply_nums.append(node)

        structure_nodes = find_nodes_with_mm(base_graph, ["MT_pre__MatchModel", "MT_pre__paired_with",
                                                          "MT_pre__ApplyModel", "MT_pre__match_contains",
                                                          "MT_pre__apply_contains"])
        structure_nums = [item.index for item in structure_nodes]
        
        link_nodes = find_nodes_with_mm(base_graph, ["MT_pre__directLink_T", "MT_pre__indirectLink_T"])
        link_nums = [item.index for item in link_nodes]


        base_graph.delete_nodes(structure_nums + link_nums + apply_nums)
        
        if self.draw_svg:
            graph_to_dot("base_graph_" + base_graph.name, base_graph)
        

        rewrite_name = rewriter_graph.name + "_rule_combinator_rewriter"



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
        combinator_matchers = []
        
        if name in self.rulesNeedingOverlapTreatment:
            subsuming_rules = self.subsumingRules[name]
        
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


            #make a copy of the rewriter graph and the backward pattern
            rewriter_graph_copy = copy_graph(rewriter_graph)
            rewriter_graph_copy.pre = copy_graph(backward_pattern)
            rewriter_graph_copy.name = rewrite_name + "_" + str(i)
            
            file_name = rewriter_graph_copy.compile(out_dir)
            if self.verbosity >= 2:
                print("Rewriter graph compiled to: " + file_name)

            rewriter_graph2 = load_class(out_dir + rewriter_graph_copy.name)
            rewriter_graph2 = list(rewriter_graph2.values())[0]

            rewriter_graph2.pre = copy_graph(backward_pattern)


            if self.draw_svg:
                graph_to_dot(rewriter_graph2.name, rewriter_graph2)

            #append the new backward pattern and name mapping
            bwPatterns.append([matcher, Rewriter(rewriter_graph2)])
            #bwPatterns2Rule[matcher] = name 
            
        return {name: bwPatterns}


    def get_match_graph(self, graph):

        if self.draw_svg:
            graph_to_dot(graph.name + "_original", graph)

        has_contains = "apply_contains" in graph.vs["mm__"]

        apply_nodes = []

        if has_contains:
            for node in find_nodes_with_mm(graph, ["apply_contains"]):
                apply_nodes.extend(flood_find_nodes(node.index, graph, ["ApplyModel", "backward_link", "trace_link"]))
        else:

            for node in find_nodes_with_mm(graph, ["ApplyModel"]):
                apply_nodes.extend(flood_find_nodes(node.index, graph, ["paired_with", "backward_link", "trace_link"]))

        apply_nodes = list(set(apply_nodes))

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

        structure_nodes = find_nodes_with_mm(graph, ["paired_with", "ApplyModel", "apply_contains"])
        graph.delete_nodes(structure_nodes)

        return graph

    def make_rewriter(self, graph, back_to_trace = True):

        rewriter = copy_graph(graph)

        #Add trace links
        #add the MT_label__ as well
        rewriter = build_traceability(rewriter, add_label = True)

        rewriter = self.changeAttrType(rewriter, make_pre = False, back_to_trace = back_to_trace)

        rewriter = makePostConditionPattern(rewriter)

        return rewriter

    def get_match_pattern(self, rule):
        name = list(rule.keys())[0]
        graph = list(rule.values())[0]

        label = 0
        for i in range(len(graph.vs)):

            graph.vs[i]["MT_label__"] = str(label)
            label += 1
        
        out_dir = "./patterns/"

        graph = self.get_match_graph(graph)     
        
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False, back_to_trace = False)

        graph["mm__"] = [graph["mm__"][0], 'MoTifRule']
        graph["MT_constraint__"] = get_default_constraint()

        old_name = graph.name

        graph.name = old_name + "_match_pattern_matcher"
        file_name = graph.compile(out_dir)
        if self.verbosity >= 2:
            print("Match pattern matcher compiled to: " + file_name)

        if self.draw_svg:
            graph_to_dot(graph.name, graph)

        #have to reload the graph to define all the eval functions
        rule = load_class(out_dir + old_name + "_match_pattern_matcher")
        match_graph = list(rule.values())[0]

        matcher = Matcher(match_graph, disambig_matching = False)

        return {name : matcher}


    #ramify a whole directory
    #@do_cprofile
    def ramify_directory(self, dir_name, transformation_layers):

        #fix up directory to be relative if needed
        if not dir_name.startswith("/") and not dir_name.startswith("./"):
            dir_name = "./" + dir_name

        #add trailing slash if needed
        if not dir_name.endswith("/"):
            dir_name += "/"

        print("Ramifying directory: " + dir_name)
        self.transformation_layers = transformation_layers
        
        rules = {}
        
        backwardPatterns = {}
        matchRulePatterns = {}
        ruleCombinators = {}

        for layer in transformation_layers:
            for rule in layer:

                #add the rule to the rules dict
                rule2 = load_class(dir_name + rule.name)
                rules.update(rule2)

                #reload the rule
                #this is probably not needed
                #but there were problems with aliasing and copying

                #get the backwards pattern for this rule
                rule3 = load_class(dir_name + rule.name)
                (bwPattern, bwP2Rule) = self.get_backward_patterns(rule3)
                backwardPatterns.update(bwPattern)

                #fresh rule for the match pattern
                rule4 = load_class(dir_name + rule.name)
                matchRulePattern = self.get_match_pattern(rule4)
                matchRulePatterns.update(matchRulePattern)

        self.rules = rules

        subsumptionHandler = SubsumptionHandler(self.rules, self.transformation_layers)
        self.ruleSubsumption, self.subsumingRules = subsumptionHandler.calculate_rule_subsumption(matchRulePatterns)

        #record which rules have backward links
        has_backward_links = {}
        for rule in self.rules:
            has_backward_links[rule] = (backwardPatterns[rule] is not None)

        self.rulesNeedingOverlapTreatment = subsumptionHandler.get_rules_needing_overlap_treatment(has_backward_links)

        #build the combinators only after calculating the dependencies between rules
        for layer in transformation_layers:
            for rule in layer:

                # fresh rule for the rule combinators
                rule5 = load_class(dir_name + "/" + rule.name + ".py")
                rule_combinator = self.get_rule_combinators(rule5)
                ruleCombinators.update(rule_combinator)
       

        self.ruleSubsumption = subsumptionHandler.remove_subsumption_between_rules(self.ruleSubsumption, has_backward_links)

        loopingRuleSubsumption = subsumptionHandler.cleanLoopingRuleSubsumption()

        # print("Rules that need overlap treatment: " + str(self.rulesNeedingOverlapTreatment))
        # print("Subsumption order between rules for all layers: " + str(self.ruleSubsumption))
        # print("Rules fully overlapping with each other: " + str(subsumptionHandler.loopingRuleSubsumption))

        #raise Exception()

        print("\n")
        print("Finished PyRamify")
        print("==================================\n")                    

        return [rules, backwardPatterns, ruleCombinators, self.rulesNeedingOverlapTreatment, self.ruleSubsumption, loopingRuleSubsumption]


    #================================================================================



if __name__ == "__main__":
     #No default action
    pass



