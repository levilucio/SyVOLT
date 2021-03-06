"""
__ExitPtConOPsOfExitPtSIB_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 18:53:42 2015
_______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__SIBLING0 import *
from MT_pre__rightExpr import *
from MT_pre__directLink_S import *
from MT_pre__hasAttribute_S import *
from MT_pre__Transition import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
from MT_pre__ExitPoint import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__Transition import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
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

def ExitPtConOPsOfExitPtSIB_Connected_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ExitPtConOPsOfExitPtSIB_Connected')
    # --- ASG attributes over ---


    self.obj10670=LHS(self)
    self.obj10670.isGraphObjectVisual = True

    if(hasattr(self.obj10670, '_setHierarchicalLink')):
      self.obj10670._setHierarchicalLink(False)

    # constraint
    self.obj10670.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'8\')[\'name\']==\'isComposite\')and (PreNode(\'12\')[\'name\']==\'true\'):\n   return True\nreturn False\n')
    self.obj10670.constraint.setHeight(15)

    self.obj10670.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,20.0,self.obj10670)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10670.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10670)
    self.globalAndLocalPostcondition(self.obj10670, rootNode)
    self.obj10670.postAction( rootNode.CREATE )

    self.obj10659=MT_pre__State(self)
    self.obj10659.isGraphObjectVisual = True

    if(hasattr(self.obj10659, '_setHierarchicalLink')):
      self.obj10659._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10659.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj10659.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10659.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10659.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10659.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10659.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj10659.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj10659.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10659.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10659.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10659.MT_pre__name.setHeight(15)

    self.obj10659.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj10659)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10659.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10659)
    self.globalAndLocalPostcondition(self.obj10659, rootNode)
    self.obj10659.postAction( rootNode.CREATE )

    self.obj10673=MT_pre__SIBLING0(self)
    self.obj10673.isGraphObjectVisual = True

    if(hasattr(self.obj10673, '_setHierarchicalLink')):
      self.obj10673._setHierarchicalLink(False)

    # MT_label__
    self.obj10673.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj10673.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj10673.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10673.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10673.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10673.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10673.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10673.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10673.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10673.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10673.MT_pivotIn__.setValue('element4')

    self.obj10673.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(80.0,140.0,self.obj10673)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10673.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10673)
    self.globalAndLocalPostcondition(self.obj10673, rootNode)
    self.obj10673.postAction( rootNode.CREATE )

    self.obj10669=MT_pre__rightExpr(self)
    self.obj10669.isGraphObjectVisual = True

    if(hasattr(self.obj10669, '_setHierarchicalLink')):
      self.obj10669._setHierarchicalLink(False)

    # MT_label__
    self.obj10669.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj10669.MT_pivotOut__.setValue('')
    self.obj10669.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10669.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10669.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10669.MT_pivotIn__.setValue('')
    self.obj10669.MT_pivotIn__.setNone()

    self.obj10669.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(387.0,339.0,self.obj10669)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10669.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10669)
    self.globalAndLocalPostcondition(self.obj10669, rootNode)
    self.obj10669.postAction( rootNode.CREATE )

    self.obj10664=MT_pre__directLink_S(self)
    self.obj10664.isGraphObjectVisual = True

    if(hasattr(self.obj10664, '_setHierarchicalLink')):
      self.obj10664._setHierarchicalLink(False)

    # MT_label__
    self.obj10664.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10664.MT_pivotOut__.setValue('')
    self.obj10664.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10664.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10664.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10664.MT_pivotIn__.setValue('')
    self.obj10664.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10664.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10664.MT_pre__associationType.setHeight(15)

    self.obj10664.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(344.5,115.0,self.obj10664)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10664.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10664)
    self.globalAndLocalPostcondition(self.obj10664, rootNode)
    self.obj10664.postAction( rootNode.CREATE )

    self.obj10665=MT_pre__directLink_S(self)
    self.obj10665.isGraphObjectVisual = True

    if(hasattr(self.obj10665, '_setHierarchicalLink')):
      self.obj10665._setHierarchicalLink(False)

    # MT_label__
    self.obj10665.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj10665.MT_pivotOut__.setValue('')
    self.obj10665.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10665.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10665.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10665.MT_pivotIn__.setValue('')
    self.obj10665.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10665.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10665.MT_pre__associationType.setHeight(15)

    self.obj10665.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(453.0,159.0,self.obj10665)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10665.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10665)
    self.globalAndLocalPostcondition(self.obj10665, rootNode)
    self.obj10665.postAction( rootNode.CREATE )

    self.obj10676=MT_pre__directLink_S(self)
    self.obj10676.isGraphObjectVisual = True

    if(hasattr(self.obj10676, '_setHierarchicalLink')):
      self.obj10676._setHierarchicalLink(False)

    # MT_label__
    self.obj10676.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj10676.MT_pivotOut__.setValue('')
    self.obj10676.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10676.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10676.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10676.MT_pivotIn__.setValue('')
    self.obj10676.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10676.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10676.MT_pre__associationType.setHeight(15)

    self.obj10676.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(369.5,215.0,self.obj10676)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10676.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10676)
    self.globalAndLocalPostcondition(self.obj10676, rootNode)
    self.obj10676.postAction( rootNode.CREATE )

    self.obj10667=MT_pre__hasAttribute_S(self)
    self.obj10667.isGraphObjectVisual = True

    if(hasattr(self.obj10667, '_setHierarchicalLink')):
      self.obj10667._setHierarchicalLink(False)

    # MT_label__
    self.obj10667.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj10667.MT_pivotOut__.setValue('')
    self.obj10667.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10667.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10667.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10667.MT_pivotIn__.setValue('')
    self.obj10667.MT_pivotIn__.setNone()

    self.obj10667.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(238.5,210.0,self.obj10667)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10667.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10667)
    self.globalAndLocalPostcondition(self.obj10667, rootNode)
    self.obj10667.postAction( rootNode.CREATE )

    self.obj10658=MT_pre__Transition(self)
    self.obj10658.isGraphObjectVisual = True

    if(hasattr(self.obj10658, '_setHierarchicalLink')):
      self.obj10658._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10658.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj10658.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10658.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10658.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10658.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10658.MT_pivotIn__.setValue('element3')

    # MT_label__
    self.obj10658.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj10658.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10658.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10658.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10658.MT_pre__name.setHeight(15)

    self.obj10658.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(260.0,140.0,self.obj10658)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10658.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10658)
    self.globalAndLocalPostcondition(self.obj10658, rootNode)
    self.obj10658.postAction( rootNode.CREATE )

    self.obj10661=MT_pre__Attribute(self)
    self.obj10661.isGraphObjectVisual = True

    if(hasattr(self.obj10661, '_setHierarchicalLink')):
      self.obj10661._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10661.MT_pivotOut__.setValue('')
    self.obj10661.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10661.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10661.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj10661.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10661.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj10661.MT_pivotIn__.setValue('')
    self.obj10661.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10661.MT_label__.setValue('8')

    # MT_pre__name
    self.obj10661.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10661.MT_pre__name.setHeight(15)

    self.obj10661.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(60.0,240.0,self.obj10661)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10661.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10661)
    self.globalAndLocalPostcondition(self.obj10661, rootNode)
    self.obj10661.postAction( rootNode.CREATE )

    self.obj10663=MT_pre__Constant(self)
    self.obj10663.isGraphObjectVisual = True

    if(hasattr(self.obj10663, '_setHierarchicalLink')):
      self.obj10663._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10663.MT_pivotOut__.setValue('')
    self.obj10663.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10663.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10663.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj10663.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10663.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj10663.MT_pivotIn__.setValue('')
    self.obj10663.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10663.MT_label__.setValue('12')

    # MT_pre__name
    self.obj10663.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10663.MT_pre__name.setHeight(15)

    self.obj10663.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(220.0,300.0,self.obj10663)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10663.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10663)
    self.globalAndLocalPostcondition(self.obj10663, rootNode)
    self.obj10663.postAction( rootNode.CREATE )

    self.obj10657=MT_pre__ExitPoint(self)
    self.obj10657.isGraphObjectVisual = True

    if(hasattr(self.obj10657, '_setHierarchicalLink')):
      self.obj10657._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10657.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj10657.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10657.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10657.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10657.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10657.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj10657.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10657.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10657.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10657.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10657.MT_pre__name.setHeight(15)

    self.obj10657.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(233.0,40.0,self.obj10657)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10657.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10657)
    self.globalAndLocalPostcondition(self.obj10657, rootNode)
    self.obj10657.postAction( rootNode.CREATE )

    self.obj10668=MT_pre__leftExpr(self)
    self.obj10668.isGraphObjectVisual = True

    if(hasattr(self.obj10668, '_setHierarchicalLink')):
      self.obj10668._setHierarchicalLink(False)

    # MT_label__
    self.obj10668.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj10668.MT_pivotOut__.setValue('')
    self.obj10668.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10668.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10668.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10668.MT_pivotIn__.setValue('')
    self.obj10668.MT_pivotIn__.setNone()

    self.obj10668.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(304.5,309.0,self.obj10668)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10668.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10668)
    self.globalAndLocalPostcondition(self.obj10668, rootNode)
    self.obj10668.postAction( rootNode.CREATE )

    self.obj10662=MT_pre__Equation(self)
    self.obj10662.isGraphObjectVisual = True

    if(hasattr(self.obj10662, '_setHierarchicalLink')):
      self.obj10662._setHierarchicalLink(False)

    # MT_label__
    self.obj10662.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj10662.MT_pivotOut__.setValue('')
    self.obj10662.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj10662.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10662.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj10662.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10662.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10662.MT_pivotIn__.setValue('')
    self.obj10662.MT_pivotIn__.setNone()

    self.obj10662.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(220.0,240.0,self.obj10662)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10662.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10662)
    self.globalAndLocalPostcondition(self.obj10662, rootNode)
    self.obj10662.postAction( rootNode.CREATE )

    # Connections for obj10670 (graphObject_: Obj25) of type LHS
    self.drawConnections(
 )
    # Connections for obj10659 (graphObject_: Obj14) of type MT_pre__State
    self.drawConnections(
(self.obj10659,self.obj10664,[257.0, 115.0, 344.5, 115.0],"true", 2),
(self.obj10659,self.obj10667,[257.0, 115.0, 238.5, 210.0],"true", 2) )
    # Connections for obj10673 (graphObject_: Obj26) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj10669 (graphObject_: Obj24) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj10669,self.obj10663,[387.0, 339.0, 385.0, 365.0],"true", 2) )
    # Connections for obj10664 (graphObject_: Obj19) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10664,self.obj10657,[344.5, 115.0, 430.0, 115.0],"true", 2) )
    # Connections for obj10665 (graphObject_: Obj20) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10665,self.obj10658,[453.0, 159.0, 457.0, 215.0],"true", 2) )
    # Connections for obj10676 (graphObject_: Obj27) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10676,self.obj10673,[369.5, 215.0, 282.0, 215.0],"true", 2) )
    # Connections for obj10667 (graphObject_: Obj22) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj10667,self.obj10661,[238.5, 210.0, 220.0, 305.0],"true", 2) )
    # Connections for obj10658 (graphObject_: Obj13) of type MT_pre__Transition
    self.drawConnections(
(self.obj10658,self.obj10676,[457.0, 215.0, 369.5, 215.0],"true", 0) )
    # Connections for obj10661 (graphObject_: Obj16) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj10663 (graphObject_: Obj18) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj10657 (graphObject_: Obj12) of type MT_pre__ExitPoint
    self.drawConnections(
(self.obj10657,self.obj10665,[430.0, 115.0, 453.0, 159.0],"true", 2) )
    # Connections for obj10668 (graphObject_: Obj23) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj10668,self.obj10661,[304.5, 309.0, 220.0, 305.0],"true", 2) )
    # Connections for obj10662 (graphObject_: Obj17) of type MT_pre__Equation
    self.drawConnections(
(self.obj10662,self.obj10668,[389.0, 313.0, 304.5, 309.0],"true", 2),
(self.obj10662,self.obj10669,[389.0, 313.0, 387.0, 339.0],"true", 2) )

newfunction = ExitPtConOPsOfExitPtSIB_Connected_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
