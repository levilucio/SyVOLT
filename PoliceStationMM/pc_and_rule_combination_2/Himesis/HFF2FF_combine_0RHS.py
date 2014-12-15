

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HFF2FF_combine_0RHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_combine_0RHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_combine_0RHS, self).__init__(name='HFF2FF_combine_0RHS', num_nodes=8, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 5), (4, 2), (2, 6), (5, 3), (3, 7), (6, 1), (1, 7)])
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
        self["GUID__"] = UUID('b3305fb2-543b-4cb4-a97b-a646762a7d99')
        
        # Set the node attributes
        self.vs[0]["MT_post__associationType"] = """
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
        self.vs[0]["MT_label__"] = """11"""
        self.vs[0]["mm__"] = """MT_post__directLink_T"""
        self.vs[0]["GUID__"] = UUID('c3371759-9a57-4ad0-a5bf-60e73db272ab')
        self.vs[1]["MT_label__"] = """10"""
        self.vs[1]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[1]["GUID__"] = UUID('ec39e6b8-d06d-4098-a18e-1a44c17ea5fc')
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["GUID__"] = UUID('17ecf412-e03b-4171-8b3f-9e3ce433e9d0')
        self.vs[3]["MT_label__"] = """6"""
        self.vs[3]["mm__"] = """MT_post__trace_link"""
        self.vs[3]["GUID__"] = UUID('b68bbcb3-e6d4-40c7-a436-125b659ec41b')
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
        self.vs[4]["mm__"] = """MT_post__Female_T"""
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
        self.vs[4]["GUID__"] = UUID('6889c7f1-9fc9-428f-8dab-9c459e6b413d')
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
        self.vs[5]["mm__"] = """MT_post__Female_T"""
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
        self.vs[5]["GUID__"] = UUID('305c8adb-61f2-425e-aad7-9d502f63cad4')
        self.vs[6]["MT_post__cardinality"] = """
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
        self.vs[6]["MT_label__"] = """1"""
        self.vs[6]["MT_post__name"] = """
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
        self.vs[6]["mm__"] = """MT_post__Female_S"""
        self.vs[6]["MT_post__classtype"] = """
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
        self.vs[6]["GUID__"] = UUID('e9e69c9d-6767-4169-9c41-6721ddc3fda3')
        self.vs[7]["MT_post__cardinality"] = """
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
        self.vs[7]["MT_label__"] = """2"""
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
        self.vs[7]["mm__"] = """MT_post__Female_S"""
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
        self.vs[7]["GUID__"] = UUID('7f5096d8-d720-48cb-9c16-10cf2e58f01e')

        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        self.pre = HFF2FF_combine_0LHS()
    
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
        # directLink_T11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # indirectLink_S10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'indirectLink_S'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Female_S1 -> indirectLink_S10
        graph.add_edges((labels['1'], labels['10']))
        # indirectLink_S10 -> Female_S2
        graph.add_edges((labels['10'], labels['2']))
        # Female_T3 -> directLink_T11
        graph.add_edges((labels['3'], labels['11']))
        # directLink_T11 -> Female_T4
        graph.add_edges((labels['11'], labels['4']))
        
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
    
