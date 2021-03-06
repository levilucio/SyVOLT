"""
__nestedStates2nestedProcDefs_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sun Mar  1 14:41:24 2015
__________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__State import *
from MT_pre__ProcDef import *
from MT_pre__LocalDef import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__Constant import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from MT_pre__hasAttribute_S import *
from MT_pre__leftExpr import *
from MT_pre__rightExpr import *
from LHS import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__LocalDef import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__directLink_T import *
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

def nestedStates2nestedProcDefs_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('nestedStates2nestedProcDefs_Complete')
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


    self.obj21183=MT_pre__State(self)
    self.obj21183.isGraphObjectVisual = True

    if(hasattr(self.obj21183, '_setHierarchicalLink')):
      self.obj21183._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21183.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj21183.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21183.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21183.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21183.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21183.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj21183.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj21183.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21183.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21183.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21183.MT_pre__name.setHeight(15)

    self.obj21183.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(100.0,80.0,self.obj21183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21183)
    self.globalAndLocalPostcondition(self.obj21183, rootNode)
    self.obj21183.postAction( rootNode.CREATE )

    self.obj21184=MT_pre__State(self)
    self.obj21184.isGraphObjectVisual = True

    if(hasattr(self.obj21184, '_setHierarchicalLink')):
      self.obj21184._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21184.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj21184.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21184.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21184.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21184.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21184.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj21184.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj21184.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21184.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21184.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21184.MT_pre__name.setHeight(15)

    self.obj21184.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(280.0,80.0,self.obj21184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21184)
    self.globalAndLocalPostcondition(self.obj21184, rootNode)
    self.obj21184.postAction( rootNode.CREATE )

    self.obj42254=MT_pre__ProcDef(self)
    self.obj42254.isGraphObjectVisual = True

    if(hasattr(self.obj42254, '_setHierarchicalLink')):
      self.obj42254._setHierarchicalLink(False)

    # MT_label__
    self.obj42254.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj42254.MT_pivotOut__.setValue('')
    self.obj42254.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42254.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42254.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42254.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42254.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj42254.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42254.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42254.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42254.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj42254.MT_pivotIn__.setValue('')
    self.obj42254.MT_pivotIn__.setNone()

    self.obj42254.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(94.0,239.0,self.obj42254)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42254.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42254)
    self.globalAndLocalPostcondition(self.obj42254, rootNode)
    self.obj42254.postAction( rootNode.CREATE )

    self.obj42256=MT_pre__ProcDef(self)
    self.obj42256.isGraphObjectVisual = True

    if(hasattr(self.obj42256, '_setHierarchicalLink')):
      self.obj42256._setHierarchicalLink(False)

    # MT_label__
    self.obj42256.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj42256.MT_pivotOut__.setValue('')
    self.obj42256.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42256.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42256.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42256.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42256.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj42256.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42256.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42256.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42256.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj42256.MT_pivotIn__.setValue('')
    self.obj42256.MT_pivotIn__.setNone()

    self.obj42256.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(277.0,250.0,self.obj42256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42256.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42256)
    self.globalAndLocalPostcondition(self.obj42256, rootNode)
    self.obj42256.postAction( rootNode.CREATE )

    self.obj42258=MT_pre__LocalDef(self)
    self.obj42258.isGraphObjectVisual = True

    if(hasattr(self.obj42258, '_setHierarchicalLink')):
      self.obj42258._setHierarchicalLink(False)

    # MT_label__
    self.obj42258.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj42258.MT_pivotOut__.setValue('')
    self.obj42258.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42258.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42258.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42258.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42258.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj42258.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42258.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42258.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42258.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj42258.MT_pivotIn__.setValue('')
    self.obj42258.MT_pivotIn__.setNone()

    self.obj42258.graphClass_= graph_MT_pre__LocalDef
    if self.genGraphics:
       new_obj = graph_MT_pre__LocalDef(160.0,312.0,self.obj42258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42258.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42258)
    self.globalAndLocalPostcondition(self.obj42258, rootNode)
    self.obj42258.postAction( rootNode.CREATE )

    self.obj21185=MT_pre__Attribute(self)
    self.obj21185.isGraphObjectVisual = True

    if(hasattr(self.obj21185, '_setHierarchicalLink')):
      self.obj21185._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21185.MT_pivotOut__.setValue('')
    self.obj21185.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21185.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21185.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21185.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21185.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21185.MT_pivotIn__.setValue('')
    self.obj21185.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21185.MT_label__.setValue('3')

    # MT_pre__name
    self.obj21185.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21185.MT_pre__name.setHeight(15)

    self.obj21185.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(96.0,179.0,self.obj21185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21185.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21185)
    self.globalAndLocalPostcondition(self.obj21185, rootNode)
    self.obj21185.postAction( rootNode.CREATE )

    self.obj21187=MT_pre__Equation(self)
    self.obj21187.isGraphObjectVisual = True

    if(hasattr(self.obj21187, '_setHierarchicalLink')):
      self.obj21187._setHierarchicalLink(False)

    # MT_label__
    self.obj21187.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj21187.MT_pivotOut__.setValue('')
    self.obj21187.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj21187.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21187.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj21187.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21187.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21187.MT_pivotIn__.setValue('')
    self.obj21187.MT_pivotIn__.setNone()

    self.obj21187.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(238.0,180.0,self.obj21187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21187)
    self.globalAndLocalPostcondition(self.obj21187, rootNode)
    self.obj21187.postAction( rootNode.CREATE )

    self.obj21189=MT_pre__Constant(self)
    self.obj21189.isGraphObjectVisual = True

    if(hasattr(self.obj21189, '_setHierarchicalLink')):
      self.obj21189._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21189.MT_pivotOut__.setValue('')
    self.obj21189.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21189.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21189.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21189.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21189.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21189.MT_pivotIn__.setValue('')
    self.obj21189.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21189.MT_label__.setValue('7')

    # MT_pre__name
    self.obj21189.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21189.MT_pre__name.setHeight(15)

    self.obj21189.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(376.0,195.0,self.obj21189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21189)
    self.globalAndLocalPostcondition(self.obj21189, rootNode)
    self.obj21189.postAction( rootNode.CREATE )

    self.obj42259=MT_pre__directLink_T(self)
    self.obj42259.isGraphObjectVisual = True

    if(hasattr(self.obj42259, '_setHierarchicalLink')):
      self.obj42259._setHierarchicalLink(False)

    # MT_label__
    self.obj42259.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj42259.MT_pivotOut__.setValue('')
    self.obj42259.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42259.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42259.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42259.MT_pivotIn__.setValue('')
    self.obj42259.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42259.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42259.MT_pre__associationType.setHeight(15)

    self.obj42259.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(440.5,376.0,self.obj42259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42259)
    self.globalAndLocalPostcondition(self.obj42259, rootNode)
    self.obj42259.postAction( rootNode.CREATE )

    self.obj42260=MT_pre__directLink_T(self)
    self.obj42260.isGraphObjectVisual = True

    if(hasattr(self.obj42260, '_setHierarchicalLink')):
      self.obj42260._setHierarchicalLink(False)

    # MT_label__
    self.obj42260.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj42260.MT_pivotOut__.setValue('')
    self.obj42260.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42260.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42260.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42260.MT_pivotIn__.setValue('')
    self.obj42260.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42260.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42260.MT_pre__associationType.setHeight(15)

    self.obj42260.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(349.0,376.5,self.obj42260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42260)
    self.globalAndLocalPostcondition(self.obj42260, rootNode)
    self.obj42260.postAction( rootNode.CREATE )

    self.obj31725=MT_pre__directLink_S(self)
    self.obj31725.isGraphObjectVisual = True

    if(hasattr(self.obj31725, '_setHierarchicalLink')):
      self.obj31725._setHierarchicalLink(False)

    # MT_label__
    self.obj31725.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj31725.MT_pivotOut__.setValue('')
    self.obj31725.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31725.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31725.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31725.MT_pivotIn__.setValue('')
    self.obj31725.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj31725.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31725.MT_pre__associationType.setHeight(15)

    self.obj31725.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(387.0,195.0,self.obj31725)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31725.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31725)
    self.globalAndLocalPostcondition(self.obj31725, rootNode)
    self.obj31725.postAction( rootNode.CREATE )

    self.obj42255=MT_pre__trace_link(self)
    self.obj42255.isGraphObjectVisual = True

    if(hasattr(self.obj42255, '_setHierarchicalLink')):
      self.obj42255._setHierarchicalLink(False)

    # MT_label__
    self.obj42255.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj42255.MT_pivotOut__.setValue('')
    self.obj42255.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42255.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42255.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42255.MT_pivotIn__.setValue('')
    self.obj42255.MT_pivotIn__.setNone()

    self.obj42255.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(306.5,258.0,self.obj42255)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42255.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42255)
    self.globalAndLocalPostcondition(self.obj42255, rootNode)
    self.obj42255.postAction( rootNode.CREATE )

    self.obj42257=MT_pre__trace_link(self)
    self.obj42257.isGraphObjectVisual = True

    if(hasattr(self.obj42257, '_setHierarchicalLink')):
      self.obj42257._setHierarchicalLink(False)

    # MT_label__
    self.obj42257.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj42257.MT_pivotOut__.setValue('')
    self.obj42257.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42257.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42257.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42257.MT_pivotIn__.setValue('')
    self.obj42257.MT_pivotIn__.setNone()

    self.obj42257.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(488.0,253.0,self.obj42257)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42257.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42257)
    self.globalAndLocalPostcondition(self.obj42257, rootNode)
    self.obj42257.postAction( rootNode.CREATE )

    self.obj42261=MT_pre__trace_link(self)
    self.obj42261.isGraphObjectVisual = True

    if(hasattr(self.obj42261, '_setHierarchicalLink')):
      self.obj42261._setHierarchicalLink(False)

    # MT_label__
    self.obj42261.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj42261.MT_pivotOut__.setValue('')
    self.obj42261.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42261.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42261.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42261.MT_pivotIn__.setValue('')
    self.obj42261.MT_pivotIn__.setNone()

    self.obj42261.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(339.5,284.0,self.obj42261)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42261.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42261)
    self.globalAndLocalPostcondition(self.obj42261, rootNode)
    self.obj42261.postAction( rootNode.CREATE )

    self.obj21186=MT_pre__hasAttribute_S(self)
    self.obj21186.isGraphObjectVisual = True

    if(hasattr(self.obj21186, '_setHierarchicalLink')):
      self.obj21186._setHierarchicalLink(False)

    # MT_label__
    self.obj21186.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj21186.MT_pivotOut__.setValue('')
    self.obj21186.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21186.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21186.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21186.MT_pivotIn__.setValue('')
    self.obj21186.MT_pivotIn__.setNone()

    self.obj21186.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(263.5,199.0,self.obj21186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21186)
    self.globalAndLocalPostcondition(self.obj21186, rootNode)
    self.obj21186.postAction( rootNode.CREATE )

    self.obj21188=MT_pre__leftExpr(self)
    self.obj21188.isGraphObjectVisual = True

    if(hasattr(self.obj21188, '_setHierarchicalLink')):
      self.obj21188._setHierarchicalLink(False)

    # MT_label__
    self.obj21188.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj21188.MT_pivotOut__.setValue('')
    self.obj21188.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21188.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21188.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21188.MT_pivotIn__.setValue('')
    self.obj21188.MT_pivotIn__.setNone()

    self.obj21188.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(369.0,250.0,self.obj21188)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21188.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21188)
    self.globalAndLocalPostcondition(self.obj21188, rootNode)
    self.obj21188.postAction( rootNode.CREATE )

    self.obj21190=MT_pre__rightExpr(self)
    self.obj21190.isGraphObjectVisual = True

    if(hasattr(self.obj21190, '_setHierarchicalLink')):
      self.obj21190._setHierarchicalLink(False)

    # MT_label__
    self.obj21190.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj21190.MT_pivotOut__.setValue('')
    self.obj21190.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21190.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21190.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21190.MT_pivotIn__.setValue('')
    self.obj21190.MT_pivotIn__.setNone()

    self.obj21190.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(405.0,208.0,self.obj21190)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21190.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21190)
    self.globalAndLocalPostcondition(self.obj21190, rootNode)
    self.obj21190.postAction( rootNode.CREATE )

    self.obj21182=LHS(self)
    self.obj21182.isGraphObjectVisual = True

    if(hasattr(self.obj21182, '_setHierarchicalLink')):
      self.obj21182._setHierarchicalLink(False)

    # constraint
    self.obj21182.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'3\')[\'name\']==\'isComposite\') and (PreNode(\'7\')[\'name\']==\'true\'):\n   return True\nreturn False\n')
    self.obj21182.constraint.setHeight(15)

    self.obj21182.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,60.0,self.obj21182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21182)
    self.globalAndLocalPostcondition(self.obj21182, rootNode)
    self.obj21182.postAction( rootNode.CREATE )

    # Connections for obj21183 (graphObject_: Obj24) of type MT_pre__State
    self.drawConnections(
(self.obj21183,self.obj21186,[297.0, 155.0, 263.5, 199.0],"true", 2),
(self.obj21183,self.obj31725,[297.0, 155.0, 387.0, 195.0],"true", 2) )
    # Connections for obj21184 (graphObject_: Obj25) of type MT_pre__State
    self.drawConnections(
 )
    # Connections for obj42254 (graphObject_: Obj33) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj42254,self.obj42255,[316.0, 340.0, 306.5, 258.0],"true", 2),
(self.obj42254,self.obj42260,[316.0, 340.0, 349.0, 376.5],"true", 2) )
    # Connections for obj42256 (graphObject_: Obj35) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj42256,self.obj42257,[499.0, 351.0, 488.0, 253.0],"true", 2) )
    # Connections for obj42258 (graphObject_: Obj37) of type MT_pre__LocalDef
    self.drawConnections(
(self.obj42258,self.obj42259,[382.0, 413.0, 440.5, 376.0],"true", 2),
(self.obj42258,self.obj42261,[382.0, 413.0, 339.5, 284.0],"true", 2) )
    # Connections for obj21185 (graphObject_: Obj26) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj21187 (graphObject_: Obj28) of type MT_pre__Equation
    self.drawConnections(
(self.obj21187,self.obj21188,[402.0, 253.0, 369.0, 250.0],"true", 2),
(self.obj21187,self.obj21190,[402.0, 253.0, 405.0, 208.0],"true", 2) )
    # Connections for obj21189 (graphObject_: Obj30) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj42259 (graphObject_: Obj38) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42259,self.obj42256,[440.5, 376.0, 499.0, 351.0],"true", 2) )
    # Connections for obj42260 (graphObject_: Obj39) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42260,self.obj42258,[349.0, 376.5, 382.0, 413.0],"true", 2) )
    # Connections for obj31725 (graphObject_: Obj32) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj31725,self.obj21184,[387.0, 195.0, 477.0, 155.0],"true", 2) )
    # Connections for obj42255 (graphObject_: Obj34) of type MT_pre__trace_link
    self.drawConnections(
(self.obj42255,self.obj21183,[306.5, 258.0, 297.0, 155.0],"true", 2) )
    # Connections for obj42257 (graphObject_: Obj36) of type MT_pre__trace_link
    self.drawConnections(
(self.obj42257,self.obj21184,[488.0, 253.0, 477.0, 155.0],"true", 2) )
    # Connections for obj42261 (graphObject_: Obj40) of type MT_pre__trace_link
    self.drawConnections(
(self.obj42261,self.obj21183,[339.5, 284.0, 297.0, 155.0],"true", 2) )
    # Connections for obj21186 (graphObject_: Obj27) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj21186,self.obj21185,[263.5, 199.0, 256.0, 244.0],"true", 2) )
    # Connections for obj21188 (graphObject_: Obj29) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj21188,self.obj21185,[369.0, 250.0, 256.0, 244.0],"true", 2) )
    # Connections for obj21190 (graphObject_: Obj31) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj21190,self.obj21189,[405.0, 208.0, 536.0, 260.0],"true", 2) )
    # Connections for obj21182 (graphObject_: Obj23) of type LHS
    self.drawConnections(
 )

newfunction = nestedStates2nestedProcDefs_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
