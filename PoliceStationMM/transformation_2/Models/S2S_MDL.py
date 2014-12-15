"""
__S2S_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Dec 12 16:29:08 2014
_________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Station_S import *
from MatchModel import *
from ApplyModel import *
from Station_T import *
from Attribute import *
from Equation import *
from Constant import *
from match_contains import *
from apply_contains import *
from paired_with import *
from hasAttr_S import *
from leftExpr import *
from rightExpr import *
from graph_hasAttr_S import *
from graph_Equation import *
from graph_match_contains import *
from graph_Attribute import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_Station_T import *
from graph_Station_S import *
from graph_paired_with import *
from graph_leftExpr import *
from graph_ApplyModel import *
from graph_Constant import *
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

def S2S_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('S2S')
    # --- ASG attributes over ---


    self.obj37=Station_S(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # classtype
    self.obj37.classtype.setValue('1')

    # cardinality
    self.obj37.cardinality.setValue('s_')

    # name
    self.obj37.name.setValue('s_')

    self.obj37.graphClass_= graph_Station_S
    if self.genGraphics:
       new_obj = graph_Station_S(420.0,140.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj35=MatchModel(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    self.obj35.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(140.0,80.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=ApplyModel(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    self.obj36.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(140.0,340.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj38=Station_T(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # classtype
    self.obj38.classtype.setValue('t_')

    # name
    self.obj38.name.setValue('s_')

    self.obj38.graphClass_= graph_Station_T
    if self.genGraphics:
       new_obj = graph_Station_T(420.0,300.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj55=Attribute(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # name
    self.obj55.name.setValue('name')

    self.obj55.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(660.0,150.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj50=Equation(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(870.0,42.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Constant(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # value
    self.obj51.value.setValue('somestation')

    self.obj51.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1010.0,142.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj39=match_contains(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    self.obj39.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(341.0,151.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=apply_contains(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    self.obj40.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(343.5,361.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj44=paired_with(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    self.obj44.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(203.5,251.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj58=hasAttr_S(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    self.obj58.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(595.0,179.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=leftExpr(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    self.obj59.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(811.0,132.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj54=rightExpr(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    self.obj54.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(987.0,132.5,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    # Connections for obj37 (graphObject_: Obj2) named s_
    self.drawConnections(
(self.obj37,self.obj58,[481.0, 181.0, 595.0, 179.5],"true", 0) )
    # Connections for obj35 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj35,self.obj39,[201.0, 121.0, 341.0, 151.0],"true", 2),
(self.obj35,self.obj44,[201.0, 121.0, 203.5, 251.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj36,self.obj40,[206.0, 381.0, 343.5, 361.0],"true", 2) )
    # Connections for obj38 (graphObject_: Obj3) named s_
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj13) named name
    self.drawConnections(
 )
    # Connections for obj50 (graphObject_: Obj10) of type Equation
    self.drawConnections(
(self.obj50,self.obj54,[909.0, 84.0, 987.0, 132.5],"true", 2),
(self.obj50,self.obj59,[909.0, 84.0, 811.0, 132.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj11) of type Constant
    self.drawConnections(
 )
    # Connections for obj39 (graphObject_: Obj4) of type match_contains
    self.drawConnections(
(self.obj39,self.obj37,[341.0, 151.0, 481.0, 181.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj5) of type apply_contains
    self.drawConnections(
(self.obj40,self.obj38,[343.5, 361.0, 481.0, 341.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj7) of type paired_with
    self.drawConnections(
(self.obj44,self.obj36,[203.5, 251.0, 206.0, 381.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj14) of type hasAttr_S
    self.drawConnections(
(self.obj58,self.obj55,[595.0, 179.5, 713.0, 180.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj15) of type leftExpr
    self.drawConnections(
(self.obj59,self.obj55,[811.0, 132.0, 713.0, 180.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj12) of type rightExpr
    self.drawConnections(
(self.obj54,self.obj51,[987.0, 132.5, 1065.0, 181.0],"true", 2) )

newfunction = S2S_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
