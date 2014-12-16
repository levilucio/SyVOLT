

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HSM2SM_combine_1RHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_combine_1RHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_combine_1RHS, self).__init__(name='HSM2SM_combine_1RHS', num_nodes=20, edges=[])
        
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
        self["GUID__"] = UUID('646f10b9-9e25-4ef5-bdce-fa6fa5f7f124')
        
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
        self.vs[0]["MT_label__"] = """50"""
        self.vs[0]["mm__"] = """MT_post__directLink_T"""
        self.vs[0]["GUID__"] = UUID('4dac2a7b-5abd-492e-8b38-84e10dea1537')
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
        self.vs[1]["GUID__"] = UUID('f1a6be66-2695-4836-9eea-9e3da5b38f22')
        self.vs[2]["MT_label__"] = """8"""
        self.vs[2]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[2]["GUID__"] = UUID('b3c1ccbd-8f7d-4a8f-8ed0-06b785e7743f')
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
        self.vs[3]["GUID__"] = UUID('064a2c3f-dc6d-46a2-9c91-62f383e93e68')
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
        self.vs[4]["GUID__"] = UUID('84146857-4b71-4655-bca4-357d9b66f887')
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
        self.vs[5]["GUID__"] = UUID('dbcee759-56cb-42bb-80ca-050e13d00979')
        self.vs[6]["MT_label__"] = """12"""
        self.vs[6]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value\u000a# of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn attr_value\u000a
p1
.""")
        self.vs[6]["mm__"] = """MT_post__Attribute"""
        self.vs[6]["GUID__"] = UUID('a7e5983d-df25-486f-af19-af8313bc4a37')
        self.vs[7]["MT_label__"] = """16"""
        self.vs[7]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value\u000a# of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn attr_value\u000a
p1
.""")
        self.vs[7]["mm__"] = """MT_post__Attribute"""
        self.vs[7]["GUID__"] = UUID('48927f53-8188-4ff8-b07c-668795be1b70')
        self.vs[8]["MT_label__"] = """20"""
        self.vs[8]["mm__"] = """MT_post__rightExpr"""
        self.vs[8]["GUID__"] = UUID('ce58dc99-322e-4ffd-8ce5-e647be43802e')
        self.vs[9]["MT_label__"] = """23"""
        self.vs[9]["mm__"] = """MT_post__rightExpr"""
        self.vs[9]["GUID__"] = UUID('a20ea26c-53e9-4559-b2af-52d55a486781')
        self.vs[10]["MT_label__"] = """13"""
        self.vs[10]["mm__"] = """MT_post__Equation"""
        self.vs[10]["GUID__"] = UUID('4e6227ef-47b8-4d74-b78b-91674f240577')
        self.vs[11]["MT_label__"] = """17"""
        self.vs[11]["mm__"] = """MT_post__Equation"""
        self.vs[11]["GUID__"] = UUID('34634efd-aca2-475e-b8b2-5e14a1bb2a15')
        self.vs[12]["MT_label__"] = """6"""
        self.vs[12]["mm__"] = """MT_post__trace_link"""
        self.vs[12]["GUID__"] = UUID('e4a8751e-4877-4ff9-a933-454e6ad91d30')
        self.vs[13]["MT_label__"] = """7"""
        self.vs[13]["mm__"] = """MT_post__trace_link"""
        self.vs[13]["GUID__"] = UUID('12b59d2a-893c-4f4b-a5af-ab2f6d2afe1d')
        self.vs[14]["MT_label__"] = """19"""
        self.vs[14]["mm__"] = """MT_post__leftExpr"""
        self.vs[14]["GUID__"] = UUID('a86f227b-4d15-4407-badf-ad1f19efb36c')
        self.vs[15]["MT_label__"] = """22"""
        self.vs[15]["mm__"] = """MT_post__leftExpr"""
        self.vs[15]["GUID__"] = UUID('601e9764-8de0-4149-b835-bd8e43cf1b44')
        self.vs[16]["MT_label__"] = """11"""
        self.vs[16]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[16]["GUID__"] = UUID('3b17530a-8ba0-4fdc-b7b5-aff70bc5e420')
        self.vs[17]["MT_label__"] = """21"""
        self.vs[17]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[17]["GUID__"] = UUID('97c46e20-0c96-4269-8446-dfa4cd391145')
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
        self.vs[18]["GUID__"] = UUID('08d76551-d26a-4f8f-9cb5-5e3851d8bb7e')
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
        self.vs[19]["GUID__"] = UUID('6ecbcd3b-652c-4915-ae02-7f1351441da7')

        from HSM2SM_combine_1LHS import HSM2SM_combine_1LHS
        self.pre = HSM2SM_combine_1LHS()
    
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
        # directLink_T50
        new_node = graph.add_node()
        labels['50'] = new_node
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
        # leftExpr19
        new_node = graph.add_node()
        labels['19'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
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
        # Equation13 -> rightExpr20
        graph.add_edges((labels['13'], labels['20']))
        # Equation13 -> leftExpr19
        graph.add_edges((labels['13'], labels['19']))
        # rightExpr20 -> Constant14
        graph.add_edges((labels['20'], labels['14']))
        # Equation17 -> rightExpr23
        graph.add_edges((labels['17'], labels['23']))
        # Equation17 -> leftExpr22
        graph.add_edges((labels['17'], labels['22']))
        # rightExpr23 -> Constant18
        graph.add_edges((labels['23'], labels['18']))
        # leftExpr19 -> Attribute12
        graph.add_edges((labels['19'], labels['12']))
        # leftExpr22 -> Attribute16
        graph.add_edges((labels['22'], labels['16']))
        # Station_T3 -> directLink_T50
        graph.add_edges((labels['3'], labels['50']))
        # directLink_T50 -> Male_T4
        graph.add_edges((labels['50'], labels['4']))
        
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
    
