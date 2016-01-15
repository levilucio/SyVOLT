
#-----------------------------------------------------------------------------
# Auto generated from the DSLTrans transformation and the properties to prove
#-----------------------------------------------------------------------------

import time

from path_condition_generator import PathConditionGenerator
from PyRamify import PyRamify

from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition

from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.ContractProver import ContractProver

from core.himesis_utils import graph_to_dot, load_directory
from util.test_script_utils import select_rules, get_sub_and_super_classes
from util.slicer import Slicer

# imports for properties' atomic contracts

from UMLRT2Kiltera_MM.Properties.HAC1_IsolatedLHS import HAC1_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.HAC1_ConnectedLHS import HAC1_ConnectedLHS
from UMLRT2Kiltera_MM.Properties.HAC1_CompleteLHS import HAC1_CompleteLHS
from UMLRT2Kiltera_MM.Properties.Hprop2_a_IsolatedLHS import Hprop2_a_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.Hprop2_a_ConnectedLHS import Hprop2_a_ConnectedLHS
from UMLRT2Kiltera_MM.Properties.Hprop2_a_CompleteLHS import Hprop2_a_CompleteLHS

from UMLRT2Kiltera_MM.Properties.Hprop2_b_IsolatedLHS import Hprop2_b_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.Hprop2_b_ConnectedLHS import Hprop2_b_ConnectedLHS
from UMLRT2Kiltera_MM.Properties.Hprop2_b_CompleteLHS import Hprop2_b_CompleteLHS


class Prover():


    def do_proof(self,args):

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)





        r0 = 'HMapRootElementRule'
        r1 = 'HState2ProcDef'
        r1_copy = 'HState2ProcDef_copy'
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



        full_transformation = [[r0,],[r1,r1_copy],[r2,],[r3,],[r4,],[r5,],[r6,],[r7,],[r8,],[r9,],[r10,],[r11,],[r12,],[r13,],[r14,],[r15,],[r16,],]

        self.rules, self.transformation = pyramify.get_rules("UMLRT2Kiltera_MM/transformation/Himesis/", full_transformation)

        inputMM = "UMLRT2Kiltera_MM/metamodels/rt_new.ecore"
        outputMM = "UMLRT2Kiltera_MM/metamodels/klt_new.ecore"
        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("UMLRT2Kiltera_MM/transformation/Himesis/", self.transformation)


        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict, dsltransInstallDir = ".")

        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy


        pyramify.set_supertypes(superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)


        # load the contracts, and add polymorphism

        if (args.draw_svg):
                graph_to_dot("property_AC1_isolated", HAC1_IsolatedLHS())
                graph_to_dot("property_AC1_connected", HAC1_ConnectedLHS())
                graph_to_dot("property_AC1_complete", HAC1_CompleteLHS())
                graph_to_dot("property_AC2_isolated", Hprop2_a_IsolatedLHS())
                graph_to_dot("property_AC2_connected", Hprop2_a_ConnectedLHS())
                graph_to_dot("property_AC2_complete", Hprop2_a_CompleteLHS())
                graph_to_dot("property_AC3_isolated", Hprop2_b_IsolatedLHS())
                graph_to_dot("property_AC3_connected", Hprop2_b_ConnectedLHS())
                graph_to_dot("property_AC3_complete", Hprop2_b_CompleteLHS())


        self.atomic_contracts = []
        self.if_then_contracts = []


        isolated = HAC1_IsolatedLHS()
        connected = HAC1_ConnectedLHS()
        complete = HAC1_CompleteLHS()

        isolated["superclasses_dict"] = superclasses_dict
        connected["superclasses_dict"] = superclasses_dict
        complete["superclasses_dict"] = superclasses_dict

        c0 = AtomicContract(isolated, connected, complete)

        self.atomic_contracts.append(("AC1", c0))



        isolated = Hprop2_a_IsolatedLHS()
        connected = Hprop2_a_ConnectedLHS()
        complete = Hprop2_a_CompleteLHS()

        isolated["superclasses_dict"] = superclasses_dict
        connected["superclasses_dict"] = superclasses_dict
        complete["superclasses_dict"] = superclasses_dict

        c1 = AtomicContract(isolated, connected, complete)

        self.atomic_contracts.append(("AC2", c1))

        isolated = Hprop2_b_IsolatedLHS()
        connected = Hprop2_b_ConnectedLHS()
        complete = Hprop2_b_CompleteLHS()

        isolated["superclasses_dict"] = superclasses_dict
        connected["superclasses_dict"] = superclasses_dict
        complete["superclasses_dict"] = superclasses_dict

        c2 = AtomicContract(isolated, connected, complete)

        self.atomic_contracts.append(("AC3", c2))



        if args.slice > 0:
            print("Slicing for contract number " + str(args.slice))
            contract = self.atomic_contracts[args.slice - 1]
            self.new_rules, self.new_transformation = slice_transformation(self.rules, self.transformation, contract, args)


        # generate path conditions
        pc_set = PathConditionGenerator(self.transformation, outputMM, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)

        ts0 = time.time()
        pc_set.build_path_conditions()
        ts1 = time.time()

        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))

        # print path conditions to screen

        if pc_set.num_path_conditions < 300:
            pc_set.print_path_conditions_screen()

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

