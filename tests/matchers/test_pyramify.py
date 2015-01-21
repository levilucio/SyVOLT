'''
Created on 2015-01-20

@author: levi
'''
import unittest

from PyRamify import PyRamify

class Test(unittest.TestCase):


    def testRamify(self):
        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("dir_for_pyramify/", True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()