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

        self.rules = pyramify.get_rules("mbeddr2C_MM/real_transformation")

        # print("Rules: " + str(self.rules.keys()))

    def select_rules(self, full_transformation, num_rules):
        selected_transformation = []

        print("Selecting " + str(num_rules) + " rules")

        i = 1
        for layer in range(len(full_transformation)):
            selected_transformation.append([])
            for rule in full_transformation[layer]:
                selected_transformation[layer].append(rule)
                i += 1
                if i > num_rules:
                    print("Returning: " + str(selected_transformation))
                    return selected_transformation


    def test_correct_mbeddr(self, args):
        pyramify = PyRamify(verbosity = 0, draw_svg = args.draw_svg)

        a0 = self.rules['Hlayer0rule0']
        a1 = self.rules['Hlayer0rule1']
        a2 = self.rules['Hlayer0rule2']
        a3 = self.rules['Hlayer0rule3']
        a4 = self.rules['Hlayer0rule4']
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
    
#        c0 = self.rules['Hlayer2rule0']
        c1 = self.rules['Hlayer2rule1']
        c2 = self.rules['Hlayer2rule2']
        c3 = self.rules['Hlayer2rule3']
     
        d0 = self.rules['Hlayer3rule0']
        d1 = self.rules['Hlayer3rule1']
        d2 = self.rules['Hlayer3rule2']
        d3 = self.rules['Hlayer3rule3']
        d4 = self.rules['Hlayer3rule4']
        d5 = self.rules['Hlayer3rule5']
              
        e0 = self.rules['Hlayer4rule0']
        e1 = self.rules['Hlayer4rule1']
        e2 = self.rules['Hlayer4rule2']
        e3 = self.rules['Hlayer4rule3']
     
        f0 = self.rules['Hlayer5rule0']
        f1 = self.rules['Hlayer5rule1']
        f2 = self.rules['Hlayer5rule2']
        f3 = self.rules['Hlayer5rule3']
        f4 = self.rules['Hlayer5rule4']
        f5 = self.rules['Hlayer5rule5']
#              
#         g0 = self.rules['Hlayer6rule0']        

        expected_num_pcs = args.num_pcs

        if args.num_rules == -1:
            # change this to select by hand the number of rules to execute
            transformation = [[a0, a1, a2, a3, a4, a6, a7, a8, a9, a10, a11], [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15],\
            [c1, c2, c3], [d0, d4, d3, d2, d1, d5], [e0, e2, e1, e3], [f0, f1, f2, f3, f4, f5]]
#            transformation = [[b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]]#,\

#         else:
#             transformation = self.select_rules([[a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]])#,[b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15],\
            #[c0, c1, c2, c3], [d0, d1, d2, d3, d4, d5], [e0, e1, e2, e3], [f0, f1, f2, f3, f4, f5], [g0]], args.num_rules)


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
            pyramify.ramify_directory("mbeddr2C_MM/real_transformation", transformation)

        s = PathConditionGenerator(transformation, self.ruleCombinators,
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
    
