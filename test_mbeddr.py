
#-----------------------------------------------------------------------------
# Auto generated from the DSLTrans transformation and the properties to prove
#-----------------------------------------------------------------------------

import time

from path_condition_generator import PathConditionGenerator
from PyRamify import PyRamify

from ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition

from PropertyVerification.state_property import StateProperty
from PropertyVerification.atomic_state_property import AtomicStateProperty
from PropertyVerification.and_state_property import AndStateProperty
from PropertyVerification.or_state_property import OrStateProperty
from PropertyVerification.not_state_property import NotStateProperty
from PropertyVerification.implication_state_property import ImplicationStateProperty

from PropertyVerification.Not import Not 					#StateSpace Prop
from PropertyVerification.Implication import Implication 	#StateSpace Prop
from PropertyVerification.And import And 					#StateSpace Prop
from PropertyVerification.Or import Or 						#StateSpace Prop

from core.himesis_utils import graph_to_dot
from util.test_script_utils import select_rules
from util.slicer import Slicer

# imports for properties' atomic contracts

from mbeddr2C_MM.Contracts.HAssignmentInstance_IsolatedLHS import HAssignmentInstance_IsolatedLHS
from mbeddr2C_MM.Contracts.HAssignmentInstance_ConnectedLHS import HAssignmentInstance_ConnectedLHS
from mbeddr2C_MM.Contracts.HAssignmentInstance_CompleteLHS import HAssignmentInstance_CompleteLHS
from mbeddr2C_MM.Contracts.HGlobalVarGetsCorrectFunctionAddressAtInit_IsolatedLHS import HGlobalVarGetsCorrectFunctionAddressAtInit_IsolatedLHS
from mbeddr2C_MM.Contracts.HGlobalVarGetsCorrectFunctionAddressAtInit_ConnectedLHS import HGlobalVarGetsCorrectFunctionAddressAtInit_ConnectedLHS
from mbeddr2C_MM.Contracts.HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS import HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS


