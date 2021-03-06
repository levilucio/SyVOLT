"""
__ConnVirtualDeviceToDistributable_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Aug 23 11:33:33 2013
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ECU import *
from VirtualDevice import *
from Distributable import *
from CompositionType import *
from ComponentPrototype import *
from SwcToEcuMapping import *
from SwCompToEcuMapping_component import *
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
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_SwCompToEcuMapping_component import *
from graph_CompositionType import *
from graph_paired_with import *
from graph_ApplyModel import *
from graph_VirtualDevice import *
from graph_ComponentPrototype import *
from graph_SwcToEcuMapping import *
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

def ConnVirtualDeviceToDistributable_MDL(self, rootNode, GM2AUTOSAR_MMRootNode=None):

    # --- Generating attributes code for ASG GM2AUTOSAR_MM ---
    if( GM2AUTOSAR_MMRootNode ): 
        # author
        GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        GM2AUTOSAR_MMRootNode.description.setValue('\n')
        GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        GM2AUTOSAR_MMRootNode.name.setValue('ConnVirtualDeviceToDistributable')
    # --- ASG attributes over ---


    self.obj41=MatchModel(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,620.0,self.obj41)
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
       new_obj = graph_ApplyModel(20.0,900.0,self.obj42)
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
       new_obj = graph_ECU(260.0,720.0,self.obj43)
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
       new_obj = graph_VirtualDevice(480.0,720.0,self.obj44)
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
       new_obj = graph_Distributable(680.0,720.0,self.obj45)
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

    self.obj46=CompositionType(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # classtype
    self.obj46.classtype.setValue('CompositionType')

    # cardinality
    self.obj46.cardinality.setValue('1')

    # name
    self.obj46.name.setValue('composty1')

    self.obj46.graphClass_= graph_CompositionType
    if self.genGraphics:
       new_obj = graph_CompositionType(280.0,960.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=ComponentPrototype(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # classtype
    self.obj47.classtype.setValue('ComponentPrototype')

    # cardinality
    self.obj47.cardinality.setValue('1')

    # name
    self.obj47.name.setValue('comp1')

    self.obj47.graphClass_= graph_ComponentPrototype
    if self.genGraphics:
       new_obj = graph_ComponentPrototype(380.0,1080.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=SwcToEcuMapping(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # classtype
    self.obj48.classtype.setValue('SwcToEcuMapping')

    # cardinality
    self.obj48.cardinality.setValue('1')

    # name
    self.obj48.name.setValue('stem1')

    self.obj48.graphClass_= graph_SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_SwcToEcuMapping(540.0,920.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.77
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=SwCompToEcuMapping_component(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # classtype
    self.obj49.classtype.setValue('SwCompToEcuMapping_component')

    # cardinality
    self.obj49.cardinality.setValue('1')

    # name
    self.obj49.name.setValue('sctemc1')

    self.obj49.graphClass_= graph_SwCompToEcuMapping_component
    if self.genGraphics:
       new_obj = graph_SwCompToEcuMapping_component(620.0,1080.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SwCompToEcuMapping_component", new_obj.tag)
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
       new_obj = graph_paired_with(157.0,804.5,self.obj50)
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
       new_obj = graph_match_contains(277.5,713.5,self.obj51)
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
       new_obj = graph_match_contains(387.5,713.5,self.obj52)
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
       new_obj = graph_match_contains(487.5,713.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=directLink_S(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # associationType
    self.obj54.associationType.setValue('virtualDevice')

    self.obj54.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(512.0,764.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=directLink_S(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # associationType
    self.obj55.associationType.setValue('distributable')

    self.obj55.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(722.0,764.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=directLink_T(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # associationType
    self.obj56.associationType.setValue('component')

    self.obj56.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(500.5,1037.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=directLink_T(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # associationType
    self.obj57.associationType.setValue('type')

    self.obj57.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(442.5,1065.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=directLink_T(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # associationType
    self.obj58.associationType.setValue('component')

    self.obj58.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(741.5,1062.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
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
       new_obj = graph_apply_contains(290.5,974.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=apply_contains(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(440.5,974.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
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
       new_obj = graph_apply_contains(342.0,1034.0,self.obj61)
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
       new_obj = graph_apply_contains(462.0,1034.0,self.obj62)
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
       new_obj = graph_backward_link(411.0,883.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=backward_link(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # type
    self.obj64.type.setValue('ruleDef')

    self.obj64.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(671.0,883.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=backward_link(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # type
    self.obj65.type.setValue('ruleDef')

    self.obj65.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(792.5,943.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=backward_link(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # type
    self.obj66.type.setValue('ruleDef')

    self.obj66.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(672.5,943.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    # Connections for obj41 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj41,self.obj50,[153.0, 663.0, 157.0, 804.5],"true", 2),
(self.obj41,self.obj51,[153.0, 663.0, 277.5, 713.5],"true", 2),
(self.obj41,self.obj52,[153.0, 663.0, 387.5, 713.5],"true", 2),
(self.obj41,self.obj53,[153.0, 663.0, 487.5, 713.5],"true", 2) )
    # Connections for obj42 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj42,self.obj59,[161.0, 946.0, 290.5, 974.0],"true", 2),
(self.obj42,self.obj60,[161.0, 946.0, 440.5, 974.0],"true", 2),
(self.obj42,self.obj61,[161.0, 946.0, 342.0, 1034.0],"true", 2),
(self.obj42,self.obj62,[161.0, 946.0, 462.0, 1034.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj2) named ecu1
    self.drawConnections(
(self.obj43,self.obj54,[402.0, 764.0, 512.0, 764.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj3) named vd1
    self.drawConnections(
(self.obj44,self.obj55,[622.0, 764.0, 722.0, 764.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj4) named dist1
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj5) named composty1
    self.drawConnections(
(self.obj46,self.obj56,[420.0, 1002.0, 500.5, 1037.0],"true", 2),
(self.obj46,self.obj63,[420.0, 1002.0, 411.0, 883.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj6) named comp1
    self.drawConnections(
(self.obj47,self.obj57,[523.0, 1122.0, 442.5, 1065.0],"true", 2),
(self.obj47,self.obj66,[523.0, 1122.0, 672.5, 943.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj7) named stem1
    self.drawConnections(
(self.obj48,self.obj58,[680.0, 962.0, 741.5, 1062.0],"true", 2),
(self.obj48,self.obj64,[680.0, 962.0, 671.0, 883.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj8) named sctemc1
    self.drawConnections(
(self.obj49,self.obj65,[763.0, 1122.0, 792.5, 943.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj9) of type paired_with
    self.drawConnections(
(self.obj50,self.obj42,[157.0, 804.5, 161.0, 946.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj10) of type match_contains
    self.drawConnections(
(self.obj51,self.obj43,[277.5, 713.5, 402.0, 764.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj11) of type match_contains
    self.drawConnections(
(self.obj52,self.obj44,[387.5, 713.5, 622.0, 764.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj12) of type match_contains
    self.drawConnections(
(self.obj53,self.obj45,[487.5, 713.5, 822.0, 764.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj13) of type directLink_S
    self.drawConnections(
(self.obj54,self.obj44,[512.0, 764.0, 622.0, 764.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj14) of type directLink_S
    self.drawConnections(
(self.obj55,self.obj45,[722.0, 764.0, 822.0, 764.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj15) of type directLink_T
    self.drawConnections(
(self.obj56,self.obj47,[500.5, 1037.0, 523.0, 1122.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj16) of type directLink_T
    self.drawConnections(
(self.obj57,self.obj46,[442.5, 1065.0, 420.0, 1002.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj17) of type directLink_T
    self.drawConnections(
(self.obj58,self.obj49,[741.5, 1062.0, 763.0, 1122.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj18) of type apply_contains
    self.drawConnections(
(self.obj59,self.obj46,[290.5, 974.0, 420.0, 1002.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj19) of type apply_contains
    self.drawConnections(
(self.obj60,self.obj48,[440.5, 974.0, 680.0, 962.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj20) of type apply_contains
    self.drawConnections(
(self.obj61,self.obj47,[342.0, 1034.0, 523.0, 1122.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj21) of type apply_contains
    self.drawConnections(
(self.obj62,self.obj49,[462.0, 1034.0, 763.0, 1122.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj22) of type backward_link
    self.drawConnections(
(self.obj63,self.obj43,[411.0, 883.0, 402.0, 764.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj23) of type backward_link
    self.drawConnections(
(self.obj64,self.obj44,[671.0, 883.0, 622.0, 764.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj24) of type backward_link
    self.drawConnections(
(self.obj65,self.obj45,[792.5, 943.0, 822.0, 764.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj25) of type backward_link
    self.drawConnections(
(self.obj66,self.obj45,[672.5, 943.0, 822.0, 764.0],"true", 2) )

newfunction = ConnVirtualDeviceToDistributable_MDL

loadedMMName = 'GM2AUTOSAR_MM_META'

atom3version = '0.3'
