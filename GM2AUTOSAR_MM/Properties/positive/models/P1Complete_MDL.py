"""
__P1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Sep 16 18:24:09 2013
________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__ExecFrame import *
from MT_pre__Signal import *
from MT_pre__CompositionType import *
from MT_pre__PPortPrototype import *
from MT_pre__directLink_S import *
from MT_pre__directLink_T import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__ECU import *
from graph_MT_pre__PPortPrototype import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__ExecFrame import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__VirtualDevice import *
from graph_MT_pre__Signal import *
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

def P1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('P1Complete')
    # --- ASG attributes over ---


    self.obj1550=MT_pre__ECU(self)
    self.obj1550.isGraphObjectVisual = True

    if(hasattr(self.obj1550, '_setHierarchicalLink')):
      self.obj1550._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1550.MT_pivotOut__.setValue('')
    self.obj1550.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1550.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1550.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1550.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1550.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1550.MT_pivotIn__.setValue('')
    self.obj1550.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1550.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj1550.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1550.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1550.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1550.MT_pre__name.setHeight(15)

    self.obj1550.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(76.0,53.0,self.obj1550)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1550.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1550)
    self.globalAndLocalPostcondition(self.obj1550, rootNode)
    self.obj1550.postAction( rootNode.CREATE )

    self.obj1551=MT_pre__VirtualDevice(self)
    self.obj1551.isGraphObjectVisual = True

    if(hasattr(self.obj1551, '_setHierarchicalLink')):
      self.obj1551._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1551.MT_pivotOut__.setValue('')
    self.obj1551.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1551.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1551.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1551.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1551.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1551.MT_pivotIn__.setValue('')
    self.obj1551.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1551.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj1551.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1551.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1551.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1551.MT_pre__name.setHeight(15)

    self.obj1551.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(260.0,52.0,self.obj1551)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1551.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1551)
    self.globalAndLocalPostcondition(self.obj1551, rootNode)
    self.obj1551.postAction( rootNode.CREATE )

    self.obj1552=MT_pre__Distributable(self)
    self.obj1552.isGraphObjectVisual = True

    if(hasattr(self.obj1552, '_setHierarchicalLink')):
      self.obj1552._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1552.MT_pivotOut__.setValue('')
    self.obj1552.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1552.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1552.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1552.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1552.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1552.MT_pivotIn__.setValue('')
    self.obj1552.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1552.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj1552.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1552.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1552.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1552.MT_pre__name.setHeight(15)

    self.obj1552.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(352.0,185.0,self.obj1552)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1552.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1552)
    self.globalAndLocalPostcondition(self.obj1552, rootNode)
    self.obj1552.postAction( rootNode.CREATE )

    self.obj1553=MT_pre__ExecFrame(self)
    self.obj1553.isGraphObjectVisual = True

    if(hasattr(self.obj1553, '_setHierarchicalLink')):
      self.obj1553._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1553.MT_pivotOut__.setValue('')
    self.obj1553.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1553.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1553.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1553.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1553.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1553.MT_pivotIn__.setValue('')
    self.obj1553.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1553.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj1553.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1553.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1553.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1553.MT_pre__name.setHeight(15)

    self.obj1553.graphClass_= graph_MT_pre__ExecFrame
    if self.genGraphics:
       new_obj = graph_MT_pre__ExecFrame(285.0,320.0,self.obj1553)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1553.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1553)
    self.globalAndLocalPostcondition(self.obj1553, rootNode)
    self.obj1553.postAction( rootNode.CREATE )

    self.obj1554=MT_pre__Signal(self)
    self.obj1554.isGraphObjectVisual = True

    if(hasattr(self.obj1554, '_setHierarchicalLink')):
      self.obj1554._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1554.MT_pivotOut__.setValue('')
    self.obj1554.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1554.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1554.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1554.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1554.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1554.MT_pivotIn__.setValue('')
    self.obj1554.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1554.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj1554.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1554.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1554.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1554.MT_pre__name.setHeight(15)

    self.obj1554.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(100.0,320.0,self.obj1554)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1554.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1554)
    self.globalAndLocalPostcondition(self.obj1554, rootNode)
    self.obj1554.postAction( rootNode.CREATE )

    self.obj1559=MT_pre__CompositionType(self)
    self.obj1559.isGraphObjectVisual = True

    if(hasattr(self.obj1559, '_setHierarchicalLink')):
      self.obj1559._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1559.MT_pivotOut__.setValue('')
    self.obj1559.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1559.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1559.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1559.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1559.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1559.MT_pivotIn__.setValue('')
    self.obj1559.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1559.MT_label__.setValue('10')

    # MT_pre__cardinality
    self.obj1559.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1559.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1559.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1559.MT_pre__name.setHeight(15)

    self.obj1559.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(72.0,160.0,self.obj1559)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1559.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1559)
    self.globalAndLocalPostcondition(self.obj1559, rootNode)
    self.obj1559.postAction( rootNode.CREATE )

    self.obj1560=MT_pre__PPortPrototype(self)
    self.obj1560.isGraphObjectVisual = True

    if(hasattr(self.obj1560, '_setHierarchicalLink')):
      self.obj1560._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1560.MT_pivotOut__.setValue('')
    self.obj1560.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1560.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1560.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1560.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1560.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1560.MT_pivotIn__.setValue('')
    self.obj1560.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1560.MT_label__.setValue('11')

    # MT_pre__cardinality
    self.obj1560.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1560.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1560.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1560.MT_pre__name.setHeight(15)

    self.obj1560.graphClass_= graph_MT_pre__PPortPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__PPortPrototype(80.0,240.0,self.obj1560)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__PPortPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1560.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1560)
    self.globalAndLocalPostcondition(self.obj1560, rootNode)
    self.obj1560.postAction( rootNode.CREATE )

    self.obj1555=MT_pre__directLink_S(self)
    self.obj1555.isGraphObjectVisual = True

    if(hasattr(self.obj1555, '_setHierarchicalLink')):
      self.obj1555._setHierarchicalLink(False)

    # MT_label__
    self.obj1555.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj1555.MT_pivotOut__.setValue('')
    self.obj1555.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1555.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1555.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1555.MT_pivotIn__.setValue('')
    self.obj1555.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1555.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1555.MT_pre__associationType.setHeight(15)

    self.obj1555.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(336.5,126.5,self.obj1555)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1555.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1555)
    self.globalAndLocalPostcondition(self.obj1555, rootNode)
    self.obj1555.postAction( rootNode.CREATE )

    self.obj1556=MT_pre__directLink_S(self)
    self.obj1556.isGraphObjectVisual = True

    if(hasattr(self.obj1556, '_setHierarchicalLink')):
      self.obj1556._setHierarchicalLink(False)

    # MT_label__
    self.obj1556.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj1556.MT_pivotOut__.setValue('')
    self.obj1556.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1556.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1556.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1556.MT_pivotIn__.setValue('')
    self.obj1556.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1556.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1556.MT_pre__associationType.setHeight(15)

    self.obj1556.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(470.0,186.0,self.obj1556)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1556.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1556)
    self.globalAndLocalPostcondition(self.obj1556, rootNode)
    self.obj1556.postAction( rootNode.CREATE )

    self.obj1557=MT_pre__directLink_S(self)
    self.obj1557.isGraphObjectVisual = True

    if(hasattr(self.obj1557, '_setHierarchicalLink')):
      self.obj1557._setHierarchicalLink(False)

    # MT_label__
    self.obj1557.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj1557.MT_pivotOut__.setValue('')
    self.obj1557.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1557.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1557.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1557.MT_pivotIn__.setValue('')
    self.obj1557.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1557.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1557.MT_pre__associationType.setHeight(15)

    self.obj1557.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.5,306.0,self.obj1557)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1557.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1557)
    self.globalAndLocalPostcondition(self.obj1557, rootNode)
    self.obj1557.postAction( rootNode.CREATE )

    self.obj1558=MT_pre__directLink_S(self)
    self.obj1558.isGraphObjectVisual = True

    if(hasattr(self.obj1558, '_setHierarchicalLink')):
      self.obj1558._setHierarchicalLink(False)

    # MT_label__
    self.obj1558.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj1558.MT_pivotOut__.setValue('')
    self.obj1558.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1558.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1558.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1558.MT_pivotIn__.setValue('')
    self.obj1558.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1558.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1558.MT_pre__associationType.setHeight(15)

    self.obj1558.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(370.5,380.0,self.obj1558)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1558.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1558)
    self.globalAndLocalPostcondition(self.obj1558, rootNode)
    self.obj1558.postAction( rootNode.CREATE )

    self.obj1562=MT_pre__directLink_T(self)
    self.obj1562.isGraphObjectVisual = True

    if(hasattr(self.obj1562, '_setHierarchicalLink')):
      self.obj1562._setHierarchicalLink(False)

    # MT_label__
    self.obj1562.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj1562.MT_pivotOut__.setValue('')
    self.obj1562.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1562.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1562.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1562.MT_pivotIn__.setValue('')
    self.obj1562.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1562.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1562.MT_pre__associationType.setHeight(15)

    self.obj1562.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(249.0,273.0,self.obj1562)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1562.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1562)
    self.globalAndLocalPostcondition(self.obj1562, rootNode)
    self.obj1562.postAction( rootNode.CREATE )

    self.obj1578=MT_pre__trace_link(self)
    self.obj1578.isGraphObjectVisual = True

    if(hasattr(self.obj1578, '_setHierarchicalLink')):
      self.obj1578._setHierarchicalLink(False)

    # MT_label__
    self.obj1578.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj1578.MT_pivotOut__.setValue('')
    self.obj1578.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1578.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1578.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1578.MT_pivotIn__.setValue('')
    self.obj1578.MT_pivotIn__.setNone()

    self.obj1578.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(245.5,180.0,self.obj1578)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1578.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1578)
    self.globalAndLocalPostcondition(self.obj1578, rootNode)
    self.obj1578.postAction( rootNode.CREATE )

    self.obj1579=MT_pre__trace_link(self)
    self.obj1579.isGraphObjectVisual = True

    if(hasattr(self.obj1579, '_setHierarchicalLink')):
      self.obj1579._setHierarchicalLink(False)

    # MT_label__
    self.obj1579.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj1579.MT_pivotOut__.setValue('')
    self.obj1579.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1579.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1579.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1579.MT_pivotIn__.setValue('')
    self.obj1579.MT_pivotIn__.setNone()

    self.obj1579.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(354.0,353.5,self.obj1579)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1579.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1579)
    self.globalAndLocalPostcondition(self.obj1579, rootNode)
    self.obj1579.postAction( rootNode.CREATE )

    self.obj1549=LHS(self)
    self.obj1549.isGraphObjectVisual = True

    if(hasattr(self.obj1549, '_setHierarchicalLink')):
      self.obj1549._setHierarchicalLink(False)

    # constraint
    self.obj1549.constraint.setValue('if PreNode(\'1\')[\'cardinality\']==\'+\' and PreNode(\'2\')[\'cardinality\']==\'+\' and PreNode(\'3\')[\'cardinality\']==\'+\' and PreNode(\'4\')[\'cardinality\']==\'+\' and PreNode(\'5\')[\'cardinality\']==\'1\' and PreNode(\'10\')[\'cardinality\']==\'+\' and PreNode(\'11\')[\'cardinality\']==\'+\' and PreNode(\'6\')[\'associationType\']==\'virtualDevice\' and PreNode(\'7\')[\'associationType\']==\'distributable\' and PreNode(\'8\')[\'associationType\']==\'execFrame\' and PreNode(\'9\')[\'associationType\']==\'provided\' and PreNode(\'12\')[\'associationType\']==\'port\':\n    return True\nreturn False\n')
    self.obj1549.constraint.setHeight(15)

    self.obj1549.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,40.0,self.obj1549)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1549.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1549)
    self.globalAndLocalPostcondition(self.obj1549, rootNode)
    self.obj1549.postAction( rootNode.CREATE )

    # Connections for obj1550 (graphObject_: Obj16) of type MT_pre__ECU
    self.drawConnections(
(self.obj1550,self.obj1555,[246.0, 127.0, 336.5, 126.5],"true", 2) )
    # Connections for obj1551 (graphObject_: Obj17) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj1551,self.obj1556,[430.0, 126.0, 470.0, 186.0],"true", 2) )
    # Connections for obj1552 (graphObject_: Obj18) of type MT_pre__Distributable
    self.drawConnections(
(self.obj1552,self.obj1557,[522.0, 259.0, 490.5, 306.0],"true", 2) )
    # Connections for obj1553 (graphObject_: Obj19) of type MT_pre__ExecFrame
    self.drawConnections(
(self.obj1553,self.obj1558,[455.0, 394.0, 370.5, 380.0],"true", 2) )
    # Connections for obj1554 (graphObject_: Obj20) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj1559 (graphObject_: Obj25) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj1559,self.obj1562,[245.0, 233.0, 249.0, 273.0],"true", 2),
(self.obj1559,self.obj1578,[245.0, 233.0, 245.5, 180.0],"true", 2) )
    # Connections for obj1560 (graphObject_: Obj26) of type MT_pre__PPortPrototype
    self.drawConnections(
(self.obj1560,self.obj1579,[253.0, 313.0, 354.0, 353.5],"true", 2) )
    # Connections for obj1555 (graphObject_: Obj21) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1555,self.obj1551,[336.5, 126.5, 430.0, 126.0],"true", 2) )
    # Connections for obj1556 (graphObject_: Obj22) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1556,self.obj1552,[470.0, 186.0, 522.0, 259.0],"true", 2) )
    # Connections for obj1557 (graphObject_: Obj23) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1557,self.obj1553,[490.5, 306.0, 455.0, 394.0],"true", 2) )
    # Connections for obj1558 (graphObject_: Obj24) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1558,self.obj1554,[370.5, 380.0, 270.0, 394.0],"true", 2) )
    # Connections for obj1562 (graphObject_: Obj27) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj1562,self.obj1560,[249.0, 273.0, 253.0, 313.0],"true", 2) )
    # Connections for obj1578 (graphObject_: Obj28) of type MT_pre__trace_link
    self.drawConnections(
(self.obj1578,self.obj1550,[245.5, 180.0, 246.0, 127.0],"true", 2) )
    # Connections for obj1579 (graphObject_: Obj29) of type MT_pre__trace_link
    self.drawConnections(
(self.obj1579,self.obj1553,[354.0, 353.5, 455.0, 394.0],"true", 2) )
    # Connections for obj1549 (graphObject_: Obj15) of type LHS
    self.drawConnections(
 )

newfunction = P1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
