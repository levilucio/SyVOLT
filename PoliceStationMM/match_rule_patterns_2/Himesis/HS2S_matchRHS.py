

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
        
        super(HS2S_matchRHS, self).__init__(name='HS2S_matchRHS', num_nodes=9, edges=[])
        
        # Add the edges
        self.add_edges([(6, 0), (4, 0), (2, 1), (1, 8), (2, 4), (7, 3), (3, 5), (5, 6)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = pickle.loads("""V#===============================================================================\u000a# This code is executed after the rule has been applied.\u000a# You can access a node labelled n matched by this rule by: PostNode('n').\u000a# To access attribute x of node n, use: PostNode('n')['x'].\u000a#===============================================================================\u000a\u000apass\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('ebc315c5-2247-426f-94c9-1f2fd0e16edc')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["MT_post__name"] = """
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
        self.vs[0]["mm__"] = """MT_post__Attribute"""
        self.vs[0]["GUID__"] = UUID('2d67beec-af35-4b66-8f77-0e686726d4a6')
        self.vs[1]["MT_label__"] = """11"""
        self.vs[1]["mm__"] = """MT_post__rightExpr"""
        self.vs[1]["GUID__"] = UUID('c6c776d3-a857-44ad-acc4-d23cf5f4d21f')
        self.vs[2]["MT_label__"] = """9"""
        self.vs[2]["mm__"] = """MT_post__Equation"""
        self.vs[2]["GUID__"] = UUID('fc9cab1c-5b70-49d8-b8c5-b35c7ca546ca')
        self.vs[3]["MT_label__"] = """5"""
        self.vs[3]["mm__"] = """MT_post__trace_link"""
        self.vs[3]["GUID__"] = UUID('a7a18126-7c25-4e0f-9b1f-23ca135ba7f2')
        self.vs[4]["MT_label__"] = """10"""
        self.vs[4]["mm__"] = """MT_post__leftExpr"""
        self.vs[4]["GUID__"] = UUID('2164a430-eec1-49ce-ab5a-885b7a92c0a0')
        self.vs[5]["MT_post__cardinality"] = """
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
        self.vs[5]["MT_label__"] = """1"""
        self.vs[5]["MT_post__name"] = """
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
        self.vs[5]["mm__"] = """MT_post__Station_S"""
        self.vs[5]["MT_post__classtype"] = """
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
        self.vs[5]["GUID__"] = UUID('29d917ac-836e-418a-bc31-cbb89f2a7169')
        self.vs[6]["MT_label__"] = """3"""
        self.vs[6]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[6]["GUID__"] = UUID('f605b655-f8c2-4ffa-9462-ffd0d2d2936a')
        self.vs[7]["MT_label__"] = """4"""
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
        self.vs[7]["GUID__"] = UUID('901bb3af-87c8-4de6-a282-6dc0fed48d4d')
        self.vs[8]["MT_post__value"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value\u000a# of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn "somestation"\u000a
p1
.""")
        self.vs[8]["MT_label__"] = """8"""
        self.vs[8]["mm__"] = """MT_post__Constant"""
        self.vs[8]["GUID__"] = UUID('fd125571-9d15-43df-8c54-e63251d77bf4')

        from HS2S_matchLHS import HS2S_matchLHS
        self.pre = HS2S_matchLHS()
    
    def set_value8(self, attr_value, PreNode, graph):
        
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
        
        return "somestation"


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
        # rightExpr11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # trace_link5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # leftExpr10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Station_T4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Station_T'
        # Constant8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['value'] = self.set_value8(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'value\'', e)
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # leftExpr10 -> Attribute2
        graph.add_edges((labels['10'], labels['2']))
        # Equation9 -> leftExpr10
        graph.add_edges((labels['9'], labels['10']))
        # Equation9 -> rightExpr11
        graph.add_edges((labels['9'], labels['11']))
        # rightExpr11 -> Constant8
        graph.add_edges((labels['11'], labels['8']))
        # Station_T4 -> trace_link5
        graph.add_edges((labels['4'], labels['5']))
        # trace_link5 -> Station_S1
        graph.add_edges((labels['5'], labels['1']))
        
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
    
