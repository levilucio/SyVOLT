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
from core.himesis_utils import draw_graphs

from util.test_script_utils import select_rules, slice_transformation

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
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectPPortPrototype_Back_CompositionType2ECULHS import HConnectPPortPrototype_Back_CompositionType2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectRPortPrototype_Back_CompositionType2ECULHS import HConnectRPortPrototype_Back_CompositionType2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_EcuInst2ECULHS import HConnECU2VirtualDevice_Back_EcuInst2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS import HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_SystemMapping2ECULHS import HConnECU2VirtualDevice_Back_SystemMapping2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS import HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS import HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS import HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS import HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS
# ##Backward Matchers -end
#
# ##Backward Matchers Complete -start
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectPPortPrototype_Back_CompleteLHS import HConnectPPortPrototype_Back_CompleteLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectRPortPrototype_Back_CompleteLHS import HConnectRPortPrototype_Back_CompleteLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_CompleteLHS import HConnECU2VirtualDevice_Back_CompleteLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_CompleteLHS import HConnVirtualDevice2Distributable_Back_CompleteLHS
##Backward Matchers Complete-end

##Properties -start

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

# from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUVDDistCompleteLHS import HECUVDDistCompleteLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUVDDistConnectedLHS import HECUVDDistConnectedLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUVDDistIsolatedLHS import HECUVDDistIsolatedLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUSysTrivialTrueIsolatedLHS import HECUSysTrivialTrueIsolatedLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUSysTrivialTrueConnectedLHS import HECUSysTrivialTrueConnectedLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HECUSysTrivialTrueCompleteLHS import HECUSysTrivialTrueCompleteLHS
#
# #Properties from he MODELS paper
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

# #A property that should trivially NOT hold
# from GM2AUTOSAR_MM.Properties.negative.Himesis.HTrivialFalseECUplusSystem1IsolatedLHS import HTrivialFalseECUplusSystem1IsolatedLHS
# from GM2AUTOSAR_MM.Properties.negative.Himesis.HTrivialFalseECUplusSystem1ConnectedLHS import HTrivialFalseECUplusSystem1ConnectedLHS
# from GM2AUTOSAR_MM.Properties.negative.Himesis.HTrivialFalseECUplusSystem1CompleteLHS import HTrivialFalseECUplusSystem1CompleteLHS
#
# #A property with an Isolated pattern that has no matches - added for experimentation, has no significant meaning
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HIsolHasNoMatchIsolatedLHS import HIsolHasNoMatchIsolatedLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HIsolHasNoMatchConnectedLHS import HIsolHasNoMatchConnectedLHS
# from GM2AUTOSAR_MM.Properties.positive.Himesis.HIsolHasNoMatchCompleteLHS import HIsolHasNoMatchCompleteLHS
#
# ##Properties -end
# ####GEHANs IMPORTS for GM2AUTOSAR transformation -END
#
# # rule overlap imports
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnectPPortPrototype_overlapLHS import HConnectPPortPrototype_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnectRPortPrototype_overlapLHS import HConnectRPortPrototype_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnECU2VirtualDevice_overlapLHS import HConnECU2VirtualDevice_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HConnVirtualDeviceToDistributable_overlapLHS import HConnVirtualDeviceToDistributable_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapDistributable_overlapLHS import HMapDistributable_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapECU2FiveElements_overlapLHS import HMapECU2FiveElements_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapVirtualDevice_overlapLHS import HMapVirtualDevice_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapECU2FiveElementsFAULTY_overlapLHS import HMapECU2FiveElementsFAULTY_overlapLHS
# from GM2AUTOSAR_MM.overlap_rules.Himesis.HMapVirtualDeviceFAULTY_overlapLHS import HMapVirtualDeviceFAULTY_overlapLHS

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

