

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HFSMConnected_run4LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFSMConnected_run4LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFSMConnected_run4LHS, self).__init__(name='HFSMConnected_run4LHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(0, 3), (0, 4), (4, 1), (3, 2)])
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
        self["name"] = """"""
        self["GUID__"] = UUID('99211cef-9a62-481a-94ab-f3b4763160ac')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
        self.vs[0]["MT_pre__cardinality"] = """
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
        self.vs[0]["GUID__"] = UUID('8f5742dd-77d4-4c43-a40f-9ad7afcef679')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["mm__"] = """MT_pre__Male_S"""
        self.vs[1]["MT_pre__cardinality"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
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
        self.vs[1]["GUID__"] = UUID('2d1fa988-1bb4-48f5-9a4c-82169f6d0cec')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[2]["GUID__"] = UUID('5e4d3c4f-74ca-47d5-b861-6a1cda2f0f36')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('36bff613-288b-49c4-8083-2e2a237b80b9')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('1935967a-7547-4f42-a4ab-9f3a6ee9b9f7')

    def eval_classtype1(self, attr_value, this):
        if attr_value == 'station4':
            return True
        else:
            return False


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


    def eval_classtype2(self, attr_value, this):
        if attr_value == 'male4':
            return True
        else:
            return False


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


    def eval_classtype3(self, attr_value, this):
        if attr_value == 'female4':
            return True
        else:
            return False


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
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================
        
        return True

