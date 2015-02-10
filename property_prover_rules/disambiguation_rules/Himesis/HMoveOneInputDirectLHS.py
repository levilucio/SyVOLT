

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HMoveOneInputDirectLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneInputDirectLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneInputDirectLHS, self).__init__(name='HMoveOneInputDirectLHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[3, 0], [0, 2]])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__UMLRT2Kiltera_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """#if len([i for i in graph.neighbors(PreNode('5').index) if graph.vs[i]['mm__'] == 'match_contains']) == 0:
#    return True

#return False
return True
"""
        self["name"] = """"""
        self["GUID__"] = UUID('f5c6dd46-2004-46c0-a627-7ae6a11afe60')
        
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
        self.vs[0]["mm__"] = """MT_pre__directLink_S"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('62e44fa5-752e-4bec-af5b-2f478335a54f')
        self.vs[1]["MT_pivotOut__"] = """element1"""
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
        self.vs[1]["MT_pivotIn__"] = """element1"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__OPTIONAL1,'
p2
aS'MT_pre__PhysicalThread'
p3
aS'MT_pre__PortRef'
p4
aS'MT_pre__PackageContainer'
p5
aS'MT_pre__Thread'
p6
aS'MT_pre__OUT2'
p7
aS'MT_pre__BASE0'
p8
aS'MT_pre__NamedElement'
p9
aS'MT_pre__Element'
p10
aS'MT_pre__OUT1'
p11
aS'MT_pre__Signal'
p12
aS'MT_pre__Package'
p13
aS'MT_pre__PortType'
p14
aS'MT_pre__PortConnectorRef'
p15
aS'MT_pre__IN1'
p16
aS'MT_pre__IN0'
p17
aS'MT_pre__LogicalThread'
p18
aS'MT_pre__RoleType'
p19
aS'MT_pre__Vertex'
p20
aS'MT_pre__SIBLING0'
p21
aS'MT_pre__InitialPoint'
p22
aS'MT_pre__PortConnector'
p23
aS'MT_pre__SignalType'
p24
aS'MT_pre__Transition'
p25
aS'MT_pre__EntryPoint'
p26
aS'MT_pre__CONJUGATE1'
p27
aS'MT_pre__Protocol'
p28
aS'MT_pre__StateMachine'
p29
aS'MT_pre__Model_S'
p30
aS'MT_pre__StateMachineElement'
p31
aS'MT_pre__Port'
p32
aS'MT_pre__TransitionType'
p33
aS'MT_pre__Capsule'
p34
aS'MT_pre__Trigger_S'
p35
aS'MT_pre__State'
p36
aS'MT_pre__PLUGIN2'
p37
aS'MT_pre__Action'
p38
aS'MT_pre__CapsuleRole'
p39
aS'MT_pre__ExitPoint'
p40
aS'MT_pre__FIXED0'
p41
a.""")
        self.vs[1]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[1]["MT_dirty__"] = False
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
        self.vs[1]["GUID__"] = UUID('d240ebeb-6eff-4974-ac6c-298a543deb29')
        self.vs[2]["MT_pivotOut__"] = """element2"""
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
        self.vs[2]["MT_pivotIn__"] = """element2"""
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__OPTIONAL1,'
p2
aS'MT_pre__PhysicalThread'
p3
aS'MT_pre__PortRef'
p4
aS'MT_pre__PackageContainer'
p5
aS'MT_pre__Thread'
p6
aS'MT_pre__OUT2'
p7
aS'MT_pre__BASE0'
p8
aS'MT_pre__NamedElement'
p9
aS'MT_pre__Element'
p10
aS'MT_pre__OUT1'
p11
aS'MT_pre__Signal'
p12
aS'MT_pre__Package'
p13
aS'MT_pre__PortType'
p14
aS'MT_pre__PortConnectorRef'
p15
aS'MT_pre__IN1'
p16
aS'MT_pre__IN0'
p17
aS'MT_pre__LogicalThread'
p18
aS'MT_pre__RoleType'
p19
aS'MT_pre__Vertex'
p20
aS'MT_pre__SIBLING0'
p21
aS'MT_pre__InitialPoint'
p22
aS'MT_pre__PortConnector'
p23
aS'MT_pre__SignalType'
p24
aS'MT_pre__Transition'
p25
aS'MT_pre__EntryPoint'
p26
aS'MT_pre__CONJUGATE1'
p27
aS'MT_pre__Protocol'
p28
aS'MT_pre__StateMachine'
p29
aS'MT_pre__Model_S'
p30
aS'MT_pre__StateMachineElement'
p31
aS'MT_pre__Port'
p32
aS'MT_pre__TransitionType'
p33
aS'MT_pre__Capsule'
p34
aS'MT_pre__Trigger_S'
p35
aS'MT_pre__State'
p36
aS'MT_pre__PLUGIN2'
p37
aS'MT_pre__Action'
p38
aS'MT_pre__CapsuleRole'
p39
aS'MT_pre__ExitPoint'
p40
aS'MT_pre__FIXED0'
p41
a.""")
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
        self.vs[2]["GUID__"] = UUID('0ec6533f-2b98-445e-9e59-66d2a8b51aed')
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
        self.vs[3]["MT_label__"] = """5"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__OPTIONAL1,'
p2
aS'MT_pre__PhysicalThread'
p3
aS'MT_pre__PortRef'
p4
aS'MT_pre__PackageContainer'
p5
aS'MT_pre__Thread'
p6
aS'MT_pre__OUT2'
p7
aS'MT_pre__BASE0'
p8
aS'MT_pre__NamedElement'
p9
aS'MT_pre__Element'
p10
aS'MT_pre__OUT1'
p11
aS'MT_pre__Signal'
p12
aS'MT_pre__Package'
p13
aS'MT_pre__PortType'
p14
aS'MT_pre__PortConnectorRef'
p15
aS'MT_pre__IN1'
p16
aS'MT_pre__IN0'
p17
aS'MT_pre__LogicalThread'
p18
aS'MT_pre__RoleType'
p19
aS'MT_pre__Vertex'
p20
aS'MT_pre__SIBLING0'
p21
aS'MT_pre__InitialPoint'
p22
aS'MT_pre__PortConnector'
p23
aS'MT_pre__SignalType'
p24
aS'MT_pre__Transition'
p25
aS'MT_pre__EntryPoint'
p26
aS'MT_pre__CONJUGATE1'
p27
aS'MT_pre__Protocol'
p28
aS'MT_pre__StateMachine'
p29
aS'MT_pre__Model_S'
p30
aS'MT_pre__StateMachineElement'
p31
aS'MT_pre__Port'
p32
aS'MT_pre__TransitionType'
p33
aS'MT_pre__Capsule'
p34
aS'MT_pre__Trigger_S'
p35
aS'MT_pre__State'
p36
aS'MT_pre__PLUGIN2'
p37
aS'MT_pre__Action'
p38
aS'MT_pre__CapsuleRole'
p39
aS'MT_pre__ExitPoint'
p40
aS'MT_pre__FIXED0'
p41
a.""")
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
        self.vs[3]["GUID__"] = UUID('68cfe848-2516-4dd3-87fd-a30fc2221c7d')

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        #if len([i for i in graph.neighbors(PreNode('5').index) if graph.vs[i]['mm__'] == 'match_contains']) == 0:
        #    return True
        
        #return False
        return True

