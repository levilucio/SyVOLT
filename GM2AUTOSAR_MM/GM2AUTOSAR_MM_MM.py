"""
__GM2AUTOSAR_MM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sat Aug 24 20:15:56 2013
___________________________________________________________________________
"""
from ASG_GM2AUTOSAR_MM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MatchModel       import *
from ApplyModel       import *
from MetaModelElement_S       import *
from MetaModelElement_T       import *
from ECU       import *
from VirtualDevice       import *
from Distributable       import *
from ExecFrame       import *
from Signal       import *
from System       import *
from SystemMapping       import *
from SoftwareComposition       import *
from CompositionType       import *
from ComponentPrototype       import *
from PPortPrototype       import *
from RPortPrototype       import *
from EcuInstance       import *
from SwcToEcuMapping       import *
from SwCompToEcuMapping_component       import *
from PortPrototype       import *
from ComponentType       import *
from paired_with       import *
from match_contains       import *
from directLink_S       import *
from directLink_T       import *
from apply_contains       import *
from indirectLink_S       import *
from backward_link       import *
from trace_link       import *
def createNewASGroot(self):
   return ASG_GM2AUTOSAR_MM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MatchModel", command=lambda x=self: x.createNewMatchModel(x, 100, 100) )
    modelMenu.add_command(label="New ApplyModel", command=lambda x=self: x.createNewApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MetaModelElement_S", command=lambda x=self: x.createNewMetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New MetaModelElement_T", command=lambda x=self: x.createNewMetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New ECU", command=lambda x=self: x.createNewECU(x, 100, 100) )
    modelMenu.add_command(label="New VirtualDevice", command=lambda x=self: x.createNewVirtualDevice(x, 100, 100) )
    modelMenu.add_command(label="New Distributable", command=lambda x=self: x.createNewDistributable(x, 100, 100) )
    modelMenu.add_command(label="New ExecFrame", command=lambda x=self: x.createNewExecFrame(x, 100, 100) )
    modelMenu.add_command(label="New Signal", command=lambda x=self: x.createNewSignal(x, 100, 100) )
    modelMenu.add_command(label="New System", command=lambda x=self: x.createNewSystem(x, 100, 100) )
    modelMenu.add_command(label="New SystemMapping", command=lambda x=self: x.createNewSystemMapping(x, 100, 100) )
    modelMenu.add_command(label="New SoftwareComposition", command=lambda x=self: x.createNewSoftwareComposition(x, 100, 100) )
    modelMenu.add_command(label="New CompositionType", command=lambda x=self: x.createNewCompositionType(x, 100, 100) )
    modelMenu.add_command(label="New ComponentPrototype", command=lambda x=self: x.createNewComponentPrototype(x, 100, 100) )
    modelMenu.add_command(label="New PPortPrototype", command=lambda x=self: x.createNewPPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New RPortPrototype", command=lambda x=self: x.createNewRPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New EcuInstance", command=lambda x=self: x.createNewEcuInstance(x, 100, 100) )
    modelMenu.add_command(label="New SwcToEcuMapping", command=lambda x=self: x.createNewSwcToEcuMapping(x, 100, 100) )
    modelMenu.add_command(label="New SwCompToEcuMapping_component", command=lambda x=self: x.createNewSwCompToEcuMapping_component(x, 100, 100) )
    modelMenu.add_command(label="New PortPrototype", command=lambda x=self: x.createNewPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New ComponentType", command=lambda x=self: x.createNewComponentType(x, 100, 100) )
    modelMenu.add_command(label="New paired_with", command=lambda x=self: x.createNewpaired_with(x, 100, 100) )
    modelMenu.add_command(label="New match_contains", command=lambda x=self: x.createNewmatch_contains(x, 100, 100) )
    modelMenu.add_command(label="New directLink_S", command=lambda x=self: x.createNewdirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New directLink_T", command=lambda x=self: x.createNewdirectLink_T(x, 100, 100) )
    modelMenu.add_command(label="New apply_contains", command=lambda x=self: x.createNewapply_contains(x, 100, 100) )
    modelMenu.add_command(label="New indirectLink_S", command=lambda x=self: x.createNewindirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New backward_link", command=lambda x=self: x.createNewbackward_link(x, 100, 100) )
    modelMenu.add_command(label="New trace_link", command=lambda x=self: x.createNewtrace_link(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['directLink_S']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['apply_contains']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'System', self.createNewSystem), ( 'SystemMapping', self.createNewSystemMapping), ( 'SoftwareComposition', self.createNewSoftwareComposition), ( 'CompositionType', self.createNewCompositionType), ( 'ComponentPrototype', self.createNewComponentPrototype), ( 'PPortPrototype', self.createNewPPortPrototype), ( 'RPortPrototype', self.createNewRPortPrototype), ( 'EcuInstance', self.createNewEcuInstance), ( 'SwcToEcuMapping', self.createNewSwcToEcuMapping), ( 'SwCompToEcuMapping_component', self.createNewSwCompToEcuMapping_component), ( 'PortPrototype', self.createNewPortPrototype), ( 'ComponentType', self.createNewComponentType)]
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'System', self.createNewSystem), ( 'SystemMapping', self.createNewSystemMapping), ( 'SoftwareComposition', self.createNewSoftwareComposition), ( 'CompositionType', self.createNewCompositionType), ( 'ComponentPrototype', self.createNewComponentPrototype), ( 'PPortPrototype', self.createNewPPortPrototype), ( 'RPortPrototype', self.createNewRPortPrototype), ( 'EcuInstance', self.createNewEcuInstance), ( 'SwcToEcuMapping', self.createNewSwcToEcuMapping), ( 'SwCompToEcuMapping_component', self.createNewSwCompToEcuMapping_component), ( 'PortPrototype', self.createNewPortPrototype), ( 'ComponentType', self.createNewComponentType)]
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'System', self.createNewSystem), ( 'SystemMapping', self.createNewSystemMapping), ( 'SoftwareComposition', self.createNewSoftwareComposition), ( 'CompositionType', self.createNewCompositionType), ( 'ComponentPrototype', self.createNewComponentPrototype), ( 'PPortPrototype', self.createNewPPortPrototype), ( 'RPortPrototype', self.createNewRPortPrototype), ( 'EcuInstance', self.createNewEcuInstance), ( 'SwcToEcuMapping', self.createNewSwcToEcuMapping), ( 'SwCompToEcuMapping_component', self.createNewSwCompToEcuMapping_component), ( 'PortPrototype', self.createNewPortPrototype), ( 'ComponentType', self.createNewComponentType)]
          ,'RPortPrototype': [] }
    self.ConnectivityMap['SystemMapping']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['Distributable']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'MetaModelElement_S': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ExecFrame': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'PortPrototype': []
          ,'Signal': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['System']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['ComponentType']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['paired_with']={
           'directLink_S': []
          ,'apply_contains': [( 'ApplyModel', self.createNewApplyModel)]
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['PPortPrototype']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['backward_link']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['ComponentPrototype']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['directLink_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'System', self.createNewSystem), ( 'SystemMapping', self.createNewSystemMapping), ( 'SoftwareComposition', self.createNewSoftwareComposition), ( 'CompositionType', self.createNewCompositionType), ( 'ComponentPrototype', self.createNewComponentPrototype), ( 'PPortPrototype', self.createNewPPortPrototype), ( 'RPortPrototype', self.createNewRPortPrototype), ( 'EcuInstance', self.createNewEcuInstance), ( 'SwcToEcuMapping', self.createNewSwcToEcuMapping), ( 'SwCompToEcuMapping_component', self.createNewSwCompToEcuMapping_component), ( 'PortPrototype', self.createNewPortPrototype), ( 'ComponentType', self.createNewComponentType)]
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'System', self.createNewSystem), ( 'SystemMapping', self.createNewSystemMapping), ( 'SoftwareComposition', self.createNewSoftwareComposition), ( 'CompositionType', self.createNewCompositionType), ( 'ComponentPrototype', self.createNewComponentPrototype), ( 'PPortPrototype', self.createNewPPortPrototype), ( 'RPortPrototype', self.createNewRPortPrototype), ( 'EcuInstance', self.createNewEcuInstance), ( 'SwcToEcuMapping', self.createNewSwcToEcuMapping), ( 'SwCompToEcuMapping_component', self.createNewSwCompToEcuMapping_component), ( 'PortPrototype', self.createNewPortPrototype), ( 'ComponentType', self.createNewComponentType)]
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'System', self.createNewSystem), ( 'SystemMapping', self.createNewSystemMapping), ( 'SoftwareComposition', self.createNewSoftwareComposition), ( 'CompositionType', self.createNewCompositionType), ( 'ComponentPrototype', self.createNewComponentPrototype), ( 'PPortPrototype', self.createNewPPortPrototype), ( 'RPortPrototype', self.createNewRPortPrototype), ( 'EcuInstance', self.createNewEcuInstance), ( 'SwcToEcuMapping', self.createNewSwcToEcuMapping), ( 'SwCompToEcuMapping_component', self.createNewSwCompToEcuMapping_component), ( 'PortPrototype', self.createNewPortPrototype), ( 'ComponentType', self.createNewComponentType)]
          ,'RPortPrototype': [] }
    self.ConnectivityMap['ApplyModel']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': [( 'apply_contains', self.createNewapply_contains)]
          ,'ComponentType': [( 'apply_contains', self.createNewapply_contains)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'apply_contains', self.createNewapply_contains)]
          ,'backward_link': []
          ,'SystemMapping': [( 'apply_contains', self.createNewapply_contains)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'apply_contains', self.createNewapply_contains)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'apply_contains', self.createNewapply_contains)]
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': [( 'apply_contains', self.createNewapply_contains)]
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': [( 'apply_contains', self.createNewapply_contains)]
          ,'Signal': []
          ,'ComponentPrototype': [( 'apply_contains', self.createNewapply_contains)]
          ,'SoftwareComposition': [( 'apply_contains', self.createNewapply_contains)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'apply_contains', self.createNewapply_contains)]
          ,'EcuInstance': [( 'apply_contains', self.createNewapply_contains)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'apply_contains', self.createNewapply_contains)] }
    self.ConnectivityMap['CompositionType']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['indirectLink_S']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['MetaModelElement_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['ECU']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'MetaModelElement_S': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ExecFrame': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'PortPrototype': []
          ,'Signal': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['MetaModelElement_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'MetaModelElement_S': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ExecFrame': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'PortPrototype': []
          ,'Signal': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['SwcToEcuMapping']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['VirtualDevice']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'MetaModelElement_S': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ExecFrame': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'PortPrototype': []
          ,'Signal': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['ExecFrame']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'MetaModelElement_S': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ExecFrame': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'PortPrototype': []
          ,'Signal': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['PortPrototype']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['Signal']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'MetaModelElement_S': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ExecFrame': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'PortPrototype': []
          ,'Signal': [( 'directLink_S', self.createNewdirectLink_S), ( 'indirectLink_S', self.createNewindirectLink_S)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['match_contains']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['SoftwareComposition']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['MatchModel']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'match_contains', self.createNewmatch_contains)]
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': [( 'paired_with', self.createNewpaired_with)]
          ,'CompositionType': []
          ,'indirectLink_S': []
          ,'MetaModelElement_T': []
          ,'ECU': [( 'match_contains', self.createNewmatch_contains)]
          ,'MetaModelElement_S': [( 'match_contains', self.createNewmatch_contains)]
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': [( 'match_contains', self.createNewmatch_contains)]
          ,'ExecFrame': [( 'match_contains', self.createNewmatch_contains)]
          ,'PortPrototype': []
          ,'Signal': [( 'match_contains', self.createNewmatch_contains)]
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['SwCompToEcuMapping_component']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['EcuInstance']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['trace_link']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': []
          ,'System': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'PPortPrototype': []
          ,'backward_link': []
          ,'SystemMapping': []
          ,'ApplyModel': []
          ,'CompositionType': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'ECU', self.createNewECU), ( 'VirtualDevice', self.createNewVirtualDevice), ( 'Distributable', self.createNewDistributable), ( 'ExecFrame', self.createNewExecFrame), ( 'Signal', self.createNewSignal)]
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'MetaModelElement_S': []
          ,'SwcToEcuMapping': []
          ,'VirtualDevice': []
          ,'ExecFrame': []
          ,'PortPrototype': []
          ,'Signal': []
          ,'ComponentPrototype': []
          ,'SoftwareComposition': []
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': []
          ,'EcuInstance': []
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [] }
    self.ConnectivityMap['RPortPrototype']={
           'directLink_S': []
          ,'apply_contains': []
          ,'directLink_T': []
          ,'Distributable': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'System': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ComponentType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'paired_with': []
          ,'PPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'SystemMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'CompositionType': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'indirectLink_S': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ECU': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'SwcToEcuMapping': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'VirtualDevice': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ExecFrame': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'PortPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Signal': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ComponentPrototype': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'SoftwareComposition': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'SwCompToEcuMapping_component': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'EcuInstance': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'RPortPrototype': [( 'directLink_T', self.createNewdirectLink_T)] }
    
    self.CardinalityTable['MatchModel']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': [('1', '1', 'Source')]
          ,'match_contains': [('0', 'N', 'Source')]
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['ApplyModel']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': [('1', '1', 'Destination')]
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['MetaModelElement_S']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MetaModelElement_T']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['ECU']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['VirtualDevice']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Distributable']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['ExecFrame']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Signal']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['System']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['SystemMapping']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['SoftwareComposition']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['CompositionType']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['ComponentPrototype']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['PPortPrototype']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['RPortPrototype']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['EcuInstance']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['SwcToEcuMapping']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['SwCompToEcuMapping_component']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['PortPrototype']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['ComponentType']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'indirectLink_S': []
          ,'backward_link': [('0', 'N', 'Source')]
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['paired_with']={
          'MatchModel': [('1', '1', 'Destination')]
          ,'ApplyModel': [('1', '1', 'Source')]
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': []
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['match_contains']={
          'MatchModel': [('0', 'N', 'Destination')]
          ,'ApplyModel': []
          ,'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MetaModelElement_T': []
          ,'ECU': [('0', 'N', 'Source')]
          ,'VirtualDevice': [('0', 'N', 'Source')]
          ,'Distributable': [('0', 'N', 'Source')]
          ,'ExecFrame': [('0', 'N', 'Source')]
          ,'Signal': [('0', 'N', 'Source')]
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['directLink_S']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MetaModelElement_T': []
          ,'ECU': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Signal': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['directLink_T']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'SystemMapping': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'SoftwareComposition': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'CompositionType': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'ComponentPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'PPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'RPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'EcuInstance': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'SwcToEcuMapping': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'SwCompToEcuMapping_component': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'PortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'ComponentType': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['apply_contains']={
          'MatchModel': []
          ,'ApplyModel': [('0', 'N', 'Destination')]
          ,'MetaModelElement_S': []
          ,'MetaModelElement_T': [('0', 'N', 'Source')]
          ,'ECU': []
          ,'VirtualDevice': []
          ,'Distributable': []
          ,'ExecFrame': []
          ,'Signal': []
          ,'System': [('0', 'N', 'Source')]
          ,'SystemMapping': [('0', 'N', 'Source')]
          ,'SoftwareComposition': [('0', 'N', 'Source')]
          ,'CompositionType': [('0', 'N', 'Source')]
          ,'ComponentPrototype': [('0', 'N', 'Source')]
          ,'PPortPrototype': [('0', 'N', 'Source')]
          ,'RPortPrototype': [('0', 'N', 'Source')]
          ,'EcuInstance': [('0', 'N', 'Source')]
          ,'SwcToEcuMapping': [('0', 'N', 'Source')]
          ,'SwCompToEcuMapping_component': [('0', 'N', 'Source')]
          ,'PortPrototype': [('0', 'N', 'Source')]
          ,'ComponentType': [('0', 'N', 'Source')]
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['indirectLink_S']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MetaModelElement_T': []
          ,'ECU': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Signal': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'System': []
          ,'SystemMapping': []
          ,'SoftwareComposition': []
          ,'CompositionType': []
          ,'ComponentPrototype': []
          ,'PPortPrototype': []
          ,'RPortPrototype': []
          ,'EcuInstance': []
          ,'SwcToEcuMapping': []
          ,'SwCompToEcuMapping_component': []
          ,'PortPrototype': []
          ,'ComponentType': []
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['backward_link']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'ECU': [('0', 'N', 'Source')]
          ,'VirtualDevice': [('0', 'N', 'Source')]
          ,'Distributable': [('0', 'N', 'Source')]
          ,'ExecFrame': [('0', 'N', 'Source')]
          ,'Signal': [('0', 'N', 'Source')]
          ,'System': [('0', 'N', 'Destination')]
          ,'SystemMapping': [('0', 'N', 'Destination')]
          ,'SoftwareComposition': [('0', 'N', 'Destination')]
          ,'CompositionType': [('0', 'N', 'Destination')]
          ,'ComponentPrototype': [('0', 'N', 'Destination')]
          ,'PPortPrototype': [('0', 'N', 'Destination')]
          ,'RPortPrototype': [('0', 'N', 'Destination')]
          ,'EcuInstance': [('0', 'N', 'Destination')]
          ,'SwcToEcuMapping': [('0', 'N', 'Destination')]
          ,'SwCompToEcuMapping_component': [('0', 'N', 'Destination')]
          ,'PortPrototype': [('0', 'N', 'Destination')]
          ,'ComponentType': [('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    self.CardinalityTable['trace_link']={
          'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'ECU': [('0', 'N', 'Source')]
          ,'VirtualDevice': [('0', 'N', 'Source')]
          ,'Distributable': [('0', 'N', 'Source')]
          ,'ExecFrame': [('0', 'N', 'Source')]
          ,'Signal': [('0', 'N', 'Source')]
          ,'System': [('0', 'N', 'Destination')]
          ,'SystemMapping': [('0', 'N', 'Destination')]
          ,'SoftwareComposition': [('0', 'N', 'Destination')]
          ,'CompositionType': [('0', 'N', 'Destination')]
          ,'ComponentPrototype': [('0', 'N', 'Destination')]
          ,'PPortPrototype': [('0', 'N', 'Destination')]
          ,'RPortPrototype': [('0', 'N', 'Destination')]
          ,'EcuInstance': [('0', 'N', 'Destination')]
          ,'SwcToEcuMapping': [('0', 'N', 'Destination')]
          ,'SwCompToEcuMapping_component': [('0', 'N', 'Destination')]
          ,'PortPrototype': [('0', 'N', 'Destination')]
          ,'ComponentType': [('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'match_contains': []
          ,'directLink_S': []
          ,'directLink_T': []
          ,'apply_contains': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'trace_link': [] }
    
    self.entitiesInMetaModel['GM2AUTOSAR_MM']=["MatchModel", "ApplyModel", "MetaModelElement_S", "MetaModelElement_T", "ECU", "VirtualDevice", "Distributable", "ExecFrame", "Signal", "System", "SystemMapping", "SoftwareComposition", "CompositionType", "ComponentPrototype", "PPortPrototype", "RPortPrototype", "EcuInstance", "SwcToEcuMapping", "SwCompToEcuMapping_component", "PortPrototype", "ComponentType", "paired_with", "match_contains", "directLink_S", "directLink_T", "apply_contains", "indirectLink_S", "backward_link", "trace_link"]

    
def createNewMatchModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MatchModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MatchModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MatchModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MatchModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewApplyModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = ApplyModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["ApplyModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ApplyModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ApplyModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMetaModelElement_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MetaModelElement_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MetaModelElement_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MetaModelElement_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MetaModelElement_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MetaModelElement_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMetaModelElement_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MetaModelElement_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MetaModelElement_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MetaModelElement_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MetaModelElement_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MetaModelElement_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewECU(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = ECU(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["ECU"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ECU(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ECU(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewVirtualDevice(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = VirtualDevice(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["VirtualDevice"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_VirtualDevice(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_VirtualDevice(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewDistributable(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Distributable(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Distributable"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Distributable(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Distributable(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Distributable", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewExecFrame(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = ExecFrame(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["ExecFrame"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ExecFrame(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ExecFrame(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ExecFrame", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSignal(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Signal(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Signal"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Signal(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Signal(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSystem(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = System(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["System"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_System(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_System(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("System", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSystemMapping(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = SystemMapping(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["SystemMapping"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_SystemMapping(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_SystemMapping(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("SystemMapping", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSoftwareComposition(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = SoftwareComposition(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["SoftwareComposition"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_SoftwareComposition(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_SoftwareComposition(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("SoftwareComposition", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewCompositionType(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = CompositionType(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["CompositionType"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_CompositionType(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_CompositionType(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("CompositionType", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewComponentPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = ComponentPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["ComponentPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ComponentPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ComponentPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ComponentPrototype", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewPPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = PPortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["PPortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_PPortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_PPortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("PPortPrototype", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewRPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = RPortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["RPortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_RPortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_RPortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("RPortPrototype", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewEcuInstance(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = EcuInstance(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["EcuInstance"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_EcuInstance(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_EcuInstance(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("EcuInstance", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSwcToEcuMapping(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = SwcToEcuMapping(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["SwcToEcuMapping"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_SwcToEcuMapping(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_SwcToEcuMapping(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("SwcToEcuMapping", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSwCompToEcuMapping_component(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = SwCompToEcuMapping_component(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["SwCompToEcuMapping_component"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_SwCompToEcuMapping_component(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_SwCompToEcuMapping_component(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("SwCompToEcuMapping_component", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = PortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["PortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_PortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_PortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("PortPrototype", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewComponentType(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = ComponentType(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["ComponentType"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ComponentType(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ComponentType(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ComponentType", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewpaired_with(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = paired_with(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["paired_with"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_paired_with(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_paired_with(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewmatch_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = match_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["match_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_match_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_match_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewdirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = directLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["directLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_directLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_directLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewdirectLink_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = directLink_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["directLink_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_directLink_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_directLink_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewapply_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = apply_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["apply_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_apply_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_apply_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewindirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = indirectLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["indirectLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_indirectLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_indirectLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("indirectLink_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewbackward_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = backward_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["backward_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_backward_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_backward_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewtrace_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = trace_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["trace_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_trace_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_trace_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("trace_link", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_GM2AUTOSAR_MM(self)
   ne = len(self.ASGroot.listNodes["ASG_GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_GM2AUTOSAR_MM", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("String", "ATOM3String", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Boolean", "ATOM3Boolean", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Float", "ATOM3Float", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Action", "ATOM3Action", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Link", "ATOM3Link", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Port", "ATOM3Port", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Connection", "ATOM3Connection", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("MSEnum", "ATOM3MSEnum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Text", "ATOM3Text", params, (None, 0) ))
    objs.append(obj)
    self.typeList.setValue(objs)

