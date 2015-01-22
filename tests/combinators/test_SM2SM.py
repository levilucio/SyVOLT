'''
Created on 2015-01-20

@author: levi
'''
'''
Created on 2015-01-19

@author: levi
'''
import unittest

from patterns.HSM2SM_Back_Complete import HSM2SM_Back_Complete
from patterns.HSM2SM_rewriter import HSM2SM_rewriter

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter

from himesis_utils import graph_to_dot

from tests.TestModules.HSM2SM import HSM2SM

class Test(unittest.TestCase):


    def testName(self):       
        i = Iterator()
        p = Packet()
        
        p.graph = HSM2SM_Back_Complete()
        
        graph_to_dot("HSM2SM_Back_Complete", p.graph)
        
#         graph_to_dot("SM2SM", p.graph)
#         
#         s2s_match = Matcher(HSM2SM_matchLHS())
#         s2s_rewrite = Rewriter(HSM2SM_rewriter())
#  
#         graph_to_dot("SM2SM_matcher", HSM2SM_matchLHS())
#         graph_to_dot("SM2SM_rewriter", HSM2SM_rewriter())        
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
#         graph_to_dot("after_SM2SM", p.graph)
        
            
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()