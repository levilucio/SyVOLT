

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HMoveOneInputIndirectLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneInputIndirectLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneInputIndirectLHS, self).__init__(name='HMoveOneInputIndirectLHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[3, 0], [0, 2]])
        # Set the graph attributes
        self["superclasses_dict"] = {'Community': ['MetaModelElement_T'], 'Parent': ['Member', 'MetaModelElement_S'], 'TownHall': ['MetaModelElement_T', 'NamedElement'], 'Facility': ['MetaModelElement_T', 'NamedElement'], 'SpecialFacility': ['MetaModelElement_T', 'NamedElement', 'Facility'], 'NamedElement': ['MetaModelElement_T', 'MetaModelElement_S'], 'Association': ['MetaModelElement_T', 'NamedElement'], 'Neighborhood': ['MetaModelElement_S'], 'District': ['MetaModelElement_T', 'NamedElement'], 'Committee': ['MetaModelElement_T', 'NamedElement'], 'Company': ['MetaModelElement_S'], 'City': ['MetaModelElement_S'], 'Service': ['MetaModelElement_S'], 'Man': ['Person', 'MetaModelElement_T'], 'Person': ['MetaModelElement_T'], 'Country': ['MetaModelElement_S'], 'Member': ['MetaModelElement_S'], 'Woman': ['Person', 'MetaModelElement_T'], 'Child': ['Member', 'MetaModelElement_S'], 'School': ['MetaModelElement_S'], 'OrdinaryFacility': ['MetaModelElement_T', 'NamedElement', 'Facility'], 'Family': ['MetaModelElement_S']}
        self["MT_constraint__"] = """return True
"""
        self["mm__"] = ['MT_pre__FamiliesToPersons_MM', 'MoTifRule']
        self["GUID__"] = 2571202128803664489
        self["name"] = """"""
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["GUID__"] = 6979274713714056209
        self.vs[0]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[1]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pivotOut__"] = """element1"""
        self.vs[1]["MT_pre__attr1"] = """
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
        self.vs[1]["GUID__"] = 3108459865723258324
        self.vs[1]["MT_pivotIn__"] = """element1"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pivotOut__"] = """element2"""
        self.vs[2]["MT_pre__attr1"] = """
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
        self.vs[2]["GUID__"] = 5100965010689216645
        self.vs[2]["MT_pivotIn__"] = """element2"""
        self.vs[2]["MT_label__"] = """4"""
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__attr1"] = """
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
        self.vs[3]["GUID__"] = 3713177797973397163
        self.vs[3]["MT_label__"] = """5"""

    def eval_attr13(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_attr14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_attr15(self, attr_value, this):
        
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

