
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

from ER_Copier_MM.properties.HERCopierProp_IsolatedLHS import HERCopierProp_IsolatedLHS
from ER_Copier_MM.properties.HERCopierProp_ConnectedLHS import HERCopierProp_ConnectedLHS
from ER_Copier_MM.properties.HERCopierProp_CompleteLHS import HERCopierProp_CompleteLHS


class Prover():


    def do_proof(self,args):    

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        

        r0 = 'HERModel'
        r1 = 'HEntityType'
        r2 = 'HAttribute'
        r3 = 'HWeakReference'
        r4 = 'HStrongReference'
        r5 = 'HermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType'
        r6 = 'HentitytypeOUTfeaturesSolveRefEntityTypeFeatureEntityTypeFeature'
        r7 = 'HweakreferenceOUTtypeSolveRefWeakReferenceEntityTypeWeakReferenceEntityType'
        r8 = 'HstrongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType'
    
        
                             
        full_transformation = [[r0,],[r1,],[r2,],[r3,],[r4,],[r5,],[r6,],[r7,],[r8,],]
        
        self.rules, self.transformation = pyramify.get_rules("ER_Copier_MM/transformation", full_transformation)
        
        inputMM = "ER_Copier_MM/ER_MM.ecore"
        outputMM = "ER_Copier_MM/ER_MM_copy.ecore"
        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ER_Copier_MM/transformation", self.transformation)

                
        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict, dsltransInstallDir = "/home/dcx/Projects/SyVOLT")
        
        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy
                                                                  
        
        pyramify.set_supertypes(superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)

            
        # load the contracts, and add polymorphism

        if (args.draw_svg): 
                graph_to_dot("property_ERCopierProp_isolated", HERCopierProp_IsolatedLHS())
                graph_to_dot("property_ERCopierProp_connected", HERCopierProp_ConnectedLHS())
                graph_to_dot("property_ERCopierProp_complete", HERCopierProp_CompleteLHS())
       

        self.atomic_contracts = []
        self.if_then_contracts = []
        
        
        isolated = HERCopierProp_IsolatedLHS()
        connected = HERCopierProp_ConnectedLHS()
        complete = HERCopierProp_CompleteLHS()
        
        isolated["superclasses_dict"] = superclasses_dict 
        connected["superclasses_dict"] = superclasses_dict 
        complete["superclasses_dict"] = superclasses_dict 
        
        c0 = AtomicContract(isolated, connected, complete)
        
        self.atomic_contracts.append(("ERCopierProp", c0))

        graph_to_dot("ERCopierProp", complete)
        
          
        
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
        