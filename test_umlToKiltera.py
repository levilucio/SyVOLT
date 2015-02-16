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

from UMLRT2Kiltera_MM.Properties.positive.Himesis.HState2procdef_IsolatedLHS import HState2procdef_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HState2procdef_CompleteLHS import HState2procdef_CompleteLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HExitpoint2procdefparTrue_IsolatedLHS import HExitpoint2procdefparTrue_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HExitpoint2procdefparTrue_ConnectedLHS import HExitpoint2procdefparTrue_ConnectedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HExitpoint2procdefparTrue_CompleteLHS import HExitpoint2procdefparTrue_CompleteLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HExitpoint2procdefparTrueNOATTR_IsolatedLHS import HExitpoint2procdefparTrueNOATTR_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HExitpoint2procdefparTrueNOATTR_ConnectedLHS import HExitpoint2procdefparTrueNOATTR_ConnectedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HExitpoint2procdefparTrueNOATTR_CompleteLHS import HExitpoint2procdefparTrueNOATTR_CompleteLHS
from UMLRT2Kiltera_MM.Properties.negative.Himesis.HState2funcdefNEG_CompleteLHS import HState2funcdefNEG_CompleteLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HState2trans2exitptTrue_IsolatedLHS import HState2trans2exitptTrue_IsolatedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HState2trans2exitptTrue_ConnectedLHS import HState2trans2exitptTrue_ConnectedLHS
from UMLRT2Kiltera_MM.Properties.positive.Himesis.HState2trans2exitptTrue_CompleteLHS import HState2trans2exitptTrue_CompleteLHS

class Test(unittest.TestCase):

    def setUp(self):
        pyramify = PyRamify()

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("UMLRT2Kiltera_MM/transformation/Himesis/")

        print("Rules: " + str(self.rules.keys()))


    def test_correct_uml2kiltera(self):

#'HMapHeirarchyOfStates2HeirarchyOfProcs':  'HTransition2QInstSIBLING': < 'HState2HProcDef': 'HCompositeState2ProcDef':  'HTransition2ListenBranch':  'HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans':  'HBasicStateNoOutgoing2ProcDef':  'HBasicState2ProcDef': , 'HState2ProcDef'

#Layer1: State2ProcDef
#Layer2: BasicStateNoOutgoing2ProcDef, BasicState2ProcDef, CompositeState2ProcDef
#Layer3: ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, State2HProcDef
#Layer4: Transition2QInstSIBLING
#Layer5: Transition2ListenBranch
#Layer6: MapHeirarchyOfStates2HeirarchyOfProcs

