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

    '''
     changeAttrType (M): Changes the type of attributes to 'string', which allows conditions and actions to be specified on attribute values in patterns.
     Also appends '__' to attributes starting with '__'. This is because the pLabel and pMatchSubtypes attributes (introduced in one of the next steps) need to be scoped appropriately for HOTs. 
     The first time a metamodel is ramified, each class will have a __pLabel and __pMatchSubtypes attribute.
     The next time, these attributes are renamed to ____pLabel and ____pMatchSubtypes, to allow a condition/action to be specified for the __pLabel and __pMatchSubtypes attributes which were introduced in the first RAMified metamodel.
    '''
    def changeAttrType(self, graph, make_pre = True):

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
                    
                elif "directLink" in node["mm__"] and attrib == "MT_pre__associationType":
                    node[attrib] = "if attr_value == \"" + node[attrib] + "\":\n    return True\nreturn False\n"
                    
                elif "Constant" in node["mm__"] and attrib == "MT_post__value":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "Attribute" in node["mm__"] and attrib == "MT_post__name":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "Constant" in node["mm__"] and attrib == "MT_post__name":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "directLink" in node["mm__"] and attrib == "MT_post__associationType":
                    node[attrib] = "return '" + node[attrib] + "'"
                    
                elif "paired_with" in node["mm__"] and attrib == "MT_post__rulename":
                    node[attrib] = "return '" + node[attrib] + "'"

                # Hack for trace_links
                elif "trace_link" in node["mm__"] and attrib == "MT_pre__type":
                    node[attrib] = None

                else:
                    #set the other values to the default match or rewrite code
                    if make_pre:
                        node[attrib] = get_default_match_code()
                    else:
                        node[attrib] = get_default_rewrite_code()

            #set some other attribs for the node
            if make_pre:
                node["MT_subtypeMatching__"] = False
                node["MT_subtypes__"] = "[]"
                node["MT_dirty__"] = False

        return graph
    
    
    '''
     changeAttrType (M): Changes the type of attributes to 'string', which allows conditions and actions to be specified on attribute values in patterns.
     Also appends '__' to attributes starting with '__'. This is because the pLabel and pMatchSubtypes attributes (introduced in one of the next steps) need to be scoped appropriately for HOTs. 
     The first time a metamodel is ramified, each class will have a __pLabel and __pMatchSubtypes attribute.
     The next time, these attributes are renamed to ____pLabel and ____pMatchSubtypes, to allow a condition/action to be specified for the __pLabel and __pMatchSubtypes attributes which were introduced in the first RAMified metamodel.
    '''
    def changeAttrTypeWithBack(self, graph, make_pre = True):

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

#                     if node["mm__"] == "backward_link":
#                         node["mm__"] = "trace_link"

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
                    
                elif "directLink" in node["mm__"] and attrib == "MT_pre__associationType":
                    node[attrib] = "if attr_value == \"" + node[attrib] + "\":\n    return True\nreturn False\n"
                    
                elif "Constant" in node["mm__"] and attrib == "MT_post__value":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "directLink" in node["mm__"] and attrib == "MT_post__associationType":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "Attribute" in node["mm__"] and attrib == "MT_post__name":
                    node[attrib] = "return '" + node[attrib] + "'"

                elif "Constant" in node["mm__"] and attrib == "MT_post__name":
                    node[attrib] = "return '" + node[attrib] + "'"

                # Hack for trace_links
                elif "trace_link" in node["mm__"] and attrib == "MT_pre__type":
                    node[attrib] = None

                else:
                    #set the other values to the default match or rewrite code
                    if make_pre:
                        node[attrib] = get_default_match_code()
                    else:
                        node[attrib] = get_default_rewrite_code()

            #set some other attribs for the node
            if make_pre:
                node["MT_subtypeMatching__"] = False
                node["MT_subtypes__"] = "[]"
                node["MT_dirty__"] = False

        return graph


    #RAMify this file
    def do_RAMify(self, graph, output_dir, remove_rule_nodes = True):
        
        input_name = graph["name"]
        #print("Starting to ramify file: " + input_name)


        #rename the class
        #graph["name"] = self.get_RAMified_name(input_name)

        #turn the backward links into trace links
        backwards_links = find_nodes_with_mm(graph, ["backward_link"])
        for node in backwards_links:
            node["mm__"] = "trace_link"

        #in some cases, the 'structural' or 'rule' nodes are removed
        if remove_rule_nodes is True:
            remove_nodes = find_nodes_with_mm(graph, ["MatchModel", "ApplyModel", "paired_with", "match_contains", "apply_contains", "directLink_T"])
            print("Removing rule nodes")
            graph.delete_nodes(remove_nodes)

        #
        # for n in graph.vs:
        #     if "Attribute" in n["mm__"]:
        #         print(n)

        #make sure this graph becomes a precondition pattern
        graph = makePreConditionPattern(graph)


        #change the attribs in this graph
        graph = self.changeAttrType(graph)


        #compile the output pattern for future study + use
        #throw everything in the output dir
        #graph.compile(output_dir)

        return graph


    #RAMify this file keeping backward links
    def do_RAMify_with_back(self, graph, output_dir, remove_rule_nodes = True):
        
        input_name = graph["name"]
        #print("Starting to ramify file: " + input_name)


        #rename the class
        #graph["name"] = self.get_RAMified_name(input_name)

