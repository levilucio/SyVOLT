"""
__ExitPtConOPsOfExitPtOUT_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 18:03:19 2015
_______________________________________________________________________________________________
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
from MT_pre__directLink_S import *
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
from graph_MT_pre__directLink_S import *
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

def ExitPtConOPsOfExitPtOUT_Connected_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ExitPtConOPsOfExitPtOUT_Connected')
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


    self.obj52840=MT_pre__ExitPoint(self)
    self.obj52840.isGraphObjectVisual = True

    if(hasattr(self.obj52840, '_setHierarchicalLink')):
      self.obj52840._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52840.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj52840.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52840.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52840.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52840.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52840.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj52840.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj52840.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52840.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52840.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52840.MT_pre__name.setHeight(15)

    self.obj52840.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(233.0,40.0,self.obj52840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52840)
    self.globalAndLocalPostcondition(self.obj52840, rootNode)
    self.obj52840.postAction( rootNode.CREATE )

    self.obj52841=MT_pre__Transition(self)
    self.obj52841.isGraphObjectVisual = True

    if(hasattr(self.obj52841, '_setHierarchicalLink')):
      self.obj52841._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52841.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj52841.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52841.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52841.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52841.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52841.MT_pivotIn__.setValue('element3')

    # MT_label__
    self.obj52841.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj52841.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52841.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52841.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52841.MT_pre__name.setHeight(15)

    self.obj52841.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(260.0,140.0,self.obj52841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52841)
    self.globalAndLocalPostcondition(self.obj52841, rootNode)
    self.obj52841.postAction( rootNode.CREATE )

    self.obj52842=MT_pre__State(self)
    self.obj52842.isGraphObjectVisual = True

    if(hasattr(self.obj52842, '_setHierarchicalLink')):
      self.obj52842._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52842.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj52842.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52842.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52842.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52842.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52842.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj52842.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj52842.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52842.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52842.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52842.MT_pre__name.setHeight(15)

    self.obj52842.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj52842)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52842.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52842)
    self.globalAndLocalPostcondition(self.obj52842, rootNode)
    self.obj52842.postAction( rootNode.CREATE )

    self.obj52843=MT_pre__OUT2(self)
    self.obj52843.isGraphObjectVisual = True

    if(hasattr(self.obj52843, '_setHierarchicalLink')):
      self.obj52843._setHierarchicalLink(False)

    # MT_label__
    self.obj52843.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj52843.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj52843.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52843.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52843.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52843.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj52843.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52843.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52843.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52843.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj52843.MT_pivotIn__.setValue('element4')

    self.obj52843.graphClass_= graph_MT_pre__OUT2
    if self.genGraphics:
       new_obj = graph_MT_pre__OUT2(60.0,129.0,self.obj52843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52843)
    self.globalAndLocalPostcondition(self.obj52843, rootNode)
    self.obj52843.postAction( rootNode.CREATE )

    self.obj52848=MT_pre__Attribute(self)
    self.obj52848.isGraphObjectVisual = True

    if(hasattr(self.obj52848, '_setHierarchicalLink')):
      self.obj52848._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52848.MT_pivotOut__.setValue('')
    self.obj52848.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52848.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52848.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj52848.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52848.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj52848.MT_pivotIn__.setValue('')
    self.obj52848.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52848.MT_label__.setValue('8')

    # MT_pre__name
    self.obj52848.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52848.MT_pre__name.setHeight(15)

    self.obj52848.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(60.0,240.0,self.obj52848)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52848.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52848)
    self.globalAndLocalPostcondition(self.obj52848, rootNode)
    self.obj52848.postAction( rootNode.CREATE )

    self.obj52850=MT_pre__Equation(self)
    self.obj52850.isGraphObjectVisual = True

    if(hasattr(self.obj52850, '_setHierarchicalLink')):
      self.obj52850._setHierarchicalLink(False)

    # MT_label__
    self.obj52850.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj52850.MT_pivotOut__.setValue('')
    self.obj52850.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj52850.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52850.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj52850.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52850.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52850.MT_pivotIn__.setValue('')
    self.obj52850.MT_pivotIn__.setNone()

    self.obj52850.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(220.0,240.0,self.obj52850)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52850.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52850)
    self.globalAndLocalPostcondition(self.obj52850, rootNode)
    self.obj52850.postAction( rootNode.CREATE )

    self.obj52852=MT_pre__Constant(self)
    self.obj52852.isGraphObjectVisual = True

    if(hasattr(self.obj52852, '_setHierarchicalLink')):
      self.obj52852._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52852.MT_pivotOut__.setValue('')
    self.obj52852.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52852.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52852.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj52852.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52852.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj52852.MT_pivotIn__.setValue('')
    self.obj52852.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52852.MT_label__.setValue('12')

    # MT_pre__name
    self.obj52852.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52852.MT_pre__name.setHeight(15)

    self.obj52852.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(220.0,300.0,self.obj52852)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52852.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52852)
    self.globalAndLocalPostcondition(self.obj52852, rootNode)
    self.obj52852.postAction( rootNode.CREATE )

    self.obj52844=MT_pre__directLink_S(self)
    self.obj52844.isGraphObjectVisual = True

    if(hasattr(self.obj52844, '_setHierarchicalLink')):
      self.obj52844._setHierarchicalLink(False)

    # MT_label__
    self.obj52844.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj52844.MT_pivotOut__.setValue('')
    self.obj52844.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52844.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52844.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52844.MT_pivotIn__.setValue('')
    self.obj52844.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52844.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52844.MT_pre__associationType.setHeight(15)

    self.obj52844.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(344.5,115.0,self.obj52844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52844)
    self.globalAndLocalPostcondition(self.obj52844, rootNode)
    self.obj52844.postAction( rootNode.CREATE )

    self.obj52845=MT_pre__directLink_S(self)
    self.obj52845.isGraphObjectVisual = True

    if(hasattr(self.obj52845, '_setHierarchicalLink')):
      self.obj52845._setHierarchicalLink(False)

    # MT_label__
    self.obj52845.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj52845.MT_pivotOut__.setValue('')
    self.obj52845.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52845.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52845.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52845.MT_pivotIn__.setValue('')
    self.obj52845.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52845.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52845.MT_pre__associationType.setHeight(15)

    self.obj52845.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(453.0,159.0,self.obj52845)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52845.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52845)
    self.globalAndLocalPostcondition(self.obj52845, rootNode)
    self.obj52845.postAction( rootNode.CREATE )

    self.obj52846=MT_pre__directLink_S(self)
    self.obj52846.isGraphObjectVisual = True

    if(hasattr(self.obj52846, '_setHierarchicalLink')):
      self.obj52846._setHierarchicalLink(False)

    # MT_label__
    self.obj52846.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj52846.MT_pivotOut__.setValue('')
    self.obj52846.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52846.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52846.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52846.MT_pivotIn__.setValue('')
    self.obj52846.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52846.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52846.MT_pre__associationType.setHeight(15)

    self.obj52846.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(365.5,203.5,self.obj52846)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52846.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52846)
    self.globalAndLocalPostcondition(self.obj52846, rootNode)
    self.obj52846.postAction( rootNode.CREATE )

    self.obj52849=MT_pre__hasAttribute_S(self)
    self.obj52849.isGraphObjectVisual = True

    if(hasattr(self.obj52849, '_setHierarchicalLink')):
      self.obj52849._setHierarchicalLink(False)

    # MT_label__
    self.obj52849.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj52849.MT_pivotOut__.setValue('')
    self.obj52849.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52849.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52849.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52849.MT_pivotIn__.setValue('')
    self.obj52849.MT_pivotIn__.setNone()

    self.obj52849.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(238.5,210.0,self.obj52849)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52849.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52849)
    self.globalAndLocalPostcondition(self.obj52849, rootNode)
    self.obj52849.postAction( rootNode.CREATE )

    self.obj52851=MT_pre__leftExpr(self)
    self.obj52851.isGraphObjectVisual = True

    if(hasattr(self.obj52851, '_setHierarchicalLink')):
      self.obj52851._setHierarchicalLink(False)

    # MT_label__
    self.obj52851.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj52851.MT_pivotOut__.setValue('')
    self.obj52851.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52851.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52851.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52851.MT_pivotIn__.setValue('')
    self.obj52851.MT_pivotIn__.setNone()

    self.obj52851.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(304.5,309.0,self.obj52851)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52851.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52851)
    self.globalAndLocalPostcondition(self.obj52851, rootNode)
    self.obj52851.postAction( rootNode.CREATE )

    self.obj52853=MT_pre__rightExpr(self)
    self.obj52853.isGraphObjectVisual = True

    if(hasattr(self.obj52853, '_setHierarchicalLink')):
      self.obj52853._setHierarchicalLink(False)

    # MT_label__
    self.obj52853.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj52853.MT_pivotOut__.setValue('')
    self.obj52853.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52853.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52853.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52853.MT_pivotIn__.setValue('')
    self.obj52853.MT_pivotIn__.setNone()

    self.obj52853.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(387.0,339.0,self.obj52853)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52853.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52853)
    self.globalAndLocalPostcondition(self.obj52853, rootNode)
    self.obj52853.postAction( rootNode.CREATE )

    self.obj52847=LHS(self)
    self.obj52847.isGraphObjectVisual = True

    if(hasattr(self.obj52847, '_setHierarchicalLink')):
      self.obj52847._setHierarchicalLink(False)

    # constraint
    self.obj52847.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'8\')[\'name\']==\'isComposite\')and (PreNode(\'12\')[\'name\']==\'true\'):\n   return True\nreturn False\n')
    self.obj52847.constraint.setHeight(15)

    self.obj52847.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(36.0,20.0,self.obj52847)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52847.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52847)
    self.globalAndLocalPostcondition(self.obj52847, rootNode)
    self.obj52847.postAction( rootNode.CREATE )

    # Connections for obj52840 (graphObject_: Obj48) of type MT_pre__ExitPoint
    self.drawConnections(
(self.obj52840,self.obj52845,[430.0, 115.0, 453.0, 159.0],"true", 2) )
    # Connections for obj52841 (graphObject_: Obj49) of type MT_pre__Transition
    self.drawConnections(
(self.obj52841,self.obj52846,[457.0, 215.0, 365.5, 203.5],"true", 2) )
    # Connections for obj52842 (graphObject_: Obj50) of type MT_pre__State
    self.drawConnections(
(self.obj52842,self.obj52844,[257.0, 115.0, 344.5, 115.0],"true", 2),
(self.obj52842,self.obj52849,[257.0, 115.0, 238.5, 210.0],"true", 2) )
    # Connections for obj52843 (graphObject_: Obj51) of type MT_pre__OUT2
    self.drawConnections(
 )
    # Connections for obj52848 (graphObject_: Obj56) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj52850 (graphObject_: Obj58) of type MT_pre__Equation
    self.drawConnections(
(self.obj52850,self.obj52851,[389.0, 313.0, 304.5, 309.0],"true", 2),
(self.obj52850,self.obj52853,[389.0, 313.0, 387.0, 339.0],"true", 2) )
    # Connections for obj52852 (graphObject_: Obj60) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj52844 (graphObject_: Obj52) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52844,self.obj52840,[344.5, 115.0, 430.0, 115.0],"true", 2) )
    # Connections for obj52845 (graphObject_: Obj53) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52845,self.obj52841,[453.0, 159.0, 457.0, 215.0],"true", 2) )
    # Connections for obj52846 (graphObject_: Obj54) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52846,self.obj52843,[365.5, 203.5, 257.0, 204.0],"true", 2) )
    # Connections for obj52849 (graphObject_: Obj57) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj52849,self.obj52848,[238.5, 210.0, 220.0, 305.0],"true", 2) )
    # Connections for obj52851 (graphObject_: Obj59) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj52851,self.obj52848,[304.5, 309.0, 220.0, 305.0],"true", 2) )
    # Connections for obj52853 (graphObject_: Obj61) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj52853,self.obj52852,[387.0, 339.0, 385.0, 365.0],"true", 2) )
    # Connections for obj52847 (graphObject_: Obj55) of type LHS
    self.drawConnections(
 )

newfunction = ExitPtConOPsOfExitPtOUT_Connected_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
