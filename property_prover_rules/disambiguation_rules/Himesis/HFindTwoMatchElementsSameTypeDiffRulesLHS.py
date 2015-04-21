

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HFindTwoMatchElementsSameTypeDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFindTwoMatchElementsSameTypeDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFindTwoMatchElementsSameTypeDiffRulesLHS, self).__init__(name='HFindTwoMatchElementsSameTypeDiffRulesLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 2), (5, 1), (1, 3)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__GM2AUTOSAR_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""Vguid1 = graph.vs[PreNode('1').index]['GUID__']\u000aguid2 = graph.vs[PreNode('2').index]['GUID__']        \u000a        \u000aif PreNode('1')['classtype'] == PreNode('2')['classtype'] and guid1.int < guid2.int:\u000a    return True\u000areturn False\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('ca93cc3b-3100-43d3-ac6f-4df37df7f38c')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__match_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('fc195a53-6e81-40ac-9978-a9d371455032')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__match_contains"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('93c83d64-cf77-43aa-b21a-e0a5abe16516')
        self.vs[2]["MT_pivotOut__"] = """element1"""
        self.vs[2]["MT_subtypeMatching__"] = True
        self.vs[2]["MT_pre__classtype"] = """
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
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__VirtualDevice'
p2
aS'MT_pre__Distributable'
p3
aS'MT_pre__ECU'
p4
aS'MT_pre__ExecFrame'
p5
aS'MT_pre__Signal'
p6
a.""")
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_dirty__"] = False
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
        self.vs[2]["GUID__"] = UUID('58ef2a69-c621-4a65-8850-cb4a2b10a8ca')
        self.vs[3]["MT_pivotOut__"] = """element2"""
        self.vs[3]["MT_subtypeMatching__"] = True
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
        self.vs[3]["MT_label__"] = """2"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__VirtualDevice'
p2
aS'MT_pre__Distributable'
p3
aS'MT_pre__ECU'
p4
aS'MT_pre__ExecFrame'
p5
aS'MT_pre__Signal'
p6
a.""")
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_dirty__"] = False
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
        self.vs[3]["GUID__"] = UUID('2fa1092b-2fa6-4931-b6a2-d7b15a804e3a')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__MatchModel"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('16ed4395-31e0-4bcc-a239-54710e2bb60f')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """4"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["mm__"] = """MT_pre__MatchModel"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('7576aed6-ae40-4119-835f-3893500a6aa8')

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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        guid1 = graph.vs[PreNode('1').index]['GUID__']
        guid2 = graph.vs[PreNode('2').index]['GUID__']        
                
        if PreNode('1')['classtype'] == PreNode('2')['classtype'] and guid1.int < guid2.int:
            return True
        return False