#         backwards_links = find_nodes_with_mm(graph, ["backward_link"])
#         for node in backwards_links:
#             node["mm__"] = "trace_link"

        #in some cases, the 'structural' or 'rule' nodes are removed
        if remove_rule_nodes is True:
            remove_nodes = find_nodes_with_mm(graph, ["MatchModel", "ApplyModel", "paired_with", "match_contains", "apply_contains", "directLink_T"])
            print("Removing rule nodes")
            graph.delete_nodes(remove_nodes)

        #
        # for n in graph.vs:
        #     if "Attribute" in n["mm__"]:
        #         print(n)

        #make sure this graph becomes a precondition pattern
        graph = makePreConditionPattern(graph)


        #change the attribs in this graph
        graph = self.changeAttrTypeWithBack(graph)


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
        


    #very hacky
    #removes this attribute in the graph nodes
    def fix_attrs_for_backward_patterns(self, graph):
        # for node in graph.vs:
        #     try:
        #         del node["MT_pre__associationType"]
        #     except Exception:
        #         pass

        return graph

    # create the backward patterns for this file
    def get_backward_patterns(self, rule):
        if self.verbosity >= 2:
            print("\nStarting get backward patterns")
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]

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

        graph = copy.deepcopy(graph)
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

        #get the ids of the structural nodes
        structure_nodes = find_nodes_with_mm(graph, ["MT_pre__MatchModel", "MT_pre__paired_with", "MT_pre__ApplyModel", "MT_pre__match_contains", "MT_pre__apply_contains"])
        structure_nums = [get_node_num(graph, item) for item in structure_nodes]


        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = copy.deepcopy(graph)
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


        #BIG HACK
        new_graph = self.fix_attrs_for_backward_patterns(new_graph)


        file_name = new_graph.compile(out_dir)

        if self.verbosity >= 2:
            print("Backward patterns compiled to: " + file_name)

        rule = load_class(out_dir + "/" + new_name)
        backward_pattern = rule[rule.keys()[0]]

        if self.draw_svg:
            graph_to_dot(new_name, backward_pattern)

        #create the Matcher
        matcher = Matcher(backward_pattern)

        #append the new backward pattern and name mapping
        bwPatterns.append(matcher)
        #bwPatterns2Rule[matcher] = name

        return [{str(return_graph.name): matcher}, bwPatterns2Rule]


    def get_links_in_apply(self, graph):
        # find the apply_contains
        apply_contains = self.find_nodes_with_mm(graph, ["MT_pre__apply_contains"])


        # find the backward links
        backwards_links = self.find_nodes_with_mm(graph, ["MT_pre__trace_link"])


        #find node nums attached to a backward link
        attached_to_backward_links = []
        for bl in backwards_links:
            attached_to_backward_links += self.look_for_attached(bl, graph)

        nodes_to_delete = []
        nodes_to_keep = []

        #look at the apply_contains link
        for apply_contain in apply_contains:
            #find the attached nodes to this link
            apply_attached_nodes = self.look_for_attached_of_attached(apply_contain, graph)


            #for the nodes
            for aan in apply_attached_nodes:
                #get the node
                node = graph.vs[aan]
                #print(node)

                if aan in attached_to_backward_links:
                    #this node is attached to a backward link, so keep it
                    nodes_to_keep.append(aan)
                elif str(node["mm__"]) not in ["MT_pre__ApplyModel", "MT_pre__apply_contains", "MT_pre__paired_with", "MT_pre__hasAttribute_T"]:
                    #don't remove important nodes, but delete all others
                    nodes_to_delete.append(node)


        #find all the hasAttribute nodes of the apply side
        hasAttributeNodes = self.find_nodes_with_mm(graph, ["MT_pre__hasAttribute_T"])
        for n in hasAttributeNodes:

            #look at all the attached nodes to the hasAttribute node
            attached = self.look_for_attached(n, graph)

            #keep this hasAttribute node if it is connected to a node that is connected to a backward link
            should_keep_attrib = False
            for a in attached:
                if a in nodes_to_keep:
                    should_keep_attrib = True

            #otherwise, delete this hasAttribute node and the attached nodes as well
            if not should_keep_attrib:
                nodes_to_delete.append(n)
                nodes_to_delete += attached

        #print("Nodes to delete: " + str(len(nodes_to_delete)))
        return nodes_to_delete


    def get_all_links(self, graph):
        pass
    
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

    # create the backward patterns for this file
    def get_rule_combinators(self, rule):

        if self.verbosity >= 2:
            print("\nStarting to get rule combinators")
        name = rule.keys()[0]
        graph = rule.values()[0]

        label = 0
        for i in range(len(graph.vs)):
            graph.vs[i]["MT_label__"] = str(label)
            label += 1

        return_graph = copy_graph(graph)

        # check to see which nodes have backward links
        backwards_links = find_nodes_with_mm(graph, ["backward_link"])

        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return {name: None}
        
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
        nodes_w_eqs = self.get_all_nodes_with_equations(base_graph)

        remove_nodes = []
        keep_nodes = []
        for n in nodes_w_eqs.keys():
            
            #node_num = self.get_node_num(graph, n)
            connected = look_for_attached(n, base_graph)

            in_match = False
            in_apply = False
            backward_link = False
            
            for c in connected:
                if graph.vs[c]["mm__"] == "MT_pre__match_contains":
                    in_match = True
                    keep_nodes.append(n)
                elif graph.vs[c]["mm__"] == "MT_pre__apply_contains":
                    in_apply = True
                elif graph.vs[c]["mm__"] == "MT_pre__trace_link":
                    backward_link = True
                    
            if in_apply and not backward_link:
                remove_nodes += nodes_w_eqs[n]
                
