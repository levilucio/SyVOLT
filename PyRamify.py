#!/bin/python
import re
import sys
import os
from t_core.matcher import Matcher
from himesis_utils import *
#from ramify_actions import *

from core.himesis import *
from itertools import combinations

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

    def makePostConditionPattern(self, old_graph):
        graph = self.copy_graph(old_graph)

        # force the class to be different
        graph.__class__ = HimesisPostConditionPattern

        # variables added in subclasses

        #from HimesisPattern
        graph.nodes_label = {}
        graph.nodes_pivot_out = {}

        #from HimesisPostConditionPattern
        graph.pre = None
        graph.import_name = 'HimesisPostConditionPattern'


    #FIXME to be proper
    def copy_graph(self, graph2):
        graph1 = copy.deepcopy(graph2)
        graph1.nodes_label = copy.deepcopy(graph2.nodes_label)
        graph1.nodes_pivot_out = copy.deepcopy(graph2.nodes_pivot_out)

        graph1.nodes_pivot_in = copy.deepcopy(graph2.nodes_pivot_in)

        graph1.import_name = copy.deepcopy(graph2.import_name)
        graph1.NACs = copy.deepcopy(graph2.NACs)

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

    '''
     changeAttrType (M): Changes the type of attributes to 'string', which allows conditions and actions to be specified on attribute values in patterns.
     Also appends '__' to attributes starting with '__'. This is because the pLabel and pMatchSubtypes attributes (introduced in one of the next steps) need to be scoped appropriately for HOTs. 
     The first time a metamodel is ramified, each class will have a __pLabel and __pMatchSubtypes attribute.
     The next time, these attributes are renamed to ____pLabel and ____pMatchSubtypes, to allow a condition/action to be specified for the __pLabel and __pMatchSubtypes attributes which were introduced in the first RAMified metamodel.
    '''
    def changeAttrType(self, graph):

        self.next_label = 0

        #change mm of the graph

        try:
            graph["mm__"] = [str(Himesis.Constants.MT_PRECOND_PREFIX + graph["mm__"][0]), 'MoTifRule']
        except IndexError:
            graph["mm__"] = "MM"

        #set the default constraint
        graph["MT_constraint__"] = self.get_default_constraint()

        #add 'MT_pre__' to all non-GUID attributes
        for i in range(len(graph.vs)):
            node = graph.vs[i]


            #add MT_PRECOND_PREFIX to attrib names
            attribs_to_skip = ["GUID__", "mm__", "MT_label__", "MT_subtypes__", "MT_dirty__", "MT_subtypeMatching__"]

            for attrib in node.attributes():

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

                #make sure to copy the value
                val = copy.deepcopy(node[attrib])

                #delete the attrib from the node
                del node[attrib]

                #re-add the value with the new attribute name
                node[Himesis.Constants.MT_PRECOND_PREFIX + attrib] = val

            #change attrib values
            #hacky, to fix some edge cases
            for attrib in node.attributes():

                #add the prefix to the mm
                if attrib == "mm__":
                    node["mm__"] = Himesis.Constants.MT_PRECOND_PREFIX + node["mm__"]
                    continue

                #skip the other attribs
                if attrib in attribs_to_skip:
                    continue

                #hacky, some attribs are set to none
                none_types = ["MT_pre__directLink_S", "MT_pre__trace_link", "directLink_S", "trace_link"]
                none_attrib = ["MT_pre__cardinality", "MT_pre__classtype", "MT_pre__name"]
                if node["mm__"] in none_types and attrib in none_attrib:
                    node[attrib] = None
                    continue

                none_types2 = ["MT_pre__trace_link", "trace_link"]
                none_attrib2 = ["MT_pre__associationType", "associationType"]
                if node["mm__"] in none_types2 and attrib in none_attrib2:
                    node[attrib] = None
                    continue

                #set the other values to the default match code
                node[attrib] = self.get_default_match_code()
                

            #set these properties
            node["MT_subtypeMatching__"] = False
            node["MT_dirty__"] = False
            node["MT_subtypes__"] = "[]"

            #set the next label
            node["MT_label__"] = str(self.next_label)
            self.next_label += 1

            #very hacky, delete this attribute if possible
            #there may be a bug with the node.attributes()
            #returning more attributes than the node has
            #--confirmed to be in igraph
            try:
                del node["MT_pre__type"]
            except Exception:
                pass

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
        return_graph = copy.deepcopy(graph)

        #check to see which nodes have backward links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])

        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return [{graph: None}, []]

        #there are backward links, so start RAMifying
        out_dir = "./patterns/"
        outfile = out_dir + self.get_RAMified_name(name) + ".py"

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

        return [{return_graph: matcher}, bwPatterns2Rule]

    # create the backward patterns for this file
    def get_rule_combinators(self, rule):
        print("\nStarting get backward patterns")
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]
        return_graph = copy.deepcopy(graph)

        # check to see which nodes have backward links
        backwards_links = self.find_nodes_with_mm(graph, ["backward_link"])

        #no backward links in file, do nothing
        if len(backwards_links) == 0:
            return {graph: None}

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
        new_graph = copy.deepcopy(graph)
        new_graph = self.makePreConditionPattern(new_graph)

        print("NACs: " + str(new_graph.NACs))
        base_graph = self.copy_graph(new_graph)

        print("NACs: " + str(base_graph.NACs))


        base_graph.delete_nodes(structure_nums)

        graph_to_dot("base_graph", base_graph)



        #TODO: Turn base_graph into RHS
        rewriter_graph = self.makePostConditionPattern(new_graph)

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

        print("Nodes to remove: " + str(nodes_to_remove))
        print("Types:")
        for n in nodes_to_remove:
            print(base_graph.vs[n]["mm__"])

        input_nodes = nodes_to_remove

        output = sum([map(list, combinations(input_nodes, i)) for i in range(len(input_nodes) + 1)], [])
        #print(input_nodes)
        #print(output)

        j = 0

        for remove_set in output:

            new_graph = self.copy_graph(base_graph)


            #remove everything except for the attached nodes and the backward link
            new_graph.delete_nodes(remove_set)


            j += 1

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

            #graph_to_dot(new_name, backward_pattern)
            graph_to_dot("remove_graph" + str(j), new_graph)

            #create the Matcher
            matcher = Matcher(backward_pattern)

            #append the new backward pattern and name mapping
            bwPatterns.append(matcher)
            #bwPatterns2Rule[matcher] = name

            #print("bwPatterns: " + str(bwPatterns))
        return {return_graph: bwPatterns}


    def get_match_pattern(self, rule):
        name = rule.keys()[0]
        graph = rule[rule.keys()[0]]
            
        new_name = name + "_overlapLHS"
        
        graph.name = new_name
        graph["name"] = new_name
        
        out_dir = "./patterns/"
        
        graph = self.do_RAMify(graph, out_dir, remove_rule_nodes = False)


        graph["mm__"] = [graph["mm__"][0], 'MoTifRule']
        graph["name"] = ""
        graph["MT_constraint__"] = self.get_default_constraint()


        match_contains = self.find_nodes_with_mm(graph, ["MT_pre__match_contains"])

        nodes_to_keep = []
        for link in match_contains:
            nodes_to_keep = nodes_to_keep + self.look_for_attached_of_attached(link, graph)



        #remove duplicates
        nodes_to_keep = list(set(nodes_to_keep))

        #print("Keep:")
        #for n in nodes_to_keep:
        #    print graph.vs[n]["mm__"]

        nodes_to_remove = []
        mms_to_remove = ["MT_pre__MatchModel", "MT_pre__match_contains", "MT_pre__paired_with", "MT_pre__trace_link"]
        for i in range(len(graph.vs)):
            if i not in nodes_to_keep or graph.vs[i]["mm__"] in mms_to_remove:
                nodes_to_remove.append(i)

        #print("Remove:")
        #for n in nodes_to_remove:
        #    print graph.vs[n]["mm__"]

        #remove everything except for the attached nodes
        graph.delete_nodes(nodes_to_remove)



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
        match_graph = rule[rule.keys()[0]]

        return {name : Matcher(match_graph)}
    #=========================

    #function to dynamically load a new class
    import importlib
    def load_class(self, full_class_string):
        directory, module_name = os.path.split(full_class_string)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, directory)

        try:
            module = __import__(module_name)
            loaded_module = {module_name : getattr(module, module_name)()}
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
            matchRulePattern = self.get_rule_combinators(rule4)
            matchRulePatterns.update(matchRulePattern)

        return [rules, backwardPatterns, backwardPatterns2Rules, backwardPatternsComplete, matchRulePatterns]

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



