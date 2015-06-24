

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HDeleteUncollapsedElementLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDeleteUncollapsedElementLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeleteUncollapsedElementLHS, self).__init__(name='HDeleteUncollapsedElementLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 3], [5, 1], [1, 2]])
        # Set the graph attributes
        self["mm__"] = ['MT_pre__UMLRT2Kiltera_MM', 'MoTifRule']
        self["MT_constraint__"] = """return True"""
        self["name"] = """"""
        self["GUID__"] = 8606295276883309858
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["mm__"] = """MT_pre__match_contains"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 2492652436716073316
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["mm__"] = """MT_pre__match_contains"""
        self.vs[1]["MT_subtypes__"] = []
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 1356976907983983460
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
        self.vs[2]["MT_label__"] = """2"""
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
        self.vs[2]["GUID__"] = 5061772226935437731
        self.vs[3]["MT_pivotOut__"] = """element1"""
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
        self.vs[3]["MT_pivotIn__"] = """element1"""
        self.vs[3]["MT_label__"] = """1"""
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
        self.vs[3]["GUID__"] = 6670895658872261885
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["mm__"] = """MT_pre__MatchModel"""
        self.vs[4]["MT_subtypes__"] = []
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = 2929545596509939901
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """4"""
        self.vs[5]["mm__"] = """MT_pre__MatchModel"""
        self.vs[5]["MT_subtypes__"] = []
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = 589586432928941143

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

