

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HMoveOneOutputIndirectLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneOutputIndirectLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneOutputIndirectLHS, self).__init__(name='HMoveOneOutputIndirectLHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[2, 0], [0, 3]])
        # Set the graph attributes
        self["mm__"] = ['MT_pre__UMLRT2Kiltera_MM', 'MoTifRule']
        self["MT_constraint__"] = """return True
"""
        self["name"] = """"""
        self["GUID__"] = 7548956408462458992
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """6"""
        self.vs[0]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 4824434143394378845
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
        self.vs[1]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[1]["MT_subtypes__"] = ['MT_pre__OPTIONAL1,', 'MT_pre__PhysicalThread', 'MT_pre__PortRef', 'MT_pre__PackageContainer', 'MT_pre__Thread', 'MT_pre__OUT2', 'MT_pre__BASE0', 'MT_pre__NamedElement', 'MT_pre__Element', 'MT_pre__OUT1', 'MT_pre__Signal', 'MT_pre__Package', 'MT_pre__PortType', 'MT_pre__PortConnectorRef', 'MT_pre__IN1', 'MT_pre__IN0', 'MT_pre__LogicalThread', 'MT_pre__RoleType', 'MT_pre__Vertex', 'MT_pre__SIBLING0', 'MT_pre__InitialPoint', 'MT_pre__PortConnector', 'MT_pre__SignalType', 'MT_pre__Transition', 'MT_pre__EntryPoint', 'MT_pre__CONJUGATE1', 'MT_pre__Protocol', 'MT_pre__StateMachine', 'MT_pre__Model_S', 'MT_pre__StateMachineElement', 'MT_pre__Port', 'MT_pre__TransitionType', 'MT_pre__Capsule', 'MT_pre__Trigger_S', 'MT_pre__State', 'MT_pre__PLUGIN2', 'MT_pre__Action', 'MT_pre__CapsuleRole', 'MT_pre__ExitPoint', 'MT_pre__FIXED0']
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
        self.vs[1]["GUID__"] = 7905240522204529542
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
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_subtypes__"] = ['MT_pre__OPTIONAL1,', 'MT_pre__PhysicalThread', 'MT_pre__PortRef', 'MT_pre__PackageContainer', 'MT_pre__Thread', 'MT_pre__OUT2', 'MT_pre__BASE0', 'MT_pre__NamedElement', 'MT_pre__Element', 'MT_pre__OUT1', 'MT_pre__Signal', 'MT_pre__Package', 'MT_pre__PortType', 'MT_pre__PortConnectorRef', 'MT_pre__IN1', 'MT_pre__IN0', 'MT_pre__LogicalThread', 'MT_pre__RoleType', 'MT_pre__Vertex', 'MT_pre__SIBLING0', 'MT_pre__InitialPoint', 'MT_pre__PortConnector', 'MT_pre__SignalType', 'MT_pre__Transition', 'MT_pre__EntryPoint', 'MT_pre__CONJUGATE1', 'MT_pre__Protocol', 'MT_pre__StateMachine', 'MT_pre__Model_S', 'MT_pre__StateMachineElement', 'MT_pre__Port', 'MT_pre__TransitionType', 'MT_pre__Capsule', 'MT_pre__Trigger_S', 'MT_pre__State', 'MT_pre__PLUGIN2', 'MT_pre__Action', 'MT_pre__CapsuleRole', 'MT_pre__ExitPoint', 'MT_pre__FIXED0']
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
        self.vs[2]["GUID__"] = 9211260118570632643
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
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_subtypes__"] = ['MT_pre__OPTIONAL1,', 'MT_pre__PhysicalThread', 'MT_pre__PortRef', 'MT_pre__PackageContainer', 'MT_pre__Thread', 'MT_pre__OUT2', 'MT_pre__BASE0', 'MT_pre__NamedElement', 'MT_pre__Element', 'MT_pre__OUT1', 'MT_pre__Signal', 'MT_pre__Package', 'MT_pre__PortType', 'MT_pre__PortConnectorRef', 'MT_pre__IN1', 'MT_pre__IN0', 'MT_pre__LogicalThread', 'MT_pre__RoleType', 'MT_pre__Vertex', 'MT_pre__SIBLING0', 'MT_pre__InitialPoint', 'MT_pre__PortConnector', 'MT_pre__SignalType', 'MT_pre__Transition', 'MT_pre__EntryPoint', 'MT_pre__CONJUGATE1', 'MT_pre__Protocol', 'MT_pre__StateMachine', 'MT_pre__Model_S', 'MT_pre__StateMachineElement', 'MT_pre__Port', 'MT_pre__TransitionType', 'MT_pre__Capsule', 'MT_pre__Trigger_S', 'MT_pre__State', 'MT_pre__PLUGIN2', 'MT_pre__Action', 'MT_pre__CapsuleRole', 'MT_pre__ExitPoint', 'MT_pre__FIXED0']
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
        self.vs[3]["GUID__"] = 3372597496876460092

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

