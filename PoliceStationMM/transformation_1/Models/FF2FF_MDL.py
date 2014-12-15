"""
__FF2FF_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 09:44:58 2014
___________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Female_S import *
from MatchModel import *
from ApplyModel import *
from Female_T import *
from match_contains import *
from apply_contains import *
from backward_link import *
from indirectLink_S import *
from directLink_T import *
from paired_with import *
from graph_match_contains import *
from graph_backward_link import *
from graph_ApplyModel import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_paired_with import *
from graph_Female_S import *
from graph_Female_T import *
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

def FF2FF_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('FF2FF')
    # --- ASG attributes over ---


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
       new_obj = graph_Female_S(460.0,220.0,self.obj50)
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

    self.obj51=Female_S(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # classtype
    self.obj51.classtype.setValue('1')

    # cardinality
    self.obj51.cardinality.setValue('s_')

    # name
    self.obj51.name.setValue('s_')

    self.obj51.graphClass_= graph_Female_S
    if self.genGraphics:
       new_obj = graph_Female_S(720.0,220.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj37=MatchModel(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    self.obj37.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(220.0,140.0,self.obj37)
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
       new_obj = graph_ApplyModel(220.0,460.0,self.obj38)
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

    self.obj52=Female_T(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # classtype
    self.obj52.classtype.setValue('t_')

    # name
    self.obj52.name.setValue('s_')

    self.obj52.graphClass_= graph_Female_T
    if self.genGraphics:
       new_obj = graph_Female_T(460.0,400.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Female_T(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # classtype
    self.obj53.classtype.setValue('t_')

    # name
    self.obj53.name.setValue('s_')

    self.obj53.graphClass_= graph_Female_T
    if self.genGraphics:
       new_obj = graph_Female_T(720.0,400.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=match_contains(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    self.obj54.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(401.0,221.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=match_contains(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(531.0,221.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
       new_obj = graph_apply_contains(403.5,471.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=apply_contains(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(533.5,471.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=backward_link(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    self.obj58.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(521.0,351.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=backward_link(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    self.obj59.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(781.0,351.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=indirectLink_S(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_indirectLink_S
    if self.genGraphics:
       new_obj = graph_indirectLink_S(651.0,261.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=directLink_T(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # associationType
    self.obj61.associationType.setValue('t_')

    self.obj61.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(651.0,441.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj49=paired_with(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(283.5,341.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    # Connections for obj50 (graphObject_: Obj15) named s_
    self.drawConnections(
(self.obj50,self.obj60,[521.0, 261.0, 651.0, 261.0],"true", 0) )
    # Connections for obj51 (graphObject_: Obj16) named s_
    self.drawConnections(
 )
    # Connections for obj37 (graphObject_: Obj2) of type MatchModel
    self.drawConnections(
(self.obj37,self.obj49,[281.0, 181.0, 283.5, 341.0],"true", 2),
(self.obj37,self.obj54,[281.0, 181.0, 401.0, 221.0],"true", 0),
(self.obj37,self.obj55,[281.0, 181.0, 531.0, 221.0],"true", 0) )
    # Connections for obj38 (graphObject_: Obj3) of type ApplyModel
    self.drawConnections(
(self.obj38,self.obj56,[286.0, 501.0, 403.5, 471.0],"true", 0),
(self.obj38,self.obj57,[286.0, 501.0, 533.5, 471.0],"true", 0) )
    # Connections for obj52 (graphObject_: Obj17) named s_
    self.drawConnections(
(self.obj52,self.obj58,[521.0, 441.0, 521.0, 351.0],"true", 0),
(self.obj52,self.obj61,[521.0, 441.0, 651.0, 441.0],"true", 0) )
    # Connections for obj53 (graphObject_: Obj18) named s_
    self.drawConnections(
(self.obj53,self.obj59,[781.0, 441.0, 781.0, 351.0],"true", 0) )
    # Connections for obj54 (graphObject_: Obj19) of type match_contains
    self.drawConnections(
(self.obj54,self.obj50,[401.0, 221.0, 521.0, 261.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj20) of type match_contains
    self.drawConnections(
(self.obj55,self.obj51,[531.0, 221.0, 781.0, 261.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj21) of type apply_contains
    self.drawConnections(
(self.obj56,self.obj52,[403.5, 471.0, 521.0, 441.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj22) of type apply_contains
    self.drawConnections(
(self.obj57,self.obj53,[533.5, 471.0, 781.0, 441.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj23) of type backward_link
    self.drawConnections(
(self.obj58,self.obj50,[521.0, 351.0, 521.0, 261.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj24) of type backward_link
    self.drawConnections(
(self.obj59,self.obj51,[781.0, 351.0, 781.0, 261.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj25) of type indirectLink_S
    self.drawConnections(
(self.obj60,self.obj51,[651.0, 261.0, 781.0, 261.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj26) of type directLink_T
    self.drawConnections(
(self.obj61,self.obj53,[651.0, 441.0, 781.0, 441.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj14) of type paired_with
    self.drawConnections(
(self.obj49,self.obj38,[283.5, 341.0, 286.0, 501.0],"true", 2) )

newfunction = FF2FF_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
