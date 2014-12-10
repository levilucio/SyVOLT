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

from himesis_utils import graph_to_dot

from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_totalLHS import HSM2SM_totalLHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_totalRHS import HSM2SM_totalRHS

from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_partial_1LHS import HSM2SM_partial_1LHS
#from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_partial_1NAC0 import HSM2SM_partial_1NAC0
#from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_partial_1NAC0Bridge import HSM2SM_partial_1NAC0Bridge
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_partial_1RHS import HSM2SM_partial_1RHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_totalLHS import HSM2SM_totalLHS
from property_prover_rules.pc_and_rule_combination.Himesis.HSM2SM_totalRHS import HSM2SM_totalRHS

from tests.TestModules.HExample_model2 import HExample_model2
from tests.TestModules.HExample_model import HExample_model

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_rewrite_double(self):
        
        
#         m = Matcher(HSM2SM_partial_1LHS())
#         
#         p = Packet()
#         
#         p.graph = HExample_model2()
#         
#         m.packet_in(p)
#         
#         if m.is_success: print "Success!"
#         else: print "Fail"

        rewrite_double = ARule(HSM2SM_partial_1LHS(),HSM2SM_partial_1RHS())
         
        p = Packet()
         
        p.graph = HExample_model2()
          
        graph_to_dot("modelbefore", p.graph, 1)        
          
        p = rewrite_double.packet_in(p)
          
        graph_to_dot("modelafter", p.graph, 1)        
            