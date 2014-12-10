

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HTraceabilityConstructionRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTraceabilityConstructionRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTraceabilityConstructionRHS, self).__init__(name='HTraceabilityConstructionRHS', num_nodes=3, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (2, 1)])
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
        self["GUID__"] = UUID('7eb20ba4-3d22-4792-a06b-29e486474b3c')
        
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
        self.vs[0]["MT_label__"] = """1"""
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
        self.vs[0]["GUID__"] = UUID('6920e0e3-5966-4122-b3ce-b768b9ec921e')
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["mm__"] = """MT_post__trace_link"""
        self.vs[1]["GUID__"] = UUID('da369dd1-a206-481a-836f-a951ab0e933c')
        self.vs[2]["MT_label__"] = """2"""
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
        self.vs[2]["mm__"] = """MT_post__MetaModelElement_T"""
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
        self.vs[2]["GUID__"] = UUID('723a03a0-8a31-45be-8f7a-560e923eb878')

        from HTraceabilityConstructionLHS import HTraceabilityConstructionLHS
        self.pre = HTraceabilityConstructionLHS()
    
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
        # trace_link3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # trace_link3 -> MetaModelElement_S1
        graph.add_edges([(labels['3'], labels['1'])])
        # MetaModelElement_T2 -> trace_link3
        graph.add_edges([(labels['2'], labels['3'])])
        
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
    
