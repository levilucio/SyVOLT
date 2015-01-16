

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
        
        super(HSM2SM_combine_1RHS, self).__init__(name='HSM2SM_combine_1RHS', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([(21, 9), (17, 9), (22, 10), (18, 10), (8, 0), (0, 1), (24, 1), (1, 12), (8, 11), (11, 6), (12, 7), (15, 13), (13, 25), (16, 14), (14, 26), (15, 17), (16, 18), (2, 19), (2, 20), (2, 5), (6, 3), (3, 7), (19, 6), (20, 7), (5, 4), (4, 23), (4, 24), (6, 21), (7, 22), (23, 8)])
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
        self["GUID__"] = UUID('66fed645-3b33-4c2d-af39-8061d816f55f')
        
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
        self.vs[0]["GUID__"] = UUID('51b8f4f4-0430-40f5-9ca5-2b3fd6eae4ca')
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
        self.vs[1]["GUID__"] = UUID('d084582a-1422-4c38-90f5-309edec60609')
        self.vs[2]["MT_label__"] = """51"""
        self.vs[2]["mm__"] = """MT_post__MatchModel"""
        self.vs[2]["GUID__"] = UUID('73c14076-b17f-4f28-b887-80dcf6398215')
        self.vs[3]["MT_label__"] = """8"""
        self.vs[3]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('b3e3fe90-f2ba-4a85-bf70-364eb4513661')
        self.vs[4]["MT_label__"] = """52"""
        self.vs[4]["mm__"] = """MT_post__ApplyModel"""
        self.vs[4]["GUID__"] = UUID('9beff39a-840a-40d8-b9f9-52793d2e4577')
        self.vs[5]["MT_label__"] = """57"""
        self.vs[5]["mm__"] = """MT_post__paired_with"""
        self.vs[5]["GUID__"] = UUID('d5156cb2-31e6-4d43-b88b-44dd5b5bc1c3')
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
        self.vs[6]["mm__"] = """MT_post__Station_S"""
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
        self.vs[6]["GUID__"] = UUID('03473d24-8b96-440a-a2e1-fa7fd3165da7')
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
        self.vs[7]["mm__"] = """MT_post__Male_S"""
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
        self.vs[7]["GUID__"] = UUID('af342b26-e886-497a-91d6-3936caf08dde')
        self.vs[8]["MT_label__"] = """3"""
        self.vs[8]["MT_post__name"] = """
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
        self.vs[8]["mm__"] = """MT_post__Station_T"""
        self.vs[8]["MT_post__classtype"] = """
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
        self.vs[8]["GUID__"] = UUID('d1a5521b-7e55-4b16-bbdc-5d0bc47e3ef6')
        self.vs[9]["MT_label__"] = """12"""
        self.vs[9]["MT_post__name"] = """
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
        self.vs[9]["mm__"] = """MT_post__Attribute"""
        self.vs[9]["GUID__"] = UUID('521cb768-c60e-44bc-b65e-ad3deb2b352e')
        self.vs[10]["MT_label__"] = """16"""
        self.vs[10]["MT_post__name"] = """
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
        self.vs[10]["mm__"] = """MT_post__Attribute"""
        self.vs[10]["GUID__"] = UUID('debf25b7-f442-477b-9f30-1b6b625e5c92')
        self.vs[11]["MT_label__"] = """6"""
        self.vs[11]["mm__"] = """MT_post__trace_link"""
        self.vs[11]["GUID__"] = UUID('b01a59bd-6912-438e-87fb-9c79a52875ec')
        self.vs[12]["MT_label__"] = """7"""
        self.vs[12]["mm__"] = """MT_post__trace_link"""
        self.vs[12]["GUID__"] = UUID('78630cbd-6981-4674-b4e6-f4bc52ac8dc3')
        self.vs[13]["MT_label__"] = """20"""
        self.vs[13]["mm__"] = """MT_post__rightExpr"""
        self.vs[13]["GUID__"] = UUID('451e7c25-efb4-406c-aae2-66a14bae50ae')
        self.vs[14]["MT_label__"] = """23"""
        self.vs[14]["mm__"] = """MT_post__rightExpr"""
        self.vs[14]["GUID__"] = UUID('731cbc80-906e-4718-b7d6-60c6a470f464')
        self.vs[15]["MT_label__"] = """13"""
        self.vs[15]["mm__"] = """MT_post__Equation"""
        self.vs[15]["GUID__"] = UUID('ae73ba5b-b539-4126-8e5d-6a6ae76d25fb')
        self.vs[16]["MT_label__"] = """17"""
        self.vs[16]["mm__"] = """MT_post__Equation"""
        self.vs[16]["GUID__"] = UUID('e1efe855-6d1f-49e0-97e0-bd17aa2bc846')
        self.vs[17]["MT_label__"] = """19"""
        self.vs[17]["mm__"] = """MT_post__leftExpr"""
        self.vs[17]["GUID__"] = UUID('26848cd9-b699-46bb-a179-98753b845fc2')
        self.vs[18]["MT_label__"] = """22"""
        self.vs[18]["mm__"] = """MT_post__leftExpr"""
        self.vs[18]["GUID__"] = UUID('ab4d437e-71fb-4edf-a22b-95cd514f326c')
        self.vs[19]["MT_label__"] = """53"""
        self.vs[19]["mm__"] = """MT_post__match_contains"""
        self.vs[19]["GUID__"] = UUID('cf687f1a-bdd7-4684-96a3-703207540c6b')
        self.vs[20]["MT_label__"] = """54"""
        self.vs[20]["mm__"] = """MT_post__match_contains"""
        self.vs[20]["GUID__"] = UUID('d52b409b-1ff5-427b-8fca-de56c98f65fc')
        self.vs[21]["MT_label__"] = """11"""
        self.vs[21]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[21]["GUID__"] = UUID('537598ba-a263-4180-b0a7-cdf1ceca1457')
        self.vs[22]["MT_label__"] = """21"""
        self.vs[22]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[22]["GUID__"] = UUID('6e041014-696a-45c5-bea8-623fca5c5bb7')
        self.vs[23]["MT_label__"] = """55"""
        self.vs[23]["mm__"] = """MT_post__apply_contains"""
        self.vs[23]["GUID__"] = UUID('eb2e2184-47d2-4856-ad56-62638b40bc68')
        self.vs[24]["MT_label__"] = """56"""
        self.vs[24]["mm__"] = """MT_post__apply_contains"""
        self.vs[24]["GUID__"] = UUID('683bf36f-9023-49ac-94cb-a4c5791af02d')
        self.vs[25]["MT_label__"] = """14"""
        self.vs[25]["mm__"] = """MT_post__Constant"""
        self.vs[25]["MT_post__value"] = """
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
        self.vs[25]["GUID__"] = UUID('b69e3d2c-e48b-4a7b-b855-37dbd099b018')
        self.vs[26]["MT_label__"] = """18"""
        self.vs[26]["mm__"] = """MT_post__Constant"""
        self.vs[26]["MT_post__value"] = """
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
        self.vs[26]["GUID__"] = UUID('3d515cc1-b81a-4650-babe-dc072cc06904')

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
        # MatchModel51
        new_node = graph.add_node()
        labels['51'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # leftExpr19
        new_node = graph.add_node()
        labels['19'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # match_contains53
        new_node = graph.add_node()
        labels['53'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # match_contains54
        new_node = graph.add_node()
        labels['54'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # ApplyModel52
        new_node = graph.add_node()
        labels['52'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # paired_with57
        new_node = graph.add_node()
        labels['57'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # apply_contains55
        new_node = graph.add_node()
        labels['55'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains56
        new_node = graph.add_node()
        labels['56'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
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
        # MatchModel51 -> match_contains53
        graph.add_edges((labels['51'], labels['53']))
        # MatchModel51 -> match_contains54
        graph.add_edges((labels['51'], labels['54']))
        # MatchModel51 -> paired_with57
        graph.add_edges((labels['51'], labels['57']))
        # paired_with57 -> ApplyModel52
        graph.add_edges((labels['57'], labels['52']))
        # ApplyModel52 -> apply_contains55
        graph.add_edges((labels['52'], labels['55']))
        # ApplyModel52 -> apply_contains56
        graph.add_edges((labels['52'], labels['56']))
        # match_contains53 -> Station_S1
        graph.add_edges((labels['53'], labels['1']))
        # match_contains54 -> Male_S2
        graph.add_edges((labels['54'], labels['2']))
        # apply_contains55 -> Station_T3
        graph.add_edges((labels['55'], labels['3']))
        # apply_contains56 -> Male_T4
        graph.add_edges((labels['56'], labels['4']))
        
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
    
