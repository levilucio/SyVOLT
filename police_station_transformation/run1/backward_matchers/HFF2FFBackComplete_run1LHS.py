

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HFF2FFBackComplete_run1LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FFBackComplete_run1LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FFBackComplete_run1LHS, self).__init__(name='HFF2FFBackComplete_run1LHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 3), (2, 4), (3, 5), (4, 6), (5, 0), (0, 6)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""V#===============================================================================\u000a# This code is executed after the nodes in the LHS have been matched.\u000a# You can access a matched node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# The given constraint must evaluate to a boolean expression:\u000a#    returning True enables the rule to be applied,\u000a#    returning False forbids the rule from being applied.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self["name"] = """FF2FFBackComplete_run1"""
        self["GUID__"] = UUID('85437239-b9e7-4acc-85fd-f913560df741')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('f5769530-eb57-4ea0-a954-cabe210c7e19')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__Female_T"""
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
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('017381d1-036c-46d0-b853-e442a7ad8071')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__Female_T"""
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
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('ad5a4ef8-ebb4-4950-927b-c7f81b4f6fb3')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """6"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__trace_link"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('4e469486-7d80-44d0-b326-9c4ea2177b18')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """7"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__trace_link"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('460a2ca9-1a90-446e-a646-ccc8c276d891')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[5]["MT_label__"] = """1"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('bf4c4a9b-3c10-40c3-9ba6-97289082a3f4')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[6]["MT_label__"] = """2"""
        self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[6]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('9b203afe-7539-441b-aeed-d16bcd700233')

    def eval_classtype3(self, attr_value, this):
        if attr_value == 'female1':
            return True
        else:
            return False


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


    def eval_classtype4(self, attr_value, this):
        if attr_value == 'female1':
            return True
        else:
            return False


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


    def eval_classtype1(self, attr_value, this):
        if attr_value == 'female1':
            return True
        else:
            return False


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
        if attr_value == 'female1':
            return True
        else:
            return False


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
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================
        
        return True

