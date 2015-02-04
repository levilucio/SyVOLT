

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NACBridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NACBridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NACBridge, self).__init__(name='HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NACBridge', num_nodes=16, edges=[])
        
        # Add the edges
        self.add_edges([[2, 0], [8, 6], [6, 12], [9, 7], [7, 13], [1, 5], [5, 15], [1, 3], [2, 4], [4, 14], [3, 2], [8, 10], [9, 11], [10, 14], [11, 15]])
        # Set the graph attributes
        self["GUID__"] = UUID('891dbee7-6fac-4c70-a40b-3e49d66396fe')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
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
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["mm__"] = """MT_pre__directLink_S"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('178dd6db-65cb-41a2-8ddb-d76300cc3c9a')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_classtype2(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_classtype2(attr_value, this)"""
        self.vs[1]["MT_pre__cardinality"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_cardinality2(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_cardinality2(attr_value, this)"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["mm__"] = """MT_pre__LocalDef"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name2(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name2(attr_value, this)"""
        self.vs[1]["GUID__"] = UUID('201aa44d-31b2-4134-861b-14fe9bb34e26')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_classtype3(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_classtype3(attr_value, this)"""
        self.vs[2]["MT_pre__cardinality"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_cardinality3(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_cardinality3(attr_value, this)"""
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["mm__"] = """MT_pre__State"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name3(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name3(attr_value, this)"""
        self.vs[2]["GUID__"] = UUID('efd74ade-6037-4638-bd4a-de435dbe54c4')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """11"""
        self.vs[3]["mm__"] = """MT_pre__trace_link"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('f13854ac-a020-4a4d-871c-dc4ff41a39cd')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """17"""
        self.vs[4]["mm__"] = """MT_pre__hasAttribute_S"""
        self.vs[4]["MT_subtypes__"] = """[]"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('5e990411-f302-49df-8fe5-75288db1b610')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """26"""
        self.vs[5]["mm__"] = """MT_pre__hasAttribute_T"""
        self.vs[5]["MT_subtypes__"] = """[]"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('3db00686-02d1-4a98-9118-b001a4ca675c')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """33"""
        self.vs[6]["mm__"] = """MT_pre__rightExpr"""
        self.vs[6]["MT_subtypes__"] = """[]"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('4c95e20c-f99d-498c-a3dc-123e9a0aea94')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """37"""
        self.vs[7]["mm__"] = """MT_pre__rightExpr"""
        self.vs[7]["MT_subtypes__"] = """[]"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('a9f0f38f-6c94-41fb-a9bc-e9b8c5f69e4b')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """39"""
        self.vs[8]["mm__"] = """MT_pre__Equation"""
        self.vs[8]["MT_subtypes__"] = """[]"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name39(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name39(attr_value, this)"""
        self.vs[8]["GUID__"] = UUID('7819f088-2be0-4123-a985-35617370f148')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """43"""
        self.vs[9]["mm__"] = """MT_pre__Equation"""
        self.vs[9]["MT_subtypes__"] = """[]"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name43(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name43(attr_value, this)"""
        self.vs[9]["GUID__"] = UUID('a76f034a-7a66-48ab-96cf-e679592051fc')
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_label__"] = """45"""
        self.vs[10]["mm__"] = """MT_pre__leftExpr"""
        self.vs[10]["MT_subtypes__"] = """[]"""
        self.vs[10]["MT_dirty__"] = False
        self.vs[10]["GUID__"] = UUID('ec133653-a79d-419e-9c58-248e8ae585ee')
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_label__"] = """49"""
        self.vs[11]["mm__"] = """MT_pre__leftExpr"""
        self.vs[11]["MT_subtypes__"] = """[]"""
        self.vs[11]["MT_dirty__"] = False
        self.vs[11]["GUID__"] = UUID('e80f429c-ff6f-41fb-8171-dbad28d4a1c0')
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_pre__Type"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type51(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type51(attr_value, this)"""
        self.vs[12]["MT_label__"] = """51"""
        self.vs[12]["mm__"] = """MT_pre__Constant"""
        self.vs[12]["MT_subtypes__"] = """[]"""
        self.vs[12]["MT_dirty__"] = False
        self.vs[12]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name51(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name51(attr_value, this)"""
        self.vs[12]["GUID__"] = UUID('513d8641-37e8-40af-b9f8-5e006b5ec6b4')
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_pre__Type"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type55(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type55(attr_value, this)"""
        self.vs[13]["MT_label__"] = """55"""
        self.vs[13]["mm__"] = """MT_pre__Constant"""
        self.vs[13]["MT_subtypes__"] = """[]"""
        self.vs[13]["MT_dirty__"] = False
        self.vs[13]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name55(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name55(attr_value, this)"""
        self.vs[13]["GUID__"] = UUID('e5bc6e7f-62ea-408e-a9d9-a146c6bbb1e9')
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_pre__Type"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type57(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type57(attr_value, this)"""
        self.vs[14]["MT_label__"] = """57"""
        self.vs[14]["mm__"] = """MT_pre__Attribute"""
        self.vs[14]["MT_subtypes__"] = """[]"""
        self.vs[14]["MT_dirty__"] = False
        self.vs[14]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name57(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name57(attr_value, this)"""
        self.vs[14]["GUID__"] = UUID('71815e93-4b43-4684-a380-04e99d660131')
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_pre__Type"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type62(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type62(attr_value, this)"""
        self.vs[15]["MT_label__"] = """62"""
        self.vs[15]["mm__"] = """MT_pre__Attribute"""
        self.vs[15]["MT_subtypes__"] = """[]"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["MT_pre__name"] = """from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name62(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name62(attr_value, this)"""
        self.vs[15]["GUID__"] = UUID('3528042d-05fb-4a35-99ef-d1d0cd689d4f')

    def eval_associationType0(self, attr_value, this):
        
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
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_classtype2(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_classtype2(attr_value, this)


    def eval_cardinality2(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_cardinality2(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_cardinality2(attr_value, this)


    def eval_name2(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name2(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name2(attr_value, this)


    def eval_classtype3(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_classtype3(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_classtype3(attr_value, this)


    def eval_cardinality3(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_cardinality3(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_cardinality3(attr_value, this)


    def eval_name3(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name3(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name3(attr_value, this)


    def eval_name39(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name39(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name39(attr_value, this)


    def eval_name43(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name43(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name43(attr_value, this)


    def eval_Type51(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type51(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type51(attr_value, this)


    def eval_name51(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name51(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name51(attr_value, this)


    def eval_Type55(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type55(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type55(attr_value, this)


    def eval_name55(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name55(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name55(attr_value, this)


    def eval_Type57(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type57(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type57(attr_value, this)


    def eval_name57(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name57(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name57(attr_value, this)


    def eval_Type62(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_Type62(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_Type62(attr_value, this)


    def eval_name62(self, attr_value, this):
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1 import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1
        from HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC
        lhs = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1()
        return HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_matcher_1().eval_name62(attr_value, this) and HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_rule_combinator_NAC(lhs).eval_name62(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

