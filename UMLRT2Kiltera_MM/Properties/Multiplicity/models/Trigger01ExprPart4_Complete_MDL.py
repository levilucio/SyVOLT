"""
__Trigger01ExprPart4_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sun Mar  1 20:55:19 2015
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

def Trigger01ExprPart4_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('Trigger01ExprPart4_Complete')
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


    self.obj31674=MT_pre__Expr(self)
    self.obj31674.isGraphObjectVisual = True

    if(hasattr(self.obj31674, '_setHierarchicalLink')):
      self.obj31674._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31674.MT_pivotOut__.setValue('')
    self.obj31674.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31674.MT_subtypeMatching__.setValue(('True', 1))
    self.obj31674.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31674.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31674.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31674.MT_pivotIn__.setValue('')
    self.obj31674.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31674.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj31674.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31674.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31674.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31674.MT_pre__name.setHeight(15)

    self.obj31674.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(240.0,60.0,self.obj31674)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31674.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31674)
    self.globalAndLocalPostcondition(self.obj31674, rootNode)
    self.obj31674.postAction( rootNode.CREATE )

    self.obj31676=MT_pre__Trigger_T(self)
    self.obj31676.isGraphObjectVisual = True

    if(hasattr(self.obj31676, '_setHierarchicalLink')):
      self.obj31676._setHierarchicalLink(False)

    # MT_label__
    self.obj31676.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj31676.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj31676.MT_subtypeMatching__.setValue(('True', 1))
    self.obj31676.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31676.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31676.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj31676.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31676.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31676.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31676.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj31676.MT_pivotIn__.setValue('element1')

    self.obj31676.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(120.0,160.0,self.obj31676)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31676.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31676)
    self.globalAndLocalPostcondition(self.obj31676, rootNode)
    self.obj31676.postAction( rootNode.CREATE )

    self.obj31675=MT_pre__directLink_T(self)
    self.obj31675.isGraphObjectVisual = True

    if(hasattr(self.obj31675, '_setHierarchicalLink')):
      self.obj31675._setHierarchicalLink(False)

    # MT_label__
    self.obj31675.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj31675.MT_pivotOut__.setValue('')
    self.obj31675.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31675.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31675.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31675.MT_pivotIn__.setValue('')
    self.obj31675.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj31675.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31675.MT_pre__associationType.setHeight(15)

    self.obj31675.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(397.0,211.0,self.obj31675)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31675.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31675)
    self.globalAndLocalPostcondition(self.obj31675, rootNode)
    self.obj31675.postAction( rootNode.CREATE )

    self.obj31673=LHS(self)
    self.obj31673.isGraphObjectVisual = True

    if(hasattr(self.obj31673, '_setHierarchicalLink')):
      self.obj31673._setHierarchicalLink(False)

    # constraint
    self.obj31673.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj31673.constraint.setHeight(15)

    self.obj31673.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,40.0,self.obj31673)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31673.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31673)
    self.globalAndLocalPostcondition(self.obj31673, rootNode)
    self.obj31673.postAction( rootNode.CREATE )

    # Connections for obj31674 (graphObject_: Obj13) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj31676 (graphObject_: Obj15) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj31676,self.obj31675,[337.0, 261.0, 397.0, 211.0],"true", 2) )
    # Connections for obj31675 (graphObject_: Obj14) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj31675,self.obj31674,[397.0, 211.0, 457.0, 161.0],"true", 2) )
    # Connections for obj31673 (graphObject_: Obj12) of type LHS
    self.drawConnections(
 )

newfunction = Trigger01ExprPart4_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