#         print("Keep nodes: ")
#         for k in keep_nodes:
#             print(k["mm__"])
            
        #print("Remove nodes: ")
        #for r in remove_nodes:
            #print(r["mm__"])
            
        for k in keep_nodes:
            
            k_num = get_node_num(base_graph, k)
            try:
                remove_nodes.remove(k_num)
            except Exception:
                pass


        base_graph.delete_nodes(remove_nodes)

        
        # # turn the backward links into trace links
        #
        # backwards_links2 = self.find_nodes_with_mm(rewriter_graph, ["backward_link"])
        # #print(backwards_links2)
        #
        # for node in backwards_links2:
        #      node["mm__"] = "trace_link
        
        

        structure_nodes = find_nodes_with_mm(base_graph, ["MT_pre__MatchModel", "MT_pre__paired_with",
                                                          "MT_pre__ApplyModel", "MT_pre__match_contains",
                                                          "MT_pre__apply_contains"])
        structure_nums = [get_node_num(base_graph, item) for item in structure_nodes]
        
        link_nodes = find_nodes_with_mm(base_graph, ["MT_pre__directLink_T", "MT_pre__indirectLink_T"])
        link_nums = [get_node_num(base_graph, item) for item in link_nodes]


        base_graph.delete_nodes(structure_nums + link_nums)
        
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

        nodes_w_eqs = self.get_all_nodes_with_equations(base_graph)

        
        input_nodes = []
        for n in nodes_w_eqs.keys():
            
            #print("Node w eqs: " + str(n["mm__"]))
            #print(nodes_w_eqs)
            
            #node_num = self.get_node_num(graph, n)
            connected = look_for_attached(n, base_graph)
            #print("Connected: " + str(connected))

            backward_link = False
            
            for c in connected:
                #print("Connected to: " + base_graph.vs[c]["mm__"])
                if base_graph.vs[c]["mm__"] == "MT_pre__trace_link":
                    #print("Connected to backward link")
                    backward_link = True
                    
            if not backward_link:
                temp_array = []
                
                for actual_node in nodes_w_eqs[n]:
                    temp_array.append(base_graph.vs[actual_node])
                    
                input_nodes.append(nodes_w_eqs[n])
        # #TODO: Handled by attr changing?
        #

        #get the list of nodes to remove
        #(which is all nodes that should not be kept)
#         nodes_to_remove = range(len(base_graph.vs))
# #        nodes_to_remove = [new_graph.vs[item] for item in nodes_to_remove if item not in nodes_to_keep]
# 
#         nodes_to_keep = []
#         match_contains = self.find_nodes_with_mm(base_graph, ["MT_pre__match_contains"])
#         for mc in match_contains:
#             mc_num = self.get_node_num(base_graph, mc)
#             nodes_to_keep += self.flood_find_nodes(mc_num, base_graph, ["MT_pre__MatchModel", "MT_pre__apply_contains", "MT_pre__directLink_T", "MT_pre__indirectLink_T"])
#         
#         nodes_to_keep = list(set(nodes_to_keep))
#         
#         #attribute_nodes = self.find_nodes_with_mm(base_graph, ["MT_pre__hasAttr_S", "MT_pre__hasAttribute_S","MT_pre__hasAttr_T", "MT_pre__hasAttribute_T", "MT_pre__Attribute"])
#         #nodes_to_keep += [self.get_node_num(base_graph, item) for item in attribute_nodes]
# 
#         # don't consider removing the backward links and attached nodes
#         for n in nodes_to_keep:
#             nodes_to_remove.remove(n)
#             
#         #delete all match contains
#         #nodes_to_remove += self.find_nodes_with_mm(graph, ["MT_pre__match_contains"])
#         nodes_to_remove = list(set(nodes_to_remove))
# 
#         #base_graph.delete_nodes(nodes_to_remove)
#         print("Removed nodes")
#         
#         
# 
#         print("Made base graph")

        #print("Nodes to remove: " + str(nodes_to_remove))
        #print("Types:")
        #for n in nodes_to_remove:
        #    print(base_graph.vs[n]["mm__"])

        #knock nodes out of the base graph to create the matchers
        #nodes_to_remove

        #print("Length: " + str(len(input_nodes)))
        #print(input_nodes)
        #input nodes stores the node numbers for the nodes you want to knock out of the base graph
        output = sum([map(list, combinations(input_nodes, i)) for i in range(len(input_nodes) + 1)], [])
        #output = []
        
        
        
        
        #print(input_nodes)
        #print(output)


        # change the attribs in this graph
        #rewriter_graph = self.changeAttrType(rewriter_graph, False)

