

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HProperty1_completeLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HProperty1_completeLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HProperty1_completeLHS, self).__init__(name='HProperty1_completeLHS', num_nodes=41, edges=[])
        
        # Add the edges
        self.add_edges([(4, 12), (2, 12), (6, 13), (8, 13), (5, 14), (3, 14), (7, 15), (9, 15), (10, 2), (11, 3), (1, 36), (36, 22), (1, 37), (37, 34), (1, 38), (38, 33), (1, 39), (39, 23), (1, 40), (40, 34), (0, 16), (0, 17), (0, 18), (0, 19), (32, 4), (35, 5), (16, 32), (17, 21), (18, 20), (19, 35), (33, 6), (34, 7), (27, 20), (20, 24), (25, 21), (21, 26), (31, 22), (22, 28), (29, 23), (23, 30), (24, 35), (35, 25), (26, 32), (32, 27), (28, 34), (34, 29), (30, 33), (33, 31), (10, 8), (11, 9)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__ECoreMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
        self["name"] = """"""
        self["GUID__"] = UUID('ad01df2c-8e26-4d62-9e02-d3203252ec43')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__MatchModel"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('0388b4db-07f8-4d06-9444-34e77ea9206c')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """11"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('8623671c-cd32-4895-8fd6-1c59404aa9d2')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """41"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__leftExpr"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('cba9fbb9-97e6-4852-b250-a1992f17628a')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """43"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__leftExpr"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('7c44abfe-4072-44d4-8fdf-fd1eaf161d3b')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """35"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__hasAttrs"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('cbee8b81-cc86-4b1c-a0b0-4083916ab28f')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """37"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["mm__"] = """MT_pre__hasAttrs"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('7999201b-f389-4f75-8cea-bb616b6b7468')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """36"""
        self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[6]["mm__"] = """MT_pre__hasAttrs"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('2f76c371-c20f-4511-ab06-95d6552c1c3f')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """38"""
        self.vs[7]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[7]["mm__"] = """MT_pre__hasAttrs"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('739e8979-77dd-4b07-9948-4c98ea77c92a')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """42"""
        self.vs[8]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """MT_pre__rightExpr"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["GUID__"] = UUID('c21019de-d96f-4dcf-80fb-8345de99a1b2')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """44"""
        self.vs[9]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[9]["mm__"] = """MT_pre__rightExpr"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["GUID__"] = UUID('62fdfd67-c403-4d25-a4e5-c826d61eadf9')
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_label__"] = """39"""
        self.vs[10]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[10]["mm__"] = """MT_pre__Equation"""
        self.vs[10]["MT_dirty__"] = False
        self.vs[10]["GUID__"] = UUID('0e6e07c1-45ec-42ed-b696-04f6b606ea2f')
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_label__"] = """40"""
        self.vs[11]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[11]["mm__"] = """MT_pre__Equation"""
        self.vs[11]["MT_dirty__"] = False
        self.vs[11]["GUID__"] = UUID('56c9a27e-3e4a-4e92-a66c-daf34ec42933')
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_label__"] = """31"""
        self.vs[12]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[12]["mm__"] = """MT_pre__Attribute"""
        self.vs[12]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[12]["MT_dirty__"] = False
        self.vs[12]["GUID__"] = UUID('b25b9536-0f39-4e9b-9b53-c9e0161ff666')
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_label__"] = """32"""
        self.vs[13]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[13]["mm__"] = """MT_pre__Attribute"""
        self.vs[13]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[13]["MT_dirty__"] = False
        self.vs[13]["GUID__"] = UUID('e2b499f0-f1a6-4d1a-b9f4-1bb6035d11eb')
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_label__"] = """33"""
        self.vs[14]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[14]["mm__"] = """MT_pre__Attribute"""
        self.vs[14]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[14]["MT_dirty__"] = False
        self.vs[14]["GUID__"] = UUID('f783bedb-b552-47ce-8bf1-90401fe68e39')
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_label__"] = """34"""
        self.vs[15]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[15]["mm__"] = """MT_pre__Attribute"""
        self.vs[15]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["GUID__"] = UUID('e08e4cf4-84b7-489e-8bc5-9c0caef9f486')
        self.vs[16]["MT_subtypeMatching__"] = False
        self.vs[16]["MT_label__"] = """7"""
        self.vs[16]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[16]["mm__"] = """MT_pre__match_contains"""
        self.vs[16]["MT_dirty__"] = False
        self.vs[16]["GUID__"] = UUID('af14c21d-329c-4863-826d-0c0130dc1447')
        self.vs[17]["MT_subtypeMatching__"] = False
        self.vs[17]["MT_label__"] = """16"""
        self.vs[17]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[17]["mm__"] = """MT_pre__match_contains"""
        self.vs[17]["MT_dirty__"] = False
        self.vs[17]["GUID__"] = UUID('024a4b03-d4d0-464e-9c05-05faad14e50a')
        self.vs[18]["MT_subtypeMatching__"] = False
        self.vs[18]["MT_label__"] = """17"""
        self.vs[18]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[18]["mm__"] = """MT_pre__match_contains"""
        self.vs[18]["MT_dirty__"] = False
        self.vs[18]["GUID__"] = UUID('e3a3e210-7dda-46f5-b710-68df099b4fd1')
        self.vs[19]["MT_subtypeMatching__"] = False
        self.vs[19]["MT_label__"] = """45"""
        self.vs[19]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[19]["mm__"] = """MT_pre__match_contains"""
        self.vs[19]["MT_dirty__"] = False
        self.vs[19]["GUID__"] = UUID('270453c0-c7f9-48f0-b31a-327ecd527811')
        self.vs[20]["MT_subtypeMatching__"] = False
        self.vs[20]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[20]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[20]["MT_label__"] = """9"""
        self.vs[20]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[20]["mm__"] = """MT_pre__EReference"""
        self.vs[20]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[20]["MT_dirty__"] = False
        self.vs[20]["GUID__"] = UUID('9a42b613-6802-431c-8e98-d93aeeb8a276')
        self.vs[21]["MT_subtypeMatching__"] = False
        self.vs[21]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[21]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[21]["MT_label__"] = """10"""
        self.vs[21]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[21]["mm__"] = """MT_pre__EReference"""
        self.vs[21]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[21]["MT_dirty__"] = False
        self.vs[21]["GUID__"] = UUID('ce4ce7bb-cb92-46b4-8fa6-d627391e31db')
        self.vs[22]["MT_subtypeMatching__"] = False
        self.vs[22]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[22]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[22]["MT_label__"] = """14"""
        self.vs[22]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[22]["mm__"] = """MT_pre__EReference"""
        self.vs[22]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[22]["MT_dirty__"] = False
        self.vs[22]["GUID__"] = UUID('2dcf52e9-2b9c-444e-8acd-8841f42a8194')
        self.vs[23]["MT_subtypeMatching__"] = False
        self.vs[23]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[23]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[23]["MT_label__"] = """15"""
        self.vs[23]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[23]["mm__"] = """MT_pre__EReference"""
        self.vs[23]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[23]["MT_dirty__"] = False
        self.vs[23]["GUID__"] = UUID('27416fcb-4382-4be0-9ed9-2c7f12ac41e0')
        self.vs[24]["MT_subtypeMatching__"] = False
        self.vs[24]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eType"
"""
        self.vs[24]["MT_label__"] = """23"""
        self.vs[24]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[24]["mm__"] = """MT_pre__directLink_S"""
        self.vs[24]["MT_dirty__"] = False
        self.vs[24]["GUID__"] = UUID('ab36e592-d9b8-42fb-87a0-ca2bffab403f')
        self.vs[25]["MT_subtypeMatching__"] = False
        self.vs[25]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eStructuralFeatures"
"""
        self.vs[25]["MT_label__"] = """24"""
        self.vs[25]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[25]["mm__"] = """MT_pre__directLink_S"""
        self.vs[25]["MT_dirty__"] = False
        self.vs[25]["GUID__"] = UUID('418792c6-baaf-448c-94e0-a018f268c384')
        self.vs[26]["MT_subtypeMatching__"] = False
        self.vs[26]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eType"
"""
        self.vs[26]["MT_label__"] = """25"""
        self.vs[26]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[26]["mm__"] = """MT_pre__directLink_S"""
        self.vs[26]["MT_dirty__"] = False
        self.vs[26]["GUID__"] = UUID('4c6f5773-5781-45c8-8812-3b046e51cb87')
        self.vs[27]["MT_subtypeMatching__"] = False
        self.vs[27]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eStructuralFeatures"
"""
        self.vs[27]["MT_label__"] = """26"""
        self.vs[27]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[27]["mm__"] = """MT_pre__directLink_S"""
        self.vs[27]["MT_dirty__"] = False
        self.vs[27]["GUID__"] = UUID('bf345f3f-576b-44ed-9134-e836362a9200')
        self.vs[28]["MT_subtypeMatching__"] = False
        self.vs[28]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eType"
"""
        self.vs[28]["MT_label__"] = """27"""
        self.vs[28]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[28]["mm__"] = """MT_pre__directLink_T"""
        self.vs[28]["MT_dirty__"] = False
        self.vs[28]["GUID__"] = UUID('a2cb8a04-b0d8-4668-af87-4aaba7231584')
        self.vs[29]["MT_subtypeMatching__"] = False
        self.vs[29]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eStructuralFeatures"
"""
        self.vs[29]["MT_label__"] = """28"""
        self.vs[29]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[29]["mm__"] = """MT_pre__directLink_T"""
        self.vs[29]["MT_dirty__"] = False
        self.vs[29]["GUID__"] = UUID('68c9ce7e-1244-4f76-89d1-4da45d52f02d')
        self.vs[30]["MT_subtypeMatching__"] = False
        self.vs[30]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eType"
"""
        self.vs[30]["MT_label__"] = """29"""
        self.vs[30]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[30]["mm__"] = """MT_pre__directLink_T"""
        self.vs[30]["MT_dirty__"] = False
        self.vs[30]["GUID__"] = UUID('07d536fa-c7af-488a-9422-1754e5484a1b')
        self.vs[31]["MT_subtypeMatching__"] = False
        self.vs[31]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "eStructuralFeatures"
"""
        self.vs[31]["MT_label__"] = """30"""
        self.vs[31]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[31]["mm__"] = """MT_pre__directLink_T"""
        self.vs[31]["MT_dirty__"] = False
        self.vs[31]["GUID__"] = UUID('58ae8e69-47a0-4293-8bcf-ec8ef7e58760')
        self.vs[32]["MT_subtypeMatching__"] = False
        self.vs[32]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[32]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[32]["MT_label__"] = """1"""
        self.vs[32]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[32]["mm__"] = """MT_pre__EClass"""
        self.vs[32]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[32]["MT_dirty__"] = False
        self.vs[32]["GUID__"] = UUID('876a2030-f24c-499b-82f5-6999295b8cb3')
        self.vs[33]["MT_subtypeMatching__"] = False
        self.vs[33]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[33]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[33]["MT_label__"] = """12"""
        self.vs[33]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[33]["mm__"] = """MT_pre__EClass"""
        self.vs[33]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[33]["MT_dirty__"] = False
        self.vs[33]["GUID__"] = UUID('ffda571a-80b1-4401-83e7-618757ecc3b5')
        self.vs[34]["MT_subtypeMatching__"] = False
        self.vs[34]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[34]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[34]["MT_label__"] = """13"""
        self.vs[34]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[34]["mm__"] = """MT_pre__EClass"""
        self.vs[34]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[34]["MT_dirty__"] = False
        self.vs[34]["GUID__"] = UUID('a9485f70-144b-4f03-931a-bc72abf6ca54')
        self.vs[35]["MT_subtypeMatching__"] = False
        self.vs[35]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[35]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[35]["MT_label__"] = """22"""
        self.vs[35]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[35]["mm__"] = """MT_pre__EClass"""
        self.vs[35]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[35]["MT_dirty__"] = False
        self.vs[35]["GUID__"] = UUID('951cf678-55b0-4a33-86d2-87c46a6c59a2')
        self.vs[36]["MT_subtypeMatching__"] = False
        self.vs[36]["MT_label__"] = """18"""
        self.vs[36]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[36]["mm__"] = """MT_pre__apply_contains"""
        self.vs[36]["MT_dirty__"] = False
        self.vs[36]["GUID__"] = UUID('925acb30-1d31-41a6-800f-b3cc4c7e373c')
        self.vs[37]["MT_subtypeMatching__"] = False
        self.vs[37]["MT_label__"] = """19"""
        self.vs[37]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[37]["mm__"] = """MT_pre__apply_contains"""
        self.vs[37]["MT_dirty__"] = False
        self.vs[37]["GUID__"] = UUID('2ef82eb8-2563-4fd5-86a3-ccbb4bdd30a4')
        self.vs[38]["MT_subtypeMatching__"] = False
        self.vs[38]["MT_label__"] = """20"""
        self.vs[38]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[38]["mm__"] = """MT_pre__apply_contains"""
        self.vs[38]["MT_dirty__"] = False
        self.vs[38]["GUID__"] = UUID('f86fdd7b-2237-4cfb-8f78-d2d29f830bb6')
        self.vs[39]["MT_subtypeMatching__"] = False
        self.vs[39]["MT_label__"] = """21"""
        self.vs[39]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[39]["mm__"] = """MT_pre__apply_contains"""
        self.vs[39]["MT_dirty__"] = False
        self.vs[39]["GUID__"] = UUID('f1b6f16c-fe51-4726-9e19-071bbcac03ff')
        self.vs[40]["MT_subtypeMatching__"] = False
        self.vs[40]["MT_label__"] = """46"""
        self.vs[40]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[40]["mm__"] = """MT_pre__apply_contains"""
        self.vs[40]["MT_dirty__"] = False
        self.vs[40]["GUID__"] = UUID('1d8a5487-8ccc-4808-8976-d7cf3735954d')

    def eval_name31(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name32(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name33(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name34(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_classtype9(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality9(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name9(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype10(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality10(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name10(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype15(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality15(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name15(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_associationType23(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eType"


    def eval_associationType24(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eStructuralFeatures"


    def eval_associationType25(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eType"


    def eval_associationType26(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eStructuralFeatures"


    def eval_associationType27(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eType"


    def eval_associationType28(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eStructuralFeatures"


    def eval_associationType29(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eType"


    def eval_associationType30(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "eStructuralFeatures"


    def eval_classtype1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype12(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality12(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name12(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype13(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality13(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name13(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype22(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality22(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name22(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================
        
        return True

