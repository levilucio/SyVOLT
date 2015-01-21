

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HFF2FF_Back_Complete_NACBridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_Back_Complete_NACBridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_Back_Complete_NACBridge, self).__init__(name='HFF2FF_Back_Complete_NACBridge', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[2, 0], [0, 4], [3, 1], [1, 5]])
        # Set the graph attributes
        self["GUID__"] = UUID('0f8453e9-3801-4c9c-8fee-957a6c768a6c')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """7"""
        self.vs[0]["mm__"] = """MT_pre__trace_link"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('5316299e-40dc-4425-b635-3f80f7d6cb6c')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """8"""
        self.vs[1]["mm__"] = """MT_pre__trace_link"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('c203a6ae-3708-4622-924a-27b7ad0efa18')
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
        self.vs[2]["MT_pre__associationType"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_associationType9(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType9(attr_value, this)"""
        self.vs[2]["MT_pre__classtype"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_classtype9(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype9(attr_value, this)"""
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
        self.vs[2]["MT_pre__name"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_name9(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name9(attr_value, this)"""
        self.vs[2]["MT_label__"] = """9"""
        self.vs[2]["mm__"] = """MT_pre__Female_T"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('b551e105-bfa3-415e-b3f0-814e5a3200af')
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
        self.vs[3]["MT_pre__associationType"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_associationType10(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType10(attr_value, this)"""
        self.vs[3]["MT_pre__classtype"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_classtype10(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype10(attr_value, this)"""
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
        self.vs[3]["MT_pre__name"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_name10(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name10(attr_value, this)"""
        self.vs[3]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_pre__Female_T"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('96c2fe7c-56ed-4001-a164-67d78b41caef')
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
        self.vs[4]["MT_pre__associationType"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_associationType11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType11(attr_value, this)"""
        self.vs[4]["MT_pre__classtype"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_classtype11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype11(attr_value, this)"""
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
        self.vs[4]["MT_pre__name"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_name11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name11(attr_value, this)"""
        self.vs[4]["MT_label__"] = """11"""
        self.vs[4]["mm__"] = """MT_pre__Female_S"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["MT_pre__cardinality"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_cardinality11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_cardinality11(attr_value, this)"""
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
        self.vs[4]["GUID__"] = UUID('06925961-9c12-4c77-aff3-8d837da79749')
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
        self.vs[5]["MT_pre__associationType"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_associationType12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType12(attr_value, this)"""
        self.vs[5]["MT_pre__classtype"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_classtype12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype12(attr_value, this)"""
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
        self.vs[5]["MT_pre__name"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_name12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name12(attr_value, this)"""
        self.vs[5]["MT_label__"] = """12"""
        self.vs[5]["mm__"] = """MT_pre__Female_S"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["MT_pre__cardinality"] = """from HFF2FF1 import HFF2FF1
from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
lhs = HFF2FF1()
return HFF2FF1().eval_cardinality12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_cardinality12(attr_value, this)"""
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
        self.vs[5]["GUID__"] = UUID('dc45b2e9-7e78-4c4f-987a-b4b491b553ad')

    def eval_associationType9(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_associationType9(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType9(attr_value, this)


    def eval_classtype9(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_classtype9(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype9(attr_value, this)


    def eval_name9(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_name9(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name9(attr_value, this)


    def eval_associationType10(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_associationType10(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType10(attr_value, this)


    def eval_classtype10(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_classtype10(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype10(attr_value, this)


    def eval_name10(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_name10(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name10(attr_value, this)


    def eval_associationType11(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_associationType11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType11(attr_value, this)


    def eval_classtype11(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_classtype11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype11(attr_value, this)


    def eval_name11(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_name11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name11(attr_value, this)


    def eval_cardinality11(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_cardinality11(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_cardinality11(attr_value, this)


    def eval_associationType12(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_associationType12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_associationType12(attr_value, this)


    def eval_classtype12(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_classtype12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_classtype12(attr_value, this)


    def eval_name12(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_name12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_name12(attr_value, this)


    def eval_cardinality12(self, attr_value, this):
        from HFF2FF1 import HFF2FF1
        from HFF2FF_Back_Complete_NAC import HFF2FF_Back_Complete_NAC
        lhs = HFF2FF1()
        return HFF2FF1().eval_cardinality12(attr_value, this) and HFF2FF_Back_Complete_NAC(lhs).eval_cardinality12(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

