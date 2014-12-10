"""
__example_model_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sun Dec  7 09:38:29 2014
___________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Station_S import *
from Male_S import *
from Female_S import *
from Station_T import *
from Male_T import *
from backward_link import *
from directLink_S import *
from graph_backward_link import *
from graph_directLink_S import *
from graph_Station_T import *
from graph_Station_S import *
from graph_Male_T import *
from graph_Female_S import *
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

def example_model_MDL(self, rootNode, PoliceStationMMRootNode=None):

    # --- Generating attributes code for ASG PoliceStationMM ---
    if( PoliceStationMMRootNode ): 
        # author
        PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        PoliceStationMMRootNode.description.setValue('\n')
        PoliceStationMMRootNode.description.setHeight(15)

        # name
        PoliceStationMMRootNode.name.setValue('example_model')
    # --- ASG attributes over ---


    self.obj30=Station_S(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # classtype
    self.obj30.classtype.setValue('1')

    # cardinality
    self.obj30.cardinality.setValue('s_')

    # name
    self.obj30.name.setValue('s_')

    self.obj30.graphClass_= graph_Station_S
    if self.genGraphics:
       new_obj = graph_Station_S(380.0,160.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Station_S", new_obj.tag)
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
    self.obj31.classtype.setValue('1')

    # cardinality
    self.obj31.cardinality.setValue('s_')

    # name
    self.obj31.name.setValue('s_')

    self.obj31.graphClass_= graph_Male_S
    if self.genGraphics:
       new_obj = graph_Male_S(620.0,160.0,self.obj31)
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

    self.obj32=Female_S(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # classtype
    self.obj32.classtype.setValue('1')

    # cardinality
    self.obj32.cardinality.setValue('s_')

    # name
    self.obj32.name.setValue('s_')

    self.obj32.graphClass_= graph_Female_S
    if self.genGraphics:
       new_obj = graph_Female_S(140.0,160.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=Station_T(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # classtype
    self.obj33.classtype.setValue('t_')

    # name
    self.obj33.name.setValue('s_')

    self.obj33.graphClass_= graph_Station_T
    if self.genGraphics:
       new_obj = graph_Station_T(380.0,360.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Station_T", new_obj.tag)
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
    self.obj34.classtype.setValue('t_')

    # name
    self.obj34.name.setValue('s_')

    self.obj34.graphClass_= graph_Male_T
    if self.genGraphics:
       new_obj = graph_Male_T(620.0,360.0,self.obj34)
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

    self.obj35=backward_link(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    self.obj35.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(441.0,301.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=backward_link(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    self.obj36.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(681.0,301.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=directLink_S(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # associationType
    self.obj37.associationType.setValue('t_')

    self.obj37.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(561.0,201.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    # Connections for obj30 (graphObject_: Obj0) named s_
    self.drawConnections(
(self.obj30,self.obj37,[441.0, 201.0, 561.0, 201.0],"true", 2) )
    # Connections for obj31 (graphObject_: Obj1) named s_
    self.drawConnections(
 )
    # Connections for obj32 (graphObject_: Obj2) named s_
    self.drawConnections(
 )
    # Connections for obj33 (graphObject_: Obj3) named s_
    self.drawConnections(
(self.obj33,self.obj35,[441.0, 401.0, 441.0, 301.0],"true", 2) )
    # Connections for obj34 (graphObject_: Obj4) named s_
    self.drawConnections(
(self.obj34,self.obj36,[681.0, 401.0, 681.0, 301.0],"true", 2) )
    # Connections for obj35 (graphObject_: Obj5) of type backward_link
    self.drawConnections(
(self.obj35,self.obj30,[441.0, 301.0, 441.0, 201.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj6) of type backward_link
    self.drawConnections(
(self.obj36,self.obj31,[681.0, 301.0, 681.0, 201.0],"true", 2) )
    # Connections for obj37 (graphObject_: Obj7) of type directLink_S
    self.drawConnections(
(self.obj37,self.obj31,[561.0, 201.0, 681.0, 201.0],"true", 2) )

newfunction = example_model_MDL

loadedMMName = 'PoliceStationMM_META'

atom3version = '0.3'
