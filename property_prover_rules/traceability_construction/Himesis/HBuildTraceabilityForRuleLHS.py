

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

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
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__S_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """#if (len([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'backward_link']) == 0) and (len([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'backward_link']) == 0):
#    return True

#return False
return True
"""
        self["name"] = """"""
        self["GUID__"] = 484876223850229858
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """6"""
        self.vs[0]["mm__"] = """MT_pre__apply_contains"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 7683400890172826658
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["mm__"] = """MT_pre__MatchModel"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 710661300048255922
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["mm__"] = """MT_pre__match_contains"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = 8745918043301311226
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = 2420179630685827351
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
        self.vs[4]["MT_label__"] = """2"""
        self.vs[4]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__ERModel'
p2
aS'MT_pre__EntityType'
p3
aS'MT_pre__Feature'
p4
aS'MT_pre__ERAttribute'
p5
aS'MT_pre__WeakReference'
p6
aS'MT_pre__StrongReference'
p7
aS'MT_pre__NamedElement'
p8
aS'MT_pre__Reference'
p9
a.""")
        self.vs[4]["MT_dirty__"] = False
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
        self.vs[4]["GUID__"] = 4034251042489893101
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
        self.vs[5]["MT_label__"] = """1"""
        self.vs[5]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__ERModel'
p2
aS'MT_pre__EntityType'
p3
aS'MT_pre__Feature'
p4
aS'MT_pre__ERAttribute'
p5
aS'MT_pre__WeakReference'
p6
aS'MT_pre__StrongReference'
p7
aS'MT_pre__NamedElement'
p8
aS'MT_pre__Reference'
p9
a.""")
        self.vs[5]["MT_dirty__"] = False
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
        self.vs[5]["GUID__"] = 2437348352955640125

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
        #if (len([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'backward_link']) == 0) and (len([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'backward_link']) == 0):
        #    return True
        
        #return False
        return True

