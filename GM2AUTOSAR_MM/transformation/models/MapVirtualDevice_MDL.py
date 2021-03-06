"""
__MapVirtualDevice_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Sep  9 15:53:32 2013
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ECU import *
from VirtualDevice import *
from Distributable import *
from SwcToEcuMapping import *
from paired_with import *
from match_contains import *
from directLink_S import *
from apply_contains import *
from graph_ECU import *
from graph_match_contains import *
from graph_Distributable import *
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

def MapVirtualDevice_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('MapVirtualDevice')
    # --- ASG attributes over ---


    self.obj91=MatchModel(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    self.obj91.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(40.0,300.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=ApplyModel(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    self.obj92.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(40.0,560.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=ECU(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # classtype
    self.obj93.classtype.setValue('ECU')

    # cardinality
    self.obj93.cardinality.setValue('1')

    # name
    self.obj93.name.setValue('ecu1')

    self.obj93.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(240.0,400.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=VirtualDevice(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # classtype
    self.obj94.classtype.setValue('VirtualDevice')

    # cardinality
    self.obj94.cardinality.setValue('+')

    # name
    self.obj94.name.setValue('vd1')

    self.obj94.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(480.0,400.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=Distributable(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # classtype
    self.obj95.classtype.setValue('Distributable')

    # cardinality
    self.obj95.cardinality.setValue('1')

    # name
    self.obj95.name.setValue('dist1')

    self.obj95.graphClass_= graph_Distributable
    if self.genGraphics:
       new_obj = graph_Distributable(740.0,400.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=SwcToEcuMapping(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # classtype
    self.obj96.classtype.setValue('SwcToEcuMapping')

    # cardinality
    self.obj96.cardinality.setValue('1')

    # name
    self.obj96.name.setValue('stem1')

    self.obj96.graphClass_= graph_SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_SwcToEcuMapping(340.0,640.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=paired_with(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    self.obj97.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(177.0,474.5,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=match_contains(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    self.obj98.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(277.5,393.5,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=match_contains(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    self.obj99.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(397.5,393.5,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=match_contains(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    self.obj100.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(527.5,393.5,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=directLink_S(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # associationType
    self.obj101.associationType.setValue('virtualDevice')

    self.obj101.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(502.0,444.0,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=directLink_S(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # associationType
    self.obj102.associationType.setValue('distributable')

    self.obj102.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(752.0,444.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=apply_contains(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    self.obj103.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(330.5,644.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    # Connections for obj91 (graphObject_: Obj24) of type MatchModel
    self.drawConnections(
(self.obj91,self.obj98,[173.0, 343.0, 277.5, 393.5],"true", 2),
(self.obj91,self.obj99,[173.0, 343.0, 397.5, 393.5],"true", 2),
(self.obj91,self.obj100,[173.0, 343.0, 527.5, 393.5],"true", 2),
(self.obj91,self.obj97,[173.0, 343.0, 177.0, 474.5],"true", 2) )
    # Connections for obj92 (graphObject_: Obj25) of type ApplyModel
    self.drawConnections(
(self.obj92,self.obj103,[181.0, 606.0, 330.5, 644.0],"true", 2) )
    # Connections for obj93 (graphObject_: Obj26) named ecu1
    self.drawConnections(
(self.obj93,self.obj101,[382.0, 444.0, 502.0, 444.0],"true", 2) )
    # Connections for obj94 (graphObject_: Obj27) named vd1
    self.drawConnections(
(self.obj94,self.obj102,[622.0, 444.0, 752.0, 444.0],"true", 2) )
    # Connections for obj95 (graphObject_: Obj28) named dist1
    self.drawConnections(
 )
    # Connections for obj96 (graphObject_: Obj29) named stem1
    self.drawConnections(
 )
    # Connections for obj97 (graphObject_: Obj30) of type paired_with
    self.drawConnections(
(self.obj97,self.obj92,[177.0, 474.5, 181.0, 606.0],"true", 2) )
    # Connections for obj98 (graphObject_: Obj31) of type match_contains
    self.drawConnections(
(self.obj98,self.obj93,[277.5, 393.5, 382.0, 444.0],"true", 2) )
    # Connections for obj99 (graphObject_: Obj32) of type match_contains
    self.drawConnections(
(self.obj99,self.obj94,[397.5, 393.5, 622.0, 444.0],"true", 2) )
    # Connections for obj100 (graphObject_: Obj33) of type match_contains
    self.drawConnections(
(self.obj100,self.obj95,[527.5, 393.5, 882.0, 444.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj34) of type directLink_S
    self.drawConnections(
(self.obj101,self.obj94,[502.0, 444.0, 622.0, 444.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj35) of type directLink_S
    self.drawConnections(
(self.obj102,self.obj95,[752.0, 444.0, 882.0, 444.0],"true", 2) )
    # Connections for obj103 (graphObject_: Obj36) of type apply_contains
    self.drawConnections(
(self.obj103,self.obj96,[330.5, 644.0, 480.0, 682.0],"true", 2) )

newfunction = MapVirtualDevice_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
