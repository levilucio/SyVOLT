"""
__Trigger01ExprPart3_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 23 15:14:38 2015
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Expr import *
from MT_pre__directLink_T import *
from MT_pre__Trigger_T import *
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

def Trigger01ExprPart3_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('Trigger01ExprPart3_Complete')
    # --- ASG attributes over ---


    self.obj73759=LHS(self)
    self.obj73759.isGraphObjectVisual = True

    if(hasattr(self.obj73759, '_setHierarchicalLink')):
      self.obj73759._setHierarchicalLink(False)

    # constraint
    self.obj73759.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj73759.constraint.setHeight(15)

    self.obj73759.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,40.0,self.obj73759)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73759.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73759)
    self.globalAndLocalPostcondition(self.obj73759, rootNode)
    self.obj73759.postAction( rootNode.CREATE )

    self.obj73760=MT_pre__Expr(self)
    self.obj73760.isGraphObjectVisual = True

    if(hasattr(self.obj73760, '_setHierarchicalLink')):
      self.obj73760._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73760.MT_pivotOut__.setValue('')
    self.obj73760.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73760.MT_subtypeMatching__.setValue(('True', 1))
    self.obj73760.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73760.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73760.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73760.MT_pivotIn__.setValue('')
    self.obj73760.MT_pivotIn__.setNone()

    # MT_label__
    self.obj73760.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj73760.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73760.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73760.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73760.MT_pre__name.setHeight(15)

    self.obj73760.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(240.0,60.0,self.obj73760)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73760.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73760)
    self.globalAndLocalPostcondition(self.obj73760, rootNode)
    self.obj73760.postAction( rootNode.CREATE )

    self.obj73761=MT_pre__Expr(self)
    self.obj73761.isGraphObjectVisual = True

    if(hasattr(self.obj73761, '_setHierarchicalLink')):
      self.obj73761._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73761.MT_pivotOut__.setValue('')
    self.obj73761.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73761.MT_subtypeMatching__.setValue(('True', 1))
    self.obj73761.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73761.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73761.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73761.MT_pivotIn__.setValue('')
    self.obj73761.MT_pivotIn__.setNone()

    # MT_label__
    self.obj73761.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj73761.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73761.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73761.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73761.MT_pre__name.setHeight(15)

    self.obj73761.graphClass_= graph_MT_pre__Expr
    if self.genGraphics:
       new_obj = graph_MT_pre__Expr(280.0,280.0,self.obj73761)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73761.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73761)
    self.globalAndLocalPostcondition(self.obj73761, rootNode)
    self.obj73761.postAction( rootNode.CREATE )

    self.obj73762=MT_pre__directLink_T(self)
    self.obj73762.isGraphObjectVisual = True

    if(hasattr(self.obj73762, '_setHierarchicalLink')):
      self.obj73762._setHierarchicalLink(False)

    # MT_label__
    self.obj73762.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj73762.MT_pivotOut__.setValue('')
    self.obj73762.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73762.MT_subtypeMatching__.setValue(('True', 0))
    self.obj73762.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj73762.MT_pivotIn__.setValue('')
    self.obj73762.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj73762.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73762.MT_pre__associationType.setHeight(15)

    self.obj73762.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(397.0,211.0,self.obj73762)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73762.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73762)
    self.globalAndLocalPostcondition(self.obj73762, rootNode)
    self.obj73762.postAction( rootNode.CREATE )

    self.obj73763=MT_pre__directLink_T(self)
    self.obj73763.isGraphObjectVisual = True

    if(hasattr(self.obj73763, '_setHierarchicalLink')):
      self.obj73763._setHierarchicalLink(False)

    # MT_label__
    self.obj73763.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj73763.MT_pivotOut__.setValue('')
    self.obj73763.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73763.MT_subtypeMatching__.setValue(('True', 0))
    self.obj73763.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj73763.MT_pivotIn__.setValue('')
    self.obj73763.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj73763.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73763.MT_pre__associationType.setHeight(15)

    self.obj73763.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(417.0,321.0,self.obj73763)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73763.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73763)
    self.globalAndLocalPostcondition(self.obj73763, rootNode)
    self.obj73763.postAction( rootNode.CREATE )

    self.obj73764=MT_pre__Trigger_T(self)
    self.obj73764.isGraphObjectVisual = True

    if(hasattr(self.obj73764, '_setHierarchicalLink')):
      self.obj73764._setHierarchicalLink(False)

    # MT_label__
    self.obj73764.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj73764.MT_pivotOut__.setValue('')
    self.obj73764.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73764.MT_subtypeMatching__.setValue(('True', 1))
    self.obj73764.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73764.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73764.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj73764.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73764.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73764.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73764.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj73764.MT_pivotIn__.setValue('element1')

    self.obj73764.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(120.0,160.0,self.obj73764)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73764.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73764)
    self.globalAndLocalPostcondition(self.obj73764, rootNode)
    self.obj73764.postAction( rootNode.CREATE )

    # Connections for obj73759 (graphObject_: Obj12) of type LHS
    self.drawConnections(
 )
    # Connections for obj73760 (graphObject_: Obj13) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj73761 (graphObject_: Obj14) of type MT_pre__Expr
    self.drawConnections(
 )
    # Connections for obj73762 (graphObject_: Obj15) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj73762,self.obj73760,[397.0, 211.0, 457.0, 161.0],"true", 2) )
    # Connections for obj73763 (graphObject_: Obj16) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj73763,self.obj73761,[417.0, 321.0, 497.0, 381.0],"true", 2) )
    # Connections for obj73764 (graphObject_: Obj17) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj73764,self.obj73762,[337.0, 261.0, 397.0, 211.0],"true", 2),
(self.obj73764,self.obj73763,[337.0, 261.0, 417.0, 321.0],"true", 2) )

newfunction = Trigger01ExprPart3_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'