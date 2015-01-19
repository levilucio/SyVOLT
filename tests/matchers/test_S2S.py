'''
Created on 2015-01-19

@author: levi
'''
import unittest

from patterns.HS2S_matchLHS import HS2S_matchLHS
from patterns.HS2S_rewriter import HS2S_rewriter

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter

from himesis_utils import graph_to_dot

from PoliceStationMM.transformation_1.Himesis.HS2S import HS2S

class Test(unittest.TestCase):


    def testName(self):       
        i = Iterator()
        p = Packet()
        
        p.graph = HS2S()
        
        graph_to_dot("before_S2S", p.graph)
        
        s2s_match = Matcher(HS2S_matchLHS())
        s2s_rewrite = Rewriter(HS2S_rewriter())

        graph_to_dot("S2S_matcher", HS2S_matchLHS())
        graph_to_dot("S2S_rewriter", HS2S_rewriter())        
        
        s2s_match.packet_in(p)
        
        if s2s_match.is_success:
            print "Yes!"
        else:
            print "no"
            
        p = i.packet_in(p)
        p = s2s_rewrite.packet_in(p)
        
        if s2s_rewrite.is_success:
            print "Yes!"
        else:
            print "no"
        
        graph_to_dot("after_S2S", p.graph)
        
            
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()