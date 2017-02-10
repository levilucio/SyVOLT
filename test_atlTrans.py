'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time
import sys

from path_condition_generator import PathConditionGenerator
from PropertyVerification.v2.ContractProver import ContractProver

from t_core.matcher import Matcher
from t_core.messages import Packet

from pyramify.PyRamify import PyRamify

from util.test_script_utils import select_rules, get_sub_and_super_classes,\
    load_transformation, changePropertyProverMetamodel, set_supertypes, load_contracts
from util.slicer import Slicer

from core.himesis_utils import graph_to_dot, load_directory
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules



from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):

        full_transformation = [
            ['HRootRule'],
            ['HMotherRule',
            'HFatherRule',
            'HSonRule',
            'HDaughterRule'],
            ['HUnionMotherRule',
            'HUnionManRule',
            'HUnionDaughterRule',
            'HUnionSonRule']
        ]
        self.rules, self.transformation = load_transformation("ATLTrans/w_equations/", full_transformation)


        inputMM = "ATLTrans/metamodels/Household.ecore"
        outputMM = "ATLTrans/metamodels/Community.ecore"

        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        pre_metamodel = ["MT_pre__FamiliesToPersons_MM", "MoTifRule"]
        post_metamodel = ["MT_post__FamiliesToPersons_MM", "MoTifRule"]

        changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict)


        #load the contracts



        # also make sure the transformation has this information
        for rule in self.rules.values():
            rule["superclasses_dict"] = superclasses_dict

        for layer in self.transformation:
            for rule in layer:
                rule["superclasses_dict"] = superclasses_dict


        # load the contracts

        contracts = load_directory("ATLTrans/props/")

        atomic_contracts = [
            #"daughterMother",
            #"fourMembers",
            #"motherFather",
        ]
        if_then_contracts = [
            # ["S1_if", "S1_then"],
        ]
        if_then_contracts += [
            # structure is 'if graph', 'then graph'
            # where the 'then graph' is made up of reverse polish notation
            ["CommunityPerson_if", ["CommunityPerson_then", "NOT"]],
        ]

        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, superclasses_dict,
                                                                       atomic_contracts, if_then_contracts,
                                                                       prop_if_then_contracts,
                                                                       args.draw_svg)


        if args.slice > 0:
            contract = self.atomic_contracts[args.slice - 1]
            print("Slicing for contract number " + str(args.slice) + " : " + contract[0])

            slicer = Slicer(self.rules, self.transformation)

            print("Number rules before: " + str(len(self.rules)))
            self.new_rules, self.new_transformation = slicer.slice_transformation(contract)
            print("Number rules after: " + str(len(self.rules)))


    def test_correct_uml2kiltera(self,args):

#'HMapHeirarchyOfStates2HeirarchyOfProcs':  'HTransition2QInstSIBLING': < 'HState2HProcDef': 'HCompositeState2ProcDef':  'HTransition2ListenBranch':  'HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans':  'HBasicStateNoOutgoing2ProcDef':  'HBasicState2ProcDef': , 'HState2ProcDef'

#Layer1: State2ProcDef
#Layer2: BasicStateNoOutgoing2ProcDef, BasicState2ProcDef, CompositeState2ProcDef
#Layer3: ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, State2HProcDef
#Layer4: Transition2QInstSIBLING
#Layer5: Transition2ListenBranch
#Layer6: MapHeirarchyOfStates2HeirarchyOfProcs

#         a1 = self.rules['HState2ProcDef']
#         b1 = self.rules['HBasicStateNoOutgoing2ProcDef']
#         b2 = self.rules['HBasicState2ProcDef']
#         b3 = self.rules['HCompositeState2ProcDef']

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)



        #get the expected num from the args
        #expected_num_pcs = args.num_pcs
        expected_num_pcs = 330
                
        #TODO: Change this number if you are modifying the transformation at all



        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ATLTrans/w_equations/", self.transformation)



        s = PathConditionGenerator(self.transformation, "ATLTrans/metamodels/Community.ecore", self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)#

        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()

        print(s.num_path_conditions)

        pc_time = ts1 - ts0
        print("\n\nTime to build the set of path conditions: " + str(pc_time))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))

        #check if the correct number of path conditions were produced
        if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:

            #TODO: Make this an exception
            num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
            print(num_pcs_s)
            #raise Exception(num_pcs_s)
 
        #print("printing path conditions")
        #s.print_path_conditions_screen()

        #raise Exception()

        #s.print_path_conditions_file()

        
        print("\nContract proving:")
  
        s.verbosity = 0
  
        contract_prover = ContractProver()
  
        contract_prover.prove_contracts(s, self.atomic_contracts, self.if_then_contracts)


def _print_states(self, s):
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

    parser.add_argument('--slice', type = int, default = 0,
                        help = 'Index of contract to slice for. Range: 0 (no slicing) to #CONTRACTS (default: 0)')
    parser.set_defaults(slice = 0)


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

    
