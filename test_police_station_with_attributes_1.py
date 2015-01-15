'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time
import sys

from path_condition_generator import PathConditionGenerator

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.messages import Packet

from PyRamify import PyRamify

from himesis_utils import graph_to_dot

from t_core.tc_python.frule import FRule
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules

from PoliceStationMM.transformation_1.Himesis.HS2S import HS2S
from PoliceStationMM.transformation_1.Himesis.HM2M import HM2M
from PoliceStationMM.transformation_1.Himesis.HF2F import HF2F
from PoliceStationMM.transformation_1.Himesis.HSM2SM import HSM2SM
from PoliceStationMM.transformation_1.Himesis.HSF2SF import HSF2SF
from PoliceStationMM.transformation_1.Himesis.HMM2MM import HMM2MM
from PoliceStationMM.transformation_1.Himesis.HFF2FF import HFF2FF

# combination rules
# ------------------

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HS2S_combineLHS import HS2S_combineLHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HS2S_combineRHS import HS2S_combineRHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HM2M_combineLHS import HM2M_combineLHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HM2M_combineRHS import HM2M_combineRHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HF2F_combineLHS import HF2F_combineLHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HF2F_combineRHS import HF2F_combineRHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_0RHS import HFF2FF_combine_0RHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_1LHS import HFF2FF_combine_1LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_1RHS import HFF2FF_combine_1RHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_0RHS import HFF2FF_combine_0RHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_1LHS import HFF2FF_combine_1LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_combine_1RHS import HFF2FF_combine_1RHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HMM2MM_combine_0RHS import HMM2MM_combine_0RHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HMM2MM_combine_1LHS import HMM2MM_combine_1LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HMM2MM_combine_1RHS import HMM2MM_combine_1RHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSF2SF_combine_0RHS import HSF2SF_combine_0RHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSF2SF_combine_1LHS import HSF2SF_combine_1LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSF2SF_combine_1RHS import HSF2SF_combine_1RHS

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSM2SM_combine_0RHS import HSM2SM_combine_0RHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSM2SM_combine_1LHS import HSM2SM_combine_1LHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSM2SM_combine_1RHS import HSM2SM_combine_1RHS

# backward link checking rules
# ------------------

from PoliceStationMM.pc_and_rule_combination_1.Himesis.HFF2FF_trace_checkLHS import HFF2FF_trace_checkLHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HMM2MM_trace_checkLHS import HMM2MM_trace_checkLHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSF2SF_trace_checkLHS import HSF2SF_trace_checkLHS
from PoliceStationMM.pc_and_rule_combination_1.Himesis.HSM2SM_trace_checkLHS import HSM2SM_trace_checkLHS


# property prover rules
# ------------------

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
from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
#from lib2to3.fixer_util import p1


from police_station_transformation.property.run1.positive.HTestLHS import HTestLHS
from police_station_transformation.property.run1.positive.HFSMIsolated_run1LHS import HFSMIsolated_run1LHS
from police_station_transformation.property.run1.positive.HFSMConnected_run1LHS import HFSMConnected_run1LHS
from police_station_transformation.property.run1.positive.HFSMComplete_run1LHS import HFSMComplete_run1LHS

from police_station_transformation.property.run1.negative.HF2FFIsolated_run1LHS import HF2FFIsolated_run1LHS
from police_station_transformation.property.run1.negative.HF2FFConnected_run1LHS import HF2FFConnected_run1LHS
from police_station_transformation.property.run1.negative.HF2FFComplete_run1LHS import HF2FFComplete_run1LHS

# transformation to built traceability for rules
from GM2AUTOSAR_MM.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from GM2AUTOSAR_MM.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS

