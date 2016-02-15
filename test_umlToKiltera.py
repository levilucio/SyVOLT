
#-----------------------------------------------------------------------------
# Auto generated from the DSLTrans transformation and the properties to prove
#-----------------------------------------------------------------------------

import time

from path_condition_generator import PathConditionGenerator
from pyramify.PyRamify import PyRamify

from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition

from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.ContractProver import ContractProver

from core.himesis_utils import graph_to_dot, load_directory
from util.test_script_utils import select_rules, get_sub_and_super_classes, load_contracts
from util.slicer import Slicer

class Prover():


    def do_proof(self,args):

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)


        do_handbuilt_transformation = True

        if do_handbuilt_transformation:
            r0 = 'HState2ProcDef'
            r1 = 'HMapRootElementRule'
            r2 = 'HRuleConnect2RootElement'
            r3 = 'HMapHeirarchyOfStates2HeirarchyOfProcs'
            r4 = 'HBasicStateNoOutgoing2ProcDef'
            r5 = 'HBasicState2ProcDef'
            r6 = 'HCompositeState2ProcDef'
            r7 = 'HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans'
            r8 = 'HState2HProcDef'
            r9 = 'HState2CProcDef'
            r10 = 'HTransition2QInstSIBLING'
            r11 = 'HTransition2QInstOUT'
            r12 = 'HTransition2Inst'
            r13 = 'HTransition2ListenBranch'
            r14 = 'HConnectOutputsOfExitPoint2BProcDefTransition2QInst'
            r15 = 'HTransition2HListenBranch'
            r16 = 'HConnectOPState2CProcDefTransition2InstotherInTransitions'

            full_transformation = [[r1, ], [r0, ], [r4, r5, r6, ], [r7, r8, r9, ], [r10, r11, r12, ],
                                   [r13, r14, r15, r16, ], [r2, r3, ], ]

            rules_dir = "UMLRT2Kiltera_MM/transformation/handbuilt/"

        else:
            r0 = 'HState2ProcDef'
            r1 = 'HMapRootElementRule'
            r2 = 'HRuleConnect2RootElement'
            r3 = 'HMapHeirarchyOfStates2HeirarchyOfProcs'
            r4 = 'HBasicStateNoOutgoing2ProcDef'
            r5 = 'HBasicState2ProcDef'
            r6 = 'HCompositeState2ProcDef'
            r7 = 'HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans'
            r8 = 'HState2HProcDef'
            r9 = 'HState2CProcDef'
            r10 = 'HTransition2QInstSIBLING'
            r11 = 'HTransition2QInstOUT'
            r12 = 'HTransition2Inst'
            r13 = 'HTransition2ListenBranch'
            r14 = 'HConnectOutputsOfExitPoint2BProcDefTransition2QInst'
            r15 = 'HTransition2HListenBranch'
            r16 = 'HConnectOPState2CProcDefTransition2InstotherInTransitions'

            full_transformation = [[r1, ], [r0, ], [r4, r5, r6, ], [r7, r8, r9, ], [r10, r11, r12, ],
                                   [r13, r14, r15, r16, ], [r2, r3, ], ]
            rules_dir = "UMLRT2Kiltera_MM/transformation/from_ATL/"

        self.rules, self.transformation = pyramify.get_rules(rules_dir, full_transformation)


        inputMM = "UMLRT2Kiltera_MM/transformation_for_prunning/metamodels/rt_new.ecore"
        outputMM = "UMLRT2Kiltera_MM/transformation_for_prunning/metamodels/klt_new.ecore"
        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory(rules_dir, self.transformation)


        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict, dsltransInstallDir = ".")

        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy


        pyramify.set_supertypes(superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)

        # load the contracts

        contracts = load_directory("UMLRT2Kiltera_MM/Properties/from_thesis/")

        atomic_contracts = [
            "PP1",
            "PP2",
            "PP3",
            "PP4",
            "PP5",
        ]
        if_then_contracts = [
            ["MM5_if", "MM5_then"],
            ["MM6_if", "MM6_then"],
            ["MM7_if", "MM7_then"],
            ["MM11_if", "MM11_then"],
            ["SS1_if", "SS1_then"],
            ["SS2_if", "SS2_then"],
        ]
        prop_if_then_contracts = [
            # structure is 'if graph', 'then graph'
            # where the 'then graph' is made up of reverse polish notation
            ["MM1_if", ["MM1_then1", "MM1_then2", "NOT", "AND"]],
            ["MM2_if", ["MM2_then1", "MM2_then2", "NOT", "AND"]],
            ["MM3_if", ["MM3_then1", "MM3_then2", "NOT", "AND"]],
            ["MM4_if", ["MM4_then1", "MM4_then2", "NOT", "AND"]],

            ["MM8_if", ["MM8_then1", "MM8_then2", "NOT", "AND", "MM8_then1", "NOT", "OR"]],
            ["MM9_if", ["MM9_then1", "MM9_then2", "NOT", "AND", "MM9_then1", "NOT", "OR"]],
            ["MM10_if", ["MM10_then1", "MM10_then2", "NOT", "AND", "MM10_then1", "NOT", "OR"]],

            [["SS3_if1", "SS3_if2", "NOT", "AND"], ["SS3_then1", "SS3_then2", "NOT", "AND"]],
        ]

        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, superclasses_dict,
                                                                       atomic_contracts, if_then_contracts,
                                                                       prop_if_then_contracts,
                                                                       args.draw_svg)

        slicer = Slicer(self.rules, self.transformation)
        if args.slice > 0:
            print("Slicing for contract number " + str(args.slice))
            contract = self.atomic_contracts[args.slice - 1]
            self.new_rules, self.new_transformation = slicer.slice_transformation(contract)


        # generate path conditions
        pc_set = PathConditionGenerator(self.transformation, outputMM, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)

        # import sys
        # sys.exit()
        ts0 = time.time()
        pc_set.build_path_conditions()
        ts1 = time.time()


        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))

        # print path conditions to screen

        #if pc_set.num_path_conditions < 300:
        #pc_set.print_path_conditions_screen()


        # now actually prove these contracts

        contract_prover = ContractProver()

        contract_prover.prove_contracts(pc_set, self.atomic_contracts, self.if_then_contracts)
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run the ecore_copier test.')

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


    prover = Prover()
    prover.do_proof(args)

