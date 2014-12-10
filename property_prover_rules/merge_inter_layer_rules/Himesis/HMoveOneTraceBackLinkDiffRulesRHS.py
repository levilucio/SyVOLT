

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HMoveOneTraceBackLinkDiffRulesRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneTraceBackLinkDiffRulesRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneTraceBackLinkDiffRulesRHS, self).__init__(name='HMoveOneTraceBackLinkDiffRulesRHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [2, 3], [1, 0], [1, 2]])
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
        self["GUID__"] = UUID('164b90c6-c694-49ac-9abe-eba281d03e6e')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """21"""
        self.vs[0]["mm__"] = """MT_post__trace_link"""
        self.vs[0]["GUID__"] = UUID('53443f7a-4c91-4fe8-ae82-15e571cb4694')
        self.vs[1]["MT_post__cardinality"] = """
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
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["MT_post__name"] = """
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
        self.vs[1]["mm__"] = """MT_post__MetaModelElement_T"""
        self.vs[1]["MT_post__classtype"] = """
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
        self.vs[1]["GUID__"] = UUID('92d146df-66a9-4d73-af3c-afcfa3b82912')
        self.vs[2]["MT_post__type"] = """
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
        self.vs[2]["MT_label__"] = """22"""
        self.vs[2]["mm__"] = """MT_post__backward_link"""
        self.vs[2]["GUID__"] = UUID('7292c127-9152-4038-adf9-e9ece5c71525')
        self.vs[3]["MT_pivotOut__"] = """element1"""
        self.vs[3]["MT_post__cardinality"] = """
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
        self.vs[3]["MT_label__"] = """7"""
        self.vs[3]["MT_post__name"] = """
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
        self.vs[3]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[3]["MT_post__classtype"] = """
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
        self.vs[3]["GUID__"] = UUID('8b7302b4-c378-458a-b899-cca62896cf1d')
        self.vs[4]["MT_pivotOut__"] = """element2"""
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
        self.vs[4]["MT_label__"] = """8"""
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
        self.vs[4]["mm__"] = """MT_post__MetaModelElement_S"""
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
        self.vs[4]["GUID__"] = UUID('2631150c-54a4-4f0b-997c-b2bb9d4a6c2f')

        from HMoveOneTraceBackLinkDiffRulesLHS import HMoveOneTraceBackLinkDiffRulesLHS
        self.pre = HMoveOneTraceBackLinkDiffRulesLHS()
    
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
        # trace_link21
        new_node = graph.add_node()
        labels['21'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # backward_link22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'backward_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # trace_link21 -> MetaModelElement_S7
        graph.add_edges([(labels['21'], labels['7'])])
        # MetaModelElement_T9 -> trace_link21
        graph.add_edges([(labels['9'], labels['21'])])
        # backward_link22 -> MetaModelElement_S7
        graph.add_edges([(labels['22'], labels['7'])])
        # MetaModelElement_T9 -> backward_link22
        graph.add_edges([(labels['9'], labels['22'])])
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        # MetaModelElement_S7
        packet.global_pivots['element1'] = graph.vs[labels['7']][Himesis.Constants.GUID]
        # MetaModelElement_S8
        packet.global_pivots['element2'] = graph.vs[labels['8']][Himesis.Constants.GUID]
        
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
        # MT_pre__trace_link11, MT_pre__backward_link10
        graph.delete_nodes([labels["11"], labels["10"]])
    