#         a1 = self.rules['HState2ProcDef']
#         b1 = self.rules['HBasicStateNoOutgoing2ProcDef']
#         b2 = self.rules['HBasicState2ProcDef']
#         b3 = self.rules['HCompositeState2ProcDef']

        pyramify = PyRamify(verbosity = 2)



        a1 = self.rules['HState2ProcDef']
        b1 = self.rules['HBasicStateNoOutgoing2ProcDef']
        b2 = self.rules['HBasicState2ProcDef']
        b3 = self.rules['HCompositeState2ProcDef']
        c1 = self.rules['HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans']
        c2 = self.rules['HState2HProcDef']
        c3 = self.rules['HState2CProcDef']
        d1 = self.rules['HTransition2QInstSIBLING']
        d2 = self.rules['HTransition2QInstOUT']
        d3 = self.rules['HTransition2Inst']
        e1 = self.rules['HTransition2ListenBranch']
        e2 = self.rules['HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst']
        e3 = self.rules['HTransition2HListenBranch']
        e4 = self.rules['HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions']
        f1 = self.rules['HMapHeirarchyOfStates2HeirarchyOfProcs']
            
        #transformation = [[a1], [b1,b2,b3], [c1,c2,c3], [d1,d2,d3], [e1,e2,e3,e4], [f1]]

        
        transformation = [[a1], [b1,b2,b3], [c1,c3]]
        
        #transformation = [[a1], [b1,b2,b3], [c1,c2,c3], [d1,d2,d3], [e1,e2,e3,e4], [f1]]
          
        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]
        subclasses_source = ["MT_pre__OPTIONAL1,","MT_pre__PhysicalThread", "MT_pre__PortRef", "MT_pre__PackageContainer", "MT_pre__Thread", "MT_pre__OUT2", "MT_pre__BASE0",\
                            "MT_pre__NamedElement", "MT_pre__Element", "MT_pre__OUT1", "MT_pre__Signal", "MT_pre__Package", "MT_pre__PortType",\
                            "MT_pre__PortConnectorRef", "MT_pre__IN1", "MT_pre__IN0", "MT_pre__LogicalThread", "MT_pre__RoleType", "MT_pre__Vertex",\
                            "MT_pre__SIBLING0", "MT_pre__InitialPoint", "MT_pre__PortConnector", "MT_pre__SignalType", "MT_pre__Transition",\
                            "MT_pre__EntryPoint", "MT_pre__CONJUGATE1", "MT_pre__Protocol", "MT_pre__StateMachine", "MT_pre__Model_S",\
                            "MT_pre__StateMachineElement", "MT_pre__Port", "MT_pre__TransitionType", "MT_pre__Capsule", "MT_pre__Trigger_S",\
                            "MT_pre__State", "MT_pre__PLUGIN2", "MT_pre__Action", "MT_pre__CapsuleRole", "MT_pre__ExitPoint", "MT_pre__FIXED0"]
        subclasses_target = ["MT_pre__Name", "MT_pre__Module", "MT_pre__ConditionBranch", "MT_pre__Delay", "MT_pre__LocalDef",\
                              "MT_pre__Expr", "MT_pre__ConditionSet", "MT_pre__Proc", "MT_pre__MatchCase", "MT_pre__Match",\
                              "MT_pre__FuncDef", "MT_pre__Null", "MT_pre__Par", "MT_pre__Inst", "MT_pre__Listen", "MT_pre__Site",\
                              "MT_pre__New", "MT_pre__PythonRef", "MT_pre__Def", "MT_pre__Seq", "MT_pre__ParIndexed", "MT_pre__Condition",\
                              "MT_pre__Print", "MT_pre__Pattern", "MT_pre__ListenBranch", "MT_pre__ProcDef", "MT_pre__Trigger_T","MT_pre__Model_T"]
 
   
        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_source, subclasses_target)

        s = PathConditionGenerator(transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, 2)# 
   
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
            
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(len(s.pathConditionSet)))
# # #         print
# # #         '\n'
# # #         print
# # #         'Time to verify True property: ' + str(tv01 - tv00)
# # #         print
# # #         '\n'
# # #         print
# # #         'Time to verify False property: ' + str(tv11 - tv10)
# #  
# #  
        print("printing path conditions")
        s.print_path_conditions_screen()
         
        s.print_path_conditions_file()
        atprop=AtomicStateProperty(HState2procdef_IsolatedLHS(),HState2procdef_IsolatedLHS(), HState2procdef_CompleteLHS())
        exitpt2procdefparprop_withattr=AtomicStateProperty(HExitpoint2procdefparTrue_IsolatedLHS(),HExitpoint2procdefparTrue_ConnectedLHS(),HExitpoint2procdefparTrue_CompleteLHS())
        exitpt2procdefparprop_noattr=AtomicStateProperty(HExitpoint2procdefparTrueNOATTR_IsolatedLHS(),HExitpoint2procdefparTrueNOATTR_ConnectedLHS(),HExitpoint2procdefparTrueNOATTR_CompleteLHS())
        atpropneg=AtomicStateProperty(HState2procdef_IsolatedLHS(), HState2procdef_IsolatedLHS(), HState2funcdefNEG_CompleteLHS())
        atpropNeedscollapse=AtomicStateProperty(HState2trans2exitptTrue_IsolatedLHS(),HState2trans2exitptTrue_ConnectedLHS(),HState2trans2exitptTrue_CompleteLHS())
        finalresult=StateProperty.verifyCompositeStateProperty(s, atpropNeedscollapse)
        print ('finalresult : ')
        print (finalresult)
