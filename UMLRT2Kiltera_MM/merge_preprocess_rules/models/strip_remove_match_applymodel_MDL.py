"""
__strip_remove_match_applymodel_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sat Jun  1 13:35:44 2013
___________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MatchModel import *
from MT_pre__ApplyModel import *
from MT_pre__paired_with import *
from RHS import *
from LHS import *
from graph_LHS import *
from graph_RHS import *
from graph_MT_pre__paired_with import *
from graph_MT_pre__MatchModel import *
from graph_MT_pre__ApplyModel import *
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

def strip_remove_match_applymodel_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__GM2AUTOSAR_MM ---
    if( MT_pre__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_pre__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_pre__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_pre__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_pre__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('StripRemoveMatchApplyModels')
    # --- ASG attributes over ---


    self.obj88=MT_pre__MatchModel(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # MT_label__
    self.obj88.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj88.MT_pivotOut__.setValue('')
    self.obj88.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj88.MT_subtypeMatching__.setValue(('True', 0))
    self.obj88.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj88.MT_pivotIn__.setValue('')
    self.obj88.MT_pivotIn__.setNone()

    self.obj88.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(320.0,180.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=MT_pre__ApplyModel(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # MT_label__
    self.obj89.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj89.MT_pivotOut__.setValue('')
    self.obj89.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj89.MT_subtypeMatching__.setValue(('True', 0))
    self.obj89.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj89.MT_pivotIn__.setValue('')
    self.obj89.MT_pivotIn__.setNone()

    self.obj89.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(320.0,360.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=MT_pre__paired_with(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # MT_label__
    self.obj90.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj90.MT_pivotOut__.setValue('')
    self.obj90.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj90.MT_subtypeMatching__.setValue(('True', 0))
    self.obj90.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj90.MT_pivotIn__.setValue('')
    self.obj90.MT_pivotIn__.setNone()

    self.obj90.graphClass_= graph_MT_pre__paired_with
    if self.genGraphics:
       new_obj = graph_MT_pre__paired_with(483.5,343.5,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=RHS(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # action
    self.obj91.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj91.action.setHeight(15)

    self.obj91.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(620.0,140.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj87=LHS(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # constraint
    self.obj87.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj87.constraint.setHeight(15)

    self.obj87.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(200.0,140.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    # Connections for obj88 (graphObject_: Obj1) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj88,self.obj90,[479.0, 253.0, 483.5, 343.5],"true", 2) )
    # Connections for obj89 (graphObject_: Obj2) of type MT_pre__ApplyModel
    self.drawConnections(
 )
    # Connections for obj90 (graphObject_: Obj3) of type MT_pre__paired_with
    self.drawConnections(
(self.obj90,self.obj89,[483.5, 343.5, 488.0, 434.0],"true", 2) )
    # Connections for obj91 (graphObject_: Obj4) of type RHS
    self.drawConnections(
 )
    # Connections for obj87 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = strip_remove_match_applymodel_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
