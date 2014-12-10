"""
__ECUVDDistConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu May 23 12:24:37 2013
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__ECU import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__VirtualDevice import *
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

def ECUVDDistConnected_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__GM2AUTOSAR_MM ---
    if( MT_pre__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_pre__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_pre__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_pre__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_pre__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ECUVDDistConnected')
    # --- ASG attributes over ---


    self.obj1485=MT_pre__ECU(self)
    self.obj1485.isGraphObjectVisual = True

    if(hasattr(self.obj1485, '_setHierarchicalLink')):
      self.obj1485._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1485.MT_pivotOut__.setValue('')
    self.obj1485.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1485.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1485.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1485.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1485.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1485.MT_pivotIn__.setValue('')
    self.obj1485.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1485.MT_label__.setValue('1')

    # MT_pre__name
    self.obj1485.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1485.MT_pre__name.setHeight(15)

    self.obj1485.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(100.0,80.0,self.obj1485)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1485.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1485)
    self.globalAndLocalPostcondition(self.obj1485, rootNode)
    self.obj1485.postAction( rootNode.CREATE )

    self.obj1486=MT_pre__VirtualDevice(self)
    self.obj1486.isGraphObjectVisual = True

    if(hasattr(self.obj1486, '_setHierarchicalLink')):
      self.obj1486._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1486.MT_pivotOut__.setValue('')
    self.obj1486.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1486.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1486.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1486.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1486.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1486.MT_pivotIn__.setValue('')
    self.obj1486.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1486.MT_label__.setValue('2')

    # MT_pre__name
    self.obj1486.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1486.MT_pre__name.setHeight(15)

    self.obj1486.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(100.0,320.0,self.obj1486)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1486.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1486)
    self.globalAndLocalPostcondition(self.obj1486, rootNode)
    self.obj1486.postAction( rootNode.CREATE )

    self.obj1487=MT_pre__Distributable(self)
    self.obj1487.isGraphObjectVisual = True

    if(hasattr(self.obj1487, '_setHierarchicalLink')):
      self.obj1487._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1487.MT_pivotOut__.setValue('')
    self.obj1487.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1487.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1487.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1487.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1487.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1487.MT_pivotIn__.setValue('')
    self.obj1487.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1487.MT_label__.setValue('3')

    # MT_pre__name
    self.obj1487.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1487.MT_pre__name.setHeight(15)

    self.obj1487.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(320.0,200.0,self.obj1487)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1487.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1487)
    self.globalAndLocalPostcondition(self.obj1487, rootNode)
    self.obj1487.postAction( rootNode.CREATE )

    self.obj1488=MT_pre__directLink_S(self)
    self.obj1488.isGraphObjectVisual = True

    if(hasattr(self.obj1488, '_setHierarchicalLink')):
      self.obj1488._setHierarchicalLink(False)

    # MT_label__
    self.obj1488.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj1488.MT_pivotOut__.setValue('')
    self.obj1488.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1488.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1488.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1488.MT_pivotIn__.setValue('')
    self.obj1488.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1488.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1488.MT_pre__associationType.setHeight(15)

    self.obj1488.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(270.0,274.0,self.obj1488)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1488.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1488)
    self.globalAndLocalPostcondition(self.obj1488, rootNode)
    self.obj1488.postAction( rootNode.CREATE )

    self.obj1489=MT_pre__directLink_S(self)
    self.obj1489.isGraphObjectVisual = True

    if(hasattr(self.obj1489, '_setHierarchicalLink')):
      self.obj1489._setHierarchicalLink(False)

    # MT_label__
    self.obj1489.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj1489.MT_pivotOut__.setValue('')
    self.obj1489.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1489.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1489.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1489.MT_pivotIn__.setValue('')
    self.obj1489.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1489.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1489.MT_pre__associationType.setHeight(15)

    self.obj1489.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(380.0,334.0,self.obj1489)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1489.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1489)
    self.globalAndLocalPostcondition(self.obj1489, rootNode)
    self.obj1489.postAction( rootNode.CREATE )

    self.obj1484=LHS(self)
    self.obj1484.isGraphObjectVisual = True

    if(hasattr(self.obj1484, '_setHierarchicalLink')):
      self.obj1484._setHierarchicalLink(False)

    # constraint
    self.obj1484.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj1484.constraint.setHeight(15)

    self.obj1484.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj1484)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1484.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1484)
    self.globalAndLocalPostcondition(self.obj1484, rootNode)
    self.obj1484.postAction( rootNode.CREATE )

    # Connections for obj1485 (graphObject_: Obj5) of type MT_pre__ECU
    self.drawConnections(
(self.obj1485,self.obj1488,[270.0, 154.0, 270.0, 274.0],"true", 2) )
    # Connections for obj1486 (graphObject_: Obj6) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj1486,self.obj1489,[270.0, 394.0, 380.0, 334.0],"true", 2) )
    # Connections for obj1487 (graphObject_: Obj7) of type MT_pre__Distributable
    self.drawConnections(
 )
    # Connections for obj1488 (graphObject_: Obj8) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1488,self.obj1486,[270.0, 274.0, 270.0, 394.0],"true", 2) )
    # Connections for obj1489 (graphObject_: Obj9) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1489,self.obj1487,[380.0, 334.0, 490.0, 274.0],"true", 2) )
    # Connections for obj1484 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )

newfunction = ECUVDDistConnected_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
