#!/bin/python
import re
import sys
import os
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from himesis_utils import *
#from ramify_actions import *

from core.himesis import *
from itertools import combinations
import inspect


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

    def __init__(self):

        #keep track of the next label to give a graph node
        self.next_label = 0
        

    #get the id number of a node in the graph
    #hacky, as this is based on the node's attributes
    def get_node_num(self, graph, node):
        for i in range(len(graph.vs)):
            if graph.vs[i].attributes() == node.attributes():
                return i
        return -1

    #=========================
    #look for the nodes attached to the node number 'num'
    #used to find backward links
    def look_for_attached(self, link, graph):
        attached_node_nums = []
        
        
        #hacky way of finding the index of the node
        node_num = self.get_node_num(graph, link)
                
        if node_num == -1:
            print("Error: no link found")
        
        #check the edge list to see if there are attached edges
        for edge in graph.get_edgelist():
            
            if node_num == edge[0]:
               attached_node_nums.append(edge[1])
            elif node_num == edge[1]:
               attached_node_nums.append(edge[0])
        
        attached_node_nums.append(node_num)
        
        return attached_node_nums

    #do a lookup of the nodes that are attached to
    #the nodes attached to this link
    def look_for_attached_of_attached(self, link, graph):
        attached_of_attached = []
        attached = self.look_for_attached(link, graph)

        for a in attached:
            attached_of_attached += self.look_for_attached(graph.vs[a], graph)

        return list(set(attached_of_attached))





    #Very hacky way of making the graph a HimesisPreConditionPatternLHS
    def makePreConditionPattern(self, graph):
        
        #force the class to be different
        graph.__class__ = HimesisPreConditionPatternLHS
        

        #variables added in subclasses

        #from HimesisPattern
        graph.nodes_label = {}
        graph.nodes_pivot_out = {}
        
        #from HimesisPreConditionPattern
        graph.nodes_pivot_in = {}
        
        #from HimesisPreConditionPatternLHS
        graph.import_name = 'HimesisPreConditionPatternLHS'
        graph.NACs = []

        return graph

    def makePreConditionPatternNAC(self, graph):

        graph = self.makePreConditionPattern(graph)

        graph.__class__ = HimesisPreConditionPatternNAC

        graph.LHS = None
        graph.bridge = None
        graph.init_params.append('LHS')
        graph.import_name = 'HimesisPreConditionPatternNAC'

        return graph


    def makePostConditionPattern(self, old_graph):
        graph = copy.deepcopy(old_graph)

        # force the class to be different
        graph.__class__ = HimesisPostConditionPattern

        # variables added in subclasses

        #from HimesisPattern
        graph.nodes_label = {}
        graph.nodes_pivot_out = {}

        #from HimesisPostConditionPattern
        graph.pre = None
        graph.import_name = 'HimesisPostConditionPattern'

        return graph


    #FIXME to be proper
    #could be smarter depending on the type
    def copy_graph(self, graph2):
        graph1 = copy.deepcopy(graph2)

        try:
            graph1.nodes_label = copy.deepcopy(graph2.nodes_label)
        except AttributeError:
            pass

        try:
            graph1.nodes_pivot_out = copy.deepcopy(graph2.nodes_pivot_out)
        except AttributeError:
            pass




        try:
            graph1.nodes_pivot_in = copy.deepcopy(graph2.nodes_pivot_in)
        except AttributeError:
            pass


        graph1.import_name = copy.deepcopy(graph2.import_name)

        try:
            graph1.NACs = copy.deepcopy(graph2.NACs)
        except AttributeError:
            pass


        try:
            graph1.pre = self.copy_graph(graph2.pre)
        except AttributeError:
            pass

        return graph1

    #the default eval match code
    #use to build the matchers
    def get_default_match_code(self):

        return """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""

    def get_default_rewrite_code(self):
        return """
