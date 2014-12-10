"""
__ConnVirtualDevice2Distributable_Back_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Nov  1 18:24:14 2013
___________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__CompositionType import *
from MT_pre__ComponentPrototype import *
from MT_pre__SwcToEcuMapping import *
from MT_pre__SwCompToEcuMapping_component import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__SwcToEcuMapping import *
from graph_MT_pre__ECU import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__ComponentPrototype import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__VirtualDevice import *
from graph_MT_pre__SwCompToEcuMapping_component import *
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

def ConnVirtualDevice2Distributable_Back_Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ConnVirtualDevice2Distributable_Back_Complete')
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

    self.obj3024=MT_pre__VirtualDevice(self)
    self.obj3024.isGraphObjectVisual = True

    if(hasattr(self.obj3024, '_setHierarchicalLink')):
      self.obj3024._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3024.MT_pivotOut__.setValue('')
    self.obj3024.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3024.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3024.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3024.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3024.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3024.MT_pivotIn__.setValue('')
    self.obj3024.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3024.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj3024.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3024.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3024.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3024.MT_pre__name.setHeight(15)

    self.obj3024.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(260.0,400.0,self.obj3024)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3024.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3024)
    self.globalAndLocalPostcondition(self.obj3024, rootNode)
    self.obj3024.postAction( rootNode.CREATE )

    self.obj3025=MT_pre__Distributable(self)
    self.obj3025.isGraphObjectVisual = True

    if(hasattr(self.obj3025, '_setHierarchicalLink')):
      self.obj3025._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3025.MT_pivotOut__.setValue('')
    self.obj3025.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3025.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3025.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3025.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3025.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3025.MT_pivotIn__.setValue('')
    self.obj3025.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3025.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj3025.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3025.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3025.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3025.MT_pre__name.setHeight(15)

    self.obj3025.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(380.0,320.0,self.obj3025)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3025.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3025)
    self.globalAndLocalPostcondition(self.obj3025, rootNode)
    self.obj3025.postAction( rootNode.CREATE )

    self.obj5996=MT_pre__CompositionType(self)
    self.obj5996.isGraphObjectVisual = True

    if(hasattr(self.obj5996, '_setHierarchicalLink')):
      self.obj5996._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj5996.MT_pivotOut__.setValue('')
    self.obj5996.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj5996.MT_subtypeMatching__.setValue(('True', 0))
    self.obj5996.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj5996.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj5996.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj5996.MT_pivotIn__.setValue('')
    self.obj5996.MT_pivotIn__.setNone()

    # MT_label__
    self.obj5996.MT_label__.setValue('6')

    # MT_pre__cardinality
    self.obj5996.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj5996.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj5996.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj5996.MT_pre__name.setHeight(15)

    self.obj5996.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(160.0,500.0,self.obj5996)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj5996.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5996)
    self.globalAndLocalPostcondition(self.obj5996, rootNode)
    self.obj5996.postAction( rootNode.CREATE )

    self.obj7482=MT_pre__ComponentPrototype(self)
    self.obj7482.isGraphObjectVisual = True

    if(hasattr(self.obj7482, '_setHierarchicalLink')):
      self.obj7482._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj7482.MT_pivotOut__.setValue('')
    self.obj7482.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj7482.MT_subtypeMatching__.setValue(('True', 0))
    self.obj7482.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj7482.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj7482.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj7482.MT_pivotIn__.setValue('')
    self.obj7482.MT_pivotIn__.setNone()

    # MT_label__
    self.obj7482.MT_label__.setValue('8')

    # MT_pre__cardinality
    self.obj7482.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj7482.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj7482.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj7482.MT_pre__name.setHeight(15)

    self.obj7482.graphClass_= graph_MT_pre__ComponentPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__ComponentPrototype(240.0,560.0,self.obj7482)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj7482.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj7482)
    self.globalAndLocalPostcondition(self.obj7482, rootNode)
    self.obj7482.postAction( rootNode.CREATE )

    self.obj8968=MT_pre__SwcToEcuMapping(self)
    self.obj8968.isGraphObjectVisual = True

    if(hasattr(self.obj8968, '_setHierarchicalLink')):
      self.obj8968._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj8968.MT_pivotOut__.setValue('')
    self.obj8968.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8968.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8968.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj8968.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8968.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj8968.MT_pivotIn__.setValue('')
    self.obj8968.MT_pivotIn__.setNone()

    # MT_label__
    self.obj8968.MT_label__.setValue('10')

    # MT_pre__cardinality
    self.obj8968.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8968.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj8968.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8968.MT_pre__name.setHeight(15)

    self.obj8968.graphClass_= graph_MT_pre__SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SwcToEcuMapping(320.0,500.0,self.obj8968)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj8968.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8968)
    self.globalAndLocalPostcondition(self.obj8968, rootNode)
    self.obj8968.postAction( rootNode.CREATE )

    self.obj10454=MT_pre__SwCompToEcuMapping_component(self)
    self.obj10454.isGraphObjectVisual = True

    if(hasattr(self.obj10454, '_setHierarchicalLink')):
      self.obj10454._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10454.MT_pivotOut__.setValue('')
    self.obj10454.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10454.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10454.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10454.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10454.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10454.MT_pivotIn__.setValue('')
    self.obj10454.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10454.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj10454.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10454.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10454.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10454.MT_pre__name.setHeight(15)

    self.obj10454.graphClass_= graph_MT_pre__SwCompToEcuMapping_component
    if self.genGraphics:
       new_obj = graph_MT_pre__SwCompToEcuMapping_component(360.0,560.0,self.obj10454)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwCompToEcuMapping_component", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10454.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10454)
    self.globalAndLocalPostcondition(self.obj10454, rootNode)
    self.obj10454.postAction( rootNode.CREATE )

    self.obj3026=MT_pre__directLink_S(self)
    self.obj3026.isGraphObjectVisual = True

    if(hasattr(self.obj3026, '_setHierarchicalLink')):
      self.obj3026._setHierarchicalLink(False)

    # MT_label__
    self.obj3026.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj3026.MT_pivotOut__.setValue('')
    self.obj3026.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3026.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3026.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3026.MT_pivotIn__.setValue('')
    self.obj3026.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3026.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3026.MT_pre__associationType.setHeight(15)

    self.obj3026.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(370.0,454.0,self.obj3026)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3026.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3026)
    self.globalAndLocalPostcondition(self.obj3026, rootNode)
    self.obj3026.postAction( rootNode.CREATE )

    self.obj3027=MT_pre__directLink_S(self)
    self.obj3027.isGraphObjectVisual = True

    if(hasattr(self.obj3027, '_setHierarchicalLink')):
      self.obj3027._setHierarchicalLink(False)

    # MT_label__
    self.obj3027.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj3027.MT_pivotOut__.setValue('')
    self.obj3027.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3027.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3027.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3027.MT_pivotIn__.setValue('')
    self.obj3027.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3027.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3027.MT_pre__associationType.setHeight(15)

    self.obj3027.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(480.0,454.0,self.obj3027)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3027.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3027)
    self.globalAndLocalPostcondition(self.obj3027, rootNode)
    self.obj3027.postAction( rootNode.CREATE )

    self.obj5997=MT_pre__trace_link(self)
    self.obj5997.isGraphObjectVisual = True

    if(hasattr(self.obj5997, '_setHierarchicalLink')):
      self.obj5997._setHierarchicalLink(False)

    # MT_label__
    self.obj5997.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj5997.MT_pivotOut__.setValue('')
    self.obj5997.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj5997.MT_subtypeMatching__.setValue(('True', 0))
    self.obj5997.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj5997.MT_pivotIn__.setValue('')
    self.obj5997.MT_pivotIn__.setNone()

    self.obj5997.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(329.0,483.5,self.obj5997)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj5997.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5997)
    self.globalAndLocalPostcondition(self.obj5997, rootNode)
    self.obj5997.postAction( rootNode.CREATE )

    self.obj7483=MT_pre__trace_link(self)
    self.obj7483.isGraphObjectVisual = True

    if(hasattr(self.obj7483, '_setHierarchicalLink')):
      self.obj7483._setHierarchicalLink(False)

    # MT_label__
    self.obj7483.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj7483.MT_pivotOut__.setValue('')
    self.obj7483.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj7483.MT_subtypeMatching__.setValue(('True', 0))
    self.obj7483.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj7483.MT_pivotIn__.setValue('')
    self.obj7483.MT_pivotIn__.setNone()

    self.obj7483.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(485.0,513.5,self.obj7483)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj7483.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj7483)
    self.globalAndLocalPostcondition(self.obj7483, rootNode)
    self.obj7483.postAction( rootNode.CREATE )

    self.obj8969=MT_pre__trace_link(self)
    self.obj8969.isGraphObjectVisual = True

    if(hasattr(self.obj8969, '_setHierarchicalLink')):
      self.obj8969._setHierarchicalLink(False)

    # MT_label__
    self.obj8969.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj8969.MT_pivotOut__.setValue('')
    self.obj8969.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8969.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8969.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj8969.MT_pivotIn__.setValue('')
    self.obj8969.MT_pivotIn__.setNone()

    self.obj8969.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(462.0,523.5,self.obj8969)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj8969.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8969)
    self.globalAndLocalPostcondition(self.obj8969, rootNode)
    self.obj8969.postAction( rootNode.CREATE )

    self.obj10460=MT_pre__trace_link(self)
    self.obj10460.isGraphObjectVisual = True

    if(hasattr(self.obj10460, '_setHierarchicalLink')):
      self.obj10460._setHierarchicalLink(False)

    # MT_label__
    self.obj10460.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj10460.MT_pivotOut__.setValue('')
    self.obj10460.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10460.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10460.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10460.MT_pivotIn__.setValue('')
    self.obj10460.MT_pivotIn__.setNone()

    self.obj10460.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(541.5,513.5,self.obj10460)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10460.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10460)
    self.globalAndLocalPostcondition(self.obj10460, rootNode)
    self.obj10460.postAction( rootNode.CREATE )

    self.obj1538=LHS(self)
    self.obj1538.isGraphObjectVisual = True

    if(hasattr(self.obj1538, '_setHierarchicalLink')):
      self.obj1538._setHierarchicalLink(False)

    # constraint
    self.obj1538.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj1538.constraint.setHeight(15)

    self.obj1538.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(140.0,300.0,self.obj1538)
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
(self.obj1539,self.obj3026,[330.0, 394.0, 370.0, 454.0],"true", 2) )
    # Connections for obj3024 (graphObject_: Obj6) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj3024,self.obj3027,[430.0, 474.0, 480.0, 454.0],"true", 2) )
    # Connections for obj3025 (graphObject_: Obj7) of type MT_pre__Distributable
    self.drawConnections(
 )
    # Connections for obj5996 (graphObject_: Obj10) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj5996,self.obj5997,[328.0, 573.0, 329.0, 483.5],"true", 2) )
    # Connections for obj7482 (graphObject_: Obj12) of type MT_pre__ComponentPrototype
    self.drawConnections(
(self.obj7482,self.obj7483,[420.0, 633.0, 485.0, 513.5],"true", 2) )
    # Connections for obj8968 (graphObject_: Obj14) of type MT_pre__SwcToEcuMapping
    self.drawConnections(
(self.obj8968,self.obj8969,[494.0, 573.0, 462.0, 523.5],"true", 2) )
    # Connections for obj10454 (graphObject_: Obj16) of type MT_pre__SwCompToEcuMapping_component
    self.drawConnections(
(self.obj10454,self.obj10460,[533.0, 633.0, 541.5, 513.5],"true", 2) )
    # Connections for obj3026 (graphObject_: Obj8) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj3026,self.obj3024,[370.0, 454.0, 430.0, 474.0],"true", 2) )
    # Connections for obj3027 (graphObject_: Obj9) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj3027,self.obj3025,[480.0, 454.0, 550.0, 394.0],"true", 2) )
    # Connections for obj5997 (graphObject_: Obj11) of type MT_pre__trace_link
    self.drawConnections(
(self.obj5997,self.obj1539,[329.0, 483.5, 330.0, 394.0],"true", 2) )
    # Connections for obj7483 (graphObject_: Obj13) of type MT_pre__trace_link
    self.drawConnections(
(self.obj7483,self.obj3025,[485.0, 513.5, 550.0, 394.0],"true", 2) )
    # Connections for obj8969 (graphObject_: Obj15) of type MT_pre__trace_link
    self.drawConnections(
(self.obj8969,self.obj3024,[462.0, 523.5, 430.0, 474.0],"true", 2) )
    # Connections for obj10460 (graphObject_: Obj18) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10460,self.obj3025,[541.5, 513.5, 550.0, 394.0],"true", 2) )
    # Connections for obj1538 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )

newfunction = ConnVirtualDevice2Distributable_Back_Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
