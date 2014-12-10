'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time

from path_condition_generator import PathConditionGenerator

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator
from t_core.messages import Packet

from t_core.tc_python.frule import FRule
from t_core.tc_python.arule import ARule

from himesis_utils import graph_to_dot
from himesis_utils import disjoint_model_union
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules

# run 1

from police_station_transformation.run1.transformation.HS2S_run1 import HS2S_run1
from police_station_transformation.run1.transformation.HM2M_run1 import HM2M_run1
from police_station_transformation.run1.transformation.HF2F_run1 import HF2F_run1
from police_station_transformation.run1.transformation.HSM2SM_run1 import HSM2SM_run1
from police_station_transformation.run1.transformation.HSF2SF_run1 import HSF2SF_run1
from police_station_transformation.run1.transformation.HMM2MM_run1 import HMM2MM_run1
from police_station_transformation.run1.transformation.HFF2FF_run1 import HFF2FF_run1

from police_station_transformation.run1.backward_matchers.HSM2SMBackS2S_run1LHS import HSM2SMBackS2S_run1LHS
from police_station_transformation.run1.backward_matchers.HSM2SMBackM2M_run1LHS import HSM2SMBackM2M_run1LHS
from police_station_transformation.run1.backward_matchers.HSF2SFBackS2S_run1LHS import HSF2SFBackS2S_run1LHS
from police_station_transformation.run1.backward_matchers.HSF2SFBackF2F_run1LHS import HSF2SFBackF2F_run1LHS
from police_station_transformation.run1.backward_matchers.HMM2MMBackM2M1_run1LHS import HMM2MMBackM2M1_run1LHS
from police_station_transformation.run1.backward_matchers.HMM2MMBackM2M2_run1LHS import HMM2MMBackM2M2_run1LHS
from police_station_transformation.run1.backward_matchers.HFF2FFBackF2F1_run1LHS import HFF2FFBackF2F1_run1LHS
from police_station_transformation.run1.backward_matchers.HFF2FFBackF2F2_run1LHS import HFF2FFBackF2F2_run1LHS

from police_station_transformation.run1.backward_matchers.HSM2SMBackComplete_run1LHS import HSM2SMBackComplete_run1LHS
from police_station_transformation.run1.backward_matchers.HSF2SFBackComplete_run1LHS import HSF2SFBackComplete_run1LHS
from police_station_transformation.run1.backward_matchers.HMM2MMBackComplete_run1LHS import HMM2MMBackComplete_run1LHS
from police_station_transformation.run1.backward_matchers.HFF2FFBackComplete_run1LHS import HFF2FFBackComplete_run1LHS


# run 2

from police_station_transformation.run2.transformation.HS2S_run2 import HS2S_run2
from police_station_transformation.run2.transformation.HM2M_run2 import HM2M_run2
from police_station_transformation.run2.transformation.HF2F_run2 import HF2F_run2
from police_station_transformation.run2.transformation.HSM2SM_run2 import HSM2SM_run2
from police_station_transformation.run2.transformation.HSF2SF_run2 import HSF2SF_run2
from police_station_transformation.run2.transformation.HMM2MM_run2 import HMM2MM_run2
from police_station_transformation.run2.transformation.HFF2FF_run2 import HFF2FF_run2

from police_station_transformation.run2.backward_matchers.HSM2SMBackS2S_run2LHS import HSM2SMBackS2S_run2LHS
from police_station_transformation.run2.backward_matchers.HSM2SMBackM2M_run2LHS import HSM2SMBackM2M_run2LHS
from police_station_transformation.run2.backward_matchers.HSF2SFBackS2S_run2LHS import HSF2SFBackS2S_run2LHS
from police_station_transformation.run2.backward_matchers.HSF2SFBackF2F_run2LHS import HSF2SFBackF2F_run2LHS
from police_station_transformation.run2.backward_matchers.HMM2MMBackM2M1_run2LHS import HMM2MMBackM2M1_run2LHS
from police_station_transformation.run2.backward_matchers.HMM2MMBackM2M2_run2LHS import HMM2MMBackM2M2_run2LHS
from police_station_transformation.run2.backward_matchers.HFF2FFBackF2F1_run2LHS import HFF2FFBackF2F1_run2LHS
from police_station_transformation.run2.backward_matchers.HFF2FFBackF2F2_run2LHS import HFF2FFBackF2F2_run2LHS

