"""
__MT_post__GM2AUTOSAR_MM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sun Aug  9 23:46:05 2015
____________________________________________________________________________________
"""
from ASG_MT_post__GM2AUTOSAR_MM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MT_post__MatchModel       import *
from MT_post__ApplyModel       import *
from MT_post__MetaModelElement_S       import *
from MT_post__MetaModelElement_T       import *
from MT_post__ECU       import *
from MT_post__VirtualDevice       import *
from MT_post__Distributable       import *
from MT_post__ExecFrame       import *
from MT_post__Signal       import *
from MT_post__System       import *
from MT_post__SystemMapping       import *
from MT_post__SoftwareComposition       import *
from MT_post__CompositionType       import *
from MT_post__ComponentPrototype       import *
from MT_post__PPortPrototype       import *
from MT_post__RPortPrototype       import *
from MT_post__EcuInstance       import *
from MT_post__SwcToEcuMapping       import *
from MT_post__SwCompToEcuMapping_component       import *
from MT_post__PortPrototype       import *
from MT_post__ComponentType       import *
from MT_post__GenericNode_GM2AUTOSAR_MM       import *
from MT_post__paired_with       import *
from MT_post__match_contains       import *
from MT_post__directLink_S       import *
from MT_post__directLink_T       import *
from MT_post__apply_contains       import *
from MT_post__indirectLink_S       import *
from MT_post__backward_link       import *
from MT_post__trace_link       import *
from MT_post__GenericEdge_GM2AUTOSAR_MM       import *
def createNewASGroot(self):
   return ASG_MT_post__GM2AUTOSAR_MM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MT_post__MatchModel", command=lambda x=self: x.createNewMT_post__MatchModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__ApplyModel", command=lambda x=self: x.createNewMT_post__ApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__MetaModelElement_S", command=lambda x=self: x.createNewMT_post__MetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__MetaModelElement_T", command=lambda x=self: x.createNewMT_post__MetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__ECU", command=lambda x=self: x.createNewMT_post__ECU(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__VirtualDevice", command=lambda x=self: x.createNewMT_post__VirtualDevice(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Distributable", command=lambda x=self: x.createNewMT_post__Distributable(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__ExecFrame", command=lambda x=self: x.createNewMT_post__ExecFrame(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Signal", command=lambda x=self: x.createNewMT_post__Signal(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__System", command=lambda x=self: x.createNewMT_post__System(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__SystemMapping", command=lambda x=self: x.createNewMT_post__SystemMapping(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__SoftwareComposition", command=lambda x=self: x.createNewMT_post__SoftwareComposition(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__CompositionType", command=lambda x=self: x.createNewMT_post__CompositionType(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__ComponentPrototype", command=lambda x=self: x.createNewMT_post__ComponentPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__PPortPrototype", command=lambda x=self: x.createNewMT_post__PPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__RPortPrototype", command=lambda x=self: x.createNewMT_post__RPortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__EcuInstance", command=lambda x=self: x.createNewMT_post__EcuInstance(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__SwcToEcuMapping", command=lambda x=self: x.createNewMT_post__SwcToEcuMapping(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__SwCompToEcuMapping_component", command=lambda x=self: x.createNewMT_post__SwCompToEcuMapping_component(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__PortPrototype", command=lambda x=self: x.createNewMT_post__PortPrototype(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__ComponentType", command=lambda x=self: x.createNewMT_post__ComponentType(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__GenericNode_GM2AUTOSAR_MM", command=lambda x=self: x.createNewMT_post__GenericNode_GM2AUTOSAR_MM(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__paired_with", command=lambda x=self: x.createNewMT_post__paired_with(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__match_contains", command=lambda x=self: x.createNewMT_post__match_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__directLink_S", command=lambda x=self: x.createNewMT_post__directLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__directLink_T", command=lambda x=self: x.createNewMT_post__directLink_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__apply_contains", command=lambda x=self: x.createNewMT_post__apply_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__indirectLink_S", command=lambda x=self: x.createNewMT_post__indirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__backward_link", command=lambda x=self: x.createNewMT_post__backward_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__trace_link", command=lambda x=self: x.createNewMT_post__trace_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__GenericEdge_GM2AUTOSAR_MM", command=lambda x=self: x.createNewMT_post__GenericEdge_GM2AUTOSAR_MM(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['MT_post__match_contains']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__MetaModelElement_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ECU': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__MetaModelElement_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__SwcToEcuMapping']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__MatchModel']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': [( 'MT_post__paired_with', self.createNewMT_post__paired_with)]
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__ECU': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__indirectLink_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__paired_with']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': [( 'MT_post__ApplyModel', self.createNewMT_post__ApplyModel)]
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__GenericNode_GM2AUTOSAR_MM']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__SoftwareComposition': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__Distributable': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__MatchModel': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__ExecFrame': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__SystemMapping': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__CompositionType': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__Signal': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__ECU': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__EcuInstance': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__PortPrototype': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__PPortPrototype': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__ComponentType': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)]
          ,'MT_post__System': [( 'MT_post__GenericEdge_GM2AUTOSAR_MM', self.createNewMT_post__GenericEdge_GM2AUTOSAR_MM)] }
    self.ConnectivityMap['MT_post__RPortPrototype']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__Distributable']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ECU': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__directLink_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__directLink_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__SoftwareComposition']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__ApplyModel']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__CompositionType': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__PortPrototype': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__PPortPrototype': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__ComponentType': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__System': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)] }
    self.ConnectivityMap['MT_post__trace_link']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__ExecFrame']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ECU': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__SystemMapping']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__CompositionType']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__Signal']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ECU': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__ECU']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ECU': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__EcuInstance']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__apply_contains']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__VirtualDevice']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ECU': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__directLink_S', self.createNewMT_post__directLink_S), ( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S)]
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__ComponentPrototype']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__PortPrototype']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__GenericEdge_GM2AUTOSAR_MM']={
           'MT_post__match_contains': [( 'MT_post__MatchModel', self.createNewMT_post__MatchModel)]
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__paired_with': [( 'MT_post__MatchModel', self.createNewMT_post__MatchModel)]
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': [( 'MT_post__ApplyModel', self.createNewMT_post__ApplyModel)]
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [( 'MT_post__GenericNode_GM2AUTOSAR_MM', self.createNewMT_post__GenericNode_GM2AUTOSAR_MM)]
          ,'MT_post__backward_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__System', self.createNewMT_post__System), ( 'MT_post__SystemMapping', self.createNewMT_post__SystemMapping), ( 'MT_post__SoftwareComposition', self.createNewMT_post__SoftwareComposition), ( 'MT_post__CompositionType', self.createNewMT_post__CompositionType), ( 'MT_post__ComponentPrototype', self.createNewMT_post__ComponentPrototype), ( 'MT_post__PPortPrototype', self.createNewMT_post__PPortPrototype), ( 'MT_post__RPortPrototype', self.createNewMT_post__RPortPrototype), ( 'MT_post__EcuInstance', self.createNewMT_post__EcuInstance), ( 'MT_post__SwcToEcuMapping', self.createNewMT_post__SwcToEcuMapping), ( 'MT_post__SwCompToEcuMapping_component', self.createNewMT_post__SwCompToEcuMapping_component), ( 'MT_post__PortPrototype', self.createNewMT_post__PortPrototype), ( 'MT_post__ComponentType', self.createNewMT_post__ComponentType)]
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__backward_link']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__Distributable': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__ECU', self.createNewMT_post__ECU), ( 'MT_post__VirtualDevice', self.createNewMT_post__VirtualDevice), ( 'MT_post__Distributable', self.createNewMT_post__Distributable), ( 'MT_post__ExecFrame', self.createNewMT_post__ExecFrame), ( 'MT_post__Signal', self.createNewMT_post__Signal)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__CompositionType': []
          ,'MT_post__Signal': []
          ,'MT_post__ECU': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__System': [] }
    self.ConnectivityMap['MT_post__SwCompToEcuMapping_component']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__PPortPrototype']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__ComponentType']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    self.ConnectivityMap['MT_post__System']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwcToEcuMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__trace_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__paired_with': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__SoftwareComposition': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Distributable': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ExecFrame': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__SystemMapping': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__CompositionType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Signal': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ECU': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__EcuInstance': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__apply_contains': []
          ,'MT_post__VirtualDevice': [( 'MT_post__backward_link', self.createNewMT_post__backward_link), ( 'MT_post__trace_link', self.createNewMT_post__trace_link)]
          ,'MT_post__ComponentPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': []
          ,'MT_post__backward_link': []
          ,'MT_post__RPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__SwCompToEcuMapping_component': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__PPortPrototype': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__ComponentType': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__System': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)] }
    
    self.CardinalityTable['MT_post__MatchModel']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': [('0', '1', 'Source')]
          ,'MT_post__match_contains': [('0', 'N', 'Source')]
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__ApplyModel']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': [('0', '1', 'Destination')]
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': [('0', 'N', 'Source')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__MetaModelElement_S']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__trace_link': [('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__MetaModelElement_T']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__ECU']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__trace_link': [('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__VirtualDevice']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__trace_link': [('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Distributable']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__trace_link': [('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__ExecFrame']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__trace_link': [('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Signal']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__trace_link': [('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__System']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__SystemMapping']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__SoftwareComposition']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__CompositionType']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__ComponentPrototype']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__PPortPrototype']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__RPortPrototype']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__EcuInstance']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__SwcToEcuMapping']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__SwCompToEcuMapping_component']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__PortPrototype']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__ComponentType']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__trace_link': [('0', 'N', 'Source')]
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__GenericNode_GM2AUTOSAR_MM']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [('0', 'N', 'Source'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__paired_with']={
          'MT_post__MatchModel': [('0', '1', 'Destination')]
          ,'MT_post__ApplyModel': [('0', '1', 'Source')]
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__match_contains']={
          'MT_post__MatchModel': [('0', 'N', 'Destination')]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': [('0', 'N', 'Source')]
          ,'MT_post__VirtualDevice': [('0', 'N', 'Source')]
          ,'MT_post__Distributable': [('0', 'N', 'Source')]
          ,'MT_post__ExecFrame': [('0', 'N', 'Source')]
          ,'MT_post__Signal': [('0', 'N', 'Source')]
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__directLink_S']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Signal': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__directLink_T']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__SystemMapping': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__SoftwareComposition': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__CompositionType': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__ComponentPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__PPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__RPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__EcuInstance': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__SwcToEcuMapping': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__SwCompToEcuMapping_component': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__PortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__ComponentType': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__apply_contains']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': [('0', 'N', 'Destination')]
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_post__ECU': []
          ,'MT_post__VirtualDevice': []
          ,'MT_post__Distributable': []
          ,'MT_post__ExecFrame': []
          ,'MT_post__Signal': []
          ,'MT_post__System': [('0', 'N', 'Source')]
          ,'MT_post__SystemMapping': [('0', 'N', 'Source')]
          ,'MT_post__SoftwareComposition': [('0', 'N', 'Source')]
          ,'MT_post__CompositionType': [('0', 'N', 'Source')]
          ,'MT_post__ComponentPrototype': [('0', 'N', 'Source')]
          ,'MT_post__PPortPrototype': [('0', 'N', 'Source')]
          ,'MT_post__RPortPrototype': [('0', 'N', 'Source')]
          ,'MT_post__EcuInstance': [('0', 'N', 'Source')]
          ,'MT_post__SwcToEcuMapping': [('0', 'N', 'Source')]
          ,'MT_post__SwCompToEcuMapping_component': [('0', 'N', 'Source')]
          ,'MT_post__PortPrototype': [('0', 'N', 'Source')]
          ,'MT_post__ComponentType': [('0', 'N', 'Source')]
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__indirectLink_S']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__ECU': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Signal': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__System': []
          ,'MT_post__SystemMapping': []
          ,'MT_post__SoftwareComposition': []
          ,'MT_post__CompositionType': []
          ,'MT_post__ComponentPrototype': []
          ,'MT_post__PPortPrototype': []
          ,'MT_post__RPortPrototype': []
          ,'MT_post__EcuInstance': []
          ,'MT_post__SwcToEcuMapping': []
          ,'MT_post__SwCompToEcuMapping_component': []
          ,'MT_post__PortPrototype': []
          ,'MT_post__ComponentType': []
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__backward_link']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_post__ECU': [('0', 'N', 'Source')]
          ,'MT_post__VirtualDevice': [('0', 'N', 'Source')]
          ,'MT_post__Distributable': [('0', 'N', 'Source')]
          ,'MT_post__ExecFrame': [('0', 'N', 'Source')]
          ,'MT_post__Signal': [('0', 'N', 'Source')]
          ,'MT_post__System': [('0', 'N', 'Destination')]
          ,'MT_post__SystemMapping': [('0', 'N', 'Destination')]
          ,'MT_post__SoftwareComposition': [('0', 'N', 'Destination')]
          ,'MT_post__CompositionType': [('0', 'N', 'Destination')]
          ,'MT_post__ComponentPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__PPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__RPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__EcuInstance': [('0', 'N', 'Destination')]
          ,'MT_post__SwcToEcuMapping': [('0', 'N', 'Destination')]
          ,'MT_post__SwCompToEcuMapping_component': [('0', 'N', 'Destination')]
          ,'MT_post__PortPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__ComponentType': [('0', 'N', 'Destination')]
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__trace_link']={
          'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_post__ECU': [('0', 'N', 'Source')]
          ,'MT_post__VirtualDevice': [('0', 'N', 'Source')]
          ,'MT_post__Distributable': [('0', 'N', 'Source')]
          ,'MT_post__ExecFrame': [('0', 'N', 'Source')]
          ,'MT_post__Signal': [('0', 'N', 'Source')]
          ,'MT_post__System': [('0', 'N', 'Destination')]
          ,'MT_post__SystemMapping': [('0', 'N', 'Destination')]
          ,'MT_post__SoftwareComposition': [('0', 'N', 'Destination')]
          ,'MT_post__CompositionType': [('0', 'N', 'Destination')]
          ,'MT_post__ComponentPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__PPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__RPortPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__EcuInstance': [('0', 'N', 'Destination')]
          ,'MT_post__SwcToEcuMapping': [('0', 'N', 'Destination')]
          ,'MT_post__SwCompToEcuMapping_component': [('0', 'N', 'Destination')]
          ,'MT_post__PortPrototype': [('0', 'N', 'Destination')]
          ,'MT_post__ComponentType': [('0', 'N', 'Destination')]
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': []
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    self.CardinalityTable['MT_post__GenericEdge_GM2AUTOSAR_MM']={
          'MT_post__MatchModel': [('0', 'N', 'Source')]
          ,'MT_post__ApplyModel': [('0', 'N', 'Source')]
          ,'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_post__ECU': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__VirtualDevice': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__Distributable': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__ExecFrame': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__Signal': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__System': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__SystemMapping': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__SoftwareComposition': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__CompositionType': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__ComponentPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__PPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__RPortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__EcuInstance': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__SwcToEcuMapping': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__SwCompToEcuMapping_component': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__PortPrototype': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__ComponentType': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__GenericNode_GM2AUTOSAR_MM': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'MT_post__paired_with': []
          ,'MT_post__match_contains': []
          ,'MT_post__directLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__apply_contains': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__backward_link': []
          ,'MT_post__trace_link': []
          ,'MT_post__GenericEdge_GM2AUTOSAR_MM': [] }
    
    self.entitiesInMetaModel['MT_post__GM2AUTOSAR_MM']=["MT_post__MatchModel", "MT_post__ApplyModel", "MT_post__MetaModelElement_S", "MT_post__MetaModelElement_T", "MT_post__ECU", "MT_post__VirtualDevice", "MT_post__Distributable", "MT_post__ExecFrame", "MT_post__Signal", "MT_post__System", "MT_post__SystemMapping", "MT_post__SoftwareComposition", "MT_post__CompositionType", "MT_post__ComponentPrototype", "MT_post__PPortPrototype", "MT_post__RPortPrototype", "MT_post__EcuInstance", "MT_post__SwcToEcuMapping", "MT_post__SwCompToEcuMapping_component", "MT_post__PortPrototype", "MT_post__ComponentType", "MT_post__GenericNode_GM2AUTOSAR_MM", "MT_post__paired_with", "MT_post__match_contains", "MT_post__directLink_S", "MT_post__directLink_T", "MT_post__apply_contains", "MT_post__indirectLink_S", "MT_post__backward_link", "MT_post__trace_link", "MT_post__GenericEdge_GM2AUTOSAR_MM"]

    
def createNewMT_post__MatchModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__MatchModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__MatchModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__MatchModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__MatchModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__MatchModel", new_obj.tag)
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
def createNewMT_post__ApplyModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__ApplyModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__ApplyModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__ApplyModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__ApplyModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
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
def createNewMT_post__MetaModelElement_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__MetaModelElement_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__MetaModelElement_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__MetaModelElement_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__MetaModelElement_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
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
def createNewMT_post__MetaModelElement_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__MetaModelElement_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__MetaModelElement_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__MetaModelElement_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__MetaModelElement_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
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
def createNewMT_post__ECU(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__ECU(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__ECU"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__ECU(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__ECU(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__ECU", new_obj.tag)
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
def createNewMT_post__VirtualDevice(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__VirtualDevice(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__VirtualDevice"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__VirtualDevice(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__VirtualDevice(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__VirtualDevice", new_obj.tag)
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
def createNewMT_post__Distributable(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Distributable(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Distributable"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Distributable(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Distributable(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Distributable", new_obj.tag)
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
def createNewMT_post__ExecFrame(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__ExecFrame(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__ExecFrame"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__ExecFrame(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__ExecFrame(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__ExecFrame", new_obj.tag)
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
def createNewMT_post__Signal(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Signal(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Signal"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Signal(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Signal(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Signal", new_obj.tag)
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
def createNewMT_post__System(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__System(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__System"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__System(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__System(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__System", new_obj.tag)
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
def createNewMT_post__SystemMapping(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__SystemMapping(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__SystemMapping"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__SystemMapping(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__SystemMapping(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__SystemMapping", new_obj.tag)
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
def createNewMT_post__SoftwareComposition(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__SoftwareComposition(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__SoftwareComposition"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__SoftwareComposition(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__SoftwareComposition(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__SoftwareComposition", new_obj.tag)
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
def createNewMT_post__CompositionType(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__CompositionType(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__CompositionType"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__CompositionType(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__CompositionType(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__CompositionType", new_obj.tag)
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
def createNewMT_post__ComponentPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__ComponentPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__ComponentPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__ComponentPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__ComponentPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__ComponentPrototype", new_obj.tag)
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
def createNewMT_post__PPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__PPortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__PPortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__PPortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__PPortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__PPortPrototype", new_obj.tag)
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
def createNewMT_post__RPortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__RPortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__RPortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__RPortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__RPortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__RPortPrototype", new_obj.tag)
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
def createNewMT_post__EcuInstance(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__EcuInstance(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__EcuInstance"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__EcuInstance(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__EcuInstance(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__EcuInstance", new_obj.tag)
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
def createNewMT_post__SwcToEcuMapping(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__SwcToEcuMapping(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__SwcToEcuMapping"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__SwcToEcuMapping(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__SwcToEcuMapping(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__SwcToEcuMapping", new_obj.tag)
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
def createNewMT_post__SwCompToEcuMapping_component(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__SwCompToEcuMapping_component(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__SwCompToEcuMapping_component"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__SwCompToEcuMapping_component(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__SwCompToEcuMapping_component(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__SwCompToEcuMapping_component", new_obj.tag)
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
def createNewMT_post__PortPrototype(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__PortPrototype(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__PortPrototype"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__PortPrototype(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__PortPrototype(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__PortPrototype", new_obj.tag)
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
def createNewMT_post__ComponentType(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__ComponentType(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__ComponentType"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__ComponentType(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__ComponentType(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__ComponentType", new_obj.tag)
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
def createNewMT_post__GenericNode_GM2AUTOSAR_MM(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__GenericNode_GM2AUTOSAR_MM(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__GenericNode_GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__GenericNode_GM2AUTOSAR_MM(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__GenericNode_GM2AUTOSAR_MM(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__GenericNode_GM2AUTOSAR_MM", new_obj.tag)
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
def createNewMT_post__paired_with(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__paired_with(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__paired_with"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__paired_with(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__paired_with(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__paired_with", new_obj.tag)
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
def createNewMT_post__match_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__match_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__match_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__match_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__match_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__match_contains", new_obj.tag)
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
def createNewMT_post__directLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__directLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__directLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__directLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__directLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__directLink_S", new_obj.tag)
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
def createNewMT_post__directLink_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__directLink_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__directLink_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__directLink_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__directLink_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
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
def createNewMT_post__apply_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__apply_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__apply_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__apply_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__apply_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
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
def createNewMT_post__indirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__indirectLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__indirectLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__indirectLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__indirectLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
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
def createNewMT_post__backward_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__backward_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__backward_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__backward_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__backward_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__backward_link", new_obj.tag)
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
def createNewMT_post__trace_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__trace_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__trace_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__trace_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__trace_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
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
def createNewMT_post__GenericEdge_GM2AUTOSAR_MM(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__GenericEdge_GM2AUTOSAR_MM(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__GenericEdge_GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__GenericEdge_GM2AUTOSAR_MM(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__GenericEdge_GM2AUTOSAR_MM(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__GenericEdge_GM2AUTOSAR_MM", new_obj.tag)
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
   new_semantic_obj = ASG_MT_post__GM2AUTOSAR_MM(self)
   ne = len(self.ASGroot.listNodes["ASG_MT_post__GM2AUTOSAR_MM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_MT_post__GM2AUTOSAR_MM", new_obj.tag)
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

