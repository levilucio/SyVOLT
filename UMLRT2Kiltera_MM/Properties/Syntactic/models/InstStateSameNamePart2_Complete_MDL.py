"""
__InstStateSameNamePart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sun Mar  1 11:12:42 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__State import *
from MT_pre__ProcDef import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__Concat import *
from MT_pre__Constant import *
from MT_pre__hasAttribute_S import *
from MT_pre__hasAttribute_T import *
from MT_pre__leftExpr import *
from MT_pre__rightExpr import *
from MT_pre__hasArgs import *
from LHS import *
from graph_MT_pre__Equation import *
from graph_MT_pre__hasArgs import *
from graph_LHS import *
from graph_MT_pre__hasAttribute_T import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__Concat import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__ProcDef import *
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

def InstStateSameNamePart2_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('InstStateSameNamePart2_Complete')
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


    self.obj121=MT_pre__State(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj121.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj121.MT_subtypeMatching__.setValue(('True', 0))
    self.obj121.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj121.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj121.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj121.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj121.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj121.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__name.setHeight(15)

    self.obj121.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj10662=MT_pre__ProcDef(self)
    self.obj10662.isGraphObjectVisual = True

    if(hasattr(self.obj10662, '_setHierarchicalLink')):
      self.obj10662._setHierarchicalLink(False)

    # MT_label__
    self.obj10662.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj10662.MT_pivotOut__.setValue('')
    self.obj10662.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10662.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10662.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10662.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10662.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10662.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10662.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10662.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10662.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10662.MT_pivotIn__.setValue('')
    self.obj10662.MT_pivotIn__.setNone()

    self.obj10662.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(60.0,260.0,self.obj10662)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10662.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10662)
    self.globalAndLocalPostcondition(self.obj10662, rootNode)
    self.obj10662.postAction( rootNode.CREATE )

    self.obj129=MT_pre__Attribute(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('')
    self.obj129.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj129.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('')
    self.obj129.MT_pivotIn__.setNone()

    # MT_label__
    self.obj129.MT_label__.setValue('2')

    # MT_pre__name
    self.obj129.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__name.setHeight(15)

    self.obj129.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,40.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=MT_pre__Attribute(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj130.MT_pivotOut__.setValue('')
    self.obj130.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj130.MT_subtypeMatching__.setValue(('True', 0))
    self.obj130.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj130.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj130.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj130.MT_pivotIn__.setValue('')
    self.obj130.MT_pivotIn__.setNone()

    # MT_label__
    self.obj130.MT_label__.setValue('5')

    # MT_pre__name
    self.obj130.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj130.MT_pre__name.setHeight(15)

    self.obj130.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(280.0,280.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj136=MT_pre__Equation(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # MT_label__
    self.obj136.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj136.MT_pivotOut__.setValue('')
    self.obj136.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj136.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj136.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj136.MT_subtypeMatching__.setValue(('True', 0))
    self.obj136.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj136.MT_pivotIn__.setValue('')
    self.obj136.MT_pivotIn__.setNone()

    self.obj136.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(320.0,200.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj138=MT_pre__Concat(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # MT_label__
    self.obj138.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj138.MT_pivotOut__.setValue('')
    self.obj138.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj138.MT_subtypeMatching__.setValue(('True', 0))
    self.obj138.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj138.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj138.MT_pre__Type.setHeight(15)

    # MT_pre__name
    self.obj138.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj138.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj138.MT_pivotIn__.setValue('')
    self.obj138.MT_pivotIn__.setNone()

    self.obj138.graphClass_= graph_MT_pre__Concat
    if self.genGraphics:
       new_obj = graph_MT_pre__Concat(80.0,200.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj141=MT_pre__Constant(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj141.MT_pivotOut__.setValue('')
    self.obj141.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj141.MT_subtypeMatching__.setValue(('True', 0))
    self.obj141.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj141.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj141.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj141.MT_pivotIn__.setValue('')
    self.obj141.MT_pivotIn__.setNone()

    # MT_label__
    self.obj141.MT_label__.setValue('12')

    # MT_pre__name
    self.obj141.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj141.MT_pre__name.setHeight(15)

    self.obj141.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(280.0,120.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj125=MT_pre__hasAttribute_S(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_label__
    self.obj125.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('')
    self.obj125.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('')
    self.obj125.MT_pivotIn__.setNone()

    self.obj125.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(338.5,110.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj10663=MT_pre__hasAttribute_T(self)
    self.obj10663.isGraphObjectVisual = True

    if(hasattr(self.obj10663, '_setHierarchicalLink')):
      self.obj10663._setHierarchicalLink(False)

    # MT_label__
    self.obj10663.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj10663.MT_pivotOut__.setValue('')
    self.obj10663.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10663.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10663.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10663.MT_pivotIn__.setValue('')
    self.obj10663.MT_pivotIn__.setNone()

    self.obj10663.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(361.0,353.0,self.obj10663)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10663.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10663)
    self.globalAndLocalPostcondition(self.obj10663, rootNode)
    self.obj10663.postAction( rootNode.CREATE )

    self.obj137=MT_pre__leftExpr(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # MT_label__
    self.obj137.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj137.MT_pivotOut__.setValue('')
    self.obj137.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj137.MT_subtypeMatching__.setValue(('True', 0))
    self.obj137.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj137.MT_pivotIn__.setValue('')
    self.obj137.MT_pivotIn__.setNone()

    self.obj137.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(462.0,309.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj139=MT_pre__rightExpr(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    # MT_label__
    self.obj139.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj139.MT_pivotOut__.setValue('')
    self.obj139.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj139.MT_subtypeMatching__.setValue(('True', 0))
    self.obj139.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj139.MT_pivotIn__.setValue('')
    self.obj139.MT_pivotIn__.setNone()

    self.obj139.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(362.0,269.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=MT_pre__hasArgs(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # MT_label__
    self.obj140.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj140.MT_pivotOut__.setValue('')
    self.obj140.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj140.MT_subtypeMatching__.setValue(('True', 0))
    self.obj140.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj140.MT_pivotIn__.setValue('')
    self.obj140.MT_pivotIn__.setNone()

    self.obj140.graphClass_= graph_MT_pre__hasArgs
    if self.genGraphics:
       new_obj = graph_MT_pre__hasArgs(239.0,161.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj142=MT_pre__hasArgs(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    # MT_label__
    self.obj142.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj142.MT_pivotOut__.setValue('')
    self.obj142.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj142.MT_subtypeMatching__.setValue(('True', 0))
    self.obj142.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj142.MT_pivotIn__.setValue('')
    self.obj142.MT_pivotIn__.setNone()

    self.obj142.graphClass_= graph_MT_pre__hasArgs
    if self.genGraphics:
       new_obj = graph_MT_pre__hasArgs(342.5,225.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj120=LHS(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # constraint
    self.obj120.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'5\')[\'name\']==\'name\') and (PreNode(\'12\')[\'name\']==\'S\'):\n   return True\nreturn False\n')
    self.obj120.constraint.setHeight(15)

    self.obj120.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,20.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    # Connections for obj121 (graphObject_: Obj1) of type MT_pre__State
    self.drawConnections(
(self.obj121,self.obj125,[257.0, 115.0, 338.5, 110.0],"true", 2) )
    # Connections for obj10662 (graphObject_: Obj21) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj10662,self.obj10663,[282.0, 361.0, 361.0, 353.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj9) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj130 (graphObject_: Obj10) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj136 (graphObject_: Obj14) of type MT_pre__Equation
    self.drawConnections(
(self.obj136,self.obj137,[484.0, 273.0, 462.0, 309.0],"true", 2),
(self.obj136,self.obj139,[484.0, 273.0, 362.0, 269.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj16) of type MT_pre__Concat
    self.drawConnections(
(self.obj138,self.obj140,[240.0, 265.0, 239.0, 161.0],"true", 2),
(self.obj138,self.obj142,[240.0, 265.0, 342.5, 225.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj19) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj125 (graphObject_: Obj5) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj125,self.obj129,[338.5, 110.0, 420.0, 105.0],"true", 2) )
    # Connections for obj10663 (graphObject_: Obj22) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj10663,self.obj130,[361.0, 353.0, 440.0, 345.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj15) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj137,self.obj130,[462.0, 309.0, 440.0, 345.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj17) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj139,self.obj138,[362.0, 269.0, 240.0, 265.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj18) of type MT_pre__hasArgs
    self.drawConnections(
(self.obj140,self.obj129,[239.0, 161.0, 420.0, 105.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj20) of type MT_pre__hasArgs
    self.drawConnections(
(self.obj142,self.obj141,[342.5, 225.0, 445.0, 185.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = InstStateSameNamePart2_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
