

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HSF2SF_combine_1RHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_combine_1RHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_combine_1RHS, self).__init__(name='HSF2SF_combine_1RHS', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([(16, 6), (14, 6), (15, 7), (17, 7), (5, 0), (0, 2), (10, 8), (8, 18), (11, 9), (9, 19), (10, 14), (11, 15), (5, 12), (12, 4), (2, 13), (13, 3), (4, 1), (1, 3), (3, 17), (4, 16)])
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
        self["GUID__"] = UUID('8eb2eb83-94a1-45ee-85ab-4699fa93d0bb')
        
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
        self.vs[0]["MT_label__"] = """24"""
        self.vs[0]["mm__"] = """MT_post__directLink_T"""
        self.vs[0]["GUID__"] = UUID('ed1f4a88-a13a-4387-a978-7006c750742b')
        self.vs[1]["MT_label__"] = """10"""
        self.vs[1]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[1]["GUID__"] = UUID('874d7827-f596-41bb-8594-8468bb177c6e')
        self.vs[2]["MT_label__"] = """4"""
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
        self.vs[2]["mm__"] = """MT_post__Female_T"""
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
        self.vs[2]["GUID__"] = UUID('71faf79e-2e6f-471f-9507-8ca144397d69')
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
        self.vs[3]["MT_label__"] = """2"""
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
        self.vs[3]["mm__"] = """MT_post__Female_S"""
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
        self.vs[3]["GUID__"] = UUID('eddfd9a1-b8a4-4a8f-89d4-89a467724a30')
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
        self.vs[4]["GUID__"] = UUID('361e9d9f-210e-4959-9cbf-132b4288df98')
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
        self.vs[5]["GUID__"] = UUID('b8206bb6-afc8-41e7-961a-f6c279958fdb')
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
        self.vs[6]["GUID__"] = UUID('1a8996db-08d9-46cd-b9fe-ab2b5c1674cc')
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
        self.vs[7]["GUID__"] = UUID('d82c7867-0333-4040-a7b9-e9a79b91d400')
        self.vs[8]["MT_label__"] = """20"""
        self.vs[8]["mm__"] = """MT_post__rightExpr"""
        self.vs[8]["GUID__"] = UUID('04223430-020c-422c-b781-31ba76e806a6')
        self.vs[9]["MT_label__"] = """23"""
        self.vs[9]["mm__"] = """MT_post__rightExpr"""
        self.vs[9]["GUID__"] = UUID('33bb371c-31fd-4cfa-ab67-3705c68d091e')
        self.vs[10]["MT_label__"] = """13"""
        self.vs[10]["mm__"] = """MT_post__Equation"""
        self.vs[10]["GUID__"] = UUID('cf06ebad-fa3f-4938-8df8-8fbbc2b7c0fb')
        self.vs[11]["MT_label__"] = """17"""
        self.vs[11]["mm__"] = """MT_post__Equation"""
        self.vs[11]["GUID__"] = UUID('eb719e1c-ada0-45e9-9e20-e193c166722c')
        self.vs[12]["MT_label__"] = """5"""
        self.vs[12]["mm__"] = """MT_post__trace_link"""
        self.vs[12]["GUID__"] = UUID('b50b2e5a-8fdc-43ac-a4ea-94a9bbbbba49')
        self.vs[13]["MT_label__"] = """6"""
        self.vs[13]["mm__"] = """MT_post__trace_link"""
        self.vs[13]["GUID__"] = UUID('96efe632-c79f-42ef-b0be-1964879a47cb')
        self.vs[14]["MT_label__"] = """19"""
        self.vs[14]["mm__"] = """MT_post__leftExpr"""
        self.vs[14]["GUID__"] = UUID('125468f0-9dcf-4f20-bd59-9fbf50358a0f')
        self.vs[15]["MT_label__"] = """22"""
        self.vs[15]["mm__"] = """MT_post__leftExpr"""
        self.vs[15]["GUID__"] = UUID('4c940ec8-3684-4625-9b04-e59267caba8e')
        self.vs[16]["MT_label__"] = """15"""
        self.vs[16]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[16]["GUID__"] = UUID('29470acc-0973-4d43-87ba-1563bd0f05b8')
        self.vs[17]["MT_label__"] = """25"""
        self.vs[17]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[17]["GUID__"] = UUID('1a2bb890-5cd6-4376-83b3-f196e44e8670')
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
        self.vs[18]["GUID__"] = UUID('9203b172-b041-47c4-a478-3317b17229b1')
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
        self.vs[19]["GUID__"] = UUID('09e2045d-04ba-4abc-906c-de168efaca85')

        from HSF2SF_combine_1LHS import HSF2SF_combine_1LHS
        self.pre = HSF2SF_combine_1LHS()
    
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
        # directLink_T24
        new_node = graph.add_node()
        labels['24'] = new_node
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
        # hasAttr_S15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_S'
        # hasAttr_S25
        new_node = graph.add_node()
        labels['25'] = new_node
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
        # hasAttr_S15 -> Attribute12
        graph.add_edges((labels['15'], labels['12']))
        # leftExpr19 -> Attribute12
        graph.add_edges((labels['19'], labels['12']))
        # Equation13 -> rightExpr20
        graph.add_edges((labels['13'], labels['20']))
        # Equation13 -> leftExpr19
        graph.add_edges((labels['13'], labels['19']))
        # rightExpr20 -> Constant14
        graph.add_edges((labels['20'], labels['14']))
        # Station_S1 -> hasAttr_S15
        graph.add_edges((labels['1'], labels['15']))
        # leftExpr22 -> Attribute16
        graph.add_edges((labels['22'], labels['16']))
        # hasAttr_S25 -> Attribute16
        graph.add_edges((labels['25'], labels['16']))
        # Equation17 -> rightExpr23
        graph.add_edges((labels['17'], labels['23']))
        # Equation17 -> leftExpr22
        graph.add_edges((labels['17'], labels['22']))
        # rightExpr23 -> Constant18
        graph.add_edges((labels['23'], labels['18']))
        # Station_T3 -> directLink_T24
        graph.add_edges((labels['3'], labels['24']))
        # directLink_T24 -> Female_T4
        graph.add_edges((labels['24'], labels['4']))
        # Female_S2 -> hasAttr_S25
        graph.add_edges((labels['2'], labels['25']))
        
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
    
