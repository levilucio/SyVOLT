"""
__F2F_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Dec 12 16:57:02 2014
_________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Female_S import *
from MatchModel import *
from ApplyModel import *
from Female_T import *
from Attribute import *
from Equation import *
from match_contains import *
from apply_contains import *
from paired_with import *
from hasAttr_S import *
from hasAttr_T import *
from leftExpr import *
from rightExpr import *
from graph_hasAttr_S import *
from graph_Equation import *
from graph_match_contains import *
from graph_hasAttr_T import *
from graph_Female_T import *
from graph_Attribute import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_leftExpr import *
from graph_Female_S import *
from graph_ApplyModel import *
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

def F2F_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('F2F')
    # --- ASG attributes over ---


    self.obj56=Female_S(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # classtype
    self.obj56.classtype.setValue('1')

    # cardinality
    self.obj56.cardinality.setValue('s_')

    # name
    self.obj56.name.setValue('s_')

    self.obj56.graphClass_= graph_Female_S
    if self.genGraphics:
       new_obj = graph_Female_S(420.0,140.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj36=MatchModel(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    self.obj36.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(140.0,80.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=ApplyModel(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    self.obj37.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(140.0,340.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj57=Female_T(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # classtype
    self.obj57.classtype.setValue('t_')

    # name
    self.obj57.name.setValue('s_')

    self.obj57.graphClass_= graph_Female_T
    if self.genGraphics:
       new_obj = graph_Female_T(420.0,300.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj39=Attribute(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # name
    self.obj39.name.setValue('name')

    self.obj39.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,149.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=Attribute(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # name
    self.obj40.name.setValue('name')

    self.obj40.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,310.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=Equation(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(840.0,220.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj58=match_contains(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    self.obj58.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(341.0,151.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=apply_contains(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    self.obj59.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(343.5,361.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

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

    self.obj60=hasAttr_S(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(607.0,180.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=hasAttr_T(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    self.obj61.graphClass_= graph_hasAttr_T
    if self.genGraphics:
       new_obj = graph_hasAttr_T(607.0,340.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj47=leftExpr(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(806.0,220.5,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=rightExpr(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(806.0,301.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    # Connections for obj56 (graphObject_: Obj21) named s_
    self.drawConnections(
(self.obj56,self.obj60,[481.0, 181.0, 607.0, 180.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj1) of type MatchModel
    self.drawConnections(
(self.obj36,self.obj44,[201.0, 121.0, 203.5, 251.0],"true", 2),
(self.obj36,self.obj58,[201.0, 121.0, 341.0, 151.0],"true", 0) )
    # Connections for obj37 (graphObject_: Obj2) of type ApplyModel
    self.drawConnections(
(self.obj37,self.obj59,[206.0, 381.0, 343.5, 361.0],"true", 0) )
    # Connections for obj57 (graphObject_: Obj22) named s_
    self.drawConnections(
(self.obj57,self.obj61,[481.0, 341.0, 607.0, 340.5],"true", 2) )
    # Connections for obj39 (graphObject_: Obj4) named name
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj5) named name
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj6) of type Equation
    self.drawConnections(
(self.obj41,self.obj47,[879.0, 262.0, 806.0, 220.5],"true", 2),
(self.obj41,self.obj48,[879.0, 262.0, 806.0, 301.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj23) of type match_contains
    self.drawConnections(
(self.obj58,self.obj56,[341.0, 151.0, 481.0, 181.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj24) of type apply_contains
    self.drawConnections(
(self.obj59,self.obj57,[343.5, 361.0, 481.0, 341.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj9) of type paired_with
    self.drawConnections(
(self.obj44,self.obj37,[203.5, 251.0, 206.0, 381.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj25) of type hasAttr_S
    self.drawConnections(
(self.obj60,self.obj39,[607.0, 180.0, 733.0, 179.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj26) of type hasAttr_T
    self.drawConnections(
(self.obj61,self.obj40,[607.0, 340.5, 733.0, 340.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj12) of type leftExpr
    self.drawConnections(
(self.obj47,self.obj39,[806.0, 220.5, 733.0, 179.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj13) of type rightExpr
    self.drawConnections(
(self.obj48,self.obj40,[806.0, 301.0, 733.0, 340.0],"true", 2) )

newfunction = F2F_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
