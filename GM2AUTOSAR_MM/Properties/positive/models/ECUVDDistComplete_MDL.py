"""
__ECUVDDistComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu May 23 13:30:50 2013
_______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__CompositionType import *
from MT_pre__ComponentPrototype import *
from MT_pre__directLink_S import *
from MT_pre__directLink_T import *
from MT_pre__backward_link import *
from LHS import *
from graph_MT_pre__ECU import *
from graph_LHS import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__ComponentPrototype import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__backward_link import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__VirtualDevice import *
from graph_MT_pre__directLink_T import *
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

def ECUVDDistComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ECUVDDistComplete')
    # --- ASG attributes over ---


    self.obj2919=MT_pre__ECU(self)
    self.obj2919.isGraphObjectVisual = True

    if(hasattr(self.obj2919, '_setHierarchicalLink')):
      self.obj2919._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj2919.MT_pivotOut__.setValue('')
    self.obj2919.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2919.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2919.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj2919.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2919.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj2919.MT_pivotIn__.setValue('')
    self.obj2919.MT_pivotIn__.setNone()

    # MT_label__
    self.obj2919.MT_label__.setValue('1')

    # MT_pre__name
    self.obj2919.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2919.MT_pre__name.setHeight(15)

    self.obj2919.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(56.0,176.0,self.obj2919)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2919.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2919)
    self.globalAndLocalPostcondition(self.obj2919, rootNode)
    self.obj2919.postAction( rootNode.CREATE )

    self.obj2920=MT_pre__VirtualDevice(self)
    self.obj2920.isGraphObjectVisual = True

    if(hasattr(self.obj2920, '_setHierarchicalLink')):
      self.obj2920._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj2920.MT_pivotOut__.setValue('')
    self.obj2920.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2920.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2920.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj2920.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2920.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj2920.MT_pivotIn__.setValue('')
    self.obj2920.MT_pivotIn__.setNone()

    # MT_label__
    self.obj2920.MT_label__.setValue('2')

    # MT_pre__name
    self.obj2920.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2920.MT_pre__name.setHeight(15)

    self.obj2920.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(160.0,55.0,self.obj2920)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2920.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2920)
    self.globalAndLocalPostcondition(self.obj2920, rootNode)
    self.obj2920.postAction( rootNode.CREATE )

    self.obj2921=MT_pre__Distributable(self)
    self.obj2921.isGraphObjectVisual = True

    if(hasattr(self.obj2921, '_setHierarchicalLink')):
      self.obj2921._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj2921.MT_pivotOut__.setValue('')
    self.obj2921.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2921.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2921.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj2921.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2921.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj2921.MT_pivotIn__.setValue('')
    self.obj2921.MT_pivotIn__.setNone()

    # MT_label__
    self.obj2921.MT_label__.setValue('3')

    # MT_pre__name
    self.obj2921.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2921.MT_pre__name.setHeight(15)

    self.obj2921.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(296.0,179.0,self.obj2921)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2921.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2921)
    self.globalAndLocalPostcondition(self.obj2921, rootNode)
    self.obj2921.postAction( rootNode.CREATE )

    self.obj2922=MT_pre__CompositionType(self)
    self.obj2922.isGraphObjectVisual = True

    if(hasattr(self.obj2922, '_setHierarchicalLink')):
      self.obj2922._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj2922.MT_pivotOut__.setValue('')
    self.obj2922.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2922.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2922.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj2922.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2922.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj2922.MT_pivotIn__.setValue('')
    self.obj2922.MT_pivotIn__.setNone()

    # MT_label__
    self.obj2922.MT_label__.setValue('4')

    # MT_pre__name
    self.obj2922.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2922.MT_pre__name.setHeight(15)

    self.obj2922.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(60.0,320.0,self.obj2922)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2922.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2922)
    self.globalAndLocalPostcondition(self.obj2922, rootNode)
    self.obj2922.postAction( rootNode.CREATE )

    self.obj2923=MT_pre__ComponentPrototype(self)
    self.obj2923.isGraphObjectVisual = True

    if(hasattr(self.obj2923, '_setHierarchicalLink')):
      self.obj2923._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj2923.MT_pivotOut__.setValue('')
    self.obj2923.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2923.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2923.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj2923.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2923.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj2923.MT_pivotIn__.setValue('')
    self.obj2923.MT_pivotIn__.setNone()

    # MT_label__
    self.obj2923.MT_label__.setValue('5')

    # MT_pre__name
    self.obj2923.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2923.MT_pre__name.setHeight(15)

    self.obj2923.graphClass_= graph_MT_pre__ComponentPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__ComponentPrototype(200.0,320.0,self.obj2923)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2923.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2923)
    self.globalAndLocalPostcondition(self.obj2923, rootNode)
    self.obj2923.postAction( rootNode.CREATE )

    self.obj2924=MT_pre__directLink_S(self)
    self.obj2924.isGraphObjectVisual = True

    if(hasattr(self.obj2924, '_setHierarchicalLink')):
      self.obj2924._setHierarchicalLink(False)

    # MT_label__
    self.obj2924.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj2924.MT_pivotOut__.setValue('')
    self.obj2924.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2924.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2924.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2924.MT_pivotIn__.setValue('')
    self.obj2924.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2924.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2924.MT_pre__associationType.setHeight(15)

    self.obj2924.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(278.0,189.5,self.obj2924)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2924.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2924)
    self.globalAndLocalPostcondition(self.obj2924, rootNode)
    self.obj2924.postAction( rootNode.CREATE )

    self.obj2925=MT_pre__directLink_S(self)
    self.obj2925.isGraphObjectVisual = True

    if(hasattr(self.obj2925, '_setHierarchicalLink')):
      self.obj2925._setHierarchicalLink(False)

    # MT_label__
    self.obj2925.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj2925.MT_pivotOut__.setValue('')
    self.obj2925.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2925.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2925.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2925.MT_pivotIn__.setValue('')
    self.obj2925.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2925.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2925.MT_pre__associationType.setHeight(15)

    self.obj2925.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(398.0,191.0,self.obj2925)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2925.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2925)
    self.globalAndLocalPostcondition(self.obj2925, rootNode)
    self.obj2925.postAction( rootNode.CREATE )

    self.obj2926=MT_pre__directLink_T(self)
    self.obj2926.isGraphObjectVisual = True

    if(hasattr(self.obj2926, '_setHierarchicalLink')):
      self.obj2926._setHierarchicalLink(False)

    # MT_label__
    self.obj2926.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj2926.MT_pivotOut__.setValue('')
    self.obj2926.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2926.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2926.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2926.MT_pivotIn__.setValue('')
    self.obj2926.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2926.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj2926.MT_pre__associationType.setHeight(15)

    self.obj2926.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(304.0,393.0,self.obj2926)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2926.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2926)
    self.globalAndLocalPostcondition(self.obj2926, rootNode)
    self.obj2926.postAction( rootNode.CREATE )

    self.obj2927=MT_pre__backward_link(self)
    self.obj2927.isGraphObjectVisual = True

    if(hasattr(self.obj2927, '_setHierarchicalLink')):
      self.obj2927._setHierarchicalLink(False)

    # MT_label__
    self.obj2927.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj2927.MT_pivotOut__.setValue('')
    self.obj2927.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2927.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2927.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2927.MT_pivotIn__.setValue('')
    self.obj2927.MT_pivotIn__.setNone()

    self.obj2927.graphClass_= graph_MT_pre__backward_link
    if self.genGraphics:
       new_obj = graph_MT_pre__backward_link(227.0,321.5,self.obj2927)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2927.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2927)
    self.globalAndLocalPostcondition(self.obj2927, rootNode)
    self.obj2927.postAction( rootNode.CREATE )

    self.obj2928=MT_pre__backward_link(self)
    self.obj2928.isGraphObjectVisual = True

    if(hasattr(self.obj2928, '_setHierarchicalLink')):
      self.obj2928._setHierarchicalLink(False)

    # MT_label__
    self.obj2928.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj2928.MT_pivotOut__.setValue('')
    self.obj2928.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2928.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2928.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2928.MT_pivotIn__.setValue('')
    self.obj2928.MT_pivotIn__.setNone()

    self.obj2928.graphClass_= graph_MT_pre__backward_link
    if self.genGraphics:
       new_obj = graph_MT_pre__backward_link(423.0,323.0,self.obj2928)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2928.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2928)
    self.globalAndLocalPostcondition(self.obj2928, rootNode)
    self.obj2928.postAction( rootNode.CREATE )

    self.obj2918=LHS(self)
    self.obj2918.isGraphObjectVisual = True

    if(hasattr(self.obj2918, '_setHierarchicalLink')):
      self.obj2918._setHierarchicalLink(False)

    # constraint
    self.obj2918.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj2918.constraint.setHeight(15)

    self.obj2918.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,40.0,self.obj2918)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj2918.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2918)
    self.globalAndLocalPostcondition(self.obj2918, rootNode)
    self.obj2918.postAction( rootNode.CREATE )

    # Connections for obj2919 (graphObject_: Obj11) of type MT_pre__ECU
    self.drawConnections(
(self.obj2919,self.obj2924,[226.0, 250.0, 278.0, 189.5],"true", 2) )
    # Connections for obj2920 (graphObject_: Obj12) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj2920,self.obj2925,[330.0, 129.0, 398.0, 191.0],"true", 2) )
    # Connections for obj2921 (graphObject_: Obj13) of type MT_pre__Distributable
    self.drawConnections(
 )
    # Connections for obj2922 (graphObject_: Obj14) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj2922,self.obj2926,[228.0, 393.0, 304.0, 393.0],"true", 2),
(self.obj2922,self.obj2927,[228.0, 393.0, 227.0, 321.5],"true", 2) )
    # Connections for obj2923 (graphObject_: Obj15) of type MT_pre__ComponentPrototype
    self.drawConnections(
(self.obj2923,self.obj2928,[380.0, 393.0, 423.0, 323.0],"true", 2) )
    # Connections for obj2924 (graphObject_: Obj16) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj2924,self.obj2920,[278.0, 189.5, 330.0, 129.0],"true", 2) )
    # Connections for obj2925 (graphObject_: Obj17) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj2925,self.obj2921,[398.0, 191.0, 466.0, 253.0],"true", 2) )
    # Connections for obj2926 (graphObject_: Obj18) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj2926,self.obj2923,[304.0, 393.0, 380.0, 393.0],"true", 2) )
    # Connections for obj2927 (graphObject_: Obj19) of type MT_pre__backward_link
    self.drawConnections(
(self.obj2927,self.obj2919,[227.0, 321.5, 226.0, 250.0],"true", 2) )
    # Connections for obj2928 (graphObject_: Obj20) of type MT_pre__backward_link
    self.drawConnections(
(self.obj2928,self.obj2921,[423.0, 323.0, 466.0, 253.0],"true", 2) )
    # Connections for obj2918 (graphObject_: Obj10) of type LHS
    self.drawConnections(
 )

newfunction = ECUVDDistComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
