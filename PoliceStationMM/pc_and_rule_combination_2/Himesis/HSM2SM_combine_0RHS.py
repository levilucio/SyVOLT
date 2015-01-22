

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
        
        super(HSM2SM_combine_0RHS, self).__init__(name='HSM2SM_combine_0RHS', num_nodes=27, edges=[])
        
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
        self["GUID__"] = UUID('2e9694cc-2ccc-48fb-ac04-d19d7df2fdaf')
        
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
        self.vs[0]["GUID__"] = UUID('fd86c463-104c-4f5d-afc5-5de301b2bd17')
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
        self.vs[1]["GUID__"] = UUID('e1085aec-3d44-470a-8fa4-3a456dba200c')
        self.vs[2]["MT_label__"] = """36"""
        self.vs[2]["mm__"] = """MT_post__MatchModel"""
        self.vs[2]["GUID__"] = UUID('c622fa0b-eb0d-45ef-a42f-e612d60e2d6e')
        self.vs[3]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('51323994-d7e4-4319-8a81-e5f1bc70daa1')
        self.vs[4]["MT_label__"] = """35"""
        self.vs[4]["mm__"] = """MT_post__ApplyModel"""
        self.vs[4]["GUID__"] = UUID('e57a13e4-0b7f-418f-b6c0-e049e52cf0da')
        self.vs[5]["MT_label__"] = """41"""
        self.vs[5]["mm__"] = """MT_post__paired_with"""
        self.vs[5]["GUID__"] = UUID('09eed243-fe01-464f-9f26-bd8e4605f007')
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
        self.vs[6]["GUID__"] = UUID('383415bf-0105-4abf-a679-03e612ce4412')
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
        self.vs[7]["GUID__"] = UUID('8ad91e0d-31e4-4b9e-bb3d-e16acbcd09c2')
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
        self.vs[8]["GUID__"] = UUID('581f7101-ec85-4950-848a-d8ce8b18cbc0')
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
        self.vs[9]["GUID__"] = UUID('57a0249f-cd6f-486e-b8fb-f98915b9c208')
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
        self.vs[10]["GUID__"] = UUID('d378fea7-1f92-4a27-ae3c-f933650c4487')
        self.vs[11]["MT_label__"] = """6"""
        self.vs[11]["mm__"] = """MT_post__trace_link"""
        self.vs[11]["GUID__"] = UUID('42c4b872-e544-4963-b1b2-14b8cdbebe04')
        self.vs[12]["MT_label__"] = """7"""
        self.vs[12]["mm__"] = """MT_post__trace_link"""
        self.vs[12]["GUID__"] = UUID('700e8766-b355-482a-9b3a-3509ace321a3')
        self.vs[13]["MT_label__"] = """20"""
        self.vs[13]["mm__"] = """MT_post__rightExpr"""
        self.vs[13]["GUID__"] = UUID('30317102-3bb5-405a-b8d2-d10a76c64403')
        self.vs[14]["MT_label__"] = """23"""
        self.vs[14]["mm__"] = """MT_post__rightExpr"""
        self.vs[14]["GUID__"] = UUID('b6448154-69e4-45f5-b6cb-6debf7a931b6')
        self.vs[15]["MT_label__"] = """13"""
        self.vs[15]["mm__"] = """MT_post__Equation"""
        self.vs[15]["GUID__"] = UUID('dc7db3df-3789-4a91-ac70-128f3c6c9d55')
        self.vs[16]["MT_label__"] = """17"""
        self.vs[16]["mm__"] = """MT_post__Equation"""
        self.vs[16]["GUID__"] = UUID('b48a7bfe-bce5-4ca6-ad24-cdc30e45308b')
        self.vs[17]["MT_label__"] = """19"""
        self.vs[17]["mm__"] = """MT_post__leftExpr"""
        self.vs[17]["GUID__"] = UUID('3087c62b-6c23-42a6-9b5a-db5356241382')
        self.vs[18]["MT_label__"] = """22"""
        self.vs[18]["mm__"] = """MT_post__leftExpr"""
        self.vs[18]["GUID__"] = UUID('0b155260-781d-413d-8eef-d31a5ff72348')
        self.vs[19]["MT_label__"] = """37"""
        self.vs[19]["mm__"] = """MT_post__match_contains"""
        self.vs[19]["GUID__"] = UUID('39cdc5ec-b06d-478e-8919-b5274035e2e6')
        self.vs[20]["MT_label__"] = """38"""
        self.vs[20]["mm__"] = """MT_post__match_contains"""
        self.vs[20]["GUID__"] = UUID('b979e2af-6490-461a-8058-157bf675f7a1')
        self.vs[21]["MT_label__"] = """31"""
        self.vs[21]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[21]["GUID__"] = UUID('989f6165-03ac-4f1b-869b-fb6a04864c74')
        self.vs[22]["MT_label__"] = """33"""
        self.vs[22]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[22]["GUID__"] = UUID('d39b8718-3cfc-4c34-947b-d923b1f16f6a')
        self.vs[23]["MT_label__"] = """39"""
        self.vs[23]["mm__"] = """MT_post__apply_contains"""
        self.vs[23]["GUID__"] = UUID('5c2404ff-f5d4-4b8a-8166-2afdea232006')
        self.vs[24]["MT_label__"] = """40"""
        self.vs[24]["mm__"] = """MT_post__apply_contains"""
        self.vs[24]["GUID__"] = UUID('8539910b-08b0-45ea-b3d2-7bcaea5c332a')
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
        self.vs[25]["GUID__"] = UUID('76df66e8-bbb4-4a17-b815-921066981a78')
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
        self.vs[26]["GUID__"] = UUID('f1d2de03-c93e-4da6-9d17-56501b19998e')

        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        self.pre = HSM2SM_combine_0LHS()
    
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
        # MatchModel36
        new_node = graph.add_node()
        labels['36'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
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
        # match_contains37
        new_node = graph.add_node()
        labels['37'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # match_contains38
        new_node = graph.add_node()
        labels['38'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # ApplyModel35
        new_node = graph.add_node()
        labels['35'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # paired_with41
        new_node = graph.add_node()
        labels['41'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # apply_contains39
        new_node = graph.add_node()
        labels['39'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains40
        new_node = graph.add_node()
        labels['40'] = new_node
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
        # Station_S1 -> indirectLink_S10
        graph.add_edges([(labels['1'], labels['10'])])
        # indirectLink_S10 -> Male_S2
        graph.add_edges([(labels['10'], labels['2'])])
        # Station_T3 -> directLink_T11
        graph.add_edges([(labels['3'], labels['11'])])
        # directLink_T11 -> Male_T4
        graph.add_edges([(labels['11'], labels['4'])])
        # Equation13 -> rightExpr20
        graph.add_edges([(labels['13'], labels['20'])])
        # Equation13 -> leftExpr19
        graph.add_edges([(labels['13'], labels['19'])])
        # rightExpr20 -> Constant14
        graph.add_edges([(labels['20'], labels['14'])])
        # Equation17 -> rightExpr23
        graph.add_edges([(labels['17'], labels['23'])])
        # Equation17 -> leftExpr22
        graph.add_edges([(labels['17'], labels['22'])])
        # rightExpr23 -> Constant18
        graph.add_edges([(labels['23'], labels['18'])])
        # leftExpr19 -> Attribute12
        graph.add_edges([(labels['19'], labels['12'])])
        # leftExpr22 -> Attribute16
        graph.add_edges([(labels['22'], labels['16'])])
        # paired_with41 -> ApplyModel35
        graph.add_edges([(labels['41'], labels['35'])])
        # ApplyModel35 -> apply_contains39
        graph.add_edges([(labels['35'], labels['39'])])
        # ApplyModel35 -> apply_contains40
        graph.add_edges([(labels['35'], labels['40'])])
        # MatchModel36 -> match_contains37
        graph.add_edges([(labels['36'], labels['37'])])
        # MatchModel36 -> match_contains38
        graph.add_edges([(labels['36'], labels['38'])])
        # MatchModel36 -> paired_with41
        graph.add_edges([(labels['36'], labels['41'])])
        # match_contains37 -> Station_S1
        graph.add_edges([(labels['37'], labels['1'])])
        # match_contains38 -> Male_S2
        graph.add_edges([(labels['38'], labels['2'])])
        # apply_contains39 -> Station_T3
        graph.add_edges([(labels['39'], labels['3'])])
        # apply_contains40 -> Male_T4
        graph.add_edges([(labels['40'], labels['4'])])
        
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
    
