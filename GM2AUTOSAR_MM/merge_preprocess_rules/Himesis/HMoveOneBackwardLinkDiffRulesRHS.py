

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HMoveOneBackwardLinkDiffRulesRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneBackwardLinkDiffRulesRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneBackwardLinkDiffRulesRHS, self).__init__(name='HMoveOneBackwardLinkDiffRulesRHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([(1, 2), (0, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__GM2AUTOSAR_MM'
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
        self["GUID__"] = UUID('37b5df85-45d3-4aac-97a8-083f719d2494')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """9"""
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
        self.vs[0]["mm__"] = """MT_post__MetaModelElement_T"""
        self.vs[0]["MT_post__classtype"] = """
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
        self.vs[0]["GUID__"] = UUID('b21ff3fa-5a4e-4881-8d2a-9a92677d96cb')
        self.vs[1]["MT_label__"] = """14"""
        self.vs[1]["mm__"] = """MT_post__backward_link"""
        self.vs[1]["GUID__"] = UUID('1a660f65-35f1-41d4-9824-059362c035a8')
        self.vs[2]["MT_pivotOut__"] = """element1"""
        self.vs[2]["MT_label__"] = """7"""
        self.vs[2]["MT_post__name"] = """
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
        self.vs[2]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[2]["MT_post__classtype"] = """
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
        self.vs[2]["GUID__"] = UUID('7cdbeba6-e1d5-4a63-a063-17343587f122')
        self.vs[3]["MT_pivotOut__"] = """element2"""
        self.vs[3]["MT_label__"] = """8"""
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
        self.vs[3]["GUID__"] = UUID('42ec575c-4b35-48dd-a659-23c96017ea9f')

        from HMoveOneBackwardLinkDiffRulesLHS import HMoveOneBackwardLinkDiffRulesLHS
        self.pre = HMoveOneBackwardLinkDiffRulesLHS()
    
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
        # backward_link14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'backward_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # backward_link14 -> MetaModelElement_S7
        graph.add_edges([(labels['14'], labels['7'])])
        # MetaModelElement_T9 -> backward_link14
        graph.add_edges([(labels['9'], labels['14'])])
        
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
        # MT_pre__backward_link13
        graph.delete_nodes([labels["13"]])
    
