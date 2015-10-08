

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HCommunityPerson2_CompleteLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HCommunityPerson2_CompleteLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCommunityPerson2_CompleteLHS, self).__init__(name='HCommunityPerson2_CompleteLHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([[3, 1], [4, 2], [0, 3], [0, 4]])
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
        self["name"] = """communityPerson2_Complete"""
        self["GUID__"] = 469007200485205499

        self["superclasses_dict"] = {"Man": ["Person"], "Woman": ["Person"]}
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__CommunityRoot"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 4377689463318154053
        self.vs[1]["MT_subtypeMatching__"] = True
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["mm__"] = """MT_pre__Person"""
        self.vs[1]["MT_subtypes__"] = ['MT_pre__Man', 'MT_pre__Woman']
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 3848934477262139697
        self.vs[2]["MT_subtypeMatching__"] = True
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["mm__"] = """MT_pre__Person"""
        self.vs[2]["MT_subtypes__"] = ['MT_pre__Man', 'MT_pre__Woman']
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = 2452608556256079194
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["mm__"] = """MT_pre__directLink_T"""
        self.vs[3]["MT_subtypes__"] = []
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = 158508756087999363
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["mm__"] = """MT_pre__directLink_T"""
        self.vs[4]["MT_subtypes__"] = []
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = 2725994969245625818

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


    def eval_classtype4(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


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


    def eval_associationType3(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_associationType5(self, attr_value, this):
        
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

