'''
Created on 2015-01-19

@author: levi
'''
import unittest
import inspect

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

        matcher = HSM2SM_py[0][0]
        rewriter = HSM2SM_py[0][1]
        
#        print rewriter.condition.vs[3]["MT_label__"]
#         rewriter.condition.vs[newnode]["MT_label__"] = """100"""
#         rewriter.condition.vs[newnode]["mm__"] = """MT_post__Station_T"""        
#        print rewriter.condition.vs[1]["MT_label__"]
#        print rewriter.condition.vs[1]["mm__"]

#        graph_to_dot("rewriter", rewriter.condition)

#         for v in range(len(rewriter.condition.vs)):
#             print rewriter.condition.vs[v] 


#         for v in range(len(rewriter.condition.vs)):
#             rewriter.condition.vs[v]["MT_label__"] = """100"""  
            
#          print_graph(rewriter.condition)
        
        
        p.graph = HSM2SM_partial() 
#         comb_match = matcher
#         comb_rewrite = rewriter
# 
#         graph_to_dot("test_SM2SM_graph", p.graph)
        graph_to_dot("comb_SM2SM_matcher", matcher.condition)
        graph_to_dot("comb_SM2SM_rewriter", rewriter.condition)
        
#         for v in range(len(comb_rewrite.condition.vs)):
#             print comb_rewrite.condition.vs[v] 
#           
        p = matcher.packet_in(p)
          
        if matcher.is_success:
            print "Yes!"
        else:
            print "no"
              
        p = i.packet_in(p)
        p = rewriter.packet_in(p)
          
        if rewriter.is_success:
            print "Yes!"
        else:
            print "no"
          
        graph_to_dot("test_after_SM2SM", p.graph)
        

                   
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()