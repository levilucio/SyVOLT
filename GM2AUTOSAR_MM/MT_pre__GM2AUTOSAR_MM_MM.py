"""
__MT_pre__GM2AUTOSAR_MM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sat Aug 24 20:17:20 2013
___________________________________________________________________________________
"""
from ASG_MT_pre__GM2AUTOSAR_MM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MT_pre__MatchModel       import *
from MT_pre__ApplyModel       import *
from MT_pre__MetaModelElement_S       import *
from MT_pre__MetaModelElement_T       import *
from MT_pre__ECU       import *
from MT_pre__VirtualDevice       import *
from MT_pre__Distributable       import *
from MT_pre__ExecFrame       import *
from MT_pre__Signal       import *
from MT_pre__System       import *
from MT_pre__SystemMapping       import *
from MT_pre__SoftwareComposition       import *
from MT_pre__CompositionType       import *
from MT_pre__ComponentPrototype       import *
from MT_pre__PPortPrototype       import *
from MT_pre__RPortPrototype       import *
from MT_pre__EcuInstance       import *
from MT_pre__SwcToEcuMapping       import *
from MT_pre__SwCompToEcuMapping_component       import *
from MT_pre__PortPrototype       import *
from MT_pre__ComponentType       import *
from MT_pre__GenericNode_GM2AUTOSAR_MM       import *
from MT_pre__paired_with       import *
from MT_pre__match_contains       import *
from MT_pre__directLink_S       import *
from MT_pre__directLink_T       import *
from MT_pre__apply_contains       import *
from MT_pre__indirectLink_S       import *
from MT_pre__backward_link       import *
from MT_pre__trace_link       import *
from MT_pre__GenericEdge_GM2AUTOSAR_MM       import *
def createNewASGroot(self):
   return ASG_MT_pre__GM2AUTOSAR_MM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MT_pre__MatchModel", command=lambda x=self: x.createNewMT_pre__MatchModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__ApplyModel", command=lambda x=self: x.createNewMT_pre__ApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__MetaModelElement_S", command=lambda x=self: x.createNewMT_pre__MetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__MetaModelElement_T", command=lambda x=self: x.createNewMT_pre__MetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__ECU", command=lambda x=self: x.createNewMT_pre__ECU(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__VirtualDevice", command=lambda x=self: x.createNewMT_pre__VirtualDevice(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Distributable", command=lambda x=self: x.createNewMT_pre__Distributable(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__ExecFrame", command=lambda x=self: x.createNewMT_pre__ExecFrame(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Signal", command=lambda x=self: x.createNewMT_pre__Signal(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__System", command=lambda x=self: x.createNewMT_pre__System(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__SystemMapping", command=lambda x=self: x.createNewMT_pre__SystemMapping(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__SoftwareComposition", command=lambda x=self: x.createNewMT_pre__SoftwareComposition(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__CompositionType", command=lambda x=self: x.createNewMT_pre__CompositionType(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__ComponentPrototype", command=lambda x=self: x.createNewMT_pre__ComponentPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__PPortPrototype", command=lambda x=self: x.createNewMT_pre__PPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__RPortPrototype", command=lambda x=self: x.createNewMT_pre__RPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__EcuInstance", command=lambda x=self: x.createNewMT_pre__EcuInstance(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__SwcToEcuMapping", command=lambda x=self: x.createNewMT_pre__SwcToEcuMapping(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__SwCompToEcuMapping_component", command=lambda x=self: x.createNewMT_pre__SwCompToEcuMapping_component(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__PortPrototype", command=lambda x=self: x.createNewMT_pre__PortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__ComponentType", command=lambda x=self: x.createNewMT_pre__ComponentType(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__GenericNode_GM2AUTOSAR_MM", command=lambda x=self: x.createNewMT_pre__GenericNode_GM2AUTOSAR_MM(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__paired_with", command=lambda x=self: x.createNewMT_pre__paired_with(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__match_contains", command=lambda x=self: x.createNewMT_pre__match_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__directLink_S", command=lambda x=self: x.createNewMT_pre__directLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__directLink_T", command=lambda x=self: x.createNewMT_pre__directLink_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__apply_contains", command=lambda x=self: x.createNewMT_pre__apply_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__indirectLink_S", command=lambda x=self: x.createNewMT_pre__indirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__backward_link", command=lambda x=self: x.createNewMT_pre__backward_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__trace_link", command=lambda x=self: x.createNewMT_pre__trace_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__GenericEdge_GM2AUTOSAR_MM", command=lambda x=self: x.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['MT_pre__VirtualDevice']={
           'MT_pre__VirtualDevice': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)] }
    self.ConnectivityMap['MT_pre__ApplyModel']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__CompositionType': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__backward_link']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__MatchModel']={
           'MT_pre__VirtualDevice': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__ApplyModel': [( 'MT_pre__paired_with', self.createNewMT_pre__paired_with)]
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)] }
    self.ConnectivityMap['MT_pre__Distributable']={
           'MT_pre__VirtualDevice': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)] }
    self.ConnectivityMap['MT_pre__SoftwareComposition']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__EcuInstance']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__match_contains']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__trace_link']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__System']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__SystemMapping']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__apply_contains']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__indirectLink_S']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__paired_with']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': [( 'MT_pre__ApplyModel', self.createNewMT_pre__ApplyModel)]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__directLink_S']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__ComponentPrototype']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__directLink_T']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__RPortPrototype']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__ECU']={
           'MT_pre__VirtualDevice': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)] }
    self.ConnectivityMap['MT_pre__PortPrototype']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__SwCompToEcuMapping_component']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__GenericEdge_GM2AUTOSAR_MM']={
           'MT_pre__VirtualDevice': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': [( 'MT_pre__MatchModel', self.createNewMT_pre__MatchModel)]
          ,'MT_pre__trace_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': [( 'MT_pre__ApplyModel', self.createNewMT_pre__ApplyModel)]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [( 'MT_pre__GenericNode_GM2AUTOSAR_MM', self.createNewMT_pre__GenericNode_GM2AUTOSAR_MM)]
          ,'MT_pre__paired_with': [( 'MT_pre__MatchModel', self.createNewMT_pre__MatchModel)]
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__System', self.createNewMT_pre__System), ( 'MT_pre__SystemMapping', self.createNewMT_pre__SystemMapping), ( 'MT_pre__SoftwareComposition', self.createNewMT_pre__SoftwareComposition), ( 'MT_pre__CompositionType', self.createNewMT_pre__CompositionType), ( 'MT_pre__ComponentPrototype', self.createNewMT_pre__ComponentPrototype), ( 'MT_pre__PPortPrototype', self.createNewMT_pre__PPortPrototype), ( 'MT_pre__RPortPrototype', self.createNewMT_pre__RPortPrototype), ( 'MT_pre__EcuInstance', self.createNewMT_pre__EcuInstance), ( 'MT_pre__SwcToEcuMapping', self.createNewMT_pre__SwcToEcuMapping), ( 'MT_pre__SwCompToEcuMapping_component', self.createNewMT_pre__SwCompToEcuMapping_component), ( 'MT_pre__PortPrototype', self.createNewMT_pre__PortPrototype), ( 'MT_pre__ComponentType', self.createNewMT_pre__ComponentType)]
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__ECU', self.createNewMT_pre__ECU), ( 'MT_pre__VirtualDevice', self.createNewMT_pre__VirtualDevice), ( 'MT_pre__Distributable', self.createNewMT_pre__Distributable), ( 'MT_pre__ExecFrame', self.createNewMT_pre__ExecFrame), ( 'MT_pre__Signal', self.createNewMT_pre__Signal)]
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__ComponentType']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__CompositionType']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__ExecFrame']={
           'MT_pre__VirtualDevice': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)] }
    self.ConnectivityMap['MT_pre__PPortPrototype']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__GenericNode_GM2AUTOSAR_MM']={
           'MT_pre__VirtualDevice': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__ApplyModel': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__Distributable': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__ECU': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__CompositionType': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__Signal': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_pre__GenericEdge_GM2AUTOSAR_MM)] }
    self.ConnectivityMap['MT_pre__SwcToEcuMapping']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__Signal']={
           'MT_pre__VirtualDevice': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)] }
    self.ConnectivityMap['MT_pre__MetaModelElement_T']={
           'MT_pre__VirtualDevice': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__SoftwareComposition': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__EcuInstance': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SystemMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ECU': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__SwCompToEcuMapping_component': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__CompositionType': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__ExecFrame': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__PPortPrototype': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Signal': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__MetaModelElement_S']={
           'MT_pre__VirtualDevice': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__Distributable': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__ECU': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ExecFrame': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__Signal': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S), ( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S)] }
    
    self.CardinalityTable['MT_pre__MatchModel']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': [('0', '1', 'Source')]
          ,'MT_pre__match_contains': [('0', 'N', 'Source')]
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__ApplyModel']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': [('0', '1', 'Destination')]
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Source')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__MetaModelElement_S']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__MetaModelElement_T']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__ECU']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__VirtualDevice']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Distributable']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__ExecFrame']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Signal']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__System']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__SystemMapping']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__SoftwareComposition']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__CompositionType']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__ComponentPrototype']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__PPortPrototype']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__RPortPrototype']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__EcuInstance']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__SwcToEcuMapping']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__SwCompToEcuMapping_component']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__PortPrototype']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__ComponentType']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__GenericNode_GM2AUTOSAR_MM']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Source'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__paired_with']={
          'MT_pre__MatchModel': [('0', '1', 'Destination')]
          ,'MT_pre__ApplyModel': [('0', '1', 'Source')]
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__match_contains']={
          'MT_pre__MatchModel': [('0', 'N', 'Destination')]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': [('0', 'N', 'Source')]
          ,'MT_pre__VirtualDevice': [('0', 'N', 'Source')]
          ,'MT_pre__Distributable': [('0', 'N', 'Source')]
          ,'MT_pre__ExecFrame': [('0', 'N', 'Source')]
          ,'MT_pre__Signal': [('0', 'N', 'Source')]
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__directLink_S']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Signal': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__directLink_T']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__SystemMapping': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__SoftwareComposition': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__CompositionType': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__ComponentPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__PPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__RPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__EcuInstance': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__SwcToEcuMapping': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__SwCompToEcuMapping_component': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__PortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__ComponentType': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__apply_contains']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': [('0', 'N', 'Destination')]
          ,'MT_pre__MetaModelElement_S': []
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_pre__ECU': []
          ,'MT_pre__VirtualDevice': []
          ,'MT_pre__Distributable': []
          ,'MT_pre__ExecFrame': []
          ,'MT_pre__Signal': []
          ,'MT_pre__System': [('0', 'N', 'Source')]
          ,'MT_pre__SystemMapping': [('0', 'N', 'Source')]
          ,'MT_pre__SoftwareComposition': [('0', 'N', 'Source')]
          ,'MT_pre__CompositionType': [('0', 'N', 'Source')]
          ,'MT_pre__ComponentPrototype': [('0', 'N', 'Source')]
          ,'MT_pre__PPortPrototype': [('0', 'N', 'Source')]
          ,'MT_pre__RPortPrototype': [('0', 'N', 'Source')]
          ,'MT_pre__EcuInstance': [('0', 'N', 'Source')]
          ,'MT_pre__SwcToEcuMapping': [('0', 'N', 'Source')]
          ,'MT_pre__SwCompToEcuMapping_component': [('0', 'N', 'Source')]
          ,'MT_pre__PortPrototype': [('0', 'N', 'Source')]
          ,'MT_pre__ComponentType': [('0', 'N', 'Source')]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__indirectLink_S']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__ECU': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Signal': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__System': []
          ,'MT_pre__SystemMapping': []
          ,'MT_pre__SoftwareComposition': []
          ,'MT_pre__CompositionType': []
          ,'MT_pre__ComponentPrototype': []
          ,'MT_pre__PPortPrototype': []
          ,'MT_pre__RPortPrototype': []
          ,'MT_pre__EcuInstance': []
          ,'MT_pre__SwcToEcuMapping': []
          ,'MT_pre__SwCompToEcuMapping_component': []
          ,'MT_pre__PortPrototype': []
          ,'MT_pre__ComponentType': []
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__backward_link']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_pre__ECU': [('0', 'N', 'Source')]
          ,'MT_pre__VirtualDevice': [('0', 'N', 'Source')]
          ,'MT_pre__Distributable': [('0', 'N', 'Source')]
          ,'MT_pre__ExecFrame': [('0', 'N', 'Source')]
          ,'MT_pre__Signal': [('0', 'N', 'Source')]
          ,'MT_pre__System': [('0', 'N', 'Destination')]
          ,'MT_pre__SystemMapping': [('0', 'N', 'Destination')]
          ,'MT_pre__SoftwareComposition': [('0', 'N', 'Destination')]
          ,'MT_pre__CompositionType': [('0', 'N', 'Destination')]
          ,'MT_pre__ComponentPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__PPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__RPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__EcuInstance': [('0', 'N', 'Destination')]
          ,'MT_pre__SwcToEcuMapping': [('0', 'N', 'Destination')]
          ,'MT_pre__SwCompToEcuMapping_component': [('0', 'N', 'Destination')]
          ,'MT_pre__PortPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__ComponentType': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__trace_link']={
          'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_pre__ECU': [('0', 'N', 'Source')]
          ,'MT_pre__VirtualDevice': [('0', 'N', 'Source')]
          ,'MT_pre__Distributable': [('0', 'N', 'Source')]
          ,'MT_pre__ExecFrame': [('0', 'N', 'Source')]
          ,'MT_pre__Signal': [('0', 'N', 'Source')]
          ,'MT_pre__System': [('0', 'N', 'Destination')]
          ,'MT_pre__SystemMapping': [('0', 'N', 'Destination')]
          ,'MT_pre__SoftwareComposition': [('0', 'N', 'Destination')]
          ,'MT_pre__CompositionType': [('0', 'N', 'Destination')]
          ,'MT_pre__ComponentPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__PPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__RPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__EcuInstance': [('0', 'N', 'Destination')]
          ,'MT_pre__SwcToEcuMapping': [('0', 'N', 'Destination')]
          ,'MT_pre__SwCompToEcuMapping_component': [('0', 'N', 'Destination')]
          ,'MT_pre__PortPrototype': [('0', 'N', 'Destination')]
          ,'MT_pre__ComponentType': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_pre__GenericEdge_GM2AUTOSAR_MM']={
          'MT_pre__MatchModel': [('0', 'N', 'Source')]
          ,'MT_pre__ApplyModel': [('0', 'N', 'Source')]
          ,'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_pre__ECU': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Signal': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__System': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__SystemMapping': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__SoftwareComposition': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__CompositionType': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__ComponentPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__PPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__RPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__EcuInstance': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__SwcToEcuMapping': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__SwCompToEcuMapping_component': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__PortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__ComponentType': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__GenericNode_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'MT_pre__paired_with': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__GenericEdge_GM2AUTOSAR_MM': [] }
    
    self.entitiesInMetaModel['MT_pre__GM2AUTOSAR_MM']=["MT_pre__MatchModel", "MT_pre__ApplyModel", "MT_pre__MetaModelElement_S", "MT_pre__MetaModelElement_T", "MT_pre__ECU", "MT_pre__VirtualDevice", "MT_pre__Distributable", "MT_pre__ExecFrame", "MT_pre__Signal", "MT_pre__System", "MT_pre__SystemMapping", "MT_pre__SoftwareComposition", "MT_pre__CompositionType", "MT_pre__ComponentPrototype", "MT_pre__PPortPrototype", "MT_pre__RPortPrototype", "MT_pre__EcuInstance", "MT_pre__SwcToEcuMapping", "MT_pre__SwCompToEcuMapping_component", "MT_pre__PortPrototype", "MT_pre__ComponentType", "MT_pre__GenericNode_GM2AUTOSAR_MM", "MT_pre__paired_with", "MT_pre__match_contains", "MT_pre__directLink_S", "MT_pre__directLink_T", "MT_pre__apply_contains", "MT_pre__indirectLink_S", "MT_pre__backward_link", "MT_pre__trace_link", "MT_pre__GenericEdge_GM2AUTOSAR_MM"]

    
