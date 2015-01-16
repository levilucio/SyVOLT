

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HDeleteUncollapsedElementApplyDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDeleteUncollapsedElementApplyDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeleteUncollapsedElementApplyDiffRulesLHS, self).__init__(name='HDeleteUncollapsedElementApplyDiffRulesLHS', num_nodes=1, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """if len([i for i in graph.neighbors(PreNode('3').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
    return True

return False
"""
        self["name"] = """"""
        self["GUID__"] = UUID('9fcc1d05-6dcc-4182-8a48-506d3c9113ec')
        
        # Set the node attributes
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
        self.vs[0]["MT_label__"] = """3"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__Station_T'
p2
aS'MT_pre__Male_T'
p3
aS'MT_pre__Female_T'
p4
a.""")
        self.vs[0]["mm__"] = """MT_pre__MetaModelElement_T"""
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
        self.vs[0]["GUID__"] = UUID('662f567b-0d9a-437e-b707-ab1716c20491')

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        if len([i for i in graph.neighbors(PreNode('3').index) if graph.vs[i]['mm__'] == 'apply_contains']) == 0:
            return True
        
        return False