class Test():

    def setUp(self,args):
        
        pyramify = PyRamify(verbosity = args.verbosity, draw_svg = args.draw_svg)

        self.do_old_transformation = False

        self.transformation_dir = "GM2AUTOSAR_MM/transformation_w_equations/"

        if self.do_old_transformation:
            self.transformation_dir = "GM2AUTOSAR_MM/transformation"
            full_transformation = [
             ['HMapDistributable', 'HMapECU2FiveElements', 'HMapVirtualDevice'],
             ['HConnECU2VirtualDevice',  'HConnVirtualDeviceToDistributable'],
             ['HConnectPPortPrototype', 'HConnectRPortPrototype']
            ]




        else:
            full_transformation = [
                ['HMapPN2FiveElements', 'HMapPartition', 'HMapModule'],
                ['HConnECU2VirtualDevice1'],
                ['HConnECU2VirtualDevice2'],
                 ['HConnVirtualDevice2Distributable1'],
                 ['HConnVirtualDevice2Distributable2'],
                 ['HConnectRPortPrototype'],
                 ['HConnectPPortPrototype']]


        self.rules, self.transformation = pyramify.get_rules(self.transformation_dir, full_transformation)

        pre_metamodel = ["MT_pre__GM2AUTOSAR_MM", "MoTifRule"]
        post_metamodel = ["MT_post__GM2AUTOSAR_MM", "MoTifRule"]

        # sanitized metamodel
        subclasses_dict = {}
        # subclasses_dict["MT_pre__MetaModelElement_S"] = ["MT_pre__PhysicalNode", "MT_pre__Partition", "MT_pre__Module",
        #                                                  "MT_pre__Scheduler", "MT_pre__Service"]
        # subclasses_dict["MT_pre__MetaModelElement_T"] = ['MT_pre__EcuInstance','MT_pre__System','MT_pre__SystemMapping','MT_pre__ComponentPrototype','MT_pre__SwCompToEcuMapping_component','MT_pre__CompositionType','MT_pre__PPortPrototype','MT_pre__SwcToEcuMapping','MT_pre__SoftwareComposition','MT_pre__RPortPrototype','MT_pre__PortPrototype', 'MT_pre__ComponentType']


        # unsanitized metamodel
        # subclasses_dict = {}

        if self.do_old_transformation:
            subclasses_dict["MT_pre__MetaModelElement_S"] = ["MT_pre__VirtualDevice", 'MT_pre__Distributable',
                                                             'MT_pre__ExecFrame', 'MT_pre__Signal', 'MT_pre__ECU']
        else:
            subclasses_dict["MT_pre__MetaModelElement_S"] = ["MT_pre__PhysicalNode", "MT_pre__Partition",
                                                             "MT_pre__Module",
                                                             "MT_pre__Scheduler", "MT_pre__Service"]

        subclasses_dict["MT_pre__MetaModelElement_T"] = ['MT_pre__EcuInstance', 'MT_pre__System',
                                                         'MT_pre__SystemMapping',
                                                         'MT_pre__ComponentPrototype',
                                                         'MT_pre__SwCompToEcuMapping_component',
                                                         'MT_pre__CompositionType', 'MT_pre__PPortPrototype',
                                                         'MT_pre__SwcToEcuMapping', 'MT_pre__SoftwareComposition',
                                                         'MT_pre__RPortPrototype', 'MT_pre__PortPrototype',
                                                         'MT_pre__ComponentType']

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)



        P1atomic=AtomicStateProperty(HP1IsolatedLHS(),HP1ConnectedLHS(), HP1CompleteLHS())
        P2atomic=AtomicStateProperty(HP2IsolatedLHS(),HP2ConnectedLHS(), HP2CompleteLHS())
        S1IfClause=AtomicStateProperty(HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseIsolatedConnectedLHS(), HS1IfClauseCompleteLHS())
        S1ThenClause=AtomicStateProperty(HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseIsolatedConnectedLHS(), HS1ThenClauseCompleteLHS())

