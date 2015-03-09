"""
__Trans2HListenBranchOUT_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 11:38:19 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__OUT2 import *
from MT_pre__Signal import *
from MT_pre__directLink_S import *
from MT_pre__Transition import *
from MT_pre__Trigger_S import *
from graph_MT_pre__Trigger_S import *
from graph_MT_pre__Signal import *
from graph_LHS import *
from graph_MT_pre__Transition import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__OUT2 import *
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

def Trans2HListenBranchOUT_Connected_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('Trans2HListenBranchOUT_Connected')
    # --- ASG attributes over ---


    self.obj63309=LHS(self)
    self.obj63309.isGraphObjectVisual = True

    if(hasattr(self.obj63309, '_setHierarchicalLink')):
      self.obj63309._setHierarchicalLink(False)

    # constraint
    self.obj63309.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj63309.constraint.setHeight(15)

    self.obj63309.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj63309)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63309.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63309)
    self.globalAndLocalPostcondition(self.obj63309, rootNode)
    self.obj63309.postAction( rootNode.CREATE )

    self.obj63319=MT_pre__OUT2(self)
    self.obj63319.isGraphObjectVisual = True

    if(hasattr(self.obj63319, '_setHierarchicalLink')):
      self.obj63319._setHierarchicalLink(False)

    # MT_label__
    self.obj63319.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj63319.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj63319.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63319.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63319.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63319.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63319.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63319.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63319.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63319.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63319.MT_pivotIn__.setValue('element2')

    self.obj63319.graphClass_= graph_MT_pre__OUT2
    if self.genGraphics:
       new_obj = graph_MT_pre__OUT2(60.0,240.0,self.obj63319)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63319.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63319)
    self.globalAndLocalPostcondition(self.obj63319, rootNode)
    self.obj63319.postAction( rootNode.CREATE )

    self.obj63310=MT_pre__Signal(self)
    self.obj63310.isGraphObjectVisual = True

    if(hasattr(self.obj63310, '_setHierarchicalLink')):
      self.obj63310._setHierarchicalLink(False)

    # MT_label__
    self.obj63310.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj63310.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj63310.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63310.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63310.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63310.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63310.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63310.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63310.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63310.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63310.MT_pivotIn__.setValue('element4')

    self.obj63310.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(240.0,200.0,self.obj63310)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63310.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63310)
    self.globalAndLocalPostcondition(self.obj63310, rootNode)
    self.obj63310.postAction( rootNode.CREATE )

    self.obj63313=MT_pre__directLink_S(self)
    self.obj63313.isGraphObjectVisual = True

    if(hasattr(self.obj63313, '_setHierarchicalLink')):
      self.obj63313._setHierarchicalLink(False)

    # MT_label__
    self.obj63313.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj63313.MT_pivotOut__.setValue('')
    self.obj63313.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63313.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63313.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63313.MT_pivotIn__.setValue('')
    self.obj63313.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63313.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63313.MT_pre__associationType.setHeight(15)

    self.obj63313.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(327.0,135.0,self.obj63313)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63313.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63313)
    self.globalAndLocalPostcondition(self.obj63313, rootNode)
    self.obj63313.postAction( rootNode.CREATE )

    self.obj63314=MT_pre__directLink_S(self)
    self.obj63314.isGraphObjectVisual = True

    if(hasattr(self.obj63314, '_setHierarchicalLink')):
      self.obj63314._setHierarchicalLink(False)

    # MT_label__
    self.obj63314.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj63314.MT_pivotOut__.setValue('')
    self.obj63314.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63314.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63314.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63314.MT_pivotIn__.setValue('')
    self.obj63314.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63314.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63314.MT_pre__associationType.setHeight(15)

    self.obj63314.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(427.0,215.0,self.obj63314)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63314.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63314)
    self.globalAndLocalPostcondition(self.obj63314, rootNode)
    self.obj63314.postAction( rootNode.CREATE )

    self.obj63322=MT_pre__directLink_S(self)
    self.obj63322.isGraphObjectVisual = True

    if(hasattr(self.obj63322, '_setHierarchicalLink')):
      self.obj63322._setHierarchicalLink(False)

    # MT_label__
    self.obj63322.MT_label__.setValue('9')

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

    self.obj63322.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(247.0,215.0,self.obj63322)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63322.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63322)
    self.globalAndLocalPostcondition(self.obj63322, rootNode)
    self.obj63322.postAction( rootNode.CREATE )

    self.obj63315=MT_pre__Transition(self)
    self.obj63315.isGraphObjectVisual = True

    if(hasattr(self.obj63315, '_setHierarchicalLink')):
      self.obj63315._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63315.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj63315.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63315.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63315.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63315.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63315.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj63315.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj63315.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63315.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63315.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63315.MT_pre__name.setHeight(15)

    self.obj63315.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(40.0,40.0,self.obj63315)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63315.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63315)
    self.globalAndLocalPostcondition(self.obj63315, rootNode)
    self.obj63315.postAction( rootNode.CREATE )

    self.obj63316=MT_pre__Trigger_S(self)
    self.obj63316.isGraphObjectVisual = True

    if(hasattr(self.obj63316, '_setHierarchicalLink')):
      self.obj63316._setHierarchicalLink(False)

    # MT_label__
    self.obj63316.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj63316.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj63316.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63316.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63316.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63316.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63316.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63316.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63316.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63316.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63316.MT_pivotIn__.setValue('element3')

    self.obj63316.graphClass_= graph_MT_pre__Trigger_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_S(220.0,80.0,self.obj63316)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63316.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63316)
    self.globalAndLocalPostcondition(self.obj63316, rootNode)
    self.obj63316.postAction( rootNode.CREATE )

    # Connections for obj63309 (graphObject_: Obj49) of type LHS
    self.drawConnections(
 )
    # Connections for obj63319 (graphObject_: Obj57) of type MT_pre__OUT2
    self.drawConnections(
 )
    # Connections for obj63310 (graphObject_: Obj50) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj63313 (graphObject_: Obj53) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj63313,self.obj63316,[327.0, 135.0, 417.0, 155.0],"true", 2) )
    # Connections for obj63314 (graphObject_: Obj54) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj63314,self.obj63310,[427.0, 215.0, 437.0, 275.0],"true", 2) )
    # Connections for obj63322 (graphObject_: Obj58) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj63322,self.obj63319,[247.0, 215.0, 257.0, 315.0],"true", 2) )
    # Connections for obj63315 (graphObject_: Obj55) of type MT_pre__Transition
    self.drawConnections(
(self.obj63315,self.obj63313,[237.0, 115.0, 327.0, 135.0],"true", 2),
(self.obj63315,self.obj63322,[237.0, 115.0, 247.0, 215.0],"true", 2) )
    # Connections for obj63316 (graphObject_: Obj56) of type MT_pre__Trigger_S
    self.drawConnections(
(self.obj63316,self.obj63314,[417.0, 155.0, 427.0, 215.0],"true", 2) )

newfunction = Trans2HListenBranchOUT_Connected_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
