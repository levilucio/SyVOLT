

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HMM2MMBackComplete_run4LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MMBackComplete_run4LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MMBackComplete_run4LHS, self).__init__(name='HMM2MMBackComplete_run4LHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(5, 1), (1, 3), (6, 2), (2, 4), (3, 0), (0, 4)])
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
        self["name"] = """SM2SM_run4"""
        self["GUID__"] = UUID('2ad97f11-56e4-47df-8143-e792ddb0302f')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """12"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('fa76885b-a517-4cb8-bb8c-1e5787e54752')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """13"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__trace_link"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('d00b00a6-cd89-4fc3-b5f7-59f0cee5fef1')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """14"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__trace_link"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('170e3d99-e06c-4073-8efc-8e1060fc9eae')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
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
        self.vs[3]["MT_label__"] = """8"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__Male_S"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__cardinality"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[3]["GUID__"] = UUID('ca3f72dc-2e52-4a37-89e0-8496e8dba9a6')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
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
        self.vs[4]["MT_label__"] = """9"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__Male_S"""
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
        self.vs[4]["GUID__"] = UUID('86d6ec71-4848-48ac-a382-f1e098d79434')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
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
        self.vs[5]["MT_label__"] = """10"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["mm__"] = """MT_pre__Male_T"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('3008aa66-ccdb-42fc-8df7-77bd09130dbb')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male4':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
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
        self.vs[6]["MT_label__"] = """11"""
        self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[6]["mm__"] = """MT_pre__Male_T"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('b7ae3897-1ae1-424a-b9bb-af7ff2d5f17a')

    def eval_classtype8(self, attr_value, this):
        if attr_value == 'male4':
            return True
        else:
            return False


    def eval_name8(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality8(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype9(self, attr_value, this):
        if attr_value == 'male4':
            return True
        else:
            return False


    def eval_name9(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality9(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype10(self, attr_value, this):
        if attr_value == 'male4':
            return True
        else:
            return False


    def eval_name10(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype11(self, attr_value, this):
        if attr_value == 'male4':
            return True
        else:
            return False


    def eval_name11(self, attr_value, this):
        
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

