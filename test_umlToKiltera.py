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

class Test(unittest.TestCase):

    def setUp(self):
        pyramify = PyRamify()
        [self.rules, self.backwardPatterns, self.backwardPatterns2Rules, self.backwardPatternsComplete, self.matchRulePatterns] = pyramify.ramify_directory("UMLRT2Kiltera_MM/transformation/Himesis/", True)

        print(self.rules)

    def test_correct_uml2kiltera(self):

#'HMapHeirarchyOfStates2HeirarchyOfProcs':  'HTransition2QInstSIBLING': < 'HState2HProcDef': 'HCompositeState2ProcDef':  'HTransition2ListenBranch':  'HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans':  'HBasicStateNoOutgoing2ProcDef':  'HBasicState2ProcDef': , 'HState2ProcDef'

#Layer1: State2ProcDef
#Layer2: BasicStateNoOutgoing2ProcDef, BasicState2ProcDef, CompositeState2ProcDef
#Layer3: ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, State2HProcDef
#Layer4: Transition2QInstSIBLING
#Layer5: Transition2ListenBranch
#Layer6: MapHeirarchyOfStates2HeirarchyOfProcs

        a1 = self.rules['HState2ProcDef']
        b1 = self.rules['HBasicStateNoOutgoing2ProcDef']
        b2 = self.rules['HBasicState2ProcDef']
        b3 = self.rules['HCompositeState2ProcDef']

        c1 = self.rules['HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans']
        c2 = self.rules['HState2HProcDef']

        d1 = self.rules['HTransition2QInstSIBLING']
        e1 = self.rules['HTransition2ListenBranch']
        f1 = self.rules['HMapHeirarchyOfStates2HeirarchyOfProcs']

        transformation = [[a1], [b1, b2, b3], [c1, c2], [d1], [e1], [f1]]

        pyramify = PyRamify()
        self.rulesIncludingBackLinks = pyramify.getRulesIncludingBackLinks(transformation, self.backwardPatterns)


        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]
        subclasses_source = ["MT_pre__UML"]
        subclasses_target = ["MT_pre__Kiltera"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)

        print("create state space")
        s = PathConditionGenerator(self.rules, transformation, self.rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules, self.backwardPatternsComplete, self.matchRulePatterns, 2, False)


        print("starting build")
        s.build_path_conditions()


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
    
