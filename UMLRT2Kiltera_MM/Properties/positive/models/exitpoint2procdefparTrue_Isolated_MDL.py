"""
__exitpoint2procdefparTrue_Isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 14:49:10 2015
_______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__State import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__Constant import *
from MT_pre__hasAttribute_S import *
from MT_pre__leftExpr import *
from MT_pre__rightExpr import *
from LHS import *
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

def exitpoint2procdefparTrue_Isolated_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

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


    self.obj31749=MT_pre__ExitPoint(self)
    self.obj31749.isGraphObjectVisual = True

    if(hasattr(self.obj31749, '_setHierarchicalLink')):
      self.obj31749._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31749.MT_pivotOut__.setValue('')
    self.obj31749.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31749.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31749.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31749.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31749.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31749.MT_pivotIn__.setValue('')
    self.obj31749.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31749.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj31749.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31749.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31749.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31749.MT_pre__name.setHeight(15)

    self.obj31749.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(300.0,240.0,self.obj31749)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31749.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31749)
    self.globalAndLocalPostcondition(self.obj31749, rootNode)
    self.obj31749.postAction( rootNode.CREATE )

    self.obj31744=MT_pre__State(self)
    self.obj31744.isGraphObjectVisual = True

    if(hasattr(self.obj31744, '_setHierarchicalLink')):
      self.obj31744._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31744.MT_pivotOut__.setValue('')
    self.obj31744.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31744.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31744.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31744.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31744.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31744.MT_pivotIn__.setValue('')
    self.obj31744.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31744.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj31744.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31744.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31744.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31744.MT_pre__name.setHeight(15)

    self.obj31744.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(80.0,300.0,self.obj31744)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31744.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31744)
    self.globalAndLocalPostcondition(self.obj31744, rootNode)
    self.obj31744.postAction( rootNode.CREATE )

    self.obj31747=MT_pre__Attribute(self)
    self.obj31747.isGraphObjectVisual = True

    if(hasattr(self.obj31747, '_setHierarchicalLink')):
      self.obj31747._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31747.MT_pivotOut__.setValue('')
    self.obj31747.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31747.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31747.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31747.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'Bool\'\n')
    self.obj31747.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31747.MT_pivotIn__.setValue('')
    self.obj31747.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31747.MT_label__.setValue('isComposite')

    # MT_pre__name
    self.obj31747.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'isComposite\'\n')
    self.obj31747.MT_pre__name.setHeight(15)

    self.obj31747.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(120.0,200.0,self.obj31747)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31747.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31747)
    self.globalAndLocalPostcondition(self.obj31747, rootNode)
    self.obj31747.postAction( rootNode.CREATE )

    self.obj31751=MT_pre__Equation(self)
    self.obj31751.isGraphObjectVisual = True

    if(hasattr(self.obj31751, '_setHierarchicalLink')):
      self.obj31751._setHierarchicalLink(False)

    # MT_label__
    self.obj31751.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj31751.MT_pivotOut__.setValue('')
    self.obj31751.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj31751.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'eq1\'\n')
    self.obj31751.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj31751.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31751.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31751.MT_pivotIn__.setValue('')
    self.obj31751.MT_pivotIn__.setNone()

    self.obj31751.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(160.0,80.0,self.obj31751)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31751.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31751)
    self.globalAndLocalPostcondition(self.obj31751, rootNode)
    self.obj31751.postAction( rootNode.CREATE )

    self.obj31748=MT_pre__Constant(self)
    self.obj31748.isGraphObjectVisual = True

    if(hasattr(self.obj31748, '_setHierarchicalLink')):
      self.obj31748._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31748.MT_pivotOut__.setValue('')
    self.obj31748.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31748.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31748.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31748.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'Bool\'\n')
    self.obj31748.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31748.MT_pivotIn__.setValue('')
    self.obj31748.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31748.MT_label__.setValue('7')

    # MT_pre__name
    self.obj31748.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'true\'\n')
    self.obj31748.MT_pre__name.setHeight(15)

    self.obj31748.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(320.0,140.0,self.obj31748)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31748.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31748)
    self.globalAndLocalPostcondition(self.obj31748, rootNode)
    self.obj31748.postAction( rootNode.CREATE )

    self.obj31746=MT_pre__hasAttribute_S(self)
    self.obj31746.isGraphObjectVisual = True

    if(hasattr(self.obj31746, '_setHierarchicalLink')):
      self.obj31746._setHierarchicalLink(False)

    # MT_label__
    self.obj31746.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj31746.MT_pivotOut__.setValue('')
    self.obj31746.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31746.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31746.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31746.MT_pivotIn__.setValue('')
    self.obj31746.MT_pivotIn__.setNone()

    self.obj31746.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(275.5,308.5,self.obj31746)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31746.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31746)
    self.globalAndLocalPostcondition(self.obj31746, rootNode)
    self.obj31746.postAction( rootNode.CREATE )

    self.obj31750=MT_pre__leftExpr(self)
    self.obj31750.isGraphObjectVisual = True

    if(hasattr(self.obj31750, '_setHierarchicalLink')):
      self.obj31750._setHierarchicalLink(False)

    # MT_label__
    self.obj31750.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj31750.MT_pivotOut__.setValue('')
    self.obj31750.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31750.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31750.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31750.MT_pivotIn__.setValue('')
    self.obj31750.MT_pivotIn__.setNone()

    self.obj31750.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(322.0,164.5,self.obj31750)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31750.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31750)
    self.globalAndLocalPostcondition(self.obj31750, rootNode)
    self.obj31750.postAction( rootNode.CREATE )

    self.obj31745=MT_pre__rightExpr(self)
    self.obj31745.isGraphObjectVisual = True

    if(hasattr(self.obj31745, '_setHierarchicalLink')):
      self.obj31745._setHierarchicalLink(False)

    # MT_label__
    self.obj31745.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj31745.MT_pivotOut__.setValue('')
    self.obj31745.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31745.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31745.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31745.MT_pivotIn__.setValue('')
    self.obj31745.MT_pivotIn__.setNone()

    self.obj31745.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(412.0,164.5,self.obj31745)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31745.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31745)
    self.globalAndLocalPostcondition(self.obj31745, rootNode)
    self.obj31745.postAction( rootNode.CREATE )

    self.obj31743=LHS(self)
    self.obj31743.isGraphObjectVisual = True

    if(hasattr(self.obj31743, '_setHierarchicalLink')):
      self.obj31743._setHierarchicalLink(False)

    # constraint
    self.obj31743.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj31743.constraint.setHeight(15)

    self.obj31743.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj31743)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31743.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31743)
    self.globalAndLocalPostcondition(self.obj31743, rootNode)
    self.obj31743.postAction( rootNode.CREATE )

    # Connections for obj31749 (graphObject_: Obj96) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj31744 (graphObject_: Obj91) of type MT_pre__State
    self.drawConnections(
(self.obj31744,self.obj31746,[277.0, 375.0, 275.5, 308.5],"true", 2) )
    # Connections for obj31747 (graphObject_: Obj94) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj31751 (graphObject_: Obj98) of type MT_pre__Equation
    self.drawConnections(
(self.obj31751,self.obj31750,[324.0, 153.0, 322.0, 164.5],"true", 2),
(self.obj31751,self.obj31745,[324.0, 153.0, 412.0, 164.5],"true", 2) )
    # Connections for obj31748 (graphObject_: Obj95) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj31746 (graphObject_: Obj93) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj31746,self.obj31747,[275.5, 308.5, 324.0, 265.0],"true", 2) )
    # Connections for obj31750 (graphObject_: Obj97) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj31750,self.obj31747,[322.0, 164.5, 324.0, 265.0],"true", 2) )
    # Connections for obj31745 (graphObject_: Obj92) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj31745,self.obj31748,[412.0, 164.5, 480.0, 205.0],"true", 2) )
    # Connections for obj31743 (graphObject_: Obj90) of type LHS
    self.drawConnections(
 )

newfunction = exitpoint2procdefparTrue_Isolated_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
