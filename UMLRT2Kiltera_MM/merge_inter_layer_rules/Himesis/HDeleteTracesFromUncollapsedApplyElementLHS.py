

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HDeleteTracesFromUncollapsedApplyElementLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDeleteTracesFromUncollapsedApplyElementLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeleteTracesFromUncollapsedApplyElementLHS, self).__init__(name='HDeleteTracesFromUncollapsedApplyElementLHS', num_nodes=3, edges=[])
        
        # Add the edges
        self.add_edges([(0, 1), (1, 2)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__GM2AUTOSAR_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""Vreturn True\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('3f3b5980-ae85-4150-b9fa-41dbcadd6759')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = True
        self.vs[0]["MT_pre__classtype"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[0]["MT_pivotIn__"] = """element2"""
        self.vs[0]["MT_label__"] = """4"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__EcuInstance'
p2
aS'MT_pre__System'
p3
aS'MT_pre__SystemMapping'
p4
aS'MT_pre__ComponentPrototype'
p5
aS'MT_pre__SwCompToEcuMapping_component'
p6
aS'MT_pre__CompositionType'
p7
aS'MT_pre__PPortPrototype'
p8
aS'MT_pre__SwcToEcuMapping'
p9
aS'MT_pre__SoftwareComposition'
p10
aS'MT_pre__RPortPrototype'
p11
aS'MT_pre__PortPrototype'
p12
aS'MT_pre__ComponentType'
p13
a.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[0]["MT_pre__cardinality"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[0]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[0]["GUID__"] = UUID('d03f7dc4-4e54-4964-b443-963b39c6eb08')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """13"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["mm__"] = """MT_pre__trace_link"""
        self.vs[1]["GUID__"] = UUID('d9cbce4f-43bc-424b-aca7-d28c83dc928e')
        self.vs[2]["MT_subtypeMatching__"] = True
        self.vs[2]["MT_pre__classtype"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
S'MT_pre__VirtualDevice'
p2
aS'MT_pre__Distributable'
p3
aS'MT_pre__Signal'
p4
aS'MT_pre__ExecFrame'
p5
aS'MT_pre__ECU'
p6
a.""")
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_pre__cardinality"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[2]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[2]["GUID__"] = UUID('1e7a44ae-46d7-4921-a488-225545e6976a')

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


    def eval_cardinality4(self, attr_value, this):
        
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


    def eval_classtype5(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality5(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


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


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

