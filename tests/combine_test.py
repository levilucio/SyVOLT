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

from merge_preprocess import MergePreprocessFactory

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
from copy import deepcopy

from himesis_utils import disjoint_model_union, graph_to_dot

from merge_inter_layer import MergeInterLayerFactory


class Test(unittest.TestCase):

    def setUp(self):
        
        self.rules = {                'HS2S_run1': HS2S_run1(),
                                      'HM2M_run1': HM2M_run1(),
                                      'HF2F_run1': HF2F_run1(),
                                      'HSM2SM_run1': HSM2SM_run1(),
                                      'HSF2SF_run1': HSF2SF_run1(),
                                      'HMM2MM_run1': HMM2MM_run1(),
                                      'HFF2FF_run1': HFF2FF_run1(),
                                      'HS2S_run2': HS2S_run2(),
                                      'HM2M_run2': HM2M_run2(),
                                      'HF2F_run2': HF2F_run2(),
                                      'HSM2SM_run2': HSM2SM_run2(),
                                      'HSF2SF_run2': HSF2SF_run2(),
                                      'HMM2MM_run2': HMM2MM_run2(),
                                      'HFF2FF_run2': HFF2FF_run2(),
                                      'HS2S_run3': HS2S_run3(),
                                      'HM2M_run3': HM2M_run3(),
                                      'HF2F_run3': HF2F_run3(),
                                      'HSM2SM_run3': HSM2SM_run3(),
                                      'HSF2SF_run3': HSF2SF_run3(),
                                      'HMM2MM_run3': HMM2MM_run3(),
                                      'HFF2FF_run3': HFF2FF_run3(),
                                      'HS2S_run4': HS2S_run4(),
                                      'HM2M_run4': HM2M_run4(),
                                      'HF2F_run4': HF2F_run4(),
                                      'HSM2SM_run4': HSM2SM_run4(),
                                      'HSF2SF_run4': HSF2SF_run4(),
                                      'HMM2MM_run4': HMM2MM_run4(),
                                      'HFF2FF_run4': HFF2FF_run4()}

        self.backwardPatterns = {     'HS2S_run1': None,
                                      'HM2M_run1': None,  
                                      'HF2F_run1': None,                 
                                      'HSM2SM_run1': [Matcher(HSM2SMBackS2S_run1LHS()),Matcher(HSM2SMBackM2M_run1LHS())],
                                      'HSF2SF_run1': [Matcher(HSF2SFBackS2S_run1LHS()),Matcher(HSF2SFBackF2F_run1LHS())],
                                      'HMM2MM_run1': [Matcher(HMM2MMBackM2M1_run1LHS()),Matcher(HMM2MMBackM2M2_run1LHS())],
                                      'HFF2FF_run1': [Matcher(HFF2FFBackF2F1_run1LHS()),Matcher(HFF2FFBackF2F2_run1LHS())],
                                      'HS2S_run2': None,
                                      'HM2M_run2': None,  
                                      'HF2F_run2': None,                 
                                      'HSM2SM_run2': [Matcher(HSM2SMBackS2S_run2LHS()),Matcher(HSM2SMBackM2M_run2LHS())],
                                      'HSF2SF_run2': [Matcher(HSF2SFBackS2S_run2LHS()),Matcher(HSF2SFBackF2F_run2LHS())],
                                      'HMM2MM_run2': [Matcher(HMM2MMBackM2M1_run2LHS()),Matcher(HMM2MMBackM2M2_run2LHS())],
                                      'HFF2FF_run2': [Matcher(HFF2FFBackF2F1_run2LHS()),Matcher(HFF2FFBackF2F2_run2LHS())],
                                      'HS2S_run3': None,
                                      'HM2M_run3': None,  
                                      'HF2F_run3': None,                 
                                      'HSM2SM_run3': [Matcher(HSM2SMBackS2S_run3LHS()),Matcher(HSM2SMBackM2M_run3LHS())],
                                      'HSF2SF_run3': [Matcher(HSF2SFBackS2S_run3LHS()),Matcher(HSF2SFBackF2F_run3LHS())],
                                      'HMM2MM_run3': [Matcher(HMM2MMBackM2M1_run3LHS()),Matcher(HMM2MMBackM2M2_run3LHS())],
                                      'HFF2FF_run3': [Matcher(HFF2FFBackF2F1_run3LHS()),Matcher(HFF2FFBackF2F2_run3LHS())],
                                      'HS2S_run4': None,
                                      'HM2M_run4': None,  
                                      'HF2F_run4': None,                 
                                      'HSM2SM_run4': [Matcher(HSM2SMBackS2S_run4LHS()),Matcher(HSM2SMBackM2M_run4LHS())],
                                      'HSF2SF_run4': [Matcher(HSF2SFBackS2S_run4LHS()),Matcher(HSF2SFBackF2F_run4LHS())],
                                      'HMM2MM_run4': [Matcher(HMM2MMBackM2M1_run4LHS()),Matcher(HMM2MMBackM2M2_run4LHS())],
                                      'HFF2FF_run4': [Matcher(HFF2FFBackF2F1_run4LHS()),Matcher(HFF2FFBackF2F2_run4LHS())]}
         
        self.backwardPatterns2Rules = {     'HSM2SMBackS2S_run1LHS': 'HSM2SM_run1',
                                            'HSM2SMBackM2M_run1LHS': 'HSM2SM_run1',
                                            'HSF2SFBackS2S_run1LHS': 'HSF2SF_run1',
                                            'HSF2SFBackF2F_run1LHS': 'HSF2SF_run1',                                        
                                            'HMM2MMBackM2M1_run1LHS': 'HMM2MM_run1',
                                            'HMM2MMBackM2M2_run1LHS': 'HMM2MM_run1',                                      
                                            'HFF2FFBackF2F1_run1LHS': 'HFF2FF_run1',
                                            'HFF2FFBackF2F2_run1LHS': 'HFF2FF_run1',
                                            'HSM2SMBackS2S_run2LHS': 'HSM2SM_run2',
                                            'HSM2SMBackM2M_run2LHS': 'HSM2SM_run2',
                                            'HSF2SFBackS2S_run2LHS': 'HSF2SF_run2',
                                            'HSF2SFBackF2F_run2LHS': 'HSF2SF_run2',                                        
                                            'HMM2MMBackM2M1_run2LHS': 'HMM2MM_run2',
                                            'HMM2MMBackM2M2_run2LHS': 'HMM2MM_run2',                                      
                                            'HFF2FFBackF2F1_run2LHS': 'HFF2FF_run2',
                                            'HFF2FFBackF2F2_run2LHS': 'HFF2FF_run2',
                                            'HSM2SMBackS2S_run3LHS': 'HSM2SM_run3',
                                            'HSM2SMBackM2M_run3LHS': 'HSM2SM_run3',
                                            'HSF2SFBackS2S_run3LHS': 'HSF2SF_run3',
                                            'HSF2SFBackF2F_run3LHS': 'HSF2SF_run3',                                        
                                            'HMM2MMBackM2M1_run3LHS': 'HMM2MM_run3',
                                            'HMM2MMBackM2M2_run3LHS': 'HMM2MM_run3',                                      
                                            'HFF2FFBackF2F1_run3LHS': 'HFF2FF_run3',
                                            'HFF2FFBackF2F2_run3LHS': 'HFF2FF_run3',
                                            'HSM2SMBackS2S_run4LHS': 'HSM2SM_run4',
                                            'HSM2SMBackM2M_run4LHS': 'HSM2SM_run4',
                                            'HSF2SFBackS2S_run4LHS': 'HSF2SF_run4',
                                            'HSF2SFBackF2F_run4LHS': 'HSF2SF_run4',                                        
                                            'HMM2MMBackM2M1_run4LHS': 'HMM2MM_run4',
                                            'HMM2MMBackM2M2_run4LHS': 'HMM2MM_run4',                                      
                                            'HFF2FFBackF2F1_run4LHS': 'HFF2FF_run4',
                                            'HFF2FFBackF2F2_run4LHS': 'HFF2FF_run4'}
        
        self.backwardPatternsComplete = {
                                      'HS2S_run1': None,
                                      'HM2M_run1': None,
                                      'HF2F_run1': None,
                                      'HSM2SM_run1': [Matcher(HSM2SMBackComplete_run1LHS())],
                                      'HSF2SF_run1': [Matcher(HSF2SFBackComplete_run1LHS())],
                                      'HMM2MM_run1': [Matcher(HMM2MMBackComplete_run1LHS())],
                                      'HFF2FF_run1': [Matcher(HFF2FFBackComplete_run1LHS())],
                                      'HS2S_run2': None,
                                      'HM2M_run2': None,
                                      'HF2F_run2': None,
                                      'HSM2SM_run2': [Matcher(HSM2SMBackComplete_run2LHS())],
                                      'HSF2SF_run2': [Matcher(HSF2SFBackComplete_run2LHS())],
                                      'HMM2MM_run2': [Matcher(HMM2MMBackComplete_run2LHS())],
                                      'HFF2FF_run2': [Matcher(HFF2FFBackComplete_run2LHS())],
                                      'HS2S_run3': None,
                                      'HM2M_run3': None,
                                      'HF2F_run3': None,
                                      'HSM2SM_run3': [Matcher(HSM2SMBackComplete_run3LHS())],
                                      'HSF2SF_run3': [Matcher(HSF2SFBackComplete_run3LHS())],
                                      'HMM2MM_run3': [Matcher(HMM2MMBackComplete_run3LHS())],
                                      'HFF2FF_run3': [Matcher(HFF2FFBackComplete_run3LHS())],
                                      'HS2S_run4': None,
                                      'HM2M_run4': None,
                                      'HF2F_run4': None,
                                      'HSM2SM_run4': [Matcher(HSM2SMBackComplete_run4LHS())],
                                      'HSF2SF_run4': [Matcher(HSF2SFBackComplete_run4LHS())],
                                      'HMM2MM_run4': [Matcher(HMM2MMBackComplete_run4LHS())],
                                      'HFF2FF_run4': [Matcher(HFF2FFBackComplete_run4LHS())]}


    def test_combine(self):
