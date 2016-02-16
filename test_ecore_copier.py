
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

from ECore_Copier_MM.properties.positive.HProp1_IsolatedLHS import HProp1_IsolatedLHS
from ECore_Copier_MM.properties.positive.HProp1_ConnectedLHS import HProp1_ConnectedLHS
from ECore_Copier_MM.properties.positive.HProp1_CompleteLHS import HProp1_CompleteLHS

from ECore_Copier_MM.properties.positive.HEC_prop2_IsolatedLHS import HEC_prop2_IsolatedLHS
from ECore_Copier_MM.properties.positive.HEC_prop2_ConnectedLHS import HEC_prop2_ConnectedLHS
from ECore_Copier_MM.properties.positive.HEC_prop2_CompleteLHS import HEC_prop2_CompleteLHS

class Prover():


    def do_proof(self,args):    

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        
        
        
        
        
        r0 = 'HEAttribute'
        r1 = 'HEClass'
        r1_1 = 'HEClass_2'
        r2 = 'HEDataType'
        r3 = 'HEEnum'
        r4 = 'HEEnumLiteral'
        r5 = 'HEFactory'
        r6 = 'HEOperation'
        r7 = 'HEPackage'
        r8 = 'HEParameter'
        r9 = 'HEReference'
        r9_1 = 'HEReference_2'
        r10 = 'HEStringToStringMapEntry'
        r11 = 'HeattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier'
        r12 = 'HeclasslefteSuperTypesSolveRefEClassEClassEClassEClass'
        r13 = 'HeclasslefteOperationsSolveRefEClassEOperationEClassEOperation'
        r14 = 'HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature'
        r15 = 'HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral'
        r16 = 'HefactoryleftePackageSolveRefEFactoryEPackageEFactoryEPackage'
        r17 = 'HeoperationlefteTypeSolveRefEOperationEClassifierEOperationEClassifier'
        r18 = 'HeoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter'
        r19 = 'HepackagelefteFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory'
        r20 = 'HepackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage'
        r21 = 'HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier'
        r22 = 'HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier'
        r23 = 'HereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference'
    
        
                             
        full_transformation = [[r0,],[r1],[r1_1],[r2,],[r3,],[r4,],[r5,],[r6,],[r7,],[r8,],[r9],[r9_1],[r10,],[r11,],[r12,],[r13,],[r14,],[r15,],[r16,],[r17,],[r18,],[r19,],[r20,],[r21,],[r22,],[r23,],]
        #full_transformation = [[r0], [r1], [r11]]
        self.rules, self.transformation = pyramify.get_rules("ECore_Copier_MM/transformation", full_transformation)
        
        inputMM = "ECore_Copier_MM/Ecore.ecore"
        outputMM = "ECore_Copier_MM/Copy.ecore"
        subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ECore_Copier_MM/transformation", self.transformation)


        print("Superclasses Dict:")
        for key in sorted(superclasses_dict.keys()):
            print(key + " : " + str(superclasses_dict[key]))

        #raise Exception()

        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, superclasses_dict, dsltransInstallDir = "/home/dcx/Projects/SyVOLT")
        
        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy
                                                                  
        
        pyramify.set_supertypes(superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)

            
        # load the contracts, and add polymorphism

        self.atomic_contracts = []
        self.if_then_contracts = []

        isolated = HProp1_IsolatedLHS()
        connected = HProp1_ConnectedLHS()
        complete = HProp1_CompleteLHS()
        
        isolated["superclasses_dict"] = superclasses_dict 
        connected["superclasses_dict"] = superclasses_dict 
        complete["superclasses_dict"] = superclasses_dict 
        
        c0 = AtomicContract(isolated, connected, complete)
        
        self.atomic_contracts.append(("Prop1", c0))
        graph_to_dot(complete.name, complete)

        isolated = HEC_prop2_IsolatedLHS()
        connected = HEC_prop2_ConnectedLHS()
        complete = HEC_prop2_CompleteLHS()

        isolated["superclasses_dict"] = superclasses_dict
        connected["superclasses_dict"] = superclasses_dict
        complete["superclasses_dict"] = superclasses_dict

        c1 = AtomicContract(isolated, connected, complete)

        self.atomic_contracts.append(("Prop2", c1))

        slicer = Slicer(self.rules, self.transformation)
        if args.slice > 0:
            print("Slicing for contract number " + str(args.slice))
            contract = self.atomic_contracts[args.slice - 1]


            print("Number rules before: " + str(len(self.rules)))
            self.new_rules, self.new_transformation = slicer.slice_transformation(contract)
            print("Number rules after: " + str(len(self.rules)))

        # generate path conditions
        pc_set = PathConditionGenerator(self.transformation, "ECore_Copier_MM/Copy.ecore", self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)
    
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
        