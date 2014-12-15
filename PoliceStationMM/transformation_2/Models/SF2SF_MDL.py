"""
__SF2SF_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 09:32:42 2014
___________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Station_S import *
from Female_S import *
from MatchModel import *
from ApplyModel import *
from Station_T import *
from Female_T import *
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
from graph_Female_T import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_Station_T import *
from graph_Station_S import *
from graph_paired_with import *
from graph_leftExpr import *
from graph_Female_S import *
from graph_ApplyModel import *
from graph_Constant import *
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

def SF2SF_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('SF2SF')
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

    self.obj50=Female_S(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # classtype
    self.obj50.classtype.setValue('1')

    # cardinality
    self.obj50.cardinality.setValue('s_')

    # name
    self.obj50.name.setValue('s_')

    self.obj50.graphClass_= graph_Female_S
    if self.genGraphics:
       new_obj = graph_Female_S(760.0,240.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

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

    self.obj51=Female_T(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # classtype
    self.obj51.classtype.setValue('t_')

    # name
    self.obj51.name.setValue('s_')

    self.obj51.graphClass_= graph_Female_T
    if self.genGraphics:
       new_obj = graph_Female_T(760.0,420.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj57=Attribute(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # name
    self.obj57.name.setValue('name')

    self.obj57.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(600.0,100.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj67=Attribute(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # name
    self.obj67.name.setValue('name')

    self.obj67.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1100.0,100.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj60=Equation(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(760.0,20.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj71=Equation(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    self.obj71.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1240.0,20.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj61=Constant(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # value
    self.obj61.value.setValue('somestation')

    self.obj61.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(900.0,100.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj72=Constant(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # value
    self.obj72.value.setValue('otherfemale')

    self.obj72.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1340.0,100.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj41=match_contains(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(461.0,231.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj55=match_contains(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(581.0,231.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj43=apply_contains(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    self.obj43.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(463.5,501.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj56=apply_contains(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(583.5,501.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj45=backward_link(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    self.obj45.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(581.0,371.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj52=backward_link(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    self.obj52.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(821.0,371.0,self.obj52)
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
       new_obj = graph_indirectLink_S(701.0,281.0,self.obj53)
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
       new_obj = graph_directLink_T(701.0,461.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj49=paired_with(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(343.5,361.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj64=hasAttr_S(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    self.obj64.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(617.0,205.5,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj70=hasAttr_S(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    self.obj70.graphClass_= graph_hasAttr_S
    if self.genGraphics:
       new_obj = graph_hasAttr_S(987.0,205.5,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj65=leftExpr(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    self.obj65.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(726.0,96.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj75=leftExpr(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    self.obj75.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1216.0,96.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj66=rightExpr(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    self.obj66.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(877.0,100.5,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj76=rightExpr(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    self.obj76.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1337.0,100.5,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    # Connections for obj35 (graphObject_: Obj0) named s_
    self.drawConnections(
(self.obj35,self.obj53,[581.0, 281.0, 701.0, 281.0],"true", 0),
(self.obj35,self.obj64,[581.0, 281.0, 617.0, 205.5],"true", 0) )
    # Connections for obj50 (graphObject_: Obj15) named s_
    self.drawConnections(
(self.obj50,self.obj70,[821.0, 281.0, 987.0, 205.5],"true", 0) )
    # Connections for obj37 (graphObject_: Obj2) of type MatchModel
    self.drawConnections(
(self.obj37,self.obj49,[341.0, 181.0, 343.5, 361.0],"true", 2),
(self.obj37,self.obj41,[341.0, 181.0, 461.0, 231.0],"true", 2),
(self.obj37,self.obj55,[341.0, 181.0, 581.0, 231.0],"true", 0) )
    # Connections for obj38 (graphObject_: Obj3) of type ApplyModel
    self.drawConnections(
(self.obj38,self.obj43,[346.0, 541.0, 463.5, 501.0],"true", 2),
(self.obj38,self.obj56,[346.0, 541.0, 583.5, 501.0],"true", 0) )
    # Connections for obj39 (graphObject_: Obj4) named s_
    self.drawConnections(
(self.obj39,self.obj45,[581.0, 461.0, 581.0, 371.0],"true", 2),
(self.obj39,self.obj54,[581.0, 461.0, 701.0, 461.0],"true", 0) )
    # Connections for obj51 (graphObject_: Obj16) named s_
    self.drawConnections(
(self.obj51,self.obj52,[821.0, 461.0, 821.0, 371.0],"true", 0) )
    # Connections for obj57 (graphObject_: Obj22) named name
    self.drawConnections(
 )
    # Connections for obj67 (graphObject_: Obj28) named name
    self.drawConnections(
 )
    # Connections for obj60 (graphObject_: Obj23) of type Equation
    self.drawConnections(
(self.obj60,self.obj65,[799.0, 62.0, 726.0, 96.0],"true", 2),
(self.obj60,self.obj66,[799.0, 62.0, 877.0, 100.5],"true", 2) )
    # Connections for obj71 (graphObject_: Obj30) of type Equation
    self.drawConnections(
(self.obj71,self.obj75,[1279.0, 62.0, 1216.0, 96.0],"true", 2),
(self.obj71,self.obj76,[1279.0, 62.0, 1337.0, 100.5],"true", 2) )
    # Connections for obj61 (graphObject_: Obj24) of type Constant
    self.drawConnections(
 )
    # Connections for obj72 (graphObject_: Obj31) of type Constant
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj6) of type match_contains
    self.drawConnections(
(self.obj41,self.obj35,[461.0, 231.0, 581.0, 281.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj20) of type match_contains
    self.drawConnections(
(self.obj55,self.obj50,[581.0, 231.0, 821.0, 281.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj8) of type apply_contains
    self.drawConnections(
(self.obj43,self.obj39,[463.5, 501.0, 581.0, 461.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj21) of type apply_contains
    self.drawConnections(
(self.obj56,self.obj51,[583.5, 501.0, 821.0, 461.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj10) of type backward_link
    self.drawConnections(
(self.obj45,self.obj35,[581.0, 371.0, 581.0, 281.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj17) of type backward_link
    self.drawConnections(
(self.obj52,self.obj50,[821.0, 371.0, 821.0, 281.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj18) of type indirectLink_S
    self.drawConnections(
(self.obj53,self.obj50,[701.0, 281.0, 821.0, 281.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj19) of type directLink_T
    self.drawConnections(
(self.obj54,self.obj51,[701.0, 461.0, 821.0, 461.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj14) of type paired_with
    self.drawConnections(
(self.obj49,self.obj38,[343.5, 361.0, 346.0, 541.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj25) of type hasAttr_S
    self.drawConnections(
(self.obj64,self.obj57,[617.0, 205.5, 653.0, 130.0],"true", 2) )
    # Connections for obj70 (graphObject_: Obj29) of type hasAttr_S
    self.drawConnections(
(self.obj70,self.obj67,[987.0, 205.5, 1153.0, 130.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj26) of type leftExpr
    self.drawConnections(
(self.obj65,self.obj57,[726.0, 96.0, 653.0, 130.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj32) of type leftExpr
    self.drawConnections(
(self.obj75,self.obj67,[1216.0, 96.0, 1153.0, 130.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj27) of type rightExpr
    self.drawConnections(
(self.obj66,self.obj61,[877.0, 100.5, 955.0, 139.0],"true", 2) )
    # Connections for obj76 (graphObject_: Obj33) of type rightExpr
    self.drawConnections(
(self.obj76,self.obj72,[1337.0, 100.5, 1395.0, 139.0],"true", 2) )

newfunction = SF2SF_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
