

from core.himesis import Himesis, HimesisPreConditionPatternLHS

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
        self["mm__"] = ['MT_pre__FamiliesToPersons_MM', 'MoTifRule']
        self["MT_constraint__"] = """return True
"""
        self["superclasses_dict"] = {'Woman': ['MetaModelElement_T'], 'HouseholdRoot': ['MetaModelElement_S'], 'Family': ['MetaModelElement_S'], 'Member': ['MetaModelElement_S'], 'Person': ['MetaModelElement_T'], 'CommunityRoot': ['MetaModelElement_T'], 'Man': ['MetaModelElement_T']}
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
        self.vs[1]["MT_pivotIn__"] = """element1"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[1]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[1]["MT_dirty__"] = False
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
        self.vs[1]["GUID__"] = 7905240522204529542
        self.vs[2]["MT_pivotOut__"] = """element2"""
        self.vs[2]["MT_subtypeMatching__"] = True
        self.vs[2]["MT_pivotIn__"] = """element2"""
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[2]["MT_dirty__"] = False
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
        self.vs[2]["GUID__"] = 9211260118570632643
        self.vs[3]["MT_subtypeMatching__"] = True
        self.vs[3]["MT_label__"] = """5"""
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
        self.vs[3]["GUID__"] = 3372597496876460092

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

