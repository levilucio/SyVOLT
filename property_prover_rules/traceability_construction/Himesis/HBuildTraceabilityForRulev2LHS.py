

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HBuildTraceabilityForRulev2LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBuildTraceabilityForRulev2LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBuildTraceabilityForRulev2LHS, self).__init__(name='HBuildTraceabilityForRulev2LHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([(3, 0), (0, 4), (1, 2), (2, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__GM2AUTOSAR_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""Vif set([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'trace_link'])) == set():\u000a    return True\u000a\u000areturn False\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('49aef741-7975-4a28-8eed-db8bb1ca4b5a')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """6"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__apply_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('e0aa36f1-83b5-4c90-b987-5348eb7d0f5a')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__MatchModel"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('987e3689-0063-45ab-85cc-a6082bf32b8b')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__match_contains"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('c8511d46-2e97-4acb-b77d-71edd8e5cb15')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """2"""
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('b11c9e40-21c0-4898-a556-5ea9768d987e')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """4"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
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
        self.vs[4]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["MT_pre__attr1"] = """
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
        self.vs[4]["GUID__"] = UUID('6af656b0-82e9-42d4-9ec3-298743f1576a')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """3"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
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
        self.vs[5]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["MT_pre__attr1"] = """
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
        self.vs[5]["GUID__"] = UUID('409e62c7-12d9-4181-84f5-94ad578b5310')

    def eval_attr14(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_attr13(self, attr_value, this):
        
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
        if set([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'trace_link'])) == set():
            return True
        
        return False

