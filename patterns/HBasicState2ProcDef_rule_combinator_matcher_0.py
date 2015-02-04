

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HBasicState2ProcDef_rule_combinator_matcher_0(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicState2ProcDef_rule_combinator_matcher_0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef_rule_combinator_matcher_0, self).__init__(name='HBasicState2ProcDef_rule_combinator_matcher_0', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[9, 6], [6, 18], [10, 7], [7, 19], [11, 8], [8, 20], [1, 3], [3, 14], [0, 4], [4, 12], [0, 5], [5, 13], [2, 0], [9, 15], [10, 16], [11, 17], [1, 2], [15, 12], [16, 13], [17, 14]])
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
        self["name"] = """HBasicState2ProcDef_rule_combinator_matcher_0_rc_matcher"""
        self["GUID__"] = UUID('bc8da8f4-6500-4462-ab6c-29a0e49f1222')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """
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
        self.vs[0]["MT_pre__cardinality"] = """
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
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["mm__"] = """MT_pre__State"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__name"] = """
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
        self.vs[0]["GUID__"] = UUID('3012d267-feb9-4748-b74e-e91056b85228')
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
        self.vs[1]["MT_label__"] = """8"""
        self.vs[1]["mm__"] = """MT_pre__ProcDef"""
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
        self.vs[1]["GUID__"] = UUID('088fd105-9105-4ef1-a256-879e34cb8519')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """9"""
        self.vs[2]["mm__"] = """MT_pre__trace_link"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('5120a558-79dd-47de-8842-819a8b768b58')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """17"""
        self.vs[3]["mm__"] = """MT_pre__hasAttribute_T"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('e78aa84f-101c-4343-8ff9-4f82905a062b')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """10"""
        self.vs[4]["mm__"] = """MT_pre__hasAttribute_S"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('8d3ea17a-819f-490b-a938-da50d2290119')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """11"""
        self.vs[5]["mm__"] = """MT_pre__hasAttribute_S"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('70191e2b-3a0f-455c-b75b-c9d4ea6a479b')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """23"""
        self.vs[6]["mm__"] = """MT_pre__rightExpr"""
        self.vs[6]["MT_subtypes__"] = """[]"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('e8d41b9b-eb54-4d1d-9144-5b8c0b89e0e2')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """24"""
        self.vs[7]["mm__"] = """MT_pre__rightExpr"""
        self.vs[7]["MT_subtypes__"] = """[]"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('b31b7e57-2473-4ec9-99ce-1c8c62ec8457')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """27"""
        self.vs[8]["mm__"] = """MT_pre__rightExpr"""
        self.vs[8]["MT_subtypes__"] = """[]"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["GUID__"] = UUID('c4141c56-b907-49d1-a64a-fca6eb60d8da')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """29"""
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
        self.vs[9]["GUID__"] = UUID('24109be7-bd49-4e1f-af95-d6e3ca61c8aa')
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_label__"] = """30"""
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
        self.vs[10]["GUID__"] = UUID('e9e8ce4a-373a-4903-8702-bef13e769bb8')
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_label__"] = """33"""
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
        self.vs[11]["GUID__"] = UUID('7577802c-4da7-4c07-804b-64eb34a0f85e')
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_label__"] = """35"""
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
        self.vs[12]["GUID__"] = UUID('6c12abeb-a14e-45f7-a8f8-9fffc4d1da7a')
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_label__"] = """36"""
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
        self.vs[13]["GUID__"] = UUID('b63caabd-4ad4-4b8c-8ee2-5fdc635a5d17')
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_label__"] = """39"""
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
        self.vs[14]["GUID__"] = UUID('ea63e387-4401-4459-92f1-4008239d576f')
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_label__"] = """41"""
        self.vs[15]["mm__"] = """MT_pre__leftExpr"""
        self.vs[15]["MT_subtypes__"] = """[]"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["GUID__"] = UUID('f6c31312-f3e4-4cd2-bedf-1bebe7cf6087')
        self.vs[16]["MT_subtypeMatching__"] = False
        self.vs[16]["MT_label__"] = """42"""
        self.vs[16]["mm__"] = """MT_pre__leftExpr"""
        self.vs[16]["MT_subtypes__"] = """[]"""
        self.vs[16]["MT_dirty__"] = False
        self.vs[16]["GUID__"] = UUID('12aa1a99-b7db-473e-b842-0ca4c257a580')
        self.vs[17]["MT_subtypeMatching__"] = False
        self.vs[17]["MT_label__"] = """45"""
        self.vs[17]["mm__"] = """MT_pre__leftExpr"""
        self.vs[17]["MT_subtypes__"] = """[]"""
        self.vs[17]["MT_dirty__"] = False
        self.vs[17]["GUID__"] = UUID('b487b571-f232-407c-a51a-f7e92bd77380')
        self.vs[18]["MT_subtypeMatching__"] = False
        self.vs[18]["MT_label__"] = """47"""
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
        self.vs[18]["GUID__"] = UUID('3b447b03-1160-4ca3-a688-ac89f25ac52e')
        self.vs[19]["MT_subtypeMatching__"] = False
        self.vs[19]["MT_label__"] = """48"""
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
        self.vs[19]["GUID__"] = UUID('a5fff7e5-0bcc-4839-a363-2b0dd2a2b6b7')
        self.vs[20]["MT_subtypeMatching__"] = False
        self.vs[20]["MT_label__"] = """51"""
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
        self.vs[20]["GUID__"] = UUID('c005919f-108f-4d54-8e89-1091d9e779fd')

    def eval_classtype2(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality2(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name2(self, attr_value, this):
        
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


    def eval_name29(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name30(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name33(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_Type35(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name35(self, attr_value, this):
        if attr_value == "isComposite":
            return True
        return False


    def eval_Type36(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name36(self, attr_value, this):
        if attr_value == "hasOutgoingTransitions":
            return True
        return False


    def eval_Type39(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name39(self, attr_value, this):
        if attr_value == "pivotin":
            return True
        return False


    def eval_Type47(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name47(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_Type48(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name48(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_Type51(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name51(self, attr_value, this):
        
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