class Test(unittest.TestCase):

    def setUp(self):
        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("PoliceStationMM/transformation_1/Himesis/", True)

        # print(self.rules)

        # self.rules = {"S2S": HS2S(),
        #               "M2M": HM2M(),
        #               "F2F": HF2F(),
        #               "SM2SM": HSM2SM(),
        #               "SF2SF": HSF2SF(),
        #               "MM2MM": HMM2MM(),
        #               "FF2FF": HFF2FF(),
        #               }
        
        self.transformation = [[self.rules["HS2S"], self.rules["HM2M"], self.rules["HF2F"]],\
                               [self.rules["HSM2SM"], self.rules["HSF2SF"], self.rules["HMM2MM"], self.rules["HFF2FF"]]]

        
#         self.rules = {self.transformation[0][0]: HS2S(),
#                       self.transformation[0][1]: HM2M(),
#                       self.transformation[0][2]: HF2F()}

        #print(self.ruleCombinators)
        # self.ruleCombinators = {self.transformation[0][0].name: None,
        #                         self.transformation[0][1].name: None,
        #                         self.transformation[0][2].name: None,
        #                         self.transformation[1][0].name: [(Matcher(HSM2SM_combine_0LHS()),Rewriter(HSM2SM_combine_0RHS())),(Matcher(HSM2SM_combine_1LHS()),Rewriter(HSM2SM_combine_1RHS()))],
        #                         self.transformation[1][1].name: [(Matcher(HSF2SF_combine_0LHS()),Rewriter(HSF2SF_combine_0RHS())),(Matcher(HSF2SF_combine_1LHS()),Rewriter(HSF2SF_combine_1RHS()))],
        #                         self.transformation[1][2].name: [(Matcher(HMM2MM_combine_0LHS()),Rewriter(HMM2MM_combine_0RHS())),(Matcher(HMM2MM_combine_1LHS()),Rewriter(HMM2MM_combine_1RHS()))],
        #                         self.transformation[1][3].name: [(Matcher(HFF2FF_combine_0LHS()),Rewriter(HFF2FF_combine_0RHS())),(Matcher(HFF2FF_combine_1LHS()),Rewriter(HFF2FF_combine_1RHS()))]}
        #

        #self.ruleCombinators[self.transformation[1][0].name] = [(Matcher(HSM2SM_combine_0LHS()), Rewriter(HSM2SM_combine_0RHS())), (Matcher(HSM2SM_combine_1LHS()), Rewriter(HSM2SM_combine_1RHS()))]
        #self.ruleCombinators[self.transformation[1][1].name] = [(Matcher(HSF2SF_combine_0LHS()),Rewriter(HSF2SF_combine_0RHS())),(Matcher(HSF2SF_combine_1LHS()),Rewriter(HSF2SF_combine_1RHS()))]
        #self.ruleCombinators[self.transformation[1][2].name] = [(Matcher(HMM2MM_combine_0LHS()),Rewriter(HMM2MM_combine_0RHS())),(Matcher(HMM2MM_combine_1LHS()),Rewriter(HMM2MM_combine_1RHS()))]
        #self.ruleCombinators[self.transformation[1][3].name] = [(Matcher(HFF2FF_combine_0LHS()),Rewriter(HFF2FF_combine_0RHS())),(Matcher(HFF2FF_combine_1LHS()),Rewriter(HFF2FF_combine_1RHS()))]

        # self.ruleTraceCheckers = {self.transformation[0][0].name: None,
        #                           self.transformation[0][1].name: None,
        #                           self.transformation[0][2].name: None,
        #                           self.transformation[1][0].name: Matcher(HSM2SM_trace_checkLHS()),
        #                           self.transformation[1][1].name: Matcher(HSF2SF_trace_checkLHS()),
        #                           self.transformation[1][2].name: Matcher(HMM2MM_trace_checkLHS()),
        #                           self.transformation[1][3].name: Matcher(HFF2FF_trace_checkLHS())}
        #

        #print(self.matchRulePatterns)

        #TODO: the rewriters are incorrect, make them correct
        self.matchRulePatterns[self.transformation[0][0].name][1] = Rewriter(HS2S_combineRHS())

        # self.matchRulePatterns = {self.transformation[0][0].name: (Matcher(HS2S_combineLHS()),Rewriter(HS2S_combineRHS())),
        #                           self.transformation[0][1].name: (Matcher(HM2M_combineLHS()),Rewriter(HM2M_combineRHS())),
        #                           self.transformation[0][2].name: (Matcher(HF2F_combineLHS()),Rewriter(HF2F_combineRHS())),
        #                           self.transformation[1][0].name: (Matcher(HSM2SM_combine_1LHS()),Rewriter(HSM2SM_combine_1RHS())),
        #                           self.transformation[1][1].name: (Matcher(HSF2SF_combine_1LHS()),Rewriter(HSF2SF_combine_1RHS())),
        #                           self.transformation[1][2].name: (Matcher(HMM2MM_combine_1LHS()),Rewriter(HMM2MM_combine_1RHS())),
        #                           self.transformation[1][3].name: (Matcher(HFF2FF_combine_1LHS()),Rewriter(HFF2FF_combine_1RHS()))}

        #print(self.matchRulePatterns)


