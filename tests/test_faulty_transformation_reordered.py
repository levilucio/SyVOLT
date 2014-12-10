'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time
import sys

from symbolic_state_space import SymbolicStateSpace

from t_core.matcher import Matcher
from t_core.messages import Packet

from himesis_utils import graph_to_dot
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules

####GEHANs IMPORTS for GM2AUTOSAR transformation -START
## transformation -start
from GM2AUTOSAR_MM.transformation.Himesis.HConnectPPortPrototype import HConnectPPortPrototype
from GM2AUTOSAR_MM.transformation.Himesis.HConnectRPortPrototype import HConnectRPortPrototype
from GM2AUTOSAR_MM.transformation.Himesis.HConnECU2VirtualDevice import HConnECU2VirtualDevice
from GM2AUTOSAR_MM.transformation.Himesis.HConnVirtualDeviceToDistributable import HConnVirtualDeviceToDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HMapDistributable import HMapDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HMapECU2FiveElements import HMapECU2FiveElements
from GM2AUTOSAR_MM.transformation.Himesis.HMapVirtualDevice import HMapVirtualDevice
from GM2AUTOSAR_MM.transformation.Himesis.HMapECU2FiveElementsFAULTY import HMapECU2FiveElementsFAULTY
from GM2AUTOSAR_MM.transformation.Himesis.HMapVirtualDeviceFAULTY import HMapVirtualDeviceFAULTY

## transformation -end
##Backward Matchers -start
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectPPortPrototype_Back_CompositionType2ECULHS import HConnectPPortPrototype_Back_CompositionType2ECULHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectRPortPrototype_Back_CompositionType2ECULHS import HConnectRPortPrototype_Back_CompositionType2ECULHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_EcuInst2ECULHS import HConnECU2VirtualDevice_Back_EcuInst2ECULHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS import HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_SystemMapping2ECULHS import HConnECU2VirtualDevice_Back_SystemMapping2ECULHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS import HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS import HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS import HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS import HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS
##Backward Matchers -end

##Backward Matchers Complete -start
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectPPortPrototype_Back_CompleteLHS import HConnectPPortPrototype_Back_CompleteLHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectRPortPrototype_Back_CompleteLHS import HConnectRPortPrototype_Back_CompleteLHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_CompleteLHS import HConnECU2VirtualDevice_Back_CompleteLHS
from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_CompleteLHS import HConnVirtualDevice2Distributable_Back_CompleteLHS
##Backward Matchers Complete-end

##Properties -start
from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUVDDistCompleteLHS import HECUVDDistCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUVDDistConnectedLHS import HECUVDDistConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUVDDistIsolatedLHS import HECUVDDistIsolatedLHS 
from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUSysTrivialTrueIsolatedLHS import HECUSysTrivialTrueIsolatedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUSysTrivialTrueConnectedLHS import HECUSysTrivialTrueConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUSysTrivialTrueCompleteLHS import HECUSysTrivialTrueCompleteLHS

#Properties from he MODELS paper
from GM2AUTOSAR_MM.Properties.positive.Himesis.HP1IsolatedLHS import HP1IsolatedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HP1ConnectedLHS import HP1ConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HP1CompleteLHS import HP1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HP2IsolatedLHS import HP2IsolatedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HP2ConnectedLHS import HP2ConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HP2CompleteLHS import HP2CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HS1IfClauseIsolatedConnectedLHS import HS1IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HS1IfClauseCompleteLHS import HS1IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HS1ThenClauseIsolatedConnectedLHS import HS1ThenClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HS1ThenClauseCompleteLHS import HS1ThenClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM1IfClauseIsolatedConnectedLHS import HM1IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM1IfClauseCompleteLHS import HM1IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM1ThenClausePart1IsolatedConnectedLHS import HM1ThenClausePart1IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM1ThenClausePart1CompleteLHS import HM1ThenClausePart1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM3IfClauseIsolatedConnectedLHS import HM3IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM3IfClauseCompleteLHS import HM3IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM3ThenClausePart1IsolatedConnectedLHS import HM3ThenClausePart1IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM3ThenClausePart1CompleteLHS import HM3ThenClausePart1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM2IfClauseIsolatedConnectedLHS import HM2IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM2IfClauseCompleteLHS import HM2IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM2ThenClausePart1IsolatedConnectedLHS import HM2ThenClausePart1IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM2ThenClausePart1CompleteLHS import HM2ThenClausePart1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM2ThenClausePart2IsolatedConnectedLHS import HM2ThenClausePart2IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM2ThenClausePart2CompleteLHS import HM2ThenClausePart2CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM4IfClauseIsolatedConnectedLHS import HM4IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM4IfClauseCompleteLHS import HM4IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM4ThenClausePart1IsolatedConnectedLHS import HM4ThenClausePart1IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM4ThenClausePart1CompleteLHS import HM4ThenClausePart1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM4ThenClausePart2IsolatedConnectedLHS import HM4ThenClausePart2IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM4ThenClausePart2CompleteLHS import HM4ThenClausePart2CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM5IfClauseIsolatedConnectedLHS import HM5IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM5IfClauseCompleteLHS import HM5IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM5ThenClausePart1IsolatedConnectedLHS import HM5ThenClausePart1IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM5ThenClausePart1CompleteLHS import HM5ThenClausePart1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM5ThenClausePart2IsolatedConnectedLHS import HM5ThenClausePart2IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM5ThenClausePart2CompleteLHS import HM5ThenClausePart2CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM6IfClauseIsolatedConnectedLHS import HM6IfClauseIsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM6IfClauseCompleteLHS import HM6IfClauseCompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM6ThenClausePart1IsolatedConnectedLHS import HM6ThenClausePart1IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM6ThenClausePart1CompleteLHS import HM6ThenClausePart1CompleteLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM6ThenClausePart2IsolatedConnectedLHS import HM6ThenClausePart2IsolatedConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HM6ThenClausePart2CompleteLHS import HM6ThenClausePart2CompleteLHS

