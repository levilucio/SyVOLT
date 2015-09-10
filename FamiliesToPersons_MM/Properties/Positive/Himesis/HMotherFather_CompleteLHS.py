

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HMotherFather_CompleteLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMotherFather_CompleteLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMotherFather_CompleteLHS, self).__init__(name='HMotherFather_CompleteLHS', num_nodes=33, edges=[])
        
        # Add the edges
        self.add_edges([[5, 24], [24, 28], [6, 25], [25, 29], [21, 28], [22, 29], [23, 30], [26, 30], [27, 30], [8, 31], [9, 31], [7, 32], [16, 32], [13, 0], [0, 8], [5, 26], [6, 27], [14, 1], [1, 7], [19, 21], [20, 22], [3, 23], [15, 5], [10, 6], [17, 9], [18, 10], [3, 11], [11, 20], [3, 12], [12, 19], [4, 2], [2, 3], [4, 13], [4, 14], [17, 15], [18, 16]])
        # Set the graph attributes
        self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
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
        self["GUID__"] = 7389341872482026452
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
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
        self.vs[0]["MT_label__"] = """11"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["mm__"] = """MT_pre__Man"""
        self.vs[0]["MT_dirty__"] = False
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
        self.vs[0]["GUID__"] = 926940418889901561
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """
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
        self.vs[1]["MT_label__"] = """13"""
        self.vs[1]["MT_subtypes__"] = []
        self.vs[1]["mm__"] = """MT_pre__Woman"""
        self.vs[1]["MT_dirty__"] = False
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
        self.vs[1]["GUID__"] = 2414569509321020864
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """19"""
        self.vs[2]["MT_subtypes__"] = []
        self.vs[2]["mm__"] = """MT_pre__trace_link"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = 7700259157212242351
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_pre__classtype"] = """
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
        self.vs[3]["MT_pre__cardinality"] = """
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
        self.vs[3]["MT_label__"] = """1"""
        self.vs[3]["MT_subtypes__"] = []
        self.vs[3]["mm__"] = """MT_pre__Family"""
        self.vs[3]["MT_dirty__"] = False
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
        self.vs[3]["GUID__"] = 2256222547494689065
        self.vs[4]["MT_subtypeMatching__"] = False
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
        self.vs[4]["MT_label__"] = """10"""
        self.vs[4]["MT_subtypes__"] = []
        self.vs[4]["mm__"] = """MT_pre__CommunityRoot"""
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
        self.vs[4]["GUID__"] = 898718170124738917
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """31"""
        self.vs[5]["MT_subtypes__"] = []
        self.vs[5]["mm__"] = """MT_pre__Concat"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = 443676638319066350
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """37"""
        self.vs[6]["MT_subtypes__"] = []
        self.vs[6]["mm__"] = """MT_pre__Concat"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = 4802453329047950267
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """28"""
        self.vs[7]["MT_subtypes__"] = []
        self.vs[7]["mm__"] = """MT_pre__hasAttr_T"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = 8861416761195245127
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """29"""
        self.vs[8]["MT_subtypes__"] = []
        self.vs[8]["mm__"] = """MT_pre__hasAttr_T"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["GUID__"] = 7939025907981755168
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """34"""
        self.vs[9]["MT_subtypes__"] = []
        self.vs[9]["mm__"] = """MT_pre__leftExpr"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["GUID__"] = 9189914318218483465
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_label__"] = """40"""
        self.vs[10]["MT_subtypes__"] = []
        self.vs[10]["mm__"] = """MT_pre__leftExpr"""
        self.vs[10]["MT_dirty__"] = False
        self.vs[10]["GUID__"] = 8672149789714037589
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "father"
"""
        self.vs[11]["MT_label__"] = """6"""
        self.vs[11]["MT_subtypes__"] = []
        self.vs[11]["mm__"] = """MT_pre__directLink_S"""
        self.vs[11]["MT_dirty__"] = False
        self.vs[11]["GUID__"] = 8320280580379178625
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "mother"
"""
        self.vs[12]["MT_label__"] = """7"""
        self.vs[12]["MT_subtypes__"] = []
        self.vs[12]["mm__"] = """MT_pre__directLink_S"""
        self.vs[12]["MT_dirty__"] = False
        self.vs[12]["GUID__"] = 3756221911521386939
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_pre__associationType"] = """
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
        self.vs[13]["MT_label__"] = """15"""
        self.vs[13]["MT_subtypes__"] = []
        self.vs[13]["mm__"] = """MT_pre__directLink_T"""
        self.vs[13]["MT_dirty__"] = False
        self.vs[13]["GUID__"] = 5225249046947265698
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_pre__associationType"] = """
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
        self.vs[14]["MT_label__"] = """18"""
        self.vs[14]["MT_subtypes__"] = []
        self.vs[14]["mm__"] = """MT_pre__directLink_T"""
        self.vs[14]["MT_dirty__"] = False
        self.vs[14]["GUID__"] = 8577281087428490400
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_label__"] = """35"""
        self.vs[15]["MT_subtypes__"] = []
        self.vs[15]["mm__"] = """MT_pre__rightExpr"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["GUID__"] = 7332625405621498123
        self.vs[16]["MT_subtypeMatching__"] = False
        self.vs[16]["MT_label__"] = """41"""
        self.vs[16]["MT_subtypes__"] = []
        self.vs[16]["mm__"] = """MT_pre__rightExpr"""
        self.vs[16]["MT_dirty__"] = False
        self.vs[16]["GUID__"] = 7961413822898766442
        self.vs[17]["MT_subtypeMatching__"] = False
        self.vs[17]["MT_label__"] = """30"""
        self.vs[17]["MT_subtypes__"] = []
        self.vs[17]["mm__"] = """MT_pre__Equation"""
        self.vs[17]["MT_dirty__"] = False
        self.vs[17]["GUID__"] = 8145297662657875172
        self.vs[18]["MT_subtypeMatching__"] = False
        self.vs[18]["MT_label__"] = """36"""
        self.vs[18]["MT_subtypes__"] = []
        self.vs[18]["mm__"] = """MT_pre__Equation"""
        self.vs[18]["MT_dirty__"] = False
        self.vs[18]["GUID__"] = 1767786765784260856
        self.vs[19]["MT_subtypeMatching__"] = False
        self.vs[19]["MT_pre__classtype"] = """
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
        self.vs[19]["MT_pre__cardinality"] = """
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
        self.vs[19]["MT_label__"] = """2"""
        self.vs[19]["MT_subtypes__"] = []
        self.vs[19]["mm__"] = """MT_pre__Member"""
        self.vs[19]["MT_dirty__"] = False
        self.vs[19]["MT_pre__name"] = """
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
        self.vs[19]["GUID__"] = 4608252762783205864
        self.vs[20]["MT_subtypeMatching__"] = False
        self.vs[20]["MT_pre__classtype"] = """
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
        self.vs[20]["MT_pre__cardinality"] = """
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
        self.vs[20]["MT_label__"] = """3"""
        self.vs[20]["MT_subtypes__"] = []
        self.vs[20]["mm__"] = """MT_pre__Member"""
        self.vs[20]["MT_dirty__"] = False
        self.vs[20]["MT_pre__name"] = """
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
        self.vs[20]["GUID__"] = 6980603574434230158
        self.vs[21]["MT_subtypeMatching__"] = False
        self.vs[21]["MT_label__"] = """22"""
        self.vs[21]["MT_subtypes__"] = []
        self.vs[21]["mm__"] = """MT_pre__hasAttr_S"""
        self.vs[21]["MT_dirty__"] = False
        self.vs[21]["GUID__"] = 7435751106484361824
        self.vs[22]["MT_subtypeMatching__"] = False
        self.vs[22]["MT_label__"] = """23"""
        self.vs[22]["MT_subtypes__"] = []
        self.vs[22]["mm__"] = """MT_pre__hasAttr_S"""
        self.vs[22]["MT_dirty__"] = False
        self.vs[22]["GUID__"] = 4173173038484739860
        self.vs[23]["MT_subtypeMatching__"] = False
        self.vs[23]["MT_label__"] = """25"""
        self.vs[23]["MT_subtypes__"] = []
        self.vs[23]["mm__"] = """MT_pre__hasAttr_S"""
        self.vs[23]["MT_dirty__"] = False
        self.vs[23]["GUID__"] = 2807351762383669826
        self.vs[24]["MT_subtypeMatching__"] = False
        self.vs[24]["MT_label__"] = """32"""
        self.vs[24]["MT_subtypes__"] = []
        self.vs[24]["mm__"] = """MT_pre__hasArgs"""
        self.vs[24]["MT_dirty__"] = False
        self.vs[24]["GUID__"] = 973590460174805350
        self.vs[25]["MT_subtypeMatching__"] = False
        self.vs[25]["MT_label__"] = """38"""
        self.vs[25]["MT_subtypes__"] = []
        self.vs[25]["mm__"] = """MT_pre__hasArgs"""
        self.vs[25]["MT_dirty__"] = False
        self.vs[25]["GUID__"] = 4726168784904521304
        self.vs[26]["MT_subtypeMatching__"] = False
        self.vs[26]["MT_label__"] = """33"""
        self.vs[26]["MT_subtypes__"] = []
        self.vs[26]["mm__"] = """MT_pre__hasArgs"""
        self.vs[26]["MT_dirty__"] = False
        self.vs[26]["GUID__"] = 5308599370429996109
        self.vs[27]["MT_subtypeMatching__"] = False
        self.vs[27]["MT_label__"] = """39"""
        self.vs[27]["MT_subtypes__"] = []
        self.vs[27]["mm__"] = """MT_pre__hasArgs"""
        self.vs[27]["MT_dirty__"] = False
        self.vs[27]["GUID__"] = 3901464584395442071
        self.vs[28]["MT_subtypeMatching__"] = False
        self.vs[28]["MT_label__"] = """20"""
        self.vs[28]["MT_subtypes__"] = []
        self.vs[28]["mm__"] = """MT_pre__Attribute"""
        self.vs[28]["MT_dirty__"] = False
        self.vs[28]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[28]["GUID__"] = 4572183557874896960
        self.vs[29]["MT_subtypeMatching__"] = False
        self.vs[29]["MT_label__"] = """21"""
        self.vs[29]["MT_subtypes__"] = []
        self.vs[29]["mm__"] = """MT_pre__Attribute"""
        self.vs[29]["MT_dirty__"] = False
        self.vs[29]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[29]["GUID__"] = 1066252096431534413
        self.vs[30]["MT_subtypeMatching__"] = False
        self.vs[30]["MT_label__"] = """24"""
        self.vs[30]["MT_subtypes__"] = []
        self.vs[30]["mm__"] = """MT_pre__Attribute"""
        self.vs[30]["MT_dirty__"] = False
        self.vs[30]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[30]["GUID__"] = 5030082477268639940
        self.vs[31]["MT_subtypeMatching__"] = False
        self.vs[31]["MT_label__"] = """26"""
        self.vs[31]["MT_subtypes__"] = []
        self.vs[31]["mm__"] = """MT_pre__Attribute"""
        self.vs[31]["MT_dirty__"] = False
        self.vs[31]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[31]["GUID__"] = 6142088400733944397
        self.vs[32]["MT_subtypeMatching__"] = False
        self.vs[32]["MT_label__"] = """27"""
        self.vs[32]["MT_subtypes__"] = []
        self.vs[32]["mm__"] = """MT_pre__Attribute"""
        self.vs[32]["MT_dirty__"] = False
        self.vs[32]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "name"
"""
        self.vs[32]["GUID__"] = 8761939429606486324

    def eval_classtype11(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


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


    def eval_classtype13(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


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


    def eval_classtype10(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


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


    def eval_associationType6(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "father"


    def eval_associationType7(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "mother"


    def eval_associationType15(self, attr_value, this):
        
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


    def eval_name20(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name21(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name24(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name26(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


    def eval_name27(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return attr_value == "name"


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

