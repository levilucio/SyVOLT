
'''
Created on 2015-01-19

@author: levi
'''
import unittest

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter

from himesis_utils import graph_to_dot, print_graph

from PyRamify import PyRamify

from tests.TestModules.HSM2SM_partial import HSM2SM_partial
from tests.TestModules.HSM2SM_complete import HSM2SM_complete

class Test(unittest.TestCase):


    def testName(self):       
        i = Iterator()
        p = Packet()

        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("dir_for_ramify_1/", True)

        HSM2SM_py = self.ruleCombinators["HSM2SM"]
        print(HSM2SM_py)

        matcher = HSM2SM_py[1][0]
        rewriter = HSM2SM_py[1][1]
        
        p.graph = HSM2SM_complete() 
         
        graph_to_dot("test_before_SM2SM_complete", HSM2SM_complete())
        
        graph_to_dot("test_SM2SM", p.graph)
         
        comb_match = matcher
        comb_rewrite = rewriter
# 
#         graph_to_dot("test_SM2SM_graph", p.graph)
        graph_to_dot("comb1_SM2SM_matcher", matcher.condition)
        graph_to_dot("comb1_SM2SM_rewriter", rewriter.condition)
          
        comb_match.packet_in(p)
          
        if comb_match.is_success:
            print "Yes!"
        else:
            print "no"
              
        p = i.packet_in(p)
        p = comb_rewrite.packet_in(p)
          
        if comb_rewrite.is_success:
            print "Yes!"
        else:
            print "no"
          
        graph_to_dot("test_after_SM2SM", p.graph)
        

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()