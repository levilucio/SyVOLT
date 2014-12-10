"""
__ConnECU2VirtualDevice_Back_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Nov  1 17:59:15 2013
_________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__VirtualDevice import *
from MT_pre__EcuInstance import *
from MT_pre__trace_link import *
from MT_pre__SystemMapping import *
from MT_pre__directLink_S import *
from MT_pre__ECU import *
from MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SystemMapping import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__VirtualDevice import *
from graph_MT_pre__ECU import *
from graph_MT_pre__EcuInstance import *
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

def ConnECU2VirtualDevice_Back_Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ConnECU2VirtualDevice_Back_Complete')
    # --- ASG attributes over ---


    self.obj99=LHS(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # constraint
    self.obj99.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj99.constraint.setHeight(15)

    self.obj99.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(149.0,299.0,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj30813=MT_pre__VirtualDevice(self)
    self.obj30813.isGraphObjectVisual = True

    if(hasattr(self.obj30813, '_setHierarchicalLink')):
      self.obj30813._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj30813.MT_pivotOut__.setValue('')
    self.obj30813.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30813.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30813.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj30813.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30813.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj30813.MT_pivotIn__.setValue('')
    self.obj30813.MT_pivotIn__.setNone()

    # MT_label__
    self.obj30813.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj30813.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30813.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj30813.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30813.MT_pre__name.setHeight(15)

    self.obj30813.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(380.0,300.0,self.obj30813)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30813.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30813)
    self.globalAndLocalPostcondition(self.obj30813, rootNode)
    self.obj30813.postAction( rootNode.CREATE )

    self.obj30816=MT_pre__EcuInstance(self)
    self.obj30816.isGraphObjectVisual = True

    if(hasattr(self.obj30816, '_setHierarchicalLink')):
      self.obj30816._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj30816.MT_pivotOut__.setValue('')
    self.obj30816.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30816.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30816.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj30816.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30816.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj30816.MT_pivotIn__.setValue('')
    self.obj30816.MT_pivotIn__.setNone()

    # MT_label__
    self.obj30816.MT_label__.setValue('7')

    # MT_pre__cardinality
    self.obj30816.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30816.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj30816.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30816.MT_pre__name.setHeight(15)

    self.obj30816.graphClass_= graph_MT_pre__EcuInstance
    if self.genGraphics:
       new_obj = graph_MT_pre__EcuInstance(380.0,540.0,self.obj30816)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EcuInstance", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30816.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30816)
    self.globalAndLocalPostcondition(self.obj30816, rootNode)
    self.obj30816.postAction( rootNode.CREATE )

    self.obj30818=MT_pre__trace_link(self)
    self.obj30818.isGraphObjectVisual = True

    if(hasattr(self.obj30818, '_setHierarchicalLink')):
      self.obj30818._setHierarchicalLink(False)

    # MT_label__
    self.obj30818.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj30818.MT_pivotOut__.setValue('')
    self.obj30818.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30818.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30818.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj30818.MT_pivotIn__.setValue('')
    self.obj30818.MT_pivotIn__.setNone()

    self.obj30818.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(335.0,493.0,self.obj30818)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj30818.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30818)
    self.globalAndLocalPostcondition(self.obj30818, rootNode)
    self.obj30818.postAction( rootNode.CREATE )

    self.obj30819=MT_pre__trace_link(self)
    self.obj30819.isGraphObjectVisual = True

    if(hasattr(self.obj30819, '_setHierarchicalLink')):
      self.obj30819._setHierarchicalLink(False)

    # MT_label__
    self.obj30819.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj30819.MT_pivotOut__.setValue('')
    self.obj30819.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30819.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30819.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj30819.MT_pivotIn__.setValue('')
    self.obj30819.MT_pivotIn__.setNone()

    self.obj30819.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(443.5,493.0,self.obj30819)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj30819.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30819)
    self.globalAndLocalPostcondition(self.obj30819, rootNode)
    self.obj30819.postAction( rootNode.CREATE )

    self.obj30820=MT_pre__trace_link(self)
    self.obj30820.isGraphObjectVisual = True

    if(hasattr(self.obj30820, '_setHierarchicalLink')):
      self.obj30820._setHierarchicalLink(False)

    # MT_label__
    self.obj30820.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj30820.MT_pivotOut__.setValue('')
    self.obj30820.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30820.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30820.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj30820.MT_pivotIn__.setValue('')
    self.obj30820.MT_pivotIn__.setNone()

    self.obj30820.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(502.0,433.5,self.obj30820)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj30820.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30820)
    self.globalAndLocalPostcondition(self.obj30820, rootNode)
    self.obj30820.postAction( rootNode.CREATE )

    self.obj30815=MT_pre__SystemMapping(self)
    self.obj30815.isGraphObjectVisual = True

    if(hasattr(self.obj30815, '_setHierarchicalLink')):
      self.obj30815._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj30815.MT_pivotOut__.setValue('')
    self.obj30815.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30815.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30815.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj30815.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30815.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj30815.MT_pivotIn__.setValue('')
    self.obj30815.MT_pivotIn__.setNone()

    # MT_label__
    self.obj30815.MT_label__.setValue('6')

    # MT_pre__cardinality
    self.obj30815.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30815.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj30815.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30815.MT_pre__name.setHeight(15)

    self.obj30815.graphClass_= graph_MT_pre__SystemMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SystemMapping(160.0,540.0,self.obj30815)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SystemMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30815.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30815)
    self.globalAndLocalPostcondition(self.obj30815, rootNode)
    self.obj30815.postAction( rootNode.CREATE )

    self.obj30814=MT_pre__directLink_S(self)
    self.obj30814.isGraphObjectVisual = True

    if(hasattr(self.obj30814, '_setHierarchicalLink')):
      self.obj30814._setHierarchicalLink(False)

    # MT_label__
    self.obj30814.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj30814.MT_pivotOut__.setValue('')
    self.obj30814.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30814.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30814.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj30814.MT_pivotIn__.setValue('')
    self.obj30814.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj30814.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30814.MT_pre__associationType.setHeight(15)

    self.obj30814.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(444.5,373.5,self.obj30814)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj30814.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30814)
    self.globalAndLocalPostcondition(self.obj30814, rootNode)
    self.obj30814.postAction( rootNode.CREATE )

    self.obj107=MT_pre__ECU(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj107.MT_pivotOut__.setValue('')
    self.obj107.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj107.MT_subtypeMatching__.setValue(('True', 0))
    self.obj107.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj107.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj107.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj107.MT_pivotIn__.setValue('')
    self.obj107.MT_pivotIn__.setNone()

    # MT_label__
    self.obj107.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj107.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj107.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj107.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj107.MT_pre__name.setHeight(15)

    self.obj107.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(169.0,299.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj30817=MT_pre__SwcToEcuMapping(self)
    self.obj30817.isGraphObjectVisual = True

    if(hasattr(self.obj30817, '_setHierarchicalLink')):
      self.obj30817._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj30817.MT_pivotOut__.setValue('')
    self.obj30817.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj30817.MT_subtypeMatching__.setValue(('True', 0))
    self.obj30817.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj30817.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30817.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj30817.MT_pivotIn__.setValue('')
    self.obj30817.MT_pivotIn__.setNone()

    # MT_label__
    self.obj30817.MT_label__.setValue('8')

    # MT_pre__cardinality
    self.obj30817.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30817.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj30817.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj30817.MT_pre__name.setHeight(15)

    self.obj30817.graphClass_= graph_MT_pre__SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SwcToEcuMapping(280.0,420.0,self.obj30817)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30817.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30817)
    self.globalAndLocalPostcondition(self.obj30817, rootNode)
    self.obj30817.postAction( rootNode.CREATE )

    # Connections for obj99 (graphObject_: Obj20) of type LHS
    self.drawConnections(
 )
    # Connections for obj30813 (graphObject_: Obj34) of type MT_pre__VirtualDevice
    self.drawConnections(
 )
    # Connections for obj30816 (graphObject_: Obj37) of type MT_pre__EcuInstance
    self.drawConnections(
(self.obj30816,self.obj30819,[548.0, 613.0, 443.5, 493.0],"true", 2) )
    # Connections for obj30818 (graphObject_: Obj39) of type MT_pre__trace_link
    self.drawConnections(
(self.obj30818,self.obj107,[335.0, 493.0, 339.0, 373.0],"true", 2) )
    # Connections for obj30819 (graphObject_: Obj40) of type MT_pre__trace_link
    self.drawConnections(
(self.obj30819,self.obj107,[443.5, 493.0, 339.0, 373.0],"true", 2) )
    # Connections for obj30820 (graphObject_: Obj41) of type MT_pre__trace_link
    self.drawConnections(
(self.obj30820,self.obj30813,[502.0, 433.5, 550.0, 374.0],"true", 2) )
    # Connections for obj30815 (graphObject_: Obj36) of type MT_pre__SystemMapping
    self.drawConnections(
(self.obj30815,self.obj30818,[331.0, 613.0, 335.0, 493.0],"true", 2) )
    # Connections for obj30814 (graphObject_: Obj35) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj30814,self.obj30813,[444.5, 373.5, 550.0, 374.0],"true", 2) )
    # Connections for obj107 (graphObject_: Obj24) of type MT_pre__ECU
    self.drawConnections(
(self.obj107,self.obj30814,[339.0, 373.0, 444.5, 373.5],"true", 0) )
    # Connections for obj30817 (graphObject_: Obj38) of type MT_pre__SwcToEcuMapping
    self.drawConnections(
(self.obj30817,self.obj30820,[454.0, 493.0, 502.0, 433.5],"true", 2) )

newfunction = ConnECU2VirtualDevice_Back_Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