from police_station_transformation.run2.backward_matchers.HSM2SMBackComplete_run2LHS import HSM2SMBackComplete_run2LHS
from police_station_transformation.run2.backward_matchers.HSF2SFBackComplete_run2LHS import HSF2SFBackComplete_run2LHS
from police_station_transformation.run2.backward_matchers.HMM2MMBackComplete_run2LHS import HMM2MMBackComplete_run2LHS
from police_station_transformation.run2.backward_matchers.HFF2FFBackComplete_run2LHS import HFF2FFBackComplete_run2LHS


# run 3

from police_station_transformation.run3.transformation.HS2S_run3 import HS2S_run3
from police_station_transformation.run3.transformation.HM2M_run3 import HM2M_run3
from police_station_transformation.run3.transformation.HF2F_run3 import HF2F_run3
from police_station_transformation.run3.transformation.HSM2SM_run3 import HSM2SM_run3
from police_station_transformation.run3.transformation.HSF2SF_run3 import HSF2SF_run3
from police_station_transformation.run3.transformation.HMM2MM_run3 import HMM2MM_run3
from police_station_transformation.run3.transformation.HFF2FF_run3 import HFF2FF_run3

from police_station_transformation.run3.backward_matchers.HSM2SMBackS2S_run3LHS import HSM2SMBackS2S_run3LHS
from police_station_transformation.run3.backward_matchers.HSM2SMBackM2M_run3LHS import HSM2SMBackM2M_run3LHS
from police_station_transformation.run3.backward_matchers.HSF2SFBackS2S_run3LHS import HSF2SFBackS2S_run3LHS
from police_station_transformation.run3.backward_matchers.HSF2SFBackF2F_run3LHS import HSF2SFBackF2F_run3LHS
from police_station_transformation.run3.backward_matchers.HMM2MMBackM2M1_run3LHS import HMM2MMBackM2M1_run3LHS
from police_station_transformation.run3.backward_matchers.HMM2MMBackM2M2_run3LHS import HMM2MMBackM2M2_run3LHS
from police_station_transformation.run3.backward_matchers.HFF2FFBackF2F1_run3LHS import HFF2FFBackF2F1_run3LHS
from police_station_transformation.run3.backward_matchers.HFF2FFBackF2F2_run3LHS import HFF2FFBackF2F2_run3LHS

from police_station_transformation.run3.backward_matchers.HSM2SMBackComplete_run3LHS import HSM2SMBackComplete_run3LHS
from police_station_transformation.run3.backward_matchers.HSF2SFBackComplete_run3LHS import HSF2SFBackComplete_run3LHS
from police_station_transformation.run3.backward_matchers.HMM2MMBackComplete_run3LHS import HMM2MMBackComplete_run3LHS
from police_station_transformation.run3.backward_matchers.HFF2FFBackComplete_run3LHS import HFF2FFBackComplete_run3LHS


# run 4

from police_station_transformation.run4.transformation.HS2S_run4 import HS2S_run4
from police_station_transformation.run4.transformation.HM2M_run4 import HM2M_run4
from police_station_transformation.run4.transformation.HF2F_run4 import HF2F_run4
from police_station_transformation.run4.transformation.HSM2SM_run4 import HSM2SM_run4
from police_station_transformation.run4.transformation.HSF2SF_run4 import HSF2SF_run4
from police_station_transformation.run4.transformation.HMM2MM_run4 import HMM2MM_run4
from police_station_transformation.run4.transformation.HFF2FF_run4 import HFF2FF_run4

from police_station_transformation.run4.backward_matchers.HSM2SMBackS2S_run4LHS import HSM2SMBackS2S_run4LHS
from police_station_transformation.run4.backward_matchers.HSM2SMBackM2M_run4LHS import HSM2SMBackM2M_run4LHS
from police_station_transformation.run4.backward_matchers.HSF2SFBackS2S_run4LHS import HSF2SFBackS2S_run4LHS
from police_station_transformation.run4.backward_matchers.HSF2SFBackF2F_run4LHS import HSF2SFBackF2F_run4LHS
from police_station_transformation.run4.backward_matchers.HMM2MMBackM2M1_run4LHS import HMM2MMBackM2M1_run4LHS
from police_station_transformation.run4.backward_matchers.HMM2MMBackM2M2_run4LHS import HMM2MMBackM2M2_run4LHS
from police_station_transformation.run4.backward_matchers.HFF2FFBackF2F1_run4LHS import HFF2FFBackF2F1_run4LHS
from police_station_transformation.run4.backward_matchers.HFF2FFBackF2F2_run4LHS import HFF2FFBackF2F2_run4LHS

