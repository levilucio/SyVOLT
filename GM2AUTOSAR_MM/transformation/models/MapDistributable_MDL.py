"""
__MapDistributable_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Aug 23 15:40:27 2013
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ECU import *
from VirtualDevice import *
from Distributable import *
from ComponentPrototype import *
from SwCompToEcuMapping_component import *
from paired_with import *
from match_contains import *
from directLink_S import *
from directLink_T import *
from apply_contains import *
from graph_ECU import *
from graph_match_contains import *
from graph_Distributable import *
from graph_SwCompToEcuMapping_component import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_paired_with import *
from graph_ApplyModel import *
from graph_VirtualDevice import *
from graph_ComponentPrototype import *
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

def MapDistributable_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('MapDistributable')
    # --- ASG attributes over ---


    self.obj41=MatchModel(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,300.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=ApplyModel(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    self.obj42.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,580.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=ECU(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # classtype
    self.obj43.classtype.setValue('ECU')

    # cardinality
    self.obj43.cardinality.setValue('1')

    # name
    self.obj43.name.setValue('ecu1')

    self.obj43.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(240.0,400.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=VirtualDevice(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # classtype
    self.obj44.classtype.setValue('VirtualDevice')

    # cardinality
    self.obj44.cardinality.setValue('1')

    # name
    self.obj44.name.setValue('vd1')

    self.obj44.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(440.0,400.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Distributable(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # classtype
    self.obj45.classtype.setValue('Distributable')

    # cardinality
    self.obj45.cardinality.setValue('+')

    # name
    self.obj45.name.setValue('dist1')

    self.obj45.graphClass_= graph_Distributable
    if self.genGraphics:
       new_obj = graph_Distributable(660.0,400.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=ComponentPrototype(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # classtype
    self.obj46.classtype.setValue('ComponentPrototype')

    # cardinality
    self.obj46.cardinality.setValue('1')

    # name
    self.obj46.name.setValue('comp1')

    self.obj46.graphClass_= graph_ComponentPrototype
    if self.genGraphics:
       new_obj = graph_ComponentPrototype(620.0,660.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=SwCompToEcuMapping_component(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # classtype
    self.obj47.classtype.setValue('SwCompToEcuMapping_component')

    # cardinality
    self.obj47.cardinality.setValue('1')

    # name
    self.obj47.name.setValue('sctemc1')

    self.obj47.graphClass_= graph_SwCompToEcuMapping_component
    if self.genGraphics:
       new_obj = graph_SwCompToEcuMapping_component(320.0,660.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SwCompToEcuMapping_component", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=paired_with(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(157.0,484.5,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=match_contains(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(267.5,393.5,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=match_contains(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(367.5,393.5,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=match_contains(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    self.obj51.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(477.5,393.5,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=directLink_S(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # associationType
    self.obj52.associationType.setValue('virtualDevice')

    self.obj52.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(482.0,444.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=directLink_S(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # associationType
    self.obj53.associationType.setValue('distributable')

    self.obj53.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(692.0,444.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=directLink_T(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # associationType
    self.obj54.associationType.setValue('componentPrototype')

    self.obj54.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(613.0,702.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=apply_contains(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(312.0,664.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=apply_contains(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(462.0,664.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    # Connections for obj41 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj41,self.obj48,[153.0, 343.0, 157.0, 484.5],"true", 2),
(self.obj41,self.obj49,[153.0, 343.0, 267.5, 393.5],"true", 2),
(self.obj41,self.obj50,[153.0, 343.0, 367.5, 393.5],"true", 2),
(self.obj41,self.obj51,[153.0, 343.0, 477.5, 393.5],"true", 2) )
    # Connections for obj42 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj42,self.obj55,[161.0, 626.0, 312.0, 664.0],"true", 2),
(self.obj42,self.obj56,[161.0, 626.0, 462.0, 664.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj2) named ecu1
    self.drawConnections(
(self.obj43,self.obj52,[382.0, 444.0, 482.0, 444.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj3) named vd1
    self.drawConnections(
(self.obj44,self.obj53,[582.0, 444.0, 692.0, 444.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj4) named dist1
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj5) named comp1
    self.drawConnections(
 )
    # Connections for obj47 (graphObject_: Obj6) named sctemc1
    self.drawConnections(
(self.obj47,self.obj54,[463.0, 702.0, 613.0, 702.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj7) of type paired_with
    self.drawConnections(
(self.obj48,self.obj42,[157.0, 484.5, 161.0, 626.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj8) of type match_contains
    self.drawConnections(
(self.obj49,self.obj43,[267.5, 393.5, 382.0, 444.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj9) of type match_contains
    self.drawConnections(
(self.obj50,self.obj44,[367.5, 393.5, 582.0, 444.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj10) of type match_contains
    self.drawConnections(
(self.obj51,self.obj45,[477.5, 393.5, 802.0, 444.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj11) of type directLink_S
    self.drawConnections(
(self.obj52,self.obj44,[482.0, 444.0, 582.0, 444.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj12) of type directLink_S
    self.drawConnections(
(self.obj53,self.obj45,[692.0, 444.0, 802.0, 444.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj13) of type directLink_T
    self.drawConnections(
(self.obj54,self.obj46,[613.0, 702.0, 763.0, 702.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj14) of type apply_contains
    self.drawConnections(
(self.obj55,self.obj47,[312.0, 664.0, 463.0, 702.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj15) of type apply_contains
    self.drawConnections(
(self.obj56,self.obj46,[462.0, 664.0, 763.0, 702.0],"true", 2) )

newfunction = MapDistributable_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
