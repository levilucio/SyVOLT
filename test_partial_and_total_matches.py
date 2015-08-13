'''
Created on 2013-01-22

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
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):
        
        self.pyramify = PyRamify(verbosity = args.verbosity, draw_svg = args.draw_svg)

        self.transformation_dir = "tests/transformation_multiple_partials/"

        full_transformation = [["Hr11"], ["Hr22"]]

        self.rules, self.transformation = self.pyramify.get_rules(self.transformation_dir, full_transformation)


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

    def test_correct_uml2kiltera(self,args):

        a1 = self.rules["Hr11"]
        b1 = self.rules['Hr22']

        expected_num_pcs = 5
                
        #TODO: Change this number if you are modifying the transformation at all
        if args.num_rules == -1:
                transformation = [[a1],[b1]]#,b1,b3]]

        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]

        subclasses_dict = {}

        subclasses_dict["MT_pre__MetaModelElement_S"] =  ["MT_pre__OPTIONAL1,","MT_pre__PhysicalThread", "MT_pre__PortRef", "MT_pre__PackageContainer", "MT_pre__Thread", "MT_pre__OUT2", "MT_pre__BASE0",\
                            "MT_pre__NamedElement", "MT_pre__Element", "MT_pre__OUT1", "MT_pre__Signal", "MT_pre__Package", "MT_pre__PortType",\
                            "MT_pre__PortConnectorRef", "MT_pre__IN1", "MT_pre__IN0", "MT_pre__LogicalThread", "MT_pre__RoleType", "MT_pre__Vertex",\
                            "MT_pre__SIBLING0", "MT_pre__InitialPoint", "MT_pre__PortConnector", "MT_pre__SignalType", "MT_pre__Transition",\
                            "MT_pre__EntryPoint", "MT_pre__CONJUGATE1", "MT_pre__Protocol", "MT_pre__StateMachine", "MT_pre__Model_S",\
                            "MT_pre__StateMachineElement", "MT_pre__Port", "MT_pre__TransitionType", "MT_pre__Capsule", "MT_pre__Trigger_S",\
                            "MT_pre__State", "MT_pre__PLUGIN2", "MT_pre__Action", "MT_pre__CapsuleRole", "MT_pre__ExitPoint", "MT_pre__FIXED0", "MT_pre__RootElement"]

        subclasses_dict["MT_pre__MetaModelElement_T"] = ["MT_pre__Name", "MT_pre__Module", "MT_pre__ConditionBranch", "MT_pre__Delay", "MT_pre__LocalDef",\
                              "MT_pre__Expr", "MT_pre__ConditionSet", "MT_pre__Proc", "MT_pre__MatchCase", "MT_pre__Match",\
                              "MT_pre__FuncDef", "MT_pre__Null", "MT_pre__Par", "MT_pre__Inst", "MT_pre__Listen", "MT_pre__Site",\
                              "MT_pre__New", "MT_pre__PythonRef", "MT_pre__Def", "MT_pre__Seq", "MT_pre__ParIndexed", "MT_pre__Condition",\
                              "MT_pre__Print", "MT_pre__Pattern", "MT_pre__ListenBranch", "MT_pre__ProcDef", "MT_pre__Trigger_T","MT_pre__Model_T", "MT_pre__RootElement"]

        subclasses_dict["MT_pre__StateMachine"] = ["MT_pre__State"]
   
        self.pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)


#        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlappingRules] = \
#            self.pyramify.ramify_directory("UMLRT2Kiltera_MM/transformation_eq_outside", transformation)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlappingRules, self.subsumption, self.loopingRuleSubsumption] = \
            self.pyramify.ramify_directory("tests/transformation_multiple_partials/", transformation)

        s = PathConditionGenerator(transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlappingRules, self.subsumption, self.loopingRuleSubsumption, args)#
    
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
             
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))
 
        #check if the correct number of path conditions were produced
        if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:
 
            #TODO: Make this an exception
            num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
            print(num_pcs_s)
            #raise Exception(num_pcs_s)
 
        #print("printing path conditions")
        s.print_path_conditions_screen()

        #s.print_path_conditions_file()



    def _print_states(self,s):
        for state in s.symbStateSpace:
            print("----------")
            if state == ():
                print('Empty')
            else:
                for s in state:
                    print(s.name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run the uml to kiltera test.')
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
    parser.set_defaults(compression = 6)

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


    uml2kiltera = Test()
    uml2kiltera.setUp(args)
    uml2kiltera.test_correct_uml2kiltera(args)

    
