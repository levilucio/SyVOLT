

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HMoveOneInputDirectApplyDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneInputDirectApplyDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneInputDirectApplyDiffRulesLHS, self).__init__(name='HMoveOneInputDirectApplyDiffRulesLHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[0, 2], [3, 0]])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__UMLRT2Kiltera_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""Vreturn True\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('0ea9f228-d190-4625-b2e6-39bb648597be')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__associationType"] = """
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
        self.vs[0]["MT_label__"] = """9"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__directLink_T"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('ee55b788-96b4-422e-b8c6-26a9c53feda1')
        self.vs[1]["MT_pivotOut__"] = """element1"""
        self.vs[1]["MT_subtypeMatching__"] = True
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
        self.vs[1]["MT_pivotIn__"] = """element1"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__Name'
p2
aS'MT_pre__Module'
p3
aS'MT_pre__ConditionBranch'
p4
aS'MT_pre__Delay'
p5
aS'MT_pre__LocalDef'
p6
aS'MT_pre__Expr'
p7
aS'MT_pre__ConditionSet'
p8
aS'MT_pre__Proc'
p9
aS'MT_pre__MatchCase'
p10
aS'MT_pre__Match'
p11
aS'MT_pre__FuncDef'
p12
aS'MT_pre__Null'
p13
aS'MT_pre__Par'
p14
aS'MT_pre__Inst'
p15
aS'MT_pre__Listen'
p16
aS'MT_pre__Site'
p17
aS'MT_pre__New'
p18
aS'MT_pre__PythonRef'
p19
aS'MT_pre__Def'
p20
aS'MT_pre__Seq'
p21
aS'MT_pre__ParIndexed'
p22
aS'MT_pre__Condition'
p23
aS'MT_pre__Print'
p24
aS'MT_pre__Pattern'
p25
aS'MT_pre__ListenBranch'
p26
aS'MT_pre__ProcDef'
p27
aS'MT_pre__Trigger_T'
p28
aS'MT_pre__Model_T'
p29
a.""")
        self.vs[1]["mm__"] = """MT_pre__MetaModelElement_T"""
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
        self.vs[1]["GUID__"] = UUID('f7acf165-6f06-49bd-8c63-e3eb11f4ef7d')
        self.vs[2]["MT_pivotOut__"] = """element2"""
        self.vs[2]["MT_subtypeMatching__"] = True
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
        self.vs[2]["MT_pivotIn__"] = """element2"""
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__Name'
p2
aS'MT_pre__Module'
p3
aS'MT_pre__ConditionBranch'
p4
aS'MT_pre__Delay'
p5
aS'MT_pre__LocalDef'
p6
aS'MT_pre__Expr'
p7
aS'MT_pre__ConditionSet'
p8
aS'MT_pre__Proc'
p9
aS'MT_pre__MatchCase'
p10
aS'MT_pre__Match'
p11
aS'MT_pre__FuncDef'
p12
aS'MT_pre__Null'
p13
aS'MT_pre__Par'
p14
aS'MT_pre__Inst'
p15
aS'MT_pre__Listen'
p16
aS'MT_pre__Site'
p17
aS'MT_pre__New'
p18
aS'MT_pre__PythonRef'
p19
aS'MT_pre__Def'
p20
aS'MT_pre__Seq'
p21
aS'MT_pre__ParIndexed'
p22
aS'MT_pre__Condition'
p23
aS'MT_pre__Print'
p24
aS'MT_pre__Pattern'
p25
aS'MT_pre__ListenBranch'
p26
aS'MT_pre__ProcDef'
p27
aS'MT_pre__Trigger_T'
p28
aS'MT_pre__Model_T'
p29
a.""")
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_T"""
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
        self.vs[2]["GUID__"] = UUID('19825800-c90d-430d-b488-f6ecbb443867')
        self.vs[3]["MT_subtypeMatching__"] = True
        self.vs[3]["MT_pre__classtype"] = """
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
        self.vs[3]["MT_pre__cardinality"] = """
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
        self.vs[3]["MT_label__"] = """5"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__Name'
p2
aS'MT_pre__Module'
p3
aS'MT_pre__ConditionBranch'
p4
aS'MT_pre__Delay'
p5
aS'MT_pre__LocalDef'
p6
aS'MT_pre__Expr'
p7
aS'MT_pre__ConditionSet'
p8
aS'MT_pre__Proc'
p9
aS'MT_pre__MatchCase'
p10
aS'MT_pre__Match'
p11
aS'MT_pre__FuncDef'
p12
aS'MT_pre__Null'
p13
aS'MT_pre__Par'
p14
aS'MT_pre__Inst'
p15
aS'MT_pre__Listen'
p16
aS'MT_pre__Site'
p17
aS'MT_pre__New'
p18
aS'MT_pre__PythonRef'
p19
aS'MT_pre__Def'
p20
aS'MT_pre__Seq'
p21
aS'MT_pre__ParIndexed'
p22
aS'MT_pre__Condition'
p23
aS'MT_pre__Print'
p24
aS'MT_pre__Pattern'
p25
aS'MT_pre__ListenBranch'
p26
aS'MT_pre__ProcDef'
p27
aS'MT_pre__Trigger_T'
p28
aS'MT_pre__Model_T'
p29
a.""")
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__name"] = """
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
        self.vs[3]["GUID__"] = UUID('fa352ce0-c2e7-4ee2-af10-bb90957138c6')

    def eval_associationType9(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype3(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality3(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name3(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


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


    def eval_classtype5(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality5(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name5(self, attr_value, this):
        
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
        return True

