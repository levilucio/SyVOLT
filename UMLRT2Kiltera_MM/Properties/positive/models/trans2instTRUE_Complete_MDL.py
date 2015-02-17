"""
__trans2instTRUE_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Tue Feb 17 14:42:22 2015
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__SIBLING0 import *
from MT_pre__trace_link import *
from MT_pre__directLink_S import *
from MT_pre__Inst import *
from MT_pre__Transition import *
from graph_MT_pre__SIBLING0 import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Transition import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
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

def trans2instTRUE_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('trans2instTRUE_Complete')
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
       new_obj = graph_LHS(20.0,40.0,self.obj123)
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

    self.obj10634=MT_pre__State(self)
    self.obj10634.isGraphObjectVisual = True

    if(hasattr(self.obj10634, '_setHierarchicalLink')):
      self.obj10634._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10634.MT_pivotOut__.setValue('')
    self.obj10634.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10634.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10634.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10634.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10634.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10634.MT_pivotIn__.setValue('')
    self.obj10634.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10634.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10634.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10634.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10634.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10634.MT_pre__name.setHeight(15)

    self.obj10634.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(40.0,60.0,self.obj10634)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10634.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10634)
    self.globalAndLocalPostcondition(self.obj10634, rootNode)
    self.obj10634.postAction( rootNode.CREATE )

    self.obj10636=MT_pre__SIBLING0(self)
    self.obj10636.isGraphObjectVisual = True

    if(hasattr(self.obj10636, '_setHierarchicalLink')):
      self.obj10636._setHierarchicalLink(False)

    # MT_label__
    self.obj10636.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj10636.MT_pivotOut__.setValue('')
    self.obj10636.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10636.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10636.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10636.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10636.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10636.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10636.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10636.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10636.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10636.MT_pivotIn__.setValue('')
    self.obj10636.MT_pivotIn__.setNone()

    self.obj10636.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(218.0,61.0,self.obj10636)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10636.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10636)
    self.globalAndLocalPostcondition(self.obj10636, rootNode)
    self.obj10636.postAction( rootNode.CREATE )

    self.obj21149=MT_pre__trace_link(self)
    self.obj21149.isGraphObjectVisual = True

    if(hasattr(self.obj21149, '_setHierarchicalLink')):
      self.obj21149._setHierarchicalLink(False)

    # MT_label__
    self.obj21149.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj21149.MT_pivotOut__.setValue('')
    self.obj21149.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21149.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21149.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21149.MT_pivotIn__.setValue('')
    self.obj21149.MT_pivotIn__.setNone()

    self.obj21149.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(347.0,317.0,self.obj21149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21149)
    self.globalAndLocalPostcondition(self.obj21149, rootNode)
    self.obj21149.postAction( rootNode.CREATE )

    self.obj21150=MT_pre__trace_link(self)
    self.obj21150.isGraphObjectVisual = True

    if(hasattr(self.obj21150, '_setHierarchicalLink')):
      self.obj21150._setHierarchicalLink(False)

    # MT_label__
    self.obj21150.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj21150.MT_pivotOut__.setValue('')
    self.obj21150.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21150.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21150.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21150.MT_pivotIn__.setValue('')
    self.obj21150.MT_pivotIn__.setNone()

    self.obj21150.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(396.0,258.5,self.obj21150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21150)
    self.globalAndLocalPostcondition(self.obj21150, rootNode)
    self.obj21150.postAction( rootNode.CREATE )

    self.obj21151=MT_pre__trace_link(self)
    self.obj21151.isGraphObjectVisual = True

    if(hasattr(self.obj21151, '_setHierarchicalLink')):
      self.obj21151._setHierarchicalLink(False)

    # MT_label__
    self.obj21151.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj21151.MT_pivotOut__.setValue('')
    self.obj21151.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21151.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21151.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21151.MT_pivotIn__.setValue('')
    self.obj21151.MT_pivotIn__.setNone()

    self.obj21151.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(307.0,258.0,self.obj21151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21151)
    self.globalAndLocalPostcondition(self.obj21151, rootNode)
    self.obj21151.postAction( rootNode.CREATE )

    self.obj10635=MT_pre__directLink_S(self)
    self.obj10635.isGraphObjectVisual = True

    if(hasattr(self.obj10635, '_setHierarchicalLink')):
      self.obj10635._setHierarchicalLink(False)

    # MT_label__
    self.obj10635.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj10635.MT_pivotOut__.setValue('')
    self.obj10635.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10635.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10635.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10635.MT_pivotIn__.setValue('')
    self.obj10635.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10635.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10635.MT_pre__associationType.setHeight(15)

    self.obj10635.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(248.0,191.0,self.obj10635)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10635.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10635)
    self.globalAndLocalPostcondition(self.obj10635, rootNode)
    self.obj10635.postAction( rootNode.CREATE )

    self.obj10637=MT_pre__directLink_S(self)
    self.obj10637.isGraphObjectVisual = True

    if(hasattr(self.obj10637, '_setHierarchicalLink')):
      self.obj10637._setHierarchicalLink(False)

    # MT_label__
    self.obj10637.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10637.MT_pivotOut__.setValue('')
    self.obj10637.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10637.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10637.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10637.MT_pivotIn__.setValue('')
    self.obj10637.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10637.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10637.MT_pre__associationType.setHeight(15)

    self.obj10637.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(345.0,195.0,self.obj10637)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10637.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10637)
    self.globalAndLocalPostcondition(self.obj10637, rootNode)
    self.obj10637.postAction( rootNode.CREATE )

    self.obj21148=MT_pre__Inst(self)
    self.obj21148.isGraphObjectVisual = True

    if(hasattr(self.obj21148, '_setHierarchicalLink')):
      self.obj21148._setHierarchicalLink(False)

    # MT_label__
    self.obj21148.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj21148.MT_pivotOut__.setValue('')
    self.obj21148.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21148.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21148.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21148.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21148.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21148.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21148.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21148.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21148.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21148.MT_pivotIn__.setValue('')
    self.obj21148.MT_pivotIn__.setNone()

    self.obj21148.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(160.0,280.0,self.obj21148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21148)
    self.globalAndLocalPostcondition(self.obj21148, rootNode)
    self.obj21148.postAction( rootNode.CREATE )

    self.obj124=MT_pre__Transition(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('')
    self.obj124.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj124.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('')
    self.obj124.MT_pivotIn__.setNone()

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
       new_obj = graph_MT_pre__Transition(120.0,178.0,self.obj124)
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

    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )
    # Connections for obj10634 (graphObject_: Obj3) of type MT_pre__State
    self.drawConnections(
(self.obj10634,self.obj10635,[237.0, 135.0, 248.0, 191.0],"true", 2) )
    # Connections for obj10636 (graphObject_: Obj5) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj21149 (graphObject_: Obj8) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21149,self.obj124,[347.0, 317.0, 317.0, 253.0],"true", 2) )
    # Connections for obj21150 (graphObject_: Obj9) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21150,self.obj10636,[396.0, 258.5, 415.0, 136.0],"true", 2) )
    # Connections for obj21151 (graphObject_: Obj10) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21151,self.obj10634,[307.0, 258.0, 237.0, 135.0],"true", 2) )
    # Connections for obj10635 (graphObject_: Obj4) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10635,self.obj124,[248.0, 191.0, 317.0, 253.0],"true", 2) )
    # Connections for obj10637 (graphObject_: Obj6) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10637,self.obj10636,[345.0, 195.0, 415.0, 136.0],"true", 2) )
    # Connections for obj21148 (graphObject_: Obj7) of type MT_pre__Inst
    self.drawConnections(
(self.obj21148,self.obj21149,[377.0, 381.0, 347.0, 317.0],"true", 2),
(self.obj21148,self.obj21150,[377.0, 381.0, 396.0, 258.5],"true", 2),
(self.obj21148,self.obj21151,[377.0, 381.0, 307.0, 258.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__Transition
    self.drawConnections(
(self.obj124,self.obj10637,[317.0, 253.0, 345.0, 195.0],"true", 2) )

newfunction = trans2instTRUE_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