#         if self.do_old_transformation:
#             self.transformation = [
#              [self.rules['HMapDistributable'], self.rules['HMapECU2FiveElements'], self.rules['HMapVirtualDevice']],
#              [self.rules['HConnECU2VirtualDevice'],  self.rules['HConnVirtualDeviceToDistributable']],
#              [self.rules['HConnectPPortPrototype'], self.rules['HConnectRPortPrototype']]]
# 
# 
# 
# 
#         else:
#             self.transformation = [
#                 [self.rules['HMapPN2FiveElements'], self.rules['HMapPartition'], self.rules['HMapModule']],
#                 [self.rules['HConnECU2VirtualDevice1']],
#                 [self.rules['HConnECU2VirtualDevice2']],
#                  [self.rules['HConnVirtualDevice2Distributable1']],
#                  [self.rules['HConnVirtualDevice2Distributable2']],
#                  [self.rules['HConnectPPortPrototype']],
#                  [self.rules['HConnectRPortPrototype']]]

        M1IfClause=AtomicStateProperty(HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseIsolatedConnectedLHS(),HM1IfClauseCompleteLHS())
        M1ThenClause=NotStateProperty(AtomicStateProperty(HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1IsolatedConnectedLHS(),HM1ThenClausePart1CompleteLHS()))
        M3IfClause=AtomicStateProperty(HM3IfClauseIsolatedConnectedLHS(),HM3IfClauseIsolatedConnectedLHS(), HM3IfClauseCompleteLHS())
        M3ThenClause=NotStateProperty(AtomicStateProperty(HM3ThenClausePart1IsolatedConnectedLHS(), HM3ThenClausePart1IsolatedConnectedLHS(),HM3ThenClausePart1CompleteLHS()))


        # 
#         ConnectPPortPrototype_Back_CompositionType2ECU = Matcher(HConnectPPortPrototype_Back_CompositionType2ECULHS())
#         ConnectRPortPrototype_Back_CompositionType2ECU = Matcher(HConnectRPortPrototype_Back_CompositionType2ECULHS())
#         ConnECU2VirtualDevice_Back_EcuInst2ECU = Matcher(HConnECU2VirtualDevice_Back_EcuInst2ECULHS())
#         ConnECU2VirtualDevice_Back_STEM2VirtualDevice = Matcher(HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS())
#         ConnECU2VirtualDevice_Back_SystemMapping2ECU = Matcher(HConnECU2VirtualDevice_Back_SystemMapping2ECULHS())
#         ConnVirtualDevice2Distributable_Back_ComponentPrototype2Distributable = Matcher(HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS())
#         ConnVirtualDevice2Distributable_Back_CompositionType2ECU = Matcher(HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS())
#         ConnVirtualDevice2Distributable_Back_SCTEMc2Distributable = Matcher(HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS())
#         ConnVirtualDevice2Distributable_Back_STEM2VirtualDevice = Matcher(HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS())

#         
#         self.rules = {                'HMapECU2FiveElements': HMapECU2FiveElements(),
#                                       'HMapDistributable': HMapDistributable(),
#                                       'HMapVirtualDevice': HMapVirtualDevice(),
#                                       'HConnectPPortPrototype': HConnectPPortPrototype(),
#                                       'HConnectRPortPrototype': HConnectRPortPrototype(),
#                                       'HConnECU2VirtualDevice': HConnECU2VirtualDevice(),
#                                       'HConnVirtualDeviceToDistributable': HConnVirtualDeviceToDistributable()}