# 
#         print("printing states")
#         self._print_states(s)
#         
# #         graph_to_dot('symbolic_exec', s.symbStateSpace[1][0], 1) 
#          
#          
#         ####REAL EXPERIMENTATION: Proving the 4 types of constraints in our MODELS paper
#         # The naming convention used for the properties (i.e., P1, P2..ETC) are the 
#         # same convention used in my MODELS paper in Table 2.
# 
# 
#         print("create property")
#         # P1atomic=AtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
#         # P2atomic=AtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
#         # S1IfClause=AtomicStateProperty(HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseCompleteLHS())
#         # S1ThenClause=AtomicStateProperty(HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseCompleteLHS())
#         # M1IfClause=AtomicStateProperty(HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseCompleteLHS())
#         # M1ThenClause=AtomicStateProperty(HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1CompleteLHS())
#         # M3IfClause=AtomicStateProperty(HM3IfClauseIsolatedConnectedLHS(),HM3IfClauseIsolatedConnectedLHS(), HM3IfClauseCompleteLHS())
#         # M3ThenClause=AtomicStateProperty(HM3ThenClausePart1IsolatedConnectedLHS(), HM3ThenClausePart1IsolatedConnectedLHS(),HM3ThenClausePart1CompleteLHS())
#         # M2IfClause=AtomicStateProperty(HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseCompleteLHS())
#         # M2ThenClause=AndStateProperty(AtomicStateProperty(HM2ThenClausePart1IsolatedConnectedLHS(),HM2ThenClausePart1IsolatedConnectedLHS(), HM2ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2CompleteLHS())))
#         # M4IfClause=AtomicStateProperty(HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseCompleteLHS())
#         # M4ThenClause=AndStateProperty(AtomicStateProperty(HM4ThenClausePart1IsolatedConnectedLHS(),HM4ThenClausePart1IsolatedConnectedLHS(), HM4ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2CompleteLHS())))
#         # M5IfClause=AtomicStateProperty(HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseCompleteLHS())
#         # M5ThenClause=AndStateProperty(AtomicStateProperty(HM5ThenClausePart1IsolatedConnectedLHS(),HM5ThenClausePart1IsolatedConnectedLHS(), HM5ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2CompleteLHS())))
#         # M6IfClause=AtomicStateProperty(HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseCompleteLHS())
#         # M6ThenClause=AndStateProperty(AtomicStateProperty(HM6ThenClausePart1IsolatedConnectedLHS(),HM6ThenClausePart1IsolatedConnectedLHS(), HM6ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2CompleteLHS())))
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
#         #finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(M5IfClause, M5ThenClause))
#         #finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(S1IfClause,S1ThenClause))
#         #print ('finalresult : ')
#         #print (finalresult)
#         
#         #Experimenting with using framework1 and framework 2 together
#         #Not(StateProperty.verifyCompositeStateProperty(s, OrStateProperty(trivnegativeprop,trivnegativeprop))).verify()
#         #Or(   StateProperty.verifyCompositeStateProperty(s, OrStateProperty(P1atomic,P2atomic))   ,   StateProperty.verifyCompositeStateProperty(s, OrStateProperty(trivnegativeprop, trivnegativeprop))   ).verify()
#         
#         ###DUMMY EXPERIMENTATION: Verifying simple atomic formulae and propositional logic formulae
#         ###To verify AtomicProp only use the following two lines:
#         #AtomicProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS()).verify(s)
#         #simpleProp=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #simpleProp.verify(s)
#         
#         ###To verify NotProp, use the following lines
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #NotProperty(atomicProperty).verify(s)
#         
#         ###To verify AndProp, use the following lines
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #AndProperty(atomicProperty,atomicProperty).verify(s)
#         
#         ###To verify OrProp, use the following lines
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #OrProperty(atomicProperty,atomicProperty).verify(s)
#         
#         ###To verify ImplicationProp, use the following lines
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #ImplicationProperty(atomicProperty,atomicProperty).verify(s)
#         
#         ###To verify complex propositional logic formulae, use the following lines
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #OrProperty(NotProperty(atomicProperty),atomicProperty).verify(s)
#         
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #AndProperty(NotProperty(atomicProperty),atomicProperty).verify(s)
#         
#         #atomicProperty=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #ImplicationProperty(NotProperty(atomicProperty),NotProperty(atomicProperty)).verify(s)
#         
#         ###To verify 2 properties in 1 complex propositional logic formulae, use the following lines
#         #atomicprop1=AtomicProperty(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())
#         #atomicprop2=AtomicProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
#         #OrProperty(NotProperty(atomicprop1),NotProperty(atomicprop2)).verify(s)
#         #ImplicationProperty(NotProperty(atomicprop1),atomicprop2).verify(s)
#         
#         #ORIGINAL CODE FROM LEVI 
#         #transformation = [[HMapDistributable(), HMapECU2FiveElements(), HMapVirtualDevice()],
#         #                  [HConnECU2VirtualDevice(), HConnVirtualDeviceToDistributable()],
#         #                  [HConnectPPortPrototype(), HConnectRPortPrototype()]]
#         #
#         #rulesIncludingBackLinks = [[],\
#         #                            [transformation[1][0], transformation[1][1]],\
#         #                            [transformation[2][0], transformation[2][1]]]
#         #
#         #s = PathConditionGenerator(transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
#         #self.overlapRulePatterns, self.multipleSameBackwardLinkRule, 1, False)
#         #s.build_path_conditions()
#         #
#         #self._print_states(s)
#         #print '\n'
#         #print 'Built ' + str(len(s.symbStateSpace)) + ' states.'
#         #
#         #s.verify_property(HECUVDDistIsolatedLHS(), HECUVDDistConnectedLHS(), HECUVDDistCompleteLHS())


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
    
