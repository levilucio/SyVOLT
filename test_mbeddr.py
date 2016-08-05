
#-----------------------------------------------------------------------------
# Auto generated from the DSLTrans transformation and the properties to prove
#-----------------------------------------------------------------------------

import time

from path_condition_generator import PathConditionGenerator
from pyramify.PyRamify import PyRamify

from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from PropertyVerification.ContractProver import ContractProver

from core.himesis_utils import graph_to_dot, load_directory
from util.test_script_utils import select_rules, get_sub_and_super_classes,\
    load_transformation, changePropertyProverMetamodel, set_supertypes, load_contracts
from util.slicer import Slicer
from util.parser import load_parser

class Prover():


    def do_proof(self,args):    

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        
        
        transformation_dir = "mbeddr2C_MM/real_transformation/no_contains"

        r0 = 'Hlayer0rule0'
        r1 = 'Hlayer0rule1'
        r2 = 'Hlayer0rule2'
        r3 = 'Hlayer0rule3'
        r4 = 'Hlayer0rule4'
        r5 = 'Hlayer0rule6'
        r6 = 'Hlayer0rule7'
        r7 = 'Hlayer0rule8'
        r8 = 'Hlayer0rule9'
        r9 = 'Hlayer0rule10'
        r10 = 'Hlayer0rule11'
        r11 = 'Hlayer1rule0'
        r12 = 'Hlayer1rule1'
        r13 = 'Hlayer1rule2'
        r14 = 'Hlayer1rule3'
        r15 = 'Hlayer1rule4'
        r16 = 'Hlayer1rule5'
        r17 = 'Hlayer1rule6'
        r18 = 'Hlayer1rule7'
        r19 = 'Hlayer1rule8'
        r20 = 'Hlayer1rule9'
        r21 = 'Hlayer1rule10'
        r22 = 'Hlayer1rule11'
        r23 = 'Hlayer1rule12'
        r24 = 'Hlayer1rule13'
        r25 = 'Hlayer1rule14'
        r26 = 'Hlayer1rule15'
        r27 = 'Hlayer2rule1'
        r28 = 'Hlayer2rule2'
        r29 = 'Hlayer2rule3'
        r30 = 'Hlayer3rule0'
        r31 = 'Hlayer3rule1'
        r32 = 'Hlayer3rule2'
        r33 = 'Hlayer3rule3'
        r34 = 'Hlayer3rule4'
        r33copy = 'Hlayer3rule3'
        r34copy = 'Hlayer3rule4'
        r35 = 'Hlayer3rule5'
        r36 = 'Hlayer4rule0'
        r37 = 'Hlayer4rule1'
        r38 = 'Hlayer4rule2'
        r39 = 'Hlayer4rule3'
        r40 = 'Hlayer5rule0'
        r41 = 'Hlayer5rule1'
        r42 = 'Hlayer5rule2'
        r43 = 'Hlayer5rule3'
        r44 = 'Hlayer5rule4'
        r45 = 'Hlayer5rule5'
        r46 = 'Hlayer6rule0'

        full_transformation = [[r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, ],
                               [r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, ],
                               [r27, r28, r29, ], [r30, r31, r32, r33, r34, r33copy, r34copy, r35, ], [r36, r37, r38, r39, ],
                               [r40, r41, r42, r43, r44, r45, ], [r46, ],
        ]

        self.rules, self.transformation = load_transformation(transformation_dir, full_transformation)

        inputMM = "./mbeddr2C_MM/ecore_metamodels/Module.ecore"
        outputMM = "./mbeddr2C_MM/ecore_metamodels/C.ecore"
        subclasses_dict, self.superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory(transformation_dir, self.transformation)

        # for rule in self.rules:
        #     graph_to_dot(rule, self.rules[rule])

        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]


        changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, self.superclasses_dict, ".")
        set_supertypes(self.superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)
        
        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy
                                                                  

            
        # load the contracts, and add polymorphism
        contracts = load_directory("mbeddr2C_MM/Contracts/")

        atomic_contracts = [
            'AssignmentInstance',
            'GlobalVarGetsCorrectFunctionAddressAtInit',
            'Simple',
            'VerySimple'
        ]

        if_then_contracts = []
        prop_if_then_contracts = []

        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, self.superclasses_dict,
                                                                       atomic_contracts, if_then_contracts,
                                                                       prop_if_then_contracts,
                                                                       args.draw_svg)


        slicer = Slicer(self.rules, self.transformation, self.superclasses_dict, self.overlapping_rules)

        if args.slice > -1:
            contract, self.atomic_contracts, self.if_then_contracts = slicer.get_contract(args.slice,
                                                                                          self.atomic_contracts,
                                                                                          self.if_then_contracts)
            self.rules, self.transformation = slicer.slice_transformation(contract)


        for layer in self.transformation:
            print("Layer:")
            for rule in layer:
                print(rule.name)

        # generate path conditions
        #raise Exception()


        inputMM = "./mbeddr2C_MM/ecore_metamodels/Module.ecore"
        pc_set = PathConditionGenerator(self.transformation, outputMM, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)

        #raise Exception()

        ts0 = time.time()
        pc_set.build_path_conditions()
        ts1 = time.time()

        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))

        # print path conditions to screen


        #pc_set.print_path_conditions_file()

        print("\nContract proving:")

        pc_set.verbosity = 0

        contract_prover = ContractProver()

        contract_prover.prove_contracts(pc_set, self.atomic_contracts, [])  # self.if_then_contracts)
        print("\n\nTime to build the set of path conditions: " + str(ts1-ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))




if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()


    prover = Prover()
    prover.do_proof(args)
        
