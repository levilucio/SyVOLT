"""
__ConditionBranch1ExprPart3_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  2 18:51:33 2015
________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__ConditionBranch import *
from MT_pre__Expr import *
from MT_pre__directLink_T import *
from graph_MT_pre__Expr import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__ConditionBranch import *
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

def ConditionBranch1ExprPart3_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ConditionBranch1ExprPart3_Complete')
    # --- ASG attributes over ---


    self.obj123=LHS(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # constraint
    self.obj123.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj123.constraint.setHeight(15)

    self.obj123.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=MT_pre__ConditionBranch(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj124.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj124.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj124.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj124.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__name.setHeight(15)

    self.obj124.graphClass_= graph_MT_pre__ConditionBranch
    if self.genGraphics:
       new_obj = graph_MT_pre__ConditionBranch(40.0,40.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ConditionBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj10639=MT_pre__Expr(self)
    self.obj10639.isGraphObjectVisual = True

    if(hasattr(self.obj10639, '_setHierarchicalLink')):
      self.obj10639._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10639.MT_pivotOut__.setValue('')
    self.obj10639.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10639.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10639.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10639.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10639.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10639.MT_pivotIn__.setValue('')
    self.obj10639.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10639.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10639.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10639.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10639.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10639.MT_pre__name.setHeight(15)

    self.obj10639.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(40.0,220.0,self.obj10639)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10639.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10639)
    self.globalAndLocalPostcondition(self.obj10639, rootNode)
    self.obj10639.postAction( rootNode.CREATE )

    self.obj21153=MT_pre__Expr(self)
    self.obj21153.isGraphObjectVisual = True

    if(hasattr(self.obj21153, '_setHierarchicalLink')):
      self.obj21153._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21153.MT_pivotOut__.setValue('')
    self.obj21153.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21153.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21153.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21153.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21153.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21153.MT_pivotIn__.setValue('')
    self.obj21153.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21153.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj21153.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21153.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21153.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21153.MT_pre__name.setHeight(15)

    self.obj21153.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(240.0,160.0,self.obj21153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21153)
    self.globalAndLocalPostcondition(self.obj21153, rootNode)
    self.obj21153.postAction( rootNode.CREATE )

    self.obj10640=MT_pre__directLink_T(self)
    self.obj10640.isGraphObjectVisual = True

    if(hasattr(self.obj10640, '_setHierarchicalLink')):
      self.obj10640._setHierarchicalLink(False)

    # MT_label__
    self.obj10640.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj10640.MT_pivotOut__.setValue('')
    self.obj10640.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10640.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10640.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10640.MT_pivotIn__.setValue('')
    self.obj10640.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10640.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10640.MT_pre__associationType.setHeight(15)

    self.obj10640.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(210.0,233.0,self.obj10640)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10640.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10640)
    self.globalAndLocalPostcondition(self.obj10640, rootNode)
    self.obj10640.postAction( rootNode.CREATE )

    self.obj21154=MT_pre__directLink_T(self)
    self.obj21154.isGraphObjectVisual = True

    if(hasattr(self.obj21154, '_setHierarchicalLink')):
      self.obj21154._setHierarchicalLink(False)

    # MT_label__
    self.obj21154.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj21154.MT_pivotOut__.setValue('')
    self.obj21154.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21154.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21154.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21154.MT_pivotIn__.setValue('')
    self.obj21154.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21154.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21154.MT_pre__associationType.setHeight(15)

    self.obj21154.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(357.0,201.0,self.obj21154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21154)
    self.globalAndLocalPostcondition(self.obj21154, rootNode)
    self.obj21154.postAction( rootNode.CREATE )

    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__ConditionBranch
    self.drawConnections(
(self.obj124,self.obj10640,[257.0, 141.0, 210.0, 233.0],"true", 2),
(self.obj124,self.obj21154,[257.0, 141.0, 357.0, 201.0],"true", 2) )
    # Connections for obj10639 (graphObject_: Obj2) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj21153 (graphObject_: Obj4) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj10640 (graphObject_: Obj3) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10640,self.obj10639,[210.0, 233.0, 257.0, 321.0],"true", 2) )
    # Connections for obj21154 (graphObject_: Obj5) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21154,self.obj21153,[357.0, 201.0, 457.0, 261.0],"true", 2) )

newfunction = ConditionBranch1ExprPart3_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
