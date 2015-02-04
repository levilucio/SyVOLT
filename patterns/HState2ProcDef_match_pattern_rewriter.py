

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HState2ProcDef_match_pattern_rewriter(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HState2ProcDef_match_pattern_rewriter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2ProcDef_match_pattern_rewriter, self).__init__(name='HState2ProcDef_match_pattern_rewriter', num_nodes=61, edges=[])
        
        # Add the edges
        self.add_edges([[5, 9], [9, 15], [5, 10], [10, 16], [5, 11], [11, 17], [31, 26], [26, 6], [32, 27], [27, 42], [33, 28], [28, 43], [34, 29], [29, 44], [35, 30], [30, 45], [5, 46], [46, 53], [15, 47], [47, 54], [16, 48], [48, 55], [17, 49], [49, 56], [5, 50], [50, 57], [5, 51], [51, 60], [3, 0], [0, 18], [0, 19], [0, 20], [0, 21], [6, 7], [7, 41], [6, 8], [8, 52], [4, 1], [1, 2], [2, 12], [12, 52], [2, 13], [13, 58], [2, 14], [14, 59], [4, 3], [31, 36], [32, 37], [33, 38], [34, 39], [35, 40], [18, 5], [19, 15], [20, 16], [21, 17], [36, 53], [37, 54], [38, 55], [39, 56], [40, 57], [5, 22], [22, 2], [15, 23], [23, 2], [16, 24], [24, 2], [17, 25], [25, 2]])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__UMLRT2Kiltera_MM'
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
        self["name"] = """State2ProcDef"""
        self["GUID__"] = UUID('83605342-dc03-4fac-bfbc-aec39dca2d8f')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["mm__"] = """MT_post__ApplyModel"""
        self.vs[0]["GUID__"] = UUID('f9d1828a-34a2-43ea-ac75-d112607a65a0')
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["mm__"] = """MT_post__match_contains"""
        self.vs[1]["GUID__"] = UUID('6d634f84-b41c-41c7-8aa5-a9f9b5f3553d')
        self.vs[2]["MT_post__cardinality"] = """
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
        self.vs[2]["mm__"] = """MT_post__State"""
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
        self.vs[2]["GUID__"] = UUID('4f9bbe8c-96e8-4e8d-837f-1d0172523241')
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["mm__"] = """MT_post__paired_with"""
        self.vs[3]["GUID__"] = UUID('3b733697-1fc1-4923-b938-e350917965ed')
        self.vs[4]["MT_label__"] = """4"""
        self.vs[4]["mm__"] = """MT_post__MatchModel"""
        self.vs[4]["GUID__"] = UUID('3e43978f-be7f-4fd4-82aa-f8d3afdcc25a')
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
        self.vs[5]["MT_label__"] = """5"""
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
        self.vs[5]["mm__"] = """MT_post__ProcDef"""
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
        self.vs[5]["GUID__"] = UUID('7c685ec3-ba62-4b35-9527-c14fdf4ed322')
        self.vs[6]["MT_post__Type"] = """
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
        self.vs[6]["MT_label__"] = """6"""
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
        self.vs[6]["mm__"] = """MT_post__Concat"""
        self.vs[6]["GUID__"] = UUID('754c469f-806a-4653-accb-edaa2b906093')
        self.vs[7]["MT_label__"] = """7"""
        self.vs[7]["mm__"] = """MT_post__hasArgs"""
        self.vs[7]["GUID__"] = UUID('74c647dc-a10d-4c7d-8bfd-e911b1388343')
        self.vs[8]["MT_label__"] = """8"""
        self.vs[8]["mm__"] = """MT_post__hasArgs"""
        self.vs[8]["GUID__"] = UUID('ef7fea39-679a-4402-a951-7799eba0dd24')
        self.vs[9]["MT_post__associationType"] = """
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
        self.vs[9]["MT_label__"] = """9"""
        self.vs[9]["mm__"] = """MT_post__directLink_T"""
        self.vs[9]["GUID__"] = UUID('9d7e0ea7-211b-442c-a5ff-0a0ce009eb54')
        self.vs[10]["MT_post__associationType"] = """
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
        self.vs[10]["MT_label__"] = """10"""
        self.vs[10]["mm__"] = """MT_post__directLink_T"""
        self.vs[10]["GUID__"] = UUID('7801474f-8a35-4f94-8af2-992bc20a8def')
        self.vs[11]["MT_post__associationType"] = """
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
        self.vs[11]["MT_label__"] = """11"""
        self.vs[11]["mm__"] = """MT_post__directLink_T"""
        self.vs[11]["GUID__"] = UUID('bffc30fc-9352-48cb-af3f-8c1c668e663f')
        self.vs[12]["MT_label__"] = """12"""
        self.vs[12]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('db7b607e-8a3f-489b-af49-2ad44b54e100')
        self.vs[13]["MT_label__"] = """13"""
        self.vs[13]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('b139a2d8-0be9-4ac8-9d7d-064635ecd75e')
        self.vs[14]["MT_label__"] = """14"""
        self.vs[14]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[14]["GUID__"] = UUID('e35cfec4-4332-4bf9-88ad-7d725cb19c2a')
        self.vs[15]["MT_post__cardinality"] = """
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
        self.vs[15]["MT_label__"] = """15"""
        self.vs[15]["MT_post__name"] = """
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
        self.vs[15]["mm__"] = """MT_post__Name"""
        self.vs[15]["MT_post__classtype"] = """
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
        self.vs[15]["GUID__"] = UUID('5b3a0f69-bec1-4032-840a-1c0c055302a1')
        self.vs[16]["MT_post__cardinality"] = """
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
        self.vs[16]["MT_label__"] = """16"""
        self.vs[16]["MT_post__name"] = """
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
        self.vs[16]["mm__"] = """MT_post__Name"""
        self.vs[16]["MT_post__classtype"] = """
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
        self.vs[16]["GUID__"] = UUID('6c76f462-e7f5-4301-9185-5ce93572b10f')
        self.vs[17]["MT_post__cardinality"] = """
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
        self.vs[17]["MT_label__"] = """17"""
        self.vs[17]["MT_post__name"] = """
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
        self.vs[17]["mm__"] = """MT_post__Name"""
        self.vs[17]["MT_post__classtype"] = """
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
        self.vs[17]["GUID__"] = UUID('72111b40-ee81-450a-9e54-d201a6b7b665')
        self.vs[18]["MT_label__"] = """18"""
        self.vs[18]["mm__"] = """MT_post__apply_contains"""
        self.vs[18]["GUID__"] = UUID('f0a95df7-4899-4503-ae2b-6d5083465763')
        self.vs[19]["MT_label__"] = """19"""
        self.vs[19]["mm__"] = """MT_post__apply_contains"""
        self.vs[19]["GUID__"] = UUID('0616f1db-94ab-4149-9936-64c10d6970df')
        self.vs[20]["MT_label__"] = """20"""
        self.vs[20]["mm__"] = """MT_post__apply_contains"""
        self.vs[20]["GUID__"] = UUID('849d6d41-acd4-4674-a6d8-1b0c8c065b2b')
        self.vs[21]["MT_label__"] = """21"""
        self.vs[21]["mm__"] = """MT_post__apply_contains"""
        self.vs[21]["GUID__"] = UUID('50bc3753-54d6-4be6-a8d0-96eb2fe92609')
        self.vs[22]["MT_label__"] = """57"""
        self.vs[22]["mm__"] = """MT_post__trace_link"""
        self.vs[22]["GUID__"] = UUID('6065e067-90aa-4d77-bfba-43e5f9492266')
        self.vs[23]["MT_label__"] = """58"""
        self.vs[23]["mm__"] = """MT_post__trace_link"""
        self.vs[23]["GUID__"] = UUID('eb925a29-1501-4e1d-9702-6b62f0b120bc')
        self.vs[24]["MT_label__"] = """59"""
        self.vs[24]["mm__"] = """MT_post__trace_link"""
        self.vs[24]["GUID__"] = UUID('eed6a339-94be-42fb-a466-60364cdb6546')
        self.vs[25]["MT_label__"] = """60"""
        self.vs[25]["mm__"] = """MT_post__trace_link"""
        self.vs[25]["GUID__"] = UUID('4dfa1157-51aa-4476-a634-2c465c1b89f5')
        self.vs[26]["MT_label__"] = """22"""
        self.vs[26]["mm__"] = """MT_post__rightExpr"""
        self.vs[26]["GUID__"] = UUID('30261a24-3669-4924-91ae-c956c873d87d')
        self.vs[27]["MT_label__"] = """23"""
        self.vs[27]["mm__"] = """MT_post__rightExpr"""
        self.vs[27]["GUID__"] = UUID('ef06bcb4-d6fe-404a-b137-1b43edd13e7c')
        self.vs[28]["MT_label__"] = """24"""
        self.vs[28]["mm__"] = """MT_post__rightExpr"""
        self.vs[28]["GUID__"] = UUID('96e7677c-5cec-41f4-802b-87a614790359')
        self.vs[29]["MT_label__"] = """25"""
        self.vs[29]["mm__"] = """MT_post__rightExpr"""
        self.vs[29]["GUID__"] = UUID('1500465b-1b49-4afa-b6d2-e49ff0be1ef0')
        self.vs[30]["MT_label__"] = """26"""
        self.vs[30]["mm__"] = """MT_post__rightExpr"""
        self.vs[30]["GUID__"] = UUID('37315f89-189f-4e4b-809c-910cf67ca99c')
        self.vs[31]["MT_label__"] = """27"""
        self.vs[31]["MT_post__name"] = """
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
        self.vs[31]["mm__"] = """MT_post__Equation"""
        self.vs[31]["GUID__"] = UUID('9bc4e826-a85a-402c-89ba-da9a1d9995cb')
        self.vs[32]["MT_label__"] = """28"""
        self.vs[32]["MT_post__name"] = """
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
        self.vs[32]["mm__"] = """MT_post__Equation"""
        self.vs[32]["GUID__"] = UUID('6f2fa1d8-cafe-4275-9716-2c3a6e50a853')
        self.vs[33]["MT_label__"] = """29"""
        self.vs[33]["MT_post__name"] = """
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
        self.vs[33]["mm__"] = """MT_post__Equation"""
        self.vs[33]["GUID__"] = UUID('1cc543c6-57cd-4294-893e-167677fbd63b')
        self.vs[34]["MT_label__"] = """30"""
        self.vs[34]["MT_post__name"] = """
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
        self.vs[34]["mm__"] = """MT_post__Equation"""
        self.vs[34]["GUID__"] = UUID('1bb14a63-4932-4c68-8a3f-44ae863637e5')
        self.vs[35]["MT_label__"] = """31"""
        self.vs[35]["MT_post__name"] = """
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
        self.vs[35]["mm__"] = """MT_post__Equation"""
        self.vs[35]["GUID__"] = UUID('1f69b2c4-12cf-460f-8324-cf74494c40b5')
        self.vs[36]["MT_label__"] = """32"""
        self.vs[36]["mm__"] = """MT_post__leftExpr"""
        self.vs[36]["GUID__"] = UUID('8475ab8d-5af5-44a4-810d-6c2f52716e7e')
        self.vs[37]["MT_label__"] = """33"""
        self.vs[37]["mm__"] = """MT_post__leftExpr"""
        self.vs[37]["GUID__"] = UUID('d7852046-9569-4866-ab49-e7ee26d5f68b')
        self.vs[38]["MT_label__"] = """34"""
        self.vs[38]["mm__"] = """MT_post__leftExpr"""
        self.vs[38]["GUID__"] = UUID('f25df314-a5fb-4a59-883f-b81d4ae86431')
        self.vs[39]["MT_label__"] = """35"""
        self.vs[39]["mm__"] = """MT_post__leftExpr"""
        self.vs[39]["GUID__"] = UUID('8523d787-09e2-4d49-8c12-9de7c1f70ceb')
        self.vs[40]["MT_label__"] = """36"""
        self.vs[40]["mm__"] = """MT_post__leftExpr"""
        self.vs[40]["GUID__"] = UUID('e916d1a0-181c-4bfa-98e9-d5a7b506b836')
        self.vs[41]["MT_post__Type"] = """
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
        self.vs[41]["MT_label__"] = """37"""
        self.vs[41]["MT_post__name"] = """return 'S'"""
        self.vs[41]["mm__"] = """MT_post__Constant"""
        self.vs[41]["GUID__"] = UUID('a398a7af-9670-4d3a-836a-a5bfed26b583')
        self.vs[42]["MT_post__Type"] = """
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
        self.vs[42]["MT_label__"] = """38"""
        self.vs[42]["MT_post__name"] = """return 'enp'"""
        self.vs[42]["mm__"] = """MT_post__Constant"""
        self.vs[42]["GUID__"] = UUID('c8163fe1-f99f-42d6-9ba4-ce8b8c91d65f')
        self.vs[43]["MT_post__Type"] = """
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
        self.vs[43]["MT_label__"] = """39"""
        self.vs[43]["MT_post__name"] = """return 'exit'"""
        self.vs[43]["mm__"] = """MT_post__Constant"""
        self.vs[43]["GUID__"] = UUID('96eef8ec-9a0c-464f-ba2d-592a38108659')
        self.vs[44]["MT_post__Type"] = """
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
        self.vs[44]["MT_label__"] = """40"""
        self.vs[44]["MT_post__name"] = """return 'exack'"""
        self.vs[44]["mm__"] = """MT_post__Constant"""
        self.vs[44]["GUID__"] = UUID('514e1a89-e3b5-4582-be2c-c517aedc4fe9')
        self.vs[45]["MT_post__Type"] = """
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
        self.vs[45]["MT_label__"] = """41"""
        self.vs[45]["MT_post__name"] = """return 'procdef'"""
        self.vs[45]["mm__"] = """MT_post__Constant"""
        self.vs[45]["GUID__"] = UUID('9a4dcb7a-3e42-4780-a023-6ff89fa3535a')
        self.vs[46]["MT_label__"] = """42"""
        self.vs[46]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[46]["GUID__"] = UUID('712c222c-6f73-4c3f-a099-66aa89023ab6')
        self.vs[47]["MT_label__"] = """43"""
        self.vs[47]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[47]["GUID__"] = UUID('b01047dd-8e3a-4cfd-86a5-e33abc8b4114')
        self.vs[48]["MT_label__"] = """44"""
        self.vs[48]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[48]["GUID__"] = UUID('cb04dfa9-1623-4ab5-883c-96774de13afd')
        self.vs[49]["MT_label__"] = """45"""
        self.vs[49]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[49]["GUID__"] = UUID('efb7392c-9bcd-4f20-aec1-6741edd7e4c9')
        self.vs[50]["MT_label__"] = """46"""
        self.vs[50]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[50]["GUID__"] = UUID('2b665356-c63d-4d69-a191-c3e610f1920b')
        self.vs[51]["MT_label__"] = """47"""
        self.vs[51]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[51]["GUID__"] = UUID('95a56e56-009a-475b-be47-87eae04d2b39')
        self.vs[52]["MT_post__Type"] = """
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
        self.vs[52]["MT_label__"] = """48"""
        self.vs[52]["MT_post__name"] = """
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
        self.vs[52]["mm__"] = """MT_post__Attribute"""
        self.vs[52]["GUID__"] = UUID('f6e1437c-aec6-478e-a219-61a956eec835')
        self.vs[53]["MT_post__Type"] = """
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
        self.vs[53]["MT_label__"] = """49"""
        self.vs[53]["MT_post__name"] = """
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
        self.vs[53]["mm__"] = """MT_post__Attribute"""
        self.vs[53]["GUID__"] = UUID('89ace4f0-41df-4819-a7f9-8f128e9ba4db')
        self.vs[54]["MT_post__Type"] = """
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
        self.vs[54]["MT_label__"] = """50"""
        self.vs[54]["MT_post__name"] = """
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
        self.vs[54]["mm__"] = """MT_post__Attribute"""
        self.vs[54]["GUID__"] = UUID('2fe95c72-0617-42fc-af4d-1a38ae658581')
        self.vs[55]["MT_post__Type"] = """
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
        self.vs[55]["MT_label__"] = """51"""
        self.vs[55]["MT_post__name"] = """
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
        self.vs[55]["mm__"] = """MT_post__Attribute"""
        self.vs[55]["GUID__"] = UUID('f3ac6cf6-74fd-4806-a53a-a9cb10e24b1d')
        self.vs[56]["MT_post__Type"] = """
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
        self.vs[56]["MT_label__"] = """52"""
        self.vs[56]["MT_post__name"] = """
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
        self.vs[56]["mm__"] = """MT_post__Attribute"""
        self.vs[56]["GUID__"] = UUID('a23f8321-e355-4653-a576-af0475aeef92')
        self.vs[57]["MT_post__Type"] = """
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
        self.vs[57]["MT_label__"] = """53"""
        self.vs[57]["MT_post__name"] = """
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
        self.vs[57]["mm__"] = """MT_post__Attribute"""
        self.vs[57]["GUID__"] = UUID('b98787e0-0f93-414b-9144-76204673b58b')
        self.vs[58]["MT_post__Type"] = """
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
        self.vs[58]["MT_label__"] = """54"""
        self.vs[58]["MT_post__name"] = """
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
        self.vs[58]["mm__"] = """MT_post__Attribute"""
        self.vs[58]["GUID__"] = UUID('4ca59740-02e0-4e73-ab5e-1fd264e4468b')
        self.vs[59]["MT_post__Type"] = """
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
        self.vs[59]["MT_label__"] = """55"""
        self.vs[59]["MT_post__name"] = """
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
        self.vs[59]["mm__"] = """MT_post__Attribute"""
        self.vs[59]["GUID__"] = UUID('9467a311-7649-4d52-9338-90be1a524b70')
        self.vs[60]["MT_post__Type"] = """
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
        self.vs[60]["MT_label__"] = """56"""
        self.vs[60]["MT_post__name"] = """
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
        self.vs[60]["mm__"] = """MT_post__Attribute"""
        self.vs[60]["GUID__"] = UUID('2f63cbe2-28e7-4f56-9e71-597ea80cc78d')

        from HState2ProcDef_match_pattern_matcher import HState2ProcDef_match_pattern_matcher
        self.pre = HState2ProcDef_match_pattern_matcher()
    
    def set_name37(self, attr_value, PreNode, graph):
        return 'S'


    def set_name38(self, attr_value, PreNode, graph):
        return 'enp'


    def set_name39(self, attr_value, PreNode, graph):
        return 'exit'


    def set_name40(self, attr_value, PreNode, graph):
        return 'exack'


    def set_name41(self, attr_value, PreNode, graph):
        return 'procdef'


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
        # ApplyModel0
        new_node = graph.add_node()
        labels['0'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # match_contains1
        new_node = graph.add_node()
        labels['1'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # paired_with3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # MatchModel4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # ProcDef5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ProcDef'
        # Concat6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Concat'
        # hasArgs7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasArgs'
        # hasArgs8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasArgs'
        # directLink_T9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # Name15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Name'
        # Name16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Name'
        # Name17
        new_node = graph.add_node()
        labels['17'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Name'
        # apply_contains18
        new_node = graph.add_node()
        labels['18'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains19
        new_node = graph.add_node()
        labels['19'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains20
        new_node = graph.add_node()
        labels['20'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains21
        new_node = graph.add_node()
        labels['21'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # rightExpr22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr23
        new_node = graph.add_node()
        labels['23'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr24
        new_node = graph.add_node()
        labels['24'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr25
        new_node = graph.add_node()
        labels['25'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr26
        new_node = graph.add_node()
        labels['26'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation27
        new_node = graph.add_node()
        labels['27'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation28
        new_node = graph.add_node()
        labels['28'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation29
        new_node = graph.add_node()
        labels['29'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation30
        new_node = graph.add_node()
        labels['30'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation31
        new_node = graph.add_node()
        labels['31'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # leftExpr32
        new_node = graph.add_node()
        labels['32'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr33
        new_node = graph.add_node()
        labels['33'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr34
        new_node = graph.add_node()
        labels['34'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr35
        new_node = graph.add_node()
        labels['35'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr36
        new_node = graph.add_node()
        labels['36'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Constant37
        new_node = graph.add_node()
        labels['37'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name37(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant38
        new_node = graph.add_node()
        labels['38'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name38(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant39
        new_node = graph.add_node()
        labels['39'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name39(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant40
        new_node = graph.add_node()
        labels['40'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name40(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant41
        new_node = graph.add_node()
        labels['41'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name41(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # hasAttribute_T42
        new_node = graph.add_node()
        labels['42'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T43
        new_node = graph.add_node()
        labels['43'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T44
        new_node = graph.add_node()
        labels['44'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T45
        new_node = graph.add_node()
        labels['45'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T46
        new_node = graph.add_node()
        labels['46'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T47
        new_node = graph.add_node()
        labels['47'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # Attribute49
        new_node = graph.add_node()
        labels['49'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute50
        new_node = graph.add_node()
        labels['50'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute51
        new_node = graph.add_node()
        labels['51'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute52
        new_node = graph.add_node()
        labels['52'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute53
        new_node = graph.add_node()
        labels['53'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute56
        new_node = graph.add_node()
        labels['56'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # trace_link57
        new_node = graph.add_node()
        labels['57'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link58
        new_node = graph.add_node()
        labels['58'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link59
        new_node = graph.add_node()
        labels['59'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link60
        new_node = graph.add_node()
        labels['60'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # paired_with3 -> ApplyModel0
        graph.add_edges([(labels['3'], labels['0'])])
        # ApplyModel0 -> apply_contains18
        graph.add_edges([(labels['0'], labels['18'])])
        # ApplyModel0 -> apply_contains19
        graph.add_edges([(labels['0'], labels['19'])])
        # ApplyModel0 -> apply_contains20
        graph.add_edges([(labels['0'], labels['20'])])
        # ApplyModel0 -> apply_contains21
        graph.add_edges([(labels['0'], labels['21'])])
        # MatchModel4 -> match_contains1
        graph.add_edges([(labels['4'], labels['1'])])
        # match_contains1 -> State2
        graph.add_edges([(labels['1'], labels['2'])])
        # ProcDef5 -> directLink_T10
        graph.add_edges([(labels['5'], labels['10'])])
        # directLink_T10 -> Name16
        graph.add_edges([(labels['10'], labels['16'])])
        # ProcDef5 -> directLink_T11
        graph.add_edges([(labels['5'], labels['11'])])
        # directLink_T11 -> Name17
        graph.add_edges([(labels['11'], labels['17'])])
        # directLink_T9 -> Name15
        graph.add_edges([(labels['9'], labels['15'])])
        # Name15 -> hasAttribute_T43
        graph.add_edges([(labels['15'], labels['43'])])
        # apply_contains19 -> Name15
        graph.add_edges([(labels['19'], labels['15'])])
        # Name15 -> trace_link58
        graph.add_edges([(labels['15'], labels['58'])])
        # Name16 -> hasAttribute_T44
        graph.add_edges([(labels['16'], labels['44'])])
        # apply_contains20 -> Name16
        graph.add_edges([(labels['20'], labels['16'])])
        # Name16 -> trace_link59
        graph.add_edges([(labels['16'], labels['59'])])
        # Name17 -> hasAttribute_T45
        graph.add_edges([(labels['17'], labels['45'])])
        # apply_contains21 -> Name17
        graph.add_edges([(labels['21'], labels['17'])])
        # Name17 -> trace_link60
        graph.add_edges([(labels['17'], labels['60'])])
        # apply_contains18 -> ProcDef5
        graph.add_edges([(labels['18'], labels['5'])])
        # Equation27 -> rightExpr22
        graph.add_edges([(labels['27'], labels['22'])])
        # rightExpr22 -> Concat6
        graph.add_edges([(labels['22'], labels['6'])])
        # Equation28 -> rightExpr23
        graph.add_edges([(labels['28'], labels['23'])])
        # rightExpr23 -> Constant38
        graph.add_edges([(labels['23'], labels['38'])])
        # Equation29 -> rightExpr24
        graph.add_edges([(labels['29'], labels['24'])])
        # rightExpr24 -> Constant39
        graph.add_edges([(labels['24'], labels['39'])])
        # Equation30 -> rightExpr25
        graph.add_edges([(labels['30'], labels['25'])])
        # rightExpr25 -> Constant40
        graph.add_edges([(labels['25'], labels['40'])])
        # Equation31 -> rightExpr26
        graph.add_edges([(labels['31'], labels['26'])])
        # rightExpr26 -> Constant41
        graph.add_edges([(labels['26'], labels['41'])])
        # Equation27 -> leftExpr32
        graph.add_edges([(labels['27'], labels['32'])])
        # Equation28 -> leftExpr33
        graph.add_edges([(labels['28'], labels['33'])])
        # Equation29 -> leftExpr34
        graph.add_edges([(labels['29'], labels['34'])])
        # MatchModel4 -> paired_with3
        graph.add_edges([(labels['4'], labels['3'])])
        # Equation30 -> leftExpr35
        graph.add_edges([(labels['30'], labels['35'])])
        # Equation31 -> leftExpr36
        graph.add_edges([(labels['31'], labels['36'])])
        # leftExpr32 -> Attribute49
        graph.add_edges([(labels['32'], labels['49'])])
        # leftExpr33 -> Attribute50
        graph.add_edges([(labels['33'], labels['50'])])
        # leftExpr34 -> Attribute51
        graph.add_edges([(labels['34'], labels['51'])])
        # leftExpr35 -> Attribute52
        graph.add_edges([(labels['35'], labels['52'])])
        # leftExpr36 -> Attribute53
        graph.add_edges([(labels['36'], labels['53'])])
        # hasArgs7 -> Constant37
        graph.add_edges([(labels['7'], labels['37'])])
        # ProcDef5 -> hasAttribute_T42
        graph.add_edges([(labels['5'], labels['42'])])
        # hasAttribute_T42 -> Attribute49
        graph.add_edges([(labels['42'], labels['49'])])
        # hasAttribute_T43 -> Attribute50
        graph.add_edges([(labels['43'], labels['50'])])
        # hasAttribute_T44 -> Attribute51
        graph.add_edges([(labels['44'], labels['51'])])
        # hasAttribute_T45 -> Attribute52
        graph.add_edges([(labels['45'], labels['52'])])
        # ProcDef5 -> hasAttribute_T46
        graph.add_edges([(labels['5'], labels['46'])])
        # hasAttribute_T46 -> Attribute53
        graph.add_edges([(labels['46'], labels['53'])])
        # ProcDef5 -> hasAttribute_T47
        graph.add_edges([(labels['5'], labels['47'])])
        # hasAttribute_T47 -> Attribute56
        graph.add_edges([(labels['47'], labels['56'])])
        # ProcDef5 -> directLink_T9
        graph.add_edges([(labels['5'], labels['9'])])
        # ProcDef5 -> trace_link57
        graph.add_edges([(labels['5'], labels['57'])])
        # trace_link57 -> State2
        graph.add_edges([(labels['57'], labels['2'])])
        # trace_link58 -> State2
        graph.add_edges([(labels['58'], labels['2'])])
        # trace_link59 -> State2
        graph.add_edges([(labels['59'], labels['2'])])
        # Concat6 -> hasArgs7
        graph.add_edges([(labels['6'], labels['7'])])
        # Concat6 -> hasArgs8
        graph.add_edges([(labels['6'], labels['8'])])
        # trace_link60 -> State2
        graph.add_edges([(labels['60'], labels['2'])])
        # hasArgs8 -> Attribute48
        graph.add_edges([(labels['8'], labels['48'])])
        
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
    
