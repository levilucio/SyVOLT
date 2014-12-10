'''
Created on 2013-01-22

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

from police_station_transformation.run1.transformation.HS2S_run1 import HS2S_run1
from police_station_transformation.run1.transformation.HM2M_run1 import HM2M_run1
from police_station_transformation.run1.transformation.HF2F_run1 import HF2F_run1

from police_station_transformation.run1.transformation.HSM2SM_run1 import HSM2SM_run1

from tests.TestModules.HExample_model import HExample_model
from tests.TestModules.HNacExampleRuleLHS import HNacExampleRuleLHS
from tests.TestModules.HNacExampleRuleNAC0 import HNacExampleRuleNAC0
from tests.TestModules.HNacExampleRuleNAC0Bridge import HNacExampleRuleNAC0Bridge
from tests.TestModules.HNacExampleRuleRHS import HNacExampleRuleRHS

from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0NAC0Bridge import HSF2SF_combine_0NAC0Bridge 
from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0RHS import HSF2SF_combine_0RHS

from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0NAC0Bridge import HSM2SM_combine_0NAC0Bridge 
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0RHS import HSM2SM_combine_0RHS

# transformation to built traceability for rules
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS
from copy import deepcopy


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_NAC(self):
        
        it = Iterator()
        
        sm_matcher = Matcher(HSM2SM_combine_0LHS())
        sm_rewriter = Rewriter(HSM2SM_combine_0RHS())

        sf_matcher = Matcher(HSF2SF_combine_0LHS())
        sf_rewriter = Rewriter(HSF2SF_combine_0RHS())
        
        trace = ARule(HBuildTraceabilityForRuleLHS(),HBuildTraceabilityForRuleRHS())
        
        p = Packet()
        p.graph = HS2S_run1()
        p = trace.packet_in(p)
        m1 = p.graph
        
        p = Packet()
        p.graph = HM2M_run1()
        p = trace.packet_in(p)
        m2 = p.graph        

        p = Packet()
        p.graph = HF2F_run1()
        p = trace.packet_in(p)
        m3 = p.graph    

        m = disjoint_model_union(m1,disjoint_model_union(m2, m3))
        
        m_copy = deepcopy(m)
        
        p = Packet()
        p.graph = m       
        p = sm_matcher.packet_in(p)
        
        p1 = Packet()
        p1.graph = m       
        p1 = sf_matcher.packet_in(p1)        
        
        p = it.packet_in(p)
        p.graph = deepcopy(p.graph)
        p = sm_rewriter.packet_in(p)
               
        p1 = it.packet_in(p1)
        p1.graph = deepcopy(p.graph)
        p1 = sf_rewriter.packet_in(p1)
        
        graph_to_dot("final", p1.graph, 1)  
        
        p.graph = deepcopy(p.graph)        
        p = sf_rewriter.packet_in(p)
               
        graph_to_dot("final2", p.graph, 1)        
            