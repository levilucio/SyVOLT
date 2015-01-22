

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HMM2MM_Back_Complete_NACBridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_Back_Complete_NACBridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_Back_Complete_NACBridge, self).__init__(name='HMM2MM_Back_Complete_NACBridge', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[2, 0], [0, 4], [3, 1], [1, 5]])
        # Set the graph attributes
        self["GUID__"] = UUID('d9251ff6-3d80-4c3c-a9dd-d6117696ea4e')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """7"""
        self.vs[0]["mm__"] = """MT_pre__trace_link"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('d28b672d-f3f1-4c70-b8f5-d93f58504f85')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """8"""
        self.vs[1]["mm__"] = """MT_pre__trace_link"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('e23bfcac-3889-47e0-91d6-7066e2cbf489')
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
        self.vs[2]["MT_pre__associationType"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_associationType11(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType11(attr_value, this)"""
        self.vs[2]["MT_pre__classtype"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_classtype11(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype11(attr_value, this)"""
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
        self.vs[2]["MT_pre__name"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_name11(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name11(attr_value, this)"""
        self.vs[2]["MT_label__"] = """11"""
        self.vs[2]["mm__"] = """MT_pre__Male_T"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('fd66dac7-f7dc-4d4a-931e-179bfc0c3258')
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
        self.vs[3]["MT_pre__associationType"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_associationType12(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType12(attr_value, this)"""
        self.vs[3]["MT_pre__classtype"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_classtype12(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype12(attr_value, this)"""
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
        self.vs[3]["MT_pre__name"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_name12(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name12(attr_value, this)"""
        self.vs[3]["MT_label__"] = """12"""
        self.vs[3]["mm__"] = """MT_pre__Male_T"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('6b96e742-bf38-4372-93d7-5ac3f66d5e36')
        self.vs[4]["associationType"] = """
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
        self.vs[4]["MT_pre__associationType"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_associationType13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType13(attr_value, this)"""
        self.vs[4]["MT_pre__classtype"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_classtype13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype13(attr_value, this)"""
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
        self.vs[4]["MT_pre__name"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_name13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name13(attr_value, this)"""
        self.vs[4]["MT_label__"] = """13"""
        self.vs[4]["mm__"] = """MT_pre__Male_S"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["MT_pre__cardinality"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_cardinality13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_cardinality13(attr_value, this)"""
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
        self.vs[4]["GUID__"] = UUID('2727158b-89fb-427c-b1ca-a7c59f80a619')
        self.vs[5]["associationType"] = """
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
        self.vs[5]["MT_pre__associationType"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_associationType14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType14(attr_value, this)"""
        self.vs[5]["MT_pre__classtype"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_classtype14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype14(attr_value, this)"""
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
        self.vs[5]["MT_pre__name"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_name14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name14(attr_value, this)"""
        self.vs[5]["MT_label__"] = """14"""
        self.vs[5]["mm__"] = """MT_pre__Male_S"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["MT_pre__cardinality"] = """from HMM2MM1 import HMM2MM1
from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
lhs = HMM2MM1()
return HMM2MM1().eval_cardinality14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_cardinality14(attr_value, this)"""
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
        self.vs[5]["GUID__"] = UUID('fbc2425d-334b-4336-bd4a-03007f4d5848')

    def eval_associationType11(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_associationType11(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType11(attr_value, this)


    def eval_classtype11(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_classtype11(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype11(attr_value, this)


    def eval_name11(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_name11(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name11(attr_value, this)


    def eval_associationType12(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_associationType12(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType12(attr_value, this)


    def eval_classtype12(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_classtype12(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype12(attr_value, this)


    def eval_name12(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_name12(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name12(attr_value, this)


    def eval_associationType13(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_associationType13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType13(attr_value, this)


    def eval_classtype13(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_classtype13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype13(attr_value, this)


    def eval_name13(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_name13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name13(attr_value, this)


    def eval_cardinality13(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_cardinality13(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_cardinality13(attr_value, this)


    def eval_associationType14(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_associationType14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_associationType14(attr_value, this)


    def eval_classtype14(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_classtype14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_classtype14(attr_value, this)


    def eval_name14(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_name14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_name14(attr_value, this)


    def eval_cardinality14(self, attr_value, this):
        from HMM2MM1 import HMM2MM1
        from HMM2MM_Back_Complete_NAC import HMM2MM_Back_Complete_NAC
        lhs = HMM2MM1()
        return HMM2MM1().eval_cardinality14(attr_value, this) and HMM2MM_Back_Complete_NAC(lhs).eval_cardinality14(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

