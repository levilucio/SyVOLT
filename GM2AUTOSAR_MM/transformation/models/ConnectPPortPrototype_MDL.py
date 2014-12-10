"""
__ConnectPPortPrototype_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 16 22:24:37 2013
___________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from directLink_S import *
from apply_contains import *
from Distributable import *
from paired_with import *
from PPortPrototype import *
from backward_link import *
from directLink_T import *
from ApplyModel import *
from CompositionType import *
from ECU import *
from VirtualDevice import *
from ExecFrame import *
from Signal import *
from match_contains import *
from MatchModel import *
from graph_ECU import *
from graph_PPortPrototype import *
from graph_match_contains import *
from graph_Distributable import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_ExecFrame import *
from graph_CompositionType import *
from graph_Signal import *
from graph_paired_with import *
from graph_ApplyModel import *
from graph_VirtualDevice import *
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

def ConnectPPortPrototype_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('ConnectPPortPrototype')
    # --- ASG attributes over ---


    self.obj67=directLink_S(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # associationType
    self.obj67.associationType.setValue('virtualDevice')

    self.obj67.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(422.0,804.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=directLink_S(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # associationType
    self.obj68.associationType.setValue('distributable')

    self.obj68.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(592.0,804.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=directLink_S(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # associationType
    self.obj69.associationType.setValue('execFrame')

    self.obj69.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(772.0,804.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=directLink_S(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # associationType
    self.obj70.associationType.setValue('provided')

    self.obj70.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(953.0,804.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=apply_contains(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    self.obj71.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(250.5,1034.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=apply_contains(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    self.obj72.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(480.5,1034.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=Distributable(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # classtype
    self.obj73.classtype.setValue('Distributable')

    # cardinality
    self.obj73.cardinality.setValue('+')

    # name
    self.obj73.name.setValue('dist1')

    self.obj73.graphClass_= graph_Distributable
    if self.genGraphics:
       new_obj = graph_Distributable(540.0,760.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=paired_with(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    self.obj74.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(157.0,844.5,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=PPortPrototype(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # classtype
    self.obj75.classtype.setValue('PPortPrototype')

    # cardinality
    self.obj75.cardinality.setValue('1')

    # name
    self.obj75.name.setValue('pport1')

    self.obj75.graphClass_= graph_PPortPrototype
    if self.genGraphics:
       new_obj = graph_PPortPrototype(660.0,1040.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("PPortPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=backward_link(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # type
    self.obj76.type.setValue('ruleDef')

    self.obj76.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,943.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=directLink_T(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # associationType
    self.obj77.associationType.setValue('port')

    self.obj77.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(570.0,1082.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=ApplyModel(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    self.obj78.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,940.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=CompositionType(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # classtype
    self.obj79.classtype.setValue('CompositionType')

    # cardinality
    self.obj79.cardinality.setValue('1')

    # name
    self.obj79.name.setValue('composty1')

    self.obj79.graphClass_= graph_CompositionType
    if self.genGraphics:
       new_obj = graph_CompositionType(200.0,1040.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=ECU(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # classtype
    self.obj80.classtype.setValue('ECU')

    # cardinality
    self.obj80.cardinality.setValue('+')

    # name
    self.obj80.name.setValue('ecu1')

    self.obj80.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(200.0,760.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=VirtualDevice(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # classtype
    self.obj81.classtype.setValue('VirtualDevice')

    # cardinality
    self.obj81.cardinality.setValue('+')

    # name
    self.obj81.name.setValue('vd1')

    self.obj81.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(360.0,760.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=ExecFrame(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # classtype
    self.obj82.classtype.setValue('ExecFrame')

    # cardinality
    self.obj82.cardinality.setValue('+')

    # name
    self.obj82.name.setValue('ef1')

    self.obj82.graphClass_= graph_ExecFrame
    if self.genGraphics:
       new_obj = graph_ExecFrame(720.0,760.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=Signal(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # classtype
    self.obj83.classtype.setValue('Signal')

    # cardinality
    self.obj83.cardinality.setValue('1')

    # name
    self.obj83.name.setValue('s1')

    self.obj83.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(900.0,760.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=match_contains(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    self.obj84.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(247.5,753.5,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=match_contains(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    self.obj85.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(337.5,753.5,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=match_contains(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    self.obj86.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(427.5,753.5,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=match_contains(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    self.obj87.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(517.5,753.5,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=match_contains(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    self.obj88.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(607.5,753.5,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=MatchModel(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    self.obj89.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,660.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    # Connections for obj67 (graphObject_: Obj23) of type directLink_S
    self.drawConnections(
(self.obj67,self.obj81,[422.0, 804.0, 502.0, 804.0],"true", 2) )
    # Connections for obj68 (graphObject_: Obj24) of type directLink_S
    self.drawConnections(
(self.obj68,self.obj73,[592.0, 804.0, 682.0, 804.0],"true", 2) )
    # Connections for obj69 (graphObject_: Obj25) of type directLink_S
    self.drawConnections(
(self.obj69,self.obj82,[772.0, 804.0, 862.0, 804.0],"true", 2) )
    # Connections for obj70 (graphObject_: Obj26) of type directLink_S
    self.drawConnections(
(self.obj70,self.obj83,[953.0, 804.0, 1042.0, 804.0],"true", 2) )
    # Connections for obj71 (graphObject_: Obj27) of type apply_contains
    self.drawConnections(
(self.obj71,self.obj79,[250.5, 1034.0, 340.0, 1082.0],"true", 2) )
    # Connections for obj72 (graphObject_: Obj28) of type apply_contains
    self.drawConnections(
(self.obj72,self.obj75,[480.5, 1034.0, 800.0, 1082.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj29) named dist1
    self.drawConnections(
(self.obj73,self.obj69,[682.0, 804.0, 772.0, 804.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj30) of type paired_with
    self.drawConnections(
(self.obj74,self.obj78,[157.0, 844.5, 161.0, 986.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj31) named pport1
    self.drawConnections(
 )
    # Connections for obj76 (graphObject_: Obj32) of type backward_link
    self.drawConnections(
(self.obj76,self.obj80,[341.0, 943.0, 342.0, 804.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj33) of type directLink_T
    self.drawConnections(
(self.obj77,self.obj75,[570.0, 1082.0, 800.0, 1082.0],"true", 2) )
    # Connections for obj78 (graphObject_: Obj34) of type ApplyModel
    self.drawConnections(
(self.obj78,self.obj71,[161.0, 986.0, 250.5, 1034.0],"true", 2),
(self.obj78,self.obj72,[161.0, 986.0, 480.5, 1034.0],"true", 2) )
    # Connections for obj79 (graphObject_: Obj35) named composty1
    self.drawConnections(
(self.obj79,self.obj77,[340.0, 1082.0, 570.0, 1082.0],"true", 2),
(self.obj79,self.obj76,[340.0, 1082.0, 341.0, 943.0],"true", 2) )
    # Connections for obj80 (graphObject_: Obj36) named ecu1
    self.drawConnections(
(self.obj80,self.obj67,[342.0, 804.0, 422.0, 804.0],"true", 2) )
    # Connections for obj81 (graphObject_: Obj37) named vd1
    self.drawConnections(
(self.obj81,self.obj68,[502.0, 804.0, 592.0, 804.0],"true", 2) )
    # Connections for obj82 (graphObject_: Obj38) named ef1
    self.drawConnections(
(self.obj82,self.obj70,[862.0, 804.0, 953.0, 804.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj39) named s1
    self.drawConnections(
 )
    # Connections for obj84 (graphObject_: Obj40) of type match_contains
    self.drawConnections(
(self.obj84,self.obj80,[247.5, 753.5, 342.0, 804.0],"true", 2) )
    # Connections for obj85 (graphObject_: Obj41) of type match_contains
    self.drawConnections(
(self.obj85,self.obj81,[337.5, 753.5, 502.0, 804.0],"true", 2) )
    # Connections for obj86 (graphObject_: Obj42) of type match_contains
    self.drawConnections(
(self.obj86,self.obj73,[427.5, 753.5, 682.0, 804.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj43) of type match_contains
    self.drawConnections(
(self.obj87,self.obj82,[517.5, 753.5, 862.0, 804.0],"true", 2) )
    # Connections for obj88 (graphObject_: Obj44) of type match_contains
    self.drawConnections(
(self.obj88,self.obj83,[607.5, 753.5, 1042.0, 804.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj45) of type MatchModel
    self.drawConnections(
(self.obj89,self.obj74,[153.0, 703.0, 157.0, 844.5],"true", 2),
(self.obj89,self.obj84,[153.0, 703.0, 247.5, 753.5],"true", 2),
(self.obj89,self.obj85,[153.0, 703.0, 337.5, 753.5],"true", 2),
(self.obj89,self.obj86,[153.0, 703.0, 427.5, 753.5],"true", 2),
(self.obj89,self.obj87,[153.0, 703.0, 517.5, 753.5],"true", 2),
(self.obj89,self.obj88,[153.0, 703.0, 607.5, 753.5],"true", 2) )

newfunction = ConnectPPortPrototype_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
