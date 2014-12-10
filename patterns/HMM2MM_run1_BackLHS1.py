

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HMM2MM_run1_BackLHS1(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_run1_BackLHS1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_run1_BackLHS1, self).__init__(name='HMM2MM_run1_BackLHS1', num_nodes=8, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [7, 4], [4, 6], [2, 0], [1, 2], [1, 5], [5, 6]])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
        self["name"] = """HMM2MM_run1_BackLHS1"""
        self["GUID__"] = UUID('f1504fc7-832a-4a16-b1e6-11b9258bd15c')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[0]["GUID__"] = UUID('d901697f-6fad-44a3-8d71-84c87d32b59e')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["mm__"] = """MT_pre__MatchModel"""
        self.vs[1]["GUID__"] = UUID('068b2404-1ee1-412d-bbb7-bfba08b39924')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["mm__"] = """MT_pre__paired_with"""
        self.vs[2]["GUID__"] = UUID('3f358e4d-5084-4ada-abdb-89917071f706')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """6"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["mm__"] = """MT_pre__apply_contains"""
        self.vs[3]["GUID__"] = UUID('bcfed88b-ba64-4f30-8454-1a54fbf99dce')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """8"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["mm__"] = """MT_pre__trace_link"""
        self.vs[4]["GUID__"] = UUID('087da965-afcb-4e01-8ea9-2da6c14c8005')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """10"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["mm__"] = """MT_pre__match_contains"""
        self.vs[5]["GUID__"] = UUID('5d95b4ac-9eb1-449c-9fac-41fedfd7f6d1')
        self.vs[6]["MT_subtypeMatching__"] = False
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
        self.vs[6]["MT_label__"] = """12"""
        self.vs[6]["MT_subtypes__"] = """[]"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["mm__"] = """MT_pre__Male_S"""
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
        self.vs[6]["GUID__"] = UUID('e167e729-df2a-412c-a880-438eb4eb9ecb')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_pre__classtype"] = """
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
        self.vs[7]["MT_label__"] = """14"""
        self.vs[7]["MT_subtypes__"] = """[]"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["mm__"] = """MT_pre__Male_T"""
        self.vs[7]["MT_pre__name"] = """
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
        self.vs[7]["MT_pre__cardinality"] = """
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
        self.vs[7]["GUID__"] = UUID('cff6fd37-e196-41e3-9bbe-e8e9f3bd4ef9')

    def eval_classtype12(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name12(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality12(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality14(self, attr_value, this):
        
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
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================
        
        return True