#A property that should trivially NOT hold
from GM2AUTOSAR_MM.Properties.negative.Himesis.HTrivialFalseECUplusSystem1IsolatedLHS import HTrivialFalseECUplusSystem1IsolatedLHS
from GM2AUTOSAR_MM.Properties.negative.Himesis.HTrivialFalseECUplusSystem1ConnectedLHS import HTrivialFalseECUplusSystem1ConnectedLHS
from GM2AUTOSAR_MM.Properties.negative.Himesis.HTrivialFalseECUplusSystem1CompleteLHS import HTrivialFalseECUplusSystem1CompleteLHS

#A property with an Isolated pattern that has no matches - added for experimentation, has no significant meaning
from GM2AUTOSAR_MM.Properties.positive.Himesis.HIsolHasNoMatchIsolatedLHS import HIsolHasNoMatchIsolatedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HIsolHasNoMatchConnectedLHS import HIsolHasNoMatchConnectedLHS
from GM2AUTOSAR_MM.Properties.positive.Himesis.HIsolHasNoMatchCompleteLHS import HIsolHasNoMatchCompleteLHS

##Properties -end
####GEHANs IMPORTS for GM2AUTOSAR transformation -END

# rule overlap imports
from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnectPPortPrototype_overlapLHS import HConnectPPortPrototype_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnectRPortPrototype_overlapLHS import HConnectRPortPrototype_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnECU2VirtualDevice_overlapLHS import HConnECU2VirtualDevice_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnVirtualDeviceToDistributable_overlapLHS import HConnVirtualDeviceToDistributable_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapDistributable_overlapLHS import HMapDistributable_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapECU2FiveElements_overlapLHS import HMapECU2FiveElements_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapVirtualDevice_overlapLHS import HMapVirtualDevice_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapECU2FiveElementsFAULTY_overlapLHS import HMapECU2FiveElementsFAULTY_overlapLHS
from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapVirtualDeviceFAULTY_overlapLHS import HMapVirtualDeviceFAULTY_overlapLHS

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

