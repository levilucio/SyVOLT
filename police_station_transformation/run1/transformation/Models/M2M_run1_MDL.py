"""
__M2M_run1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Nov 10 14:36:44 2014
______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Male_S import *
from MatchModel import *
from ApplyModel import *
from Male_T import *
from match_contains import *
from apply_contains import *
from paired_with import *
from graph_paired_with import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_match_contains import *
from graph_Male_T import *
from graph_ApplyModel import *
from graph_Male_S import *
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

def M2M_run1_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('M2M_run1')
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
    self.obj30.name.setValue('3.m')

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

    self.obj31=MatchModel(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    self.obj31.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(140.0,160.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=ApplyModel(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    self.obj32.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(140.0,400.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=Male_T(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # classtype
    self.obj33.classtype.setValue('male1')

    # name
    self.obj33.name.setValue('3.m')

    self.obj33.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(400.0,460.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=match_contains(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    self.obj34.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(331.0,231.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=apply_contains(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    self.obj35.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(333.5,471.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=paired_with(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    self.obj36.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(203.5,321.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    # Connections for obj30 (graphObject_: Obj0) named 3.m
    self.drawConnections(
 )
    # Connections for obj31 (graphObject_: Obj1) of type MatchModel
    self.drawConnections(
(self.obj31,self.obj36,[201.0, 201.0, 203.5, 321.0],"true", 2),
(self.obj31,self.obj34,[201.0, 201.0, 331.0, 231.0],"true", 2) )
    # Connections for obj32 (graphObject_: Obj2) of type ApplyModel
    self.drawConnections(
(self.obj32,self.obj35,[206.0, 441.0, 333.5, 471.0],"true", 2) )
    # Connections for obj33 (graphObject_: Obj3) named 3.m
    self.drawConnections(
 )
    # Connections for obj34 (graphObject_: Obj4) of type match_contains
    self.drawConnections(
(self.obj34,self.obj30,[331.0, 231.0, 461.0, 261.0],"true", 2) )
    # Connections for obj35 (graphObject_: Obj5) of type apply_contains
    self.drawConnections(
(self.obj35,self.obj33,[333.5, 471.0, 461.0, 501.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj6) of type paired_with
    self.drawConnections(
(self.obj36,self.obj32,[203.5, 321.0, 206.0, 441.0],"true", 2) )

newfunction = M2M_run1_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
