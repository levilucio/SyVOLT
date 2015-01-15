

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HS2S_matchRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S_matchRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S_matchRHS, self).__init__(name='HS2S_matchRHS', num_nodes=10, edges=[])
        
        # Add the edges
        self.add_edges([(5, 8), (3, 8), (6, 9), (0, 9), (1, 0), (1, 3), (7, 2), (2, 4), (4, 5), (7, 6)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""
        self["name"] = """"""
        self["GUID__"] = UUID('a84f973d-866f-453d-8563-9c9aa2076a3e')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """10"""
        self.vs[0]["mm__"] = """MT_post__rightExpr"""
        self.vs[0]["GUID__"] = UUID('d662bf98-d4a9-4c4f-9dae-2326e949c127')
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["mm__"] = """MT_post__Equation"""
        self.vs[1]["GUID__"] = UUID('caff5113-d102-443a-836b-e78b5ec48bca')
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["GUID__"] = UUID('86933f7d-3825-4e2d-ad96-d3f53e14d422')
        self.vs[3]["MT_label__"] = """9"""
        self.vs[3]["mm__"] = """MT_post__leftExpr"""
        self.vs[3]["GUID__"] = UUID('fc4d7ed0-67b5-4ed7-a30e-7f9006ea17dc')
        self.vs[4]["MT_post__cardinality"] = """
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
        self.vs[4]["MT_label__"] = """1"""
        self.vs[4]["MT_post__name"] = """
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
        self.vs[4]["mm__"] = """MT_post__Station_S"""
        self.vs[4]["MT_post__classtype"] = """
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
        self.vs[4]["GUID__"] = UUID('b60ea705-09fa-44e0-98da-8e322feae98b')
        self.vs[5]["MT_label__"] = """7"""
        self.vs[5]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[5]["GUID__"] = UUID('c6c55db4-ebec-4e84-8ec4-ba198f10ac47')
        self.vs[6]["MT_label__"] = """8"""
        self.vs[6]["mm__"] = """MT_post__hasAttr_T"""
        self.vs[6]["GUID__"] = UUID('90798ce3-23ae-48a0-ac04-025a15e7daa6')
        self.vs[7]["MT_label__"] = """3"""
        self.vs[7]["MT_post__name"] = """
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
        self.vs[7]["mm__"] = """MT_post__Station_T"""
        self.vs[7]["MT_post__classtype"] = """
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
        self.vs[7]["GUID__"] = UUID('340728d5-51fb-48f9-8609-caad395a209a')
        self.vs[8]["MT_label__"] = """2"""
        self.vs[8]["MT_post__name"] = """
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
        self.vs[8]["mm__"] = """MT_post__Attribute"""
        self.vs[8]["GUID__"] = UUID('a8ad1d09-a77b-4f2b-a1b8-8b6c00f9cf2e')
        self.vs[9]["MT_label__"] = """4"""
        self.vs[9]["MT_post__name"] = """
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

return "name"
"""
        self.vs[9]["mm__"] = """MT_post__Attribute"""
        self.vs[9]["GUID__"] = UUID('5cfaf0b6-744e-4210-98fa-55c11eca11a3')

        from HS2S_matchLHS import HS2S_matchLHS
        self.pre = HS2S_matchLHS()
    
    def set_name4(self, attr_value, PreNode, graph):
        
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
        
        return "name"


    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        #===============================================================================
        # This code is executed after the rule has been applied.
        # You can access a node labelled n matched by this rule by: PostNode('n').
        # To access attribute x of node n, use: PostNode('n')['x'].
        #===============================================================================
        
        pass

    def execute(self, packet, match):
        """
            Transforms the current match of the packet according to the rule %s.
            Pivots are also assigned, if any.
            @param packet: The input packet.
            @param match: The match to rewrite.
        """
        graph = packet.graph
        
        # Build a dictionary {label: node index} mapping each label of the pattern to a node in the graph to rewrite.
        # Because of the uniqueness property of labels in a rule, we can store all LHS labels
        # and subsequently add the labels corresponding to the nodes to be created.
        labels = match.copy()
        
        #===============================================================================
        # Update attribute values
        #===============================================================================
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # Attribute4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        try:
            graph.vs[new_node]['name'] = self.set_name4(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # rightExpr10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # trace_link5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # leftExpr9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # hasAttr_T8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_T'
        # Station_T3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Station_T'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # rightExpr10 -> Attribute4
        graph.add_edges((labels['10'], labels['4']))
        # Equation6 -> rightExpr10
        graph.add_edges((labels['6'], labels['10']))
        # Station_T3 -> trace_link5
        graph.add_edges((labels['3'], labels['5']))
        # Station_T3 -> hasAttr_T8
        graph.add_edges((labels['3'], labels['8']))
        # hasAttr_T8 -> Attribute4
        graph.add_edges((labels['8'], labels['4']))
        # trace_link5 -> Station_S1
        graph.add_edges((labels['5'], labels['1']))
        # Equation6 -> leftExpr9
        graph.add_edges((labels['6'], labels['9']))
        # leftExpr9 -> Attribute2
        graph.add_edges((labels['9'], labels['2']))
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        
        #===============================================================================
        # Perform the post-action
        #===============================================================================
        try:
            self.action(lambda i: graph.vs[labels[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while applying the post-action', e)
        #===============================================================================
        # Finally, delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
    
