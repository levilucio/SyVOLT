

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HBuildTraceabilityForRuleLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBuildTraceabilityForRuleLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBuildTraceabilityForRuleLHS, self).__init__(name='HBuildTraceabilityForRuleLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[3, 0], [0, 4], [1, 2], [2, 5]])
        # Set the graph attributes
        self["mm__"] = ['MT_pre__FamiliesToPersons_MM', 'MoTifRule']
        self["MT_constraint__"] = """if set([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'trace_link'])) == set():
    return True

return False
"""
        self["name"] = """"""
        self["GUID__"] = 1339043830988334966
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """6"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["mm__"] = """MT_pre__apply_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 6601769124712063922
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["MT_subtypes__"] = []
        self.vs[1]["mm__"] = """MT_pre__MatchModel"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 3211031155982416150
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["MT_subtypes__"] = []
        self.vs[2]["mm__"] = """MT_pre__match_contains"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = 3676593120352744638
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["MT_subtypes__"] = []
        self.vs[3]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = 3729121856167067283
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
        self.vs[4]["MT_label__"] = """2"""
        self.vs[4]["MT_subtypes__"] = ['MT_pre__CommunityRoot', 'MT_pre__Person', 'MT_pre__Man', 'MT_pre__Woman']
        self.vs[4]["mm__"] = """MT_pre__MetaModelElement_T"""
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
        self.vs[4]["GUID__"] = 925503974014884163
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
        self.vs[5]["MT_label__"] = """1"""
        self.vs[5]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[5]["mm__"] = """MT_pre__MetaModelElement_S"""
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
        self.vs[5]["GUID__"] = 9053659576832917539

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        if set([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'trace_link'])) == set():
            return True
        
        return False

