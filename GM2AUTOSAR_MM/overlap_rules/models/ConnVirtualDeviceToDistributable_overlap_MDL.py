"""
__ConnVirtualDeviceToDistributable_overlap_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Jun  6 11:52:21 2013
______________________________________________________________________________________________________
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

def ConnVirtualDeviceToDistributable_overlap_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ConnVirtualDeviceToDistributable_overlap')
    # --- ASG attributes over ---


    self.obj55=MT_pre__ECU(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj55.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    # MT_label__
    self.obj55.MT_label__.setValue('1')

    # MT_pre__name
    self.obj55.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__name.setHeight(15)

    self.obj55.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(100.0,80.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=MT_pre__VirtualDevice(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj56.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    # MT_label__
    self.obj56.MT_label__.setValue('2')

    # MT_pre__name
    self.obj56.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__name.setHeight(15)

    self.obj56.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(100.0,320.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj8512=MT_pre__Distributable(self)
    self.obj8512.isGraphObjectVisual = True

    if(hasattr(self.obj8512, '_setHierarchicalLink')):
      self.obj8512._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj8512.MT_pivotOut__.setValue('')
    self.obj8512.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8512.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8512.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj8512.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8512.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj8512.MT_pivotIn__.setValue('')
    self.obj8512.MT_pivotIn__.setNone()

    # MT_label__
    self.obj8512.MT_label__.setValue('5')

    # MT_pre__name
    self.obj8512.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8512.MT_pre__name.setHeight(15)

    self.obj8512.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(320.0,180.0,self.obj8512)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj8512.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8512)
    self.globalAndLocalPostcondition(self.obj8512, rootNode)
    self.obj8512.postAction( rootNode.CREATE )

    self.obj58=MT_pre__directLink_S(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # MT_label__
    self.obj58.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj58.MT_pivotOut__.setValue('')
    self.obj58.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj58.MT_subtypeMatching__.setValue(('True', 0))
    self.obj58.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj58.MT_pivotIn__.setValue('')
    self.obj58.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj58.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj58.MT_pre__associationType.setHeight(15)

    self.obj58.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(270.0,274.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj8513=MT_pre__directLink_S(self)
    self.obj8513.isGraphObjectVisual = True

    if(hasattr(self.obj8513, '_setHierarchicalLink')):
      self.obj8513._setHierarchicalLink(False)

    # MT_label__
    self.obj8513.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj8513.MT_pivotOut__.setValue('')
    self.obj8513.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8513.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8513.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj8513.MT_pivotIn__.setValue('')
    self.obj8513.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj8513.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8513.MT_pre__associationType.setHeight(15)

    self.obj8513.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(380.0,324.0,self.obj8513)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj8513.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8513)
    self.globalAndLocalPostcondition(self.obj8513, rootNode)
    self.obj8513.postAction( rootNode.CREATE )

    self.obj60=LHS(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # constraint
    self.obj60.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj60.constraint.setHeight(15)

    self.obj60.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    # Connections for obj55 (graphObject_: Obj0) of type MT_pre__ECU
    self.drawConnections(
(self.obj55,self.obj58,[270.0, 154.0, 270.0, 274.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj1) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj56,self.obj8513,[270.0, 394.0, 380.0, 324.0],"true", 2) )
    # Connections for obj8512 (graphObject_: Obj6) of type MT_pre__Distributable
    self.drawConnections(
 )
    # Connections for obj58 (graphObject_: Obj3) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj58,self.obj56,[270.0, 274.0, 270.0, 394.0],"true", 2) )
    # Connections for obj8513 (graphObject_: Obj7) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj8513,self.obj8512,[380.0, 324.0, 490.0, 254.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj5) of type LHS
    self.drawConnections(
 )

newfunction = ConnVirtualDeviceToDistributable_overlap_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