#        print("Rule combinators: Generating " + str(len(output)) + " different possibilities")


        rewrite_name = rewriter_graph.name + "_rule_combinator_rewriter"

        levis_tiny_hack = True
        if levis_tiny_hack and len(output) > 1:
            output = [output[0], output[-1]]


        # LEVI: we only need the total and the partial combinator.
        # the total combinator includes all the base graph as match and no NAC.
        # the partial combinator includes only the backward links, and has as NAC the remaining base graph.
        # FOR BENTLEY: I have changed the loop going through all the combinations of match nodes
        # such that we only have these two combinators.
        
        # first build the total combinator (just the base graph)        
        total_combinator_matcher = copy_graph(base_graph)
        
        # now build the partial combinator by removing everything except for the backward links
        partial_combinator_matcher = copy_graph(base_graph)
        
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
        
        combinator_matchers = [partial_combinator_matcher, total_combinator_matcher]
        
        #graph_to_dot("combinator_after" + base_graph.name, partial_combinator_matcher) 
        
        #write out the combinator
        
        for i in range(len(combinator_matchers)):
            
            #create a new name for this backward matcher
            #replace the pattern name with the partial pattern name
            new_name = combinator_matchers[i].name + "_rule_combinator_matcher_" + str(i)
            
            combinator_matchers[i].name = new_name
            combinator_matchers[i]["name"] = new_name + "_rc_matcher"    
    
            #BIG HACK
            combinator_matchers[i] = self.fix_attrs_for_backward_patterns(combinator_matchers[i])
    
            file_name = combinator_matchers[i].compile(out_dir)
            if self.verbosity >= 2:
                print("Rule combinator matcher compiled to: " + file_name)
    
            rule = load_class(out_dir + "/" + new_name)
            
            # debug printout
            if self.draw_svg:
                graph_to_dot(combinator_matchers[i].name, combinator_matchers[i])
            
            backward_pattern = rule.values()[0]
            
            if i == 0:
                # now build the NAC for the first combinator (just the complete base graph) 
                
                NAC_graph = copy_graph(base_graph)
                NAC_graph = makePreConditionPatternNAC(NAC_graph)
                NAC_graph.name += "_rule_combinator_NAC"
                
                NAC_graph.LHS = backward_pattern
                
                file_name = NAC_graph.compile(out_dir)
                if self.verbosity >= 2:
                    print("Nac graph compiled to: " + file_name)
                
                NAC_graph = load_class(out_dir + NAC_graph.name, [backward_pattern])
                NAC_graph = NAC_graph.values()[0]
                
                # debug printout
                if self.draw_svg:
                    graph_to_dot(NAC_graph.name, NAC_graph)
                       
                backward_pattern.NACs = [NAC_graph]

            #create the Matcher
            matcher = Matcher(backward_pattern)
 
 
            #TODO: Make rewriter code simpler, and same as match pattern rewriter
 
            rewriter_graph_copy = copy_graph(rewriter_graph)
 
            rewriter_graph_copy.pre = copy_graph(backward_pattern)
            #graph_to_dot(rewriter_graph_copy.pre.name + "_pre", rewriter_graph_copy.pre)
 
 
            rewriter_graph_copy.name = rewrite_name + "_" + str(i)
            file_name = rewriter_graph_copy.compile(out_dir)
            if self.verbosity >= 2:
                print("Rewriter graph compiled to: " + file_name)
            
            
 
            rewriter_graph2 = load_class(out_dir + rewriter_graph_copy.name)
            rewriter_graph2 = rewriter_graph2.values()[0]
 
            # print(inspect.getargspec(rewriter_graph2.execute))
            # print(rewriter_graph2.__class__)
            # print(rewriter_graph2.name)
            # print("Hierarchy:")
            # print(inspect.getmro(rewriter_graph2.__class__))
 
            # debug printout
            if self.draw_svg:
                graph_to_dot(rewriter_graph2.name, rewriter_graph2)
 
            rewriter_graph2.pre = copy_graph(backward_pattern)
 
 
            #rewrite_name = rewriter_graph2.name
            #rewriter_graph2.name += "_loaded_rewriter"
            #rewriter_graph2.compile("./patterns")
            #rewriter_graph2.name = rewrite_name
 
            rewriter_graph2.pre = copy_graph(backward_pattern)
 
            for n in range(len(rewriter_graph2.pre.vs)):
                node = rewriter_graph2.pre.vs[n]
                #print("mm2__: " + node["mm__"])
 
            rewriter = Rewriter(rewriter_graph2)
 
 
            #append the new backward pattern and name mapping
            bwPatterns.append([matcher, rewriter])
            #bwPatterns2Rule[matcher] = name

        return {name: bwPatterns}        
        
