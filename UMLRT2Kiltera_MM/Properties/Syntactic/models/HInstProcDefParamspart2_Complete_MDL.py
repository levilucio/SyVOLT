"""
__HInstProcDefParamspart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Mar  6 16:46:41 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
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
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Constant import *
from graph_MT_pre__rightExpr import *
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

def HInstProcDefParamspart2_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('HInstProcDefParamspart2_Complete')
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


    self.obj42253=MT_pre__Name(self)
    self.obj42253.isGraphObjectVisual = True

    if(hasattr(self.obj42253, '_setHierarchicalLink')):
      self.obj42253._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42253.MT_pivotOut__.setValue('')
    self.obj42253.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42253.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42253.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42253.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42253.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42253.MT_pivotIn__.setValue('')
    self.obj42253.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42253.MT_label__.setValue('8')

    # MT_pre__cardinality
    self.obj42253.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42253.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42253.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42253.MT_pre__name.setHeight(15)

    self.obj42253.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(220.0,60.0,self.obj42253)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42253.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42253)
    self.globalAndLocalPostcondition(self.obj42253, rootNode)
    self.obj42253.postAction( rootNode.CREATE )

    self.obj42258=MT_pre__Name(self)
    self.obj42258.isGraphObjectVisual = True

    if(hasattr(self.obj42258, '_setHierarchicalLink')):
      self.obj42258._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42258.MT_pivotOut__.setValue('')
    self.obj42258.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42258.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42258.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42258.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42258.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42258.MT_pivotIn__.setValue('')
    self.obj42258.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42258.MT_label__.setValue('9')

    # MT_pre__cardinality
    self.obj42258.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42258.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42258.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42258.MT_pre__name.setHeight(15)

    self.obj42258.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(60.0,260.0,self.obj42258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42258.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42258)
    self.globalAndLocalPostcondition(self.obj42258, rootNode)
    self.obj42258.postAction( rootNode.CREATE )

    self.obj42259=MT_pre__Name(self)
    self.obj42259.isGraphObjectVisual = True

    if(hasattr(self.obj42259, '_setHierarchicalLink')):
      self.obj42259._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42259.MT_pivotOut__.setValue('')
    self.obj42259.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42259.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42259.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42259.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42259.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42259.MT_pivotIn__.setValue('')
    self.obj42259.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42259.MT_label__.setValue('10')

    # MT_pre__cardinality
    self.obj42259.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42259.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42259.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42259.MT_pre__name.setHeight(15)

    self.obj42259.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(240.0,200.0,self.obj42259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42259)
    self.globalAndLocalPostcondition(self.obj42259, rootNode)
    self.obj42259.postAction( rootNode.CREATE )

    self.obj52773=MT_pre__Name(self)
    self.obj52773.isGraphObjectVisual = True

    if(hasattr(self.obj52773, '_setHierarchicalLink')):
      self.obj52773._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52773.MT_pivotOut__.setValue('')
    self.obj52773.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52773.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52773.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52773.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52773.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52773.MT_pivotIn__.setValue('')
    self.obj52773.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52773.MT_label__.setValue('14')

    # MT_pre__cardinality
    self.obj52773.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52773.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52773.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52773.MT_pre__name.setHeight(15)

    self.obj52773.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(220.0,140.0,self.obj52773)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52773.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52773)
    self.globalAndLocalPostcondition(self.obj52773, rootNode)
    self.obj52773.postAction( rootNode.CREATE )

    self.obj42241=MT_pre__Inst(self)
    self.obj42241.isGraphObjectVisual = True

    if(hasattr(self.obj42241, '_setHierarchicalLink')):
      self.obj42241._setHierarchicalLink(False)

    # MT_label__
    self.obj42241.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj42241.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj42241.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42241.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42241.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42241.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj42241.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42241.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42241.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42241.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj42241.MT_pivotIn__.setValue('element1')

    self.obj42241.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(60.0,60.0,self.obj42241)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42241.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42241)
    self.globalAndLocalPostcondition(self.obj42241, rootNode)
    self.obj42241.postAction( rootNode.CREATE )

    self.obj42242=MT_pre__Attribute(self)
    self.obj42242.isGraphObjectVisual = True

    if(hasattr(self.obj42242, '_setHierarchicalLink')):
      self.obj42242._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42242.MT_pivotOut__.setValue('')
    self.obj42242.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42242.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42242.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj42242.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42242.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj42242.MT_pivotIn__.setValue('')
    self.obj42242.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42242.MT_label__.setValue('2')

    # MT_pre__name
    self.obj42242.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42242.MT_pre__name.setHeight(15)

    self.obj42242.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(80.0,240.0,self.obj42242)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42242.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42242)
    self.globalAndLocalPostcondition(self.obj42242, rootNode)
    self.obj42242.postAction( rootNode.CREATE )

    self.obj42243=MT_pre__Equation(self)
    self.obj42243.isGraphObjectVisual = True

    if(hasattr(self.obj42243, '_setHierarchicalLink')):
      self.obj42243._setHierarchicalLink(False)

    # MT_label__
    self.obj42243.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj42243.MT_pivotOut__.setValue('')
    self.obj42243.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj42243.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42243.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj42243.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42243.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42243.MT_pivotIn__.setValue('')
    self.obj42243.MT_pivotIn__.setNone()

    self.obj42243.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(280.0,280.0,self.obj42243)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42243.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42243)
    self.globalAndLocalPostcondition(self.obj42243, rootNode)
    self.obj42243.postAction( rootNode.CREATE )

    self.obj42244=MT_pre__Constant(self)
    self.obj42244.isGraphObjectVisual = True

    if(hasattr(self.obj42244, '_setHierarchicalLink')):
      self.obj42244._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42244.MT_pivotOut__.setValue('')
    self.obj42244.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42244.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42244.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj42244.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42244.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj42244.MT_pivotIn__.setValue('')
    self.obj42244.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42244.MT_label__.setValue('3')

    # MT_pre__name
    self.obj42244.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42244.MT_pre__name.setHeight(15)

    self.obj42244.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(300.0,160.0,self.obj42244)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42244.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42244)
    self.globalAndLocalPostcondition(self.obj42244, rootNode)
    self.obj42244.postAction( rootNode.CREATE )

    self.obj42260=MT_pre__directLink_T(self)
    self.obj42260.isGraphObjectVisual = True

    if(hasattr(self.obj42260, '_setHierarchicalLink')):
      self.obj42260._setHierarchicalLink(False)

    # MT_label__
    self.obj42260.MT_label__.setValue('11')

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
       new_obj = graph_MT_pre__directLink_T(357.0,161.0,self.obj42260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42260)
    self.globalAndLocalPostcondition(self.obj42260, rootNode)
    self.obj42260.postAction( rootNode.CREATE )

    self.obj42261=MT_pre__directLink_T(self)
    self.obj42261.isGraphObjectVisual = True

    if(hasattr(self.obj42261, '_setHierarchicalLink')):
      self.obj42261._setHierarchicalLink(False)

    # MT_label__
    self.obj42261.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj42261.MT_pivotOut__.setValue('')
    self.obj42261.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42261.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42261.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42261.MT_pivotIn__.setValue('')
    self.obj42261.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42261.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42261.MT_pre__associationType.setHeight(15)

    self.obj42261.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(369.5,231.0,self.obj42261)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42261.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42261)
    self.globalAndLocalPostcondition(self.obj42261, rootNode)
    self.obj42261.postAction( rootNode.CREATE )

    self.obj42262=MT_pre__directLink_T(self)
    self.obj42262.isGraphObjectVisual = True

    if(hasattr(self.obj42262, '_setHierarchicalLink')):
      self.obj42262._setHierarchicalLink(False)

    # MT_label__
    self.obj42262.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj42262.MT_pivotOut__.setValue('')
    self.obj42262.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42262.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42262.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42262.MT_pivotIn__.setValue('')
    self.obj42262.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42262.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42262.MT_pre__associationType.setHeight(15)

    self.obj42262.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(277.0,261.0,self.obj42262)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42262.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42262)
    self.globalAndLocalPostcondition(self.obj42262, rootNode)
    self.obj42262.postAction( rootNode.CREATE )

    self.obj52774=MT_pre__directLink_T(self)
    self.obj52774.isGraphObjectVisual = True

    if(hasattr(self.obj52774, '_setHierarchicalLink')):
      self.obj52774._setHierarchicalLink(False)

    # MT_label__
    self.obj52774.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj52774.MT_pivotOut__.setValue('')
    self.obj52774.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52774.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52774.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52774.MT_pivotIn__.setValue('')
    self.obj52774.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52774.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52774.MT_pre__associationType.setHeight(15)

    self.obj52774.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(359.5,201.0,self.obj52774)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52774.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52774)
    self.globalAndLocalPostcondition(self.obj52774, rootNode)
    self.obj52774.postAction( rootNode.CREATE )

    self.obj42245=MT_pre__hasAttribute_T(self)
    self.obj42245.isGraphObjectVisual = True

    if(hasattr(self.obj42245, '_setHierarchicalLink')):
      self.obj42245._setHierarchicalLink(False)

    # MT_label__
    self.obj42245.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj42245.MT_pivotOut__.setValue('')
    self.obj42245.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42245.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42245.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42245.MT_pivotIn__.setValue('')
    self.obj42245.MT_pivotIn__.setNone()

    self.obj42245.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(278.5,233.0,self.obj42245)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42245.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42245)
    self.globalAndLocalPostcondition(self.obj42245, rootNode)
    self.obj42245.postAction( rootNode.CREATE )

    self.obj42246=MT_pre__leftExpr(self)
    self.obj42246.isGraphObjectVisual = True

    if(hasattr(self.obj42246, '_setHierarchicalLink')):
      self.obj42246._setHierarchicalLink(False)

    # MT_label__
    self.obj42246.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj42246.MT_pivotOut__.setValue('')
    self.obj42246.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42246.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42246.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42246.MT_pivotIn__.setValue('')
    self.obj42246.MT_pivotIn__.setNone()

    self.obj42246.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(362.0,329.0,self.obj42246)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42246.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42246)
    self.globalAndLocalPostcondition(self.obj42246, rootNode)
    self.obj42246.postAction( rootNode.CREATE )

    self.obj42247=MT_pre__rightExpr(self)
    self.obj42247.isGraphObjectVisual = True

    if(hasattr(self.obj42247, '_setHierarchicalLink')):
      self.obj42247._setHierarchicalLink(False)

    # MT_label__
    self.obj42247.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj42247.MT_pivotOut__.setValue('')
    self.obj42247.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42247.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42247.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42247.MT_pivotIn__.setValue('')
    self.obj42247.MT_pivotIn__.setNone()

    self.obj42247.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(442.0,289.0,self.obj42247)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42247.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42247)
    self.globalAndLocalPostcondition(self.obj42247, rootNode)
    self.obj42247.postAction( rootNode.CREATE )

    self.obj42248=LHS(self)
    self.obj42248.isGraphObjectVisual = True

    if(hasattr(self.obj42248, '_setHierarchicalLink')):
      self.obj42248._setHierarchicalLink(False)

    # constraint
    self.obj42248.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'3\')[\'name\']==\'H\'):\n   return True\nreturn False\n')
    self.obj42248.constraint.setHeight(15)

    self.obj42248.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,40.0,self.obj42248)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42248.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42248)
    self.globalAndLocalPostcondition(self.obj42248, rootNode)
    self.obj42248.postAction( rootNode.CREATE )

    # Connections for obj42253 (graphObject_: Obj46) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj42258 (graphObject_: Obj47) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj42259 (graphObject_: Obj48) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj52773 (graphObject_: Obj52) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj42241 (graphObject_: Obj38) of type MT_pre__Inst
    self.drawConnections(
(self.obj42241,self.obj42245,[277.0, 161.0, 278.5, 233.0],"true", 2),
(self.obj42241,self.obj42260,[277.0, 161.0, 357.0, 161.0],"true", 2),
(self.obj42241,self.obj42261,[277.0, 161.0, 369.5, 231.0],"true", 2),
(self.obj42241,self.obj42262,[277.0, 161.0, 277.0, 261.0],"true", 2),
(self.obj42241,self.obj52774,[277.0, 161.0, 359.5, 201.0],"true", 2) )
    # Connections for obj42242 (graphObject_: Obj39) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj42243 (graphObject_: Obj40) of type MT_pre__Equation
    self.drawConnections(
(self.obj42243,self.obj42246,[444.0, 353.0, 362.0, 329.0],"true", 2),
(self.obj42243,self.obj42247,[444.0, 353.0, 442.0, 289.0],"true", 2) )
    # Connections for obj42244 (graphObject_: Obj41) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj42260 (graphObject_: Obj49) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42260,self.obj42253,[357.0, 161.0, 437.0, 161.0],"true", 2) )
    # Connections for obj42261 (graphObject_: Obj50) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42261,self.obj42259,[369.5, 231.0, 462.0, 301.0],"true", 2) )
    # Connections for obj42262 (graphObject_: Obj51) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42262,self.obj42258,[277.0, 261.0, 277.0, 361.0],"true", 2) )
    # Connections for obj52774 (graphObject_: Obj53) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj52774,self.obj52773,[359.5, 201.0, 442.0, 241.0],"true", 2) )
    # Connections for obj42245 (graphObject_: Obj42) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj42245,self.obj42242,[278.5, 233.0, 240.0, 305.0],"true", 2) )
    # Connections for obj42246 (graphObject_: Obj43) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj42246,self.obj42242,[362.0, 329.0, 240.0, 305.0],"true", 2) )
    # Connections for obj42247 (graphObject_: Obj44) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj42247,self.obj42244,[442.0, 289.0, 460.0, 225.0],"true", 2) )
    # Connections for obj42248 (graphObject_: Obj45) of type LHS
    self.drawConnections(
 )

newfunction = HInstProcDefParamspart2_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