#===============================================================================
# You can access the value of the current node's attribute value by: attr_value.
# If the current node shall be created you MUST initialize it here!
# You can access a node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# Note that the attribute values are those before the match is rewritten.
# The order in which this code is executed depends on the label value
# of the encapsulating node.
# The given action must return the new value of the attribute.
#===============================================================================

return attr_value
"""

    #the default constraint for each attribute
    #as in the bottom of matchers
    def get_default_constraint(self):
        return """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""

    def get_default_action(self):
        return """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""


    '''
     changeAttrType (M): Changes the type of attributes to 'string', which allows conditions and actions to be specified on attribute values in patterns.
     Also appends '__' to attributes starting with '__'. This is because the pLabel and pMatchSubtypes attributes (introduced in one of the next steps) need to be scoped appropriately for HOTs. 
     The first time a metamodel is ramified, each class will have a __pLabel and __pMatchSubtypes attribute.
     The next time, these attributes are renamed to ____pLabel and ____pMatchSubtypes, to allow a condition/action to be specified for the __pLabel and __pMatchSubtypes attributes which were introduced in the first RAMified metamodel.
    '''
    def changeAttrType(self, graph, make_pre = True):

        self.next_label = 0

        #change mm of the graph

        try:
            if make_pre:
                graph["mm__"] = [str(Himesis.Constants.MT_PRECOND_PREFIX + graph["mm__"][0]), 'MoTifRule']
            else:
                graph["mm__"] = [str(Himesis.Constants.MT_POSTCOND_PREFIX + graph["mm__"][0]), 'MoTifRule']
        except IndexError:
            graph["mm__"] = "MM"


        if make_pre:
            #set the default constraint
            graph["MT_constraint__"] = self.get_default_constraint()
        else:
            graph["MT_action__"] = self.get_default_action()


        #add 'MT_pre__' to all non-GUID attributes
        for i in range(len(graph.vs)):
            node = graph.vs[i]


            #add MT_PRECOND_PREFIX to attrib names
            attribs_to_skip = ["GUID__", "mm__", "MT_label__", "MT_subtypes__", "MT_dirty__", "MT_subtypeMatching__"]

            #work around the igraph bug about giving too many attributes
            node_attributes = []
            #print("Node Attributes: " + str(node.attributes()))
            for attrib in node.attributes().keys():
                try:
                    node[attrib] = node[attrib]
                    node_attributes.append(attrib)
                except KeyError:
                    pass

            #print("Attributes: " + str(node_attributes))

            for attrib in node_attributes:

                #skip some of the attribs
                if attrib in attribs_to_skip:
                    continue

                #if the value is none, skip it
                if node[attrib] is None:
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
                del node[attrib]

                #re-add the value with the new attribute name

                if make_pre:
                    node[Himesis.Constants.MT_PRECOND_PREFIX + attrib] = val
                else:
                    node[Himesis.Constants.MT_POSTCOND_PREFIX + attrib] = val

            #change attrib values
            #hacky, to fix some edge cases
            for attrib in node_attributes:

                #add the prefix to the mm
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

                #hacky, some attribs are set to none
                none_types = ["MT_pre__directLink_S", "MT_post__directLink_S",
                              "MT_pre__trace_link", "MT_post__trace_link",
                              "directLink_S", "trace_link"]
                none_attrib = ["MT_pre__cardinality", "MT_pre__classtype", "MT_pre__name",
                               "MT_post__cardinality", "MT_post__classtype", "MT_post__name"]
                if node["mm__"] in none_types and attrib in none_attrib:
                    node[attrib] = None
                    continue

                none_types2 = ["MT_pre__trace_link", "MT_post__trace_link", "trace_link", "backward_link"]
                none_attrib2 = ["MT_pre__associationType", "MT_post__associationType", "associationType"]
                if node["mm__"] in none_types2 and attrib in none_attrib2:
                    node[attrib] = None
                    continue

                #set the other values to the default match code
                if make_pre:
                    node[attrib] = self.get_default_match_code()
                else:
                    node[attrib] = self.get_default_rewrite_code()
                

            #set these properties

            if make_pre:
                node["MT_subtypeMatching__"] = False
                node["MT_subtypes__"] = "[]"
                node["MT_dirty__"] = False

            #set the next label
            node["MT_label__"] = str(self.next_label)
            self.next_label += 1

            #very hacky, delete this attribute if possible
            #there may be a bug with the node.attributes()
            #returning more attributes than the node has
            #--confirmed to be in igraph
            # try:
            #     del node["MT_pre__type"]
            #
            # except Exception:
            #     pass
            #
            # try:
            #     pass
            #     #node["MT_pre__associationType"] = None
            # except Exception:
            #     pass
            #
            # try:
            #     del node["MT_post__type"]
            #     del node["MT_post__associationType"]
            # except Exception:
            #     pass

        return graph

    #RAMify this file
    def do_RAMify(self, graph, output_dir, remove_rule_nodes = True):
        
        input_name = graph["name"]
        print("Starting to ramify file: " + input_name)


        #rename the class
        graph["name"] = self.get_RAMified_name(input_name)

        #turn the backward links into trace links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])
        for node in backwards_links:
            node["mm__"] = "trace_link"

        #in some cases, the 'structural' or 'rule' nodes are removed
        if remove_rule_nodes == True:
            remove_nodes = self.find_nodes_with_mm(graph, ["MatchModel", "ApplyModel", "paired_with", "match_contains", "apply_contains", "directLink_T"])
            print("Removing rule nodes")
            graph.delete_nodes(remove_nodes)
        
        #make sure this graph becomes a precondition pattern
        graph = self.makePreConditionPattern(graph)

        #change the attribs in this graph
        graph = self.changeAttrType(graph)
        

        #this may be needed in future
#       #see if there are stored evals for this graph
#       #stored evals are so the matcher-writing person
#       #can define evals ahead of time
#       h = add_stored_evals(h, input_name)

        #compile the output pattern for future study + use
        #throw everything in the output dir
        graph.compile(output_dir)

        return graph


    #=========================
    #=========================

    #hacky, could be extended to better match hand-built rules
    def get_RAMified_name(self, name, partial=False):
        s = name.replace(".py", "") + "_Back"
        if not partial:
            s = s + "_Complete"
        else:
            s = s + "LHS"
        return s
        
        
    #find the nodes with this mm name
    def find_nodes_with_mm(self, graph, mm_names):
        nodes = []
        for node in graph.vs:
            if node["mm__"] in mm_names:
                nodes.append(node)
        return nodes
    
    #create the backward patterns for this file
    #could be combined with get_backward_patterns below
    def get_complete_backward_pattern(self, rule, skip_pausing):
        print("\nStarting get complete backward pattern")

        #from the rule, grab the name and the graph
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]

        #check to see which nodes have backward links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])
        
        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return {name:[]}
            
        #there are backward links, so start RAMifying
        out_dir = "./patterns/"
        outfile = out_dir + self.get_RAMified_name(name) + ".py"



        # remove all apply nodes not connected to a backward link

        # find the apply_contains
        apply_contains = self.find_nodes_with_mm(graph, ["apply_contains"])

        #find the backward links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])

        #find node nums attached to a backward link
        attached_to_backward_links = []
        for bl in backwards_links:
            attached_to_backward_links += self.look_for_attached(bl, graph)

        nodes_to_delete = []

        #look at the apply_contains link
        for apply_contain in apply_contains:

            #find the attached nodes to this link
            apply_attached_nodes = self.look_for_attached(apply_contain, graph)

            #for the nodes
            for aan in apply_attached_nodes:

                #get the node
                node = graph.vs[aan]

                if aan in attached_to_backward_links:
                    #this node is attached to a backward link, so leave it
                    pass
                elif str(node["mm__"]) not in ["ApplyModel", "apply_contains"]:
                    #don't remove important nodes, but delete all others
                    nodes_to_delete.append(node)

        #remove the nodes
        graph.delete_nodes(nodes_to_delete)


        graph = self.do_RAMify(graph, out_dir)
        
        #we might want to pause to let the matcher-writer edit the complete matcher before continuing
        #TODO: do we?
        if not skip_pausing:
            print("Please examine " + outfile + " and correct as necessary.")
            temp = raw_input("Press ENTER to continue, or Ctrl-C to abort:\n")
        
        #create the actual matcher from the graph
        complete_pattern = Matcher(graph)

        #do debugging drawing
        graph_to_dot(self.get_RAMified_name(name), graph)

        return {name:[complete_pattern]}


    #very hacky
    #removes this attribute in the graph nodes
    def fix_attrs_for_backward_patterns(self, graph):
        for node in graph.vs:
            try:
                del node["MT_pre__associationType"]
            except Exception:
                pass

        return graph

    # create the backward patterns for this file
    def get_backward_patterns(self, rule, skip_pausing):
        print("\nStarting get backward patterns")
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]
        return_graph = graph

        #check to see which nodes have backward links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])

        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return [{graph: None}, []]

        #there are backward links, so start RAMifying
        out_dir = "./patterns/"
        outfile = out_dir + self.get_RAMified_name(name) + ".py"

        graph = copy.deepcopy(graph)
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)

        #we might want to pause to let the matcher-writer edit the complete matcher before continuing
        #TODO: do we?
        if not skip_pausing:
            print("Please examine " + outfile + " and correct as necessary.")
            temp = raw_input("Press ENTER to continue, or Ctrl-C to abort:\n")

        #change the graph's name
        graph.name = self.get_RAMified_name(name)
        graph["name"] = self.get_RAMified_name(name)

        #output the graph
        graph.compile(out_dir)

        bwPatterns = []
        bwPatterns2Rule = {}

        #The node mappings may have changed
        #So to be safe, find the backward/trace links again
        backwards_links = self.find_nodes_with_mm(graph, ["MT_pre__trace_link"])

        #get the ids of the structural nodes
        structure_nodes = self.find_nodes_with_mm(graph, ["MT_pre__MatchModel", "MT_pre__paired_with", "MT_pre__ApplyModel", "MT_pre__match_contains", "MT_pre__apply_contains"])
        structure_nums = [self.get_node_num(graph, item) for item in structure_nodes]


        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = copy.deepcopy(graph)
        new_graph = self.makePreConditionPattern(new_graph)


        # keep the nodes attached to the backward link plus the 'structural' nodes
        #that should be kept
        nodes_to_keep = []  # + new_structure


        #for each backward link found, create a matcher for the attached nodes
        i = 0
        for link in backwards_links:
            #find the nodes attached to the backwards link
            attached_nodes = self.look_for_attached(link, new_graph)


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
        new_name = self.get_RAMified_name(name, True) + str(i)
        i += 1

        #write out the file
        new_graph.name = new_name
        new_graph["name"] = new_name


        #BIG HACK
        new_graph = self.fix_attrs_for_backward_patterns(new_graph)

        new_graph.compile(out_dir)

        rule = self.load_class(out_dir + "/" + new_name)
        backward_pattern = rule[rule.keys()[0]]

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
                    #this node is attached to a backward link, so leave it
                    pass
                elif str(node["mm__"]) not in ["MT_pre__ApplyModel", "MT_pre__apply_contains", "MT_pre__paired_with"]:
                    #don't remove important nodes, but delete all others
                    nodes_to_delete.append(node)

        print("Nodes to delete: " + str(len(nodes_to_delete)))
        return nodes_to_delete


    # create the backward patterns for this file
    def get_rule_combinators(self, rule):
        print("\nStarting get backward patterns")
        name = rule.keys()[0]
        graph = rule.values()[0]
        return_graph = self.copy_graph(graph)

        # check to see which nodes have backward links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])

        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return {name: None}

        #there are backward links, so start RAMifying
        out_dir = "./patterns/"
        outfile = out_dir + self.get_RAMified_name(name) + ".py"

        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)

        #change the graph's name
        graph.name = self.get_RAMified_name(name)
        graph["name"] = self.get_RAMified_name(name)

        #output the graph
        graph.compile(out_dir)

        bwPatterns = []
        bwPatterns2Rule = {}

        #The node mappings may have changed
        #So to be safe, find the backward/trace links again
        backwards_links = self.find_nodes_with_mm(graph, ["MT_pre__trace_link"])

        #get the ids of the structural nodes
        structure_nodes = self.find_nodes_with_mm(graph, ["MT_pre__MatchModel", "MT_pre__paired_with",
                                                          "MT_pre__ApplyModel", "MT_pre__match_contains",
                                                          "MT_pre__apply_contains"])
        structure_nums = [self.get_node_num(graph, item) for item in structure_nodes]

        # make sure to copy the graph, as we will make multiple smaller matchers from it
        new_graph = self.copy_graph(graph)
        new_graph = self.makePreConditionPattern(new_graph)



        base_graph = self.copy_graph(new_graph)


        #TODO: Get rewriter graph from matcher rewriter
        rewriter_graph = self.copy_graph(return_graph)


        #TODO: Handled by attr changing?

        # turn the backward links into trace links

        backwards_links2 = self.find_nodes_with_mm(rewriter_graph, ["backward_link"])
        #print(backwards_links2)

        for node in backwards_links2:
             node["mm__"] = "trace_link"




        #graph_to_dot("base_graph_before", base_graph)
        apply_links = self.get_links_in_apply(base_graph)

        base_graph.delete_nodes(structure_nums + apply_links)
        rewriter_graph.delete_nodes(structure_nums)


        #graph_to_dot("base_graph", base_graph)

        #graph_to_dot("rewriter_graph_before", rewriter_graph)
        #Turn rewriter_graph into RHS
        rewriter_graph = self.makePostConditionPattern(rewriter_graph)


        #graph_to_dot("rewriter_graph", rewriter_graph)

        # keep the nodes attached to the backward link plus the 'structural' nodes
        #that should be kept
        nodes_to_keep = []  # + new_structure


        #for each backward link found, create a matcher for the attached nodes
        i = 0
        for link in backwards_links:
            #find the nodes attached to the backwards link
            attached_nodes = self.look_for_attached(link, base_graph)
            nodes_to_keep += attached_nodes


        #get the list of nodes to remove
        #(which is all nodes that should not be kept)
        nodes_to_remove = range(len(base_graph.vs))
#        nodes_to_remove = [new_graph.vs[item] for item in nodes_to_remove if item not in nodes_to_keep]



        # don't consider removing the backward links and attached nodes
        for n in nodes_to_keep:
            nodes_to_remove.remove(n)

        #print("Nodes to remove: " + str(nodes_to_remove))
        #print("Types:")
        #for n in nodes_to_remove:
        #    print(base_graph.vs[n]["mm__"])

        input_nodes = nodes_to_remove

        output = sum([map(list, combinations(input_nodes, i)) for i in range(len(input_nodes) + 1)], [])
        #print(input_nodes)
        #print(output)


        # change the attribs in this graph
        rewriter_graph = self.changeAttrType(rewriter_graph, False)


        j = 0
        for remove_set in reversed(output):

            new_graph = self.copy_graph(base_graph)


            #remove everything except for the attached nodes and the backward link
            new_graph.delete_nodes(remove_set)



            #create the matcher

            j += 1

            #create a new name for this backward matcher
            #replace the pattern name with the partial pattern name
            new_name = name + str(i)
            i += 1

            #write out the file
            new_graph.name = new_name
            new_graph["name"] = new_name


            #BIG HACK
            new_graph = self.fix_attrs_for_backward_patterns(new_graph)



            new_graph.compile(out_dir)

            rule = self.load_class(out_dir + "/" + new_name)
            backward_pattern = rule.values()[0]

            #graph_to_dot(new_name, backward_pattern)
            #graph_to_dot("remove_graph" + str(j), new_graph)



            if remove_set == []:
                backward_pattern.NACs = []
            else:

                NAC_nodes_to_remove = []

                for to_remove in nodes_to_remove:
                    node = base_graph.vs[to_remove]
                    if node["mm__"] in ["indirectLink_S", "indirectLink_T", "directLink_S", "directLink_T"] \
                        and not node in remove_set:
                        NAC_nodes_to_remove.append(to_remove)

                #create the NAC if needed
                NAC_graph = self.copy_graph(base_graph)

                NAC_graph.delete_nodes(NAC_nodes_to_remove)


                NAC_graph = self.makePreConditionPatternNAC(NAC_graph)

                NAC_graph.name += "_NAC"

                NAC_graph.LHS = backward_pattern

                file_name = NAC_graph.compile(out_dir)
                #print("Compiled to: " + file_name)

                NAC_graph = self.load_class(out_dir + NAC_graph.name, [backward_pattern])
                NAC_graph = NAC_graph.values()[0]


                backward_pattern.NACs = [NAC_graph]

            #create the Matcher
            matcher = Matcher(backward_pattern)





            #TODO: Make rewriter code simpler, and same as match pattern rewriter

            rewriter_graph_copy = self.copy_graph(rewriter_graph)

            rewriter_graph_copy.pre = self.copy_graph(backward_pattern)
            rewriter_graph_copy.name += "_rewriter"
            file_name = rewriter_graph_copy.compile(out_dir)
            #print("Compiled to: " + file_name)

            rewriter_graph2 = self.load_class(out_dir + rewriter_graph_copy.name)
            rewriter_graph2 = rewriter_graph2.values()[0]

            # print(inspect.getargspec(rewriter_graph2.execute))
            # print(rewriter_graph2.__class__)
            # print(rewriter_graph2.name)
            # print("Hierarchy:")
            # print(inspect.getmro(rewriter_graph2.__class__))


            rewriter_graph2.pre = self.copy_graph(backward_pattern)

            rewriter = Rewriter(rewriter_graph2)






            #append the new backward pattern and name mapping
            bwPatterns.append([matcher, rewriter])
            #bwPatterns2Rule[matcher] = name

            #print("bwPatterns: " + str(bwPatterns))
        return {name: bwPatterns}


    def remove_equation_nodes(self, graph):
        structure_nodes = self.find_nodes_with_mm(graph, ["Equation", "leftExpr", "rightExpr"])
        graph.delete_nodes(structure_nodes)
        return graph

    def remove_structure_nodes(self, graph):
        structure_nodes = self.find_nodes_with_mm(graph, ["MatchModel", "match_contains", "paired_with", "ApplyModel", "apply_contains"])
        graph.delete_nodes(structure_nodes)
        return graph


    def flood_find_nodes(self, start_node, graph, stop_mms = []):
        node_stack = [start_node]
        return_nodes = []
        while len(node_stack) > 0:
            node = node_stack.pop()

            if graph.vs[node]["mm__"] in stop_mms:
                continue

            if node in return_nodes:
                continue

            return_nodes.append(node)

            for edge in graph.get_edgelist():
                if node == edge[0]:
                    node_stack.append(edge[1])
                elif node == edge[1]:
                    node_stack.append(edge[0])

        return return_nodes

    def get_match_graph(self, graph):
        graph = self.remove_equation_nodes(graph)

        apply_contain_node = self.find_nodes_with_mm(graph, ["apply_contains"])
        apply_contain_node = self.get_node_num(graph, apply_contain_node[0])

        apply_nodes = self.flood_find_nodes(apply_contain_node, graph, ["ApplyModel", "backward_link", "trace_link"])
        apply_nodes = list(set(apply_nodes))

        backward_links = self.find_nodes_with_mm(graph, ["backward_link"])
        attached_apply = []
        for bl in backward_links:
            attached_apply += self.look_for_attached(bl, graph)

        for an in attached_apply:

            try:
                apply_nodes.remove(an)
            except ValueError:
                pass

        graph.delete_nodes(apply_nodes)
        graph = self.remove_structure_nodes(graph)

        return graph


    def make_rewriter(self, graph):

        rewriter = self.copy_graph(graph)

        #Add trace links
        match_contains = self.find_nodes_with_mm(graph, ["match_contains"])
        match_attached = []
        for mc in match_contains:
            match_attached += self.look_for_attached(mc, rewriter)

        apply_contains = self.find_nodes_with_mm(graph, ["apply_contains"])
        apply_attached = []
        for ac in apply_contains:
            apply_attached += self.look_for_attached(ac, rewriter)

        linked_nodes = []

        backward_links = self.find_nodes_with_mm(graph, ["backward_link"])
        for bl in backward_links:
            bl_attached = self.look_for_attached(bl, rewriter)
            #print("BL attached: " + str(bl_attached))

            linked_nodes.append([bl_attached[0], bl_attached[1]])

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

                    if (a == match_node and b == apply_node) or \
                        (b == match_node and a == apply_node):
                        #there is already a link here
                        found_link = True
                        #print("Found the link")

                if not found_link:
                    #print("Did not find link")
                    new_node = rewriter.add_node()
                    rewriter.vs[new_node]["mm__"] = "trace_link"
                    rewriter.vs[new_node]["MT_label"] = str(len(rewriter.vs))

                    rewriter.add_edge(apply_node, new_node)
                    rewriter.add_edge(new_node, match_node)


        #graph_to_dot("the_rewriter_graph_" + rewriter.name, rewriter)

        rewriter = self.changeAttrType(rewriter, False)

        rewriter = self.makePostConditionPattern(rewriter)

        #graph_to_dot("the_rewriter_graph_after_post_" + rewriter.name, rewriter)


        return rewriter

    def get_match_pattern(self, rule):
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]


        rewriter = self.make_rewriter(graph)
        
        graph_to_dot("rewriter_pyr", rewriter)

        new_name = name + "_matchLHS"
        
        graph.name = new_name
        graph["name"] = new_name
        
        out_dir = "./patterns/"

        graph = self.get_match_graph(graph)
        
        graph_to_dot("matcher_pyr", graph)        
        
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)

        graph["mm__"] = [graph["mm__"][0], 'MoTifRule']
        graph["name"] = ""
        graph["MT_constraint__"] = self.get_default_constraint()



        #Remove pre_cardinality
        for i in range(len(graph.vs)):
            node = graph.vs[i]
            try:
                del(node["MT_pre__cardinality"])
            except:
                pass

            if node["mm__"] != "MT_pre__directLink_S":
                node["MT_pre__associationType"] = None

        graph.compile(out_dir)

        #have to reload the graph to define all the eval functions
        rule = self.load_class(out_dir + "/" + new_name)
        match_graph = rule.values()[0]


        rewriter.pre = match_graph
        rewriter.name += "_rewriter"
        #graph_to_dot("the_rewriter_graph" + rewriter.name, rewriter)

        rewriter.compile(out_dir)

        rewriter_dict = self.load_class(out_dir + rewriter.name)
        rewriter = rewriter_dict.values()[0]

        #graph_to_dot("the_rewriter_graph_after" + rewriter.name, rewriter)

        return {name : [Matcher(match_graph), Rewriter(rewriter)]}
    #=========================

    #function to dynamically load a new class
    import importlib
    def load_class(self, full_class_string, args = []):
        directory, module_name = os.path.split(full_class_string)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, directory)

        try:
            module = __import__(module_name)

            if args == []:
                loaded_module = {module_name : getattr(module, module_name)()}
            else:
                loaded_module = {module_name : getattr(module, module_name)(args[0])}
        finally:
            sys.path[:] = path # restore
        return loaded_module

    #ramify a whole directory
    def ramify_directory(self, dir_name, skip_pausing = True):
        print("Ramifying directory: " + dir_name)
        
        rules = {}
        
        backwardPatterns = {}
        backwardPatterns2Rules = {}
        backwardPatternsComplete = {}
        matchRulePatterns = {}
        ruleCombinators = {}

        #examine all the files in this dir
        for f in os.listdir(dir_name):

            #skip these files
            if f.endswith(".pyc") or f == "__init__.py" or os.path.isdir(dir_name + "/" + f):
                continue

            print("\n\nFile: " + f)

            #add the rule to the rules dict
            rule = self.load_class(dir_name + "/" + f)
            rules.update(rule)

            #reload the rule
            #this is probably not needed
            #but there were problems with aliasing and copying
            rule2 = self.load_class(dir_name + "/" + f)
            #get the complete backwards pattern
            BwPComplete = None#self.get_complete_backward_pattern(rule2, skip_pausing)
            #backwardPatternsComplete.update(BwPComplete)

            #get the backwards pattern for this rule
            rule3 = self.load_class(dir_name + "/" + f)
            (bwPattern, bwP2Rule) = self.get_backward_patterns(rule3, skip_pausing)
            backwardPatterns.update(bwPattern)

            if not bwP2Rule is None:
                backwardPatterns2Rules.update(bwP2Rule)

            #fresh rule for the match pattern
            rule4 = self.load_class(dir_name + "/" + f)
            matchRulePattern = self.get_match_pattern(rule4)
            matchRulePatterns.update(matchRulePattern)


            # fresh rule for the rule combinators
            rule5 = self.load_class(dir_name + "/" + f)
            rule_combinator = self.get_rule_combinators(rule5)
            ruleCombinators.update(rule_combinator)

        return [rules, backwardPatterns, backwardPatterns2Rules, backwardPatternsComplete, matchRulePatterns, ruleCombinators]

    #helper function for the user, to list all of the
    #rules in the transformation that have backward links
    def getRulesIncludingBackLinks(self, transformation, backwardPatterns):
        rulesIncludingBackLinks = []

        for layer in transformation:
            back_links = []
            for rule in layer:
                
                bp = backwardPatterns[rule.name]
                if bp == []:
                    continue

                #if the rule has a backwards pattern,
                #then it has backwards links
                back_links.append(rule)

            #keep the layered structure
            rulesIncludingBackLinks.append(back_links)
        return rulesIncludingBackLinks

    def changePropertyProverMetamodel(self, pre_metamodel, post_metamodel, subclasses_source, subclasses_target):
        himesis_files = []
        property_prover_rules_dir = "./property_prover_rules/"
        for d in os.listdir(property_prover_rules_dir):

            if not os.path.isdir(property_prover_rules_dir + d):
                continue

            #print(d)
            rule_dir = property_prover_rules_dir + d + "/Himesis/"
            for f in os.listdir(rule_dir):
                if f == "__init__.py" or f.endswith(".pyc") or f.startswith("."):
                    continue
                #print f

                #curr_wd = os.getcwd()
                #os.chdir(rule_dir)

                rule_file = rule_dir + f
                try:
                    rule = self.load_class(rule_file)
                except ImportError:
                    print("ERROR " + rule_file)
                    continue

                name = rule.keys()[0]
                graph = rule[rule.keys()[0]]

                if f.endswith("LHS.py"):
                    graph["mm__"] = pre_metamodel
                elif f.endswith("RHS.py"):
                    graph["mm__"] = post_metamodel
                else:
                    print "Error: Not LHS or RHS rule"

                for node in graph.vs:

                    if "MT_subtypeMatching__" in node.attributes().keys() and node["MT_subtypeMatching__"] == False:
                        continue

                    if "MT_subtypes__" in node.attributes().keys() and len(node["MT_subtypes__"]) >= 1:
                        #print("\n" + node["mm__"])
                        #print(node["MT_subtypes__"])
                        if node["mm__"] == "MT_pre__MetaModelElement_S":
                            #print(subclasses_source)
                            node["MT_subtypes__"] = subclasses_source
                        elif node["mm__"] == "MT_pre__MetaModelElement_T":
                            #print(subclasses_target)
                            node["MT_subtypes__"] = subclasses_target



                graph.compile(rule_dir)

                #os.chdir(curr_wd)

if __name__ == "__main__":
     #No default action
    pass



