

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HReconnectApplyElementsLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HReconnectApplyElementsLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HReconnectApplyElementsLHS, self).__init__(name='HReconnectApplyElementsLHS', num_nodes=2, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__UMLRT2Kiltera_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """if len([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
    return True

return False
"""
        self["name"] = """"""
        self["GUID__"] = UUID('2836f807-76f0-4504-bb77-0224deecf2b6')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = True
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
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
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
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('c9dace57-af66-4fef-ab7a-effdbf32a44b')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('67e3d1e8-f626-45de-9da2-6b8eaec0dd90')

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        if len([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
            return True
        
        return False

