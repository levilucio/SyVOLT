

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HSM2SM_combine_0RHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_combine_0RHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_combine_0RHS, self).__init__(name='HSM2SM_combine_0RHS', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([(16, 6), (14, 6), (17, 7), (15, 7), (5, 0), (0, 1), (1, 13), (10, 8), (8, 18), (11, 9), (9, 19), (10, 14), (11, 15), (5, 12), (12, 3), (13, 4), (3, 2), (2, 4), (3, 16), (4, 17)])
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
        self["GUID__"] = UUID('c7868d70-7b95-4028-b2e6-0dbedc07c5a1')
        
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
        self.vs[0]["GUID__"] = UUID('2181da46-23eb-4c06-8eb6-476d24f59ac6')
        self.vs[1]["MT_label__"] = """4"""
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
        self.vs[1]["mm__"] = """MT_post__Male_T"""
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
        self.vs[1]["GUID__"] = UUID('790dfafc-f3e5-47bc-83b5-689c235ed6b6')
        self.vs[2]["MT_label__"] = """10"""
        self.vs[2]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[2]["GUID__"] = UUID('28d75810-8445-48b2-beb6-093f5bcc0b8e')
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
        self.vs[3]["MT_label__"] = """1"""
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
        self.vs[3]["mm__"] = """MT_post__Station_S"""
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
        self.vs[3]["GUID__"] = UUID('50cc6b50-e5a1-41d0-b6d7-86f1ea515032')
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
        self.vs[4]["MT_label__"] = """2"""
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
        self.vs[4]["mm__"] = """MT_post__Male_S"""
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
        self.vs[4]["GUID__"] = UUID('dc16eb9c-1aa5-4e74-b134-41d6ff3f7c53')
        self.vs[5]["MT_label__"] = """3"""
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
        self.vs[5]["mm__"] = """MT_post__Station_T"""
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
        self.vs[5]["GUID__"] = UUID('e0dacb21-a458-4728-8177-530abf0c2b35')
        self.vs[6]["MT_label__"] = """12"""
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

return "name"
"""
        self.vs[6]["mm__"] = """MT_post__Attribute"""
        self.vs[6]["GUID__"] = UUID('ac2ad86b-dfd9-4ee5-b036-4d626c0fde2e')
        self.vs[7]["MT_label__"] = """16"""
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

return "name"
"""
        self.vs[7]["mm__"] = """MT_post__Attribute"""
        self.vs[7]["GUID__"] = UUID('29ecf2e6-e802-416d-aa24-906907ed694f')
        self.vs[8]["MT_label__"] = """20"""
        self.vs[8]["mm__"] = """MT_post__rightExpr"""
        self.vs[8]["GUID__"] = UUID('8807e23d-d04b-40c2-83e3-3b8f629eaea4')
        self.vs[9]["MT_label__"] = """23"""
        self.vs[9]["mm__"] = """MT_post__rightExpr"""
        self.vs[9]["GUID__"] = UUID('9b0d459b-ec6d-43e7-868c-5275ff3270d1')
        self.vs[10]["MT_label__"] = """13"""
        self.vs[10]["mm__"] = """MT_post__Equation"""
        self.vs[10]["GUID__"] = UUID('166095a0-5f46-4973-971a-1b1581601d96')
        self.vs[11]["MT_label__"] = """17"""
        self.vs[11]["mm__"] = """MT_post__Equation"""
        self.vs[11]["GUID__"] = UUID('a7d2a5ba-0b38-429f-82bf-ec1f903dccd9')
        self.vs[12]["MT_label__"] = """6"""
        self.vs[12]["mm__"] = """MT_post__trace_link"""
        self.vs[12]["GUID__"] = UUID('49b09203-c05f-4c8b-a82e-e089c5012492')
        self.vs[13]["MT_label__"] = """7"""
        self.vs[13]["mm__"] = """MT_post__trace_link"""
        self.vs[13]["GUID__"] = UUID('012cdfaf-2d1b-4c24-b153-b58cf7dc5b1d')
        self.vs[14]["MT_label__"] = """19"""
        self.vs[14]["mm__"] = """MT_post__leftExpr"""
        self.vs[14]["GUID__"] = UUID('5ad14dee-65ff-4914-9f0a-a37bfe9691c2')
        self.vs[15]["MT_label__"] = """22"""
        self.vs[15]["mm__"] = """MT_post__leftExpr"""
        self.vs[15]["GUID__"] = UUID('0d02c1a2-7f8b-4a81-b7ac-55e10292aae4')
        self.vs[16]["MT_label__"] = """15"""
        self.vs[16]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[16]["GUID__"] = UUID('32b215e3-7c9c-409b-b220-4a41ded0fa64')
        self.vs[17]["MT_label__"] = """21"""
        self.vs[17]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[17]["GUID__"] = UUID('bf762305-9cb0-42cb-b8e9-9d750000262a')
        self.vs[18]["MT_label__"] = """14"""
        self.vs[18]["mm__"] = """MT_post__Constant"""
        self.vs[18]["MT_post__value"] = """
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
"""
        self.vs[18]["GUID__"] = UUID('e3dcc521-4cf6-47fb-8f31-2614f254550f')
        self.vs[19]["MT_label__"] = """18"""
        self.vs[19]["mm__"] = """MT_post__Constant"""
        self.vs[19]["MT_post__value"] = """
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

return "somemale"
"""
        self.vs[19]["GUID__"] = UUID('2416bcf2-a9d8-4ad0-a223-b180ae9b444a')

        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        self.pre = HSM2SM_combine_0LHS()
    
    def set_name12(self, attr_value, PreNode, graph):
        
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


    def set_name16(self, attr_value, PreNode, graph):
        
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


    def set_value14(self, attr_value, PreNode, graph):
        
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


    def set_value18(self, attr_value, PreNode, graph):
        
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
        
        return "somemale"


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
        # Attribute12
        new_node = graph.add_node()
        labels['12'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        try:
            graph.vs[new_node]['name'] = self.set_name12(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Attribute16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        try:
            graph.vs[new_node]['name'] = self.set_name16(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # directLink_T11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # rightExpr20
        new_node = graph.add_node()
        labels['20'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr23
        new_node = graph.add_node()
        labels['23'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation13
        new_node = graph.add_node()
        labels['13'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation17
        new_node = graph.add_node()
        labels['17'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # indirectLink_S10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'indirectLink_S'
        # leftExpr19
        new_node = graph.add_node()
        labels['19'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # hasAttr_S15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_S'
        # hasAttr_S21
        new_node = graph.add_node()
        labels['21'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_S'
        # Constant14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['value'] = self.set_value14(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'value\'', e)
        # Constant18
        new_node = graph.add_node()
        labels['18'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['value'] = self.set_value18(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'value\'', e)
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Station_S1 -> indirectLink_S10
        graph.add_edges([(labels['1'], labels['10'])])
        # indirectLink_S10 -> Male_S2
        graph.add_edges([(labels['10'], labels['2'])])
        # Station_T3 -> directLink_T11
        graph.add_edges([(labels['3'], labels['11'])])
        # directLink_T11 -> Male_T4
        graph.add_edges([(labels['11'], labels['4'])])
        # hasAttr_S15 -> Attribute12
        graph.add_edges([(labels['15'], labels['12'])])
        # leftExpr19 -> Attribute12
        graph.add_edges([(labels['19'], labels['12'])])
        # Equation13 -> rightExpr20
        graph.add_edges([(labels['13'], labels['20'])])
        # Equation13 -> leftExpr19
        graph.add_edges([(labels['13'], labels['19'])])
        # rightExpr20 -> Constant14
        graph.add_edges([(labels['20'], labels['14'])])
        # Station_S1 -> hasAttr_S15
        graph.add_edges([(labels['1'], labels['15'])])
        # hasAttr_S21 -> Attribute16
        graph.add_edges([(labels['21'], labels['16'])])
        # leftExpr22 -> Attribute16
        graph.add_edges([(labels['22'], labels['16'])])
        # Equation17 -> rightExpr23
        graph.add_edges([(labels['17'], labels['23'])])
        # Equation17 -> leftExpr22
        graph.add_edges([(labels['17'], labels['22'])])
        # rightExpr23 -> Constant18
        graph.add_edges([(labels['23'], labels['18'])])
        # Male_S2 -> hasAttr_S21
        graph.add_edges([(labels['2'], labels['21'])])
        
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
    