class Prover():


    def do_proof(self,args):    

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        
        
        
        
        
        r0 = 'Hlayer0rule0'
        r1 = 'Hlayer0rule1'
        r2 = 'Hlayer0rule2'
        r3 = 'Hlayer0rule3'
        r4 = 'Hlayer0rule4'
        r5 = 'Hlayer0rule5'
        r6 = 'Hlayer0rule6'
        r7 = 'Hlayer0rule7'
        r8 = 'Hlayer0rule8'
        r9 = 'Hlayer0rule9'
        r10 = 'Hlayer0rule10'
        r11 = 'Hlayer0rule11'
        r12 = 'Hlayer1rule0'
        r13 = 'Hlayer1rule1'
        r14 = 'Hlayer1rule2'
        r15 = 'Hlayer1rule3'
        r16 = 'Hlayer1rule4'
        r17 = 'Hlayer1rule5'
        r18 = 'Hlayer1rule6'
        r19 = 'Hlayer1rule7'
        r20 = 'Hlayer1rule8'
        r21 = 'Hlayer1rule9'
        r22 = 'Hlayer1rule10'
        r23 = 'Hlayer1rule11'
        r24 = 'Hlayer1rule12'
        r25 = 'Hlayer1rule13'
        r26 = 'Hlayer1rule14'
        r27 = 'Hlayer1rule15'
        r28 = 'Hlayer2rule0'
        r29 = 'Hlayer2rule1'
        r30 = 'Hlayer2rule2'
        r31 = 'Hlayer2rule3'
        r32 = 'Hlayer3rule0'
        r33 = 'Hlayer3rule1'
        r34 = 'Hlayer3rule2'
        r35 = 'Hlayer3rule3'
        r36 = 'Hlayer3rule4'
        r37 = 'Hlayer3rule5'
        r38 = 'Hlayer4rule0'
        r39 = 'Hlayer4rule1'
        r40 = 'Hlayer4rule2'
        r41 = 'Hlayer4rule3'
        r42 = 'Hlayer5rule0'
        r43 = 'Hlayer5rule1'
        r44 = 'Hlayer5rule2'
        r45 = 'Hlayer5rule3'
        r46 = 'Hlayer5rule4'
        r47 = 'Hlayer5rule5'
        r48 = 'Hlayer6rule0'
    
        
                             
        full_transformation = [[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,],[r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,],[r28,r29,r30,r31,],[r32,r33,r34,r35,r36,r37,],[r38,r39,r40,r41,],[r42,r43,r44,r45,r46,r47,],[r48,],]
        
        self.rules, self.transformation = pyramify.get_rules("/home/boakes/Projects/SyVOLT/eclipse_integration/backend/generated/transformation", full_transformation)
        
        subclasses_dict, superclasses_dict = self.get_sub_and_super_classes()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("/home/boakes/Projects/SyVOLT/eclipse_integration/backend/generated/transformation", self.transformation)   

                
        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, "/home/boakes/Projects/SyVOLT")
        
        # go through all the matchers, combinators and tracers to add polymorphism on all classes in an inheritance hierarchy
                                                                  
        
        # add polymorphism for the matchers
        for matcher_key in self.matchRulePatterns.keys():
            self.matchRulePatterns[matcher_key][0].condition["superclasses_dict"] = superclasses_dict
            
        # add polymorphism for the combinators
        for combs_key in self.ruleCombinators.keys():
            if self.ruleCombinators[combs_key] != None:
                for combinator in self.ruleCombinators[combs_key]:
                    combinator[0].condition["superclasses_dict"] = superclasses_dict

        # add polymorphism for the tracers
        for tracer_key in self.ruleTraceCheckers.keys():
            if self.ruleTraceCheckers[tracer_key] != None:
                self.ruleTraceCheckers[tracer_key].condition["superclasses_dict"] = superclasses_dict

        #also make sure the transformation has this information
        for rule in self.rules.values():
            rule["superclasses_dict"] = superclasses_dict

        for layer in self.transformation:
            for rule in layer:
                rule["superclasses_dict"] = superclasses_dict
            
		# load the contracts, and add polymorphism

        if (args.draw_svg):
        	graph_to_dot("property_AssignmentInstance_isolated", HAssignmentInstance_IsolatedLHS())
        	graph_to_dot("property_AssignmentInstance_connected", HAssignmentInstance_ConnectedLHS())
        	graph_to_dot("property_AssignmentInstance_complete", HAssignmentInstance_CompleteLHS())
        	graph_to_dot("property_GlobalVarGetsCorrectFunctionAddressAtInit_isolated", HGlobalVarGetsCorrectFunctionAddressAtInit_IsolatedLHS())
        	graph_to_dot("property_GlobalVarGetsCorrectFunctionAddressAtInit_connected", HGlobalVarGetsCorrectFunctionAddressAtInit_ConnectedLHS())
        	graph_to_dot("property_GlobalVarGetsCorrectFunctionAddressAtInit_complete", HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS())


        self.atomic_contracts = []


        isolated = HAssignmentInstance_IsolatedLHS()
        connected = HAssignmentInstance_ConnectedLHS()
        complete = HAssignmentInstance_CompleteLHS()

        isolated["superclasses_dict"] = superclasses_dict
        connected["superclasses_dict"] = superclasses_dict
        complete["superclasses_dict"] = superclasses_dict

        c0 = AtomicStateProperty(isolated, connected, complete)

        self.atomic_contracts.append(("AssignmentInstance", c0))



        isolated = HGlobalVarGetsCorrectFunctionAddressAtInit_IsolatedLHS()
        connected = HGlobalVarGetsCorrectFunctionAddressAtInit_ConnectedLHS()
        complete = HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS()

        isolated["superclasses_dict"] = superclasses_dict
        connected["superclasses_dict"] = superclasses_dict
        complete["superclasses_dict"] = superclasses_dict

        c0 = AtomicStateProperty(isolated, connected, complete)

        self.atomic_contracts.append(("GlobalVarGetsCorrectFunctionAddressAtInit", c0))


        if args.slice > 0:
            contract = self.atomic_contracts[args.slice - 1]
            print("Slicing for contract number " + str(args.slice) + " : " + contract[0])

            slicer = Slicer()

            print("Number rules before: " + str(len(self.rules)))
            self.rules, self.transformation = slicer.slice_transformation(self.rules, self.transformation, contract, args)
            print("Number rules after: " + str(len(self.rules)))

        # for layer in self.transformation:
        #     print("Layer:")
        #     for rule in layer:
        #         print(rule.name)

        #raise Exception()

		# generate path conditions
        pc_set = PathConditionGenerator(self.transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)

        ts0 = time.time()
        pc_set.build_path_conditions()
        ts1 = time.time()

        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        print("Number of path conditions: " + str(pc_set.num_path_conditions))

        # print path conditions to screen

        if pc_set.num_path_conditions < 300:
            pc_set.print_path_conditions_screen()

        # now actually prove these contracts


        ts0 = time.time()

        verifier = StateProperty()

        for name, a_c in self.atomic_contracts:
            result = verifier.verifyCompositeStateProperty(pc_set, a_c)
            if len(result) == 0:
            	print("\n")
            	print("Contract " + name + " holds!")
            else:
            	print("\n")
            	print("Contract " + name + " does not hold!")
            	print(result)
        
        ts1 = time.time()
        
        print("\n\nTime to verify properties: " + str(ts1 - ts0) + " seconds.")

        
    def get_sub_and_super_classes(self):
            subclasses_dict = {}     
            
            inputMM = "./mbeddr2C_MM/ecore_metamodels/Module.ecore"
            outputMM = "./mbeddr2C_MM/ecore_metamodels/C.ecore"
         
            inMM = EcoreUtils(inputMM)          
            subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(inMM.getMetamodelClassNames())
            
            print(subclasses_dict["MT_pre__MetaModelElement_S"])

            outMM = EcoreUtils(outputMM)  
            subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(outMM.getMetamodelClassNames()) 
            
            print(subclasses_dict["MT_pre__MetaModelElement_T"])

            # keep a dictionary from each child to its parent
            supertypes = {}

            for supertype in subclasses_dict:
                for subtype in subclasses_dict[supertype]:
                    subtype = subtype[8:]
                    try:
                        supertypes[subtype].append(supertype[8:])
                    except KeyError:
                        supertypes[subtype] = [supertype[8:]]

            return subclasses_dict, supertypes



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
        