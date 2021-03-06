"""
__HInstProcDefParamspart3_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Mar  6 16:55:08 2015
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ProcDef import *
from MT_pre__Name import *
from MT_pre__Inst import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__Constant import *
from MT_pre__directLink_T import *
from MT_pre__hasAttribute_T import *
from MT_pre__leftExpr import *
from MT_pre__rightExpr import *
from LHS import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__hasAttribute_T import *
from graph_MT_pre__Name import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Constant import *
from graph_MT_pre__rightExpr import *
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

def HInstProcDefParamspart3_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('HInstProcDefParamspart3_Complete')
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


    self.obj63289=MT_pre__ProcDef(self)
    self.obj63289.isGraphObjectVisual = True

    if(hasattr(self.obj63289, '_setHierarchicalLink')):
      self.obj63289._setHierarchicalLink(False)

    # MT_label__
    self.obj63289.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj63289.MT_pivotOut__.setValue('')
    self.obj63289.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63289.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63289.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63289.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63289.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63289.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63289.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63289.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63289.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63289.MT_pivotIn__.setValue('')
    self.obj63289.MT_pivotIn__.setNone()

    self.obj63289.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(180.0,160.0,self.obj63289)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63289.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63289)
    self.globalAndLocalPostcondition(self.obj63289, rootNode)
    self.obj63289.postAction( rootNode.CREATE )

    self.obj63319=MT_pre__Name(self)
    self.obj63319.isGraphObjectVisual = True

    if(hasattr(self.obj63319, '_setHierarchicalLink')):
      self.obj63319._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63319.MT_pivotOut__.setValue('')
    self.obj63319.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63319.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63319.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63319.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63319.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63319.MT_pivotIn__.setValue('')
    self.obj63319.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63319.MT_label__.setValue('15')

    # MT_pre__cardinality
    self.obj63319.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63319.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63319.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63319.MT_pre__name.setHeight(15)

    self.obj63319.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(100.0,60.0,self.obj63319)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63319.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63319)
    self.globalAndLocalPostcondition(self.obj63319, rootNode)
    self.obj63319.postAction( rootNode.CREATE )

    self.obj63321=MT_pre__Name(self)
    self.obj63321.isGraphObjectVisual = True

    if(hasattr(self.obj63321, '_setHierarchicalLink')):
      self.obj63321._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63321.MT_pivotOut__.setValue('')
    self.obj63321.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63321.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63321.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63321.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63321.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63321.MT_pivotIn__.setValue('')
    self.obj63321.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63321.MT_label__.setValue('17')

    # MT_pre__cardinality
    self.obj63321.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63321.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63321.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63321.MT_pre__name.setHeight(15)

    self.obj63321.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(180.0,60.0,self.obj63321)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63321.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63321)
    self.globalAndLocalPostcondition(self.obj63321, rootNode)
    self.obj63321.postAction( rootNode.CREATE )

    self.obj63323=MT_pre__Name(self)
    self.obj63323.isGraphObjectVisual = True

    if(hasattr(self.obj63323, '_setHierarchicalLink')):
      self.obj63323._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63323.MT_pivotOut__.setValue('')
    self.obj63323.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63323.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63323.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63323.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63323.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63323.MT_pivotIn__.setValue('')
    self.obj63323.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63323.MT_label__.setValue('19')

    # MT_pre__cardinality
    self.obj63323.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63323.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63323.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63323.MT_pre__name.setHeight(15)

    self.obj63323.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(60.0,120.0,self.obj63323)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63323.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63323)
    self.globalAndLocalPostcondition(self.obj63323, rootNode)
    self.obj63323.postAction( rootNode.CREATE )

    self.obj63290=MT_pre__Inst(self)
    self.obj63290.isGraphObjectVisual = True

    if(hasattr(self.obj63290, '_setHierarchicalLink')):
      self.obj63290._setHierarchicalLink(False)

    # MT_label__
    self.obj63290.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj63290.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj63290.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63290.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63290.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63290.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63290.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63290.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63290.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63290.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63290.MT_pivotIn__.setValue('element1')

    self.obj63290.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(54.0,54.0,self.obj63290)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63290.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63290)
    self.globalAndLocalPostcondition(self.obj63290, rootNode)
    self.obj63290.postAction( rootNode.CREATE )

    self.obj63291=MT_pre__Attribute(self)
    self.obj63291.isGraphObjectVisual = True

    if(hasattr(self.obj63291, '_setHierarchicalLink')):
      self.obj63291._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63291.MT_pivotOut__.setValue('')
    self.obj63291.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63291.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63291.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj63291.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63291.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj63291.MT_pivotIn__.setValue('')
    self.obj63291.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63291.MT_label__.setValue('2')

    # MT_pre__name
    self.obj63291.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63291.MT_pre__name.setHeight(15)

    self.obj63291.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(54.0,200.0,self.obj63291)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63291.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63291)
    self.globalAndLocalPostcondition(self.obj63291, rootNode)
    self.obj63291.postAction( rootNode.CREATE )

    self.obj63292=MT_pre__Attribute(self)
    self.obj63292.isGraphObjectVisual = True

    if(hasattr(self.obj63292, '_setHierarchicalLink')):
      self.obj63292._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63292.MT_pivotOut__.setValue('')
    self.obj63292.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63292.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63292.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj63292.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63292.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj63292.MT_pivotIn__.setValue('')
    self.obj63292.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63292.MT_label__.setValue('9')

    # MT_pre__name
    self.obj63292.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63292.MT_pre__name.setHeight(15)

    self.obj63292.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,60.0,self.obj63292)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63292.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63292)
    self.globalAndLocalPostcondition(self.obj63292, rootNode)
    self.obj63292.postAction( rootNode.CREATE )

    self.obj63293=MT_pre__Equation(self)
    self.obj63293.isGraphObjectVisual = True

    if(hasattr(self.obj63293, '_setHierarchicalLink')):
      self.obj63293._setHierarchicalLink(False)

    # MT_label__
    self.obj63293.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj63293.MT_pivotOut__.setValue('')
    self.obj63293.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj63293.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63293.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj63293.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63293.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63293.MT_pivotIn__.setValue('')
    self.obj63293.MT_pivotIn__.setNone()

    self.obj63293.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(55.0,322.0,self.obj63293)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63293.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63293)
    self.globalAndLocalPostcondition(self.obj63293, rootNode)
    self.obj63293.postAction( rootNode.CREATE )

    self.obj63294=MT_pre__Equation(self)
    self.obj63294.isGraphObjectVisual = True

    if(hasattr(self.obj63294, '_setHierarchicalLink')):
      self.obj63294._setHierarchicalLink(False)

    # MT_label__
    self.obj63294.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj63294.MT_pivotOut__.setValue('')
    self.obj63294.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj63294.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63294.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj63294.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63294.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63294.MT_pivotIn__.setValue('')
    self.obj63294.MT_pivotIn__.setNone()

    self.obj63294.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(320.0,200.0,self.obj63294)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63294.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63294)
    self.globalAndLocalPostcondition(self.obj63294, rootNode)
    self.obj63294.postAction( rootNode.CREATE )

    self.obj63295=MT_pre__Constant(self)
    self.obj63295.isGraphObjectVisual = True

    if(hasattr(self.obj63295, '_setHierarchicalLink')):
      self.obj63295._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63295.MT_pivotOut__.setValue('')
    self.obj63295.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63295.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63295.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj63295.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63295.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj63295.MT_pivotIn__.setValue('')
    self.obj63295.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63295.MT_label__.setValue('3')

    # MT_pre__name
    self.obj63295.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63295.MT_pre__name.setHeight(15)

    self.obj63295.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(220.0,320.0,self.obj63295)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63295.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63295)
    self.globalAndLocalPostcondition(self.obj63295, rootNode)
    self.obj63295.postAction( rootNode.CREATE )

    self.obj63296=MT_pre__Constant(self)
    self.obj63296.isGraphObjectVisual = True

    if(hasattr(self.obj63296, '_setHierarchicalLink')):
      self.obj63296._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63296.MT_pivotOut__.setValue('')
    self.obj63296.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63296.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63296.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj63296.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63296.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj63296.MT_pivotIn__.setValue('')
    self.obj63296.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63296.MT_label__.setValue('13')

    # MT_pre__name
    self.obj63296.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63296.MT_pre__name.setHeight(15)

    self.obj63296.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(280.0,300.0,self.obj63296)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63296.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63296)
    self.globalAndLocalPostcondition(self.obj63296, rootNode)
    self.obj63296.postAction( rootNode.CREATE )

    self.obj63320=MT_pre__directLink_T(self)
    self.obj63320.isGraphObjectVisual = True

    if(hasattr(self.obj63320, '_setHierarchicalLink')):
      self.obj63320._setHierarchicalLink(False)

    # MT_label__
    self.obj63320.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj63320.MT_pivotOut__.setValue('')
    self.obj63320.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63320.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63320.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63320.MT_pivotIn__.setValue('')
    self.obj63320.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63320.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63320.MT_pre__associationType.setHeight(15)

    self.obj63320.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(359.5,211.0,self.obj63320)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63320.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63320)
    self.globalAndLocalPostcondition(self.obj63320, rootNode)
    self.obj63320.postAction( rootNode.CREATE )

    self.obj63322=MT_pre__directLink_T(self)
    self.obj63322.isGraphObjectVisual = True

    if(hasattr(self.obj63322, '_setHierarchicalLink')):
      self.obj63322._setHierarchicalLink(False)

    # MT_label__
    self.obj63322.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj63322.MT_pivotOut__.setValue('')
    self.obj63322.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63322.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63322.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63322.MT_pivotIn__.setValue('')
    self.obj63322.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63322.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63322.MT_pre__associationType.setHeight(15)

    self.obj63322.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(399.5,211.0,self.obj63322)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63322.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63322)
    self.globalAndLocalPostcondition(self.obj63322, rootNode)
    self.obj63322.postAction( rootNode.CREATE )

    self.obj63324=MT_pre__directLink_T(self)
    self.obj63324.isGraphObjectVisual = True

    if(hasattr(self.obj63324, '_setHierarchicalLink')):
      self.obj63324._setHierarchicalLink(False)

    # MT_label__
    self.obj63324.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj63324.MT_pivotOut__.setValue('')
    self.obj63324.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63324.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63324.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63324.MT_pivotIn__.setValue('')
    self.obj63324.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63324.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63324.MT_pre__associationType.setHeight(15)

    self.obj63324.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(339.5,241.0,self.obj63324)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63324.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63324)
    self.globalAndLocalPostcondition(self.obj63324, rootNode)
    self.obj63324.postAction( rootNode.CREATE )

    self.obj63297=MT_pre__hasAttribute_T(self)
    self.obj63297.isGraphObjectVisual = True

    if(hasattr(self.obj63297, '_setHierarchicalLink')):
      self.obj63297._setHierarchicalLink(False)

    # MT_label__
    self.obj63297.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj63297.MT_pivotOut__.setValue('')
    self.obj63297.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63297.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63297.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63297.MT_pivotIn__.setValue('')
    self.obj63297.MT_pivotIn__.setNone()

    self.obj63297.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(175.5,215.0,self.obj63297)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63297.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63297)
    self.globalAndLocalPostcondition(self.obj63297, rootNode)
    self.obj63297.postAction( rootNode.CREATE )

    self.obj63298=MT_pre__hasAttribute_T(self)
    self.obj63298.isGraphObjectVisual = True

    if(hasattr(self.obj63298, '_setHierarchicalLink')):
      self.obj63298._setHierarchicalLink(False)

    # MT_label__
    self.obj63298.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj63298.MT_pivotOut__.setValue('')
    self.obj63298.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63298.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63298.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63298.MT_pivotIn__.setValue('')
    self.obj63298.MT_pivotIn__.setNone()

    self.obj63298.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(408.5,213.0,self.obj63298)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63298.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63298)
    self.globalAndLocalPostcondition(self.obj63298, rootNode)
    self.obj63298.postAction( rootNode.CREATE )

    self.obj63299=MT_pre__leftExpr(self)
    self.obj63299.isGraphObjectVisual = True

    if(hasattr(self.obj63299, '_setHierarchicalLink')):
      self.obj63299._setHierarchicalLink(False)

    # MT_label__
    self.obj63299.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj63299.MT_pivotOut__.setValue('')
    self.obj63299.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63299.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63299.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63299.MT_pivotIn__.setValue('')
    self.obj63299.MT_pivotIn__.setNone()

    self.obj63299.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(180.0,320.0,self.obj63299)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63299.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63299)
    self.globalAndLocalPostcondition(self.obj63299, rootNode)
    self.obj63299.postAction( rootNode.CREATE )

    self.obj63300=MT_pre__leftExpr(self)
    self.obj63300.isGraphObjectVisual = True

    if(hasattr(self.obj63300, '_setHierarchicalLink')):
      self.obj63300._setHierarchicalLink(False)

    # MT_label__
    self.obj63300.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj63300.MT_pivotOut__.setValue('')
    self.obj63300.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63300.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63300.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63300.MT_pivotIn__.setValue('')
    self.obj63300.MT_pivotIn__.setNone()

    self.obj63300.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(464.5,219.0,self.obj63300)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63300.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63300)
    self.globalAndLocalPostcondition(self.obj63300, rootNode)
    self.obj63300.postAction( rootNode.CREATE )

    self.obj63301=MT_pre__rightExpr(self)
    self.obj63301.isGraphObjectVisual = True

    if(hasattr(self.obj63301, '_setHierarchicalLink')):
      self.obj63301._setHierarchicalLink(False)

    # MT_label__
    self.obj63301.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj63301.MT_pivotOut__.setValue('')
    self.obj63301.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63301.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63301.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63301.MT_pivotIn__.setValue('')
    self.obj63301.MT_pivotIn__.setNone()

    self.obj63301.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(398.0,418.0,self.obj63301)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63301.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63301)
    self.globalAndLocalPostcondition(self.obj63301, rootNode)
    self.obj63301.postAction( rootNode.CREATE )

    self.obj63302=MT_pre__rightExpr(self)
    self.obj63302.isGraphObjectVisual = True

    if(hasattr(self.obj63302, '_setHierarchicalLink')):
      self.obj63302._setHierarchicalLink(False)

    # MT_label__
    self.obj63302.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj63302.MT_pivotOut__.setValue('')
    self.obj63302.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63302.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63302.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63302.MT_pivotIn__.setValue('')
    self.obj63302.MT_pivotIn__.setNone()

    self.obj63302.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(467.0,319.0,self.obj63302)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63302.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63302)
    self.globalAndLocalPostcondition(self.obj63302, rootNode)
    self.obj63302.postAction( rootNode.CREATE )

    self.obj63303=LHS(self)
    self.obj63303.isGraphObjectVisual = True

    if(hasattr(self.obj63303, '_setHierarchicalLink')):
      self.obj63303._setHierarchicalLink(False)

    # constraint
    self.obj63303.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'3\')[\'name\']==\'H\') and (PreNode(\'9\')[\'name\']==\'name\') and (PreNode(\'13\')[\'name\']==\'H\'):\n   return True\nreturn False\n')
    self.obj63303.constraint.setHeight(15)

    self.obj63303.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,40.0,self.obj63303)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63303.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63303)
    self.globalAndLocalPostcondition(self.obj63303, rootNode)
    self.obj63303.postAction( rootNode.CREATE )

    # Connections for obj63289 (graphObject_: Obj54) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj63289,self.obj63298,[397.0, 261.0, 408.5, 213.0],"true", 2),
(self.obj63289,self.obj63320,[397.0, 261.0, 359.5, 211.0],"true", 2),
(self.obj63289,self.obj63322,[397.0, 261.0, 399.5, 211.0],"true", 2),
(self.obj63289,self.obj63324,[397.0, 261.0, 339.5, 241.0],"true", 2) )
    # Connections for obj63319 (graphObject_: Obj69) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj63321 (graphObject_: Obj71) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj63323 (graphObject_: Obj73) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj63290 (graphObject_: Obj55) of type MT_pre__Inst
    self.drawConnections(
(self.obj63290,self.obj63297,[271.0, 155.0, 175.5, 215.0],"true", 2) )
    # Connections for obj63291 (graphObject_: Obj56) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj63292 (graphObject_: Obj57) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj63293 (graphObject_: Obj58) of type MT_pre__Equation
    self.drawConnections(
(self.obj63293,self.obj63299,[219.0, 395.0, 180.0, 320.0],"true", 2),
(self.obj63293,self.obj63301,[219.0, 395.0, 398.0, 418.0],"true", 2) )
    # Connections for obj63294 (graphObject_: Obj59) of type MT_pre__Equation
    self.drawConnections(
(self.obj63294,self.obj63300,[489.0, 273.0, 464.5, 219.0],"true", 2),
(self.obj63294,self.obj63302,[489.0, 273.0, 467.0, 319.0],"true", 2) )
    # Connections for obj63295 (graphObject_: Obj60) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj63296 (graphObject_: Obj61) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj63320 (graphObject_: Obj70) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj63320,self.obj63319,[359.5, 211.0, 322.0, 161.0],"true", 2) )
    # Connections for obj63322 (graphObject_: Obj72) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj63322,self.obj63321,[399.5, 211.0, 402.0, 161.0],"true", 2) )
    # Connections for obj63324 (graphObject_: Obj74) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj63324,self.obj63323,[339.5, 241.0, 282.0, 221.0],"true", 2) )
    # Connections for obj63297 (graphObject_: Obj62) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj63297,self.obj63291,[175.5, 215.0, 214.0, 265.0],"true", 2) )
    # Connections for obj63298 (graphObject_: Obj63) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj63298,self.obj63292,[408.5, 213.0, 420.0, 125.0],"true", 2) )
    # Connections for obj63299 (graphObject_: Obj64) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj63299,self.obj63291,[180.0, 320.0, 214.0, 265.0],"true", 2) )
    # Connections for obj63300 (graphObject_: Obj65) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj63300,self.obj63292,[464.5, 219.0, 420.0, 125.0],"true", 2) )
    # Connections for obj63301 (graphObject_: Obj66) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj63301,self.obj63295,[398.0, 418.0, 380.0, 385.0],"true", 2) )
    # Connections for obj63302 (graphObject_: Obj67) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj63302,self.obj63296,[467.0, 319.0, 445.0, 365.0],"true", 2) )
    # Connections for obj63303 (graphObject_: Obj68) of type LHS
    self.drawConnections(
 )

newfunction = HInstProcDefParamspart3_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