#         self.ruleCombinators = {self.transformation[0][0]: None,
#                                 self.transformation[0][1]: None,
#                                 self.transformation[0][2]: None}

#         self.backwardPatternsComplete = {
#             self.transformation[0][0]: None,
#             self.transformation[0][1]: None,
#             self.transformation[0][2]: None,
#             self.transformation[1][0]: [Matcher(HSM2SMBackComplete_run1LHS())],
#             self.transformation[1][1]: [Matcher(HSF2SFBackComplete_run1LHS())],
#             self.transformation[1][2]: [Matcher(HMM2MMBackComplete_run1LHS())],
#             self.transformation[1][3]: [Matcher(HFF2FFBackComplete_run1LHS())]}
        
#         self.backwardPatternsComplete = {
#             self.transformation[0][0]: None,
#             self.transformation[0][1]: None,
#             self.transformation[0][2]: None}

#         [rules, self.backwardPatterns, self.backwardPatterns2Rules, self.backwardPatternsComplete, self.matchRulePatterns] = \
#                 pyramify.ramify_directory("police_station_transformation/run1/transformation/", True)


        #print(self.rules)

#     def test_matching(self):
#         build_traceability_for_rule = FRule(HBuildTraceabilityForRuleLHS(), HBuildTraceabilityForRuleRHS())
#         
#         p = Packet()
#         p.graph = self.rules['HS2S_run1']
#         p = build_traceability_for_rule.packet_in(p)
#         if (build_traceability_for_rule.is_success):
#             print("Yes!!!")
#         else:
#             print("No")
#         m = Matcher(HSM2SMBackS2S_run1LHS())
#         m.packet_in(p)
#         if (m.is_success):
#             print("Yes!!!")
#         else:
#             print("No")

    
    def test_correct_police_station(self):

        pre_metamodel = ["MT_pre__PoliceStationMM", "MoTifRule"]
        post_metamodel = ["MT_post__PoliceStationMM", "MoTifRule"]
        subclasses_source = ["MT_pre__Station_S", "MT_pre__Male_S","MT_pre__Female_S"]
        subclasses_target = ["MT_pre__Station_T","MT_pre__Male_T","MT_pre__Female_T"]
 
        pyramify = PyRamify()

        #pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)

        print("create state space")
        s = PathConditionGenerator(self.transformation, self.ruleCombinators, self.ruleTraceCheckers, \
                                   self.matchRulePatterns, 2)
 
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
 
