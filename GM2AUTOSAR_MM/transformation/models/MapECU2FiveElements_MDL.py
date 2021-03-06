"""
__MapECU2FiveElements_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Sep  9 15:50:46 2013
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ECU import *
from VirtualDevice import *
from Distributable import *
from System import *
from SystemMapping import *
from SoftwareComposition import *
from CompositionType import *
from EcuInstance import *
from paired_with import *
from match_contains import *
from directLink_S import *
from directLink_T import *
from apply_contains import *
from graph_EcuInstance import *
from graph_ECU import *
from graph_SoftwareComposition import *
from graph_match_contains import *
from graph_Distributable import *
from graph_SystemMapping import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_ApplyModel import *
from graph_apply_contains import *
from graph_CompositionType import *
from graph_paired_with import *
from graph_MatchModel import *
from graph_System import *
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

def MapECU2FiveElements_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('MapECU2FiveElements')
    # --- ASG attributes over ---


    self.obj44=MatchModel(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    self.obj44.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,220.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=ApplyModel(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    self.obj45.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,480.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=ECU(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # classtype
    self.obj46.classtype.setValue('ECU')

    # cardinality
    self.obj46.cardinality.setValue('+')

    # name
    self.obj46.name.setValue('ecu1')

    self.obj46.graphClass_= graph_ECU
    if self.genGraphics:
       new_obj = graph_ECU(200.0,320.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=VirtualDevice(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # classtype
    self.obj47.classtype.setValue('VirtualDevice')

    # cardinality
    self.obj47.cardinality.setValue('1')

    # name
    self.obj47.name.setValue('vd1')

    self.obj47.graphClass_= graph_VirtualDevice
    if self.genGraphics:
       new_obj = graph_VirtualDevice(400.0,320.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Distributable(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # classtype
    self.obj48.classtype.setValue('Distributable')

    # cardinality
    self.obj48.cardinality.setValue('1')

    # name
    self.obj48.name.setValue('dist1')

    self.obj48.graphClass_= graph_Distributable
    if self.genGraphics:
       new_obj = graph_Distributable(600.0,320.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=System(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # classtype
    self.obj49.classtype.setValue('System')

    # cardinality
    self.obj49.cardinality.setValue('1')

    # name
    self.obj49.name.setValue('sys1')

    self.obj49.graphClass_= graph_System
    if self.genGraphics:
       new_obj = graph_System(200.0,540.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=SystemMapping(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # classtype
    self.obj50.classtype.setValue('SystemMapping')

    # cardinality
    self.obj50.cardinality.setValue('1')

    # name
    self.obj50.name.setValue('sysmap1')

    self.obj50.graphClass_= graph_SystemMapping
    if self.genGraphics:
       new_obj = graph_SystemMapping(491.0,640.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SystemMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=SoftwareComposition(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # classtype
    self.obj51.classtype.setValue('SoftwareComposition')

    # cardinality
    self.obj51.cardinality.setValue('1')

    # name
    self.obj51.name.setValue('swcompos1')

    self.obj51.graphClass_= graph_SoftwareComposition
    if self.genGraphics:
       new_obj = graph_SoftwareComposition(400.0,540.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=CompositionType(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # classtype
    self.obj52.classtype.setValue('CompositionType')

    # cardinality
    self.obj52.cardinality.setValue('1')

    # name
    self.obj52.name.setValue('composty1')

    self.obj52.graphClass_= graph_CompositionType
    if self.genGraphics:
       new_obj = graph_CompositionType(600.0,540.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=EcuInstance(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # classtype
    self.obj53.classtype.setValue('EcuInstance')

    # cardinality
    self.obj53.cardinality.setValue('1')

    # name
    self.obj53.name.setValue('ecuinst1')

    self.obj53.graphClass_= graph_EcuInstance
    if self.genGraphics:
       new_obj = graph_EcuInstance(320.0,640.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("EcuInstance", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=paired_with(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    self.obj54.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(157.0,394.5,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
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
       new_obj = graph_match_contains(247.5,313.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=match_contains(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(347.5,313.5,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=match_contains(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(447.5,313.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
    self.obj58.associationType.setValue('virtualDevice')

    self.obj58.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(442.0,364.0,self.obj58)
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
    self.obj59.associationType.setValue('distributable')

    self.obj59.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(642.0,364.0,self.obj59)
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
    self.obj60.associationType.setValue('softwareComposition')

    self.obj60.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.5,582.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
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
    self.obj61.associationType.setValue('softwareComposition')

    self.obj61.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(642.5,582.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=directLink_T(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # associationType
    self.obj62.associationType.setValue('mapping')

    self.obj62.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(478.0,635.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=apply_contains(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    self.obj63.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(260.5,554.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=apply_contains(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    self.obj64.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(353.0,554.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=apply_contains(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    self.obj65.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(450.5,554.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=apply_contains(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    self.obj66.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(310.5,604.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=apply_contains(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    self.obj67.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(413.5,627.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj44,self.obj54,[153.0, 263.0, 157.0, 394.5],"true", 2),
(self.obj44,self.obj55,[153.0, 263.0, 247.5, 313.5],"true", 2),
(self.obj44,self.obj56,[153.0, 263.0, 347.5, 313.5],"true", 2),
(self.obj44,self.obj57,[153.0, 263.0, 447.5, 313.5],"true", 2) )
    # Connections for obj45 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj45,self.obj63,[161.0, 526.0, 260.5, 554.0],"true", 2),
(self.obj45,self.obj64,[161.0, 526.0, 353.0, 554.0],"true", 2),
(self.obj45,self.obj65,[161.0, 526.0, 450.5, 554.0],"true", 2),
(self.obj45,self.obj66,[161.0, 526.0, 310.5, 604.0],"true", 2),
(self.obj45,self.obj67,[161.0, 526.0, 413.5, 627.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj2) named ecu1
    self.drawConnections(
(self.obj46,self.obj58,[342.0, 364.0, 442.0, 364.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj3) named vd1
    self.drawConnections(
(self.obj47,self.obj59,[542.0, 364.0, 642.0, 364.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj4) named dist1
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj5) named sys1
    self.drawConnections(
(self.obj49,self.obj60,[340.0, 582.0, 452.5, 582.0],"true", 2),
(self.obj49,self.obj62,[340.0, 582.0, 478.0, 635.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj6) named sysmap1
    self.drawConnections(
 )
    # Connections for obj51 (graphObject_: Obj7) named swcompos1
    self.drawConnections(
(self.obj51,self.obj61,[545.0, 582.0, 642.5, 582.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj8) named composty1
    self.drawConnections(
 )
    # Connections for obj53 (graphObject_: Obj9) named ecuinst1
    self.drawConnections(
 )
    # Connections for obj54 (graphObject_: Obj10) of type paired_with
    self.drawConnections(
(self.obj54,self.obj45,[157.0, 394.5, 161.0, 526.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj11) of type match_contains
    self.drawConnections(
(self.obj55,self.obj46,[247.5, 313.5, 342.0, 364.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj12) of type match_contains
    self.drawConnections(
(self.obj56,self.obj47,[347.5, 313.5, 542.0, 364.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj13) of type match_contains
    self.drawConnections(
(self.obj57,self.obj48,[447.5, 313.5, 742.0, 364.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj14) of type directLink_S
    self.drawConnections(
(self.obj58,self.obj47,[442.0, 364.0, 542.0, 364.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj15) of type directLink_S
    self.drawConnections(
(self.obj59,self.obj48,[642.0, 364.0, 742.0, 364.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj16) of type directLink_T
    self.drawConnections(
(self.obj60,self.obj51,[452.5, 582.0, 545.0, 582.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj17) of type directLink_T
    self.drawConnections(
(self.obj61,self.obj52,[642.5, 582.0, 740.0, 582.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj18) of type directLink_T
    self.drawConnections(
(self.obj62,self.obj50,[476.0, 627.0, 631.0, 682.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj19) of type apply_contains
    self.drawConnections(
(self.obj63,self.obj49,[260.5, 554.0, 340.0, 582.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj20) of type apply_contains
    self.drawConnections(
(self.obj64,self.obj51,[353.0, 554.0, 545.0, 582.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj21) of type apply_contains
    self.drawConnections(
(self.obj65,self.obj52,[450.5, 554.0, 740.0, 582.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj22) of type apply_contains
    self.drawConnections(
(self.obj66,self.obj53,[310.5, 604.0, 460.0, 682.0],"true", 2) )
    # Connections for obj67 (graphObject_: Obj23) of type apply_contains
    self.drawConnections(
(self.obj67,self.obj50,[413.5, 627.0, 631.0, 682.0],"true", 2) )

newfunction = MapECU2FiveElements_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
