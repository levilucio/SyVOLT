"""
__MapVirtualDeviceFAULTY_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sat Feb  1 21:24:22 2014
____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from directLink_S import *
from apply_contains import *
from paired_with import *
from ApplyModel import *
from ECU import *
from SwcToEcuMapping import *
from VirtualDevice import *
from match_contains import *
from MatchModel import *
from graph_ECU import *
from graph_match_contains import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_paired_with import *
from graph_ApplyModel import *
from graph_VirtualDevice import *
from graph_SwcToEcuMapping import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def MapVirtualDeviceFAULTY_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('MapVirtualDeviceFAULTY')
    # --- ASG attributes over ---


    self.obj220=directLink_S(self)
    self.obj220.isGraphObjectVisual = True

    if(hasattr(self.obj220, '_setHierarchicalLink')):
      self.obj220._setHierarchicalLink(False)

    # associationType
    self.obj220.associationType.setValue('virtualDevice')

    self.obj220.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(692.0,244.0,self.obj220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj220)
    self.globalAndLocalPostcondition(self.obj220, rootNode)
    self.obj220.postAction( rootNode.CREATE )

    self.obj213=apply_contains(self)
    self.obj213.isGraphObjectVisual = True

    if(hasattr(self.obj213, '_setHierarchicalLink')):
      self.obj213._setHierarchicalLink(False)

    self.obj213.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(470.5,514.0,self.obj213)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj213.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj213)
    self.globalAndLocalPostcondition(self.obj213, rootNode)
    self.obj213.postAction( rootNode.CREATE )

    self.obj211=paired_with(self)
    self.obj211.isGraphObjectVisual = True

    if(hasattr(self.obj211, '_setHierarchicalLink')):
      self.obj211._setHierarchicalLink(False)

    self.obj211.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(307.0,354.5,self.obj211)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj211.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj211)
    self.globalAndLocalPostcondition(self.obj211, rootNode)
    self.obj211.postAction( rootNode.CREATE )

    self.obj210=ApplyModel(self)
    self.obj210.isGraphObjectVisual = True

    if(hasattr(self.obj210, '_setHierarchicalLink')):
      self.obj210._setHierarchicalLink(False)

    self.obj210.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(180.0,440.0,self.obj210)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj210.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj210)
    self.globalAndLocalPostcondition(self.obj210, rootNode)
    self.obj210.postAction( rootNode.CREATE )

    self.obj216=ECU(self)
    self.obj216.isGraphObjectVisual = True

    if(hasattr(self.obj216, '_setHierarchicalLink')):
      self.obj216._setHierarchicalLink(False)

    # classtype
    self.obj216.classtype.setValue('ECU')

    # cardinality
    self.obj216.cardinality.setValue('1')

    # name
    self.obj216.name.setValue('ecu1')

    self.obj216.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(420.0,240.0,self.obj216)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj216.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj216)
    self.globalAndLocalPostcondition(self.obj216, rootNode)
    self.obj216.postAction( rootNode.CREATE )

    self.obj212=SwcToEcuMapping(self)
    self.obj212.isGraphObjectVisual = True

    if(hasattr(self.obj212, '_setHierarchicalLink')):
      self.obj212._setHierarchicalLink(False)

    # classtype
    self.obj212.classtype.setValue('SwcToEcuMapping')

    # cardinality
    self.obj212.cardinality.setValue('1')

    # name
    self.obj212.name.setValue('stem1')

    self.obj212.graphClass_= graph_SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_SwcToEcuMapping(480.0,500.0,self.obj212)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj212.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj212)
    self.globalAndLocalPostcondition(self.obj212, rootNode)
    self.obj212.postAction( rootNode.CREATE )

    self.obj219=VirtualDevice(self)
    self.obj219.isGraphObjectVisual = True

    if(hasattr(self.obj219, '_setHierarchicalLink')):
      self.obj219._setHierarchicalLink(False)

    # classtype
    self.obj219.classtype.setValue('VirtualDevice')

    # cardinality
    self.obj219.cardinality.setValue('+')

    # name
    self.obj219.name.setValue('vd1')

    self.obj219.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(700.0,240.0,self.obj219)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj219.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj219)
    self.globalAndLocalPostcondition(self.obj219, rootNode)
    self.obj219.postAction( rootNode.CREATE )

    self.obj226=match_contains(self)
    self.obj226.isGraphObjectVisual = True

    if(hasattr(self.obj226, '_setHierarchicalLink')):
      self.obj226._setHierarchicalLink(False)

    self.obj226.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(427.5,253.5,self.obj226)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj226.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj226)
    self.globalAndLocalPostcondition(self.obj226, rootNode)
    self.obj226.postAction( rootNode.CREATE )

    self.obj227=match_contains(self)
    self.obj227.isGraphObjectVisual = True

    if(hasattr(self.obj227, '_setHierarchicalLink')):
      self.obj227._setHierarchicalLink(False)

    self.obj227.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(567.5,253.5,self.obj227)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj227.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj227)
    self.globalAndLocalPostcondition(self.obj227, rootNode)
    self.obj227.postAction( rootNode.CREATE )

    self.obj209=MatchModel(self)
    self.obj209.isGraphObjectVisual = True

    if(hasattr(self.obj209, '_setHierarchicalLink')):
      self.obj209._setHierarchicalLink(False)

    self.obj209.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(160.0,180.0,self.obj209)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj209.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj209)
    self.globalAndLocalPostcondition(self.obj209, rootNode)
    self.obj209.postAction( rootNode.CREATE )

    # Connections for obj220 (graphObject_: Obj70) of type directLink_S
    self.drawConnections(
(self.obj220,self.obj219,[692.0, 244.0, 842.0, 284.0],"true", 2) )
    # Connections for obj213 (graphObject_: Obj67) of type apply_contains
    self.drawConnections(
(self.obj213,self.obj212,[470.5, 514.0, 620.0, 542.0],"true", 2) )
    # Connections for obj211 (graphObject_: Obj65) of type paired_with
    self.drawConnections(
(self.obj211,self.obj210,[307.0, 354.5, 321.0, 486.0],"true", 2) )
    # Connections for obj210 (graphObject_: Obj64) of type ApplyModel
    self.drawConnections(
(self.obj210,self.obj213,[321.0, 486.0, 470.5, 514.0],"true", 2) )
    # Connections for obj216 (graphObject_: Obj68) named ecu1
    self.drawConnections(
(self.obj216,self.obj220,[562.0, 284.0, 692.0, 244.0],"true", 2) )
    # Connections for obj212 (graphObject_: Obj66) named stem1
    self.drawConnections(
 )
    # Connections for obj219 (graphObject_: Obj69) named vd1
    self.drawConnections(
 )
    # Connections for obj226 (graphObject_: Obj71) of type match_contains
    self.drawConnections(
(self.obj226,self.obj216,[427.5, 253.5, 562.0, 284.0],"true", 2) )
    # Connections for obj227 (graphObject_: Obj72) of type match_contains
    self.drawConnections(
(self.obj227,self.obj219,[567.5, 253.5, 842.0, 284.0],"true", 2) )
    # Connections for obj209 (graphObject_: Obj63) of type MatchModel
    self.drawConnections(
(self.obj209,self.obj211,[293.0, 223.0, 307.0, 354.5],"true", 2),
(self.obj209,self.obj226,[293.0, 223.0, 427.5, 253.5],"true", 2),
(self.obj209,self.obj227,[293.0, 223.0, 567.5, 253.5],"true", 2) )

newfunction = MapVirtualDeviceFAULTY_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
