from core.himesis import *

#get the id number of a node in the graph
#hacky, as this is based on the node's attributes
def get_node_num(graph, node):
    for i in range(len(graph.vs)):
        if graph.vs[i]["GUID__"] == node["GUID__"]:

            if not graph.vs[i]["mm__"] == node["mm__"]:
                raise Exception("get_node_num is wrong!!!")
            return i
    return -1

#find the nodes with this mm name
def find_nodes_with_mm(graph, mm_names):
    nodes = []
    for node in graph.vs:
        if node["mm__"] in mm_names:
            nodes.append(node)
    return nodes

#=========================
#look for the nodes attached to the node number 'num'
#used to find backward links
def look_for_attached(link, graph):
    attached_node_nums = []


    #hacky way of finding the index of the node
    node_num = get_node_num(graph, link)

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
def look_for_attached_of_attached(link, graph):
    attached_of_attached = []
    attached = look_for_attached(link, graph)

    for a in attached:
        attached_of_attached += look_for_attached(graph.vs[a], graph)

    return list(set(attached_of_attached))


def flood_find_nodes(start_node, graph, stop_mms = [], stop_and_include_mms = []):
    node_stack = [start_node]
    return_nodes = []
    while len(node_stack) > 0:
        node = node_stack.pop()

        if graph.vs[node]["mm__"] in stop_and_include_mms:
            return_nodes.append(node)
            continue

        if graph.vs[node]["mm__"] in stop_mms:
            continue

        if node in return_nodes:
            continue

        return_nodes.append(node)

        for edge in graph.get_edgelist():
            mm1 = graph.vs[edge[0]]["mm__"]
            mm2 = graph.vs[edge[1]]["mm__"]

            if node == edge[0]:
                node_stack.append(edge[1])
            elif node == edge[1]:
                node_stack.append(edge[0])

    return return_nodes


#Very hacky way of making the graph a HimesisPreConditionPatternLHS
def makePreConditionPattern(graph):

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

def makePreConditionPatternNAC(graph):

    graph = makePreConditionPattern(graph)

    graph.__class__ = HimesisPreConditionPatternNAC

    graph.LHS = None
    graph.bridge = None
    graph.init_params.append('LHS')
    graph.import_name = 'HimesisPreConditionPatternNAC'

    return graph


def makePostConditionPattern(old_graph):
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
def copy_graph(graph2):
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
        graph1.pre = copy_graph(graph2.pre)
    except AttributeError:
        pass

    return graph1


# helper function for the user, to list all of the
#rules in the transformation that have backward links
def getRulesIncludingBackLinks(transformation, backwardPatterns):
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


#the default eval match code
#use to build the matchers
def get_default_match_code():

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

def get_default_rewrite_code():
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
def get_default_constraint():
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

def get_default_action():
    return """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""