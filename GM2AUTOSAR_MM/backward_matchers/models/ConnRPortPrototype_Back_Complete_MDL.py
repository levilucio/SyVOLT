"""
__ConnRPortPrototype_Back_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Nov  1 18:43:44 2013
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__ExecFrame import *
from MT_pre__Signal import *
from MT_pre__CompositionType import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__ECU import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__ExecFrame import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__directLink_S import *
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

def ConnRPortPrototype_Back_Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ConnectRPortPrototype_Back_Complete')
    # --- ASG attributes over ---


    self.obj1539=MT_pre__ECU(self)
    self.obj1539.isGraphObjectVisual = True

    if(hasattr(self.obj1539, '_setHierarchicalLink')):
      self.obj1539._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1539.MT_pivotOut__.setValue('')
    self.obj1539.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1539.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1539.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1539.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1539.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1539.MT_pivotIn__.setValue('')
    self.obj1539.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1539.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj1539.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1539.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1539.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1539.MT_pre__name.setHeight(15)

    self.obj1539.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(160.0,320.0,self.obj1539)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1539.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1539)
    self.globalAndLocalPostcondition(self.obj1539, rootNode)
    self.obj1539.postAction( rootNode.CREATE )

    self.obj15651=MT_pre__VirtualDevice(self)
    self.obj15651.isGraphObjectVisual = True

    if(hasattr(self.obj15651, '_setHierarchicalLink')):
      self.obj15651._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj15651.MT_pivotOut__.setValue('')
    self.obj15651.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15651.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15651.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj15651.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15651.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj15651.MT_pivotIn__.setValue('')
    self.obj15651.MT_pivotIn__.setNone()

    # MT_label__
    self.obj15651.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj15651.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15651.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj15651.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15651.MT_pre__name.setHeight(15)

    self.obj15651.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(160.0,420.0,self.obj15651)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15651.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15651)
    self.globalAndLocalPostcondition(self.obj15651, rootNode)
    self.obj15651.postAction( rootNode.CREATE )

    self.obj17377=MT_pre__Distributable(self)
    self.obj17377.isGraphObjectVisual = True

    if(hasattr(self.obj17377, '_setHierarchicalLink')):
      self.obj17377._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj17377.MT_pivotOut__.setValue('')
    self.obj17377.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj17377.MT_subtypeMatching__.setValue(('True', 0))
    self.obj17377.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj17377.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj17377.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj17377.MT_pivotIn__.setValue('')
    self.obj17377.MT_pivotIn__.setNone()

    # MT_label__
    self.obj17377.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj17377.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj17377.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj17377.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj17377.MT_pre__name.setHeight(15)

    self.obj17377.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(320.0,320.0,self.obj17377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj17377.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj17377)
    self.globalAndLocalPostcondition(self.obj17377, rootNode)
    self.obj17377.postAction( rootNode.CREATE )

    self.obj22555=MT_pre__ExecFrame(self)
    self.obj22555.isGraphObjectVisual = True

    if(hasattr(self.obj22555, '_setHierarchicalLink')):
      self.obj22555._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj22555.MT_pivotOut__.setValue('')
    self.obj22555.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj22555.MT_subtypeMatching__.setValue(('True', 0))
    self.obj22555.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj22555.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22555.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj22555.MT_pivotIn__.setValue('')
    self.obj22555.MT_pivotIn__.setNone()

    # MT_label__
    self.obj22555.MT_label__.setValue('6')

    # MT_pre__cardinality
    self.obj22555.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22555.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj22555.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22555.MT_pre__name.setHeight(15)

    self.obj22555.graphClass_= graph_MT_pre__ExecFrame
    if self.genGraphics:
       new_obj = graph_MT_pre__ExecFrame(320.0,420.0,self.obj22555)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22555.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22555)
    self.globalAndLocalPostcondition(self.obj22555, rootNode)
    self.obj22555.postAction( rootNode.CREATE )

    self.obj24281=MT_pre__Signal(self)
    self.obj24281.isGraphObjectVisual = True

    if(hasattr(self.obj24281, '_setHierarchicalLink')):
      self.obj24281._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj24281.MT_pivotOut__.setValue('')
    self.obj24281.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24281.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24281.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj24281.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24281.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj24281.MT_pivotIn__.setValue('')
    self.obj24281.MT_pivotIn__.setNone()

    # MT_label__
    self.obj24281.MT_label__.setValue('8')

    # MT_pre__cardinality
    self.obj24281.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24281.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj24281.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24281.MT_pre__name.setHeight(15)

    self.obj24281.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(320.0,540.0,self.obj24281)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24281.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24281)
    self.globalAndLocalPostcondition(self.obj24281, rootNode)
    self.obj24281.postAction( rootNode.CREATE )

    self.obj24283=MT_pre__CompositionType(self)
    self.obj24283.isGraphObjectVisual = True

    if(hasattr(self.obj24283, '_setHierarchicalLink')):
      self.obj24283._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj24283.MT_pivotOut__.setValue('')
    self.obj24283.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24283.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24283.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj24283.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24283.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj24283.MT_pivotIn__.setValue('')
    self.obj24283.MT_pivotIn__.setNone()

    # MT_label__
    self.obj24283.MT_label__.setValue('10')

    # MT_pre__cardinality
    self.obj24283.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24283.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj24283.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24283.MT_pre__name.setHeight(15)

    self.obj24283.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(140.0,540.0,self.obj24283)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24283.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24283)
    self.globalAndLocalPostcondition(self.obj24283, rootNode)
    self.obj24283.postAction( rootNode.CREATE )

    self.obj15652=MT_pre__directLink_S(self)
    self.obj15652.isGraphObjectVisual = True

    if(hasattr(self.obj15652, '_setHierarchicalLink')):
      self.obj15652._setHierarchicalLink(False)

    # MT_label__
    self.obj15652.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj15652.MT_pivotOut__.setValue('')
    self.obj15652.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15652.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15652.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj15652.MT_pivotIn__.setValue('')
    self.obj15652.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj15652.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15652.MT_pre__associationType.setHeight(15)

    self.obj15652.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(330.0,444.0,self.obj15652)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj15652.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15652)
    self.globalAndLocalPostcondition(self.obj15652, rootNode)
    self.obj15652.postAction( rootNode.CREATE )

    self.obj17378=MT_pre__directLink_S(self)
    self.obj17378.isGraphObjectVisual = True

    if(hasattr(self.obj17378, '_setHierarchicalLink')):
      self.obj17378._setHierarchicalLink(False)

    # MT_label__
    self.obj17378.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj17378.MT_pivotOut__.setValue('')
    self.obj17378.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj17378.MT_subtypeMatching__.setValue(('True', 0))
    self.obj17378.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj17378.MT_pivotIn__.setValue('')
    self.obj17378.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj17378.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj17378.MT_pre__associationType.setHeight(15)

    self.obj17378.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(410.0,444.0,self.obj17378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj17378.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj17378)
    self.globalAndLocalPostcondition(self.obj17378, rootNode)
    self.obj17378.postAction( rootNode.CREATE )

    self.obj22556=MT_pre__directLink_S(self)
    self.obj22556.isGraphObjectVisual = True

    if(hasattr(self.obj22556, '_setHierarchicalLink')):
      self.obj22556._setHierarchicalLink(False)

    # MT_label__
    self.obj22556.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj22556.MT_pivotOut__.setValue('')
    self.obj22556.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj22556.MT_subtypeMatching__.setValue(('True', 0))
    self.obj22556.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj22556.MT_pivotIn__.setValue('')
    self.obj22556.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj22556.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22556.MT_pre__associationType.setHeight(15)

    self.obj22556.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,442.0,self.obj22556)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj22556.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22556)
    self.globalAndLocalPostcondition(self.obj22556, rootNode)
    self.obj22556.postAction( rootNode.CREATE )

    self.obj24282=MT_pre__directLink_S(self)
    self.obj24282.isGraphObjectVisual = True

    if(hasattr(self.obj24282, '_setHierarchicalLink')):
      self.obj24282._setHierarchicalLink(False)

    # MT_label__
    self.obj24282.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj24282.MT_pivotOut__.setValue('')
    self.obj24282.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24282.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24282.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj24282.MT_pivotIn__.setValue('')
    self.obj24282.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj24282.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24282.MT_pre__associationType.setHeight(15)

    self.obj24282.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,554.0,self.obj24282)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj24282.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24282)
    self.globalAndLocalPostcondition(self.obj24282, rootNode)
    self.obj24282.postAction( rootNode.CREATE )

    self.obj24284=MT_pre__trace_link(self)
    self.obj24284.isGraphObjectVisual = True

    if(hasattr(self.obj24284, '_setHierarchicalLink')):
      self.obj24284._setHierarchicalLink(False)

    # MT_label__
    self.obj24284.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj24284.MT_pivotOut__.setValue('')
    self.obj24284.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24284.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24284.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj24284.MT_pivotIn__.setValue('')
    self.obj24284.MT_pivotIn__.setNone()

    self.obj24284.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(321.5,503.5,self.obj24284)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj24284.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24284)
    self.globalAndLocalPostcondition(self.obj24284, rootNode)
    self.obj24284.postAction( rootNode.CREATE )

    self.obj1538=LHS(self)
    self.obj1538.isGraphObjectVisual = True

    if(hasattr(self.obj1538, '_setHierarchicalLink')):
      self.obj1538._setHierarchicalLink(False)

    # constraint
    self.obj1538.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj1538.constraint.setHeight(15)

    self.obj1538.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,300.0,self.obj1538)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1538.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1538)
    self.globalAndLocalPostcondition(self.obj1538, rootNode)
    self.obj1538.postAction( rootNode.CREATE )

    # Connections for obj1539 (graphObject_: Obj5) of type MT_pre__ECU
    self.drawConnections(
(self.obj1539,self.obj15652,[330.0, 394.0, 330.0, 444.0],"true", 2) )
    # Connections for obj15651 (graphObject_: Obj26) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj15651,self.obj17378,[330.0, 494.0, 410.0, 444.0],"true", 2) )
    # Connections for obj17377 (graphObject_: Obj28) of type MT_pre__Distributable
    self.drawConnections(
(self.obj17377,self.obj22556,[490.0, 394.0, 490.0, 442.0],"true", 2) )
    # Connections for obj22555 (graphObject_: Obj32) of type MT_pre__ExecFrame
    self.drawConnections(
(self.obj22555,self.obj24282,[490.0, 494.0, 490.0, 554.0],"true", 2) )
    # Connections for obj24281 (graphObject_: Obj34) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj24283 (graphObject_: Obj36) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj24283,self.obj24284,[313.0, 613.0, 321.5, 503.5],"true", 2) )
    # Connections for obj15652 (graphObject_: Obj27) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj15652,self.obj15651,[330.0, 444.0, 330.0, 494.0],"true", 2) )
    # Connections for obj17378 (graphObject_: Obj29) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj17378,self.obj17377,[410.0, 444.0, 490.0, 394.0],"true", 2) )
    # Connections for obj22556 (graphObject_: Obj33) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj22556,self.obj22555,[490.0, 442.0, 490.0, 494.0],"true", 2) )
    # Connections for obj24282 (graphObject_: Obj35) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj24282,self.obj24281,[490.0, 554.0, 490.0, 614.0],"true", 2) )
    # Connections for obj24284 (graphObject_: Obj37) of type MT_pre__trace_link
    self.drawConnections(
(self.obj24284,self.obj1539,[321.5, 503.5, 330.0, 394.0],"true", 2) )
    # Connections for obj1538 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )

newfunction = ConnRPortPrototype_Back_Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
