"""
__InstHProcDefHpart1_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Mar  6 09:36:58 2015
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Inst import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__Constant import *
from MT_pre__hasAttribute_T import *
from MT_pre__leftExpr import *
from MT_pre__rightExpr import *
from LHS import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__hasAttribute_T import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__Inst import *
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

def InstHProcDefHpart1_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('InstHProcDefHpart1_Complete')
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


    self.obj10666=MT_pre__Inst(self)
    self.obj10666.isGraphObjectVisual = True

    if(hasattr(self.obj10666, '_setHierarchicalLink')):
      self.obj10666._setHierarchicalLink(False)

    # MT_label__
    self.obj10666.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj10666.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj10666.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10666.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10666.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10666.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10666.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10666.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10666.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10666.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10666.MT_pivotIn__.setValue('')
    self.obj10666.MT_pivotIn__.setNone()

    self.obj10666.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(60.0,60.0,self.obj10666)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10666.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10666)
    self.globalAndLocalPostcondition(self.obj10666, rootNode)
    self.obj10666.postAction( rootNode.CREATE )

    self.obj10668=MT_pre__Attribute(self)
    self.obj10668.isGraphObjectVisual = True

    if(hasattr(self.obj10668, '_setHierarchicalLink')):
      self.obj10668._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10668.MT_pivotOut__.setValue('')
    self.obj10668.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10668.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10668.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj10668.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10668.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj10668.MT_pivotIn__.setValue('')
    self.obj10668.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10668.MT_label__.setValue('2')

    # MT_pre__name
    self.obj10668.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10668.MT_pre__name.setHeight(15)

    self.obj10668.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(80.0,240.0,self.obj10668)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10668.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10668)
    self.globalAndLocalPostcondition(self.obj10668, rootNode)
    self.obj10668.postAction( rootNode.CREATE )

    self.obj10671=MT_pre__Equation(self)
    self.obj10671.isGraphObjectVisual = True

    if(hasattr(self.obj10671, '_setHierarchicalLink')):
      self.obj10671._setHierarchicalLink(False)

    # MT_label__
    self.obj10671.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10671.MT_pivotOut__.setValue('')
    self.obj10671.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj10671.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10671.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj10671.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10671.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10671.MT_pivotIn__.setValue('')
    self.obj10671.MT_pivotIn__.setNone()

    self.obj10671.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(280.0,280.0,self.obj10671)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10671.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10671)
    self.globalAndLocalPostcondition(self.obj10671, rootNode)
    self.obj10671.postAction( rootNode.CREATE )

    self.obj10669=MT_pre__Constant(self)
    self.obj10669.isGraphObjectVisual = True

    if(hasattr(self.obj10669, '_setHierarchicalLink')):
      self.obj10669._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10669.MT_pivotOut__.setValue('')
    self.obj10669.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10669.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10669.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj10669.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10669.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj10669.MT_pivotIn__.setValue('')
    self.obj10669.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10669.MT_label__.setValue('3')

    # MT_pre__name
    self.obj10669.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10669.MT_pre__name.setHeight(15)

    self.obj10669.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(300.0,160.0,self.obj10669)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10669.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10669)
    self.globalAndLocalPostcondition(self.obj10669, rootNode)
    self.obj10669.postAction( rootNode.CREATE )

    self.obj10667=MT_pre__hasAttribute_T(self)
    self.obj10667.isGraphObjectVisual = True

    if(hasattr(self.obj10667, '_setHierarchicalLink')):
      self.obj10667._setHierarchicalLink(False)

    # MT_label__
    self.obj10667.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj10667.MT_pivotOut__.setValue('')
    self.obj10667.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10667.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10667.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10667.MT_pivotIn__.setValue('')
    self.obj10667.MT_pivotIn__.setNone()

    self.obj10667.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(278.5,233.0,self.obj10667)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10667.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10667)
    self.globalAndLocalPostcondition(self.obj10667, rootNode)
    self.obj10667.postAction( rootNode.CREATE )

    self.obj10670=MT_pre__leftExpr(self)
    self.obj10670.isGraphObjectVisual = True

    if(hasattr(self.obj10670, '_setHierarchicalLink')):
      self.obj10670._setHierarchicalLink(False)

    # MT_label__
    self.obj10670.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj10670.MT_pivotOut__.setValue('')
    self.obj10670.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10670.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10670.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10670.MT_pivotIn__.setValue('')
    self.obj10670.MT_pivotIn__.setNone()

    self.obj10670.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(362.0,329.0,self.obj10670)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10670.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10670)
    self.globalAndLocalPostcondition(self.obj10670, rootNode)
    self.obj10670.postAction( rootNode.CREATE )

    self.obj10665=MT_pre__rightExpr(self)
    self.obj10665.isGraphObjectVisual = True

    if(hasattr(self.obj10665, '_setHierarchicalLink')):
      self.obj10665._setHierarchicalLink(False)

    # MT_label__
    self.obj10665.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj10665.MT_pivotOut__.setValue('')
    self.obj10665.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10665.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10665.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10665.MT_pivotIn__.setValue('')
    self.obj10665.MT_pivotIn__.setNone()

    self.obj10665.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(442.0,289.0,self.obj10665)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10665.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10665)
    self.globalAndLocalPostcondition(self.obj10665, rootNode)
    self.obj10665.postAction( rootNode.CREATE )

    self.obj10664=LHS(self)
    self.obj10664.isGraphObjectVisual = True

    if(hasattr(self.obj10664, '_setHierarchicalLink')):
      self.obj10664._setHierarchicalLink(False)

    # constraint
    self.obj10664.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'3\')[\'name\']==\'H\'):\n   return True\nreturn False\n')
    self.obj10664.constraint.setHeight(15)

    self.obj10664.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,40.0,self.obj10664)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10664.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10664)
    self.globalAndLocalPostcondition(self.obj10664, rootNode)
    self.obj10664.postAction( rootNode.CREATE )

    # Connections for obj10666 (graphObject_: Obj17) of type MT_pre__Inst
    self.drawConnections(
(self.obj10666,self.obj10667,[277.0, 161.0, 278.5, 233.0],"true", 2) )
    # Connections for obj10668 (graphObject_: Obj19) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj10671 (graphObject_: Obj22) of type MT_pre__Equation
    self.drawConnections(
(self.obj10671,self.obj10670,[444.0, 353.0, 362.0, 329.0],"true", 2),
(self.obj10671,self.obj10665,[444.0, 353.0, 442.0, 289.0],"true", 2) )
    # Connections for obj10669 (graphObject_: Obj20) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj10667 (graphObject_: Obj18) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj10667,self.obj10668,[278.5, 233.0, 240.0, 305.0],"true", 2) )
    # Connections for obj10670 (graphObject_: Obj21) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj10670,self.obj10668,[362.0, 329.0, 240.0, 305.0],"true", 2) )
    # Connections for obj10665 (graphObject_: Obj16) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj10665,self.obj10669,[442.0, 289.0, 460.0, 225.0],"true", 2) )
    # Connections for obj10664 (graphObject_: Obj15) of type LHS
    self.drawConnections(
 )

newfunction = InstHProcDefHpart1_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
