"""
__Trans2HListenBranchSIBLING_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 10:06:04 2015
__________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Signal import *
from MT_pre__SIBLING0 import *
from MT_pre__directLink_S import *
from MT_pre__Transition import *
from MT_pre__Trigger_S import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__Trigger_S import *
from graph_MT_pre__Signal import *
from graph_LHS import *
from graph_MT_pre__Transition import *
from graph_MT_pre__directLink_S import *
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

def Trans2HListenBranchSIBLING_Connected_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('Trans2HListenBranchSIBLING_Connected')
    # --- ASG attributes over ---


    self.obj123=LHS(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # constraint
    self.obj123.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj123.constraint.setHeight(15)

    self.obj123.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj129=MT_pre__Signal(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_label__
    self.obj129.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj129.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj129.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj129.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('element4')

    self.obj129.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(240.0,200.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj125=MT_pre__SIBLING0(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_label__
    self.obj125.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj125.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj125.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj125.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('element2')

    self.obj125.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(60.0,220.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj10672=MT_pre__directLink_S(self)
    self.obj10672.isGraphObjectVisual = True

    if(hasattr(self.obj10672, '_setHierarchicalLink')):
      self.obj10672._setHierarchicalLink(False)

    # MT_label__
    self.obj10672.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10672.MT_pivotOut__.setValue('')
    self.obj10672.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10672.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10672.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10672.MT_pivotIn__.setValue('')
    self.obj10672.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10672.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10672.MT_pre__associationType.setHeight(15)

    self.obj10672.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(247.0,205.0,self.obj10672)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10672.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10672)
    self.globalAndLocalPostcondition(self.obj10672, rootNode)
    self.obj10672.postAction( rootNode.CREATE )

    self.obj10673=MT_pre__directLink_S(self)
    self.obj10673.isGraphObjectVisual = True

    if(hasattr(self.obj10673, '_setHierarchicalLink')):
      self.obj10673._setHierarchicalLink(False)

    # MT_label__
    self.obj10673.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj10673.MT_pivotOut__.setValue('')
    self.obj10673.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10673.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10673.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10673.MT_pivotIn__.setValue('')
    self.obj10673.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10673.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10673.MT_pre__associationType.setHeight(15)

    self.obj10673.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(327.0,135.0,self.obj10673)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10673.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10673)
    self.globalAndLocalPostcondition(self.obj10673, rootNode)
    self.obj10673.postAction( rootNode.CREATE )

    self.obj10674=MT_pre__directLink_S(self)
    self.obj10674.isGraphObjectVisual = True

    if(hasattr(self.obj10674, '_setHierarchicalLink')):
      self.obj10674._setHierarchicalLink(False)

    # MT_label__
    self.obj10674.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj10674.MT_pivotOut__.setValue('')
    self.obj10674.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10674.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10674.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10674.MT_pivotIn__.setValue('')
    self.obj10674.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10674.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10674.MT_pre__associationType.setHeight(15)

    self.obj10674.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(427.0,215.0,self.obj10674)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10674.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10674)
    self.globalAndLocalPostcondition(self.obj10674, rootNode)
    self.obj10674.postAction( rootNode.CREATE )

    self.obj124=MT_pre__Transition(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj124.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj124.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj124.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj124.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__name.setHeight(15)

    self.obj124.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(40.0,40.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj126=MT_pre__Trigger_S(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # MT_label__
    self.obj126.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj126.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj126.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj126.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj126.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj126.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj126.MT_pivotIn__.setValue('element3')

    self.obj126.graphClass_= graph_MT_pre__Trigger_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_S(220.0,80.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )
    # Connections for obj129 (graphObject_: Obj4) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj125 (graphObject_: Obj2) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj10672 (graphObject_: Obj5) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10672,self.obj125,[247.0, 205.0, 257.0, 295.0],"true", 2) )
    # Connections for obj10673 (graphObject_: Obj6) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10673,self.obj126,[327.0, 135.0, 417.0, 155.0],"true", 2) )
    # Connections for obj10674 (graphObject_: Obj7) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10674,self.obj129,[427.0, 215.0, 437.0, 275.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__Transition
    self.drawConnections(
(self.obj124,self.obj10672,[237.0, 115.0, 247.0, 205.0],"true", 2),
(self.obj124,self.obj10673,[237.0, 115.0, 327.0, 135.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj3) of type MT_pre__Trigger_S
    self.drawConnections(
(self.obj126,self.obj10674,[417.0, 155.0, 427.0, 215.0],"true", 2) )

newfunction = Trans2HListenBranchSIBLING_Connected_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
