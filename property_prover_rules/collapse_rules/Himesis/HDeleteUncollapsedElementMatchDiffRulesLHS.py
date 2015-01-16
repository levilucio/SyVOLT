

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HDeleteUncollapsedElementMatchDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDeleteUncollapsedElementMatchDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeleteUncollapsedElementMatchDiffRulesLHS, self).__init__(name='HDeleteUncollapsedElementMatchDiffRulesLHS', num_nodes=1, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""Vif len([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'match_contains']) == 0:\u000a    return True\u000a\u000areturn False\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('d18979c6-45ff-4440-adbf-0e3ea957224f')
        
        # Set the node attributes
        self.vs[0]["MT_pivotOut__"] = """element2"""
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
        self.vs[0]["MT_pivotIn__"] = """element2"""
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__Station_S'
p2
aS'MT_pre__Male_S'
p3
aS'MT_pre__Female_S'
p4
a.""")
        self.vs[0]["mm__"] = """MT_pre__MetaModelElement_S"""
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
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('6ba502a7-b818-43ff-9bdb-c46d1f0d1544')

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        if len([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'match_contains']) == 0:
            return True
        
        return False

