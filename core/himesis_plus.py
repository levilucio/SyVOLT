from core.himesis import *

#find the nodes with these mm names
def find_nodes_with_mm(graph, mm_names):
    return [node for node in graph.vs if node["mm__"] in mm_names]

#=========================
def get_all_attached(graph):

    attached = [[] for x in range(graph.vcount())]

    for edge in graph.es:
        source, target = edge.tuple
        attached[source].append(target)
        attached[target].append(source)

    for i in range(len(attached)):
        attached[i].append(i)

    return attached

#look for the nodes attached to the link_node
def look_for_attached(link_node, graph):
    #attached_node_nums = []

    try:
        node_num = int(link_node)
    except TypeError:
        #find the index of the node
        node_num = link_node.index

    #check the edge list to see if there are attached edges
    attached_node_nums = [x for x in [edge.source if edge.target == node_num else edge.target if edge.source == node_num else None for edge in graph.es] if x is not None]

    # for edge in graph.es:
    #     source = edge.source
    #     target = edge.target
    #     if node_num == source:
    #         attached_node_nums.append(target)
    #     elif node_num == target:
    #         attached_node_nums.append(source)

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

def find_connected_match_node(node, graph):
    containing_node = graph.neighbors(node, 2)[0]
    mms = graph.vs["mm__"]

    if mms[containing_node] == "match_contains" or mms[containing_node] == "apply_contains" :
        containing_node = graph.neighbors(containing_node, 2)[0]

    if mms[containing_node] == "MatchModel":
        return containing_node

    #containing node should be the ApplyModel now

    paired_with_node = graph.neighbors(containing_node, 2)[0]

    match_model = graph.neighbors(paired_with_node, 2)[0]

    if mms[match_model] != "MatchModel":
        raise Exception("The node is not a MatchModel!")
    return match_model

#flood fill throughout the graph starting at the start node
#this flood occurs through the edges in the graph
#until a stop mm is reached
#stop mm nodes will not be included in the returned array
#while stop_and_include mms will
def flood_find_nodes(start_node, graph, stop_mms = None, stop_and_include_mms = None, filter_mms = None):

    return_nodes = []

    mms = graph.vs["mm__"]

    vcount = graph.vcount()

    neighbours = [[] for i in range(vcount)]

    for e in graph.es:
        source, target = e.tuple
        neighbours[source].append(target)
        neighbours[target].append(source)

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

        if not filter_mms or mms[node] in filter_mms:
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
return True
"""

def get_default_rewrite_code():
    return """
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
