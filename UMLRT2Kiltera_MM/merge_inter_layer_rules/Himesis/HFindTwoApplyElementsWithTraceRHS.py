

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HFindTwoApplyElementsWithTraceRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFindTwoApplyElementsWithTraceRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFindTwoApplyElementsWithTraceRHS, self).__init__(name='HFindTwoApplyElementsWithTraceRHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (4, 1), (2, 3), (3, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__GM2AUTOSAR_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = """cardinality1 = PostNode('3')['cardinality']
cardinality2 = PostNode('4')['cardinality']

if cardinality1 != cardinality2:
    PostNode('3')['cardinality'] = '+'
"""
        self["name"] = """"""
        self["GUID__"] = UUID('93aed66b-dea6-4fa6-8a73-eb0bada24431')
        
        # Set the node attributes
        self.vs[0]["MT_post__cardinality"] = """
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
        self.vs[0]["MT_label__"] = """5"""
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
        self.vs[0]["mm__"] = """MT_post__MetaModelElement_S"""
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
        self.vs[0]["GUID__"] = UUID('7760a9ab-2a49-47f1-9c57-36762542d124')
        self.vs[1]["MT_label__"] = """11"""
        self.vs[1]["mm__"] = """MT_post__trace_link"""
        self.vs[1]["GUID__"] = UUID('4831d275-510f-4438-ae17-519c6792506e')
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["mm__"] = """MT_post__ApplyModel"""
        self.vs[2]["GUID__"] = UUID('6bcef979-1dac-4981-a4da-f1dc051c746c')
        self.vs[3]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_post__apply_contains"""
        self.vs[3]["GUID__"] = UUID('be461811-fe4d-402b-ab10-c71ef3e79d30')
        self.vs[4]["MT_pivotOut__"] = """element1"""
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
        self.vs[4]["MT_label__"] = """3"""
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
        self.vs[4]["mm__"] = """MT_post__MetaModelElement_T"""
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
        self.vs[4]["GUID__"] = UUID('b3ba943e-0c6b-4f9d-8a43-5c9b3ae7e78a')
        self.vs[5]["MT_pivotOut__"] = """element2"""
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
        self.vs[5]["MT_label__"] = """4"""
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
        self.vs[5]["mm__"] = """MT_post__MetaModelElement_T"""
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
        self.vs[5]["GUID__"] = UUID('595f0748-435e-4d30-9c16-357e6c6c69a5')

        from HFindTwoApplyElementsWithTraceLHS import HFindTwoApplyElementsWithTraceLHS
        self.pre = HFindTwoApplyElementsWithTraceLHS()
    
    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        cardinality1 = PostNode('3')['cardinality']
        cardinality2 = PostNode('4')['cardinality']
        
        if cardinality1 != cardinality2:
            PostNode('3')['cardinality'] = '+'

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
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        # MetaModelElement_T3
        packet.global_pivots['element1'] = graph.vs[labels['3']][Himesis.Constants.GUID]
        # MetaModelElement_T4
        packet.global_pivots['element2'] = graph.vs[labels['4']][Himesis.Constants.GUID]
        
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
        # MT_pre__backward_link12
        graph.delete_nodes([labels["12"]])
    
