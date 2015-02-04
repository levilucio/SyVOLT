

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HBasicState2ProcDef_rule_combinator_rewriter_1(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicState2ProcDef_rule_combinator_rewriter_1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef_rule_combinator_rewriter_1, self).__init__(name='HBasicState2ProcDef_rule_combinator_rewriter_1', num_nodes=56, edges=[])
        
        # Add the edges
        self.add_edges([[8, 11], [11, 4], [4, 12], [12, 7], [7, 13], [13, 5], [32, 26], [26, 50], [33, 27], [27, 51], [34, 28], [28, 52], [35, 29], [29, 53], [36, 30], [30, 54], [37, 31], [31, 55], [7, 15], [15, 40], [5, 16], [16, 41], [8, 17], [17, 42], [4, 18], [18, 43], [3, 0], [0, 19], [0, 20], [0, 21], [0, 22], [6, 1], [1, 2], [2, 9], [9, 38], [2, 10], [10, 39], [14, 2], [6, 3], [20, 4], [22, 5], [32, 44], [33, 45], [34, 46], [35, 47], [36, 48], [37, 49], [19, 8], [21, 7], [8, 14], [44, 38], [45, 39], [46, 40], [47, 41], [48, 42], [49, 43], [4, 23], [23, 2], [7, 24], [24, 2], [5, 25], [25, 2]])
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
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = UUID('bc8da8f4-6500-4462-ab6c-29a0e49f1222')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["mm__"] = """MT_post__ApplyModel"""
        self.vs[0]["GUID__"] = UUID('d66e30a9-d745-4680-b687-ee0ffc4916bb')
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["mm__"] = """MT_post__match_contains"""
        self.vs[1]["GUID__"] = UUID('5b44394f-ed77-4f93-b163-18cfd7d5b429')
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
        self.vs[2]["GUID__"] = UUID('3012d267-feb9-4748-b74e-e91056b85228')
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["mm__"] = """MT_post__paired_with"""
        self.vs[3]["GUID__"] = UUID('f8c54198-b5bd-49d4-a6b3-12727ca55922')
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
        self.vs[4]["MT_label__"] = """4"""
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
        self.vs[4]["mm__"] = """MT_post__Listen"""
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
        self.vs[4]["GUID__"] = UUID('6a97b30e-a214-474e-a65b-503a8b143618')
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
        self.vs[5]["GUID__"] = UUID('7f232bf7-5a7f-4224-8fa3-1cbdffde0d32')
        self.vs[6]["MT_label__"] = """6"""
        self.vs[6]["mm__"] = """MT_post__MatchModel"""
        self.vs[6]["GUID__"] = UUID('43339e57-f2f8-4809-bcd1-309114864f80')
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
        self.vs[7]["mm__"] = """MT_post__ListenBranch"""
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
        self.vs[7]["GUID__"] = UUID('e0d19d9a-d66f-4768-89fb-9a19bd9004bc')
        self.vs[8]["MT_post__cardinality"] = """
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
        self.vs[8]["mm__"] = """MT_post__ProcDef"""
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
        self.vs[8]["GUID__"] = UUID('088fd105-9105-4ef1-a256-879e34cb8519')
        self.vs[9]["MT_label__"] = """10"""
        self.vs[9]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[9]["GUID__"] = UUID('8d3ea17a-819f-490b-a938-da50d2290119')
        self.vs[10]["MT_label__"] = """11"""
        self.vs[10]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('70191e2b-3a0f-455c-b75b-c9d4ea6a479b')
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
        self.vs[11]["MT_label__"] = """12"""
        self.vs[11]["mm__"] = """MT_post__directLink_T"""
        self.vs[11]["GUID__"] = UUID('7f9fcaa8-8810-4d14-a5ea-b82c7e37a4c0')
        self.vs[12]["MT_post__associationType"] = """
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
        self.vs[12]["MT_label__"] = """13"""
        self.vs[12]["mm__"] = """MT_post__directLink_T"""
        self.vs[12]["GUID__"] = UUID('1b3a7ce9-9914-4ca6-90e1-ee238093fc0d')
        self.vs[13]["MT_post__associationType"] = """
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
        self.vs[13]["MT_label__"] = """14"""
        self.vs[13]["mm__"] = """MT_post__directLink_T"""
        self.vs[13]["GUID__"] = UUID('dffe0786-06ce-48f2-aacf-66923dd056ea')
        self.vs[14]["MT_label__"] = """9"""
        self.vs[14]["MT_post__type"] = """
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
        self.vs[14]["mm__"] = """MT_post__trace_link"""
        self.vs[14]["GUID__"] = UUID('5120a558-79dd-47de-8842-819a8b768b58')
        self.vs[15]["MT_label__"] = """15"""
        self.vs[15]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[15]["GUID__"] = UUID('51834f92-5a85-4db0-9e85-4e93e1c30b11')
        self.vs[16]["MT_label__"] = """16"""
        self.vs[16]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[16]["GUID__"] = UUID('c60c345b-b402-458c-b8f0-700f7377b91a')
        self.vs[17]["MT_label__"] = """17"""
        self.vs[17]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('e78aa84f-101c-4343-8ff9-4f82905a062b')
        self.vs[18]["MT_label__"] = """18"""
        self.vs[18]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('42e37b7a-ba7e-46dd-8ae1-923e85b16afe')
        self.vs[19]["MT_label__"] = """19"""
        self.vs[19]["mm__"] = """MT_post__apply_contains"""
        self.vs[19]["GUID__"] = UUID('d0e956a8-de28-4156-9a9a-2df798b27cf6')
        self.vs[20]["MT_label__"] = """20"""
        self.vs[20]["mm__"] = """MT_post__apply_contains"""
        self.vs[20]["GUID__"] = UUID('6672d46a-f947-4382-bb54-5071648b23ba')
        self.vs[21]["MT_label__"] = """21"""
        self.vs[21]["mm__"] = """MT_post__apply_contains"""
        self.vs[21]["GUID__"] = UUID('0d1452d7-1322-445d-a134-2280aef4bfce')
        self.vs[22]["MT_label__"] = """22"""
        self.vs[22]["mm__"] = """MT_post__apply_contains"""
        self.vs[22]["GUID__"] = UUID('629b6622-ad47-4bfc-96c0-8ce7570e8be1')
        self.vs[23]["MT_label__"] = """53"""
        self.vs[23]["mm__"] = """MT_post__trace_link"""
        self.vs[23]["GUID__"] = UUID('18174c72-d405-49aa-a64a-9512c81f3628')
        self.vs[24]["MT_label__"] = """54"""
        self.vs[24]["mm__"] = """MT_post__trace_link"""
        self.vs[24]["GUID__"] = UUID('439e2f05-6254-4e47-856d-0e85505e21aa')
        self.vs[25]["MT_label__"] = """55"""
        self.vs[25]["mm__"] = """MT_post__trace_link"""
        self.vs[25]["GUID__"] = UUID('2d67642b-17d4-4afb-858e-cfca378c7eb0')
        self.vs[26]["MT_label__"] = """23"""
        self.vs[26]["mm__"] = """MT_post__rightExpr"""
        self.vs[26]["GUID__"] = UUID('e8d41b9b-eb54-4d1d-9144-5b8c0b89e0e2')
        self.vs[27]["MT_label__"] = """24"""
        self.vs[27]["mm__"] = """MT_post__rightExpr"""
        self.vs[27]["GUID__"] = UUID('b31b7e57-2473-4ec9-99ce-1c8c62ec8457')
        self.vs[28]["MT_label__"] = """25"""
        self.vs[28]["mm__"] = """MT_post__rightExpr"""
        self.vs[28]["GUID__"] = UUID('b0a7fa7e-318d-4d1b-bd60-7bd91d94d888')
        self.vs[29]["MT_label__"] = """26"""
        self.vs[29]["mm__"] = """MT_post__rightExpr"""
        self.vs[29]["GUID__"] = UUID('9b85ea2d-a017-4c07-abd0-d65a8d282814')
        self.vs[30]["MT_label__"] = """27"""
        self.vs[30]["mm__"] = """MT_post__rightExpr"""
        self.vs[30]["GUID__"] = UUID('c4141c56-b907-49d1-a64a-fca6eb60d8da')
        self.vs[31]["MT_label__"] = """28"""
        self.vs[31]["mm__"] = """MT_post__rightExpr"""
        self.vs[31]["GUID__"] = UUID('58f724c6-4363-4728-81e1-699816c5f975')
        self.vs[32]["MT_label__"] = """29"""
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
        self.vs[32]["GUID__"] = UUID('24109be7-bd49-4e1f-af95-d6e3ca61c8aa')
        self.vs[33]["MT_label__"] = """30"""
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
        self.vs[33]["GUID__"] = UUID('e9e8ce4a-373a-4903-8702-bef13e769bb8')
        self.vs[34]["MT_label__"] = """31"""
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
        self.vs[34]["GUID__"] = UUID('7c0f9dc9-ff1e-41e0-8aaa-ca008508cfdf')
        self.vs[35]["MT_label__"] = """32"""
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
        self.vs[35]["GUID__"] = UUID('ace37e5d-80ae-43bf-95ce-d97e6a8a089c')
        self.vs[36]["MT_label__"] = """33"""
        self.vs[36]["MT_post__name"] = """
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
        self.vs[36]["mm__"] = """MT_post__Equation"""
        self.vs[36]["GUID__"] = UUID('7577802c-4da7-4c07-804b-64eb34a0f85e')
        self.vs[37]["MT_label__"] = """34"""
        self.vs[37]["MT_post__name"] = """
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
        self.vs[37]["mm__"] = """MT_post__Equation"""
        self.vs[37]["GUID__"] = UUID('bf7b5530-8570-4cce-9692-72be5eb11cdd')
        self.vs[38]["MT_post__Type"] = """
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
        self.vs[38]["MT_label__"] = """35"""
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
        self.vs[38]["mm__"] = """MT_post__Attribute"""
        self.vs[38]["GUID__"] = UUID('6c12abeb-a14e-45f7-a8f8-9fffc4d1da7a')
        self.vs[39]["MT_post__Type"] = """
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
        self.vs[39]["MT_label__"] = """36"""
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
        self.vs[39]["mm__"] = """MT_post__Attribute"""
        self.vs[39]["GUID__"] = UUID('b63caabd-4ad4-4b8c-8ee2-5fdc635a5d17')
        self.vs[40]["MT_post__Type"] = """
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
        self.vs[40]["MT_label__"] = """37"""
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
        self.vs[40]["mm__"] = """MT_post__Attribute"""
        self.vs[40]["GUID__"] = UUID('64698796-8c81-4112-b484-b3b3cec25b19')
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
        self.vs[41]["MT_label__"] = """38"""
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
        self.vs[41]["mm__"] = """MT_post__Attribute"""
        self.vs[41]["GUID__"] = UUID('5f7d851e-6760-4b03-981b-ab8157a55e79')
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
        self.vs[42]["MT_label__"] = """39"""
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
        self.vs[42]["mm__"] = """MT_post__Attribute"""
        self.vs[42]["GUID__"] = UUID('ea63e387-4401-4459-92f1-4008239d576f')
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
        self.vs[43]["MT_label__"] = """40"""
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
        self.vs[43]["mm__"] = """MT_post__Attribute"""
        self.vs[43]["GUID__"] = UUID('112f4f22-32a0-42b1-b3ce-37f41ee596bb')
        self.vs[44]["MT_label__"] = """41"""
        self.vs[44]["mm__"] = """MT_post__leftExpr"""
        self.vs[44]["GUID__"] = UUID('f6c31312-f3e4-4cd2-bedf-1bebe7cf6087')
        self.vs[45]["MT_label__"] = """42"""
        self.vs[45]["mm__"] = """MT_post__leftExpr"""
        self.vs[45]["GUID__"] = UUID('12aa1a99-b7db-473e-b842-0ca4c257a580')
        self.vs[46]["MT_label__"] = """43"""
        self.vs[46]["mm__"] = """MT_post__leftExpr"""
        self.vs[46]["GUID__"] = UUID('9f1172df-f03c-4405-8ac1-0aa0f8933357')
        self.vs[47]["MT_label__"] = """44"""
        self.vs[47]["mm__"] = """MT_post__leftExpr"""
        self.vs[47]["GUID__"] = UUID('e2e74508-528e-4d9d-9ca0-d80ac7972c1b')
        self.vs[48]["MT_label__"] = """45"""
        self.vs[48]["mm__"] = """MT_post__leftExpr"""
        self.vs[48]["GUID__"] = UUID('b487b571-f232-407c-a51a-f7e92bd77380')
        self.vs[49]["MT_label__"] = """46"""
        self.vs[49]["mm__"] = """MT_post__leftExpr"""
        self.vs[49]["GUID__"] = UUID('5e5dbafa-dbf6-42f8-a4e6-881f508e6cca')
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
        self.vs[50]["MT_label__"] = """47"""
        self.vs[50]["MT_post__name"] = """return 'false'"""
        self.vs[50]["mm__"] = """MT_post__Constant"""
        self.vs[50]["GUID__"] = UUID('3b447b03-1160-4ca3-a688-ac89f25ac52e')
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
        self.vs[51]["MT_label__"] = """48"""
        self.vs[51]["MT_post__name"] = """return 'true'"""
        self.vs[51]["mm__"] = """MT_post__Constant"""
        self.vs[51]["GUID__"] = UUID('a5fff7e5-0bcc-4839-a363-2b0dd2a2b6b7')
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
        self.vs[52]["MT_label__"] = """49"""
        self.vs[52]["MT_post__name"] = """return 'exit'"""
        self.vs[52]["mm__"] = """MT_post__Constant"""
        self.vs[52]["GUID__"] = UUID('711fe26a-0550-4135-b08e-b15a4f8762af')
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
        self.vs[53]["MT_label__"] = """50"""
        self.vs[53]["MT_post__name"] = """return 'exack'"""
        self.vs[53]["mm__"] = """MT_post__Constant"""
        self.vs[53]["GUID__"] = UUID('d6684611-ce79-4e4b-9150-1e53bd491e3b')
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
        self.vs[54]["MT_label__"] = """51"""
        self.vs[54]["MT_post__name"] = """return 'procdef'"""
        self.vs[54]["mm__"] = """MT_post__Constant"""
        self.vs[54]["GUID__"] = UUID('c005919f-108f-4d54-8e89-1091d9e779fd')
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
        self.vs[55]["MT_label__"] = """52"""
        self.vs[55]["MT_post__name"] = """return 'listensimplestate'"""
        self.vs[55]["mm__"] = """MT_post__Constant"""
        self.vs[55]["GUID__"] = UUID('c433d296-cc96-431a-be8a-b7561f3f481d')

        from HBasicState2ProcDef_rule_combinator_matcher_0 import HBasicState2ProcDef_rule_combinator_matcher_0
        self.pre = HBasicState2ProcDef_rule_combinator_matcher_0()
    
    def set_name47(self, attr_value, PreNode, graph):
        return 'false'


    def set_name48(self, attr_value, PreNode, graph):
        return 'true'


    def set_name49(self, attr_value, PreNode, graph):
        return 'exit'


    def set_name50(self, attr_value, PreNode, graph):
        return 'exack'


    def set_name51(self, attr_value, PreNode, graph):
        return 'procdef'


    def set_name52(self, attr_value, PreNode, graph):
        return 'listensimplestate'


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
        # Constant48
        try:
            graph.vs[labels['48']]['name'] = self.set_name48(graph.vs[labels['48']]['name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        graph.vs[labels['48']][Himesis.Constants.MT_DIRTY] = True
        # Constant47
        try:
            graph.vs[labels['47']]['name'] = self.set_name47(graph.vs[labels['47']]['name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        graph.vs[labels['47']][Himesis.Constants.MT_DIRTY] = True
        # Constant51
        try:
            graph.vs[labels['51']]['name'] = self.set_name51(graph.vs[labels['51']]['name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        graph.vs[labels['51']][Himesis.Constants.MT_DIRTY] = True
        
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
        # Listen4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Listen'
        # Trigger_T5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Trigger_T'
        # MatchModel6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # ListenBranch7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ListenBranch'
        # directLink_T12
        new_node = graph.add_node()
        labels['12'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T13
        new_node = graph.add_node()
        labels['13'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # directLink_T14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # hasAttribute_T15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # hasAttribute_T18
        new_node = graph.add_node()
        labels['18'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
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
        # apply_contains22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # rightExpr25
        new_node = graph.add_node()
        labels['25'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr26
        new_node = graph.add_node()
        labels['26'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr28
        new_node = graph.add_node()
        labels['28'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation31
        new_node = graph.add_node()
        labels['31'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation32
        new_node = graph.add_node()
        labels['32'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation34
        new_node = graph.add_node()
        labels['34'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Attribute37
        new_node = graph.add_node()
        labels['37'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute38
        new_node = graph.add_node()
        labels['38'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # Attribute40
        new_node = graph.add_node()
        labels['40'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # leftExpr43
        new_node = graph.add_node()
        labels['43'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr44
        new_node = graph.add_node()
        labels['44'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr46
        new_node = graph.add_node()
        labels['46'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Constant49
        new_node = graph.add_node()
        labels['49'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name49(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant50
        new_node = graph.add_node()
        labels['50'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name50(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant52
        new_node = graph.add_node()
        labels['52'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name52(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # trace_link53
        new_node = graph.add_node()
        labels['53'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link54
        new_node = graph.add_node()
        labels['54'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # trace_link55
        new_node = graph.add_node()
        labels['55'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # paired_with3 -> ApplyModel0
        graph.add_edges([(labels['3'], labels['0'])])
        # ApplyModel0 -> apply_contains19
        graph.add_edges([(labels['0'], labels['19'])])
        # ApplyModel0 -> apply_contains20
        graph.add_edges([(labels['0'], labels['20'])])
        # ApplyModel0 -> apply_contains21
        graph.add_edges([(labels['0'], labels['21'])])
        # ApplyModel0 -> apply_contains22
        graph.add_edges([(labels['0'], labels['22'])])
        # MatchModel6 -> match_contains1
        graph.add_edges([(labels['6'], labels['1'])])
        # match_contains1 -> State2
        graph.add_edges([(labels['1'], labels['2'])])
        # ProcDef8 -> directLink_T12
        graph.add_edges([(labels['8'], labels['12'])])
        # directLink_T12 -> Listen4
        graph.add_edges([(labels['12'], labels['4'])])
        # Listen4 -> directLink_T13
        graph.add_edges([(labels['4'], labels['13'])])
        # directLink_T13 -> ListenBranch7
        graph.add_edges([(labels['13'], labels['7'])])
        # ListenBranch7 -> directLink_T14
        graph.add_edges([(labels['7'], labels['14'])])
        # directLink_T14 -> Trigger_T5
        graph.add_edges([(labels['14'], labels['5'])])
        # ListenBranch7 -> hasAttribute_T15
        graph.add_edges([(labels['7'], labels['15'])])
        # hasAttribute_T15 -> Attribute37
        graph.add_edges([(labels['15'], labels['37'])])
        # Trigger_T5 -> hasAttribute_T16
        graph.add_edges([(labels['5'], labels['16'])])
        # hasAttribute_T16 -> Attribute38
        graph.add_edges([(labels['16'], labels['38'])])
        # Listen4 -> hasAttribute_T18
        graph.add_edges([(labels['4'], labels['18'])])
        # hasAttribute_T18 -> Attribute40
        graph.add_edges([(labels['18'], labels['40'])])
        # apply_contains19 -> ProcDef8
        graph.add_edges([(labels['19'], labels['8'])])
        # apply_contains20 -> Listen4
        graph.add_edges([(labels['20'], labels['4'])])
        # apply_contains21 -> ListenBranch7
        graph.add_edges([(labels['21'], labels['7'])])
        # apply_contains22 -> Trigger_T5
        graph.add_edges([(labels['22'], labels['5'])])
        # Equation31 -> rightExpr25
        graph.add_edges([(labels['31'], labels['25'])])
        # rightExpr25 -> Constant49
        graph.add_edges([(labels['25'], labels['49'])])
        # Equation32 -> rightExpr26
        graph.add_edges([(labels['32'], labels['26'])])
        # rightExpr26 -> Constant50
        graph.add_edges([(labels['26'], labels['50'])])
        # Equation34 -> rightExpr28
        graph.add_edges([(labels['34'], labels['28'])])
        # rightExpr28 -> Constant52
        graph.add_edges([(labels['28'], labels['52'])])
        # MatchModel6 -> paired_with3
        graph.add_edges([(labels['6'], labels['3'])])
        # Equation31 -> leftExpr43
        graph.add_edges([(labels['31'], labels['43'])])
        # Equation32 -> leftExpr44
        graph.add_edges([(labels['32'], labels['44'])])
        # Equation34 -> leftExpr46
        graph.add_edges([(labels['34'], labels['46'])])
        # leftExpr43 -> Attribute37
        graph.add_edges([(labels['43'], labels['37'])])
        # leftExpr44 -> Attribute38
        graph.add_edges([(labels['44'], labels['38'])])
        # Listen4 -> trace_link53
        graph.add_edges([(labels['4'], labels['53'])])
        # leftExpr46 -> Attribute40
        graph.add_edges([(labels['46'], labels['40'])])
        # Trigger_T5 -> trace_link55
        graph.add_edges([(labels['5'], labels['55'])])
        # trace_link53 -> State2
        graph.add_edges([(labels['53'], labels['2'])])
        # ListenBranch7 -> trace_link54
        graph.add_edges([(labels['7'], labels['54'])])
        # trace_link54 -> State2
        graph.add_edges([(labels['54'], labels['2'])])
        # trace_link55 -> State2
        graph.add_edges([(labels['55'], labels['2'])])
        
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
    