#         
#         
#         
#         remove_set = output[1]
#         
#         to_remove = []
#         #flatten the list of nodes to remove
#         for r in remove_set:
#         #remove everything except for the attached nodes and the backward link
#             to_remove += r
#                     
#         print "<--------------------------->"
#         print to_remove
#         for l in remove_set:
#             print partial_combinator_matcher.vs[l[0]]["mm__"]
#         print "<--------------------------->"        
#         
#         partial_combinator_matcher.delete_nodes(to_remove)
#         
#         graph_to_dot("combinator_before" + base_graph.name, partial_combinator_matcher)        
#         
#         # remove also all the indirect and direct links attached to the nodes to remove
# 
#         remove_links = []
# 
#         for n in partial_combinator_matcher.vs:
#              
#             if not ("directLink" in n["mm__"] or "indirectLink" in n["mm__"]):
#                 continue
#              
#             print "going in..."     
#             connected = self.look_for_attached(n, partial_combinator_matcher)
#             # remove only dangling links, that are not connected to two nodes
#             print str(len(connected))
#             if len(connected) < 3:
#                 remove_links.append(n)
#         
#         print remove_links
#               
#         partial_combinator_matcher.delete_nodes(remove_links)        
#         
#         # finally remove all the equation-related nodes
#         
#         partial_combinator_matcher = self.remove_pre_equation_nodes(partial_combinator_matcher)
# 
#         graph_to_dot("combinator_after" + base_graph.name, partial_combinator_matcher)        
        
        
#         #BIG HACK
#         new_graph = self.fix_attrs_for_backward_patterns(new_graph)
# 
#         file_name = new_graph.compile(out_dir)
#         print("Rule combinator matcher compiled to: " + file_name)
# 
#         rule = load_class(out_dir + "/" + new_name)
#         backward_pattern = rule.values()[0]
# 
#         j = 0
#         for remove_set in reversed(output):
# 
#             new_graph = self.copy_graph(base_graph)
# 
# 
#             print("Remove set")
#             print(remove_set)
#             
#             to_remove = []
#             for r in remove_set:
#             #remove everything except for the attached nodes and the backward link
#                 to_remove += r
#                 
#                 
#             graph_to_dot(new_graph.name + "_before", new_graph)    
#                                
#             new_graph.delete_nodes(to_remove)
# 
# 
#             #delete links that are not connected to two nodes
#             remove_links = []
#             for n in new_graph.vs:
#                 
#                 if not ("directLink" in n["mm__"] or "indirectLink" in n["mm__"]):
#                     continue
#                      
#                 connected = self.look_for_attached(n, base_graph)
#                 if len(connected) < 3:
#                     remove_links.append(n)
#                     
#             new_graph.delete_nodes(remove_links)
#             
#             graph_to_dot(new_graph.name + "_after", new_graph)            
#             
#             
# 
#             remove_set = to_remove + remove_links
#             
#             
# 
#             #create the matcher
# 
#             j += 1
# 
#             #create a new name for this backward matcher
#             #replace the pattern name with the partial pattern name
#             new_name = name + "_rule_combinator_matcher_" + str(i)
#             i += 1
# 
#             #write out the file
#             new_graph.name = new_name
#             new_graph["name"] = new_name + "_rc_matcher"
# 
# 
#             #BIG HACK
#             new_graph = self.fix_attrs_for_backward_patterns(new_graph)
# 
#             file_name = new_graph.compile(out_dir)
#             print("Rule combinator matcher compiled to: " + file_name)
# 
#             rule = load_class(out_dir + "/" + new_name)
#             backward_pattern = rule.values()[0]
# 
# 
#             #graph_to_dot(new_name, backward_pattern)
#             #graph_to_dot("remove_graph" + str(j), new_graph)
# 
# 
# 
#             if remove_set == []:
#                 backward_pattern.NACs = []
#             else:
# 
#                 NAC_nodes_to_remove = []
# 
#                 for node_to_remove in to_remove:
#                     node = base_graph.vs[node_to_remove]
#                     if node["mm__"] in ["MT_pre__indirectLink_S", "MT_pre__indirectLink_T", "MT_pre__directLink_S", "MT_pre__directLink_T"] \
#                         and not node in to_remove:
#                         NAC_nodes_to_remove.append(node_to_remove)
# 
#                 #create the NAC if needed
#                 NAC_graph = self.copy_graph(base_graph)
# 
#                 NAC_graph.delete_nodes(NAC_nodes_to_remove)
# 
# 
#                 NAC_graph = self.makePreConditionPatternNAC(NAC_graph)
# 
#                 NAC_graph.name += "_rule_combinator_NAC"
# 
#                 NAC_graph.LHS = backward_pattern
# 
#                 file_name = NAC_graph.compile(out_dir)
#                 print("Nac graph compiled to: " + file_name)
# 
#                 NAC_graph = load_class(out_dir + NAC_graph.name, [backward_pattern])
#                 NAC_graph = NAC_graph.values()[0]
# 
# 
#                 backward_pattern.NACs = [NAC_graph]
# 
#             #create the Matcher
#             matcher = Matcher(backward_pattern)
# 
# 
#             #TODO: Make rewriter code simpler, and same as match pattern rewriter
# 
#             rewriter_graph_copy = self.copy_graph(rewriter_graph)
# 
#             rewriter_graph_copy.pre = self.copy_graph(backward_pattern)
#             #graph_to_dot(rewriter_graph_copy.pre.name + "_pre", rewriter_graph_copy.pre)
# 
# 
#             rewriter_graph_copy.name = rewrite_name + "_" + str(j)
#             file_name = rewriter_graph_copy.compile(out_dir)
#             print("Rewriter graph compiled to: " + file_name)
# 
#             rewriter_graph2 = load_class(out_dir + rewriter_graph_copy.name)
#             rewriter_graph2 = rewriter_graph2.values()[0]
# 
#             # print(inspect.getargspec(rewriter_graph2.execute))
#             # print(rewriter_graph2.__class__)
#             # print(rewriter_graph2.name)
#             # print("Hierarchy:")
#             # print(inspect.getmro(rewriter_graph2.__class__))
# 
#             #graph_to_dot(rewriter_graph2.name + "_loaded_rewriter", rewriter_graph2)
# 
#             rewriter_graph2.pre = self.copy_graph(backward_pattern)
# 
# 
#             #rewrite_name = rewriter_graph2.name
#             #rewriter_graph2.name += "_loaded_rewriter"
#             #rewriter_graph2.compile("./patterns")
#             #rewriter_graph2.name = rewrite_name
# 
#             rewriter_graph2.pre = self.copy_graph(backward_pattern)
# 
#             for n in range(len(rewriter_graph2.pre.vs)):
#                 node = rewriter_graph2.pre.vs[n]
#                 #print("mm2__: " + node["mm__"])
# 
#             rewriter = Rewriter(rewriter_graph2)
# 
# 
#             #append the new backward pattern and name mapping
#             bwPatterns.append([matcher, rewriter])
#             #bwPatterns2Rule[matcher] = name
# 
#             #print("bwPatterns: " + str(bwPatterns))
#             print("Returning from rule combinators")
#        return {name: bwPatterns}


    def remove_equation_nodes(self, graph):        
        
        eq_nodes = find_nodes_with_mm(graph, ["Equation"])
        nodes_to_remove = []
        for eq in eq_nodes:
            eq_num = get_node_num(graph, eq)
            equation_attrib_nodes = flood_find_nodes(eq_num, graph, None, ["Attribute", "Constant"])
            equation_attrib_nodes = [node for node in  equation_attrib_nodes if graph.vs[node]["mm__"] == "Attribute"]