class Test(unittest.TestCase):

    def setUp(self):
        
        ConnectPPortPrototype_Back_CompositionType2ECU = Matcher(HConnectPPortPrototype_Back_CompositionType2ECULHS())
        ConnectRPortPrototype_Back_CompositionType2ECU = Matcher(HConnectRPortPrototype_Back_CompositionType2ECULHS())
        ConnECU2VirtualDevice_Back_EcuInst2ECU = Matcher(HConnECU2VirtualDevice_Back_EcuInst2ECULHS())
        ConnECU2VirtualDevice_Back_STEM2VirtualDevice = Matcher(HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS())
        ConnECU2VirtualDevice_Back_SystemMapping2ECU = Matcher(HConnECU2VirtualDevice_Back_SystemMapping2ECULHS())
        ConnVirtualDevice2Distributable_Back_ComponentPrototype2Distributable = Matcher(HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS())
        ConnVirtualDevice2Distributable_Back_CompositionType2ECU = Matcher(HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS())
        ConnVirtualDevice2Distributable_Back_SCTEMc2Distributable = Matcher(HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS())
        ConnVirtualDevice2Distributable_Back_STEM2VirtualDevice = Matcher(HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS())

        self.rules = {                'HMapECU2FiveElementsFAULTY': HMapECU2FiveElementsFAULTY(),
                                      'HMapDistributable': HMapDistributable(),
                                      'HMapVirtualDeviceFAULTY': HMapVirtualDeviceFAULTY(),
                                      'HConnectPPortPrototype': HConnectPPortPrototype(),
                                      'HConnectRPortPrototype': HConnectRPortPrototype(),
                                      'HConnECU2VirtualDevice': HConnECU2VirtualDevice(),
                                      'HConnVirtualDeviceToDistributable': HConnVirtualDeviceToDistributable()}

        self.backwardPatterns = {     'HMapECU2FiveElementsFAULTY': [],
                                      'HMapDistributable': [],
                                      'HMapVirtualDeviceFAULTY': [],
                                      'HConnectPPortPrototype': [ConnectPPortPrototype_Back_CompositionType2ECU],
                                      'HConnectRPortPrototype': [ConnectRPortPrototype_Back_CompositionType2ECU],
                                      'HConnECU2VirtualDevice': [ConnECU2VirtualDevice_Back_EcuInst2ECU, ConnECU2VirtualDevice_Back_STEM2VirtualDevice, ConnECU2VirtualDevice_Back_SystemMapping2ECU],
                                      'HConnVirtualDeviceToDistributable': [ConnVirtualDevice2Distributable_Back_ComponentPrototype2Distributable, ConnVirtualDevice2Distributable_Back_CompositionType2ECU, ConnVirtualDevice2Distributable_Back_SCTEMc2Distributable, ConnVirtualDevice2Distributable_Back_STEM2VirtualDevice]}
         
        self.backwardPatterns2Rules = {
                                      ConnectPPortPrototype_Back_CompositionType2ECU: 'HConnectPPortPrototype',
                                      ConnectRPortPrototype_Back_CompositionType2ECU: 'HConnectRPortPrototype',
                                      ConnECU2VirtualDevice_Back_EcuInst2ECU: 'HConnECU2VirtualDevice',
                                      ConnECU2VirtualDevice_Back_STEM2VirtualDevice: 'HConnECU2VirtualDevice',
                                      ConnECU2VirtualDevice_Back_SystemMapping2ECU: 'HConnECU2VirtualDevice',
                                      ConnVirtualDevice2Distributable_Back_ComponentPrototype2Distributable: 'HConnVirtualDeviceToDistributable', 
                                      ConnVirtualDevice2Distributable_Back_CompositionType2ECU: 'HConnVirtualDeviceToDistributable', 
                                      ConnVirtualDevice2Distributable_Back_SCTEMc2Distributable: 'HConnVirtualDeviceToDistributable', 
                                      ConnVirtualDevice2Distributable_Back_STEM2VirtualDevice: 'HConnVirtualDeviceToDistributable'}
        
        self.backwardPatternsComplete = {
                                      'HMapECU2FiveElementsFAULTY': [],
                                      'HMapDistributable': [],
                                      'HMapVirtualDeviceFAULTY': [],
                                      'HConnectPPortPrototype': [Matcher(HConnectPPortPrototype_Back_CompleteLHS())],
                                      'HConnectRPortPrototype': [Matcher(HConnectRPortPrototype_Back_CompleteLHS())],
                                      'HConnECU2VirtualDevice': [Matcher(HConnECU2VirtualDevice_Back_CompleteLHS())],
                                      'HConnVirtualDeviceToDistributable': [Matcher(HConnVirtualDevice2Distributable_Back_CompleteLHS())]}
        
        self.matchRulePatterns = {    'HMapECU2FiveElementsFAULTY': Matcher(HMapECU2FiveElementsFAULTY_overlapLHS()),
                                      'HMapDistributable': Matcher(HMapDistributable_overlapLHS()),
                                      'HMapVirtualDeviceFAULTY': Matcher(HMapVirtualDeviceFAULTY_overlapLHS()),
                                      'HConnectPPortPrototype': Matcher(HConnectPPortPrototype_overlapLHS()),
                                      'HConnectRPortPrototype': Matcher(HConnectRPortPrototype_overlapLHS()),
                                      'HConnECU2VirtualDevice': Matcher(HConnECU2VirtualDevice_overlapLHS()),
                                      'HConnVirtualDeviceToDistributable': Matcher(HConnVirtualDeviceToDistributable_overlapLHS())}       



    def test_faulty_GM_transformation(self):
        
        transformation = [[self.rules['HMapDistributable'], self.rules['HMapECU2FiveElementsFAULTY'], self.rules['HMapVirtualDeviceFAULTY']],
                          [self.rules['HConnECU2VirtualDevice'], self.rules['HConnVirtualDeviceToDistributable'], self.rules['HConnectPPortPrototype'], self.rules['HConnectRPortPrototype']]]
        
        rulesIncludingBackLinks = [[],\
                                   [transformation[1][0], transformation[1][1], transformation[1][2], transformation[1][3]]]

        s = SymbolicStateSpace(self.rules, transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
                               self.backwardPatternsComplete, self.matchRulePatterns, 1, False)        

        s.build_symbolic_state_space()
        
        self._print_states(s)
        
        print '\n-------------------------------------------------------------'
        
