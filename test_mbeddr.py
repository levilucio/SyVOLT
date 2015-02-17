'''
Created on 2015-02-14

@author: levi
'''


import unittest
import time
import sys

from path_condition_generator import PathConditionGenerator

from t_core.matcher import Matcher
from t_core.messages import Packet

from PyRamify import PyRamify

from himesis_utils import graph_to_dot

from ecore_utils import EcoreUtils
from himesis_plus import buildPreListFromClassNames

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.state_property import StateProperty
from PropertyVerification.atomic_state_property import AtomicStateProperty
from PropertyVerification.and_state_property import AndStateProperty
from PropertyVerification.or_state_property import OrStateProperty
from PropertyVerification.not_state_property import NotStateProperty
from PropertyVerification.implication_state_property import ImplicationStateProperty
from PropertyVerification.Not import Not #StateSpace Prop
from PropertyVerification.Implication import Implication #StateSpace Prop
from PropertyVerification.And import And #StateSpace Prop
from PropertyVerification.Or import Or #StateSpace Prop
from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
#from lib2to3.fixer_util import p1



class Test(unittest.TestCase):

    def setUp(self):
        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("mbeddr2C_MM/real_transformation")

        print("Rules: " + str(self.rules.keys()))


    def test_correct_uml2kiltera(self):

        pyramify = PyRamify(verbosity = 2)

        a0 = self.rules['Hlayer0rule0']
        a1 = self.rules['Hlayer0rule1']
        a2 = self.rules['Hlayer0rule2']
        a3 = self.rules['Hlayer0rule3']
        a4 = self.rules['Hlayer0rule4']
        a5 = self.rules['Hlayer0rule5']
        a6 = self.rules['Hlayer0rule6']
        a7 = self.rules['Hlayer0rule7']
        a8 = self.rules['Hlayer0rule8']
        a9 = self.rules['Hlayer0rule9']
        a10 = self.rules['Hlayer0rule10']
        a11 = self.rules['Hlayer0rule11']

        b0 = self.rules['Hlayer1rule0']
        b1 = self.rules['Hlayer1rule1']
        b2 = self.rules['Hlayer1rule2']
        b3 = self.rules['Hlayer1rule3']
        b4 = self.rules['Hlayer1rule4']
        b5 = self.rules['Hlayer1rule5']
        b6 = self.rules['Hlayer1rule6']
        b7 = self.rules['Hlayer1rule7']
        b8 = self.rules['Hlayer1rule8']
        b9 = self.rules['Hlayer1rule9']
        b10 = self.rules['Hlayer1rule10']
        b11 = self.rules['Hlayer1rule11']
        b12 = self.rules['Hlayer1rule12']
        b13 = self.rules['Hlayer1rule13']
        b15 = self.rules['Hlayer1rule14']
        b15 = self.rules['Hlayer1rule15']

        c0 = self.rules['Hlayer2rule0']
        c1 = self.rules['Hlayer2rule1']
        c2 = self.rules['Hlayer2rule2']
        c3 = self.rules['Hlayer2rule3']

        d0 = self.rules['Hlayer3rule0']
        d1 = self.rules['Hlayer3rule1']
        d2 = self.rules['Hlayer3rule2']
        d3 = self.rules['Hlayer3rule3']
        d4 = self.rules['Hlayer3rule4']
        d5 = self.rules['Hlayer3rule5']
            
        transformation = [[a0,a1,a2,a3,a4,a5,a6],[b3,b4,b5,b6,b7,b8],[c0,c1,c2,c3],[d0,d1,d2,d3,d4,d5]]
          
        pre_metamodel = ["MT_pre__mbeddr_MM", "MoTifRule"]
        post_metamodel = ["MT_post__mbeddr", "MoTifRule"]
        
        eu1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore") 
        subclasses_source = buildPreListFromClassNames(eu1.getMetamodelClassNames())
        eu2 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/C.ecore") 
        subclasses_target = buildPreListFromClassNames(eu2.getMetamodelClassNames())
   
        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)
 
        s = PathConditionGenerator(transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, 2)
    
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
             
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(len(s.pathConditionSet)))
#         print("printing path conditions")
#         s.print_path_conditions_screen()
#          
#        s.print_path_conditions_file()



    def _print_states(self,s):
        for state in s.symbStateSpace:
            print "----------"
            if state == ():
                print 'Empty'
            else:
                for s in state:
                    print s.name


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
    