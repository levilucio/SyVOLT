'''
Created on 2015-01-27

@author: levi
'''
import unittest
import time

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator
from t_core.messages import Packet

from t_core.tc_python.frule import FRule
from t_core.tc_python.arule import ARule

from himesis_utils import graph_to_dot, disjoint_model_union

from PyRamify import PyRamify

from tests.TestModules.HKiltera_backward2trace import HKiltera_backward2trace


# transformation to built traceability for rules
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS
from copy import deepcopy


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_back(self):
        
        pyramify = PyRamify()

        pyramify = PyRamify()
#        self.rulesIncludingBackLinks = pyramify.getRulesIncludingBackLinks(transformation, self.backwardPatterns)
 
        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]
        subclasses_source = ["MT_pre__OPTIONAL1,","MT_pre__PhysicalThread", "MT_pre__PortRef", "MT_pre__PackageContainer", "MT_pre__Thread", "MT_pre__OUT2", "MT_pre__BASE0",\
                            "MT_pre__NamedElement", "MT_pre__Element", "MT_pre__OUT1", "MT_pre__Signal", "MT_pre__Package", "MT_pre__PortType",\
                            "MT_pre__PortConnectorRef", "MT_pre__IN1", "MT_pre__IN0", "MT_pre__LogicalThread", "MT_pre__RoleType", "MT_pre__Vertex",\
                            "MT_pre__SIBLING0", "MT_pre__InitialPoint", "MT_pre__PortConnector", "MT_pre__SignalType", "MT_pre__Transition",\
                            "MT_pre__EntryPoint", "MT_pre__CONJUGATE1", "MT_pre__Protocol", "MT_pre__StateMachine", "MT_pre__Model_S",\
                            "MT_pre__StateMachineElement", "MT_pre__Port", "MT_pre__TransitionType", "MT_pre__Capsule", "MT_pre__Trigger_S",\
                            "MT_pre__State", "MT_pre__PLUGIN2", "MT_pre__Action", "MT_pre__CapsuleRole", "MT_pre__ExitPoint", "MT_pre__FIXED0"]
        subclasses_target = ["MT_pre__Name", "MT_pre__Module", "MT_pre__ConditionBranch", "MT_pre__Delay", "MT_pre__LocalDef",\
                              "MT_pre__Expr", "MT_pre__ConditionSet", "MT_pre__Proc", "MT_pre__MatchCase", "MT_pre__Match",\
                              "MT_pre__FuncDef", "MT_pre__Null", "MT_pre__Par", "MT_pre__Inst", "MT_pre__Listen", "MT_pre__Site",\
                              "MT_pre__New", "MT_pre__PythonRef", "MT_pre__Def", "MT_pre__Seq", "MT_pre__ParIndexed", "MT_pre__Condition",\
                              "MT_pre__Print", "MT_pre__Pattern", "MT_pre__ListenBranch", "MT_pre__ProcDef", "MT_pre__Trigger_T","MT_pre__Model_T"]

  
        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)
        
        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)
        
        trace = ARule(HBuildTraceabilityForRuleLHS(),HBuildTraceabilityForRuleRHS())
        
        p = Packet()
        p.graph = HKiltera_backward2trace()
        p = trace.packet_in(p)
        m1 = p.graph
        
        print trace.is_success
        
        graph_to_dot("trace_result", p.graph)
        
        