

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HSM2SM_Back_Complete_NACBridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_Back_Complete_NACBridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_Back_Complete_NACBridge, self).__init__(name='HSM2SM_Back_Complete_NACBridge', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[1, 4], [4, 0], [2, 5], [5, 3]])
        # Set the graph attributes
        self["GUID__"] = UUID('9efcdb21-a966-4628-ad3b-47b5a85da033')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """
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
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["name"] = """
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
        self.vs[0]["MT_pre__associationType"] = """
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
        self.vs[0]["MT_pre__classtype"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_classtype4(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype4(attr_value, this)"""
        self.vs[0]["classtype"] = """
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
        self.vs[0]["MT_pre__name"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_name4(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name4(attr_value, this)"""
        self.vs[0]["MT_label__"] = """4"""
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_pre__cardinality"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_cardinality4(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality4(attr_value, this)"""
        self.vs[0]["cardinality"] = """
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
        self.vs[0]["GUID__"] = UUID('1eb29cc0-6f72-4fbd-b452-b1992a41f473')
        self.vs[1]["associationType"] = """
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
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["name"] = """
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
        self.vs[1]["MT_pre__associationType"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_associationType5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_associationType5(attr_value, this)"""
        self.vs[1]["MT_pre__classtype"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_classtype5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype5(attr_value, this)"""
        self.vs[1]["classtype"] = """
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
        self.vs[1]["MT_pre__name"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_name5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name5(attr_value, this)"""
        self.vs[1]["MT_label__"] = """5"""
        self.vs[1]["mm__"] = """MT_pre__Station_T"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_pre__cardinality"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_cardinality5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality5(attr_value, this)"""
        self.vs[1]["cardinality"] = """
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
        self.vs[1]["GUID__"] = UUID('269ae635-3c89-4bf7-8d0f-8f75c71893e0')
        self.vs[2]["associationType"] = """
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
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["name"] = """
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
        self.vs[2]["MT_pre__associationType"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_associationType6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_associationType6(attr_value, this)"""
        self.vs[2]["MT_pre__classtype"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_classtype6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype6(attr_value, this)"""
        self.vs[2]["classtype"] = """
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
        self.vs[2]["MT_pre__name"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_name6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name6(attr_value, this)"""
        self.vs[2]["MT_label__"] = """6"""
        self.vs[2]["mm__"] = """MT_pre__Male_T"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_pre__cardinality"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_cardinality6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality6(attr_value, this)"""
        self.vs[2]["cardinality"] = """
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
        self.vs[2]["GUID__"] = UUID('8861e26f-a52d-4731-ab78-b2d1de7e7020')
        self.vs[3]["associationType"] = """
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
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["name"] = """
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
        self.vs[3]["MT_pre__associationType"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_associationType8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_associationType8(attr_value, this)"""
        self.vs[3]["MT_pre__classtype"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_classtype8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype8(attr_value, this)"""
        self.vs[3]["classtype"] = """
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
        self.vs[3]["MT_pre__name"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_name8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name8(attr_value, this)"""
        self.vs[3]["MT_label__"] = """8"""
        self.vs[3]["mm__"] = """MT_pre__Male_S"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_pre__cardinality"] = """from HSM2SM1 import HSM2SM1
from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
lhs = HSM2SM1()
return HSM2SM1().eval_cardinality8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality8(attr_value, this)"""
        self.vs[3]["cardinality"] = """
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
        self.vs[3]["GUID__"] = UUID('e7e201bc-0566-49ad-be9a-3258fc2f2b01')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["name"] = """
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
        self.vs[4]["classtype"] = """
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
        self.vs[4]["MT_label__"] = """11"""
        self.vs[4]["mm__"] = """MT_pre__trace_link"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["cardinality"] = """
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
        self.vs[4]["GUID__"] = UUID('d7c197b3-4bca-4aa7-ad07-f2871a497999')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["name"] = """
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
        self.vs[5]["classtype"] = """
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
        self.vs[5]["MT_label__"] = """12"""
        self.vs[5]["mm__"] = """MT_pre__trace_link"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["cardinality"] = """
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
        self.vs[5]["GUID__"] = UUID('49384bb0-96aa-4187-ae2b-8a79a5bb538f')

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


    def eval_classtype4(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_classtype4(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype4(attr_value, this)


    def eval_name4(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_name4(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name4(attr_value, this)


    def eval_cardinality4(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_cardinality4(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality4(attr_value, this)


    def eval_associationType5(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_associationType5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_associationType5(attr_value, this)


    def eval_classtype5(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_classtype5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype5(attr_value, this)


    def eval_name5(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_name5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name5(attr_value, this)


    def eval_cardinality5(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_cardinality5(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality5(attr_value, this)


    def eval_associationType6(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_associationType6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_associationType6(attr_value, this)


    def eval_classtype6(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_classtype6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype6(attr_value, this)


    def eval_name6(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_name6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name6(attr_value, this)


    def eval_cardinality6(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_cardinality6(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality6(attr_value, this)


    def eval_associationType8(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_associationType8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_associationType8(attr_value, this)


    def eval_classtype8(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_classtype8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_classtype8(attr_value, this)


    def eval_name8(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_name8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_name8(attr_value, this)


    def eval_cardinality8(self, attr_value, this):
        from HSM2SM1 import HSM2SM1
        from HSM2SM_Back_Complete_NAC import HSM2SM_Back_Complete_NAC
        lhs = HSM2SM1()
        return HSM2SM1().eval_cardinality8(attr_value, this) and HSM2SM_Back_Complete_NAC(lhs).eval_cardinality8(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

