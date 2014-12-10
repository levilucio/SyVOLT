

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HECUVDDistConnectedLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HECUVDDistConnectedLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HECUVDDistConnectedLHS, self).__init__(name='HECUVDDistConnectedLHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (2, 3), (3, 1), (1, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__GM2AUTOSAR_MM'
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
        self["GUID__"] = UUID('6b7df65e-3a34-49f5-ad10-8981922e4f9f')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[0]["MT_label__"] = """3"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__Distributable"""
        self.vs[0]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('8053f181-d0fe-4f02-8baa-3d1df579c51c')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__VirtualDevice"""
        self.vs[1]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('4ca69a0c-33ae-44b6-92ed-e9f8233efb4f')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__ECU"""
        self.vs[2]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('d28cf946-6b80-485b-817e-7ae4b09d43c5')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_pre__associationType"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__directLink_S"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('9945ad05-6ed2-46e7-872c-161c255a7681')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_pre__associationType"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = """MT_pre__directLink_S"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('f4ab9920-721b-44b7-af8f-9b111aa019e7')

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


    def eval_associationType4(self, attr_value, this):
        
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

