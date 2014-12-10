"""
__rule1_2_exists_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Aug 22 14:05:43 2013
____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ECU import *
from VirtualDevice import *
from System import *
from SoftwareComposition import *
from paired_with import *
from match_contains import *
from directLink_S import *
from directLink_T import *
from apply_contains import *
from backward_link import *
from graph_ECU import *
from graph_SoftwareComposition import *
from graph_match_contains import *
from graph_backward_link import *
from graph_ApplyModel import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_paired_with import *
from graph_System import *
from graph_VirtualDevice import *
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

def rule1_2_exists_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('rule1_2Exists')
    # --- ASG attributes over ---


    self.obj41=MatchModel(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(240.0,160.0,self.obj41)
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
       new_obj = graph_ApplyModel(240.0,460.0,self.obj42)
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
    self.obj43.name.setValue('ecu2')

    self.obj43.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(480.0,260.0,self.obj43)
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
    self.obj44.name.setValue('vd2')

    self.obj44.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(780.0,260.0,self.obj44)
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

    self.obj45=System(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # classtype
    self.obj45.classtype.setValue('System')

    # cardinality
    self.obj45.cardinality.setValue('1')

    # name
    self.obj45.name.setValue('s2')

    self.obj45.graphClass_= graph_System
    if self.genGraphics:
       new_obj = graph_System(480.0,560.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=SoftwareComposition(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # classtype
    self.obj46.classtype.setValue('SoftwareComposition')

    # cardinality
    self.obj46.cardinality.setValue('1')

    # name
    self.obj46.name.setValue('sc2')

    self.obj46.graphClass_= graph_SoftwareComposition
    if self.genGraphics:
       new_obj = graph_SoftwareComposition(780.0,560.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=paired_with(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(377.0,354.5,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=match_contains(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(497.5,253.5,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
       new_obj = graph_match_contains(647.5,253.5,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=directLink_S(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # associationType
    self.obj50.associationType.setValue('virtualDevice')

    self.obj50.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(772.0,304.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=directLink_T(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # associationType
    self.obj51.associationType.setValue('softwareComposition')

    self.obj51.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(772.5,602.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=apply_contains(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    self.obj52.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(500.5,554.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=apply_contains(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    self.obj53.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(653.0,554.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=backward_link(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # type
    self.obj54.type.setValue('ruleDef')

    self.obj54.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(621.0,453.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=backward_link(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # type
    self.obj55.type.setValue('ruleDef')

    self.obj55.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(923.5,453.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    # Connections for obj41 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj41,self.obj48,[373.0, 203.0, 497.5, 253.5],"true", 2),
(self.obj41,self.obj49,[373.0, 203.0, 647.5, 253.5],"true", 2),
(self.obj41,self.obj47,[373.0, 203.0, 377.0, 354.5],"true", 2) )
    # Connections for obj42 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj42,self.obj52,[381.0, 506.0, 500.5, 554.0],"true", 2),
(self.obj42,self.obj53,[381.0, 506.0, 653.0, 554.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj2) named ecu2
    self.drawConnections(
(self.obj43,self.obj50,[622.0, 304.0, 772.0, 304.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj3) named vd2
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj4) named s2
    self.drawConnections(
(self.obj45,self.obj51,[620.0, 602.0, 772.5, 602.0],"true", 2),
(self.obj45,self.obj54,[620.0, 602.0, 621.0, 453.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj5) named sc2
    self.drawConnections(
(self.obj46,self.obj55,[925.0, 602.0, 923.5, 453.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj6) of type paired_with
    self.drawConnections(
(self.obj47,self.obj42,[377.0, 354.5, 381.0, 506.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj7) of type match_contains
    self.drawConnections(
(self.obj48,self.obj43,[497.5, 253.5, 622.0, 304.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj8) of type match_contains
    self.drawConnections(
(self.obj49,self.obj44,[647.5, 253.5, 922.0, 304.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj9) of type directLink_S
    self.drawConnections(
(self.obj50,self.obj44,[772.0, 304.0, 922.0, 304.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj10) of type directLink_T
    self.drawConnections(
(self.obj51,self.obj46,[772.5, 602.0, 925.0, 602.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj11) of type apply_contains
    self.drawConnections(
(self.obj52,self.obj45,[500.5, 554.0, 620.0, 602.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj12) of type apply_contains
    self.drawConnections(
(self.obj53,self.obj46,[653.0, 554.0, 925.0, 602.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj13) of type backward_link
    self.drawConnections(
(self.obj54,self.obj43,[621.0, 453.0, 622.0, 304.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj14) of type backward_link
    self.drawConnections(
(self.obj55,self.obj44,[923.5, 453.0, 922.0, 304.0],"true", 2) )

newfunction = rule1_2_exists_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