#         self.backwardPatterns = {     'HMapECU2FiveElements': [],
#                                       'HMapDistributable': [],
#                                       'HMapVirtualDevice': [],
#                                       'HConnectPPortPrototype': [ConnectPPortPrototype_Back_CompositionType2ECU],
#                                       'HConnectRPortPrototype': [ConnectRPortPrototype_Back_CompositionType2ECU],
#                                       'HConnECU2VirtualDevice': [ConnECU2VirtualDevice_Back_EcuInst2ECU, ConnECU2VirtualDevice_Back_STEM2VirtualDevice, ConnECU2VirtualDevice_Back_SystemMapping2ECU],
#                                       'HConnVirtualDeviceToDistributable': [ConnVirtualDevice2Distributable_Back_ComponentPrototype2Distributable, ConnVirtualDevice2Distributable_Back_CompositionType2ECU, ConnVirtualDevice2Distributable_Back_SCTEMc2Distributable, ConnVirtualDevice2Distributable_Back_STEM2VirtualDevice]}
#          
#         self.backwardPatterns2Rules = {
#                                       ConnectPPortPrototype_Back_CompositionType2ECU: 'HConnectPPortPrototype',
#                                       ConnectRPortPrototype_Back_CompositionType2ECU: 'HConnectRPortPrototype',
#                                       ConnECU2VirtualDevice_Back_EcuInst2ECU: 'HConnECU2VirtualDevice',
#                                       ConnECU2VirtualDevice_Back_STEM2VirtualDevice: 'HConnECU2VirtualDevice',
#                                       ConnECU2VirtualDevice_Back_SystemMapping2ECU: 'HConnECU2VirtualDevice',
#                                       ConnVirtualDevice2Distributable_Back_ComponentPrototype2Distributable: 'HConnVirtualDeviceToDistributable', 
#                                       ConnVirtualDevice2Distributable_Back_CompositionType2ECU: 'HConnVirtualDeviceToDistributable', 
#                                       ConnVirtualDevice2Distributable_Back_SCTEMc2Distributable: 'HConnVirtualDeviceToDistributable', 
#                                       ConnVirtualDevice2Distributable_Back_STEM2VirtualDevice: 'HConnVirtualDeviceToDistributable'}
#         
#         self.backwardPatternsComplete = {
#                                       'HMapECU2FiveElements': [],
#                                       'HMapDistributable': [],
#                                       'HMapVirtualDevice': [],
#                                       'HConnectPPortPrototype': [Matcher(HConnectPPortPrototype_Back_CompleteLHS())],
#                                       'HConnectRPortPrototype': [Matcher(HConnectRPortPrototype_Back_CompleteLHS())],
#                                       'HConnECU2VirtualDevice': [Matcher(HConnECU2VirtualDevice_Back_CompleteLHS())],
#                                       'HConnVirtualDeviceToDistributable': [Matcher(HConnVirtualDevice2Distributable_Back_CompleteLHS())]}
#         
#         self.matchRulePatterns = {    'HMapECU2FiveElements': Matcher(HMapECU2FiveElements_overlapLHS()),
#                                       'HMapDistributable': Matcher(HMapDistributable_overlapLHS()),
#                                       'HMapVirtualDevice': Matcher(HMapVirtualDevice_overlapLHS()),
#                                       'HConnectPPortPrototype': Matcher(HConnectPPortPrototype_overlapLHS()),
#                                       'HConnectRPortPrototype': Matcher(HConnectRPortPrototype_overlapLHS()),
#                                       'HConnECU2VirtualDevice': Matcher(HConnECU2VirtualDevice_overlapLHS()),
#                                       'HConnVirtualDeviceToDistributable': Matcher(HConnVirtualDeviceToDistributable_overlapLHS())}


        # print("\n===\nrules:")
        # for rule in sorted(self.rules):
        #     print(str(rule))
        #
        # print("\n===\nbackwardPatterns:")
        # for backwardPattern in sorted(self.backwardPatterns):
        #     print(str(backwardPattern))
        #
        # print("\n===\nbackwardPatterns2Rules:")
        # for backwardPatterns2Rule in sorted(self.backwardPatterns2Rules):
        #     print(str(backwardPatterns2Rule))
        #
        # print("\n===\nbackwardPatternsComplete:")
        # for backwardPatternsComplete in sorted(self.backwardPatternsComplete):
        #     print(str(backwardPatternsComplete))
        #
        # print("\n===\nmatchRulePatterns:")
        # for matchRulePattern in sorted(self.matchRulePatterns):
        #     print(str(matchRulePattern))

        M2IfClause = AtomicStateProperty(HM2IfClauseIsolatedConnectedLHS(), HM2IfClauseIsolatedConnectedLHS(),
            HM2IfClauseCompleteLHS())
        M2ThenClause = NotStateProperty(
            AtomicStateProperty(HM2ThenClausePart2IsolatedConnectedLHS(), HM2ThenClausePart2IsolatedConnectedLHS(),
                HM2ThenClausePart2CompleteLHS()))
        M4IfClause = AtomicStateProperty(HM4IfClauseIsolatedConnectedLHS(), HM4IfClauseIsolatedConnectedLHS(),
            HM4IfClauseCompleteLHS())
        M4ThenClause = NotStateProperty(
            AtomicStateProperty(HM4ThenClausePart2IsolatedConnectedLHS(), HM4ThenClausePart2IsolatedConnectedLHS(),
                HM4ThenClausePart2CompleteLHS()))

        M5IfClause = AtomicStateProperty(HM5IfClauseIsolatedConnectedLHS(), HM5IfClauseIsolatedConnectedLHS(),
            HM5IfClauseCompleteLHS())
        M5ThenClause = NotStateProperty(
            AtomicStateProperty(HM5ThenClausePart2IsolatedConnectedLHS(), HM5ThenClausePart2IsolatedConnectedLHS(),
                HM5ThenClausePart2CompleteLHS()))
        M6IfClause = AtomicStateProperty(HM6IfClauseIsolatedConnectedLHS(), HM6IfClauseIsolatedConnectedLHS(),
            HM6IfClauseCompleteLHS())
        M6ThenClause = NotStateProperty(
            AtomicStateProperty(HM6ThenClausePart2IsolatedConnectedLHS(), HM6ThenClausePart2IsolatedConnectedLHS(),
                HM6ThenClausePart2CompleteLHS()))