#        graph_to_dot('symbolic_exec', s.symbStateSpace[4][0], 1) 
        
        
        ####REAL EXPERIMENTATION: Proving the 4 types of constraints in our MODELS paper
        # The naming convention used for the properties (i.e., P1, P2..ETC) are the 
        # same convention used in my MODELS paper in Table 2.
        
        P1atomic=AtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
        P2atomic=AtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
        S1IfClause=AtomicStateProperty(HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseCompleteLHS())
        S1ThenClause=AtomicStateProperty(HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseCompleteLHS())
        M1IfClause=AtomicStateProperty(HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseCompleteLHS())
        M1ThenClause=AtomicStateProperty(HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1CompleteLHS())
        M3IfClause=AtomicStateProperty(HM3IfClauseIsolatedConnectedLHS(),HM3IfClauseIsolatedConnectedLHS(), HM3IfClauseCompleteLHS())
        M3ThenClause=AtomicStateProperty(HM3ThenClausePart1IsolatedConnectedLHS(), HM3ThenClausePart1IsolatedConnectedLHS(),HM3ThenClausePart1CompleteLHS())
        M2IfClause=AtomicStateProperty(HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseCompleteLHS())
        M2ThenClause=AndStateProperty(AtomicStateProperty(HM2ThenClausePart1IsolatedConnectedLHS(),HM2ThenClausePart1IsolatedConnectedLHS(), HM2ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2CompleteLHS())))
        M4IfClause=AtomicStateProperty(HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseCompleteLHS())
        M4ThenClause=AndStateProperty(AtomicStateProperty(HM4ThenClausePart1IsolatedConnectedLHS(),HM4ThenClausePart1IsolatedConnectedLHS(), HM4ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2CompleteLHS())))
        M5IfClause=AtomicStateProperty(HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseCompleteLHS())
        M5ThenClause=AndStateProperty(AtomicStateProperty(HM5ThenClausePart1IsolatedConnectedLHS(),HM5ThenClausePart1IsolatedConnectedLHS(), HM5ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2CompleteLHS())))
        M6IfClause=AtomicStateProperty(HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseCompleteLHS())
        M6ThenClause=AndStateProperty(AtomicStateProperty(HM6ThenClausePart1IsolatedConnectedLHS(),HM6ThenClausePart1IsolatedConnectedLHS(), HM6ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2CompleteLHS())))
#        
#        #andprop=AndStateProperty(AndStateProperty(atomic1,atomic2),atomic1)
#        #P1atomicOldImpl=BKUPAtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
#        #P2atomicOldImpl=BKUPAtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
#        
#        trivatomicprop=AtomicStateProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
#        
#        #NOTE: Even if you are verifying an ANDstateProperty where the 2 operands are the same AtomicStateProperty, then store two copies of the AtomicStateProperty in 2 different variables
#        #Why? variables in this case are references to objects. So if you want the 2 copies of the same AtomicStateProperty to have different values set for certain attributes, then you must store them in 2 different variables
#        trivnegativeprop=AtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
#        trivnegativepropcopy=AtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
#        trivatomicpropOldImpl=BKUPAtomicStateProperty(HECUSysTrivialTrueIsolatedLHS(),HECUSysTrivialTrueConnectedLHS(), HECUSysTrivialTrueCompleteLHS())
#        trivnegativepropOldImpl=BKUPAtomicStateProperty(HTrivialFalseECUplusSystem1IsolatedLHS(),HTrivialFalseECUplusSystem1ConnectedLHS(),HTrivialFalseECUplusSystem1CompleteLHS())
#        IsolHasNoMatch=AtomicStateProperty(HIsolHasNoMatchIsolatedLHS(), HIsolHasNoMatchConnectedLHS(), HIsolHasNoMatchCompleteLHS())
#        #trivnegativepropOldImpl.verify(s)
#        #finalresult=StateProperty.verifyCompositeStateProperty(s, P1atomic)
#        #StateProperty.verifyCompositeStateProperty(s, OrStateProperty(P2atomic,trivnegativeprop))
        finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(M4IfClause, M4ThenClause))
#        finalresult=StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(S1IfClause,S1ThenClause))
        print ('finalresult : ')
        print (finalresult)
        
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
        #s = SymbolicStateSpace(transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
        #self.overlapRulePatterns, self.multipleSameBackwardLinkRule, 1, False)
        #s.build_symbolic_state_space()
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
                    print s


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
    