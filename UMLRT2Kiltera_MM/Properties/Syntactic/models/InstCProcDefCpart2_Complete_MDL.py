"""
__InstCProcDefCpart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Mar  6 10:59:44 2015
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ProcDef import *
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
from graph_MT_pre__leftExpr import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__ProcDef import *
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

def InstCProcDefCpart2_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('InstCProcDefCpart2_Complete')
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


    self.obj31708=MT_pre__ProcDef(self)
    self.obj31708.isGraphObjectVisual = True

    if(hasattr(self.obj31708, '_setHierarchicalLink')):
      self.obj31708._setHierarchicalLink(False)

    # MT_label__
    self.obj31708.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj31708.MT_pivotOut__.setValue('')
    self.obj31708.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31708.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31708.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31708.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31708.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj31708.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31708.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31708.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31708.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj31708.MT_pivotIn__.setValue('')
    self.obj31708.MT_pivotIn__.setNone()

    self.obj31708.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(180.0,160.0,self.obj31708)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31708.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31708)
    self.globalAndLocalPostcondition(self.obj31708, rootNode)
    self.obj31708.postAction( rootNode.CREATE )

    self.obj31709=MT_pre__Inst(self)
    self.obj31709.isGraphObjectVisual = True

    if(hasattr(self.obj31709, '_setHierarchicalLink')):
      self.obj31709._setHierarchicalLink(False)

    # MT_label__
    self.obj31709.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj31709.MT_pivotOut__.setValue('')
    self.obj31709.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31709.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31709.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31709.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31709.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj31709.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31709.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31709.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31709.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj31709.MT_pivotIn__.setValue('element1')

    self.obj31709.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(54.0,54.0,self.obj31709)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31709.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31709)
    self.globalAndLocalPostcondition(self.obj31709, rootNode)
    self.obj31709.postAction( rootNode.CREATE )

    self.obj31710=MT_pre__Attribute(self)
    self.obj31710.isGraphObjectVisual = True

    if(hasattr(self.obj31710, '_setHierarchicalLink')):
      self.obj31710._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31710.MT_pivotOut__.setValue('')
    self.obj31710.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31710.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31710.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31710.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31710.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31710.MT_pivotIn__.setValue('')
    self.obj31710.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31710.MT_label__.setValue('2')

    # MT_pre__name
    self.obj31710.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31710.MT_pre__name.setHeight(15)

    self.obj31710.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(54.0,200.0,self.obj31710)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31710.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31710)
    self.globalAndLocalPostcondition(self.obj31710, rootNode)
    self.obj31710.postAction( rootNode.CREATE )

    self.obj31711=MT_pre__Attribute(self)
    self.obj31711.isGraphObjectVisual = True

    if(hasattr(self.obj31711, '_setHierarchicalLink')):
      self.obj31711._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31711.MT_pivotOut__.setValue('')
    self.obj31711.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31711.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31711.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31711.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31711.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31711.MT_pivotIn__.setValue('')
    self.obj31711.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31711.MT_label__.setValue('9')

    # MT_pre__name
    self.obj31711.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31711.MT_pre__name.setHeight(15)

    self.obj31711.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,60.0,self.obj31711)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31711.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31711)
    self.globalAndLocalPostcondition(self.obj31711, rootNode)
    self.obj31711.postAction( rootNode.CREATE )

    self.obj31712=MT_pre__Equation(self)
    self.obj31712.isGraphObjectVisual = True

    if(hasattr(self.obj31712, '_setHierarchicalLink')):
      self.obj31712._setHierarchicalLink(False)

    # MT_label__
    self.obj31712.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj31712.MT_pivotOut__.setValue('')
    self.obj31712.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj31712.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31712.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj31712.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31712.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31712.MT_pivotIn__.setValue('')
    self.obj31712.MT_pivotIn__.setNone()

    self.obj31712.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(55.0,322.0,self.obj31712)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31712.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31712)
    self.globalAndLocalPostcondition(self.obj31712, rootNode)
    self.obj31712.postAction( rootNode.CREATE )

    self.obj31713=MT_pre__Equation(self)
    self.obj31713.isGraphObjectVisual = True

    if(hasattr(self.obj31713, '_setHierarchicalLink')):
      self.obj31713._setHierarchicalLink(False)

    # MT_label__
    self.obj31713.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj31713.MT_pivotOut__.setValue('')
    self.obj31713.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj31713.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31713.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj31713.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31713.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31713.MT_pivotIn__.setValue('')
    self.obj31713.MT_pivotIn__.setNone()

    self.obj31713.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(320.0,200.0,self.obj31713)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31713.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31713)
    self.globalAndLocalPostcondition(self.obj31713, rootNode)
    self.obj31713.postAction( rootNode.CREATE )

    self.obj31714=MT_pre__Constant(self)
    self.obj31714.isGraphObjectVisual = True

    if(hasattr(self.obj31714, '_setHierarchicalLink')):
      self.obj31714._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31714.MT_pivotOut__.setValue('')
    self.obj31714.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31714.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31714.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31714.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31714.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31714.MT_pivotIn__.setValue('')
    self.obj31714.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31714.MT_label__.setValue('3')

    # MT_pre__name
    self.obj31714.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31714.MT_pre__name.setHeight(15)

    self.obj31714.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(220.0,320.0,self.obj31714)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31714.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31714)
    self.globalAndLocalPostcondition(self.obj31714, rootNode)
    self.obj31714.postAction( rootNode.CREATE )

    self.obj31715=MT_pre__Constant(self)
    self.obj31715.isGraphObjectVisual = True

    if(hasattr(self.obj31715, '_setHierarchicalLink')):
      self.obj31715._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31715.MT_pivotOut__.setValue('')
    self.obj31715.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31715.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31715.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj31715.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31715.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj31715.MT_pivotIn__.setValue('')
    self.obj31715.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31715.MT_label__.setValue('13')

    # MT_pre__name
    self.obj31715.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31715.MT_pre__name.setHeight(15)

    self.obj31715.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(280.0,300.0,self.obj31715)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31715.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31715)
    self.globalAndLocalPostcondition(self.obj31715, rootNode)
    self.obj31715.postAction( rootNode.CREATE )

    self.obj31716=MT_pre__hasAttribute_T(self)
    self.obj31716.isGraphObjectVisual = True

    if(hasattr(self.obj31716, '_setHierarchicalLink')):
      self.obj31716._setHierarchicalLink(False)

    # MT_label__
    self.obj31716.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj31716.MT_pivotOut__.setValue('')
    self.obj31716.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31716.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31716.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31716.MT_pivotIn__.setValue('')
    self.obj31716.MT_pivotIn__.setNone()

    self.obj31716.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(175.5,215.0,self.obj31716)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31716.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31716)
    self.globalAndLocalPostcondition(self.obj31716, rootNode)
    self.obj31716.postAction( rootNode.CREATE )

    self.obj31717=MT_pre__hasAttribute_T(self)
    self.obj31717.isGraphObjectVisual = True

    if(hasattr(self.obj31717, '_setHierarchicalLink')):
      self.obj31717._setHierarchicalLink(False)

    # MT_label__
    self.obj31717.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj31717.MT_pivotOut__.setValue('')
    self.obj31717.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31717.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31717.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31717.MT_pivotIn__.setValue('')
    self.obj31717.MT_pivotIn__.setNone()

    self.obj31717.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(408.5,213.0,self.obj31717)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31717.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31717)
    self.globalAndLocalPostcondition(self.obj31717, rootNode)
    self.obj31717.postAction( rootNode.CREATE )

    self.obj31718=MT_pre__leftExpr(self)
    self.obj31718.isGraphObjectVisual = True

    if(hasattr(self.obj31718, '_setHierarchicalLink')):
      self.obj31718._setHierarchicalLink(False)

    # MT_label__
    self.obj31718.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj31718.MT_pivotOut__.setValue('')
    self.obj31718.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31718.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31718.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31718.MT_pivotIn__.setValue('')
    self.obj31718.MT_pivotIn__.setNone()

    self.obj31718.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(180.0,320.0,self.obj31718)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31718.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31718)
    self.globalAndLocalPostcondition(self.obj31718, rootNode)
    self.obj31718.postAction( rootNode.CREATE )

    self.obj31719=MT_pre__leftExpr(self)
    self.obj31719.isGraphObjectVisual = True

    if(hasattr(self.obj31719, '_setHierarchicalLink')):
      self.obj31719._setHierarchicalLink(False)

    # MT_label__
    self.obj31719.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj31719.MT_pivotOut__.setValue('')
    self.obj31719.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31719.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31719.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31719.MT_pivotIn__.setValue('')
    self.obj31719.MT_pivotIn__.setNone()

    self.obj31719.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(464.5,219.0,self.obj31719)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31719.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31719)
    self.globalAndLocalPostcondition(self.obj31719, rootNode)
    self.obj31719.postAction( rootNode.CREATE )

    self.obj31720=MT_pre__rightExpr(self)
    self.obj31720.isGraphObjectVisual = True

    if(hasattr(self.obj31720, '_setHierarchicalLink')):
      self.obj31720._setHierarchicalLink(False)

    # MT_label__
    self.obj31720.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj31720.MT_pivotOut__.setValue('')
    self.obj31720.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31720.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31720.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31720.MT_pivotIn__.setValue('')
    self.obj31720.MT_pivotIn__.setNone()

    self.obj31720.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(398.0,418.0,self.obj31720)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31720.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31720)
    self.globalAndLocalPostcondition(self.obj31720, rootNode)
    self.obj31720.postAction( rootNode.CREATE )

    self.obj31721=MT_pre__rightExpr(self)
    self.obj31721.isGraphObjectVisual = True

    if(hasattr(self.obj31721, '_setHierarchicalLink')):
      self.obj31721._setHierarchicalLink(False)

    # MT_label__
    self.obj31721.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj31721.MT_pivotOut__.setValue('')
    self.obj31721.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31721.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31721.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31721.MT_pivotIn__.setValue('')
    self.obj31721.MT_pivotIn__.setNone()

    self.obj31721.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(467.0,319.0,self.obj31721)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31721.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31721)
    self.globalAndLocalPostcondition(self.obj31721, rootNode)
    self.obj31721.postAction( rootNode.CREATE )

    self.obj31722=LHS(self)
    self.obj31722.isGraphObjectVisual = True

    if(hasattr(self.obj31722, '_setHierarchicalLink')):
      self.obj31722._setHierarchicalLink(False)

    # constraint
    self.obj31722.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'3\')[\'name\']==\'C\') and (PreNode(\'9\')[\'name\']==\'name\') and (PreNode(\'13\')[\'name\']==\'C\'):\n   return True\nreturn False\n')
    self.obj31722.constraint.setHeight(15)

    self.obj31722.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,40.0,self.obj31722)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31722.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31722)
    self.globalAndLocalPostcondition(self.obj31722, rootNode)
    self.obj31722.postAction( rootNode.CREATE )

    # Connections for obj31708 (graphObject_: Obj23) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj31708,self.obj31717,[397.0, 261.0, 408.5, 213.0],"true", 2) )
    # Connections for obj31709 (graphObject_: Obj24) of type MT_pre__Inst
    self.drawConnections(
(self.obj31709,self.obj31716,[271.0, 155.0, 175.5, 215.0],"true", 2) )
    # Connections for obj31710 (graphObject_: Obj25) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj31711 (graphObject_: Obj26) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj31712 (graphObject_: Obj27) of type MT_pre__Equation
    self.drawConnections(
(self.obj31712,self.obj31718,[219.0, 395.0, 180.0, 320.0],"true", 2),
(self.obj31712,self.obj31720,[219.0, 395.0, 398.0, 418.0],"true", 2) )
    # Connections for obj31713 (graphObject_: Obj28) of type MT_pre__Equation
    self.drawConnections(
(self.obj31713,self.obj31719,[489.0, 273.0, 464.5, 219.0],"true", 2),
(self.obj31713,self.obj31721,[489.0, 273.0, 467.0, 319.0],"true", 2) )
    # Connections for obj31714 (graphObject_: Obj29) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj31715 (graphObject_: Obj30) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj31716 (graphObject_: Obj31) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj31716,self.obj31710,[175.5, 215.0, 214.0, 265.0],"true", 2) )
    # Connections for obj31717 (graphObject_: Obj32) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj31717,self.obj31711,[408.5, 213.0, 420.0, 125.0],"true", 2) )
    # Connections for obj31718 (graphObject_: Obj33) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj31718,self.obj31710,[180.0, 320.0, 214.0, 265.0],"true", 2) )
    # Connections for obj31719 (graphObject_: Obj34) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj31719,self.obj31711,[464.5, 219.0, 420.0, 125.0],"true", 2) )
    # Connections for obj31720 (graphObject_: Obj35) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj31720,self.obj31714,[398.0, 418.0, 380.0, 385.0],"true", 2) )
    # Connections for obj31721 (graphObject_: Obj36) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj31721,self.obj31715,[467.0, 319.0, 445.0, 365.0],"true", 2) )
    # Connections for obj31722 (graphObject_: Obj37) of type LHS
    self.drawConnections(
 )

newfunction = InstCProcDefCpart2_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
