

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_rewriter_2(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_rewriter_2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_rewriter_2, self).__init__(name='HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_rewriter_2', num_nodes=72, edges=[])
        
        # Add the edges
        self.add_edges([[3, 0], [0, 10], [2, 18], [18, 7], [7, 19], [19, 11], [7, 20], [20, 9], [9, 21], [21, 5], [38, 32], [32, 50], [39, 33], [33, 8], [40, 34], [34, 52], [41, 35], [35, 53], [42, 36], [36, 54], [43, 37], [37, 55], [7, 22], [22, 58], [11, 23], [23, 59], [5, 24], [24, 60], [2, 25], [25, 61], [9, 26], [26, 62], [4, 1], [1, 27], [1, 28], [1, 29], [1, 30], [1, 31], [8, 12], [12, 51], [8, 13], [13, 57], [27, 2], [2, 63], [6, 14], [14, 3], [6, 15], [15, 10], [3, 16], [16, 56], [10, 17], [17, 57], [63, 3], [6, 4], [31, 5], [38, 44], [39, 45], [40, 46], [41, 47], [42, 48], [43, 49], [28, 7], [29, 11], [30, 9], [44, 56], [45, 58], [46, 59], [47, 60], [48, 61], [49, 62], [7, 64], [64, 3], [11, 65], [65, 3], [9, 66], [66, 3], [5, 67], [67, 3], [7, 68], [68, 10], [11, 69], [69, 10], [9, 70], [70, 10], [5, 71], [71, 10]])
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
        self["name"] = """ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = UUID('1183d5ee-c357-4119-8219-2e753a67efac')
        
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
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["mm__"] = """MT_post__directLink_S"""
        self.vs[0]["GUID__"] = UUID('178dd6db-65cb-41a2-8ddb-d76300cc3c9a')
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["mm__"] = """MT_post__ApplyModel"""
        self.vs[1]["GUID__"] = UUID('2d3701f7-1de2-4a9b-9e9f-1fa12ee39a15')
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
        self.vs[2]["mm__"] = """MT_post__LocalDef"""
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
        self.vs[2]["GUID__"] = UUID('201aa44d-31b2-4134-861b-14fe9bb34e26')
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
        self.vs[3]["MT_label__"] = """3"""
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
        self.vs[3]["mm__"] = """MT_post__State"""
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
        self.vs[3]["GUID__"] = UUID('efd74ade-6037-4638-bd4a-de435dbe54c4')
        self.vs[4]["MT_label__"] = """4"""
        self.vs[4]["mm__"] = """MT_post__paired_with"""
        self.vs[4]["GUID__"] = UUID('7a63fc9a-9309-481e-a1ab-628212797861')
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
        self.vs[5]["mm__"] = """MT_post__Trigger_T"""
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
        self.vs[5]["GUID__"] = UUID('3d7eba1d-adaa-4968-bc48-eabad05ec6c9')
        self.vs[6]["MT_label__"] = """6"""
        self.vs[6]["mm__"] = """MT_post__MatchModel"""
        self.vs[6]["GUID__"] = UUID('1835505e-54fe-41bb-afc7-96c16500fd25')
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
        self.vs[7]["MT_label__"] = """7"""
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
        self.vs[7]["mm__"] = """MT_post__ProcDef"""
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
        self.vs[7]["GUID__"] = UUID('5e9bf28f-d761-44e7-a656-62dfc73f486f')
        self.vs[8]["MT_post__Type"] = """
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
        self.vs[8]["MT_label__"] = """8"""
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
        self.vs[8]["mm__"] = """MT_post__Concat"""
        self.vs[8]["GUID__"] = UUID('e60ca335-e483-4437-8412-18a412905253')
        self.vs[9]["MT_post__cardinality"] = """
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
        self.vs[9]["mm__"] = """MT_post__Par"""
        self.vs[9]["MT_post__classtype"] = """
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
        self.vs[9]["GUID__"] = UUID('5e0c244f-3db3-4c75-a7aa-d564224a59bd')
        self.vs[10]["MT_post__cardinality"] = """
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
        self.vs[10]["mm__"] = """MT_post__ExitPoint"""
        self.vs[10]["MT_post__classtype"] = """
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
        self.vs[10]["GUID__"] = UUID('9990bcd6-06fd-4300-911b-c0e5e2a0f557')
        self.vs[11]["MT_post__cardinality"] = """
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
        self.vs[11]["MT_label__"] = """12"""
        self.vs[11]["MT_post__name"] = """
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
        self.vs[11]["mm__"] = """MT_post__Name"""
        self.vs[11]["MT_post__classtype"] = """
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
        self.vs[11]["GUID__"] = UUID('ac13fe6a-6123-457e-b365-3f356ec2bf0b')
        self.vs[12]["MT_label__"] = """13"""
        self.vs[12]["mm__"] = """MT_post__hasArgs"""
        self.vs[12]["GUID__"] = UUID('6e1e4eb4-8d77-4af2-8e25-9cd0eb5060b5')
        self.vs[13]["MT_label__"] = """14"""
        self.vs[13]["mm__"] = """MT_post__hasArgs"""
        self.vs[13]["GUID__"] = UUID('2239827d-f1a5-4473-849a-b4f56d05b63f')
        self.vs[14]["MT_label__"] = """15"""
        self.vs[14]["mm__"] = """MT_post__match_contains"""
        self.vs[14]["GUID__"] = UUID('b2b131cf-c664-430e-aeba-b3244487c6c6')
        self.vs[15]["MT_label__"] = """16"""
        self.vs[15]["mm__"] = """MT_post__match_contains"""
        self.vs[15]["GUID__"] = UUID('ebfc487e-7ce3-4082-a681-0e3286e1f510')
        self.vs[16]["MT_label__"] = """17"""
        self.vs[16]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[16]["GUID__"] = UUID('5e990411-f302-49df-8fe5-75288db1b610')
        self.vs[17]["MT_label__"] = """18"""
        self.vs[17]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[17]["GUID__"] = UUID('ec4a28de-d190-459d-880c-11beb6c065ef')
        self.vs[18]["MT_post__associationType"] = """
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
        self.vs[18]["MT_label__"] = """19"""
        self.vs[18]["mm__"] = """MT_post__directLink_T"""
        self.vs[18]["GUID__"] = UUID('31be52e4-1e6b-4e6a-a6f4-3ad733964d61')
        self.vs[19]["MT_post__associationType"] = """
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
        self.vs[19]["MT_label__"] = """20"""
        self.vs[19]["mm__"] = """MT_post__directLink_T"""
        self.vs[19]["GUID__"] = UUID('ffd917f1-fe1d-468a-943e-ce9387c3e1c0')
        self.vs[20]["MT_post__associationType"] = """
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
        self.vs[20]["MT_label__"] = """21"""
        self.vs[20]["mm__"] = """MT_post__directLink_T"""
        self.vs[20]["GUID__"] = UUID('03963299-5560-4bba-ba71-081bf57a4827')
        self.vs[21]["MT_post__associationType"] = """
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
        self.vs[21]["MT_label__"] = """22"""
        self.vs[21]["mm__"] = """MT_post__directLink_T"""
        self.vs[21]["GUID__"] = UUID('b2aeb2dc-c426-4960-bbe0-7733c3cfbe35')
        self.vs[22]["MT_label__"] = """23"""
        self.vs[22]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('a337b9bc-a0ba-441b-9840-fe3d533efe8c')
        self.vs[23]["MT_label__"] = """24"""
        self.vs[23]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('b051b6e2-5c03-4e55-a2ea-5586f02e1a82')
        self.vs[24]["MT_label__"] = """25"""
        self.vs[24]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('a450989d-4506-4941-a766-40d6f3ba545a')
        self.vs[25]["MT_label__"] = """26"""
        self.vs[25]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('3db00686-02d1-4a98-9118-b001a4ca675c')
        self.vs[26]["MT_label__"] = """27"""
        self.vs[26]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('f13560bf-9883-4948-90b5-f2b523df45d8')
        self.vs[27]["MT_label__"] = """28"""
        self.vs[27]["mm__"] = """MT_post__apply_contains"""
        self.vs[27]["GUID__"] = UUID('ef05773b-b7b4-4ce5-afca-db96d714bb8f')
        self.vs[28]["MT_label__"] = """29"""
        self.vs[28]["mm__"] = """MT_post__apply_contains"""
        self.vs[28]["GUID__"] = UUID('b57f9f2b-cee5-4fdc-90b2-5b023a640193')
        self.vs[29]["MT_label__"] = """30"""
        self.vs[29]["mm__"] = """MT_post__apply_contains"""
        self.vs[29]["GUID__"] = UUID('99f4fb18-36c3-4db1-9468-37bbb3760ffe')
        self.vs[30]["MT_label__"] = """31"""
        self.vs[30]["mm__"] = """MT_post__apply_contains"""
        self.vs[30]["GUID__"] = UUID('1792e38e-5733-4b39-98df-45fa76cdce52')
        self.vs[31]["MT_label__"] = """32"""
        self.vs[31]["mm__"] = """MT_post__apply_contains"""
        self.vs[31]["GUID__"] = UUID('996425ec-e4bc-4752-8239-8e71ed0bb9b2')
        self.vs[32]["MT_label__"] = """33"""
        self.vs[32]["mm__"] = """MT_post__rightExpr"""
        self.vs[32]["GUID__"] = UUID('4c95e20c-f99d-498c-a3dc-123e9a0aea94')
        self.vs[33]["MT_label__"] = """34"""
        self.vs[33]["mm__"] = """MT_post__rightExpr"""
        self.vs[33]["GUID__"] = UUID('d343cc6b-e2cc-44ee-a255-c900511d2b26')
        self.vs[34]["MT_label__"] = """35"""
        self.vs[34]["mm__"] = """MT_post__rightExpr"""
        self.vs[34]["GUID__"] = UUID('bc182aba-3f3a-475c-ac92-1fc8fdb8a353')
        self.vs[35]["MT_label__"] = """36"""
        self.vs[35]["mm__"] = """MT_post__rightExpr"""
        self.vs[35]["GUID__"] = UUID('7999fbdc-21ad-4d87-9f39-cd330444c3af')
        self.vs[36]["MT_label__"] = """37"""
        self.vs[36]["mm__"] = """MT_post__rightExpr"""
        self.vs[36]["GUID__"] = UUID('a9f0f38f-6c94-41fb-a9bc-e9b8c5f69e4b')
        self.vs[37]["MT_label__"] = """38"""
        self.vs[37]["mm__"] = """MT_post__rightExpr"""
        self.vs[37]["GUID__"] = UUID('0cc20b97-a476-4c03-b160-71df2b56c054')
        self.vs[38]["MT_label__"] = """39"""
        self.vs[38]["MT_post__name"] = """
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
        self.vs[38]["mm__"] = """MT_post__Equation"""
        self.vs[38]["GUID__"] = UUID('7819f088-2be0-4123-a985-35617370f148')
        self.vs[39]["MT_label__"] = """40"""
        self.vs[39]["MT_post__name"] = """
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
        self.vs[39]["mm__"] = """MT_post__Equation"""
        self.vs[39]["GUID__"] = UUID('40ee8765-0f88-4036-8708-232ff8b2c8cd')
        self.vs[40]["MT_label__"] = """41"""
        self.vs[40]["MT_post__name"] = """
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
        self.vs[40]["mm__"] = """MT_post__Equation"""
        self.vs[40]["GUID__"] = UUID('796b5027-ee2a-4543-919b-8dc77cb083dc')
        self.vs[41]["MT_label__"] = """42"""
        self.vs[41]["MT_post__name"] = """
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
        self.vs[41]["mm__"] = """MT_post__Equation"""
        self.vs[41]["GUID__"] = UUID('318989a8-4191-483c-a3ab-d47925923a35')
        self.vs[42]["MT_label__"] = """43"""
        self.vs[42]["MT_post__name"] = """
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
        self.vs[42]["mm__"] = """MT_post__Equation"""
        self.vs[42]["GUID__"] = UUID('a76f034a-7a66-48ab-96cf-e679592051fc')
        self.vs[43]["MT_label__"] = """44"""
        self.vs[43]["MT_post__name"] = """
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
        self.vs[43]["mm__"] = """MT_post__Equation"""
        self.vs[43]["GUID__"] = UUID('b6e459b6-de34-44ec-94d1-78c3b82b9b55')
        self.vs[44]["MT_label__"] = """45"""
        self.vs[44]["mm__"] = """MT_post__leftExpr"""
        self.vs[44]["GUID__"] = UUID('ec133653-a79d-419e-9c58-248e8ae585ee')
        self.vs[45]["MT_label__"] = """46"""
        self.vs[45]["mm__"] = """MT_post__leftExpr"""
        self.vs[45]["GUID__"] = UUID('1c85c190-6222-4b5e-8176-7fda4ad13a48')
        self.vs[46]["MT_label__"] = """47"""
        self.vs[46]["mm__"] = """MT_post__leftExpr"""
        self.vs[46]["GUID__"] = UUID('c6505416-ee64-4b82-8a87-8b269d1197f9')
        self.vs[47]["MT_label__"] = """48"""
        self.vs[47]["mm__"] = """MT_post__leftExpr"""
        self.vs[47]["GUID__"] = UUID('eb3e7aaf-fa26-48cf-9306-002b449fb58c')
        self.vs[48]["MT_label__"] = """49"""
        self.vs[48]["mm__"] = """MT_post__leftExpr"""
        self.vs[48]["GUID__"] = UUID('e80f429c-ff6f-41fb-8171-dbad28d4a1c0')
        self.vs[49]["MT_label__"] = """50"""
        self.vs[49]["mm__"] = """MT_post__leftExpr"""
        self.vs[49]["GUID__"] = UUID('ba9401c5-0e80-4417-90c1-5b4152573f1f')
        self.vs[50]["MT_post__Type"] = """
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
        self.vs[50]["MT_label__"] = """51"""
        self.vs[50]["MT_post__name"] = """return 'true'"""
        self.vs[50]["mm__"] = """MT_post__Constant"""
        self.vs[50]["GUID__"] = UUID('513d8641-37e8-40af-b9f8-5e006b5ec6b4')
        self.vs[51]["MT_post__Type"] = """
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
        self.vs[51]["MT_label__"] = """52"""
        self.vs[51]["MT_post__name"] = """return 'B'"""
        self.vs[51]["mm__"] = """MT_post__Constant"""
        self.vs[51]["GUID__"] = UUID('c357e0cc-de98-4910-9079-5860ffb86bd9')
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
        self.vs[52]["MT_label__"] = """53"""
        self.vs[52]["MT_post__name"] = """return 'sh_in'"""
        self.vs[52]["mm__"] = """MT_post__Constant"""
        self.vs[52]["GUID__"] = UUID('72293817-40bf-408a-b81b-5e7ed1dc822a')
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
        self.vs[53]["MT_label__"] = """54"""
        self.vs[53]["MT_post__name"] = """return 'sh_in'"""
        self.vs[53]["mm__"] = """MT_post__Constant"""
        self.vs[53]["GUID__"] = UUID('02afb59c-a14c-4d40-82c1-341542977da5')
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
        self.vs[54]["MT_label__"] = """55"""
        self.vs[54]["MT_post__name"] = """return 'localdefcompstate'"""
        self.vs[54]["mm__"] = """MT_post__Constant"""
        self.vs[54]["GUID__"] = UUID('e5bc6e7f-62ea-408e-a9d9-a146c6bbb1e9')
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
        self.vs[55]["MT_label__"] = """56"""
        self.vs[55]["MT_post__name"] = """return 'parexitpoint'"""
        self.vs[55]["mm__"] = """MT_post__Constant"""
        self.vs[55]["GUID__"] = UUID('7d2d52cb-6943-44f3-9df2-72ad7ae0606e')
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
        self.vs[56]["MT_label__"] = """57"""
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
        self.vs[56]["GUID__"] = UUID('71815e93-4b43-4684-a380-04e99d660131')
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
        self.vs[57]["MT_label__"] = """58"""
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
        self.vs[57]["GUID__"] = UUID('01572dbf-4922-4286-9f1c-5bf0e1337f61')
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
        self.vs[58]["MT_label__"] = """59"""
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
        self.vs[58]["GUID__"] = UUID('39c6321c-da19-414e-93fe-6816d2d1f87e')
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
        self.vs[59]["MT_label__"] = """60"""
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
        self.vs[59]["GUID__"] = UUID('5bd92f89-3d9d-40b1-9c89-48ea732f9808')
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
        self.vs[60]["MT_label__"] = """61"""
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
        self.vs[60]["GUID__"] = UUID('6baf6d61-c721-48de-9b49-62a2c238c1e0')
        self.vs[61]["MT_post__Type"] = """
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
        self.vs[61]["MT_label__"] = """62"""
        self.vs[61]["MT_post__name"] = """
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
        self.vs[61]["mm__"] = """MT_post__Attribute"""
        self.vs[61]["GUID__"] = UUID('3528042d-05fb-4a35-99ef-d1d0cd689d4f')
        self.vs[62]["MT_post__Type"] = """
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
        self.vs[62]["MT_label__"] = """63"""
        self.vs[62]["MT_post__name"] = """
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
        self.vs[62]["mm__"] = """MT_post__Attribute"""
        self.vs[62]["GUID__"] = UUID('88f528da-6c52-4086-8a8e-d1974eebbec5')
        self.vs[63]["MT_label__"] = """11"""
        self.vs[63]["MT_post__type"] = """
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
        self.vs[63]["mm__"] = """MT_post__trace_link"""
        self.vs[63]["GUID__"] = UUID('f13854ac-a020-4a4d-871c-dc4ff41a39cd')
        self.vs[64]["MT_label__"] = """64"""
        self.vs[64]["mm__"] = """MT_post__trace_link"""
        self.vs[64]["GUID__"] = UUID('387365f5-e7c3-47f3-b808-fb613d36edd1')
        self.vs[65]["MT_label__"] = """65"""
        self.vs[65]["mm__"] = """MT_post__trace_link"""
        self.vs[65]["GUID__"] = UUID('27b623d6-d5f9-4514-9a4e-a595499d2b99')
        self.vs[66]["MT_label__"] = """66"""
        self.vs[66]["mm__"] = """MT_post__trace_link"""
        self.vs[66]["GUID__"] = UUID('e7d39f11-7d10-4903-b950-f431320f6521')
        self.vs[67]["MT_label__"] = """67"""
        self.vs[67]["mm__"] = """MT_post__trace_link"""
        self.vs[67]["GUID__"] = UUID('27378daa-52d2-4c27-99ba-9e64d8f15cd0')
        self.vs[68]["MT_label__"] = """68"""
        self.vs[68]["mm__"] = """MT_post__trace_link"""
        self.vs[68]["GUID__"] = UUID('47c46564-1692-4924-aac3-7dc81c3f314f')
        self.vs[69]["MT_label__"] = """69"""
        self.vs[69]["mm__"] = """MT_post__trace_link"""
        self.vs[69]["GUID__"] = UUID('b7ef7d4b-178a-4125-b65e-a556c1c8a657')
        self.vs[70]["MT_label__"] = """70"""
        self.vs[70]["mm__"] = """MT_post__trace_link"""
        self.vs[70]["GUID__"] = UUID('c411cbc8-b626-4d90-94cf-738669351554')
        self.vs[71]["MT_label__"] = """71"""
        self.vs[71]["mm__"] = """MT_post__trace_link"""
        self.vs[71]["GUID__"] = UUID('580e039f-17e8-43f9-a0b0-a6d5d3fefdd5')

        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_2 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_2
        self.pre = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_2()
    
    def set_name51(self, attr_value, PreNode, graph):
        return 'true'


    def set_name52(self, attr_value, PreNode, graph):
        return 'B'


    def set_name53(self, attr_value, PreNode, graph):
        return 'sh_in'


    def set_name54(self, attr_value, PreNode, graph):
        return 'sh_in'


    def set_name55(self, attr_value, PreNode, graph):
        return 'localdefcompstate'


    def set_name56(self, attr_value, PreNode, graph):
        return 'parexitpoint'


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
        # Constant55
        try:
            graph.vs[labels['55']]['name'] = self.set_name55(graph.vs[labels['55']]['name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        graph.vs[labels['55']][Himesis.Constants.MT_DIRTY] = True
        # Constant51
        try:
            graph.vs[labels['51']]['name'] = self.set_name51(graph.vs[labels['51']]['name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        graph.vs[labels['51']][Himesis.Constants.MT_DIRTY] = True
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # ApplyModel1
        new_node = graph.add_node()
        labels['1'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # paired_with4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # Trigger_T5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Trigger_T'
        # MatchModel6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # ProcDef7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ProcDef'
        # Concat8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Concat'
        # Par9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Par'
        # Name12
        new_node = graph.add_node()
        labels['12'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Name'
        # hasArgs13
        new_node = graph.add_node()
        labels['13'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasArgs'
        # hasArgs14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasArgs'
        # match_contains15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # match_contains16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # hasAttribute_S18
        new_node = graph.add_node()
        labels['18'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_S'
        # directLink_T19
        new_node = graph.add_node()
        labels['19'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T20
        new_node = graph.add_node()
        labels['20'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T21
        new_node = graph.add_node()
        labels['21'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # hasAttribute_T23
        new_node = graph.add_node()
        labels['23'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T24
        new_node = graph.add_node()
        labels['24'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T25
        new_node = graph.add_node()
        labels['25'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T27
        new_node = graph.add_node()
        labels['27'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # apply_contains28
        new_node = graph.add_node()
        labels['28'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains29
        new_node = graph.add_node()
        labels['29'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains30
        new_node = graph.add_node()
        labels['30'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains31
        new_node = graph.add_node()
        labels['31'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains32
        new_node = graph.add_node()
        labels['32'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # rightExpr34
        new_node = graph.add_node()
        labels['34'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr35
        new_node = graph.add_node()
        labels['35'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr36
        new_node = graph.add_node()
        labels['36'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr38
        new_node = graph.add_node()
        labels['38'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation40
        new_node = graph.add_node()
        labels['40'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation41
        new_node = graph.add_node()
        labels['41'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation42
        new_node = graph.add_node()
        labels['42'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation44
        new_node = graph.add_node()
        labels['44'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # leftExpr46
        new_node = graph.add_node()
        labels['46'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr47
        new_node = graph.add_node()
        labels['47'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr48
        new_node = graph.add_node()
        labels['48'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr50
        new_node = graph.add_node()
        labels['50'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Constant52
        new_node = graph.add_node()
        labels['52'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name52(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant53
        new_node = graph.add_node()
        labels['53'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name53(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant54
        new_node = graph.add_node()
        labels['54'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name54(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant56
        new_node = graph.add_node()
        labels['56'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name56(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Attribute58
        new_node = graph.add_node()
        labels['58'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute59
        new_node = graph.add_node()
        labels['59'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute60
        new_node = graph.add_node()
        labels['60'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute61
        new_node = graph.add_node()
        labels['61'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute63
        new_node = graph.add_node()
        labels['63'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # trace_link64
        new_node = graph.add_node()
        labels['64'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link65
        new_node = graph.add_node()
        labels['65'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link66
        new_node = graph.add_node()
        labels['66'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link67
        new_node = graph.add_node()
        labels['67'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link68
        new_node = graph.add_node()
        labels['68'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link69
        new_node = graph.add_node()
        labels['69'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link70
        new_node = graph.add_node()
        labels['70'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link71
        new_node = graph.add_node()
        labels['71'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # paired_with4 -> ApplyModel1
        graph.add_edges([(labels['4'], labels['1'])])
        # ApplyModel1 -> apply_contains28
        graph.add_edges([(labels['1'], labels['28'])])
        # ApplyModel1 -> apply_contains29
        graph.add_edges([(labels['1'], labels['29'])])
        # ApplyModel1 -> apply_contains30
        graph.add_edges([(labels['1'], labels['30'])])
        # ApplyModel1 -> apply_contains31
        graph.add_edges([(labels['1'], labels['31'])])
        # ApplyModel1 -> apply_contains32
        graph.add_edges([(labels['1'], labels['32'])])
        # directLink_T20 -> Name12
        graph.add_edges([(labels['20'], labels['12'])])
        # Name12 -> hasAttribute_T24
        graph.add_edges([(labels['12'], labels['24'])])
        # apply_contains30 -> Name12
        graph.add_edges([(labels['30'], labels['12'])])
        # Name12 -> trace_link65
        graph.add_edges([(labels['12'], labels['65'])])
        # Name12 -> trace_link69
        graph.add_edges([(labels['12'], labels['69'])])
        # Concat8 -> hasArgs13
        graph.add_edges([(labels['8'], labels['13'])])
        # hasArgs13 -> Constant52
        graph.add_edges([(labels['13'], labels['52'])])
        # Concat8 -> hasArgs14
        graph.add_edges([(labels['8'], labels['14'])])
        # hasArgs14 -> Attribute58
        graph.add_edges([(labels['14'], labels['58'])])
        # MatchModel6 -> match_contains15
        graph.add_edges([(labels['6'], labels['15'])])
        # match_contains15 -> State3
        graph.add_edges([(labels['15'], labels['3'])])
        # MatchModel6 -> match_contains16
        graph.add_edges([(labels['6'], labels['16'])])
        # match_contains16 -> ExitPoint10
        graph.add_edges([(labels['16'], labels['10'])])
        # ExitPoint10 -> hasAttribute_S18
        graph.add_edges([(labels['10'], labels['18'])])
        # hasAttribute_S18 -> Attribute58
        graph.add_edges([(labels['18'], labels['58'])])
        # LocalDef2 -> directLink_T19
        graph.add_edges([(labels['2'], labels['19'])])
        # directLink_T19 -> ProcDef7
        graph.add_edges([(labels['19'], labels['7'])])
        # ProcDef7 -> directLink_T20
        graph.add_edges([(labels['7'], labels['20'])])
        # ProcDef7 -> directLink_T21
        graph.add_edges([(labels['7'], labels['21'])])
        # directLink_T21 -> Par9
        graph.add_edges([(labels['21'], labels['9'])])
        # Par9 -> directLink_T22
        graph.add_edges([(labels['9'], labels['22'])])
        # directLink_T22 -> Trigger_T5
        graph.add_edges([(labels['22'], labels['5'])])
        # ProcDef7 -> hasAttribute_T23
        graph.add_edges([(labels['7'], labels['23'])])
        # hasAttribute_T23 -> Attribute59
        graph.add_edges([(labels['23'], labels['59'])])
        # hasAttribute_T24 -> Attribute60
        graph.add_edges([(labels['24'], labels['60'])])
        # Trigger_T5 -> hasAttribute_T25
        graph.add_edges([(labels['5'], labels['25'])])
        # hasAttribute_T25 -> Attribute61
        graph.add_edges([(labels['25'], labels['61'])])
        # Par9 -> hasAttribute_T27
        graph.add_edges([(labels['9'], labels['27'])])
        # hasAttribute_T27 -> Attribute63
        graph.add_edges([(labels['27'], labels['63'])])
        # apply_contains28 -> LocalDef2
        graph.add_edges([(labels['28'], labels['2'])])
        # apply_contains29 -> ProcDef7
        graph.add_edges([(labels['29'], labels['7'])])
        # apply_contains31 -> Par9
        graph.add_edges([(labels['31'], labels['9'])])
        # apply_contains32 -> Trigger_T5
        graph.add_edges([(labels['32'], labels['5'])])
        # Equation40 -> rightExpr34
        graph.add_edges([(labels['40'], labels['34'])])
        # rightExpr34 -> Concat8
        graph.add_edges([(labels['34'], labels['8'])])
        # Equation41 -> rightExpr35
        graph.add_edges([(labels['41'], labels['35'])])
        # rightExpr35 -> Constant53
        graph.add_edges([(labels['35'], labels['53'])])
        # Equation42 -> rightExpr36
        graph.add_edges([(labels['42'], labels['36'])])
        # rightExpr36 -> Constant54
        graph.add_edges([(labels['36'], labels['54'])])
        # Equation44 -> rightExpr38
        graph.add_edges([(labels['44'], labels['38'])])
        # rightExpr38 -> Constant56
        graph.add_edges([(labels['38'], labels['56'])])
        # MatchModel6 -> paired_with4
        graph.add_edges([(labels['6'], labels['4'])])
        # Equation40 -> leftExpr46
        graph.add_edges([(labels['40'], labels['46'])])
        # Equation41 -> leftExpr47
        graph.add_edges([(labels['41'], labels['47'])])
        # Equation42 -> leftExpr48
        graph.add_edges([(labels['42'], labels['48'])])
        # Equation44 -> leftExpr50
        graph.add_edges([(labels['44'], labels['50'])])
        # leftExpr46 -> Attribute59
        graph.add_edges([(labels['46'], labels['59'])])
        # leftExpr47 -> Attribute60
        graph.add_edges([(labels['47'], labels['60'])])
        # leftExpr48 -> Attribute61
        graph.add_edges([(labels['48'], labels['61'])])
        # Trigger_T5 -> trace_link67
        graph.add_edges([(labels['5'], labels['67'])])
        # Trigger_T5 -> trace_link71
        graph.add_edges([(labels['5'], labels['71'])])
        # leftExpr50 -> Attribute63
        graph.add_edges([(labels['50'], labels['63'])])
        # ProcDef7 -> trace_link64
        graph.add_edges([(labels['7'], labels['64'])])
        # trace_link64 -> State3
        graph.add_edges([(labels['64'], labels['3'])])
        # trace_link65 -> State3
        graph.add_edges([(labels['65'], labels['3'])])
        # Par9 -> trace_link66
        graph.add_edges([(labels['9'], labels['66'])])
        # trace_link66 -> State3
        graph.add_edges([(labels['66'], labels['3'])])
        # trace_link67 -> State3
        graph.add_edges([(labels['67'], labels['3'])])
        # ProcDef7 -> trace_link68
        graph.add_edges([(labels['7'], labels['68'])])
        # trace_link68 -> ExitPoint10
        graph.add_edges([(labels['68'], labels['10'])])
        # trace_link69 -> ExitPoint10
        graph.add_edges([(labels['69'], labels['10'])])
        # Par9 -> trace_link70
        graph.add_edges([(labels['9'], labels['70'])])
        # trace_link70 -> ExitPoint10
        graph.add_edges([(labels['70'], labels['10'])])
        # trace_link71 -> ExitPoint10
        graph.add_edges([(labels['71'], labels['10'])])
        
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
    
