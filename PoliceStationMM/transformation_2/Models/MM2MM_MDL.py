"""
__MM2MM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 09:38:32 2014
___________________________________________________________________
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
from graph_match_contains import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
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

def MM2MM_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('MM2MM')
    # --- ASG attributes over ---


    self.obj37=Male_S(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # classtype
    self.obj37.classtype.setValue('1')

    # cardinality
    self.obj37.cardinality.setValue('s_')

    # name
    self.obj37.name.setValue('s_')

    self.obj37.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(460.0,220.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj40=Male_S(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # classtype
    self.obj40.classtype.setValue('1')

    # cardinality
    self.obj40.cardinality.setValue('s_')

    # name
    self.obj40.name.setValue('s_')

    self.obj40.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(720.0,220.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj35=MatchModel(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    self.obj35.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(220.0,140.0,self.obj35)
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
       new_obj = graph_ApplyModel(220.0,460.0,self.obj36)
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

    self.obj42=Male_T(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # classtype
    self.obj42.classtype.setValue('t_')

    # name
    self.obj42.name.setValue('s_')

    self.obj42.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(460.0,400.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=Male_T(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # classtype
    self.obj43.classtype.setValue('t_')

    # name
    self.obj43.name.setValue('s_')

    self.obj43.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(720.0,400.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj39=match_contains(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    self.obj39.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(401.0,221.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj41=match_contains(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(531.0,221.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj44=apply_contains(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    self.obj44.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(403.5,471.0,self.obj44)
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
       new_obj = graph_apply_contains(533.5,471.0,self.obj45)
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
       new_obj = graph_backward_link(521.0,351.0,self.obj48)
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
       new_obj = graph_backward_link(781.0,351.0,self.obj49)
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
       new_obj = graph_indirectLink_S(651.0,261.0,self.obj46)
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
       new_obj = graph_directLink_T(651.0,441.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj50=paired_with(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(283.5,341.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    # Connections for obj37 (graphObject_: Obj2) named s_
    self.drawConnections(
(self.obj37,self.obj46,[521.0, 261.0, 651.0, 261.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj5) named s_
    self.drawConnections(
 )
    # Connections for obj35 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj35,self.obj39,[281.0, 181.0, 401.0, 221.0],"true", 2),
(self.obj35,self.obj41,[281.0, 181.0, 531.0, 221.0],"true", 2),
(self.obj35,self.obj50,[281.0, 181.0, 283.5, 341.0],"true", 0) )
    # Connections for obj36 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj36,self.obj44,[286.0, 501.0, 403.5, 471.0],"true", 2),
(self.obj36,self.obj45,[286.0, 501.0, 533.5, 471.0],"true", 2) )
    # Connections for obj42 (graphObject_: Obj7) named s_
    self.drawConnections(
(self.obj42,self.obj47,[521.0, 441.0, 651.0, 441.0],"true", 2),
(self.obj42,self.obj48,[521.0, 441.0, 521.0, 351.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj8) named s_
    self.drawConnections(
(self.obj43,self.obj49,[781.0, 441.0, 781.0, 351.0],"true", 2) )
    # Connections for obj39 (graphObject_: Obj4) of type match_contains
    self.drawConnections(
(self.obj39,self.obj37,[401.0, 221.0, 521.0, 261.0],"true", 2) )
    # Connections for obj41 (graphObject_: Obj6) of type match_contains
    self.drawConnections(
(self.obj41,self.obj40,[531.0, 221.0, 781.0, 261.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj9) of type apply_contains
    self.drawConnections(
(self.obj44,self.obj42,[403.5, 471.0, 521.0, 441.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj10) of type apply_contains
    self.drawConnections(
(self.obj45,self.obj43,[533.5, 471.0, 781.0, 441.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj13) of type backward_link
    self.drawConnections(
(self.obj48,self.obj37,[521.0, 351.0, 521.0, 261.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj14) of type backward_link
    self.drawConnections(
(self.obj49,self.obj40,[781.0, 351.0, 781.0, 261.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj11) of type indirectLink_S
    self.drawConnections(
(self.obj46,self.obj40,[651.0, 261.0, 781.0, 261.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj12) of type directLink_T
    self.drawConnections(
(self.obj47,self.obj43,[651.0, 441.0, 781.0, 441.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj15) of type paired_with
    self.drawConnections(
(self.obj50,self.obj36,[283.5, 341.0, 286.0, 501.0],"true", 2) )

newfunction = MM2MM_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
