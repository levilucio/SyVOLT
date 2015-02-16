"""
__state2trans2exitptTrue_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 16:18:35 2015
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


    self.obj31749=MT_pre__ExitPoint(self)
    self.obj31749.isGraphObjectVisual = True

    if(hasattr(self.obj31749, '_setHierarchicalLink')):
      self.obj31749._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31749.MT_pivotOut__.setValue('')
    self.obj31749.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31749.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31749.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31749.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31749.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31749.MT_pivotIn__.setValue('')
    self.obj31749.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31749.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj31749.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31749.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31749.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31749.MT_pre__name.setHeight(15)

    self.obj31749.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(260.0,100.0,self.obj31749)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31749.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31749)
    self.globalAndLocalPostcondition(self.obj31749, rootNode)
    self.obj31749.postAction( rootNode.CREATE )

    self.obj42266=MT_pre__Transition(self)
    self.obj42266.isGraphObjectVisual = True

    if(hasattr(self.obj42266, '_setHierarchicalLink')):
      self.obj42266._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42266.MT_pivotOut__.setValue('')
    self.obj42266.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42266.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42266.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42266.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42266.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42266.MT_pivotIn__.setValue('')
    self.obj42266.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42266.MT_label__.setValue('13')

    # MT_pre__cardinality
    self.obj42266.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42266.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42266.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42266.MT_pre__name.setHeight(15)

    self.obj42266.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(80.0,120.0,self.obj42266)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42266.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42266)
    self.globalAndLocalPostcondition(self.obj42266, rootNode)
    self.obj42266.postAction( rootNode.CREATE )

    self.obj31744=MT_pre__State(self)
    self.obj31744.isGraphObjectVisual = True

    if(hasattr(self.obj31744, '_setHierarchicalLink')):
      self.obj31744._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31744.MT_pivotOut__.setValue('')
    self.obj31744.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj31744.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31744.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31744.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31744.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31744.MT_pivotIn__.setValue('')
    self.obj31744.MT_pivotIn__.setNone()

    # MT_label__
    self.obj31744.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj31744.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31744.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31744.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31744.MT_pre__name.setHeight(15)

    self.obj31744.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(160.0,80.0,self.obj31744)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31744.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31744)
    self.globalAndLocalPostcondition(self.obj31744, rootNode)
    self.obj31744.postAction( rootNode.CREATE )

    self.obj63287=MT_pre__ProcDef(self)
    self.obj63287.isGraphObjectVisual = True

    if(hasattr(self.obj63287, '_setHierarchicalLink')):
      self.obj63287._setHierarchicalLink(False)

    # MT_label__
    self.obj63287.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj63287.MT_pivotOut__.setValue('')
    self.obj63287.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63287.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63287.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63287.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63287.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63287.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63287.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63287.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63287.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63287.MT_pivotIn__.setValue('')
    self.obj63287.MT_pivotIn__.setNone()

    self.obj63287.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(80.0,240.0,self.obj63287)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63287.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63287)
    self.globalAndLocalPostcondition(self.obj63287, rootNode)
    self.obj63287.postAction( rootNode.CREATE )

    self.obj63294=MT_pre__Trigger_T(self)
    self.obj63294.isGraphObjectVisual = True

    if(hasattr(self.obj63294, '_setHierarchicalLink')):
      self.obj63294._setHierarchicalLink(False)

    # MT_label__
    self.obj63294.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj63294.MT_pivotOut__.setValue('')
    self.obj63294.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63294.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63294.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63294.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63294.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63294.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63294.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63294.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63294.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63294.MT_pivotIn__.setValue('')
    self.obj63294.MT_pivotIn__.setNone()

    self.obj63294.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(220.0,300.0,self.obj63294)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63294.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63294)
    self.globalAndLocalPostcondition(self.obj63294, rootNode)
    self.obj63294.postAction( rootNode.CREATE )

    self.obj63290=MT_pre__Par(self)
    self.obj63290.isGraphObjectVisual = True

    if(hasattr(self.obj63290, '_setHierarchicalLink')):
      self.obj63290._setHierarchicalLink(False)

    # MT_label__
    self.obj63290.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj63290.MT_pivotOut__.setValue('')
    self.obj63290.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63290.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63290.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63290.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63290.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63290.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63290.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63290.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63290.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63290.MT_pivotIn__.setValue('')
    self.obj63290.MT_pivotIn__.setNone()

    self.obj63290.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(280.0,200.0,self.obj63290)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63290.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63290)
    self.globalAndLocalPostcondition(self.obj63290, rootNode)
    self.obj63290.postAction( rootNode.CREATE )

    self.obj63291=MT_pre__directLink_T(self)
    self.obj63291.isGraphObjectVisual = True

    if(hasattr(self.obj63291, '_setHierarchicalLink')):
      self.obj63291._setHierarchicalLink(False)

    # MT_label__
    self.obj63291.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj63291.MT_pivotOut__.setValue('')
    self.obj63291.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63291.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63291.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63291.MT_pivotIn__.setValue('')
    self.obj63291.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63291.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63291.MT_pre__associationType.setHeight(15)

    self.obj63291.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(402.0,321.0,self.obj63291)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63291.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63291)
    self.globalAndLocalPostcondition(self.obj63291, rootNode)
    self.obj63291.postAction( rootNode.CREATE )

    self.obj63295=MT_pre__directLink_T(self)
    self.obj63295.isGraphObjectVisual = True

    if(hasattr(self.obj63295, '_setHierarchicalLink')):
      self.obj63295._setHierarchicalLink(False)

    # MT_label__
    self.obj63295.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj63295.MT_pivotOut__.setValue('')
    self.obj63295.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63295.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63295.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63295.MT_pivotIn__.setValue('')
    self.obj63295.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj63295.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63295.MT_pre__associationType.setHeight(15)

    self.obj63295.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(472.0,351.0,self.obj63295)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63295.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63295)
    self.globalAndLocalPostcondition(self.obj63295, rootNode)
    self.obj63295.postAction( rootNode.CREATE )

    self.obj52775=MT_pre__directLink_S(self)
    self.obj52775.isGraphObjectVisual = True

    if(hasattr(self.obj52775, '_setHierarchicalLink')):
      self.obj52775._setHierarchicalLink(False)

    # MT_label__
    self.obj52775.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj52775.MT_pivotOut__.setValue('')
    self.obj52775.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52775.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52775.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52775.MT_pivotIn__.setValue('')
    self.obj52775.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52775.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==\'initialTransition\'\n')
    self.obj52775.MT_pre__associationType.setHeight(15)

    self.obj52775.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(389.5,205.0,self.obj52775)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52775.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52775)
    self.globalAndLocalPostcondition(self.obj52775, rootNode)
    self.obj52775.postAction( rootNode.CREATE )

    self.obj52776=MT_pre__directLink_S(self)
    self.obj52776.isGraphObjectVisual = True

    if(hasattr(self.obj52776, '_setHierarchicalLink')):
      self.obj52776._setHierarchicalLink(False)

    # MT_label__
    self.obj52776.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj52776.MT_pivotOut__.setValue('')
    self.obj52776.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52776.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52776.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52776.MT_pivotIn__.setValue('')
    self.obj52776.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52776.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52776.MT_pre__associationType.setHeight(15)

    self.obj52776.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(318.5,173.0,self.obj52776)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52776.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52776)
    self.globalAndLocalPostcondition(self.obj52776, rootNode)
    self.obj52776.postAction( rootNode.CREATE )

    self.obj63288=MT_pre__trace_link(self)
    self.obj63288.isGraphObjectVisual = True

    if(hasattr(self.obj63288, '_setHierarchicalLink')):
      self.obj63288._setHierarchicalLink(False)

    # MT_label__
    self.obj63288.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj63288.MT_pivotOut__.setValue('')
    self.obj63288.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63288.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63288.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63288.MT_pivotIn__.setValue('')
    self.obj63288.MT_pivotIn__.setNone()

    self.obj63288.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(382.0,258.0,self.obj63288)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63288.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63288)
    self.globalAndLocalPostcondition(self.obj63288, rootNode)
    self.obj63288.postAction( rootNode.CREATE )

    self.obj63289=MT_pre__trace_link(self)
    self.obj63289.isGraphObjectVisual = True

    if(hasattr(self.obj63289, '_setHierarchicalLink')):
      self.obj63289._setHierarchicalLink(False)

    # MT_label__
    self.obj63289.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj63289.MT_pivotOut__.setValue('')
    self.obj63289.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63289.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63289.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63289.MT_pivotIn__.setValue('')
    self.obj63289.MT_pivotIn__.setNone()

    self.obj63289.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(329.5,248.0,self.obj63289)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63289.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63289)
    self.globalAndLocalPostcondition(self.obj63289, rootNode)
    self.obj63289.postAction( rootNode.CREATE )

    self.obj63292=MT_pre__trace_link(self)
    self.obj63292.isGraphObjectVisual = True

    if(hasattr(self.obj63292, '_setHierarchicalLink')):
      self.obj63292._setHierarchicalLink(False)

    # MT_label__
    self.obj63292.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj63292.MT_pivotOut__.setValue('')
    self.obj63292.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63292.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63292.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63292.MT_pivotIn__.setValue('')
    self.obj63292.MT_pivotIn__.setNone()

    self.obj63292.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(482.0,238.0,self.obj63292)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63292.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63292)
    self.globalAndLocalPostcondition(self.obj63292, rootNode)
    self.obj63292.postAction( rootNode.CREATE )

    self.obj63293=MT_pre__trace_link(self)
    self.obj63293.isGraphObjectVisual = True

    if(hasattr(self.obj63293, '_setHierarchicalLink')):
      self.obj63293._setHierarchicalLink(False)

    # MT_label__
    self.obj63293.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj63293.MT_pivotOut__.setValue('')
    self.obj63293.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63293.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63293.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63293.MT_pivotIn__.setValue('')
    self.obj63293.MT_pivotIn__.setNone()

    self.obj63293.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(429.5,228.0,self.obj63293)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63293.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63293)
    self.globalAndLocalPostcondition(self.obj63293, rootNode)
    self.obj63293.postAction( rootNode.CREATE )

    self.obj63296=MT_pre__trace_link(self)
    self.obj63296.isGraphObjectVisual = True

    if(hasattr(self.obj63296, '_setHierarchicalLink')):
      self.obj63296._setHierarchicalLink(False)

    # MT_label__
    self.obj63296.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj63296.MT_pivotOut__.setValue('')
    self.obj63296.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63296.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63296.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63296.MT_pivotIn__.setValue('')
    self.obj63296.MT_pivotIn__.setNone()

    self.obj63296.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(452.0,288.0,self.obj63296)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63296.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63296)
    self.globalAndLocalPostcondition(self.obj63296, rootNode)
    self.obj63296.postAction( rootNode.CREATE )

    self.obj63297=MT_pre__trace_link(self)
    self.obj63297.isGraphObjectVisual = True

    if(hasattr(self.obj63297, '_setHierarchicalLink')):
      self.obj63297._setHierarchicalLink(False)

    # MT_label__
    self.obj63297.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj63297.MT_pivotOut__.setValue('')
    self.obj63297.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63297.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63297.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63297.MT_pivotIn__.setValue('')
    self.obj63297.MT_pivotIn__.setNone()

    self.obj63297.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(399.5,278.0,self.obj63297)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63297.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63297)
    self.globalAndLocalPostcondition(self.obj63297, rootNode)
    self.obj63297.postAction( rootNode.CREATE )

    self.obj31743=LHS(self)
    self.obj31743.isGraphObjectVisual = True

    if(hasattr(self.obj31743, '_setHierarchicalLink')):
      self.obj31743._setHierarchicalLink(False)

    # constraint
    self.obj31743.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj31743.constraint.setHeight(15)

    self.obj31743.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj31743)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31743.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31743)
    self.globalAndLocalPostcondition(self.obj31743, rootNode)
    self.obj31743.postAction( rootNode.CREATE )

    # Connections for obj31749 (graphObject_: Obj96) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj42266 (graphObject_: Obj99) of type MT_pre__Transition
    self.drawConnections(
 )
    # Connections for obj31744 (graphObject_: Obj91) of type MT_pre__State
    self.drawConnections(
(self.obj31744,self.obj52775,[357.0, 155.0, 389.5, 205.0],"true", 2),
(self.obj31744,self.obj52776,[357.0, 155.0, 318.5, 173.0],"true", 2) )
    # Connections for obj63287 (graphObject_: Obj102) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj63287,self.obj63288,[302.0, 341.0, 382.0, 258.0],"true", 2),
(self.obj63287,self.obj63289,[302.0, 341.0, 329.5, 248.0],"true", 2),
(self.obj63287,self.obj63291,[302.0, 341.0, 402.0, 321.0],"true", 2) )
    # Connections for obj63294 (graphObject_: Obj109) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj63294,self.obj63296,[442.0, 401.0, 452.0, 288.0],"true", 2),
(self.obj63294,self.obj63297,[442.0, 401.0, 399.5, 278.0],"true", 2) )
    # Connections for obj63290 (graphObject_: Obj105) of type MT_pre__Par
    self.drawConnections(
(self.obj63290,self.obj63292,[502.0, 301.0, 482.0, 238.0],"true", 2),
(self.obj63290,self.obj63293,[502.0, 301.0, 429.5, 228.0],"true", 2),
(self.obj63290,self.obj63295,[502.0, 301.0, 472.0, 351.0],"true", 2) )
    # Connections for obj63291 (graphObject_: Obj106) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj63291,self.obj63290,[402.0, 321.0, 502.0, 301.0],"true", 2) )
    # Connections for obj63295 (graphObject_: Obj110) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj63295,self.obj63294,[472.0, 351.0, 442.0, 401.0],"true", 2) )
    # Connections for obj52775 (graphObject_: Obj100) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52775,self.obj31749,[389.5, 205.0, 462.0, 175.0],"true", 2) )
    # Connections for obj52776 (graphObject_: Obj101) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52776,self.obj42266,[318.5, 173.0, 282.0, 195.0],"true", 2) )
    # Connections for obj63288 (graphObject_: Obj103) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63288,self.obj31749,[382.0, 258.0, 462.0, 175.0],"true", 2) )
    # Connections for obj63289 (graphObject_: Obj104) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63289,self.obj31744,[329.5, 248.0, 357.0, 155.0],"true", 2) )
    # Connections for obj63292 (graphObject_: Obj107) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63292,self.obj31749,[482.0, 238.0, 462.0, 175.0],"true", 2) )
    # Connections for obj63293 (graphObject_: Obj108) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63293,self.obj31744,[429.5, 228.0, 357.0, 155.0],"true", 2) )
    # Connections for obj63296 (graphObject_: Obj111) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63296,self.obj31749,[452.0, 288.0, 462.0, 175.0],"true", 2) )
    # Connections for obj63297 (graphObject_: Obj112) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63297,self.obj31744,[399.5, 278.0, 357.0, 155.0],"true", 2) )
    # Connections for obj31743 (graphObject_: Obj90) of type LHS
    self.drawConnections(
 )

newfunction = state2trans2exitptTrue_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