# M2IfClause=AtomicStateProperty(HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseIsolatedConnectedLHS(),HM2IfClauseCompleteLHS())
        # M2ThenClause=AndStateProperty(AtomicStateProperty(HM2ThenClausePart1IsolatedConnectedLHS(),HM2ThenClausePart1IsolatedConnectedLHS(), HM2ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2IsolatedConnectedLHS(),HM2ThenClausePart2CompleteLHS())))
        # M4IfClause=AtomicStateProperty(HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseIsolatedConnectedLHS(),HM4IfClauseCompleteLHS())
        # M4ThenClause=AndStateProperty(AtomicStateProperty(HM4ThenClausePart1IsolatedConnectedLHS(),HM4ThenClausePart1IsolatedConnectedLHS(), HM4ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2IsolatedConnectedLHS(),HM4ThenClausePart2CompleteLHS())))
        # M5IfClause=AtomicStateProperty(HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseIsolatedConnectedLHS(),HM5IfClauseCompleteLHS())
        # M5ThenClause=AndStateProperty(AtomicStateProperty(HM5ThenClausePart1IsolatedConnectedLHS(),HM5ThenClausePart1IsolatedConnectedLHS(), HM5ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2IsolatedConnectedLHS(),HM5ThenClausePart2CompleteLHS())))
        # M6IfClause=AtomicStateProperty(HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseIsolatedConnectedLHS(),HM6IfClauseCompleteLHS())
        # M6ThenClause=AndStateProperty(AtomicStateProperty(HM6ThenClausePart1IsolatedConnectedLHS(),HM6ThenClausePart1IsolatedConnectedLHS(), HM6ThenClausePart1CompleteLHS()),NotStateProperty(AtomicStateProperty(HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2IsolatedConnectedLHS(),HM6ThenClausePart2CompleteLHS())))

        self.atomic_properties = [["P1", P1atomic], ["P2", P2atomic]]

        self.if_then_properties = []
        #["S1", S1IfClause, S1ThenClause], ["M1", M1IfClause, M1ThenClause],
                      #["M3", M3IfClause, M3ThenClause], ["M2", M2IfClause, M2ThenClause], ["M4", M4IfClause, M4ThenClause],
                      #["M5", M5IfClause, M5ThenClause], ["M6", M6IfClause, M6ThenClause]]


        if args.slice > 0:
            contract = self.atomic_properties[args.slice - 1]
            self.rules, self.transformation = slice_transformation(self.rules, self.transformation, contract, args)


    def test_correct_GM_transformation(self,args):
