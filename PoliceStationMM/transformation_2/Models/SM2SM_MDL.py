"""
__SM2SM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 09:26:06 2014
___________________________________________________________________
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
from Equation import *
from Constant import *
from match_contains import *
from apply_contains import *
from backward_link import *
from indirectLink_S import *
from directLink_T import *
from paired_with import *
from hasAttr_S import *
from leftExpr import *
from rightExpr import *
from graph_hasAttr_S import *
from graph_Equation import *
from graph_match_contains import *
from graph_Attribute import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_Station_T import *
from graph_Station_S import *
from graph_paired_with import *
from graph_leftExpr import *
from graph_Male_T import *
from graph_ApplyModel import *
from graph_Constant import *
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

def SM2SM_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('SM2SM')
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
       new_obj = graph_Station_S(520.0,240.0,self.obj37)
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

    self.obj39=Male_S(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # classtype
    self.obj39.classtype.setValue('1')

    # cardinality
    self.obj39.cardinality.setValue('s_')

    # name
    self.obj39.name.setValue('s_')

    self.obj39.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(780.0,240.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj35=MatchModel(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    self.obj35.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(280.0,140.0,self.obj35)
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
       new_obj = graph_ApplyModel(280.0,500.0,self.obj36)
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
       new_obj = graph_Station_T(520.0,420.0,self.obj38)
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

    self.obj50=Attribute(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # name
    self.obj50.name.setValue('name')

    self.obj50.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(560.0,80.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj64=Attribute(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # name
    self.obj64.name.setValue('name')

    self.obj64.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1040.0,80.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj56=Equation(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(720.0,20.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj67=Equation(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    self.obj67.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1200.0,20.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj57=Constant(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # value
    self.obj57.value.setValue('somestation')

    self.obj57.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(840.0,80.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj68=Constant(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # value
    self.obj68.value.setValue('somemale')

    self.obj68.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1340.0,80.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj42=match_contains(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    self.obj42.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(461.0,231.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=match_contains(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    self.obj43.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(591.0,231.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=apply_contains(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    self.obj44.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(463.5,501.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=apply_contains(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    self.obj45.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(593.5,501.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj48=backward_link(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(581.0,371.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=backward_link(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(841.0,371.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj46=indirectLink_S(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    self.obj46.graphClass_= graph_indirectLink_S
    if self.genGraphics:
       new_obj = graph_indirectLink_S(711.0,281.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=directLink_T(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # associationType
    self.obj47.associationType.setValue('t_')

    self.obj47.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(711.0,461.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj41=paired_with(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(343.5,361.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj55=hasAttr_S(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(597.0,195.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj75=hasAttr_S(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    self.obj75.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(967.0,195.5,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj62=leftExpr(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    self.obj62.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(686.0,86.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj73=leftExpr(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    self.obj73.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1166.0,86.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj63=rightExpr(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    self.obj63.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(827.0,90.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj74=rightExpr(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    self.obj74.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1317.0,90.5,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    # Connections for obj37 (graphObject_: Obj2) named s_
    self.drawConnections(
(self.obj37,self.obj46,[581.0, 281.0, 711.0, 281.0],"true", 2),
(self.obj37,self.obj55,[581.0, 281.0, 597.0, 195.5],"true", 0) )
    # Connections for obj39 (graphObject_: Obj4) named s_
    self.drawConnections(
(self.obj39,self.obj75,[841.0, 281.0, 967.0, 195.5],"true", 0) )
    # Connections for obj35 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj35,self.obj41,[341.0, 181.0, 343.5, 361.0],"true", 2),
(self.obj35,self.obj42,[341.0, 181.0, 461.0, 231.0],"true", 2),
(self.obj35,self.obj43,[341.0, 181.0, 591.0, 231.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj36,self.obj44,[346.0, 541.0, 463.5, 501.0],"true", 2),
(self.obj36,self.obj45,[346.0, 541.0, 593.5, 501.0],"true", 2) )
    # Connections for obj38 (graphObject_: Obj3) named s_
    self.drawConnections(
(self.obj38,self.obj47,[581.0, 461.0, 711.0, 461.0],"true", 2),
(self.obj38,self.obj48,[581.0, 461.0, 581.0, 371.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj5) named s_
    self.drawConnections(
(self.obj40,self.obj49,[841.0, 461.0, 841.0, 371.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj15) named name
    self.drawConnections(
 )
    # Connections for obj64 (graphObject_: Obj21) named name
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj17) of type Equation
    self.drawConnections(
(self.obj56,self.obj62,[759.0, 62.0, 686.0, 86.0],"true", 2),
(self.obj56,self.obj63,[759.0, 62.0, 827.0, 90.5],"true", 2) )
    # Connections for obj67 (graphObject_: Obj22) of type Equation
    self.drawConnections(
(self.obj67,self.obj73,[1239.0, 62.0, 1166.0, 86.0],"true", 2),
(self.obj67,self.obj74,[1239.0, 62.0, 1317.0, 90.5],"true", 2) )
    # Connections for obj57 (graphObject_: Obj18) of type Constant
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj23) of type Constant
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj7) of type match_contains
    self.drawConnections(
(self.obj42,self.obj37,[461.0, 231.0, 581.0, 281.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj8) of type match_contains
    self.drawConnections(
(self.obj43,self.obj39,[591.0, 231.0, 841.0, 281.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj9) of type apply_contains
    self.drawConnections(
(self.obj44,self.obj38,[463.5, 501.0, 581.0, 461.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj10) of type apply_contains
    self.drawConnections(
(self.obj45,self.obj40,[593.5, 501.0, 841.0, 461.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj13) of type backward_link
    self.drawConnections(
(self.obj48,self.obj37,[581.0, 371.0, 581.0, 281.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj14) of type backward_link
    self.drawConnections(
(self.obj49,self.obj39,[841.0, 371.0, 841.0, 281.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj11) of type indirectLink_S
    self.drawConnections(
(self.obj46,self.obj39,[711.0, 281.0, 841.0, 281.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj12) of type directLink_T
    self.drawConnections(
(self.obj47,self.obj40,[711.0, 461.0, 841.0, 461.0],"true", 2) )
    # Connections for obj41 (graphObject_: Obj6) of type paired_with
    self.drawConnections(
(self.obj41,self.obj36,[343.5, 361.0, 346.0, 541.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj16) of type hasAttr_S
    self.drawConnections(
(self.obj55,self.obj50,[597.0, 195.5, 613.0, 110.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj26) of type hasAttr_S
    self.drawConnections(
(self.obj75,self.obj64,[967.0, 195.5, 1093.0, 110.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj19) of type leftExpr
    self.drawConnections(
(self.obj62,self.obj50,[686.0, 86.0, 613.0, 110.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj24) of type leftExpr
    self.drawConnections(
(self.obj73,self.obj64,[1166.0, 86.0, 1093.0, 110.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj20) of type rightExpr
    self.drawConnections(
(self.obj63,self.obj57,[827.0, 90.5, 895.0, 119.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj25) of type rightExpr
    self.drawConnections(
(self.obj74,self.obj68,[1317.0, 90.5, 1395.0, 119.0],"true", 2) )

newfunction = SM2SM_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
