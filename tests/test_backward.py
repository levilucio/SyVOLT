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
#        self.rulesIncludingBackLinks = pyramify.getRulesIncludingBackLinks(transformation, self.backwardPatterns)
 
 
        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]
        subclasses_source = ["MT_pre__Trigger_S"]
        subclasses_target = ["MT_pre__Kiltera_T"]
        
        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)
        
        trace = ARule(HBuildTraceabilityForRuleLHS(),HBuildTraceabilityForRuleRHS())
        
        p = Packet()
        p.graph = HKiltera_backward2trace()
        p = trace.packet_in(p)
        m1 = p.graph
        
        print trace.is_success
        
        graph_to_dot("trace_result", p.graph)
        
        