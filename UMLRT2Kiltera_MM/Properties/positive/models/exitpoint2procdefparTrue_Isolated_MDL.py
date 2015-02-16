"""
__exitpoint2procdefparTrue_Isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 11:26:03 2015
_______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__rightExpr import *
from MT_pre__hasAttribute_S import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
from MT_pre__ExitPoint import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__leftExpr import *
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

def exitpoint2procdefparTrue_Isolated_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('exitpoint2procdefparTrue_Isolated')
    # --- ASG attributes over ---


    self.obj31694=LHS(self)
    self.obj31694.isGraphObjectVisual = True

    if(hasattr(self.obj31694, '_setHierarchicalLink')):
      self.obj31694._setHierarchicalLink(False)

    # constraint
    self.obj31694.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj31694.constraint.setHeight(15)

    self.obj31694.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj31694)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31694.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31694)
    self.globalAndLocalPostcondition(self.obj31694, rootNode)
    self.obj31694.postAction( rootNode.CREATE )

    self.obj31695=MT_pre__State(self)
    self.obj31695.isGraphObjectVisual = True

    if(hasattr(self.obj31695, '_setHierarchicalLink')):
      self.obj31695._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31695.MT_pivotOut__.setValue('')
    self.obj31695.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31695.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31695.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31695.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31695.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31695.MT_pivotIn__.setValue('')
    self.obj31695.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31695.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj31695.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31695.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31695.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31695.MT_pre__name.setHeight(15)

    self.obj31695.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(80.0,300.0,self.obj31695)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31695.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31695)
    self.globalAndLocalPostcondition(self.obj31695, rootNode)
    self.obj31695.postAction( rootNode.CREATE )

    self.obj31696=MT_pre__rightExpr(self)
    self.obj31696.isGraphObjectVisual = True

    if(hasattr(self.obj31696, '_setHierarchicalLink')):
      self.obj31696._setHierarchicalLink(False)

    # MT_label__
    self.obj31696.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj31696.MT_pivotOut__.setValue('')
    self.obj31696.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31696.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31696.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31696.MT_pivotIn__.setValue('')
    self.obj31696.MT_pivotIn__.setNone()

    self.obj31696.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(412.0,164.5,self.obj31696)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31696.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31696)
    self.globalAndLocalPostcondition(self.obj31696, rootNode)
    self.obj31696.postAction( rootNode.CREATE )

    self.obj31697=MT_pre__hasAttribute_S(self)
    self.obj31697.isGraphObjectVisual = True

    if(hasattr(self.obj31697, '_setHierarchicalLink')):
      self.obj31697._setHierarchicalLink(False)

    # MT_label__
    self.obj31697.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj31697.MT_pivotOut__.setValue('')
    self.obj31697.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31697.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31697.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31697.MT_pivotIn__.setValue('')
    self.obj31697.MT_pivotIn__.setNone()

    self.obj31697.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(275.5,308.5,self.obj31697)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31697.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31697)
    self.globalAndLocalPostcondition(self.obj31697, rootNode)
    self.obj31697.postAction( rootNode.CREATE )

    self.obj31698=MT_pre__Attribute(self)
    self.obj31698.isGraphObjectVisual = True

    if(hasattr(self.obj31698, '_setHierarchicalLink')):
      self.obj31698._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31698.MT_pivotOut__.setValue('')
    self.obj31698.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31698.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31698.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31698.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'Bool\'\n')
    self.obj31698.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31698.MT_pivotIn__.setValue('')
    self.obj31698.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31698.MT_label__.setValue('isComposite')

    # MT_pre__name
    self.obj31698.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'isComposite\'\n')
    self.obj31698.MT_pre__name.setHeight(15)

    self.obj31698.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(120.0,200.0,self.obj31698)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31698.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31698)
    self.globalAndLocalPostcondition(self.obj31698, rootNode)
    self.obj31698.postAction( rootNode.CREATE )

    self.obj31699=MT_pre__Constant(self)
    self.obj31699.isGraphObjectVisual = True

    if(hasattr(self.obj31699, '_setHierarchicalLink')):
      self.obj31699._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31699.MT_pivotOut__.setValue('')
    self.obj31699.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31699.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31699.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31699.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'Bool\'\n')
    self.obj31699.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31699.MT_pivotIn__.setValue('')
    self.obj31699.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31699.MT_label__.setValue('7')

    # MT_pre__name
    self.obj31699.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'true\'\n')
    self.obj31699.MT_pre__name.setHeight(15)

    self.obj31699.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(320.0,140.0,self.obj31699)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31699.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31699)
    self.globalAndLocalPostcondition(self.obj31699, rootNode)
    self.obj31699.postAction( rootNode.CREATE )

    self.obj31700=MT_pre__ExitPoint(self)
    self.obj31700.isGraphObjectVisual = True

    if(hasattr(self.obj31700, '_setHierarchicalLink')):
      self.obj31700._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31700.MT_pivotOut__.setValue('')
    self.obj31700.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31700.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31700.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31700.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31700.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31700.MT_pivotIn__.setValue('')
    self.obj31700.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31700.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj31700.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31700.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31700.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31700.MT_pre__name.setHeight(15)

    self.obj31700.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(300.0,240.0,self.obj31700)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31700.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31700)
    self.globalAndLocalPostcondition(self.obj31700, rootNode)
    self.obj31700.postAction( rootNode.CREATE )

    self.obj31701=MT_pre__leftExpr(self)
    self.obj31701.isGraphObjectVisual = True

    if(hasattr(self.obj31701, '_setHierarchicalLink')):
      self.obj31701._setHierarchicalLink(False)

    # MT_label__
    self.obj31701.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj31701.MT_pivotOut__.setValue('')
    self.obj31701.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31701.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31701.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31701.MT_pivotIn__.setValue('')
    self.obj31701.MT_pivotIn__.setNone()

    self.obj31701.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(322.0,164.5,self.obj31701)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31701.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31701)
    self.globalAndLocalPostcondition(self.obj31701, rootNode)
    self.obj31701.postAction( rootNode.CREATE )

    self.obj31702=MT_pre__Equation(self)
    self.obj31702.isGraphObjectVisual = True

    if(hasattr(self.obj31702, '_setHierarchicalLink')):
      self.obj31702._setHierarchicalLink(False)

    # MT_label__
    self.obj31702.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj31702.MT_pivotOut__.setValue('')
    self.obj31702.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj31702.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31702.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj31702.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31702.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31702.MT_pivotIn__.setValue('')
    self.obj31702.MT_pivotIn__.setNone()

    self.obj31702.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(160.0,80.0,self.obj31702)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31702.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31702)
    self.globalAndLocalPostcondition(self.obj31702, rootNode)
    self.obj31702.postAction( rootNode.CREATE )

    # Connections for obj31694 (graphObject_: Obj18) of type LHS
    self.drawConnections(
 )
    # Connections for obj31695 (graphObject_: Obj19) of type MT_pre__State
    self.drawConnections(
(self.obj31695,self.obj31697,[277.0, 375.0, 275.5, 308.5],"true", 2) )
    # Connections for obj31696 (graphObject_: Obj20) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj31696,self.obj31699,[412.0, 164.5, 480.0, 205.0],"true", 2) )
    # Connections for obj31697 (graphObject_: Obj21) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj31697,self.obj31698,[275.5, 308.5, 324.0, 265.0],"true", 2) )
    # Connections for obj31698 (graphObject_: Obj22) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj31699 (graphObject_: Obj23) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj31700 (graphObject_: Obj24) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj31701 (graphObject_: Obj25) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj31701,self.obj31698,[322.0, 164.5, 324.0, 265.0],"true", 2) )
    # Connections for obj31702 (graphObject_: Obj26) of type MT_pre__Equation
    self.drawConnections(
(self.obj31702,self.obj31701,[324.0, 153.0, 322.0, 164.5],"true", 2),
(self.obj31702,self.obj31696,[324.0, 153.0, 412.0, 164.5],"true", 2) )

newfunction = exitpoint2procdefparTrue_Isolated_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
