

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HBasicStateNoOutgoing2ProcDef_rule_combinator_matcher_0(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicStateNoOutgoing2ProcDef_rule_combinator_matcher_0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicStateNoOutgoing2ProcDef_rule_combinator_matcher_0, self).__init__(name='HBasicStateNoOutgoing2ProcDef_rule_combinator_matcher_0', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[10, 6], [6, 19], [9, 7], [7, 18], [11, 8], [8, 20], [2, 0], [0, 14], [1, 4], [4, 12], [1, 5], [5, 13], [3, 1], [9, 15], [10, 16], [11, 17], [2, 3], [15, 12], [16, 13], [17, 14]])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__UMLRT2Kiltera_MM'
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
        self["name"] = """HBasicStateNoOutgoing2ProcDef_rule_combinator_matcher_0_rc_matcher"""
        self["GUID__"] = UUID('08346ac3-1a47-4fed-a83e-4b403ea6994d')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__hasAttribute_T"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('9fb62753-1769-4343-a251-1e39317acbe9')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """
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
        self.vs[1]["MT_pre__cardinality"] = """
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
        self.vs[1]["MT_label__"] = """4"""
        self.vs[1]["mm__"] = """MT_pre__State"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__name"] = """
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
        self.vs[1]["GUID__"] = UUID('c6922e5f-99ee-4364-a792-6c57221d528a')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = """
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
        self.vs[2]["MT_pre__cardinality"] = """
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
        self.vs[2]["MT_label__"] = """8"""
        self.vs[2]["mm__"] = """MT_pre__ProcDef"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__name"] = """
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
        self.vs[2]["GUID__"] = UUID('9233ea41-f0ba-46a2-9cf5-1afcc0e29357')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """9"""
        self.vs[3]["mm__"] = """MT_pre__trace_link"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('ec016c81-d5de-4142-be2b-a2c199b4bd4d')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """10"""
        self.vs[4]["mm__"] = """MT_pre__hasAttribute_S"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('08746aa3-1cce-4d1b-836a-a4a32027579c')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """11"""
        self.vs[5]["mm__"] = """MT_pre__hasAttribute_S"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('c044e48e-3dbf-4672-a699-664c44b592ea')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """14"""
        self.vs[6]["mm__"] = """MT_pre__rightExpr"""
        self.vs[6]["MT_subtypes__"] = """[]"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('2084dd88-dcc6-4cc4-bf73-4e6ba642889d')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """15"""
        self.vs[7]["mm__"] = """MT_pre__rightExpr"""
        self.vs[7]["MT_subtypes__"] = """[]"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('5f6be339-0999-4fd7-9e9d-eb543ad11b08')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """16"""
        self.vs[8]["mm__"] = """MT_pre__rightExpr"""
        self.vs[8]["MT_subtypes__"] = """[]"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["GUID__"] = UUID('0db1fbd6-cb67-4813-963f-9e0c55025b24')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """17"""
        self.vs[9]["mm__"] = """MT_pre__Equation"""
        self.vs[9]["MT_subtypes__"] = """[]"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["MT_pre__name"] = """
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
        self.vs[9]["GUID__"] = UUID('8b49bbf3-1bf9-428d-84ed-d98e720da5d5')
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_label__"] = """18"""
        self.vs[10]["mm__"] = """MT_pre__Equation"""
        self.vs[10]["MT_subtypes__"] = """[]"""
        self.vs[10]["MT_dirty__"] = False
        self.vs[10]["MT_pre__name"] = """
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
        self.vs[10]["GUID__"] = UUID('97df9a79-4269-4dfe-8196-a03ec0a36eca')
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_label__"] = """19"""
        self.vs[11]["mm__"] = """MT_pre__Equation"""
        self.vs[11]["MT_subtypes__"] = """[]"""
        self.vs[11]["MT_dirty__"] = False
        self.vs[11]["MT_pre__name"] = """
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
        self.vs[11]["GUID__"] = UUID('7d22d7b5-ae26-4fae-8ca0-6ac250ed9d1b')
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_label__"] = """20"""
        self.vs[12]["mm__"] = """MT_pre__Attribute"""
        self.vs[12]["MT_pre__Type"] = """
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
        self.vs[12]["MT_subtypes__"] = """[]"""
        self.vs[12]["MT_dirty__"] = False
        self.vs[12]["MT_pre__name"] = """if attr_value == "isComposite":
    return True
return False
"""
        self.vs[12]["GUID__"] = UUID('a9c9e9b8-d009-40a7-a9ea-df0fc913200d')
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_label__"] = """21"""
        self.vs[13]["mm__"] = """MT_pre__Attribute"""
        self.vs[13]["MT_pre__Type"] = """
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
        self.vs[13]["MT_subtypes__"] = """[]"""
        self.vs[13]["MT_dirty__"] = False
        self.vs[13]["MT_pre__name"] = """if attr_value == "hasOutgoingTransitions":
    return True
return False
"""
        self.vs[13]["GUID__"] = UUID('afd9794f-4f68-4d05-94ab-d63985935fce')
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_label__"] = """22"""
        self.vs[14]["mm__"] = """MT_pre__Attribute"""
        self.vs[14]["MT_pre__Type"] = """
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
        self.vs[14]["MT_subtypes__"] = """[]"""
        self.vs[14]["MT_dirty__"] = False
        self.vs[14]["MT_pre__name"] = """if attr_value == "pivotin":
    return True
return False
"""
        self.vs[14]["GUID__"] = UUID('ab7d9cc5-6f6b-496b-a28b-9f5d80992d12')
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_label__"] = """23"""
        self.vs[15]["mm__"] = """MT_pre__leftExpr"""
        self.vs[15]["MT_subtypes__"] = """[]"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["GUID__"] = UUID('f76659f6-1300-451e-91d1-41677c07802c')
        self.vs[16]["MT_subtypeMatching__"] = False
        self.vs[16]["MT_label__"] = """24"""
        self.vs[16]["mm__"] = """MT_pre__leftExpr"""
        self.vs[16]["MT_subtypes__"] = """[]"""
        self.vs[16]["MT_dirty__"] = False
        self.vs[16]["GUID__"] = UUID('d6d9217b-413d-485e-92b7-714d2727a400')
        self.vs[17]["MT_subtypeMatching__"] = False
        self.vs[17]["MT_label__"] = """25"""
        self.vs[17]["mm__"] = """MT_pre__leftExpr"""
        self.vs[17]["MT_subtypes__"] = """[]"""
        self.vs[17]["MT_dirty__"] = False
        self.vs[17]["GUID__"] = UUID('6c08f50c-fa5f-417e-ae40-7d2964489148')
        self.vs[18]["MT_subtypeMatching__"] = False
        self.vs[18]["MT_label__"] = """26"""
        self.vs[18]["mm__"] = """MT_pre__Constant"""
        self.vs[18]["MT_pre__Type"] = """
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
        self.vs[18]["MT_subtypes__"] = """[]"""
        self.vs[18]["MT_dirty__"] = False
        self.vs[18]["MT_pre__name"] = """
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
        self.vs[18]["GUID__"] = UUID('780ccb04-ca3a-4391-a999-828acfbc3691')
        self.vs[19]["MT_subtypeMatching__"] = False
        self.vs[19]["MT_label__"] = """27"""
        self.vs[19]["mm__"] = """MT_pre__Constant"""
        self.vs[19]["MT_pre__Type"] = """
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
        self.vs[19]["MT_subtypes__"] = """[]"""
        self.vs[19]["MT_dirty__"] = False
        self.vs[19]["MT_pre__name"] = """
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
        self.vs[19]["GUID__"] = UUID('4ebd2dfc-60e3-47f5-ac8a-395158a30a95')
        self.vs[20]["MT_subtypeMatching__"] = False
        self.vs[20]["MT_label__"] = """28"""
        self.vs[20]["mm__"] = """MT_pre__Constant"""
        self.vs[20]["MT_pre__Type"] = """
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
        self.vs[20]["MT_subtypes__"] = """[]"""
        self.vs[20]["MT_dirty__"] = False
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
        self.vs[20]["GUID__"] = UUID('e1138885-34ab-4053-98d8-8006df3406f3')

    def eval_classtype4(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality4(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name4(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype8(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality8(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name8(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name17(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name18(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name19(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_Type20(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name20(self, attr_value, this):
        if attr_value == "isComposite":
            return True
        return False


    def eval_Type21(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name21(self, attr_value, this):
        if attr_value == "hasOutgoingTransitions":
            return True
        return False


    def eval_Type22(self, attr_value, this):
        
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
        if attr_value == "pivotin":
            return True
        return False


    def eval_Type26(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name26(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_Type27(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name27(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_Type28(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name28(self, attr_value, this):
        
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