def createNewMT_pre__MatchModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__MatchModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__MatchModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__MatchModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__MatchModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
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
def createNewMT_pre__ApplyModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__ApplyModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__ApplyModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__ApplyModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__ApplyModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
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
def createNewMT_pre__MetaModelElement_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__MetaModelElement_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__MetaModelElement_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__MetaModelElement_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__MetaModelElement_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
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
def createNewMT_pre__MetaModelElement_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__MetaModelElement_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__MetaModelElement_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__MetaModelElement_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__MetaModelElement_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
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
def createNewMT_pre__ECU(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__ECU(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__ECU"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__ECU(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__ECU(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
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
def createNewMT_pre__VirtualDevice(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__VirtualDevice(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__VirtualDevice"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__VirtualDevice(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__VirtualDevice(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
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
def createNewMT_pre__Distributable(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Distributable(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Distributable"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Distributable(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Distributable(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
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
def createNewMT_pre__ExecFrame(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__ExecFrame(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__ExecFrame"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__ExecFrame(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__ExecFrame(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__ExecFrame", new_obj.tag)
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
def createNewMT_pre__Signal(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Signal(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Signal"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Signal(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Signal(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
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
def createNewMT_pre__System(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__System(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__System"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__System(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__System(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
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
def createNewMT_pre__SystemMapping(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__SystemMapping(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__SystemMapping"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__SystemMapping(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__SystemMapping(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__SystemMapping", new_obj.tag)
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
def createNewMT_pre__SoftwareComposition(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__SoftwareComposition(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__SoftwareComposition"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__SoftwareComposition(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__SoftwareComposition(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
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
def createNewMT_pre__CompositionType(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__CompositionType(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__CompositionType"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__CompositionType(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__CompositionType(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
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
def createNewMT_pre__ComponentPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__ComponentPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__ComponentPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__ComponentPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__ComponentPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
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
def createNewMT_pre__PPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__PPortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__PPortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__PPortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__PPortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__PPortPrototype", new_obj.tag)
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
def createNewMT_pre__RPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__RPortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__RPortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__RPortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__RPortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__RPortPrototype", new_obj.tag)
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
def createNewMT_pre__EcuInstance(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__EcuInstance(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__EcuInstance"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__EcuInstance(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__EcuInstance(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__EcuInstance", new_obj.tag)
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
def createNewMT_pre__SwcToEcuMapping(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__SwcToEcuMapping(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__SwcToEcuMapping"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__SwcToEcuMapping(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__SwcToEcuMapping(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
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
def createNewMT_pre__SwCompToEcuMapping_component(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__SwCompToEcuMapping_component(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__SwCompToEcuMapping_component"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__SwCompToEcuMapping_component(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__SwCompToEcuMapping_component(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__SwCompToEcuMapping_component", new_obj.tag)
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
def createNewMT_pre__PortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__PortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__PortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__PortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__PortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__PortPrototype", new_obj.tag)
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
def createNewMT_pre__ComponentType(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__ComponentType(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__ComponentType"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__ComponentType(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__ComponentType(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__ComponentType", new_obj.tag)
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
def createNewMT_pre__GenericNode_GM2AUTOSAR_MM(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__GenericNode_GM2AUTOSAR_MM(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__GenericNode_GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__GenericNode_GM2AUTOSAR_MM(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__GenericNode_GM2AUTOSAR_MM(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__GenericNode_GM2AUTOSAR_MM", new_obj.tag)
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
def createNewMT_pre__paired_with(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__paired_with(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__paired_with"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__paired_with(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__paired_with(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__paired_with", new_obj.tag)
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
def createNewMT_pre__match_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__match_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__match_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__match_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__match_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
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
def createNewMT_pre__directLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__directLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__directLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__directLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__directLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
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
def createNewMT_pre__directLink_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__directLink_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__directLink_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__directLink_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__directLink_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
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
def createNewMT_pre__apply_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__apply_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__apply_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__apply_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__apply_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
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
def createNewMT_pre__indirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__indirectLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__indirectLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__indirectLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__indirectLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
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
def createNewMT_pre__backward_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__backward_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__backward_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__backward_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__backward_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
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
def createNewMT_pre__trace_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__trace_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__trace_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__trace_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__trace_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
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
def createNewMT_pre__GenericEdge_GM2AUTOSAR_MM(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__GenericEdge_GM2AUTOSAR_MM(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__GenericEdge_GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__GenericEdge_GM2AUTOSAR_MM(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__GenericEdge_GM2AUTOSAR_MM(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__GenericEdge_GM2AUTOSAR_MM", new_obj.tag)
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
   new_semantic_obj = ASG_MT_pre__GM2AUTOSAR_MM(self)
   ne = len(self.ASGroot.listNodes["ASG_MT_pre__GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_MT_pre__GM2AUTOSAR_MM", new_obj.tag)
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

