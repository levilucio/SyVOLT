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

from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

#from util.test_script_utils import select_rules, slice_transformation

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.state_property import StateProperty
from PropertyVerification.atomic_state_property import AtomicStateProperty
from PropertyVerification.and_state_property import AndStateProperty
from PropertyVerification.or_state_property import OrStateProperty
from PropertyVerification.not_state_property import NotStateProperty
from PropertyVerification.implication_state_property import ImplicationStateProperty
from PropertyVerification.Not import Not #StateSpace Prop
from PropertyVerification.Implication import Implication #StateSpace Prop
from PropertyVerification.And import And #StateSpace Prop
from PropertyVerification.Or import Or #StateSpace Prop


from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):
        self.pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)


        full_transformation = [
            ['HMapRootElementRule'],
            ['HState2ProcDef'],
#            ['HBasicStateNoOutgoing2ProcDef', 'HBasicState2ProcDef', 'HCompositeState2ProcDef'],
#            ['HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans', 'HState2HProcDef', 'HState2CProcDef'],
#             ['HTransition2QInstSIBLING', 'HTransition2QInstOUT', 'HTransition2Inst'],
#             ['HTransition2ListenBranch','HConnectOutputsOfExitPoint2BProcDefTransition2QInst',
#              'HTransition2HListenBranch','HConnectOPState2CProcDefTransition2InstotherInTransitions'],    
             ['HMapHeirarchyOfStates2HeirarchyOfProcs', 'HRuleConnect2RootElement']
        ]

        #get the expected num from the args
        #expected_num_pcs = args.num_pcs
        expected_num_pcs = 330



        self.rules, self.transformation = self.pyramify.get_rules("UMLRT2Kiltera_MM/transformation_eq_outside/", full_transformation)


    def test_correct_uml2kiltera(self,args):

#'HMapHeirarchyOfStates2HeirarchyOfProcs':  'HTransition2QInstSIBLING': < 'HState2HProcDef': 'HCompositeState2ProcDef':  'HTransition2ListenBranch':  'HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans':  'HBasicStateNoOutgoing2ProcDef':  'HBasicState2ProcDef': , 'HState2ProcDef'

#Layer1: State2ProcDef
#Layer2: BasicStateNoOutgoing2ProcDef, BasicState2ProcDef, CompositeState2ProcDef
#Layer3: ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, State2HProcDef
#Layer4: Transition2QInstSIBLING
#Layer5: Transition2ListenBranch
#Layer6: MapHeirarchyOfStates2HeirarchyOfProcs


        #pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)




        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]
        
        subclasses_dict, superclasses_dict = self.get_sub_and_super_classes() 
        
        print("\n\n")
        print("Superclasses dict: " + str(superclasses_dict))
        print("\n")
        print("Subclasses dict: " + str(subclasses_dict))
        print("\n\n")
   
        self.pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)


#        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlappingRules] = \
#            self.pyramify.ramify_directory("UMLRT2Kiltera_MM/transformation_eq_outside", transformation)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlappingRules, self.subsumption, self.loopingRuleSubsumption] = \
            self.pyramify.ramify_directory("UMLRT2Kiltera_MM/transformation_eq_outside/", self.transformation)

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

        s = PathConditionGenerator(self.transformation, "UMLRT2Kiltera_MM/metamodels/klt_new.ecore", self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlappingRules, self.subsumption, self.loopingRuleSubsumption, args)#
     
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
              
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))
         
        s.check_rule_reachability()
 
        #check if the correct number of path conditions were produced
        # if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:
        #
        #     #TODO: Make this an exception
        #     num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
        #     print(num_pcs_s)
            #raise Exception(num_pcs_s)
 
#         print("printing path conditions")
        s.print_path_conditions_screen()

