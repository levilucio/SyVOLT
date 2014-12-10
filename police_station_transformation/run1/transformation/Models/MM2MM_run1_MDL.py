"""
__MM2MM_run1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Dec  4 14:08:15 2014
________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Male_S import *
from MatchModel import *
from ApplyModel import *
from Male_T import *
from match_contains import *
from apply_contains import *
from backward_link import *
from indirectLink_S import *
from directLink_T import *
from paired_with import *
from graph_paired_with import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_match_contains import *
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

def MM2MM_run1_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('MM2MM_run1')
    # --- ASG attributes over ---


    self.obj30=Male_S(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # classtype
    self.obj30.classtype.setValue('male1')

    # cardinality
    self.obj30.cardinality.setValue('+')

    # name
    self.obj30.name.setValue('6.m1')

    self.obj30.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(400.0,220.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=Male_S(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # classtype
    self.obj31.classtype.setValue('male1')

    # cardinality
    self.obj31.cardinality.setValue('+')

    # name
    self.obj31.name.setValue('6.m2')

    self.obj31.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(660.0,220.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=MatchModel(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    self.obj32.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(140.0,160.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=ApplyModel(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    self.obj33.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(140.0,400.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=Male_T(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # classtype
    self.obj34.classtype.setValue('male1')

    # name
    self.obj34.name.setValue('6.m')

    self.obj34.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(400.0,460.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=Male_T(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # classtype
    self.obj35.classtype.setValue('male1')

    # name
    self.obj35.name.setValue('6.m2')

    self.obj35.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(660.0,460.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=match_contains(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    self.obj36.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(331.0,231.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=match_contains(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    self.obj37.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(461.0,231.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=apply_contains(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    self.obj38.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(333.5,471.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=apply_contains(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    self.obj39.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(463.5,471.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=backward_link(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    self.obj40.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(461.0,381.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=backward_link(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(721.0,381.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=indirectLink_S(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    self.obj42.graphClass_= graph_indirectLink_S
    if self.genGraphics:
       new_obj = graph_indirectLink_S(591.0,261.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=directLink_T(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # associationType
    self.obj43.associationType.setValue('m2m')

    self.obj43.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(591.0,501.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=paired_with(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    self.obj44.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(203.5,321.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    # Connections for obj30 (graphObject_: Obj0) named 6.m1
    self.drawConnections(
(self.obj30,self.obj42,[461.0, 261.0, 591.0, 261.0],"true", 2) )
    # Connections for obj31 (graphObject_: Obj1) named 6.m2
    self.drawConnections(
 )
    # Connections for obj32 (graphObject_: Obj2) of type MatchModel
    self.drawConnections(
(self.obj32,self.obj44,[201.0, 201.0, 203.5, 321.0],"true", 2),
(self.obj32,self.obj36,[201.0, 201.0, 331.0, 231.0],"true", 2),
(self.obj32,self.obj37,[201.0, 201.0, 461.0, 231.0],"true", 2) )
    # Connections for obj33 (graphObject_: Obj3) of type ApplyModel
    self.drawConnections(
(self.obj33,self.obj38,[206.0, 441.0, 333.5, 471.0],"true", 2),
(self.obj33,self.obj39,[206.0, 441.0, 463.5, 471.0],"true", 2) )
    # Connections for obj34 (graphObject_: Obj4) named 6.m
    self.drawConnections(
(self.obj34,self.obj40,[461.0, 501.0, 461.0, 381.0],"true", 2),
(self.obj34,self.obj43,[461.0, 501.0, 591.0, 501.0],"true", 2) )
    # Connections for obj35 (graphObject_: Obj5) named 6.m2
    self.drawConnections(
(self.obj35,self.obj41,[721.0, 501.0, 721.0, 381.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj6) of type match_contains
    self.drawConnections(
(self.obj36,self.obj30,[331.0, 231.0, 461.0, 261.0],"true", 2) )
    # Connections for obj37 (graphObject_: Obj7) of type match_contains
    self.drawConnections(
(self.obj37,self.obj31,[461.0, 231.0, 721.0, 261.0],"true", 2) )
    # Connections for obj38 (graphObject_: Obj8) of type apply_contains
    self.drawConnections(
(self.obj38,self.obj34,[333.5, 471.0, 461.0, 501.0],"true", 2) )
    # Connections for obj39 (graphObject_: Obj9) of type apply_contains
    self.drawConnections(
(self.obj39,self.obj35,[463.5, 471.0, 721.0, 501.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj10) of type backward_link
    self.drawConnections(
(self.obj40,self.obj30,[461.0, 381.0, 461.0, 261.0],"true", 2) )
    # Connections for obj41 (graphObject_: Obj11) of type backward_link
    self.drawConnections(
(self.obj41,self.obj31,[721.0, 381.0, 721.0, 261.0],"true", 2) )
    # Connections for obj42 (graphObject_: Obj12) of type indirectLink_S
    self.drawConnections(
(self.obj42,self.obj31,[591.0, 261.0, 721.0, 261.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj13) of type directLink_T
    self.drawConnections(
(self.obj43,self.obj35,[591.0, 501.0, 721.0, 501.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj14) of type paired_with
    self.drawConnections(
(self.obj44,self.obj33,[203.5, 321.0, 206.0, 441.0],"true", 2) )

newfunction = MM2MM_run1_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
