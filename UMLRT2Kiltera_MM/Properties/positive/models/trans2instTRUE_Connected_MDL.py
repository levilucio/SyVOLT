"""
__trans2instTRUE_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Tue Feb 17 16:15:09 2015
______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__SIBLING0 import *
from MT_pre__directLink_S import *
from MT_pre__Transition import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__Transition import *
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

def trans2instTRUE_Connected_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('trans2instTRUE_Connected')
    # --- ASG attributes over ---


    self.obj31666=LHS(self)
    self.obj31666.isGraphObjectVisual = True

    if(hasattr(self.obj31666, '_setHierarchicalLink')):
      self.obj31666._setHierarchicalLink(False)

    # constraint
    self.obj31666.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj31666.constraint.setHeight(15)

    self.obj31666.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,40.0,self.obj31666)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31666.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31666)
    self.globalAndLocalPostcondition(self.obj31666, rootNode)
    self.obj31666.postAction( rootNode.CREATE )

    self.obj31667=MT_pre__State(self)
    self.obj31667.isGraphObjectVisual = True

    if(hasattr(self.obj31667, '_setHierarchicalLink')):
      self.obj31667._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31667.MT_pivotOut__.setValue('')
    self.obj31667.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31667.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31667.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31667.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31667.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31667.MT_pivotIn__.setValue('')
    self.obj31667.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31667.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj31667.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31667.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31667.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31667.MT_pre__name.setHeight(15)

    self.obj31667.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(40.0,80.0,self.obj31667)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31667.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31667)
    self.globalAndLocalPostcondition(self.obj31667, rootNode)
    self.obj31667.postAction( rootNode.CREATE )

    self.obj31668=MT_pre__SIBLING0(self)
    self.obj31668.isGraphObjectVisual = True

    if(hasattr(self.obj31668, '_setHierarchicalLink')):
      self.obj31668._setHierarchicalLink(False)

    # MT_label__
    self.obj31668.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj31668.MT_pivotOut__.setValue('')
    self.obj31668.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31668.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31668.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31668.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31668.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj31668.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31668.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31668.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31668.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj31668.MT_pivotIn__.setValue('')
    self.obj31668.MT_pivotIn__.setNone()

    self.obj31668.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(240.0,120.0,self.obj31668)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31668.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31668)
    self.globalAndLocalPostcondition(self.obj31668, rootNode)
    self.obj31668.postAction( rootNode.CREATE )

    self.obj31669=MT_pre__directLink_S(self)
    self.obj31669.isGraphObjectVisual = True

    if(hasattr(self.obj31669, '_setHierarchicalLink')):
      self.obj31669._setHierarchicalLink(False)

    # MT_label__
    self.obj31669.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj31669.MT_pivotOut__.setValue('')
    self.obj31669.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31669.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31669.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31669.MT_pivotIn__.setValue('')
    self.obj31669.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj31669.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31669.MT_pre__associationType.setHeight(15)

    self.obj31669.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(277.0,245.0,self.obj31669)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31669.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31669)
    self.globalAndLocalPostcondition(self.obj31669, rootNode)
    self.obj31669.postAction( rootNode.CREATE )

    self.obj31670=MT_pre__directLink_S(self)
    self.obj31670.isGraphObjectVisual = True

    if(hasattr(self.obj31670, '_setHierarchicalLink')):
      self.obj31670._setHierarchicalLink(False)

    # MT_label__
    self.obj31670.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj31670.MT_pivotOut__.setValue('')
    self.obj31670.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31670.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31670.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj31670.MT_pivotIn__.setValue('')
    self.obj31670.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj31670.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31670.MT_pre__associationType.setHeight(15)

    self.obj31670.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(377.0,265.0,self.obj31670)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj31670.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31670)
    self.globalAndLocalPostcondition(self.obj31670, rootNode)
    self.obj31670.postAction( rootNode.CREATE )

    self.obj31671=MT_pre__Transition(self)
    self.obj31671.isGraphObjectVisual = True

    if(hasattr(self.obj31671, '_setHierarchicalLink')):
      self.obj31671._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31671.MT_pivotOut__.setValue('')
    self.obj31671.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31671.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31671.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31671.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31671.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31671.MT_pivotIn__.setValue('')
    self.obj31671.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31671.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj31671.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31671.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31671.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31671.MT_pre__name.setHeight(15)

    self.obj31671.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(120.0,260.0,self.obj31671)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31671.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31671)
    self.globalAndLocalPostcondition(self.obj31671, rootNode)
    self.obj31671.postAction( rootNode.CREATE )

    # Connections for obj31666 (graphObject_: Obj11) of type LHS
    self.drawConnections(
 )
    # Connections for obj31667 (graphObject_: Obj12) of type MT_pre__State
    self.drawConnections(
(self.obj31667,self.obj31669,[237.0, 155.0, 277.0, 245.0],"true", 2) )
    # Connections for obj31668 (graphObject_: Obj13) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj31669 (graphObject_: Obj14) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj31669,self.obj31671,[277.0, 245.0, 317.0, 335.0],"true", 2) )
    # Connections for obj31670 (graphObject_: Obj15) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj31670,self.obj31668,[377.0, 265.0, 437.0, 195.0],"true", 2) )
    # Connections for obj31671 (graphObject_: Obj16) of type MT_pre__Transition
    self.drawConnections(
(self.obj31671,self.obj31670,[317.0, 335.0, 377.0, 265.0],"true", 2) )

newfunction = trans2instTRUE_Connected_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
