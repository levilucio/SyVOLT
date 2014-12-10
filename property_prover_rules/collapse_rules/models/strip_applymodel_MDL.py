"""
__strip_applymodel_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sat Jun  1 13:27:00 2013
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ApplyModel import *
from MT_pre__MetaModelElement_T import *
from MT_pre__apply_contains import *
from MT_post__MetaModelElement_T import *
from MT_post__ApplyModel import *
from RHS import *
from LHS import *
from graph_MT_pre__apply_contains import *
from graph_MT_post__MetaModelElement_T import *
from graph_LHS import *
from graph_MT_post__ApplyModel import *
from graph_MT_pre__ApplyModel import *
from graph_MT_pre__MetaModelElement_T import *
from graph_RHS import *
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

def strip_applymodel_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MT_post__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MT_post__GM2AUTOSAR_MM ---
    if( MT_post__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_post__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_post__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_post__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_post__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_post__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('StripApplyModel')
    # --- ASG attributes over ---


    self.obj9490=MT_pre__ApplyModel(self)
    self.obj9490.isGraphObjectVisual = True

    if(hasattr(self.obj9490, '_setHierarchicalLink')):
      self.obj9490._setHierarchicalLink(False)

    # MT_label__
    self.obj9490.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj9490.MT_pivotOut__.setValue('')
    self.obj9490.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj9490.MT_subtypeMatching__.setValue(('True', 0))
    self.obj9490.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj9490.MT_pivotIn__.setValue('')
    self.obj9490.MT_pivotIn__.setNone()

    self.obj9490.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(280.0,160.0,self.obj9490)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj9490.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj9490)
    self.globalAndLocalPostcondition(self.obj9490, rootNode)
    self.obj9490.postAction( rootNode.CREATE )

    self.obj9491=MT_pre__MetaModelElement_T(self)
    self.obj9491.isGraphObjectVisual = True

    if(hasattr(self.obj9491, '_setHierarchicalLink')):
      self.obj9491._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj9491.MT_pivotOut__.setValue('')
    self.obj9491.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj9491.MT_subtypeMatching__.setValue(('True', 1))
    self.obj9491.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj9491.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj9491.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj9491.MT_pivotIn__.setValue('')
    self.obj9491.MT_pivotIn__.setNone()

    # MT_label__
    self.obj9491.MT_label__.setValue('2')

    # MT_pre__name
    self.obj9491.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj9491.MT_pre__name.setHeight(15)

    self.obj9491.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(280.0,320.0,self.obj9491)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj9491.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj9491)
    self.globalAndLocalPostcondition(self.obj9491, rootNode)
    self.obj9491.postAction( rootNode.CREATE )

    self.obj9498=MT_pre__apply_contains(self)
    self.obj9498.isGraphObjectVisual = True

    if(hasattr(self.obj9498, '_setHierarchicalLink')):
      self.obj9498._setHierarchicalLink(False)

    # MT_label__
    self.obj9498.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj9498.MT_pivotOut__.setValue('')
    self.obj9498.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj9498.MT_subtypeMatching__.setValue(('True', 0))
    self.obj9498.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj9498.MT_pivotIn__.setValue('')
    self.obj9498.MT_pivotIn__.setNone()

    self.obj9498.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(448.0,313.5,self.obj9498)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj9498.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj9498)
    self.globalAndLocalPostcondition(self.obj9498, rootNode)
    self.obj9498.postAction( rootNode.CREATE )

    self.obj14196=MT_post__MetaModelElement_T(self)
    self.obj14196.isGraphObjectVisual = True

    if(hasattr(self.obj14196, '_setHierarchicalLink')):
      self.obj14196._setHierarchicalLink(False)

    # MT_label__
    self.obj14196.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj14196.MT_pivotOut__.setValue('')
    self.obj14196.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj14196.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj14196.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj14196.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj14196.MT_post__name.setHeight(15)

    self.obj14196.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(780.0,320.0,self.obj14196)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14196.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14196)
    self.globalAndLocalPostcondition(self.obj14196, rootNode)
    self.obj14196.postAction( rootNode.CREATE )

    self.obj9499=MT_post__ApplyModel(self)
    self.obj9499.isGraphObjectVisual = True

    if(hasattr(self.obj9499, '_setHierarchicalLink')):
      self.obj9499._setHierarchicalLink(False)

    # MT_label__
    self.obj9499.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj9499.MT_pivotOut__.setValue('')
    self.obj9499.MT_pivotOut__.setNone()

    self.obj9499.graphClass_= graph_MT_post__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_post__ApplyModel(780.0,160.0,self.obj9499)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj9499.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj9499)
    self.globalAndLocalPostcondition(self.obj9499, rootNode)
    self.obj9499.postAction( rootNode.CREATE )

    self.obj91=RHS(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # action
    self.obj91.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj91.action.setHeight(15)

    self.obj91.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(580.0,120.0,self.obj91)
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
       new_obj = graph_LHS(140.0,120.0,self.obj87)
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

    # Connections for obj9490 (graphObject_: Obj6) of type MT_pre__ApplyModel
    self.drawConnections(
(self.obj9490,self.obj9498,[448.0, 234.0, 448.0, 313.5],"true", 2) )
    # Connections for obj9491 (graphObject_: Obj7) of type MT_pre__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj9498 (graphObject_: Obj8) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj9498,self.obj9491,[448.0, 313.5, 448.0, 393.0],"true", 2) )
    # Connections for obj14196 (graphObject_: Obj10) of type MT_post__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj9499 (graphObject_: Obj9) of type MT_post__ApplyModel
    self.drawConnections(
 )
    # Connections for obj91 (graphObject_: Obj4) of type RHS
    self.drawConnections(
 )
    # Connections for obj87 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = strip_applymodel_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MT_post__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