from police_station_transformation.run4.backward_matchers.HSM2SMBackComplete_run4LHS import HSM2SMBackComplete_run4LHS
from police_station_transformation.run4.backward_matchers.HSF2SFBackComplete_run4LHS import HSF2SFBackComplete_run4LHS
from police_station_transformation.run4.backward_matchers.HMM2MMBackComplete_run4LHS import HMM2MMBackComplete_run4LHS
from police_station_transformation.run4.backward_matchers.HFF2FFBackComplete_run4LHS import HFF2FFBackComplete_run4LHS

from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS

from police_station_transformation.traceability.HTraceabilityConstructionLHS import HTraceabilityConstructionLHS
from police_station_transformation.traceability.HTraceabilityConstructionRHS import HTraceabilityConstructionRHS

from police_station_transformation.traceability.HBuildTraceabilityGMLHS import HBuildTraceabilityGMLHS
from police_station_transformation.traceability.HBuildTraceabilityGMRHS import HBuildTraceabilityGMRHS

from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0NAC0Bridge import HSF2SF_combine_0NAC0Bridge 
from property_prover_rules.pc_and_rule_combination.Himesis.HSF2SF_combine_0RHS import HSF2SF_combine_0RHS

from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0NAC0Bridge import HSM2SM_combine_0NAC0Bridge 
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_combine_0RHS import HSM2SM_combine_0RHS

from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS


from copy import deepcopy
from himesis_utils import disjoint_model_union, graph_to_dot


class Test(unittest.TestCase):

 

    def test_matching(self):
#        build_traceability_for_rule = ARule(HBuildTraceabilityNoBackwardLHS(),HBuildTraceabilityNoBackwardRHS())
#        build_traceability_for_rule = ARule(HTraceabilityConstructionLHS(),HTraceabilityConstructionRHS())
        build_traceability_for_rule = ARule(HBuildTraceabilityForRuleLHS(),HBuildTraceabilityForRuleRHS())
#        build_traceability_for_rule = ARule(HBuildTraceabilityGMLHS(),HBuildTraceabilityGMRHS())

        match_sm = Matcher(HSM2SM_combine_0LHS())
        match_sf = Matcher(HSM2SM_combine_0LHS())
        
        match_sm = Rewriter(HSM2SM_combine_0RHS())
        match_sf = Rewriter(HSM2SM_combine_0RHS())
        
        
        iter = Iterator(max_iterations=1)

        trace = ARule(HBuildTraceabilityForRuleLHS(),HBuildTraceabilityForRuleRHS())
        
        p = Packet()
        p.graph = HS2S_run1()
        p = trace.packet_in(p)
        m1 = p.graph
        
        p = Packet()
        p.graph = HM2M_run1()
        p = trace.packet_in(p)
        m2 = p.graph        

        m = disjoint_model_union(m1,m2)

#        final = disjoint_model_union(s2s,disjoint_model_union(m2m, f2f)) 
        
#        finalcopy = deepcopy(final)
        
                 
        
        
#         sm2sm = HSM2SM_run1()
#         sf2sf = HSF2SF_run1()
#         
#         s2s_new = deepcopy(s2s)
#         m2m_new = deepcopy(m2m)
#         f2f_new = deepcopy(f2f)    
#         
#         s22_merge_f2f = disjoint_model_union(s2s_new,f2f_new)  
#                 
#         p = Packet()
#         p.graph = s2s
#         p = build_traceability_for_rule_match.packet_in(p)
#         
#         p = iter.packet_in(p)
#         
#         print "----------------------"
#         print p
#         print "----------------------"
                
#         p.graph = s22_merge_f2f
#  
#         print "----------------------"
#         print p
#         print "----------------------"
#         
#         p = build_traceability_for_rule_rewrite.packet_in(p)
#         
#         if (build_traceability_for_rule_rewrite.is_success):
#             print("Yes!!!")
#         else:
#             print("No")        

        graph_to_dot("final",m)
            