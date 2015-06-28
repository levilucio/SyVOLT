

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HFindTwoMatchElementsSameTypeDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFindTwoMatchElementsSameTypeDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFindTwoMatchElementsSameTypeDiffRulesLHS, self).__init__(name='HFindTwoMatchElementsSameTypeDiffRulesLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 2], [5, 1], [1, 3]])
        # Set the graph attributes
        self["GUID__"] = 4448450274503426919
        self["name"] = """"""
        self["MT_constraint__"] = """
guid1 = PreNode('1').index
guid2 = PreNode('2').index

matchModel1ID = PreNode('3').index
matchModel2ID = PreNode('4').index

if PreNode('1')['classtype'] == PreNode('2')['classtype'] and int(guid1) < int(guid2) and int(matchModel1ID) < int(matchModel2ID):
    return True
return False
"""
        self["mm__"] = ['MT_pre__FamiliesToPersons_MM', 'MoTifRule']
        
        # Set the node attributes
        self.vs[0]["GUID__"] = 7181928297639646230
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["mm__"] = """MT_pre__match_contains"""
        self.vs[1]["GUID__"] = 7943422122721247554
        self.vs[1]["MT_subtypes__"] = []
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["mm__"] = """MT_pre__match_contains"""
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
        self.vs[2]["GUID__"] = 2210858195324649237
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
        self.vs[2]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
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
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["MT_subtypeMatching__"] = True
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pivotOut__"] = """element1"""
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
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
        self.vs[3]["GUID__"] = 2056133774871146816
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
        self.vs[3]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
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
        self.vs[3]["MT_label__"] = """2"""
        self.vs[3]["MT_subtypeMatching__"] = True
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pivotOut__"] = """element2"""
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[4]["GUID__"] = 4699185555220633200
        self.vs[4]["MT_subtypes__"] = []
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["mm__"] = """MT_pre__MatchModel"""
        self.vs[5]["GUID__"] = 1687034107671583005
        self.vs[5]["MT_subtypes__"] = []
        self.vs[5]["MT_label__"] = """4"""
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["mm__"] = """MT_pre__MatchModel"""

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        
        guid1 = PreNode('1').index
        guid2 = PreNode('2').index
        
        matchModel1ID = PreNode('3').index
        matchModel2ID = PreNode('4').index
        
        if PreNode('1')['classtype'] == PreNode('2')['classtype'] and int(guid1) < int(guid2) and int(matchModel1ID) < int(matchModel2ID):
            return True
        return False

