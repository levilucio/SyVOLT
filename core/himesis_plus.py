from core.himesis import *

#get the postion of this node in the Himesis graph
def get_node_num(graph, node):
    for i in range(len(graph.vs)):
        if graph.vs[i]["GUID__"] == node["GUID__"]:
            return i
    raise Exception("The node " + node["mm__"] + " was not found in this graph")

#find the nodes with these mm names
def find_nodes_with_mm(graph, mm_names):
    nodes = []
    for node in graph.vs:
        if node["mm__"] in mm_names:
            nodes.append(node)
    return nodes

#=========================
#look for the nodes attached to the link_node
def look_for_attached(link_node, graph):
    attached_node_nums = []

    #find the index of the node
    node_num = get_node_num(graph, link_node)

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
def look_for_attached_of_attached(link_node, graph):
    attached = look_for_attached(link_node, graph)

    attached_of_attached = []
    for a in attached:
        attached_of_attached += look_for_attached(graph.vs[a], graph)

    #ignore duplicates
    return list(set(attached_of_attached))


#flood fill throughout the graph starting at the start node
#this flood occurs through the edges in the graph
#until a stop mm is reached
#stop mm nodes will not be included in the returned array
#while stop_and_include mms will
def flood_find_nodes(start_node, graph, stop_mms = None, stop_and_include_mms = None):

    return_nodes = []

    mms = graph.vs["mm__"]

    vcount = graph.vcount()

    neighbours = [[] for i in range(vcount)]

    for e in graph.es:
        neighbours[e.source].append(e.target)
        neighbours[e.target].append(e.source)

    visited = [False] * vcount

    node_stack = [start_node]
    while len(node_stack) > 0:
        node = node_stack.pop()

        visited[node] = True

        #don't look at already-included nodes
        #if node in return_nodes:
        #    continue

        #include this node, but don't add neighbours to the stack
        if stop_and_include_mms is not None and mms[node] in stop_and_include_mms:
            return_nodes.append(node)
            continue

        #don't add neighbours to the stack
        if stop_mms is not None and mms[node] in stop_mms:
            continue

        return_nodes.append(node)

        #add neighbours to the stack
        new_neighbours = [n for n in neighbours[node] if not visited[n]]
        node_stack += new_neighbours
        # for edge in graph.get_edgelist():
        #     if node == edge[0]:
        #         node_stack.append(edge[1])
        #     elif node == edge[1]:
        #         node_stack.append(edge[0])

    return set(return_nodes)


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
    #graph.import_name = 'HimesisPreConditionPatternLHS'
    graph.NACs = []

    return graph

def makePreConditionPatternNAC(graph):

    graph = makePreConditionPattern(graph)

    graph.__class__ = HimesisPreConditionPatternNAC

    graph.LHS = None
    graph.bridge = None
    #graph.import_name = 'HimesisPreConditionPatternNAC'

    return graph


def makePostConditionPattern(old_graph):
    graph = old_graph.copy()

    # force the class to be different
    graph.__class__ = HimesisPostConditionPattern

    # variables added in subclasses

    #from HimesisPattern
    graph.nodes_label = {}
    graph.nodes_pivot_out = {}

    #from HimesisPostConditionPattern
    graph.pre = None
    #graph.import_name = 'HimesisPostConditionPattern'

    return graph


def buildPreListFromClassNames(classNameList):
    '''
    adds the 'MT_pre__' prefix to a set of class names
    '''
    return ["MT_pre__" + className for className in classNameList]

#FIXME to be proper
#could be smarter depending on the type

#TODO: Use Himesis' copy operation to do this
def copy_graph(graph2):
    graph1 = graph2.copy()

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

    #graph1.import_name = copy.deepcopy(graph2.import_name)

    try:
        graph1.NACs = [N.copy() for N in graph2.NACs]
    except AttributeError:
        pass

    try:
        graph1.pre = copy_graph(graph2.pre)
    except AttributeError:
        pass

    return graph1


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