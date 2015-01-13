'''
Created on 2015-01-13

@author: levi
'''
import unittest
from pyswip import Prolog


class Test(unittest.TestCase):


    def testName(self):
        prolog = Prolog()
        prolog.assertz("father(michael,john)")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()