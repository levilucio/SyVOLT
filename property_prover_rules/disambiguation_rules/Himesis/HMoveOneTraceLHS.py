

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HMoveOneTraceLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneTraceLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneTraceLHS, self).__init__(name='HMoveOneTraceLHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[0, 1], [1, 3]])
        # Set the graph attributes
        self["mm__"] = ['MT_pre__UMLRT2Kiltera_MM', 'MoTifRule']
        self["MT_constraint__"] = """#if len([i for i in graph.neighbors(PreNode('9').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
#    return True

#return False
return True
"""
        self["name"] = """"""
        self["GUID__"] = 1380157641660176096
        
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
        self.vs[0]["MT_label__"] = """9"""
        self.vs[0]["MT_subtypes__"] = ['MT_pre__Name', 'MT_pre__Module', 'MT_pre__ConditionBranch', 'MT_pre__Delay', 'MT_pre__LocalDef', 'MT_pre__Expr', 'MT_pre__ConditionSet', 'MT_pre__Proc', 'MT_pre__MatchCase', 'MT_pre__Match', 'MT_pre__FuncDef', 'MT_pre__Null', 'MT_pre__Par', 'MT_pre__Inst', 'MT_pre__Listen', 'MT_pre__Site', 'MT_pre__New', 'MT_pre__PythonRef', 'MT_pre__Def', 'MT_pre__Seq', 'MT_pre__ParIndexed', 'MT_pre__Condition', 'MT_pre__Print', 'MT_pre__Pattern', 'MT_pre__ListenBranch', 'MT_pre__ProcDef', 'MT_pre__Trigger_T', 'MT_pre__Model_T']
        self.vs[0]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[0]["MT_dirty__"] = False
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
        self.vs[0]["GUID__"] = 2331649011858856719
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """10"""
        self.vs[1]["MT_subtypes__"] = []
        self.vs[1]["mm__"] = """MT_pre__trace_link"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 643142311743453749
        self.vs[2]["MT_pivotOut__"] = """element1"""
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
        self.vs[2]["MT_pivotIn__"] = """element1"""
        self.vs[2]["MT_label__"] = """7"""
        self.vs[2]["MT_subtypes__"] = ['MT_pre__OPTIONAL1,', 'MT_pre__PhysicalThread', 'MT_pre__PortRef', 'MT_pre__PackageContainer', 'MT_pre__Thread', 'MT_pre__OUT2', 'MT_pre__BASE0', 'MT_pre__NamedElement', 'MT_pre__Element', 'MT_pre__OUT1', 'MT_pre__Signal', 'MT_pre__Package', 'MT_pre__PortType', 'MT_pre__PortConnectorRef', 'MT_pre__IN1', 'MT_pre__IN0', 'MT_pre__LogicalThread', 'MT_pre__RoleType', 'MT_pre__Vertex', 'MT_pre__SIBLING0', 'MT_pre__InitialPoint', 'MT_pre__PortConnector', 'MT_pre__SignalType', 'MT_pre__Transition', 'MT_pre__EntryPoint', 'MT_pre__CONJUGATE1', 'MT_pre__Protocol', 'MT_pre__StateMachine', 'MT_pre__Model_S', 'MT_pre__StateMachineElement', 'MT_pre__Port', 'MT_pre__TransitionType', 'MT_pre__Capsule', 'MT_pre__Trigger_S', 'MT_pre__State', 'MT_pre__PLUGIN2', 'MT_pre__Action', 'MT_pre__CapsuleRole', 'MT_pre__ExitPoint', 'MT_pre__FIXED0']
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_dirty__"] = False
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
        self.vs[2]["GUID__"] = 8612786979184624768
        self.vs[3]["MT_pivotOut__"] = """element2"""
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
        self.vs[3]["MT_pivotIn__"] = """element2"""
        self.vs[3]["MT_label__"] = """8"""
        self.vs[3]["MT_subtypes__"] = ['MT_pre__OPTIONAL1,', 'MT_pre__PhysicalThread', 'MT_pre__PortRef', 'MT_pre__PackageContainer', 'MT_pre__Thread', 'MT_pre__OUT2', 'MT_pre__BASE0', 'MT_pre__NamedElement', 'MT_pre__Element', 'MT_pre__OUT1', 'MT_pre__Signal', 'MT_pre__Package', 'MT_pre__PortType', 'MT_pre__PortConnectorRef', 'MT_pre__IN1', 'MT_pre__IN0', 'MT_pre__LogicalThread', 'MT_pre__RoleType', 'MT_pre__Vertex', 'MT_pre__SIBLING0', 'MT_pre__InitialPoint', 'MT_pre__PortConnector', 'MT_pre__SignalType', 'MT_pre__Transition', 'MT_pre__EntryPoint', 'MT_pre__CONJUGATE1', 'MT_pre__Protocol', 'MT_pre__StateMachine', 'MT_pre__Model_S', 'MT_pre__StateMachineElement', 'MT_pre__Port', 'MT_pre__TransitionType', 'MT_pre__Capsule', 'MT_pre__Trigger_S', 'MT_pre__State', 'MT_pre__PLUGIN2', 'MT_pre__Action', 'MT_pre__CapsuleRole', 'MT_pre__ExitPoint', 'MT_pre__FIXED0']
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_dirty__"] = False
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
        self.vs[3]["GUID__"] = 1749774053392192765

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


    def eval_classtype7(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name7(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality7(self, attr_value, this):
        
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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        #if len([i for i in graph.neighbors(PreNode('9').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
        #    return True
        
        #return False
        return True

