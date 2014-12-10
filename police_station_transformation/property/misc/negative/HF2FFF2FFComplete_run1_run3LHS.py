

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HF2FFF2FFComplete_run1_run3LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2FFF2FFComplete_run1_run3LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2FFF2FFComplete_run1_run3LHS, self).__init__(name='HF2FFF2FFComplete_run1_run3LHS', num_nodes=10, edges=[])
        
        # Add the edges
        self.add_edges([(4, 6), (7, 2), (7, 4), (8, 3), (8, 5), (5, 9), (2, 0), (3, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__SimpleDSLTransMM'
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
        self["GUID__"] = UUID('84b59523-8417-4abd-a18b-1b76e90ea8fd')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """if attr_value == 'female1':
    return True
else:
    return False
"""
        self.vs[0]["MT_label__"] = """15"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[0]["GUID__"] = UUID('b07de162-6b6c-4375-bd00-b666e866586c')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """if attr_value == 'female3':
    return True
else:
    return False
"""
        self.vs[1]["MT_label__"] = """18"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[1]["GUID__"] = UUID('b059e0d6-729e-4dab-b079-dd066474e51c')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """16"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__backward_link"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('9a12bff9-4506-406f-820c-efea24ad26f9')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """21"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__backward_link"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('929ed6f5-c1c8-4ef2-b453-dd0beba966e9')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_pre__associationType"] = """
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
        self.vs[4]["MT_label__"] = """17"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__directLink_T"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('1103316d-a806-4d33-bf10-ad8b4839b605')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_pre__associationType"] = """
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
        self.vs[5]["MT_label__"] = """22"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["mm__"] = """MT_pre__directLink_T"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('b4ba6855-08dd-417a-8790-a450f8fbd2b3')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_pre__classtype"] = """if attr_value == 'female1':
    return True
else:
    return False
"""
        self.vs[6]["MT_label__"] = """13"""
        self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[6]["mm__"] = """MT_pre__Female_T"""
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
        self.vs[6]["GUID__"] = UUID('b01afb63-8f9a-48ed-8534-cbf0da50bc5d')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_pre__classtype"] = """if attr_value == 'female1':
    return True
else:
    return False
"""
        self.vs[7]["MT_label__"] = """14"""
        self.vs[7]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[7]["mm__"] = """MT_pre__Female_T"""
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
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('32ad7274-023f-4602-a6aa-d8ad3421652f')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_pre__classtype"] = """if attr_value == 'female3':
    return True
else:
    return False
"""
        self.vs[8]["MT_label__"] = """19"""
        self.vs[8]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """MT_pre__Female_T"""
        self.vs[8]["MT_pre__name"] = """
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
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["GUID__"] = UUID('567c2a44-498f-4887-a640-44f6740a0f23')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_pre__classtype"] = """if attr_value == 'female3':
    return True
else:
    return False
"""
        self.vs[9]["MT_label__"] = """20"""
        self.vs[9]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[9]["mm__"] = """MT_pre__Female_T"""
        self.vs[9]["MT_pre__name"] = """
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
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["GUID__"] = UUID('f4357225-fb88-4b23-9547-016f71384f76')

    def eval_classtype13(self, attr_value, this):
        if attr_value == 'female1':
            return True
        else:
            return False


    def eval_name13(self, attr_value, this):
        
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
        if attr_value == 'female1':
            return True
        else:
            return False


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


    def eval_classtype19(self, attr_value, this):
        if attr_value == 'female3':
            return True
        else:
            return False


    def eval_name19(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype20(self, attr_value, this):
        if attr_value == 'female3':
            return True
        else:
            return False


    def eval_name20(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype15(self, attr_value, this):
        if attr_value == 'female1':
            return True
        else:
            return False


    def eval_name15(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype18(self, attr_value, this):
        if attr_value == 'female3':
            return True
        else:
            return False


    def eval_name18(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_associationType17(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_associationType22(self, attr_value, this):
        
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

