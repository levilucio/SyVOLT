'''
Created on 2015-01-20

@author: levi
'''
import unittest

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator
from t_core.messages import Packet

from t_core.tc_python.frule import FRule
from t_core.tc_python.arule import ARule

from patterns.Hr2_rule_combinator_matcher_1 import Hr2_rule_combinator_matcher_1
from tests.TestModules.Hr1 import Hr1

class Test(unittest.TestCase):


    def testClaudioRules(self):
        m = Matcher(Hr2_rule_combinator_matcher_1())
        p = Packet()
        p.graph = Hr1()
        p = m.packet_in(p)
        print(str(m.is_success))
        
  
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()