#            print "---------------- " + str(eq_num) + " -----------------------> Number of attribute nodes: " + str(len(equation_attrib_nodes))
            
            # equation is between an attribute of the match model and an attribute of the apply model
            if len(equation_attrib_nodes) >= 2:
                nodes_to_remove += flood_find_nodes(eq_num, graph, None, ["hasAttribute_S", "hasAttribute_T"])
#                print flood_find_nodes(eq_num, graph, None, ["hasAttribute_S", "hasAttribute_T"])
            # check if the equation is part of the elements of the apply model and remove it in that case
            # don't remove the equation if it is part of the elements of the match model
            else:
                nodes_equation_is_connected_to = flood_find_nodes(equation_attrib_nodes[0], graph, ["paired_with", "backward_link","Equation"])         
                for node in nodes_equation_is_connected_to:
                    if graph.vs[node]["mm__"] == "ApplyModel":
                        nodes_to_remove += flood_find_nodes(eq_num, graph, ["Attribute"])
                
        nodes_to_remove = list(set(nodes_to_remove))

        graph.delete_nodes(nodes_to_remove)
        return graph

    def remove_structure_nodes(self, graph):
        structure_nodes = find_nodes_with_mm(graph, ["MatchModel", "match_contains", "paired_with", "ApplyModel", "apply_contains"])
        graph.delete_nodes(structure_nodes)
        return graph




    def get_match_graph(self, graph):

        if self.draw_svg:
            graph_to_dot(graph.name + "_original", graph)
        graph = self.remove_equation_nodes(graph)

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


        rewriter = self.changeAttrType(rewriter, False)

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

        rewriter = self.changeAttrTypeWithBack(rewriter, False)

        rewriter = makePostConditionPattern(rewriter)

        #graph_to_dot("the_rewriter_graph_after_post_" + rewriter.name, rewriter)


        return rewriter

    def get_match_pattern(self, rule):
    
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]

        label = 0
        for i in range(len(graph.vs)):

            graph.vs[i]["MT_label__"] = str(label)
            label += 1

        rewriter = self.make_rewriter_with_back(graph)
        
        out_dir = "./patterns/"

        graph = self.get_match_graph(graph)     
        
        graph = self.do_RAMify_with_back(graph, out_dir, remove_rule_nodes = False)

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
        match_graph = rule.values()[0]


        rewriter.pre = match_graph
        rewriter.name = old_name + "_match_pattern_rewriter"
        #graph_to_dot("the_rewriter_graph" + rewriter.name, rewriter)

        file_name = rewriter.compile(out_dir)
        if self.verbosity >= 2:
            print("Match pattern rewriter compiled to: " + file_name)

        rewriter_dict = load_class(out_dir + rewriter.name)
        rewriter = rewriter_dict.values()[0]

        #graph_to_dot("the_rewriter_graph_after" + rewriter.name, rewriter)

        return {name : [Matcher(match_graph), Rewriter(rewriter)]}

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
        for ruleKey in self.ruleSubsumption.keys():
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
        
        ruleObjects = []
        ruleKeys = self.rules.keys()
        for key in ruleKeys:
            ruleObjects.append(key)
            
        rulepairs = list(permutations(ruleObjects,2))
        
        ruleSubsumption = {}
        for pair in rulepairs:
            p = Packet()
            p.graph = self.rules[pair[1]]
            p = matchRulePatterns[pair[0]][0].packet_in(p)
            if matchRulePatterns[pair[0]][0].is_success:
                # the partial order may branch, so we need lists to store the smaller elements
                if pair[1] not in ruleSubsumption.keys():
                    ruleSubsumption[pair[1]] = [pair[0]]
                else:
                    ruleSubsumption[pair[1]].append(pair[0])                   
            
        return ruleSubsumption


    # return the layer a rule occurs in
    def layer_rule_occurs_in(self, rule):
        for layerIndex in range(len(self.transformation_layers)):
            if self.rules[rule] in self.transformation_layers[layerIndex]:
                return layerIndex
        return None
        

    # Calculate if the rules need special treatment because they overlap.
    # This happens when:
    # - Rule A is subsumed by Rule B, rule A has no backward links and Rule B appears in the same layer as rule A, or in a layer before
    # - Rule A is subsumed by rule B and both rule A and rule B have backward links
    # returns a list of pairs of rules for which combinators need to be built for
    def rules_needing_overlap_treatment(self):
        rules_needing_overlap_treatment = []
        for rule in self.rules.keys():            
            subsuming_rules = self.get_subsuming_rules(rule)
            for s_rule in subsuming_rules:
                if (not self.rule_has_backward_links(rule) and not self.rule_has_backward_links(s_rule)) or\
                   (self.rule_has_backward_links(rule) and not self.rule_has_backward_links(s_rule)):
                    if self.layer_rule_occurs_in(rule) >= self.layer_rule_occurs_in(s_rule):
                        rules_needing_overlap_treatment.append((self.rules[rule],s_rule))
                        
                elif (self.rule_has_backward_links(rule) and self.rule_has_backward_links(s_rule)):
                    if self.layer_rule_occurs_in(rule) == self.layer_rule_occurs_in(s_rule):
                        rules_needing_overlap_treatment.append((rule,s_rule))
        
        return rules_needing_overlap_treatment              
                    
    

    # get all the rules in the transformation 
    def get_rules(self, dir_name):
        print("Ramifying directory: " + dir_name)
        
        rules = {}
        
        #examine all the files in this dir
        for f in os.listdir(dir_name):

            #skip these files
            if not f.endswith(".py") or f == "__init__.py" or os.path.isdir(dir_name + "/" + f):
                continue

            print("\nFile: " + f)

            #add the rule to the rules dict
            rule = load_class(dir_name + "/" + f)
            rules.update(rule)
            
        self.rules = rules

        return rules


    #ramify a whole directory
    def ramify_directory(self, dir_name, transformation_layers):
        print("Ramifying directory: " + dir_name)
        
        self.transformation_layers = transformation_layers
        
        rules = {}
        
        backwardPatterns = {}
        backwardPatterns2Rules = {}
        backwardPatternsComplete = {}
        matchRulePatterns = {}
        ruleCombinators = {}

        #examine all the files in this dir
        for f in os.listdir(dir_name):

            #skip these files
            if not f.endswith(".py") or f == "__init__.py" or os.path.isdir(dir_name + "/" + f):
                continue

            print("File: " + f)

            #add the rule to the rules dict
            rule = load_class(dir_name + "/" + f)
            rules.update(rule)

            #reload the rule
            #this is probably not needed
            #but there were problems with aliasing and copying

            #get the backwards pattern for this rule
            rule3 = load_class(dir_name + "/" + f)
            (bwPattern, bwP2Rule) = self.get_backward_patterns(rule3)
            backwardPatterns.update(bwPattern)

            if not bwP2Rule is None:
                backwardPatterns2Rules.update(bwP2Rule)

            #fresh rule for the match pattern
            rule4 = load_class(dir_name + "/" + f)
            matchRulePattern = self.get_match_pattern(rule4)
            matchRulePatterns.update(matchRulePattern)

            # fresh rule for the rule combinators
            rule5 = load_class(dir_name + "/" + f)
            rule_combinator = self.get_rule_combinators(rule5)
            ruleCombinators.update(rule_combinator)
            
        self.ruleSubsumption = self.calculate_rule_subsumption(matchRulePatterns)
            
