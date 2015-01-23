"""
__SM2SM_partial_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Jan 22 15:46:41 2015
___________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Station_S import *
from Male_S import *
from MatchModel import *
from ApplyModel import *
from Station_T import *
from Male_T import *
from Attribute import *
from match_contains import *
from apply_contains import *
from backward_link import *
from indirectLink_S import *
from directLink_T import *
from paired_with import *
from hasAttr_S import *
from graph_hasAttr_S import *
from graph_match_contains import *
from graph_Attribute import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_Station_T import *
from graph_Station_S import *
from graph_paired_with import *
from graph_Male_T import *
from graph_ApplyModel import *
from graph_Male_S import *
from graph_indirectLink_S import *
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

def SM2SM_partial_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('SM2SM_partial')
    # --- ASG attributes over ---


    self.obj35=Station_S(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # classtype
    self.obj35.classtype.setValue('1')

    # cardinality
    self.obj35.cardinality.setValue('s_')

    # name
    self.obj35.name.setValue('s_')

    self.obj35.graphClass_= graph_Station_S
    if self.genGraphics:
       new_obj = graph_Station_S(520.0,240.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=Male_S(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # classtype
    self.obj36.classtype.setValue('1')

    # cardinality
    self.obj36.cardinality.setValue('s_')

    # name
    self.obj36.name.setValue('s_')

    self.obj36.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(780.0,240.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=MatchModel(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    self.obj37.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(280.0,140.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=ApplyModel(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    self.obj38.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(280.0,500.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=Station_T(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # classtype
    self.obj39.classtype.setValue('t_')

    # name
    self.obj39.name.setValue('s_')

    self.obj39.graphClass_= graph_Station_T
    if self.genGraphics:
       new_obj = graph_Station_T(520.0,420.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=Male_T(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # classtype
    self.obj40.classtype.setValue('t_')

    # name
    self.obj40.name.setValue('s_')

    self.obj40.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(780.0,420.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=Attribute(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # name
    self.obj41.name.setValue('name')

    self.obj41.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(560.0,80.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=Attribute(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # name
    self.obj42.name.setValue('name')

    self.obj42.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1040.0,80.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj47=match_contains(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(461.0,231.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
       new_obj = graph_match_contains(591.0,231.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=apply_contains(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(463.5,501.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=apply_contains(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(593.5,501.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=backward_link(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    self.obj51.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(581.0,371.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=backward_link(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    self.obj52.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(841.0,371.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=indirectLink_S(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    self.obj53.graphClass_= graph_indirectLink_S
    if self.genGraphics:
       new_obj = graph_indirectLink_S(711.0,281.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("indirectLink_S", new_obj.tag)
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
    self.obj54.associationType.setValue('t_')

    self.obj54.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(711.0,461.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=paired_with(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(343.5,361.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=hasAttr_S(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(597.0,195.5,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=hasAttr_S(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(967.0,195.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    # Connections for obj35 (graphObject_: Obj0) named s_
    self.drawConnections(
(self.obj35,self.obj53,[581.0, 281.0, 711.0, 281.0],"true", 2),
(self.obj35,self.obj56,[581.0, 281.0, 597.0, 195.5],"true", 2) )
    # Connections for obj36 (graphObject_: Obj1) named s_
    self.drawConnections(
(self.obj36,self.obj57,[841.0, 281.0, 967.0, 195.5],"true", 2) )
    # Connections for obj37 (graphObject_: Obj2) of type MatchModel
    self.drawConnections(
(self.obj37,self.obj55,[341.0, 181.0, 343.5, 361.0],"true", 2),
(self.obj37,self.obj47,[341.0, 181.0, 461.0, 231.0],"true", 2),
(self.obj37,self.obj48,[341.0, 181.0, 591.0, 231.0],"true", 2) )
    # Connections for obj38 (graphObject_: Obj3) of type ApplyModel
    self.drawConnections(
(self.obj38,self.obj49,[346.0, 541.0, 463.5, 501.0],"true", 2),
(self.obj38,self.obj50,[346.0, 541.0, 593.5, 501.0],"true", 2) )
    # Connections for obj39 (graphObject_: Obj4) named s_
    self.drawConnections(
(self.obj39,self.obj54,[581.0, 461.0, 711.0, 461.0],"true", 2),
(self.obj39,self.obj51,[581.0, 461.0, 581.0, 371.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj5) named s_
    self.drawConnections(
(self.obj40,self.obj52,[841.0, 461.0, 841.0, 371.0],"true", 2) )
    # Connections for obj41 (graphObject_: Obj6) named name
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj7) named name
    self.drawConnections(
 )
    # Connections for obj47 (graphObject_: Obj12) of type match_contains
    self.drawConnections(
(self.obj47,self.obj35,[461.0, 231.0, 581.0, 281.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj13) of type match_contains
    self.drawConnections(
(self.obj48,self.obj36,[591.0, 231.0, 841.0, 281.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj14) of type apply_contains
    self.drawConnections(
(self.obj49,self.obj39,[463.5, 501.0, 581.0, 461.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj15) of type apply_contains
    self.drawConnections(
(self.obj50,self.obj40,[593.5, 501.0, 841.0, 461.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj16) of type backward_link
    self.drawConnections(
(self.obj51,self.obj35,[581.0, 371.0, 581.0, 281.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj17) of type backward_link
    self.drawConnections(
(self.obj52,self.obj36,[841.0, 371.0, 841.0, 281.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj18) of type indirectLink_S
    self.drawConnections(
(self.obj53,self.obj36,[711.0, 281.0, 841.0, 281.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj19) of type directLink_T
    self.drawConnections(
(self.obj54,self.obj40,[711.0, 461.0, 841.0, 461.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj20) of type paired_with
    self.drawConnections(
(self.obj55,self.obj38,[343.5, 361.0, 346.0, 541.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj21) of type hasAttr_S
    self.drawConnections(
(self.obj56,self.obj41,[597.0, 195.5, 613.0, 110.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj22) of type hasAttr_S
    self.drawConnections(
(self.obj57,self.obj42,[967.0, 195.5, 1093.0, 110.0],"true", 2) )

newfunction = SM2SM_partial_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
