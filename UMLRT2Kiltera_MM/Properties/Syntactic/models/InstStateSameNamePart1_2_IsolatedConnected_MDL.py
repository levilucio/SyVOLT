"""
__InstStateSameNamePart1_2_IsolatedConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Feb 27 15:52:57 2015
________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__State import *
from MT_pre__Attribute import *
from MT_pre__hasAttribute_S import *
from LHS import *
from graph_MT_pre__State import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__hasAttribute_S import *
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

def InstStateSameNamePart1_2_IsolatedConnected_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('InstStateSameNamePart1_2_IsolatedConnected')
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


    self.obj42208=MT_pre__State(self)
    self.obj42208.isGraphObjectVisual = True

    if(hasattr(self.obj42208, '_setHierarchicalLink')):
      self.obj42208._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42208.MT_pivotOut__.setValue('')
    self.obj42208.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42208.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42208.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42208.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42208.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42208.MT_pivotIn__.setValue('')
    self.obj42208.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42208.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj42208.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42208.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42208.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42208.MT_pre__name.setHeight(15)

    self.obj42208.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(120.0,120.0,self.obj42208)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42208.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42208)
    self.globalAndLocalPostcondition(self.obj42208, rootNode)
    self.obj42208.postAction( rootNode.CREATE )

    self.obj136=MT_pre__Attribute(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj136.MT_pivotOut__.setValue('')
    self.obj136.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj136.MT_subtypeMatching__.setValue(('True', 0))
    self.obj136.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj136.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj136.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj136.MT_pivotIn__.setValue('')
    self.obj136.MT_pivotIn__.setNone()

    # MT_label__
    self.obj136.MT_label__.setValue('2')

    # MT_pre__name
    self.obj136.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj136.MT_pre__name.setHeight(15)

    self.obj136.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,260.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj42209=MT_pre__hasAttribute_S(self)
    self.obj42209.isGraphObjectVisual = True

    if(hasattr(self.obj42209, '_setHierarchicalLink')):
      self.obj42209._setHierarchicalLink(False)

    # MT_label__
    self.obj42209.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj42209.MT_pivotOut__.setValue('')
    self.obj42209.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42209.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42209.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42209.MT_pivotIn__.setValue('')
    self.obj42209.MT_pivotIn__.setNone()

    self.obj42209.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(368.5,260.0,self.obj42209)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42209.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42209)
    self.globalAndLocalPostcondition(self.obj42209, rootNode)
    self.obj42209.postAction( rootNode.CREATE )

    self.obj120=LHS(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # constraint
    self.obj120.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\n#return True\nif (PreNode(\'2\')[\'name\']==\'name\'):\n   return True\nreturn False   \n')
    self.obj120.constraint.setHeight(15)

    self.obj120.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    # Connections for obj42208 (graphObject_: Obj10) of type MT_pre__State
    self.drawConnections(
(self.obj42208,self.obj42209,[317.0, 195.0, 368.5, 260.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj8) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj42209 (graphObject_: Obj11) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj42209,self.obj136,[368.5, 260.0, 420.0, 325.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = InstStateSameNamePart1_2_IsolatedConnected_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
