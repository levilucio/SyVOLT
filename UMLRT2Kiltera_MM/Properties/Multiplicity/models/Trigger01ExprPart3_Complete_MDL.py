"""
__Trigger01ExprPart3_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sun Mar  1 20:53:50 2015
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Expr import *
from MT_pre__Trigger_T import *
from MT_pre__directLink_T import *
from LHS import *
from graph_MT_pre__Expr import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Trigger_T import *
from graph_LHS import *
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

def Trigger01ExprPart3_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('Trigger01ExprPart3_Complete')
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MT_pre__UMLRT2Kiltera_MM ---
    if( MT_pre__UMLRT2Kiltera_MMRootNode ): 
        # author
        MT_pre__UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setValue('')
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj21156=MT_pre__Expr(self)
    self.obj21156.isGraphObjectVisual = True

    if(hasattr(self.obj21156, '_setHierarchicalLink')):
      self.obj21156._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21156.MT_pivotOut__.setValue('')
    self.obj21156.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21156.MT_subtypeMatching__.setValue(('True', 1))
    self.obj21156.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21156.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21156.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21156.MT_pivotIn__.setValue('')
    self.obj21156.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21156.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj21156.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21156.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21156.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21156.MT_pre__name.setHeight(15)

    self.obj21156.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(240.0,60.0,self.obj21156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21156)
    self.globalAndLocalPostcondition(self.obj21156, rootNode)
    self.obj21156.postAction( rootNode.CREATE )

    self.obj21157=MT_pre__Expr(self)
    self.obj21157.isGraphObjectVisual = True

    if(hasattr(self.obj21157, '_setHierarchicalLink')):
      self.obj21157._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21157.MT_pivotOut__.setValue('')
    self.obj21157.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21157.MT_subtypeMatching__.setValue(('True', 1))
    self.obj21157.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21157.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21157.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21157.MT_pivotIn__.setValue('')
    self.obj21157.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21157.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj21157.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21157.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21157.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21157.MT_pre__name.setHeight(15)

    self.obj21157.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(280.0,280.0,self.obj21157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21157)
    self.globalAndLocalPostcondition(self.obj21157, rootNode)
    self.obj21157.postAction( rootNode.CREATE )

    self.obj21160=MT_pre__Trigger_T(self)
    self.obj21160.isGraphObjectVisual = True

    if(hasattr(self.obj21160, '_setHierarchicalLink')):
      self.obj21160._setHierarchicalLink(False)

    # MT_label__
    self.obj21160.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj21160.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj21160.MT_subtypeMatching__.setValue(('True', 1))
    self.obj21160.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21160.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21160.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21160.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21160.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21160.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21160.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21160.MT_pivotIn__.setValue('element1')

    self.obj21160.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(120.0,160.0,self.obj21160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21160)
    self.globalAndLocalPostcondition(self.obj21160, rootNode)
    self.obj21160.postAction( rootNode.CREATE )

    self.obj21158=MT_pre__directLink_T(self)
    self.obj21158.isGraphObjectVisual = True

    if(hasattr(self.obj21158, '_setHierarchicalLink')):
      self.obj21158._setHierarchicalLink(False)

    # MT_label__
    self.obj21158.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj21158.MT_pivotOut__.setValue('')
    self.obj21158.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21158.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21158.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21158.MT_pivotIn__.setValue('')
    self.obj21158.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21158.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21158.MT_pre__associationType.setHeight(15)

    self.obj21158.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(397.0,211.0,self.obj21158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21158)
    self.globalAndLocalPostcondition(self.obj21158, rootNode)
    self.obj21158.postAction( rootNode.CREATE )

    self.obj21159=MT_pre__directLink_T(self)
    self.obj21159.isGraphObjectVisual = True

    if(hasattr(self.obj21159, '_setHierarchicalLink')):
      self.obj21159._setHierarchicalLink(False)

    # MT_label__
    self.obj21159.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj21159.MT_pivotOut__.setValue('')
    self.obj21159.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21159.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21159.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21159.MT_pivotIn__.setValue('')
    self.obj21159.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21159.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21159.MT_pre__associationType.setHeight(15)

    self.obj21159.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(417.0,321.0,self.obj21159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21159)
    self.globalAndLocalPostcondition(self.obj21159, rootNode)
    self.obj21159.postAction( rootNode.CREATE )

    self.obj21155=LHS(self)
    self.obj21155.isGraphObjectVisual = True

    if(hasattr(self.obj21155, '_setHierarchicalLink')):
      self.obj21155._setHierarchicalLink(False)

    # constraint
    self.obj21155.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj21155.constraint.setHeight(15)

    self.obj21155.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,40.0,self.obj21155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21155)
    self.globalAndLocalPostcondition(self.obj21155, rootNode)
    self.obj21155.postAction( rootNode.CREATE )

    # Connections for obj21156 (graphObject_: Obj7) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj21157 (graphObject_: Obj8) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj21160 (graphObject_: Obj11) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj21160,self.obj21158,[337.0, 261.0, 397.0, 211.0],"true", 2),
(self.obj21160,self.obj21159,[337.0, 261.0, 417.0, 321.0],"true", 2) )
    # Connections for obj21158 (graphObject_: Obj9) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21158,self.obj21156,[397.0, 211.0, 457.0, 161.0],"true", 2) )
    # Connections for obj21159 (graphObject_: Obj10) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21159,self.obj21157,[417.0, 321.0, 497.0, 381.0],"true", 2) )
    # Connections for obj21155 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )

newfunction = Trigger01ExprPart3_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