#         if self.verbosity >= 2:
#             print "Subsumption order between rules for all layers:"                   
#             print ruleSubsumption
#             print "\n"

        print "Subsumption order between rules for all layers:"    
        print self.ruleSubsumption
        for ruleName in rules.keys():
            print ruleName + ": " +str(self.get_subsuming_rules(ruleName))
        print "Rules that need overlap treatment: " + str(self.rules_needing_overlap_treatment())            
            

        print("Finished PyRamify")
        print("==================================\n")

        return [rules, backwardPatterns, backwardPatterns2Rules, {}, matchRulePatterns, ruleCombinators]


    #================================================================================


    #renames elements from one metamodel into another metamodel
    def changeGraphMetamodel(self, mapping, directory):
        print("Starting to rename elements in graphs")
        #print("Mapping: " + str(mapping))

        for d in os.listdir(directory):
            if not os.path.isdir(directory + d):
                continue

            # ignore svn dirs
            if d.startswith('.'):
                continue

            graph_dir = directory + d + "/Himesis/"

            try:
                files = os.listdir(graph_dir)
            except OSError:
                print("Warning: " + graph_dir + " does not exist")
                files = []

            for f in files:


                if f == "__init__.py" or not f.endswith(".py") or f.startswith("."):
                    continue

                #print("Examining " + graph_dir + f)

                graph_file = graph_dir + f
                try:
                    g = load_class(graph_file)
                except ImportError:
                    print("ERROR " + graph_file)
                    continue

                name = g.keys()[0]
                graph = g.values()[0]

                for node in graph.vs:
                    if not node["mm__"] in mapping.keys():
                        continue

                    #set the new subtypes
                    node["mm__"] = mapping[node["mm__"]]

                #need to compile rule back in order to update the file
                graph.compile(graph_dir)

        print("Finished changing graph metamodels\n")

    #change the proper prover matchers and rewriters to
    #refer to the correct metamodel
    def changePropertyProverMetamodel(self, pre_metamodel, post_metamodel, subclasses_dict, dsltransInstallDir = "."):
        print("Starting to change property prover metamodel")

        property_prover_rules_dir = dsltransInstallDir + "/property_prover_rules/"
        for d in os.listdir(property_prover_rules_dir):

            if not os.path.isdir(property_prover_rules_dir + d):
                continue

            #ignore svn dirs
            if d.startswith('.'):
                continue

            rule_dir = property_prover_rules_dir + d + "/Himesis/"

            try:
                files = os.listdir(rule_dir)
            except OSError:
                print("Warning: " + rule_dir + " does not exist")
                files = []

            for f in files:
                if f == "__init__.py" or not f.endswith(".py") or f.startswith("."):
                    continue

                rule_file = rule_dir + f
                try:
                    rule = load_class(rule_file)
                except ImportError as e:
                    print("ERROR loading " + rule_file)
                    traceback.print_exc()
                    continue

                name = rule.keys()[0]
                graph = rule[rule.keys()[0]]

                #TODO: Make this less fragile
                if "LHS" in f:
                    graph["mm__"] = pre_metamodel
                elif "RHS" in f:
                    graph["mm__"] = post_metamodel
                else:
                    raise Exception("Error: Not LHS or RHS rule")

                for node in graph.vs:

                    #the node doesn't match subtypes
                    if "MT_subtypeMatching__" in node.attributes().keys() and node["MT_subtypeMatching__"] == False:
                        continue

                    #the node does look at subtypes
                    if "MT_subtypes__" in node.attributes().keys() and len(node["MT_subtypes__"]) >= 1:

                        # we are not changing this mm's subtypes
                        if not node["mm__"] in subclasses_dict.keys():
                            continue

                        #set the new subtypes
                        node["MT_subtypes__"] = subclasses_dict[node["mm__"]]

                #need to compile rule back in order to update the file
                graph.compile(rule_dir)

        print("Finished changing property prover metamodel\n")

if __name__ == "__main__":
     #No default action
    pass