#         pass
#         
#         transformation = [[HMapDistributable(), HMapECU2FiveElementsFAULTY(), HMapVirtualDeviceFAULTY()],
#                           [HConnECU2VirtualDevice(), HConnVirtualDeviceToDistributable()],
#                           [HConnectPPortPrototype(), HConnectRPortPrototype()]]
# 
#         transformation = [[self.rules['HMapDistributable'], self.rules['HMapECU2FiveElements'], self.rules['HMapVirtualDevice']],
#                           [self.rules['HConnECU2VirtualDevice'], self.rules['HConnVirtualDeviceToDistributable']],
#                           [self.rules['HConnectPPortPrototype'], self.rules['HConnectRPortPrototype']]]
# 
# 
#         self.rulesIncludingBackLinks = [[],\
#                                    [transformation[1][0], transformation[1][1]],\
#                                    [transformation[2][0], transformation[2][1]]]

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        #self.rulesIncludingBackLinks = pyramify.getRulesIncludingBackLinks(transformation, self.backwardPatterns)



        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators, self.overlappingRules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("GM2AUTOSAR_MM/transformation_w_equations/", self.transformation)


        s = PathConditionGenerator(self.transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlappingRules, self.subsumption, self.loopingRuleSubsumption, args)#



        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()

        print(s.num_path_conditions)

        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
        # print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))
        
        s.print_path_conditions_screen()

        s.check_rule_reachability()
#
#        s.print_path_conditions_file()


#         expected_num_pcs = 3
#         # check if the correct number of path conditions were produced
#         if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:
#             #TODO: Make this an exception
#             num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(
#                 expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
#             print(num_pcs_s)
# 
#         print("printing states")
        #self._print_states(s)

#         graph_to_dot('symbolic_exec', s.symbStateSpace[1][0], 1)


        ####REAL EXPERIMENTATION: Proving the 4 types of constraints in our MODELS paper
        # The naming convention used for the properties (i.e., P1, P2..ETC) are the
        # same convention used in my MODELS paper in Table 2.

        #turn off verification debugging


        #s.print_path_conditions_file()

#         #s.verbosity = 2
#
        ts0 = time.time()

        print("\nProperty Proving:")


        verifier = StateProperty()
        for name, atomic_prop in self.atomic_properties:
            finalresult = verifier.verifyCompositeStateProperty(s, atomic_prop)
            if len(finalresult) == 0:
                print("Atomic property: " + name + " does hold\n")
            else:
                print("Atomic property: " + name + " does not hold\n")


        for name, i, t in self.if_then_properties:
            finalresult = verifier.verifyCompositeStateProperty(s, ImplicationStateProperty(i, t))
            if len(finalresult) == 0:
                print("If-then property: " + name + " does hold\n")
            else:
                print("If-then property: " + name + " does not hold\n")


        ts1 = time.time()

        prop_length = len(self.atomic_properties) + len(self.if_then_properties)
        print("\n\nTime to verify " + str(prop_length) + " properties: " + str(ts1 - ts0))



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

    parser = argparse.ArgumentParser(description = 'Run the uml to kiltera test.')
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


    ps2 = Test()
    ps2.setUp(args)
    ps2.test_correct_GM_transformation(args)
    
