'''
Created on 2015-01-30

@author: levi
'''
import unittest

from UMLRT2Kiltera_MM.transformation.Himesis.HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans import HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans
from solver.prolog_attribute_equation_evaluator import PrologAttributeEquationEvaluator

class Test(unittest.TestCase):


    def testName(self):
        pc = HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans()
        attributeEquationEvaluator = PrologAttributeEquationEvaluator(2)
        attributeEquationEvaluator(pc) 
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()