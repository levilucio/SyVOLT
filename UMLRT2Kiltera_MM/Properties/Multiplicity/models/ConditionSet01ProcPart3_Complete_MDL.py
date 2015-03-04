"""
__ConditionSet01ProcPart3_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Mar  4 17:07:29 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ConditionSet import *
from MT_pre__directLink_T import *
from MT_pre__Proc import *
from LHS import *
from graph_MT_pre__ConditionSet import *
from graph_MT_pre__directLink_T import *
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

def ConditionSet01ProcPart3_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ConditionSet01ProcPart3_Complete')
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


    self.obj124=MT_pre__ConditionSet(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_label__
    self.obj124.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
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

    self.obj124.graphClass_= graph_MT_pre__ConditionSet
    if self.genGraphics:
       new_obj = graph_MT_pre__ConditionSet(40.0,40.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ConditionSet", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj10638=MT_pre__directLink_T(self)
    self.obj10638.isGraphObjectVisual = True

    if(hasattr(self.obj10638, '_setHierarchicalLink')):
      self.obj10638._setHierarchicalLink(False)

    # MT_label__
    self.obj10638.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj10638.MT_pivotOut__.setValue('')
    self.obj10638.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10638.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10638.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10638.MT_pivotIn__.setValue('')
    self.obj10638.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10638.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10638.MT_pre__associationType.setHeight(15)

    self.obj10638.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(176.0,220.0,self.obj10638)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10638.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10638)
    self.globalAndLocalPostcondition(self.obj10638, rootNode)
    self.obj10638.postAction( rootNode.CREATE )

    self.obj31676=MT_pre__directLink_T(self)
    self.obj31676.isGraphObjectVisual = True

    if(hasattr(self.obj31676, '_setHierarchicalLink')):
      self.obj31676._setHierarchicalLink(False)

    # MT_label__
    self.obj31676.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj31676.MT_pivotOut__.setValue('')
    self.obj31676.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31676.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31676.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31676.MT_pivotIn__.setValue('')
    self.obj31676.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj31676.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31676.MT_pre__associationType.setHeight(15)

    self.obj31676.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(347.0,171.0,self.obj31676)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31676.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31676)
    self.globalAndLocalPostcondition(self.obj31676, rootNode)
    self.obj31676.postAction( rootNode.CREATE )

    self.obj10637=MT_pre__Proc(self)
    self.obj10637.isGraphObjectVisual = True

    if(hasattr(self.obj10637, '_setHierarchicalLink')):
      self.obj10637._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10637.MT_pivotOut__.setValue('')
    self.obj10637.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10637.MT_subtypeMatching__.setValue(('True', 1))
    self.obj10637.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10637.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10637.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10637.MT_pivotIn__.setValue('')
    self.obj10637.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10637.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10637.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10637.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10637.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10637.MT_pre__name.setHeight(15)

    self.obj10637.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(40.0,200.0,self.obj10637)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10637.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10637)
    self.globalAndLocalPostcondition(self.obj10637, rootNode)
    self.obj10637.postAction( rootNode.CREATE )

    self.obj31675=MT_pre__Proc(self)
    self.obj31675.isGraphObjectVisual = True

    if(hasattr(self.obj31675, '_setHierarchicalLink')):
      self.obj31675._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31675.MT_pivotOut__.setValue('')
    self.obj31675.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31675.MT_subtypeMatching__.setValue(('True', 1))
    self.obj31675.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31675.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31675.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31675.MT_pivotIn__.setValue('')
    self.obj31675.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31675.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj31675.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31675.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31675.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31675.MT_pre__name.setHeight(15)

    self.obj31675.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(220.0,100.0,self.obj31675)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31675.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31675)
    self.globalAndLocalPostcondition(self.obj31675, rootNode)
    self.obj31675.postAction( rootNode.CREATE )

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

    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__ConditionSet
    self.drawConnections(
(self.obj124,self.obj10638,[257.0, 141.0, 176.0, 220.0],"true", 2),
(self.obj124,self.obj31676,[257.0, 141.0, 347.0, 171.0],"true", 2) )
    # Connections for obj10638 (graphObject_: Obj3) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10638,self.obj10637,[176.0, 220.0, 257.0, 301.0],"true", 2) )
    # Connections for obj31676 (graphObject_: Obj5) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj31676,self.obj31675,[347.0, 171.0, 437.0, 201.0],"true", 2) )
    # Connections for obj10637 (graphObject_: Obj2) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj31675 (graphObject_: Obj4) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = ConditionSet01ProcPart3_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
