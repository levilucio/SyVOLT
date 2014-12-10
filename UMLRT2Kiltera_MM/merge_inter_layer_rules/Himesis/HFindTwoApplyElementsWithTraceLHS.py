

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HFindTwoApplyElementsWithTraceLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFindTwoApplyElementsWithTraceLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFindTwoApplyElementsWithTraceLHS, self).__init__(name='HFindTwoApplyElementsWithTraceLHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(3, 0), (0, 5), (6, 1), (1, 4), (5, 2), (2, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__GM2AUTOSAR_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """if PreNode('4')['classtype'] == PreNode('3')['classtype']:
    if len([i for i in graph.neighbors(PreNode('4').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
    	return True

return False
"""
        self["name"] = """"""
        self["GUID__"] = UUID('02cd9831-fcc7-4958-9de6-3053378bf1c6')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """10"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__apply_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('119659ed-dfaa-4d7c-99e0-46613f599969')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__type"] = """
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
        self.vs[1]["MT_label__"] = """12"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__backward_link"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('5c3a2b43-0013-4803-b4b3-836c1e4ce7fb')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """11"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__trace_link"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('d8fb8a92-95ff-4430-89e7-2065538da51b')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """1"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('d6405da9-989d-41f9-8fb6-d06bfe674080')
        self.vs[4]["MT_subtypeMatching__"] = True
        self.vs[4]["MT_pre__classtype"] = """
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
        self.vs[4]["MT_pre__name"] = """
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
        self.vs[4]["MT_pivotIn__"] = """element1"""
        self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__VirtualDevice'
p2
aS'MT_pre__Distributable'
p3
aS'MT_pre__Signal'
p4
aS'MT_pre__ExecFrame'
p5
aS'MT_pre__ECU'
p6
a.""")
        self.vs[4]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["MT_pre__cardinality"] = """
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
        self.vs[4]["GUID__"] = UUID('090c34e2-8e32-4255-acd6-0b50a42b7ff0')
        self.vs[5]["MT_pivotOut__"] = """element1"""
        self.vs[5]["MT_subtypeMatching__"] = True
        self.vs[5]["MT_pre__classtype"] = """
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
        self.vs[5]["MT_pre__name"] = """
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
        self.vs[5]["MT_label__"] = """3"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__EcuInstance'
p2
aS'MT_pre__System'
p3
aS'MT_pre__SystemMapping'
p4
aS'MT_pre__ComponentPrototype'
p5
aS'MT_pre__SwCompToEcuMapping_component'
p6
aS'MT_pre__CompositionType'
p7
aS'MT_pre__PPortPrototype'
p8
aS'MT_pre__SwcToEcuMapping'
p9
aS'MT_pre__SoftwareComposition'
p10
aS'MT_pre__RPortPrototype'
p11
aS'MT_pre__PortPrototype'
p12
aS'MT_pre__ComponentType'
p13
a.""")
        self.vs[5]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["MT_pre__cardinality"] = """
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
        self.vs[5]["GUID__"] = UUID('a219eb52-212c-4e1e-a21f-08509bdfa3dc')
        self.vs[6]["MT_pivotOut__"] = """element2"""
        self.vs[6]["MT_subtypeMatching__"] = True
        self.vs[6]["MT_pre__classtype"] = """
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
        self.vs[6]["MT_pre__name"] = """
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
        self.vs[6]["MT_label__"] = """4"""
        self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__EcuInstance'
p2
aS'MT_pre__System'
p3
aS'MT_pre__SystemMapping'
p4
aS'MT_pre__ComponentPrototype'
p5
aS'MT_pre__SwCompToEcuMapping_component'
p6
aS'MT_pre__CompositionType'
p7
aS'MT_pre__PPortPrototype'
p8
aS'MT_pre__SwcToEcuMapping'
p9
aS'MT_pre__SoftwareComposition'
p10
aS'MT_pre__RPortPrototype'
p11
aS'MT_pre__PortPrototype'
p12
aS'MT_pre__ComponentType'
p13
a.""")
        self.vs[6]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["MT_pre__cardinality"] = """
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
        self.vs[6]["GUID__"] = UUID('b8c48f5b-5f5f-4b0b-95ee-03bfdc065909')

    def eval_type12(self, attr_value, this):
        
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
        if PreNode('4')['classtype'] == PreNode('3')['classtype']:
            if len([i for i in graph.neighbors(PreNode('4').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
            	return True
        
        return False

