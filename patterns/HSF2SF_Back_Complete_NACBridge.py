

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HSF2SF_Back_Complete_NACBridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_Back_Complete_NACBridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_Back_Complete_NACBridge, self).__init__(name='HSF2SF_Back_Complete_NACBridge', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[2, 4], [4, 1], [0, 5], [5, 3]])
        # Set the graph attributes
        self["GUID__"] = UUID('f87faad5-c21d-4feb-a17c-9b7ad37241ad')
        
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
        self.vs[0]["MT_pre__classtype"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_classtype3(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype3(attr_value, this)"""
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
        self.vs[0]["MT_pre__name"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_name3(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name3(attr_value, this)"""
        self.vs[0]["MT_label__"] = """3"""
        self.vs[0]["mm__"] = """MT_pre__Female_T"""
        self.vs[0]["MT_subtypes__"] = """[]"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('ca29863c-d63e-48c1-bfaa-69ae58b31b80')
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
        self.vs[1]["MT_pre__associationType"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_associationType5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_associationType5(attr_value, this)"""
        self.vs[1]["MT_pre__classtype"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_classtype5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype5(attr_value, this)"""
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
        self.vs[1]["MT_pre__name"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_name5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name5(attr_value, this)"""
        self.vs[1]["MT_label__"] = """5"""
        self.vs[1]["mm__"] = """MT_pre__Station_S"""
        self.vs[1]["MT_subtypes__"] = """[]"""
        self.vs[1]["MT_pre__cardinality"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_cardinality5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_cardinality5(attr_value, this)"""
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
        self.vs[1]["GUID__"] = UUID('0164d0c3-6f5a-4221-bfc2-48992a04def8')
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
        self.vs[2]["MT_pre__associationType"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_associationType6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_associationType6(attr_value, this)"""
        self.vs[2]["MT_pre__classtype"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_classtype6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype6(attr_value, this)"""
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
        self.vs[2]["MT_pre__name"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_name6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name6(attr_value, this)"""
        self.vs[2]["MT_label__"] = """6"""
        self.vs[2]["mm__"] = """MT_pre__Station_T"""
        self.vs[2]["MT_subtypes__"] = """[]"""
        self.vs[2]["MT_pre__cardinality"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_cardinality6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_cardinality6(attr_value, this)"""
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
        self.vs[2]["GUID__"] = UUID('9c9491e7-3572-42a5-bebf-7d2ce3719e3c')
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
        self.vs[3]["MT_pre__associationType"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_associationType7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_associationType7(attr_value, this)"""
        self.vs[3]["MT_pre__classtype"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_classtype7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype7(attr_value, this)"""
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
        self.vs[3]["MT_pre__name"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_name7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name7(attr_value, this)"""
        self.vs[3]["MT_label__"] = """7"""
        self.vs[3]["mm__"] = """MT_pre__Female_S"""
        self.vs[3]["MT_subtypes__"] = """[]"""
        self.vs[3]["MT_pre__cardinality"] = """from HSF2SF1 import HSF2SF1
from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
lhs = HSF2SF1()
return HSF2SF1().eval_cardinality7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_cardinality7(attr_value, this)"""
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
        self.vs[3]["GUID__"] = UUID('655f179c-24de-49f9-b91c-4f9238eea279')
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
        self.vs[4]["GUID__"] = UUID('cdeb65d6-aff4-4b8f-9549-af9660ddda55')
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
        self.vs[5]["GUID__"] = UUID('9e9e357d-093a-4ffa-bd7a-b7ebc8660ab9')

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


    def eval_classtype3(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_classtype3(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype3(attr_value, this)


    def eval_name3(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_name3(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name3(attr_value, this)


    def eval_associationType5(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_associationType5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_associationType5(attr_value, this)


    def eval_classtype5(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_classtype5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype5(attr_value, this)


    def eval_name5(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_name5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name5(attr_value, this)


    def eval_cardinality5(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_cardinality5(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_cardinality5(attr_value, this)


    def eval_associationType6(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_associationType6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_associationType6(attr_value, this)


    def eval_classtype6(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_classtype6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype6(attr_value, this)


    def eval_name6(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_name6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name6(attr_value, this)


    def eval_cardinality6(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_cardinality6(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_cardinality6(attr_value, this)


    def eval_associationType7(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_associationType7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_associationType7(attr_value, this)


    def eval_classtype7(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_classtype7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_classtype7(attr_value, this)


    def eval_name7(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_name7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_name7(attr_value, this)


    def eval_cardinality7(self, attr_value, this):
        from HSF2SF1 import HSF2SF1
        from HSF2SF_Back_Complete_NAC import HSF2SF_Back_Complete_NAC
        lhs = HSF2SF1()
        return HSF2SF1().eval_cardinality7(attr_value, this) and HSF2SF_Back_Complete_NAC(lhs).eval_cardinality7(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

