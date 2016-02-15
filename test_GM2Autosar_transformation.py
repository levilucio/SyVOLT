
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

        do_old_transformation = True

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        
        if do_old_transformation:
            r0 = 'HMapPN2FiveElements'
            r1 = 'HMapPartition'
            r2 = 'HMapModule'
            r3 = 'HConnECU2VirtualDevice1'
            r4 = 'HConnVirtualDevice2Distributable1'
            r5 = 'HConnectPPortPrototype'
            r6 = 'HConnectRPortPrototype'
            r7 = 'HConnVirtualDevice2Distributable2'
            r8 = 'HConnECU2VirtualDevice2'

            full_transformation = [[r0, r1, r2, ], [r3, ], [r4, ], [r7, ], [r8, ], [r5, r6, ], ]

            rule_dir = "GM2AUTOSAR_MM/transformation"

        else:
            r0 = 'HcreateComponent'
            r1 = 'HinitSysTemp'
            r2 = 'HinitSingleSwc2EcuMapping'
            r3 = 'HsysmappingswMappingSolveRefPhysicalNodePartitionSystemMappingSwcToEcuMapping'
            r4 = 'HcompostypecomponentSolveRefPhysicalNodePartitionModuleCompositionTypeComponentPrototype'
            r5 = 'HcompostypeportSolveRefPhysicalNodePartitionModuleSchedulerServiceCompositionTypePPortPrototype'
            r6 = 'HcompostypeportSolveRefPhysicalNodePartitionModuleSchedulerServiceCompositionTypeRPortPrototype'
            r7 = 'HmappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent'
            r8 = 'HmappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance'
            full_transformation = [[r0,],[r1,r2,],[r3,],[r4,],[r5,],[r6,],[r7,],[r8,],]

            rule_dir = "GM2AUTOSAR_MM/transformation_from_ATL/"
        
        self.rules, self.transformation = pyramify.get_rules(rule_dir, full_transformation)
        
        inputMM = "GM2AUTOSAR_MM/metamodels/Industrial.ecore"
        outputMM = "GM2AUTOSAR_MM/metamodels/Autosar.ecore"
        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory(rule_dir, self.transformation)

        for layer in self.transformation:
            for r in layer:
                graph_to_dot("rule_" + r.name, r)
                
        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict, dsltransInstallDir = "/home/dcx/Projects/SyVOLT")
        
        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy
                                                                  
        
        pyramify.set_supertypes(superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)


        # load the contracts

        contracts = load_directory("GM2AUTOSAR_MM/Properties/from_eclipse/")

        atomic_contracts = [
            "P1",
            #"P2",
        ]
        if_then_contracts = [
            #["S1_if", "S1_then"],
            #["M1_if", "M1_then"],
            #["M3_if", "M3_then"],
        ]
        prop_if_then_contracts = [
            #structure is 'if graph', 'then graph'
            #where the 'then graph' is made up of reverse polish notation
            # ["M2_if", ["M2_then1", "M2_then2", "NOT", "AND"]],
            # ["M4_if", ["M4_then1", "M4_then2", "NOT", "AND"]],
            # ["M5_if", ["M5_then1", "M5_then2", "NOT", "AND"]],
            # ["M6_if", ["M6_then1", "M6_then2", "NOT", "AND"]],

        ]

        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, superclasses_dict,
                                                                       atomic_contracts, if_then_contracts, prop_if_then_contracts,
                                                                       args.draw_svg)
        
        if args.slice > 0:
            print("Slicing for contract number " + str(args.slice))
            contract = self.atomic_contracts[args.slice - 1]
            slicer = Slicer(self.rules, self.transformation)

            print("Number rules before: " + str(len(self.rules)))
            self.rules, self.transformation = slicer.slice_transformation(contract)
            print("Number rules after: " + str(len(self.rules)))
            
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
        