#        s.print_path_conditions_file()
#
#         atprop=AtomicStateProperty(HState2procdef_IsolatedLHS(),HState2procdef_IsolatedLHS(), HState2procdef_CompleteLHS())
#         exitpt2procdefparprop_withattr=AtomicStateProperty(HExitpoint2procdefparTrue_IsolatedLHS(),HExitpoint2procdefparTrue_ConnectedLHS(),HExitpoint2procdefparTrue_CompleteLHS())
#         exitpt2procdefparprop_noattr=AtomicStateProperty(HExitpoint2procdefparTrueNOATTR_IsolatedLHS(),HExitpoint2procdefparTrueNOATTR_ConnectedLHS(),HExitpoint2procdefparTrueNOATTR_CompleteLHS())
#         atpropneg=AtomicStateProperty(HState2procdef_IsolatedLHS(), HState2procdef_IsolatedLHS(), HState2funcdefNEG_CompleteLHS())
#         atpropNeedscollapse_no=AtomicStateProperty(HState2trans2exitptTrue_IsolatedLHS(),HState2trans2exitptTrue_ConnectedLHS(),HState2trans2exitptTrue_CompleteLHS())
#         collapsable=AtomicStateProperty(HTrans2instTRUE_IsolatedLHS(), HTrans2instTRUE_ConnectedLHS(),HTrans2instTRUE_CompleteLHS())
#
#         ######Multiplicity Invariants - Begin
#         #Par2Procs
#         par2ProcsIfClause=AtomicStateProperty(HPar2ProcsPart1_2_IsolatedLHS(), HPar2ProcsPart1_2_IsolatedLHS(), HPar2ProcsPart1_CompleteLHS())
#         par2ProcsThenClause=AtomicStateProperty(HPar2ProcsPart1_2_IsolatedLHS(), HPar2ProcsPart1_2_IsolatedLHS(), HPar2ProcsPart2_CompleteLHS())
#         par2ProcsFULL=ImplicationStateProperty(par2ProcsIfClause, par2ProcsThenClause)
#         #Trigger01Expr
#         Trigger01Expr_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(), HTrigger01ExprPart1_CompleteLHS())
#         Trigger01Expr_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(), HTrigger01ExprPart2_CompleteLHS())
#         Trigger01Expr_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(), HTrigger01ExprPart3_CompleteLHS())
#         Trigger01Expr_part4=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(), HTrigger01ExprPart4_CompleteLHS())
#         Trigger01ExprFULL=ImplicationStateProperty (Trigger01Expr_part1,OrStateProperty(AndStateProperty(Trigger01Expr_part2, NotStateProperty(Trigger01Expr_part3)),NotStateProperty(Trigger01Expr_part4)))
#         #Listen 1 or more listenBranch
#         Listen1orMoreListenBranch_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(), HListen1orMoreListenBranchPart1_CompleteLHS())
#         Listen1orMoreListenBranch_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(), HListen1orMoreListenBranchPart2_CompleteLHS())
#         Listen1orMoreListenBranch_FULL=ImplicationStateProperty(Listen1orMoreListenBranch_part1, Listen1orMoreListenBranch_part2)
#         #New1OrMoreName
#         New1orMoreName_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HNew1orMoreNamePart1_CompleteLHS())
#         New1orMoreName_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HNew1orMoreNamePart2_CompleteLHS())
#         New1orMoreName_FULL=ImplicationStateProperty(New1orMoreName_part1,New1orMoreName_part2)
#         #COnditionSet1orMOreCOnditionBranch
#         ConditionSet1orMoreConditionBranch_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionSet1orMoreConditionBranchPart1_CompleteLHS())
#         ConditionSet1orMoreConditionBranch_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionSet1orMoreConditionBranchPart2_CompleteLHS())
#         ConditionSet1orMoreConditionBranch_FULL=ImplicationStateProperty(ConditionSet1orMoreConditionBranch_part1,ConditionSet1orMoreConditionBranch_part2)
#         #localDef1orMoreDef
#         LocalDef1orMoreDef_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HLocalDef1orMoreDefPart1_CompleteLHS())
#         LocalDef1orMoreDef_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HLocalDef1orMoreDefPart2_CompleteLHS())
#         LocalDef1orMoreDef_FULL=ImplicationStateProperty(LocalDef1orMoreDef_part1,LocalDef1orMoreDef_part2)
#         #COnditionBranch1Expr
#         ConditionBranch1Expr_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionBranch1ExprPart1_CompleteLHS())
#         ConditionBranch1Expr_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionBranch1ExprPart2_CompleteLHS())
#         ConditionBranch1Expr_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionBranch1ExprPart3_CompleteLHS())
#         ConditionBranch1Expr_FULL=ImplicationStateProperty(ConditionBranch1Expr_part1,AndStateProperty(ConditionBranch1Expr_part2,NotStateProperty(ConditionBranch1Expr_part3)))
#         #ListenBranch01Pattern
#         ListenBranch01Pattern_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch01PatternPart1_CompleteLHS())
#         ListenBranch01Pattern_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch01PatternPart2_CompleteLHS())
#         ListenBranch01Pattern_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch01PatternPart3_CompleteLHS())
#         ListenBranch01Pattern_part4=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch01PatternPart4_CompleteLHS())
#         ListenBranch01Pattern_FULL=ImplicationStateProperty(ListenBranch01Pattern_part1,OrStateProperty(AndStateProperty(ListenBranch01Pattern_part2,NotStateProperty(ListenBranch01Pattern_part3)),NotStateProperty(ListenBranch01Pattern_part4)))
#         #ConditionSet01Proc
#         ConditionSet01Proc_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionSet01ProcPart1_CompleteLHS())
#         ConditionSet01Proc_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionSet01ProcPart2_CompleteLHS())
#         ConditionSet01Proc_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionSet01ProcPart3_CompleteLHS())
#         ConditionSet01Proc_part4=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionSet01ProcPart4_CompleteLHS())
#         ConditionSet01Proc_FULL=ImplicationStateProperty(ConditionSet01Proc_part1,OrStateProperty(AndStateProperty(ConditionSet01Proc_part2, NotStateProperty(ConditionSet01Proc_part3)),NotStateProperty(ConditionSet01Proc_part4)))
#         #ProcDef1Proc
#         ProcDef1Proc_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HProcDef1ProcPart1_CompleteLHS())
#         ProcDef1Proc_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HProcDef1ProcPart2_CompleteLHS())
#         ProcDef1Proc_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HProcDef1ProcPart3_CompleteLHS())
#         ProcDef1Proc_FULL=ImplicationStateProperty(ProcDef1Proc_part1,AndStateProperty(ProcDef1Proc_part2, NotStateProperty(ProcDef1Proc_part3)))
#         #ListenBranch1Proc
#         ListenBranch1Proc_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch1ProcPart1_CompleteLHS())
#         ListenBranch1Proc_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch1ProcPart2_CompleteLHS())
#         ListenBranch1Proc_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HListenBranch1ProcPart3_CompleteLHS())
#         ListenBranch1Proc_FULL=ImplicationStateProperty(ListenBranch1Proc_part1,AndStateProperty(ListenBranch1Proc_part2,NotStateProperty(ListenBranch1Proc_part3)))
#         #New1Proc
#         New1Proc_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HNew1ProcPart1_CompleteLHS())
#         New1Proc_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HNew1ProcPart2_CompleteLHS())
#         New1Proc_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HNew1ProcPart3_CompleteLHS())
#         New1Proc_FULL=ImplicationStateProperty(New1Proc_part1, AndStateProperty(New1Proc_part2, NotStateProperty(New1Proc_part3)))
#         #LocalDef1Proc
#         LocalDef1Proc_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HLocalDef1ProcPart1_CompleteLHS())
#         LocalDef1Proc_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HLocalDef1ProcPart2_CompleteLHS())
#         LocalDef1Proc_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HLocalDef1ProcPart3_CompleteLHS())
#         LocalDef1Proc_FULL=ImplicationStateProperty(LocalDef1Proc_part1,AndStateProperty(LocalDef1Proc_part2,NotStateProperty(LocalDef1Proc_part3)))
#         #ConditionBranch1Proc
#         ConditionBranch1Proc_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionBranch1ProcPart1_CompleteLHS())
#         ConditionBranch1Proc_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionBranch1ProcPart2_CompleteLHS())
#         ConditionBranch1Proc_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HConditionBranch1ProcPart3_CompleteLHS())
#         ConditionBranch1Proc_FULL=ImplicationStateProperty(ConditionBranch1Proc_part1,AndStateProperty(ConditionBranch1Proc_part2,NotStateProperty(ConditionBranch1Proc_part3)))
#         ######Multiplicity INvariants - End
#
#         ######Syntactic COntracts - Begin
#         InstStateSameName_part1=AtomicStateProperty(HInstStateSameNamePart1_2_IsolatedConnectedLHS(), HInstStateSameNamePart1_2_IsolatedConnectedLHS(), HInstStateSameNamePart1_CompleteLHS)
#         InstStateSameName_part2=AtomicStateProperty(HInstStateSameNamePart1_2_IsolatedConnectedLHS(), HInstStateSameNamePart1_2_IsolatedConnectedLHS(), HInstStateSameNamePart2_CompleteLHS)
#         InstSTateSameName_FULL=ImplicationStateProperty(InstStateSameName_part1, InstStateSameName_part2)
#         InstHProcDefH_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstHProcDefHpart1_CompleteLHS())
#         InstHProcDefH_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstHProcDefHpart2_CompleteLHS())
#         InstHProcDefH_FULL=ImplicationStateProperty(InstHProcDefH_part1,InstHProcDefH_part2)
#         InstCProcDefC_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstCProcDefCpart1_CompleteLHS())
#         InstCProcDefC_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstCProcDefCpart2_CompleteLHS())
#         InstCProcDefC_FULL=ImplicationStateProperty(InstCProcDefC_part1,InstCProcDefC_part2)
#         HInstProcDefParams_part1=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstProcDefParamspart1_CompleteLHS())
#         HInstProcDefParams_part2=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstProcDefParamspart2_CompleteLHS())
#         HInstProcDefParams_part3=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstProcDefParamspart3_CompleteLHS())
#         HInstProcDefParams_part4=AtomicStateProperty(HEmpty_IsolatedConnectedLHS(),HEmpty_IsolatedConnectedLHS(),HInstProcDefParamspart4_CompleteLHS())
#         HInstProcDefParams_FULL=ImplicationStateProperty(AndStateProperty(HInstProcDefParams_part1,NotStateProperty(HInstProcDefParams_part2)),AndStateProperty(HInstProcDefParams_part3,NotStateProperty(HInstProcDefParams_part4)))
#         ######Syntactic COntracts - ENd
#
#         ##PatternContracts - BEGIN
#         nestedStates2NestedProcDefs_FULL=AtomicStateProperty(HNestedStates2nestedProcDefs_IsolatedLHS(),HNestedStates2nestedProcDefs_ConnectedLHS(),HNestedStates2nestedProcDefs_CompleteLHS())
#         ##PatternContracts - END
#         #StateProperty.SETverifVerbosity(2)
#         ts2 = time.time()
#         finalresult=StateProperty.verifyCompositeStateProperty(s,Listen1orMoreListenBranch_FULL)
#         ##for Levi - properties to try Listen1orMoreListenBranch_FULL, par2ProcsFULL, Trigger01ExprFULL,nestedStates2NestedProcDefs_FULL, New1orMoreName_FULL, ConditionSet1orMoreConditionBranch_FULL, LocalDef1orMoreDef_FULL, ConditionBranch1Expr_FULL, LocalDef1orMoreDef_FULL,ConditionSet01Proc_FULL, ProcDef1Proc_FULL, ListenBranch1Proc_FULL,LocalDef1Proc_FULL
#         #New1Proc_FULL, InstHProcDefH_FULL, InstCProcDefC_FULL
#         ts3 = time.time()
#         print("\n\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
# #        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
#         print("Number of path conditions: " + str(s.num_path_conditions))
#         print("Time to verify the input property: " + str(ts3 - ts2))
#         #to debug tomorrow par2ProcsFULL InstStateSameName
#         #finalresult=StateProperty.verifyCompositeStateProperty(s, collapsable)
#         if finalresult:
#             print ('Property HOLDS on the transformation.')
#         else:
#             print ('Property DOES NOT HOLD on the transformation.')
#
#         #CHecking Rule Reachability
# #         StateProperty.checkRuleReachability('HMapHeirarchyOfStates2HeirarchyOfProcs', s)
# #         StateProperty.checkRuleReachability('HCompositeState2ProcDef', s)
#
# #         print("printing states")
# #         self._print_states(s)
#
# #         graph_to_dot('symbolic_exec', s.symbStateSpace[1][0], 1)
#
#
#         ####REAL EXPERIMENTATION: Proving the 4 types of constraints in our MODELS paper
#         # The naming convention used for the properties (i.e., P1, P2..ETC) are the
#         # same convention used in my MODELS paper in Table 2.
#
#
# #         print("create property")
#         P1atomic=AtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
#         P2atomic=AtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
#         S1IfClause=AtomicStateProperty(HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseCompleteLHS())
#         S1ThenClause=AtomicStateProperty(HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseCompleteLHS())
#         M1IfClause=AtomicStateProperty(HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseCompleteLHS())
#         M1ThenClause=AtomicStateProperty(HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1CompleteLHS())
#         M3IfClause=AtomicStateProperty(HM3IfClauseIsolatedConnectedLHS(),HM3IfClauseIsolatedConnectedLHS(), HM3IfClauseCompleteLHS())
#         M3ThenClause=AtomicStateProperty(HM3ThenClausePart1IsolatedConnectedLHS(), HM3ThenClausePart1IsolatedConnectedLHS(),HM3ThenClausePart1CompleteLHS())
#         M2IfClause=AtomicStateProperty(HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseCompleteLHS())
#         M2ThenClause=AndStateProperty(AtomicStateProperty(HM2ThenClausePart1IsolatedConnectedLHS(),HM2ThenClausePart1IsolatedConnectedLHS(), HM2ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2CompleteLHS())))
#         M4IfClause=AtomicStateProperty(HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseCompleteLHS())
#         M4ThenClause=AndStateProperty(AtomicStateProperty(HM4ThenClausePart1IsolatedConnectedLHS(),HM4ThenClausePart1IsolatedConnectedLHS(), HM4ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2CompleteLHS())))
#         M5IfClause=AtomicStateProperty(HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseCompleteLHS())
#         M5ThenClause=AndStateProperty(AtomicStateProperty(HM5ThenClausePart1IsolatedConnectedLHS(),HM5ThenClausePart1IsolatedConnectedLHS(), HM5ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2CompleteLHS())))
#         M6IfClause=AtomicStateProperty(HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseCompleteLHS())
#         M6ThenClause=AndStateProperty(AtomicStateProperty(HM6ThenClausePart1IsolatedConnectedLHS(),HM6ThenClausePart1IsolatedConnectedLHS(), HM6ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2CompleteLHS())))
#
#         #andprop=AndStateProperty(AndStateProperty(atomic1,atomic2),atomic1)
#         #P1atomicOldImpl=BKUPAtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
#         #P2atomicOldImpl=BKUPAtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
#
# #        trivatomicprop=AtomicStateProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
#
#         #NOTE: Even if you are verifying an ANDstateProperty where the 2 operands are the same AtomicStateProperty, then store two copies of the AtomicStateProperty in 2 different variables
#         #Why? variables in this case are references to objects. So if you want the 2 copies of the same AtomicStateProperty to have different values set for certain attributes, then you must store them in 2 different variables
# #        trivnegativeprop=AtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
# #        trivnegativepropcopy=AtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
# #        trivatomicpropOldImpl=BKUPAtomicStateProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
# #        trivnegativepropOldImpl=BKUPAtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
# #        IsolHasNoMatch=AtomicStateProperty(HIsolHasNoMatchIsolatedLHS(), HIsolHasNoMatchConnectedLHS(), HIsolHasNoMatchCompleteLHS())
#         #trivnegativepropOldImpl.verify(s)
#         #finalresult=StateProperty.verifyCompositeStateProperty(s, P1atomic)
#         #StateProperty.verifyCompositeStateProperty(s, OrStateProperty(P2atomic,trivnegativeprop))
#         finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(M5IfClause, M5ThenClause))
#         #finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(S1IfClause,S1ThenClause))
#         print ('finalresult : ')
#         print (finalresult)


    def get_sub_and_super_classes(self):
            subclasses_dict = {}     
            
            inputMM = "UMLRT2Kiltera_MM/metamodels/rt_new.ecore"
            outputMM = "UMLRT2Kiltera_MM/metamodels/klt_new.ecore"
         
            inMM = EcoreUtils(inputMM)          
            subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(inMM.getMetamodelClassNames())      
            
            inMMinheritanceTree = inMM.getSubClassInheritanceRelationForClasses()
            
            for className in inMMinheritanceTree:
                subclasses_dict["MT_pre__" + className] = buildPreListFromClassNames(inMMinheritanceTree[className])
            
            outMM = EcoreUtils(outputMM)  
            subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(outMM.getMetamodelClassNames())

            outMMinheritanceTree = outMM.getSubClassInheritanceRelationForClasses()
            for className in outMMinheritanceTree:
                subclasses_dict["MT_pre__" + className] = buildPreListFromClassNames(outMMinheritanceTree[className])            
            
#             print("========================")
#             print("Inheritance: " + str(subclasses_dict))
#             print("========================")      

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

    
