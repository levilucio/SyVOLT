"""
__state2trans2exitptTrue_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 19:40:24 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__Transition import *
from MT_pre__State import *
from MT_pre__ProcDef import *
from MT_pre__Trigger_T import *
from MT_pre__Par import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__Trigger_T import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Transition import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Par import *
from graph_MT_pre__ProcDef import *
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

def state2trans2exitptTrue_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('state2trans2exitptTrue_Complete')
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


    self.obj10670=MT_pre__ExitPoint(self)
    self.obj10670.isGraphObjectVisual = True

    if(hasattr(self.obj10670, '_setHierarchicalLink')):
      self.obj10670._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10670.MT_pivotOut__.setValue('')
    self.obj10670.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10670.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10670.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10670.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10670.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10670.MT_pivotIn__.setValue('')
    self.obj10670.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10670.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj10670.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10670.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10670.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10670.MT_pre__name.setHeight(15)

    self.obj10670.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(260.0,100.0,self.obj10670)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10670.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10670)
    self.globalAndLocalPostcondition(self.obj10670, rootNode)
    self.obj10670.postAction( rootNode.CREATE )

    self.obj10669=MT_pre__Transition(self)
    self.obj10669.isGraphObjectVisual = True

    if(hasattr(self.obj10669, '_setHierarchicalLink')):
      self.obj10669._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10669.MT_pivotOut__.setValue('')
    self.obj10669.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10669.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10669.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10669.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10669.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10669.MT_pivotIn__.setValue('')
    self.obj10669.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10669.MT_label__.setValue('13')

    # MT_pre__cardinality
    self.obj10669.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10669.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10669.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10669.MT_pre__name.setHeight(15)

    self.obj10669.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(73.0,120.0,self.obj10669)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10669.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10669)
    self.globalAndLocalPostcondition(self.obj10669, rootNode)
    self.obj10669.postAction( rootNode.CREATE )

    self.obj10657=MT_pre__State(self)
    self.obj10657.isGraphObjectVisual = True

    if(hasattr(self.obj10657, '_setHierarchicalLink')):
      self.obj10657._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10657.MT_pivotOut__.setValue('')
    self.obj10657.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10657.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10657.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10657.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10657.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10657.MT_pivotIn__.setValue('')
    self.obj10657.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10657.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj10657.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10657.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10657.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10657.MT_pre__name.setHeight(15)

    self.obj10657.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(160.0,74.0,self.obj10657)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10657.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10657)
    self.globalAndLocalPostcondition(self.obj10657, rootNode)
    self.obj10657.postAction( rootNode.CREATE )

    self.obj10671=MT_pre__ProcDef(self)
    self.obj10671.isGraphObjectVisual = True

    if(hasattr(self.obj10671, '_setHierarchicalLink')):
      self.obj10671._setHierarchicalLink(False)

    # MT_label__
    self.obj10671.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj10671.MT_pivotOut__.setValue('')
    self.obj10671.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10671.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10671.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10671.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10671.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10671.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10671.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10671.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10671.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10671.MT_pivotIn__.setValue('')
    self.obj10671.MT_pivotIn__.setNone()

    self.obj10671.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(80.0,240.0,self.obj10671)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10671.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10671)
    self.globalAndLocalPostcondition(self.obj10671, rootNode)
    self.obj10671.postAction( rootNode.CREATE )

    self.obj10672=MT_pre__Trigger_T(self)
    self.obj10672.isGraphObjectVisual = True

    if(hasattr(self.obj10672, '_setHierarchicalLink')):
      self.obj10672._setHierarchicalLink(False)

    # MT_label__
    self.obj10672.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj10672.MT_pivotOut__.setValue('')
    self.obj10672.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10672.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10672.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10672.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10672.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10672.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10672.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10672.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10672.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10672.MT_pivotIn__.setValue('')
    self.obj10672.MT_pivotIn__.setNone()

    self.obj10672.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(220.0,300.0,self.obj10672)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10672.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10672)
    self.globalAndLocalPostcondition(self.obj10672, rootNode)
    self.obj10672.postAction( rootNode.CREATE )

    self.obj10658=MT_pre__Par(self)
    self.obj10658.isGraphObjectVisual = True

    if(hasattr(self.obj10658, '_setHierarchicalLink')):
      self.obj10658._setHierarchicalLink(False)

    # MT_label__
    self.obj10658.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj10658.MT_pivotOut__.setValue('')
    self.obj10658.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10658.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10658.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10658.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10658.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj10658.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10658.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10658.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10658.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj10658.MT_pivotIn__.setValue('')
    self.obj10658.MT_pivotIn__.setNone()

    self.obj10658.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(280.0,200.0,self.obj10658)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10658.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10658)
    self.globalAndLocalPostcondition(self.obj10658, rootNode)
    self.obj10658.postAction( rootNode.CREATE )

    self.obj10667=MT_pre__directLink_T(self)
    self.obj10667.isGraphObjectVisual = True

    if(hasattr(self.obj10667, '_setHierarchicalLink')):
      self.obj10667._setHierarchicalLink(False)

    # MT_label__
    self.obj10667.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj10667.MT_pivotOut__.setValue('')
    self.obj10667.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10667.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10667.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10667.MT_pivotIn__.setValue('')
    self.obj10667.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10667.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10667.MT_pre__associationType.setHeight(15)

    self.obj10667.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(402.0,321.0,self.obj10667)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10667.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10667)
    self.globalAndLocalPostcondition(self.obj10667, rootNode)
    self.obj10667.postAction( rootNode.CREATE )

    self.obj10668=MT_pre__directLink_T(self)
    self.obj10668.isGraphObjectVisual = True

    if(hasattr(self.obj10668, '_setHierarchicalLink')):
      self.obj10668._setHierarchicalLink(False)

    # MT_label__
    self.obj10668.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj10668.MT_pivotOut__.setValue('')
    self.obj10668.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10668.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10668.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10668.MT_pivotIn__.setValue('')
    self.obj10668.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10668.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10668.MT_pre__associationType.setHeight(15)

    self.obj10668.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(472.0,351.0,self.obj10668)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10668.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10668)
    self.globalAndLocalPostcondition(self.obj10668, rootNode)
    self.obj10668.postAction( rootNode.CREATE )

    self.obj10665=MT_pre__directLink_S(self)
    self.obj10665.isGraphObjectVisual = True

    if(hasattr(self.obj10665, '_setHierarchicalLink')):
      self.obj10665._setHierarchicalLink(False)

    # MT_label__
    self.obj10665.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj10665.MT_pivotOut__.setValue('')
    self.obj10665.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10665.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10665.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10665.MT_pivotIn__.setValue('')
    self.obj10665.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10665.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10665.MT_pre__associationType.setHeight(15)

    self.obj10665.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(390.5,104.0,self.obj10665)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10665.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10665)
    self.globalAndLocalPostcondition(self.obj10665, rootNode)
    self.obj10665.postAction( rootNode.CREATE )

    self.obj10666=MT_pre__directLink_S(self)
    self.obj10666.isGraphObjectVisual = True

    if(hasattr(self.obj10666, '_setHierarchicalLink')):
      self.obj10666._setHierarchicalLink(False)

    # MT_label__
    self.obj10666.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj10666.MT_pivotOut__.setValue('')
    self.obj10666.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10666.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10666.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10666.MT_pivotIn__.setValue('')
    self.obj10666.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10666.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10666.MT_pre__associationType.setHeight(15)

    self.obj10666.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(318.5,173.0,self.obj10666)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10666.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10666)
    self.globalAndLocalPostcondition(self.obj10666, rootNode)
    self.obj10666.postAction( rootNode.CREATE )

    self.obj10659=MT_pre__trace_link(self)
    self.obj10659.isGraphObjectVisual = True

    if(hasattr(self.obj10659, '_setHierarchicalLink')):
      self.obj10659._setHierarchicalLink(False)

    # MT_label__
    self.obj10659.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj10659.MT_pivotOut__.setValue('')
    self.obj10659.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10659.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10659.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10659.MT_pivotIn__.setValue('')
    self.obj10659.MT_pivotIn__.setNone()

    self.obj10659.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(382.0,258.0,self.obj10659)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10659.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10659)
    self.globalAndLocalPostcondition(self.obj10659, rootNode)
    self.obj10659.postAction( rootNode.CREATE )

    self.obj10660=MT_pre__trace_link(self)
    self.obj10660.isGraphObjectVisual = True

    if(hasattr(self.obj10660, '_setHierarchicalLink')):
      self.obj10660._setHierarchicalLink(False)

    # MT_label__
    self.obj10660.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj10660.MT_pivotOut__.setValue('')
    self.obj10660.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10660.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10660.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10660.MT_pivotIn__.setValue('')
    self.obj10660.MT_pivotIn__.setNone()

    self.obj10660.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(329.5,248.0,self.obj10660)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10660.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10660)
    self.globalAndLocalPostcondition(self.obj10660, rootNode)
    self.obj10660.postAction( rootNode.CREATE )

    self.obj10661=MT_pre__trace_link(self)
    self.obj10661.isGraphObjectVisual = True

    if(hasattr(self.obj10661, '_setHierarchicalLink')):
      self.obj10661._setHierarchicalLink(False)

    # MT_label__
    self.obj10661.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj10661.MT_pivotOut__.setValue('')
    self.obj10661.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10661.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10661.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10661.MT_pivotIn__.setValue('')
    self.obj10661.MT_pivotIn__.setNone()

    self.obj10661.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(482.0,238.0,self.obj10661)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10661.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10661)
    self.globalAndLocalPostcondition(self.obj10661, rootNode)
    self.obj10661.postAction( rootNode.CREATE )

    self.obj10662=MT_pre__trace_link(self)
    self.obj10662.isGraphObjectVisual = True

    if(hasattr(self.obj10662, '_setHierarchicalLink')):
      self.obj10662._setHierarchicalLink(False)

    # MT_label__
    self.obj10662.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj10662.MT_pivotOut__.setValue('')
    self.obj10662.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10662.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10662.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10662.MT_pivotIn__.setValue('')
    self.obj10662.MT_pivotIn__.setNone()

    self.obj10662.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(429.5,228.0,self.obj10662)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10662.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10662)
    self.globalAndLocalPostcondition(self.obj10662, rootNode)
    self.obj10662.postAction( rootNode.CREATE )

    self.obj10663=MT_pre__trace_link(self)
    self.obj10663.isGraphObjectVisual = True

    if(hasattr(self.obj10663, '_setHierarchicalLink')):
      self.obj10663._setHierarchicalLink(False)

    # MT_label__
    self.obj10663.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj10663.MT_pivotOut__.setValue('')
    self.obj10663.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10663.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10663.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10663.MT_pivotIn__.setValue('')
    self.obj10663.MT_pivotIn__.setNone()

    self.obj10663.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(452.0,288.0,self.obj10663)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10663.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10663)
    self.globalAndLocalPostcondition(self.obj10663, rootNode)
    self.obj10663.postAction( rootNode.CREATE )

    self.obj10664=MT_pre__trace_link(self)
    self.obj10664.isGraphObjectVisual = True

    if(hasattr(self.obj10664, '_setHierarchicalLink')):
      self.obj10664._setHierarchicalLink(False)

    # MT_label__
    self.obj10664.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj10664.MT_pivotOut__.setValue('')
    self.obj10664.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10664.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10664.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10664.MT_pivotIn__.setValue('')
    self.obj10664.MT_pivotIn__.setNone()

    self.obj10664.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(399.5,278.0,self.obj10664)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10664.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10664)
    self.globalAndLocalPostcondition(self.obj10664, rootNode)
    self.obj10664.postAction( rootNode.CREATE )

    self.obj10656=LHS(self)
    self.obj10656.isGraphObjectVisual = True

    if(hasattr(self.obj10656, '_setHierarchicalLink')):
      self.obj10656._setHierarchicalLink(False)

    # constraint
    self.obj10656.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj10656.constraint.setHeight(15)

    self.obj10656.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj10656)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10656.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10656)
    self.globalAndLocalPostcondition(self.obj10656, rootNode)
    self.obj10656.postAction( rootNode.CREATE )

    # Connections for obj10670 (graphObject_: Obj20) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj10669 (graphObject_: Obj19) of type MT_pre__Transition
    self.drawConnections(
 )
    # Connections for obj10657 (graphObject_: Obj7) of type MT_pre__State
    self.drawConnections(
(self.obj10657,self.obj10665,[357.0, 149.0, 390.5, 104.0],"true", 2),
(self.obj10657,self.obj10666,[357.0, 149.0, 318.5, 173.0],"true", 2) )
    # Connections for obj10671 (graphObject_: Obj21) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj10671,self.obj10659,[302.0, 341.0, 382.0, 258.0],"true", 2),
(self.obj10671,self.obj10660,[302.0, 341.0, 329.5, 248.0],"true", 2),
(self.obj10671,self.obj10667,[302.0, 341.0, 402.0, 321.0],"true", 2) )
    # Connections for obj10672 (graphObject_: Obj22) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj10672,self.obj10663,[442.0, 401.0, 452.0, 288.0],"true", 2),
(self.obj10672,self.obj10664,[442.0, 401.0, 399.5, 278.0],"true", 2) )
    # Connections for obj10658 (graphObject_: Obj8) of type MT_pre__Par
    self.drawConnections(
(self.obj10658,self.obj10661,[502.0, 301.0, 482.0, 238.0],"true", 2),
(self.obj10658,self.obj10662,[502.0, 301.0, 429.5, 228.0],"true", 2),
(self.obj10658,self.obj10668,[502.0, 301.0, 472.0, 351.0],"true", 2) )
    # Connections for obj10667 (graphObject_: Obj17) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10667,self.obj10658,[402.0, 321.0, 502.0, 301.0],"true", 2) )
    # Connections for obj10668 (graphObject_: Obj18) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10668,self.obj10672,[472.0, 351.0, 442.0, 401.0],"true", 2) )
    # Connections for obj10665 (graphObject_: Obj15) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10665,self.obj10670,[390.5, 104.0, 462.0, 175.0],"true", 2) )
    # Connections for obj10666 (graphObject_: Obj16) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10666,self.obj10669,[318.5, 173.0, 275.0, 195.0],"true", 2) )
    # Connections for obj10659 (graphObject_: Obj9) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10659,self.obj10670,[382.0, 258.0, 462.0, 175.0],"true", 2) )
    # Connections for obj10660 (graphObject_: Obj10) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10660,self.obj10657,[329.5, 248.0, 357.0, 149.0],"true", 2) )
    # Connections for obj10661 (graphObject_: Obj11) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10661,self.obj10670,[482.0, 238.0, 462.0, 175.0],"true", 2) )
    # Connections for obj10662 (graphObject_: Obj12) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10662,self.obj10657,[429.5, 228.0, 357.0, 149.0],"true", 2) )
    # Connections for obj10663 (graphObject_: Obj13) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10663,self.obj10670,[452.0, 288.0, 462.0, 175.0],"true", 2) )
    # Connections for obj10664 (graphObject_: Obj14) of type MT_pre__trace_link
    self.drawConnections(
(self.obj10664,self.obj10657,[399.5, 278.0, 357.0, 149.0],"true", 2) )
    # Connections for obj10656 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )

newfunction = state2trans2exitptTrue_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
