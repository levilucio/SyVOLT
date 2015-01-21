'''
Created on 2015-01-20

@author: levi
'''
import unittest
from himesis_utils import graph_to_dot

from tests.TestModules.Hlayer3rule0 import Hlayer3rule0

class Test(unittest.TestCase):


    def testClaudioRules(self):
        rule = Hlayer3rule0()
        
        for v in rule.vs():
            print v

        for e in rule.es():
            print e
        graph_to_dot("claudio", rule)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()