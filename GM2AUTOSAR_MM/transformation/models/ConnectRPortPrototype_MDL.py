"""
__ConnectRPortPrototype_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Aug 23 15:48:12 2013
___________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ECU import *
from VirtualDevice import *
from Distributable import *
from ExecFrame import *
from Signal import *
from CompositionType import *
from RPortPrototype import *
from paired_with import *
from match_contains import *
from directLink_S import *
from directLink_T import *
from apply_contains import *
from backward_link import *
from graph_ECU import *
from graph_match_contains import *
from graph_Distributable import *
from graph_backward_link import *
from graph_RPortPrototype import *
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

def ConnectRPortPrototype_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('ConnectRPortPrototype')
    # --- ASG attributes over ---


    self.obj41=MatchModel(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(40.0,660.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=ApplyModel(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    self.obj42.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(40.0,920.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=ECU(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # classtype
    self.obj43.classtype.setValue('ECU')

    # cardinality
    self.obj43.cardinality.setValue('+')

    # name
    self.obj43.name.setValue('ecu1')

    self.obj43.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(200.0,760.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=VirtualDevice(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # classtype
    self.obj44.classtype.setValue('VirtualDevice')

    # cardinality
    self.obj44.cardinality.setValue('+')

    # name
    self.obj44.name.setValue('vd1')

    self.obj44.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(380.0,760.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Distributable(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # classtype
    self.obj45.classtype.setValue('Distributable')

    # cardinality
    self.obj45.cardinality.setValue('+')

    # name
    self.obj45.name.setValue('dist1')

    self.obj45.graphClass_= graph_Distributable
    if self.genGraphics:
       new_obj = graph_Distributable(560.0,760.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=ExecFrame(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # classtype
    self.obj46.classtype.setValue('ExecFrame')

    # cardinality
    self.obj46.cardinality.setValue('+')

    # name
    self.obj46.name.setValue('ef1')

    self.obj46.graphClass_= graph_ExecFrame
    if self.genGraphics:
       new_obj = graph_ExecFrame(720.0,760.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=Signal(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # classtype
    self.obj47.classtype.setValue('Signal')

    # cardinality
    self.obj47.cardinality.setValue('1')

    # name
    self.obj47.name.setValue('sig1')

    self.obj47.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(880.0,760.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=CompositionType(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # classtype
    self.obj48.classtype.setValue('CompositionType')

    # cardinality
    self.obj48.cardinality.setValue('1')

    # name
    self.obj48.name.setValue('composty1')

    self.obj48.graphClass_= graph_CompositionType
    if self.genGraphics:
       new_obj = graph_CompositionType(260.0,1040.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=RPortPrototype(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # classtype
    self.obj49.classtype.setValue('RPortPrototype')

    # cardinality
    self.obj49.cardinality.setValue('1')

    # name
    self.obj49.name.setValue('rport1')

    self.obj49.graphClass_= graph_RPortPrototype
    if self.genGraphics:
       new_obj = graph_RPortPrototype(720.0,1040.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RPortPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=paired_with(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(177.0,834.5,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=match_contains(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    self.obj51.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(257.5,753.5,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=match_contains(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    self.obj52.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(347.5,753.5,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=match_contains(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    self.obj53.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(437.5,753.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
       new_obj = graph_match_contains(517.5,753.5,self.obj54)
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
       new_obj = graph_match_contains(597.5,753.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=directLink_S(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # associationType
    self.obj56.associationType.setValue('virtualDevice')

    self.obj56.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(432.0,804.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=directLink_S(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # associationType
    self.obj57.associationType.setValue('distributable')

    self.obj57.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(612.0,804.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=directLink_S(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # associationType
    self.obj58.associationType.setValue('execFrame')

    self.obj58.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(782.0,804.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=directLink_S(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # associationType
    self.obj59.associationType.setValue('required')

    self.obj59.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(942.0,803.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=directLink_T(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # associationType
    self.obj60.associationType.setValue('port')

    self.obj60.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(630.0,1082.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=apply_contains(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    self.obj61.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(290.5,1024.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=apply_contains(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    self.obj62.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(520.5,1024.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=backward_link(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # type
    self.obj63.type.setValue('ruleDef')

    self.obj63.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(371.0,943.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    # Connections for obj41 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj41,self.obj50,[173.0, 703.0, 177.0, 834.5],"true", 2),
(self.obj41,self.obj51,[173.0, 703.0, 257.5, 753.5],"true", 2),
(self.obj41,self.obj52,[173.0, 703.0, 347.5, 753.5],"true", 2),
(self.obj41,self.obj53,[173.0, 703.0, 437.5, 753.5],"true", 2),
(self.obj41,self.obj54,[173.0, 703.0, 517.5, 753.5],"true", 2),
(self.obj41,self.obj55,[173.0, 703.0, 597.5, 753.5],"true", 2) )
    # Connections for obj42 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj42,self.obj61,[181.0, 966.0, 290.5, 1024.0],"true", 2),
(self.obj42,self.obj62,[181.0, 966.0, 520.5, 1024.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj2) named ecu1
    self.drawConnections(
(self.obj43,self.obj56,[342.0, 804.0, 432.0, 804.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj3) named vd1
    self.drawConnections(
(self.obj44,self.obj57,[522.0, 804.0, 612.0, 804.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj4) named dist1
    self.drawConnections(
(self.obj45,self.obj58,[702.0, 804.0, 782.0, 804.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj5) named ef1
    self.drawConnections(
(self.obj46,self.obj59,[862.0, 804.0, 942.0, 803.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj6) named sig1
    self.drawConnections(
 )
    # Connections for obj48 (graphObject_: Obj7) named composty1
    self.drawConnections(
(self.obj48,self.obj60,[400.0, 1082.0, 630.0, 1082.0],"true", 2),
(self.obj48,self.obj63,[400.0, 1082.0, 371.0, 943.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj8) named rport1
    self.drawConnections(
 )
    # Connections for obj50 (graphObject_: Obj9) of type paired_with
    self.drawConnections(
(self.obj50,self.obj42,[177.0, 834.5, 181.0, 966.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj10) of type match_contains
    self.drawConnections(
(self.obj51,self.obj43,[257.5, 753.5, 342.0, 804.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj11) of type match_contains
    self.drawConnections(
(self.obj52,self.obj44,[347.5, 753.5, 522.0, 804.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj12) of type match_contains
    self.drawConnections(
(self.obj53,self.obj45,[437.5, 753.5, 702.0, 804.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj13) of type match_contains
    self.drawConnections(
(self.obj54,self.obj46,[517.5, 753.5, 862.0, 804.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj14) of type match_contains
    self.drawConnections(
(self.obj55,self.obj47,[597.5, 753.5, 1022.0, 804.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj15) of type directLink_S
    self.drawConnections(
(self.obj56,self.obj44,[432.0, 804.0, 522.0, 804.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj16) of type directLink_S
    self.drawConnections(
(self.obj57,self.obj45,[612.0, 804.0, 702.0, 804.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj17) of type directLink_S
    self.drawConnections(
(self.obj58,self.obj46,[782.0, 804.0, 862.0, 804.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj18) of type directLink_S
    self.drawConnections(
(self.obj59,self.obj47,[942.0, 803.0, 1022.0, 804.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj19) of type directLink_T
    self.drawConnections(
(self.obj60,self.obj49,[630.0, 1082.0, 860.0, 1082.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj20) of type apply_contains
    self.drawConnections(
(self.obj61,self.obj48,[290.5, 1024.0, 400.0, 1082.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj21) of type apply_contains
    self.drawConnections(
(self.obj62,self.obj49,[520.5, 1024.0, 860.0, 1082.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj22) of type backward_link
    self.drawConnections(
(self.obj63,self.obj43,[371.0, 943.0, 342.0, 804.0],"true", 2) )

newfunction = ConnectRPortPrototype_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
