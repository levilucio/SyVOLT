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

from core.himesis_utils import graph_to_dot

from ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames
from util.select_rules import select_rules

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.state_property import StateProperty
from PropertyVerification.atomic_state_property import AtomicStateProperty
from PropertyVerification.and_state_property import AndStateProperty
from PropertyVerification.or_state_property import OrStateProperty
from PropertyVerification.not_state_property import NotStateProperty
from PropertyVerification.implication_state_property import ImplicationStateProperty
from PropertyVerification.Not import Not  # StateSpace Prop
from PropertyVerification.Implication import Implication  # StateSpace Prop
from PropertyVerification.And import And  # StateSpace Prop
from PropertyVerification.Or import Or  # StateSpace Prop
from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
# from lib2to3.fixer_util import p1



class Test():
    def setUp(self, args):
        pyramify = PyRamify(draw_svg = args.draw_svg)



        full_transformation = [

            ['Hlayer0rule0',
            'Hlayer0rule1',
            'Hlayer0rule2',
            'Hlayer0rule3',
            'Hlayer0rule4',
            'Hlayer0rule6',
            'Hlayer0rule7',
            'Hlayer0rule8',
            'Hlayer0rule9',
            'Hlayer0rule10',
            'Hlayer0rule11'],

            ['Hlayer1rule0',
            'Hlayer1rule1',
            'Hlayer1rule2',
            'Hlayer1rule3',
            'Hlayer1rule4',
            'Hlayer1rule5',
            'Hlayer1rule6',
            'Hlayer1rule7',
            'Hlayer1rule8',
            'Hlayer1rule9',
            'Hlayer1rule10',
            'Hlayer1rule11',
            'Hlayer1rule12',
            'Hlayer1rule13',
            'Hlayer1rule14',
            'Hlayer1rule15'],

    #        'Hlayer2rule0']
            ['Hlayer2rule1',
            'Hlayer2rule2',
            'Hlayer2rule3'],

            ['Hlayer3rule0',
            'Hlayer3rule1',
            'Hlayer3rule2',
            'Hlayer3rule3',
            'Hlayer3rule4',
            'Hlayer3rule5'],

            ['Hlayer4rule0',
            'Hlayer4rule1',
            'Hlayer4rule2',
            'Hlayer4rule3'],

            ['Hlayer5rule0',
            'Hlayer5rule1',
            'Hlayer5rule2',
            'Hlayer5rule3',
            'Hlayer5rule4',
            'Hlayer5rule5']



        ]

        self.rules, self.transformation = pyramify.get_rules("mbeddr2C_MM/real_transformation", full_transformation)

        # print("Rules: " + str(self.rules.keys()))


    def test_correct_mbeddr(self, args):
        pyramify = PyRamify(verbosity = 0, draw_svg = args.draw_svg)


#              
#         g0 = self.rules['Hlayer6rule0']        

        expected_num_pcs = args.num_pcs



        pre_metamodel = ["MT_pre__mbeddr_MM", "MoTifRule"]
        post_metamodel = ["MT_post__mbeddr", "MoTifRule"]

        subclasses_dict = {}
        eu1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
        subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(eu1.getMetamodelClassNames())
        eu2 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/C.ecore")
        subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(eu2.getMetamodelClassNames())

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("mbeddr2C_MM/real_transformation", self.transformation)

        s = PathConditionGenerator(self.transformation, self.ruleCombinators,
                                   self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
   
        pc_time = ts1 - ts0
        print("\n\nTime to build the set of path conditions: " + str(pc_time))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))
         
        s.check_rule_reachability()

#        s.print_path_conditions_screen()
# 
#         # check if the correct number of path conditions were produced
#         if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == len(s.pathConditionSet):
#             # TODO: Make this an exception
#             num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(
#                 expected_num_pcs) + " were expected, but " + str(
#                 len(s.pathConditionSet)) + " were produced."
#             print(num_pcs_s)
#             # raise Exception(num_pcs_s)

        # print("printing path conditions")
        #s.print_path_conditions_screen()
        #
        # s.print_path_conditions_file()



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description = 'Run the mbeddr test.')

    parser.add_argument('--skip_tests', dest = 'run_tests', action = 'store_false',
                        help = 'Option to skip the running of matching tests')
    parser.set_defaults(run_tests = True)

    parser.add_argument('--skip_parallel', dest = 'do_parallel', action = 'store_false',
                        help = 'Option to force computation to run single-thread')
    parser.set_defaults(do_parallel = True)

    parser.add_argument('--skip_pickle', dest = 'do_pickle', action = 'store_false',
                        help = 'Option to skip the use of pickling')
    parser.set_defaults(do_pickle = True)

    parser.add_argument('--compression', type = int, default = 6,
                        help = 'Level of compression to use with pickling. Range: 0 (no compression) to 9 (high compression) (default: 6)')
    parser.set_defaults(compression = True)

    parser.add_argument('--no_svg', dest = 'draw_svg', action = 'store_false',
                        help = 'Flag to force svg files to not be drawn')
    parser.set_defaults(draw_svg = True)

    parser.add_argument('--num_pcs', type = int, default = -1,
                        help = 'Number of path conditions which should be produced by this test (default: -1)')

    parser.add_argument('--num_rules', type = int, default = -1,
                        help = 'Number of rules in the transformation (default: -1)')

    parser.add_argument('--verbosity', type = int, default = 0,
                        help = 'Verbosity level (default: 0 - minimum output)')

    args = parser.parse_args()

    mbeddr = Test()
    mbeddr.setUp(args)
    mbeddr.test_correct_mbeddr(args)
    
