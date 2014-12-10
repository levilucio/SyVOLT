

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HFSMFSMComplete_run1_run3LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFSMFSMComplete_run1_run3LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFSMFSMComplete_run1_run3LHS, self).__init__(name='HFSMFSMComplete_run1_run3LHS', num_nodes=26, edges=[])
        
        # Add the edges
        self.add_edges([(21, 0), (0, 12), (0, 13), (24, 1), (1, 14), (1, 15), (17, 2), (2, 23), (19, 3), (3, 22), (13, 4), (22, 4), (15, 5), (23, 5), (12, 8), (14, 9), (6, 20), (20, 8), (10, 21), (11, 24), (7, 25), (25, 9), (11, 16), (16, 7), (11, 17), (10, 18), (18, 6), (10, 19)])
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
        self["GUID__"] = UUID('6548bc7e-01e2-4d9c-95ea-b4b1e393481d')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
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
        self.vs[0]["GUID__"] = UUID('6bfe10f1-80df-4927-b63b-206516fa7cc4')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station3':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__Station_S"""
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
        self.vs[1]["GUID__"] = UUID('f1edb3de-23e8-4a89-9a0e-cb32638c96a4')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male3':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[2]["MT_label__"] = """11"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__Male_T"""
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
        self.vs[2]["GUID__"] = UUID('c0ff6ebe-1d06-46c4-8c18-232f14980f05')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[3]["MT_label__"] = """12"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__Male_T"""
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
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('990f05f7-cc18-4f15-b7c0-c0922efb162e')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__Male_S"""
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
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('691a9503-704a-4e48-9920-244cf897d9d6')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'male3':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[5]["MT_label__"] = """5"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["mm__"] = """MT_pre__Male_S"""
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
        self.vs[5]["GUID__"] = UUID('a9b360f4-730b-4ee5-bf27-3b07320cad8c')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[6]["MT_label__"] = """15"""
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
        self.vs[6]["GUID__"] = UUID('60049ef0-1ec0-456f-920d-b5e941159899')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female3':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[7]["MT_label__"] = """16"""
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
        self.vs[7]["GUID__"] = UUID('f21adb70-4eca-4649-959b-14bbae9b93db')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[8]["MT_label__"] = """2"""
        self.vs[8]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[8]["GUID__"] = UUID('fe6242e0-5f3e-48fb-94cb-226b284a1b38')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'female3':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[9]["MT_label__"] = """4"""
        self.vs[9]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[9]["mm__"] = """MT_pre__Female_S"""
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
        self.vs[9]["GUID__"] = UUID('432777f8-e98e-4652-977b-4e7d7a9b3a77')
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station1':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[10]["MT_label__"] = """13"""
        self.vs[10]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[10]["mm__"] = """MT_pre__Station_T"""
        self.vs[10]["MT_pre__name"] = """
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
        self.vs[10]["MT_dirty__"] = False
        self.vs[10]["GUID__"] = UUID('9bb4d2ed-b84e-4779-a3ab-f2f35b262e39')
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station3':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[11]["MT_label__"] = """14"""
        self.vs[11]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[11]["mm__"] = """MT_pre__Station_T"""
        self.vs[11]["MT_pre__name"] = """
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
        self.vs[11]["MT_dirty__"] = False
        self.vs[11]["GUID__"] = UUID('d269e05f-da45-4e25-94bc-207424777005')
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_label__"] = """7"""
        self.vs[12]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[12]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[12]["MT_dirty__"] = False
        self.vs[12]["GUID__"] = UUID('34abdb80-18da-4619-8864-e75fb3f319d3')
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_label__"] = """8"""
        self.vs[13]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[13]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[13]["MT_dirty__"] = False
        self.vs[13]["GUID__"] = UUID('2aa332c7-483d-403d-9f33-d78b8e19cd08')
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_label__"] = """9"""
        self.vs[14]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[14]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[14]["MT_dirty__"] = False
        self.vs[14]["GUID__"] = UUID('66a078b3-d85d-411d-be2e-07aa25368190')
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_label__"] = """10"""
        self.vs[15]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[15]["mm__"] = """MT_pre__indirectLink_S"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["GUID__"] = UUID('46c74b59-8389-4a94-8b39-38122dff0c72')
        self.vs[16]["MT_subtypeMatching__"] = False
        self.vs[16]["MT_pre__associationType"] = """
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
        self.vs[16]["MT_label__"] = """17"""
        self.vs[16]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[16]["mm__"] = """MT_pre__directLink_T"""
        self.vs[16]["MT_dirty__"] = False
        self.vs[16]["GUID__"] = UUID('cb79de6d-cce2-48f1-b1bc-1e1221c21c34')
        self.vs[17]["MT_subtypeMatching__"] = False
        self.vs[17]["MT_pre__associationType"] = """
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
        self.vs[17]["MT_label__"] = """18"""
        self.vs[17]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[17]["mm__"] = """MT_pre__directLink_T"""
        self.vs[17]["MT_dirty__"] = False
        self.vs[17]["GUID__"] = UUID('9d73eceb-6fd0-4288-a961-4361274a0536')
        self.vs[18]["MT_subtypeMatching__"] = False
        self.vs[18]["MT_pre__associationType"] = """
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
        self.vs[18]["MT_label__"] = """19"""
        self.vs[18]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[18]["mm__"] = """MT_pre__directLink_T"""
        self.vs[18]["MT_dirty__"] = False
        self.vs[18]["GUID__"] = UUID('4bddf5be-7ef2-4e19-865a-a41d81fb36ab')
        self.vs[19]["MT_subtypeMatching__"] = False
        self.vs[19]["MT_pre__associationType"] = """
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
        self.vs[19]["MT_label__"] = """20"""
        self.vs[19]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[19]["mm__"] = """MT_pre__directLink_T"""
        self.vs[19]["MT_dirty__"] = False
        self.vs[19]["GUID__"] = UUID('c5984331-ad1a-451b-bfe5-49ccd9026876')
        self.vs[20]["MT_subtypeMatching__"] = False
        self.vs[20]["MT_label__"] = """21"""
        self.vs[20]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[20]["mm__"] = """MT_pre__backward_link"""
        self.vs[20]["MT_dirty__"] = False
        self.vs[20]["GUID__"] = UUID('96c6804e-da73-4913-a237-a903be954b26')
        self.vs[21]["MT_subtypeMatching__"] = False
        self.vs[21]["MT_label__"] = """22"""
        self.vs[21]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[21]["mm__"] = """MT_pre__backward_link"""
        self.vs[21]["MT_dirty__"] = False
        self.vs[21]["GUID__"] = UUID('399f6736-ec6a-4a4f-9a42-50659a2025ee')
        self.vs[22]["MT_subtypeMatching__"] = False
        self.vs[22]["MT_label__"] = """23"""
        self.vs[22]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[22]["mm__"] = """MT_pre__backward_link"""
        self.vs[22]["MT_dirty__"] = False
        self.vs[22]["GUID__"] = UUID('4eaa80cb-81d7-4b1a-ab5c-47ab3094f7bb')
        self.vs[23]["MT_subtypeMatching__"] = False
        self.vs[23]["MT_label__"] = """24"""
        self.vs[23]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[23]["mm__"] = """MT_pre__backward_link"""
        self.vs[23]["MT_dirty__"] = False
        self.vs[23]["GUID__"] = UUID('f4592a49-ef4e-4cf7-84ba-398ee6b6607d')
        self.vs[24]["MT_subtypeMatching__"] = False
        self.vs[24]["MT_label__"] = """25"""
        self.vs[24]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[24]["mm__"] = """MT_pre__backward_link"""
        self.vs[24]["MT_dirty__"] = False
        self.vs[24]["GUID__"] = UUID('36b52071-31cc-4678-81d4-4852afdbfa7d')
        self.vs[25]["MT_subtypeMatching__"] = False
        self.vs[25]["MT_label__"] = """26"""
        self.vs[25]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[25]["mm__"] = """MT_pre__backward_link"""
        self.vs[25]["MT_dirty__"] = False
        self.vs[25]["GUID__"] = UUID('08f1ef33-0e12-4db6-b29d-2d9465e74a70')

    def eval_classtype1(self, attr_value, this):
        if attr_value == 'station1':
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


    def eval_classtype6(self, attr_value, this):
        if attr_value == 'station3':
            return True
        else:
            return False


    def eval_name6(self, attr_value, this):
        
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
        if attr_value == 'male3':
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


    def eval_classtype12(self, attr_value, this):
        if attr_value == 'male1':
            return True
        else:
            return False


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


    def eval_classtype3(self, attr_value, this):
        if attr_value == 'male1':
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


    def eval_classtype5(self, attr_value, this):
        if attr_value == 'male3':
            return True
        else:
            return False


    def eval_name5(self, attr_value, this):
        
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


    def eval_associationType18(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_associationType19(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_associationType20(self, attr_value, this):
        
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


    def eval_classtype16(self, attr_value, this):
        if attr_value == 'female3':
            return True
        else:
            return False


    def eval_name16(self, attr_value, this):
        
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


    def eval_classtype4(self, attr_value, this):
        if attr_value == 'female3':
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


    def eval_classtype13(self, attr_value, this):
        if attr_value == 'station1':
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
        if attr_value == 'station3':
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

