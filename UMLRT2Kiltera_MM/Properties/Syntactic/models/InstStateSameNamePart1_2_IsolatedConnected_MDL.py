"""
__InstStateSameNamePart1_2_IsolatedConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sat Feb 28 23:18:21 2015
________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__hasAttribute_S import *
from MT_pre__Attribute import *
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

def InstStateSameNamePart1_2_IsolatedConnected_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('InstStateSameNamePart1_2_IsolatedConnected')
    # --- ASG attributes over ---


    self.obj10662=LHS(self)
    self.obj10662.isGraphObjectVisual = True

    if(hasattr(self.obj10662, '_setHierarchicalLink')):
      self.obj10662._setHierarchicalLink(False)

    # constraint
    self.obj10662.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\n#return True\nif (PreNode(\'2\')[\'name\']==\'name\'):\n   return True\nreturn False   \n')
    self.obj10662.constraint.setHeight(15)

    self.obj10662.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj10662)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10662.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10662)
    self.globalAndLocalPostcondition(self.obj10662, rootNode)
    self.obj10662.postAction( rootNode.CREATE )

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
    self.obj10659.MT_pivotIn__.setValue('')
    self.obj10659.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10659.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj10659.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10659.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10659.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10659.MT_pre__name.setHeight(15)

    self.obj10659.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(120.0,120.0,self.obj10659)
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

    self.obj10661=MT_pre__hasAttribute_S(self)
    self.obj10661.isGraphObjectVisual = True

    if(hasattr(self.obj10661, '_setHierarchicalLink')):
      self.obj10661._setHierarchicalLink(False)

    # MT_label__
    self.obj10661.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj10661.MT_pivotOut__.setValue('')
    self.obj10661.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10661.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10661.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10661.MT_pivotIn__.setValue('')
    self.obj10661.MT_pivotIn__.setNone()

    self.obj10661.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(368.5,260.0,self.obj10661)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10661.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10661)
    self.globalAndLocalPostcondition(self.obj10661, rootNode)
    self.obj10661.postAction( rootNode.CREATE )

    self.obj10660=MT_pre__Attribute(self)
    self.obj10660.isGraphObjectVisual = True

    if(hasattr(self.obj10660, '_setHierarchicalLink')):
      self.obj10660._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10660.MT_pivotOut__.setValue('')
    self.obj10660.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10660.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10660.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj10660.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10660.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj10660.MT_pivotIn__.setValue('')
    self.obj10660.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10660.MT_label__.setValue('2')

    # MT_pre__name
    self.obj10660.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10660.MT_pre__name.setHeight(15)

    self.obj10660.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,260.0,self.obj10660)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10660.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10660)
    self.globalAndLocalPostcondition(self.obj10660, rootNode)
    self.obj10660.postAction( rootNode.CREATE )

    # Connections for obj10662 (graphObject_: Obj21) of type LHS
    self.drawConnections(
 )
    # Connections for obj10659 (graphObject_: Obj18) of type MT_pre__State
    self.drawConnections(
(self.obj10659,self.obj10661,[317.0, 195.0, 368.5, 260.0],"true", 2) )
    # Connections for obj10661 (graphObject_: Obj20) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj10661,self.obj10660,[368.5, 260.0, 420.0, 325.0],"true", 2) )
    # Connections for obj10660 (graphObject_: Obj19) of type MT_pre__Attribute
    self.drawConnections(
 )

newfunction = InstStateSameNamePart1_2_IsolatedConnected_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
