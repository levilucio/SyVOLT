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

from himesis_utils import graph_to_dot
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
from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
#from lib2to3.fixer_util import p1


from police_station_transformation.property.run1.positive.HTestLHS import HTestLHS
from police_station_transformation.property.run1.positive.HFSMIsolated_run1LHS import HFSMIsolated_run1LHS
from police_station_transformation.property.run1.positive.HFSMConnected_run1LHS import HFSMConnected_run1LHS
from police_station_transformation.property.run1.positive.HFSMComplete_run1LHS import HFSMComplete_run1LHS

from police_station_transformation.property.run1.negative.HF2FFIsolated_run1LHS import HF2FFIsolated_run1LHS
from police_station_transformation.property.run1.negative.HF2FFConnected_run1LHS import HF2FFConnected_run1LHS
from police_station_transformation.property.run1.negative.HF2FFComplete_run1LHS import HF2FFComplete_run1LHS

class Test(unittest.TestCase):

    def setUp(self):
        pyramify = PyRamify()
        [self.rules, self.backwardPatterns, self.backwardPatterns2Rules, self.backwardPatternsComplete, self.matchRulePatterns] = pyramify.ramify_directory("police_station_transformation/run1/transformation/", True)

        print(self.rules)

    def test_correct_police_station(self):

        transformation = [[self.rules['HS2S_run1'],self.rules['HM2M_run1'],self.rules['HF2F_run1']],
                          [self.rules['HSM2SM_run1'], self.rules['HMM2MM_run1'], self.rules['HSF2SF_run1'], self.rules['HFF2FF_run1']]]

        #transformation = [[HS2S_run1(), HM2M_run1(), HF2F_run1()], [HSM2SM_run1(), HMM2MM_run1(), HSF2SF_run1(), HFF2FF_run1()]]
        rulesIncludingBackLinks = [[], [transformation[1][0], transformation[1][1], transformation[1][2], transformation[1][3]]]


        #rulesIncludingBackLinks = [[]]


        print("create state space")
        s = PathConditionGenerator(self.rules, transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
                               self.backwardPatternsComplete, self.matchRulePatterns, 2, False)

        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()

        tv00 = time.time()
        #s.verify_property(HFSMIsolated_run1LHS(), HFSMConnected_run1LHS(), HFSMComplete_run1LHS())
        pos = AtomicStateProperty(HFSMIsolated_run1LHS(), HFSMConnected_run1LHS(), HFSMComplete_run1LHS())
        finalresult = StateProperty.verifyCompositeStateProperty(s, pos)
        print('finalresult : ')
        print(finalresult)
        tv01 = time.time()

        tv10 = time.time()
        #s.verify_property(HF2FFIsolated_run1LHS(), HF2FFConnected_run1LHS(), HF2FFComplete_run1LHS())
        neg = AtomicStateProperty(HF2FFIsolated_run1LHS(), HF2FFConnected_run1LHS(), HF2FFComplete_run1LHS())
        finalresult = StateProperty.verifyCompositeStateProperty(s, neg)
        print('finalresult : ')
        print(finalresult)
        tv11 = time.time()

        print
        'Time to build symbolic execution: ' + str(ts1 - ts0)
        print
        'Symbolic execution size: ' + str(sys.getsizeof(s.symbStateSpace) / 1024)
        print
        'Number of states: ' + str(len(s.symbStateSpace))
        print
        '\n'
        print
        'Time to verify True property: ' + str(tv01 - tv00)
        print
        '\n'
        print
        'Time to verify False property: ' + str(tv11 - tv10)


        print("printing states")
        self._print_states(s)
        
#         graph_to_dot('symbolic_exec', s.symbStateSpace[1][0], 1) 
         
         
        ####REAL EXPERIMENTATION: Proving the 4 types of constraints in our MODELS paper
        # The naming convention used for the properties (i.e., P1, P2..ETC) are the 
        # same convention used in my MODELS paper in Table 2.


        print("create property")
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


    def _print_states(self,s):
        for state in s.symbStateSpace:
            print "----------"
            if state == ():
                print 'Empty'
            else:
                for s in state:
                    print s.name


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
    
