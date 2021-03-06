"""
__Par2ProcsPart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sun Feb 22 11:04:16 2015
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Par import *
from MT_pre__directLink_T import *
from MT_pre__Proc import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Par import *
from graph_MT_pre__Proc import *
from graph_LHS import *
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

def Par2ProcsPart2_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('Par2ProcsPart2_Complete')
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

    self.obj124=MT_pre__Par(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_label__
    self.obj124.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('')
    self.obj124.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 1))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj124.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj124.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj124.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('element1')

    self.obj124.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(34.0,100.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj10645=MT_pre__directLink_T(self)
    self.obj10645.isGraphObjectVisual = True

    if(hasattr(self.obj10645, '_setHierarchicalLink')):
      self.obj10645._setHierarchicalLink(False)

    # MT_label__
    self.obj10645.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj10645.MT_pivotOut__.setValue('')
    self.obj10645.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10645.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10645.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10645.MT_pivotIn__.setValue('')
    self.obj10645.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10645.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10645.MT_pre__associationType.setHeight(15)

    self.obj10645.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(339.5,181.5,self.obj10645)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10645.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10645)
    self.globalAndLocalPostcondition(self.obj10645, rootNode)
    self.obj10645.postAction( rootNode.CREATE )

    self.obj10646=MT_pre__directLink_T(self)
    self.obj10646.isGraphObjectVisual = True

    if(hasattr(self.obj10646, '_setHierarchicalLink')):
      self.obj10646._setHierarchicalLink(False)

    # MT_label__
    self.obj10646.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10646.MT_pivotOut__.setValue('')
    self.obj10646.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10646.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10646.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10646.MT_pivotIn__.setValue('')
    self.obj10646.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10646.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10646.MT_pre__associationType.setHeight(15)

    self.obj10646.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(343.0,252.5,self.obj10646)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10646.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10646)
    self.globalAndLocalPostcondition(self.obj10646, rootNode)
    self.obj10646.postAction( rootNode.CREATE )

    self.obj10643=MT_pre__Proc(self)
    self.obj10643.isGraphObjectVisual = True

    if(hasattr(self.obj10643, '_setHierarchicalLink')):
      self.obj10643._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10643.MT_pivotOut__.setValue('')
    self.obj10643.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10643.MT_subtypeMatching__.setValue(('True', 1))
    self.obj10643.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10643.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10643.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10643.MT_pivotIn__.setValue('')
    self.obj10643.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10643.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10643.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10643.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10643.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10643.MT_pre__name.setHeight(15)

    self.obj10643.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(211.0,61.0,self.obj10643)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10643.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10643)
    self.globalAndLocalPostcondition(self.obj10643, rootNode)
    self.obj10643.postAction( rootNode.CREATE )

    self.obj10644=MT_pre__Proc(self)
    self.obj10644.isGraphObjectVisual = True

    if(hasattr(self.obj10644, '_setHierarchicalLink')):
      self.obj10644._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10644.MT_pivotOut__.setValue('')
    self.obj10644.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10644.MT_subtypeMatching__.setValue(('True', 1))
    self.obj10644.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10644.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10644.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10644.MT_pivotIn__.setValue('')
    self.obj10644.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10644.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj10644.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10644.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10644.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10644.MT_pre__name.setHeight(15)

    self.obj10644.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(218.0,203.0,self.obj10644)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10644.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10644)
    self.globalAndLocalPostcondition(self.obj10644, rootNode)
    self.obj10644.postAction( rootNode.CREATE )

    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__Par
    self.drawConnections(
(self.obj124,self.obj10645,[251.0, 201.0, 339.5, 181.5],"true", 0),
(self.obj124,self.obj10646,[251.0, 201.0, 343.0, 252.5],"true", 0) )
    # Connections for obj10645 (graphObject_: Obj4) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10645,self.obj10643,[339.5, 181.5, 428.0, 162.0],"true", 2) )
    # Connections for obj10646 (graphObject_: Obj5) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10646,self.obj10644,[343.0, 252.5, 435.0, 304.0],"true", 2) )
    # Connections for obj10643 (graphObject_: Obj2) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj10644 (graphObject_: Obj3) of type MT_pre__Proc
    self.drawConnections(
 )

newfunction = Par2ProcsPart2_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
