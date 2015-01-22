'''
Created on 2015-01-20

@author: levi
'''
import unittest
from himesis_utils import graph_to_dot

from PyRamify import PyRamify

class Test(unittest.TestCase):


    def testRamify(self):
        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("dir_for_pyramify/", True)
            
        matcher = self.matchRulePatterns.values()[0][0]
        rewriter = self.matchRulePatterns.values()[0][1]
        
        graph_to_dot("matcher",matcher.condition)
        graph_to_dot("rewriter",rewriter.condition)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()