

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
        self["GUID__"] = UUID('70b79780-cc68-4108-aac1-86ecf481b151')
        
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
        self.vs[0]["MT_label__"] = """8"""
        self.vs[0]["mm__"] = """MT_post__directLink_T"""
        self.vs[0]["GUID__"] = UUID('cdfe6cd5-7a45-4bf8-9eba-e57cd7dfb499')
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[1]["GUID__"] = UUID('991a3363-09cc-46cb-b002-16ce17369f6c')
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["GUID__"] = UUID('94730ef3-0384-4ecf-989d-f8fb2817c9b4')
        self.vs[3]["MT_label__"] = """6"""
        self.vs[3]["mm__"] = """MT_post__trace_link"""
        self.vs[3]["GUID__"] = UUID('af7c08fb-1ddf-42a1-a2d6-47387265f80b')
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
        self.vs[4]["GUID__"] = UUID('d8bc07ed-adf5-4813-baf0-8cd19f55fabd')
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
        self.vs[5]["GUID__"] = UUID('2455ec24-5134-4789-8977-6be89f21e7df')
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
        self.vs[6]["GUID__"] = UUID('020586a3-97e6-406f-9ec4-05b5c84cc1a9')
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
        self.vs[7]["GUID__"] = UUID('74404ece-d48b-4a29-95ae-5185995ed45b')

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
        # directLink_T8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # indirectLink_S9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'indirectLink_S'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Female_T3 -> directLink_T8
        graph.add_edges((labels['3'], labels['8']))
        # directLink_T8 -> Female_T4
        graph.add_edges((labels['8'], labels['4']))
        # Female_S1 -> indirectLink_S9
        graph.add_edges((labels['1'], labels['9']))
        # indirectLink_S9 -> Female_S2
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
    
