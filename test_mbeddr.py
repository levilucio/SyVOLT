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



class Test():

    def setUp(self, args):
        pyramify = PyRamify(draw_svg=args.draw_svg)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("mbeddr2C_MM/real_transformation")

        #print("Rules: " + str(self.rules.keys()))


    def test_correct_mbeddr(self, args):

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
        b14 = self.rules['Hlayer1rule14']
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

        expected_num_pcs = args.num_pcs
        transformation = [[a0,a1,a2,a3,a4,a5,a6, a7, a8, a9, a10, a11]]#,[b0, b1, b2, b3,b4,b5,b6,b7,b8, b9, b10, b11, b12, b13,b14,b15]]#,[c0,c1,c2,c3],[d0,d1,d2,d3,d4,d5]]
          
        pre_metamodel = ["MT_pre__mbeddr_MM", "MoTifRule"]
        post_metamodel = ["MT_post__mbeddr", "MoTifRule"]
        
        eu1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore") 
        subclasses_source = buildPreListFromClassNames(eu1.getMetamodelClassNames())
        eu2 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/C.ecore") 
        subclasses_target = buildPreListFromClassNames(eu2.getMetamodelClassNames())
   
        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)
 
        s = PathConditionGenerator(transformation, self.ruleCombinators,
                                   self.ruleTraceCheckers, self.matchRulePatterns, 2, draw_svg = args.draw_svg, run_tests = args.run_tests)
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
             
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(len(s.pathConditionSet)))

        # check if the correct number of path conditions were produced
        if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == len(s.pathConditionSet):
            #TODO: Make this an exception
            num_pcs_s = "The number of produced path conditions is incorrect.\n" + args.num_pcs + " were expected, but " + str(
                len(s.pathConditionSet)) + " were produced."
            print(num_pcs_s)
            #raise Exception(num_pcs_s)

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
    import argparse

    parser = argparse.ArgumentParser(description = 'Run the mbeddr test.')
    parser.add_argument('--run_tests', type = bool, default = True,
                        help = 'Bool for whether extra testing should be performed (default: True)')
    parser.add_argument('--draw_svg', type=bool, default = True,
                        help = 'Bool for whether svg files should be drawn (default: True)')
    parser.add_argument('--num_pcs', default = -1,
                        help = 'Number of path conditions which should be produced by this test (default: -1)')

    args = parser.parse_args()

    mbeddr = Test()
    mbeddr.setUp(args)
    mbeddr.test_correct_mbeddr(args)
    
