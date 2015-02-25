"""
__InstStateSameNamePart1_2_IsolatedConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 23 22:27:39 2015
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


    self.obj94795=LHS(self)
    self.obj94795.isGraphObjectVisual = True

    if(hasattr(self.obj94795, '_setHierarchicalLink')):
      self.obj94795._setHierarchicalLink(False)

    # constraint
    self.obj94795.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\nif (PreNode[\'2\'][\'name\']==\'name\'):\n   return True\nreturn False   \n')
    self.obj94795.constraint.setHeight(15)

    self.obj94795.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj94795)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94795.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94795)
    self.globalAndLocalPostcondition(self.obj94795, rootNode)
    self.obj94795.postAction( rootNode.CREATE )

    self.obj94796=MT_pre__State(self)
    self.obj94796.isGraphObjectVisual = True

    if(hasattr(self.obj94796, '_setHierarchicalLink')):
      self.obj94796._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj94796.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj94796.MT_subtypeMatching__.setValue(('True', 1))
    self.obj94796.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj94796.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj94796.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj94796.MT_pivotIn__.setValue('')
    self.obj94796.MT_pivotIn__.setNone()

    # MT_label__
    self.obj94796.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj94796.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj94796.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj94796.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj94796.MT_pre__name.setHeight(15)

    self.obj94796.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(140.0,100.0,self.obj94796)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94796.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94796)
    self.globalAndLocalPostcondition(self.obj94796, rootNode)
    self.obj94796.postAction( rootNode.CREATE )

    self.obj94801=MT_pre__hasAttribute_S(self)
    self.obj94801.isGraphObjectVisual = True

    if(hasattr(self.obj94801, '_setHierarchicalLink')):
      self.obj94801._setHierarchicalLink(False)

    # MT_label__
    self.obj94801.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj94801.MT_pivotOut__.setValue('')
    self.obj94801.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj94801.MT_subtypeMatching__.setValue(('True', 0))
    self.obj94801.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj94801.MT_pivotIn__.setValue('')
    self.obj94801.MT_pivotIn__.setNone()

    self.obj94801.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(408.5,240.0,self.obj94801)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj94801.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94801)
    self.globalAndLocalPostcondition(self.obj94801, rootNode)
    self.obj94801.postAction( rootNode.CREATE )

    self.obj94799=MT_pre__Attribute(self)
    self.obj94799.isGraphObjectVisual = True

    if(hasattr(self.obj94799, '_setHierarchicalLink')):
      self.obj94799._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj94799.MT_pivotOut__.setValue('')
    self.obj94799.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj94799.MT_subtypeMatching__.setValue(('True', 0))
    self.obj94799.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj94799.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\nreturn True\n')
    self.obj94799.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj94799.MT_pivotIn__.setValue('')
    self.obj94799.MT_pivotIn__.setNone()

    # MT_label__
    self.obj94799.MT_label__.setValue('2')

    # MT_pre__name
    self.obj94799.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\nreturn True \n')
    self.obj94799.MT_pre__name.setHeight(15)

    self.obj94799.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(320.0,240.0,self.obj94799)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94799.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94799)
    self.globalAndLocalPostcondition(self.obj94799, rootNode)
    self.obj94799.postAction( rootNode.CREATE )

    # Connections for obj94795 (graphObject_: Obj22) of type LHS
    self.drawConnections(
 )
    # Connections for obj94796 (graphObject_: Obj23) of type MT_pre__State
    self.drawConnections(
(self.obj94796,self.obj94801,[337.0, 175.0, 408.5, 240.0],"true", 2) )
    # Connections for obj94801 (graphObject_: Obj25) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj94801,self.obj94799,[408.5, 240.0, 480.0, 305.0],"true", 2) )
    # Connections for obj94799 (graphObject_: Obj24) of type MT_pre__Attribute
    self.drawConnections(
 )

newfunction = InstStateSameNamePart1_2_IsolatedConnected_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