#        build_traceability_for_rule = ARule(HBuildTraceabilityNoBackwardLHS(),HBuildTraceabilityNoBackwardRHS())
#        build_traceability_for_rule = ARule(HTraceabilityConstructionLHS(),HTraceabilityConstructionRHS())
        build_traceability_for_rule = ARule(HBuildTraceabilityForRuleLHS(),HBuildTraceabilityForRuleRHS())
#        build_traceability_for_rule = ARule(HBuildTraceabilityGMLHS(),HBuildTraceabilityGMRHS())

        build_traceability_for_rule_match = Matcher(HBuildTraceabilityForRuleLHS())
        build_traceability_for_rule_rewrite = Rewriter(HBuildTraceabilityForRuleRHS())

        s2s = HS2S_run1() 
        m2m = HM2M_run1()        
        f2f = HF2F_run1()    
        
        sm2sm = HSM2SM_run1()
        sf2sf = HSF2SF_run1()
        mm2mm = HMM2MM_run1()
        ff2ff = HFF2FF_run1()
        
        mergeInterLayerFactory = MergeInterLayerFactory(1)        
        combineResult = mergeInterLayerFactory.merge_two_rules_inter_layer(mm2mm,m2m)
        
        graph_to_dot("combinelargerrule", combineResult, 1)
        
        l = [HSM2SM_run1(),HFF2FF_run1()]
        l.extend([])
        print l

#        graph_to_dot("bla",p.graph)
            