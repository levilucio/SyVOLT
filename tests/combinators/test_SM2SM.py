'''
Created on 2015-01-20

@author: levi
'''
'''
Created on 2015-01-19

@author: levi
'''
import unittest

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter

from himesis_utils import graph_to_dot

from PyRamify import PyRamify

from tests.TestModules.HSM2SM_partial import HSM2SM_partial
from tests.TestModules.HSM2SM_complete import HSM2SM_complete

class Test(unittest.TestCase):


    def testName(self):       
        i = Iterator()
        p = Packet()

        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("dir_for_pyramify/", True)

        HSM2SM_py = self.ruleCombinators["HSM2SM"]
        print(HSM2SM_py)

        matcher = HSM2SM_py[0][0]
        rewriter = HSM2SM_py[0][1]
        
#         p.graph = HSM2SM()
# 
#         
#         graph_to_dot("test_before_SM2SM", HSM2SM())
#         
#         graph_to_dot("test_SM2SM", p.graph)
#         
#         s2s_match = matcher
#         s2s_rewrite = rewriter
# 
#         graph_to_dot("test_SM2SM_graph", p.graph)
        graph_to_dot("test_SM2SM_matcher", matcher.condition)
        graph_to_dot("test_SM2SM_rewriter", rewriter.condition)
#          
#         s2s_match.packet_in(p)
#          
#         if s2s_match.is_success:
#             print "Yes!"
#         else:
#             print "no"
#              
#         p = i.packet_in(p)
#         p = s2s_rewrite.packet_in(p)
#          
#         if s2s_rewrite.is_success:
#             print "Yes!"
#         else:
#             print "no"
#          
#         graph_to_dot("test_after_SM2SM", p.graph)
        
            
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()