#         tv00 = time.time()
#         #s.verify_property(HFSMIsolated_run1LHS(), HFSMConnected_run1LHS(), HFSMComplete_run1LHS())
#         pos = AtomicStateProperty(HFSMIsolated_run1LHS(), HFSMConnected_run1LHS(), HFSMComplete_run1LHS())
#         finalresult = StateProperty.verifyCompositeStateProperty(s, pos)
#         print('finalresult : ')
#         print(finalresult)
#         tv01 = time.time()
#  
#         tv10 = time.time()
#         #s.verify_property(HF2FFIsolated_run1LHS(), HF2FFConnected_run1LHS(), HF2FFComplete_run1LHS())
#         neg = AtomicStateProperty(HF2FFIsolated_run1LHS(), HF2FFConnected_run1LHS(), HF2FFComplete_run1LHS())
#         finalresult = StateProperty.verifyCompositeStateProperty(s, neg)
#         print('finalresult : ')
#         print(finalresult)
#         tv11 = time.time()
 
        print("Time to build the set of path conditions: " + str(ts1 - ts0))
        print("Size of the set of path conditions: " + str(sys.getsizeof(s.pathConditionSet) / 1024))
        print("Number of path conditions: " + str(len(s.pathConditionSet)))
#         print
#         '\n'
#         print
#         'Time to verify True property: ' + str(tv01 - tv00)
#         print
#         '\n'
#         print
#         'Time to verify False property: ' + str(tv11 - tv10)
 
 
        print("printing path conditions")
        s.print_path_conditions_screen()
         
        s.print_path_conditions_file()        

          
          
        ####REAL EXPERIMENTATION: Proving the 4 types of constraints in our MODELS paper
        # The naming convention used for the properties (i.e., P1, P2..ETC) are the 
        # same convention used in my MODELS paper in Table 2.
 
 
        #print("create property")
        # P1atomic=AtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
        # P2atomic=AtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
        # S1IfClause=AtomicStateProperty(HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseCompleteLHS())
        # S1ThenClause=AtomicStateProperty(HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseCompleteLHS())
        # M1IfClause=AtomicStateProperty(HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseCompleteLHS())
        # M1ThenClause=AtomicStateProperty(HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1CompleteLHS())
        # M3IfClause=AtomicStateProperty(HM3IfClauseIsolatedConnectedLHS(),HM3IfClauseIsolatedConnectedLHS(), HM3IfClauseCompleteLHS())
        # M3ThenClause=AtomicStateProperty(HM3ThenClausePart1IsolatedConnectedLHS(), HM3ThenClausePart1IsolatedConnectedLHS(),HM3ThenClausePart1CompleteLHS())
        # M2IfClause=AtomicStateProperty(HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseCompleteLHS())
        # M2ThenClause=AndStateProperty(AtomicStateProperty(HM2ThenClausePart1IsolatedConnectedLHS(),HM2ThenClausePart1IsolatedConnectedLHS(), HM2ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2CompleteLHS())))
        # M4IfClause=AtomicStateProperty(HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseCompleteLHS())
        # M4ThenClause=AndStateProperty(AtomicStateProperty(HM4ThenClausePart1IsolatedConnectedLHS(),HM4ThenClausePart1IsolatedConnectedLHS(), HM4ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2CompleteLHS())))
        # M5IfClause=AtomicStateProperty(HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseCompleteLHS())
        # M5ThenClause=AndStateProperty(AtomicStateProperty(HM5ThenClausePart1IsolatedConnectedLHS(),HM5ThenClausePart1IsolatedConnectedLHS(), HM5ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2CompleteLHS())))
        # M6IfClause=AtomicStateProperty(HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseCompleteLHS())
        # M6ThenClause=AndStateProperty(AtomicStateProperty(HM6ThenClausePart1IsolatedConnectedLHS(),HM6ThenClausePart1IsolatedConnectedLHS(), HM6ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2CompleteLHS())))
         
        #andprop=AndStateProperty(AndStateProperty(atomic1,atomic2),atomic1)
        #P1atomicOldImpl=BKUPAtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
        #P2atomicOldImpl=BKUPAtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
         
