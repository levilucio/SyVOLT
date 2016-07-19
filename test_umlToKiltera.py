
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
from util.test_script_utils import select_rules, get_sub_and_super_classes,\
    load_transformation, changePropertyProverMetamodel, set_supertypes, load_contracts
from util.slicer import Slicer
from util.parser import load_parser

class Prover():


    def do_proof(self,args):

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)


        do_handbuilt_transformation = args.handbuilt

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
                                   [r13, r14, r15, r16, ], [r2], [r3, ], ]

            rules_dir = "UMLRT2Kiltera_MM/transformation/no_contains/"

        else:
            r0 = 'HMapRootElementRule'
            r1 = 'HState2ProcDef'
            r2 = 'HBasicState2ProcDef'
            r3 = 'HBasicStateNoOutgoing2ProcDef'
            r4 = 'HCompositeState2ProcDef'
            r5 = 'HState2HProcDef'
            r6 = 'HState2CProcDef'
            r7 = 'HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans'
            r8 = 'HTransition2QInstSIBLING'
            r9 = 'HTransition2QInstOUT'
            r10 = 'HTransition2Inst'
            r11 = 'HTransition2ListenBranch'
            r12 = 'HConnectOutputsOfExitPoint2BProcDefTransition2QInst'
            r13 = 'HTransitionHListenBranch'
            r14 = 'HConnectOPState2CProcDefTransition2InstotherInTransitions'
            r15 = 'HRuleConnect2RootElement'
            r16 = 'HMapHierarchyOfStates2HierarchyOfProcs'

            #full_transformation = [[r0, ], [r1, ], [r2, ], [r3, ], [r4, ], [r5, ], [r6, ], [r7, ], [r8, ], [r9, ],
            #                        [r10, ], [r11, ], [r12, ], [r13, ], [r14, ], [r15, ], [r16, ], ]
            full_transformation = [[r0], [r1, ], [r3, r2, r4, ], [r7, r5, r6, ], [r8, r9, r10, ], \
                                   [r11, r12, r13, r14, ], [r15], [r16, ],]

            rules_dir = "UMLRT2Kiltera_MM/transformation/from_ATL/"




        self.rules, self.transformation = load_transformation(rules_dir, full_transformation)

        # hb = "handbuilt_" if args.handbuilt else ""
        #
        # for layer in self.transformation:
        #     for r in layer:
        #
        #         graph_to_dot("rule_" + hb + r.name, r)

        inputMM = "UMLRT2Kiltera_MM/transformation_for_prunning/metamodels/rt_new.ecore"
        outputMM = "UMLRT2Kiltera_MM/transformation_for_prunning/metamodels/klt_new.ecore"
        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory(rules_dir, self.transformation)

        #raise Exception()

        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict, dsltransInstallDir = ".")

        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy


        set_supertypes(superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)

        # load the contracts

        contracts = load_directory("UMLRT2Kiltera_MM/Properties/from_thesis/")

        atomic_contracts = [
            "PP1",
            "PP2",
            "PP3",
            "PP4",
            # #"PP5",
        ]

        if args.contract >=0 and args.contract <= 3:
            atomic_contracts = atomic_contracts[args.contract:args.contract+1]
        elif args.contract >= 0:
            atomic_contracts = []

        if_then_contracts = [
            ["MM5_if", "MM5_then"],
            ["MM6_if", "MM6_then"],
            ["MM7_if", "MM7_then"],
            ["MM11_if", "MM11_then"],
            ["SS1_if", "SS1_then"],

            #skip this one
            # #["SS2_if", "SS2_then"],

            #["SS3_if1", "SS3_then1"],
            #["SS3_if2", "SS3_then2"],
        ]

        if args.contract >= 4 and args.contract <= 8:
            args.contract -= 4
            if_then_contracts = if_then_contracts[args.contract:args.contract + 1]
        elif args.contract >= 0:
            if_then_contracts = []

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

            #skip this one
            #  #[["SS3_if1", "SS3_if2", "NOT", "AND"], ["SS3_then1", "SS3_then2", "NOT", "AND"]],
        ]
        if args.contract >= 9 and args.contract <= 15:
            args.contract -= 9
            prop_if_then_contracts = prop_if_then_contracts[args.contract:args.contract + 1]
        elif args.contract >= 0:
            prop_if_then_contracts = []

        # if args.contract > -1:
        #     prop_if_then_contracts = prop_if_then_contracts[args.contract:args.contract+1]
            #print(prop_if_then_contracts)


        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, superclasses_dict,
                                                                       atomic_contracts, if_then_contracts,
                                                                       prop_if_then_contracts,
                                                                       args.draw_svg)


        slicer = Slicer(self.rules, self.transformation, superclasses_dict)
        if args.slice >= 0:
            print("Slicing for contract number " + str(args.slice))
            contract = None

            if_then_slice = args.slice - len(self.atomic_contracts)

            if args.slice >= 0 and args.slice <= len(self.atomic_contracts) -1:
                contract = self.atomic_contracts[args.slice]
                self.atomic_contracts = [contract]
                self.if_then_contracts = []
            elif if_then_slice >= 0 and if_then_slice <= len(self.if_then_contracts) - 1:
                contract = self.if_then_contracts[if_then_slice]
                self.atomic_contracts = []
                self.if_then_contracts = [contract]

            print("Number rules before: " + str(len(self.rules)))
            self.rules2, self.transformation2 = slicer.slice_transformation(contract)
            # for l in self.transformation:
            #     for r in l:
            #         print(r.name)
            #     print("---")
            # print("==============")
            # for l in self.transformation2:
            #     for r in l:
            #         print(r.name)
            #     print("---")

            raise Exception()
            print("Number rules after: " + str(len(self.rules)))

            # import sys
            # sys.exit()


        # generate path conditions
        pc_set = PathConditionGenerator(self.transformation, outputMM, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)

        ts0 = time.time()
        pc_set.build_path_conditions()
        ts1 = time.time()


        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))

        # print path conditions to screen

        #if pc_set.num_path_conditions < 300:
        #pc_set.print_path_conditions_screen()
        #pc_set.print_path_conditions_file()

        # now actually prove these contracts
        
        contract_prover = ContractProver()

        contract_prover.prove_contracts(pc_set, self.atomic_contracts, self.if_then_contracts)
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))
        print("Number rules after: " + str(len(self.rules)))

if __name__ == "__main__":

    parser = load_parser()
    args = parser.parse_args()

    prover = Prover()
    prover.do_proof(args)

