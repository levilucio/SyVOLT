"""
__ExitPtConOPsOfExitPtOUT_Isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 18:06:44 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__Transition import *
from MT_pre__State import *
from MT_pre__OUT2 import *
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
from graph_MT_pre__Transition import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__OUT2 import *
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

def ExitPtConOPsOfExitPtOUT_Isolated_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ExitPtConOPsOfExitPtOUT_Isolated')
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


    self.obj63368=MT_pre__ExitPoint(self)
    self.obj63368.isGraphObjectVisual = True

    if(hasattr(self.obj63368, '_setHierarchicalLink')):
      self.obj63368._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63368.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj63368.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63368.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63368.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63368.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63368.MT_pivotIn__.setValue('')
    self.obj63368.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63368.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj63368.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63368.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63368.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63368.MT_pre__name.setHeight(15)

    self.obj63368.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(234.0,40.0,self.obj63368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63368.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63368)
    self.globalAndLocalPostcondition(self.obj63368, rootNode)
    self.obj63368.postAction( rootNode.CREATE )

    self.obj63369=MT_pre__Transition(self)
    self.obj63369.isGraphObjectVisual = True

    if(hasattr(self.obj63369, '_setHierarchicalLink')):
      self.obj63369._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63369.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj63369.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63369.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63369.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63369.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63369.MT_pivotIn__.setValue('')
    self.obj63369.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63369.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj63369.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63369.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63369.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63369.MT_pre__name.setHeight(15)

    self.obj63369.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(277.0,128.0,self.obj63369)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63369.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63369)
    self.globalAndLocalPostcondition(self.obj63369, rootNode)
    self.obj63369.postAction( rootNode.CREATE )

    self.obj63370=MT_pre__State(self)
    self.obj63370.isGraphObjectVisual = True

    if(hasattr(self.obj63370, '_setHierarchicalLink')):
      self.obj63370._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63370.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj63370.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63370.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63370.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63370.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63370.MT_pivotIn__.setValue('')
    self.obj63370.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63370.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj63370.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63370.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63370.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63370.MT_pre__name.setHeight(15)

    self.obj63370.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj63370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63370.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63370)
    self.globalAndLocalPostcondition(self.obj63370, rootNode)
    self.obj63370.postAction( rootNode.CREATE )

    self.obj63371=MT_pre__OUT2(self)
    self.obj63371.isGraphObjectVisual = True

    if(hasattr(self.obj63371, '_setHierarchicalLink')):
      self.obj63371._setHierarchicalLink(False)

    # MT_label__
    self.obj63371.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj63371.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj63371.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63371.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63371.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63371.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63371.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63371.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63371.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63371.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63371.MT_pivotIn__.setValue('')
    self.obj63371.MT_pivotIn__.setNone()

    self.obj63371.graphClass_= graph_MT_pre__OUT2
    if self.genGraphics:
       new_obj = graph_MT_pre__OUT2(60.0,129.0,self.obj63371)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63371.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63371)
    self.globalAndLocalPostcondition(self.obj63371, rootNode)
    self.obj63371.postAction( rootNode.CREATE )

    self.obj63375=MT_pre__Attribute(self)
    self.obj63375.isGraphObjectVisual = True

    if(hasattr(self.obj63375, '_setHierarchicalLink')):
      self.obj63375._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63375.MT_pivotOut__.setValue('')
    self.obj63375.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63375.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63375.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj63375.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63375.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj63375.MT_pivotIn__.setValue('')
    self.obj63375.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63375.MT_label__.setValue('7')

    # MT_pre__name
    self.obj63375.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63375.MT_pre__name.setHeight(15)

    self.obj63375.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(80.0,220.0,self.obj63375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63375.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63375)
    self.globalAndLocalPostcondition(self.obj63375, rootNode)
    self.obj63375.postAction( rootNode.CREATE )

    self.obj63374=MT_pre__Equation(self)
    self.obj63374.isGraphObjectVisual = True

    if(hasattr(self.obj63374, '_setHierarchicalLink')):
      self.obj63374._setHierarchicalLink(False)

    # MT_label__
    self.obj63374.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj63374.MT_pivotOut__.setValue('')
    self.obj63374.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj63374.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63374.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj63374.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63374.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63374.MT_pivotIn__.setValue('')
    self.obj63374.MT_pivotIn__.setNone()

    self.obj63374.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(240.0,220.0,self.obj63374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63374.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63374)
    self.globalAndLocalPostcondition(self.obj63374, rootNode)
    self.obj63374.postAction( rootNode.CREATE )

    self.obj63373=MT_pre__Constant(self)
    self.obj63373.isGraphObjectVisual = True

    if(hasattr(self.obj63373, '_setHierarchicalLink')):
      self.obj63373._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63373.MT_pivotOut__.setValue('')
    self.obj63373.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63373.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63373.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj63373.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63373.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj63373.MT_pivotIn__.setValue('')
    self.obj63373.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63373.MT_label__.setValue('5')

    # MT_pre__name
    self.obj63373.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63373.MT_pre__name.setHeight(15)

    self.obj63373.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(240.0,300.0,self.obj63373)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63373.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63373)
    self.globalAndLocalPostcondition(self.obj63373, rootNode)
    self.obj63373.postAction( rootNode.CREATE )

    self.obj63376=MT_pre__hasAttribute_S(self)
    self.obj63376.isGraphObjectVisual = True

    if(hasattr(self.obj63376, '_setHierarchicalLink')):
      self.obj63376._setHierarchicalLink(False)

    # MT_label__
    self.obj63376.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj63376.MT_pivotOut__.setValue('')
    self.obj63376.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63376.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63376.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63376.MT_pivotIn__.setValue('')
    self.obj63376.MT_pivotIn__.setNone()

    self.obj63376.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(258.5,220.0,self.obj63376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63376.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63376)
    self.globalAndLocalPostcondition(self.obj63376, rootNode)
    self.obj63376.postAction( rootNode.CREATE )

    self.obj63377=MT_pre__leftExpr(self)
    self.obj63377.isGraphObjectVisual = True

    if(hasattr(self.obj63377, '_setHierarchicalLink')):
      self.obj63377._setHierarchicalLink(False)

    # MT_label__
    self.obj63377.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj63377.MT_pivotOut__.setValue('')
    self.obj63377.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63377.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63377.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63377.MT_pivotIn__.setValue('')
    self.obj63377.MT_pivotIn__.setNone()

    self.obj63377.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(322.0,289.0,self.obj63377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63377.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63377)
    self.globalAndLocalPostcondition(self.obj63377, rootNode)
    self.obj63377.postAction( rootNode.CREATE )

    self.obj63378=MT_pre__rightExpr(self)
    self.obj63378.isGraphObjectVisual = True

    if(hasattr(self.obj63378, '_setHierarchicalLink')):
      self.obj63378._setHierarchicalLink(False)

    # MT_label__
    self.obj63378.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj63378.MT_pivotOut__.setValue('')
    self.obj63378.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63378.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63378.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63378.MT_pivotIn__.setValue('')
    self.obj63378.MT_pivotIn__.setNone()

    self.obj63378.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(392.0,329.0,self.obj63378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63378.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63378)
    self.globalAndLocalPostcondition(self.obj63378, rootNode)
    self.obj63378.postAction( rootNode.CREATE )

    self.obj63372=LHS(self)
    self.obj63372.isGraphObjectVisual = True

    if(hasattr(self.obj63372, '_setHierarchicalLink')):
      self.obj63372._setHierarchicalLink(False)

    # constraint
    self.obj63372.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'7\')[\'name\']==\'isComposite\')and (PreNode(\'5\')[\'name\']==\'true\'):\n   return True\nreturn False\n')
    self.obj63372.constraint.setHeight(15)

    self.obj63372.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(36.0,20.0,self.obj63372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63372.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63372)
    self.globalAndLocalPostcondition(self.obj63372, rootNode)
    self.obj63372.postAction( rootNode.CREATE )

    # Connections for obj63368 (graphObject_: Obj62) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj63369 (graphObject_: Obj63) of type MT_pre__Transition
    self.drawConnections(
 )
    # Connections for obj63370 (graphObject_: Obj64) of type MT_pre__State
    self.drawConnections(
(self.obj63370,self.obj63376,[257.0, 115.0, 258.5, 220.0],"true", 2) )
    # Connections for obj63371 (graphObject_: Obj65) of type MT_pre__OUT2
    self.drawConnections(
 )
    # Connections for obj63375 (graphObject_: Obj69) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj63374 (graphObject_: Obj68) of type MT_pre__Equation
    self.drawConnections(
(self.obj63374,self.obj63377,[404.0, 293.0, 322.0, 289.0],"true", 2),
(self.obj63374,self.obj63378,[404.0, 293.0, 392.0, 329.0],"true", 2) )
    # Connections for obj63373 (graphObject_: Obj67) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj63376 (graphObject_: Obj70) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj63376,self.obj63375,[258.5, 220.0, 240.0, 285.0],"true", 2) )
    # Connections for obj63377 (graphObject_: Obj71) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj63377,self.obj63375,[322.0, 289.0, 240.0, 285.0],"true", 2) )
    # Connections for obj63378 (graphObject_: Obj72) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj63378,self.obj63373,[392.0, 329.0, 400.0, 365.0],"true", 2) )
    # Connections for obj63372 (graphObject_: Obj66) of type LHS
    self.drawConnections(
 )

newfunction = ExitPtConOPsOfExitPtOUT_Isolated_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