#        trivatomicprop=AtomicStateProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
         
        #NOTE: Even if you are verifying an ANDstateProperty where the 2 operands are the same AtomicStateProperty, then store two copies of the AtomicStateProperty in 2 different variables
        #Why? variables in this case are references to objects. So if you want the 2 copies of the same AtomicStateProperty to have different values set for certain attributes, then you must store them in 2 different variables
#        trivnegativeprop=AtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
#        trivnegativepropcopy=AtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
#        trivatomicpropOldImpl=BKUPAtomicStateProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
#        trivnegativepropOldImpl=BKUPAtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
#        IsolHasNoMatch=AtomicStateProperty(HIsolHasNoMatchIsolatedLHS(), HIsolHasNoMatchConnectedLHS(), HIsolHasNoMatchCompleteLHS())
        #trivnegativepropOldImpl.verify(s)
        #finalresult=StateProperty.verifyCompositeStateProperty(s, P1atomic)
        #StateProperty.verifyCompositeStateProperty(s, OrStateProperty(P2atomic,trivnegativeprop))
        #finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(M5IfClause, M5ThenClause))
        #finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(S1IfClause,S1ThenClause))
        #print ('finalresult : ')
        #print (finalresult)
        
        #Experimenting with using framework1 and framework 2 together
        #Not(StateProperty.verifyCompositeStateProperty(s, OrStateProperty(trivnegativeprop,trivnegativeprop))).verify()
        #Or(   StateProperty.verifyCompositeStateProperty(s, OrStateProperty(P1atomic,P2atomic))   ,   StateProperty.verifyCompositeStateProperty(s, OrStateProperty(trivnegativeprop, trivnegativeprop))   ).verify()
        
        ###DUMMY EXPERIMENTATION: Verifying simple atomic formulae and propositional logic formulae
        ###To verify AtomicProp only use the following two lines:
        #AtomicProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS()).verify(s)
        #simpleProp=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #simpleProp.verify(s)
        
        ###To verify NotProp, use the following lines
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #NotProperty(atomicProperty).verify(s)
        
        ###To verify AndProp, use the following lines
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #AndProperty(atomicProperty,atomicProperty).verify(s)
        
        ###To verify OrProp, use the following lines
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #OrProperty(atomicProperty,atomicProperty).verify(s)
        
        ###To verify ImplicationProp, use the following lines
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #ImplicationProperty(atomicProperty,atomicProperty).verify(s)
        
        ###To verify complex propositional logic formulae, use the following lines
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #OrProperty(NotProperty(atomicProperty),atomicProperty).verify(s)
        
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #AndProperty(NotProperty(atomicProperty),atomicProperty).verify(s)
        
        #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #ImplicationProperty(NotProperty(atomicProperty),NotProperty(atomicProperty)).verify(s)
        
        ###To verify 2 properties in 1 complex propositional logic formulae, use the following lines
        #atomicprop1=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
        #atomicprop2=AtomicProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
        #OrProperty(NotProperty(atomicprop1),NotProperty(atomicprop2)).verify(s)
        #ImplicationProperty(NotProperty(atomicprop1),atomicprop2).verify(s)
        
        #ORIGINAL CODE FROM LEVI 
        #transformation = [[HMapDistributable(), HMapECU2FiveElements(), HMapVirtualDevice()],
        #                  [HConnECU2VirtualDevice(), HConnVirtualDeviceToDistributable()],
        #                  [HConnectPPortPrototype(), HConnectRPortPrototype()]]
        #
        #rulesIncludingBackLinks = [[],\
        #                            [transformation[1][0], transformation[1][1]],\
        #                            [transformation[2][0], transformation[2][1]]]
        #
        #s = PathConditionGenerator(transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
        #self.overlapRulePatterns, self.multipleSameBackwardLinkRule, 1, False)
        #s.build_path_conditions()
        #
        #self._print_states(s)
        #print '\n'
        #print 'Built ' + str(len(s.symbStateSpace)) + ' states.'
        #
        #s.verify_property(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()

