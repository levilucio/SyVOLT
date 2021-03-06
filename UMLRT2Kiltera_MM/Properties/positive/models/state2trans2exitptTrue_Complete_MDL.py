"""
__state2trans2exitptTrue_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 21:52:20 2015
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


    self.obj52755=MT_pre__ExitPoint(self)
    self.obj52755.isGraphObjectVisual = True

    if(hasattr(self.obj52755, '_setHierarchicalLink')):
      self.obj52755._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52755.MT_pivotOut__.setValue('')
    self.obj52755.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52755.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52755.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52755.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52755.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52755.MT_pivotIn__.setValue('')
    self.obj52755.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52755.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj52755.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52755.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52755.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52755.MT_pre__name.setHeight(15)

    self.obj52755.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(260.0,100.0,self.obj52755)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52755.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52755)
    self.globalAndLocalPostcondition(self.obj52755, rootNode)
    self.obj52755.postAction( rootNode.CREATE )

    self.obj52756=MT_pre__Transition(self)
    self.obj52756.isGraphObjectVisual = True

    if(hasattr(self.obj52756, '_setHierarchicalLink')):
      self.obj52756._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52756.MT_pivotOut__.setValue('')
    self.obj52756.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52756.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52756.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52756.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52756.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52756.MT_pivotIn__.setValue('')
    self.obj52756.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52756.MT_label__.setValue('13')

    # MT_pre__cardinality
    self.obj52756.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52756.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52756.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52756.MT_pre__name.setHeight(15)

    self.obj52756.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(73.0,120.0,self.obj52756)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52756.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52756)
    self.globalAndLocalPostcondition(self.obj52756, rootNode)
    self.obj52756.postAction( rootNode.CREATE )

    self.obj52757=MT_pre__State(self)
    self.obj52757.isGraphObjectVisual = True

    if(hasattr(self.obj52757, '_setHierarchicalLink')):
      self.obj52757._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52757.MT_pivotOut__.setValue('')
    self.obj52757.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52757.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52757.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52757.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52757.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52757.MT_pivotIn__.setValue('')
    self.obj52757.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52757.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj52757.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52757.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52757.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52757.MT_pre__name.setHeight(15)

    self.obj52757.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(160.0,74.0,self.obj52757)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52757.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52757)
    self.globalAndLocalPostcondition(self.obj52757, rootNode)
    self.obj52757.postAction( rootNode.CREATE )

    self.obj52758=MT_pre__ProcDef(self)
    self.obj52758.isGraphObjectVisual = True

    if(hasattr(self.obj52758, '_setHierarchicalLink')):
      self.obj52758._setHierarchicalLink(False)

    # MT_label__
    self.obj52758.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj52758.MT_pivotOut__.setValue('')
    self.obj52758.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52758.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52758.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52758.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52758.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj52758.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52758.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52758.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52758.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj52758.MT_pivotIn__.setValue('')
    self.obj52758.MT_pivotIn__.setNone()

    self.obj52758.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(80.0,240.0,self.obj52758)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52758.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52758)
    self.globalAndLocalPostcondition(self.obj52758, rootNode)
    self.obj52758.postAction( rootNode.CREATE )

    self.obj52759=MT_pre__Trigger_T(self)
    self.obj52759.isGraphObjectVisual = True

    if(hasattr(self.obj52759, '_setHierarchicalLink')):
      self.obj52759._setHierarchicalLink(False)

    # MT_label__
    self.obj52759.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj52759.MT_pivotOut__.setValue('')
    self.obj52759.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52759.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52759.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52759.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52759.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj52759.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52759.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52759.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52759.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj52759.MT_pivotIn__.setValue('')
    self.obj52759.MT_pivotIn__.setNone()

    self.obj52759.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(220.0,300.0,self.obj52759)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52759.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52759)
    self.globalAndLocalPostcondition(self.obj52759, rootNode)
    self.obj52759.postAction( rootNode.CREATE )

    self.obj52760=MT_pre__Par(self)
    self.obj52760.isGraphObjectVisual = True

    if(hasattr(self.obj52760, '_setHierarchicalLink')):
      self.obj52760._setHierarchicalLink(False)

    # MT_label__
    self.obj52760.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj52760.MT_pivotOut__.setValue('')
    self.obj52760.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52760.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52760.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52760.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52760.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj52760.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52760.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52760.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52760.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj52760.MT_pivotIn__.setValue('')
    self.obj52760.MT_pivotIn__.setNone()

    self.obj52760.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(280.0,200.0,self.obj52760)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52760.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52760)
    self.globalAndLocalPostcondition(self.obj52760, rootNode)
    self.obj52760.postAction( rootNode.CREATE )

    self.obj52761=MT_pre__directLink_T(self)
    self.obj52761.isGraphObjectVisual = True

    if(hasattr(self.obj52761, '_setHierarchicalLink')):
      self.obj52761._setHierarchicalLink(False)

    # MT_label__
    self.obj52761.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj52761.MT_pivotOut__.setValue('')
    self.obj52761.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52761.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52761.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52761.MT_pivotIn__.setValue('')
    self.obj52761.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52761.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52761.MT_pre__associationType.setHeight(15)

    self.obj52761.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(402.0,321.0,self.obj52761)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52761.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52761)
    self.globalAndLocalPostcondition(self.obj52761, rootNode)
    self.obj52761.postAction( rootNode.CREATE )

    self.obj52762=MT_pre__directLink_T(self)
    self.obj52762.isGraphObjectVisual = True

    if(hasattr(self.obj52762, '_setHierarchicalLink')):
      self.obj52762._setHierarchicalLink(False)

    # MT_label__
    self.obj52762.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj52762.MT_pivotOut__.setValue('')
    self.obj52762.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52762.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52762.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52762.MT_pivotIn__.setValue('')
    self.obj52762.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52762.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52762.MT_pre__associationType.setHeight(15)

    self.obj52762.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(472.0,351.0,self.obj52762)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52762.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52762)
    self.globalAndLocalPostcondition(self.obj52762, rootNode)
    self.obj52762.postAction( rootNode.CREATE )

    self.obj52763=MT_pre__directLink_S(self)
    self.obj52763.isGraphObjectVisual = True

    if(hasattr(self.obj52763, '_setHierarchicalLink')):
      self.obj52763._setHierarchicalLink(False)

    # MT_label__
    self.obj52763.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj52763.MT_pivotOut__.setValue('')
    self.obj52763.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52763.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52763.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52763.MT_pivotIn__.setValue('')
    self.obj52763.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52763.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52763.MT_pre__associationType.setHeight(15)

    self.obj52763.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(390.5,104.0,self.obj52763)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52763.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52763)
    self.globalAndLocalPostcondition(self.obj52763, rootNode)
    self.obj52763.postAction( rootNode.CREATE )

    self.obj52764=MT_pre__directLink_S(self)
    self.obj52764.isGraphObjectVisual = True

    if(hasattr(self.obj52764, '_setHierarchicalLink')):
      self.obj52764._setHierarchicalLink(False)

    # MT_label__
    self.obj52764.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj52764.MT_pivotOut__.setValue('')
    self.obj52764.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52764.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52764.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52764.MT_pivotIn__.setValue('')
    self.obj52764.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52764.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52764.MT_pre__associationType.setHeight(15)

    self.obj52764.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(318.5,173.0,self.obj52764)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52764.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52764)
    self.globalAndLocalPostcondition(self.obj52764, rootNode)
    self.obj52764.postAction( rootNode.CREATE )

    self.obj52765=MT_pre__trace_link(self)
    self.obj52765.isGraphObjectVisual = True

    if(hasattr(self.obj52765, '_setHierarchicalLink')):
      self.obj52765._setHierarchicalLink(False)

    # MT_label__
    self.obj52765.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj52765.MT_pivotOut__.setValue('')
    self.obj52765.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52765.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52765.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52765.MT_pivotIn__.setValue('')
    self.obj52765.MT_pivotIn__.setNone()

    self.obj52765.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(382.0,258.0,self.obj52765)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52765.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52765)
    self.globalAndLocalPostcondition(self.obj52765, rootNode)
    self.obj52765.postAction( rootNode.CREATE )

    self.obj52766=MT_pre__trace_link(self)
    self.obj52766.isGraphObjectVisual = True

    if(hasattr(self.obj52766, '_setHierarchicalLink')):
      self.obj52766._setHierarchicalLink(False)

    # MT_label__
    self.obj52766.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj52766.MT_pivotOut__.setValue('')
    self.obj52766.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52766.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52766.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52766.MT_pivotIn__.setValue('')
    self.obj52766.MT_pivotIn__.setNone()

    self.obj52766.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(329.5,248.0,self.obj52766)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52766.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52766)
    self.globalAndLocalPostcondition(self.obj52766, rootNode)
    self.obj52766.postAction( rootNode.CREATE )

    self.obj52767=MT_pre__trace_link(self)
    self.obj52767.isGraphObjectVisual = True

    if(hasattr(self.obj52767, '_setHierarchicalLink')):
      self.obj52767._setHierarchicalLink(False)

    # MT_label__
    self.obj52767.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj52767.MT_pivotOut__.setValue('')
    self.obj52767.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52767.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52767.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52767.MT_pivotIn__.setValue('')
    self.obj52767.MT_pivotIn__.setNone()

    self.obj52767.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(482.0,238.0,self.obj52767)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52767.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52767)
    self.globalAndLocalPostcondition(self.obj52767, rootNode)
    self.obj52767.postAction( rootNode.CREATE )

    self.obj52768=MT_pre__trace_link(self)
    self.obj52768.isGraphObjectVisual = True

    if(hasattr(self.obj52768, '_setHierarchicalLink')):
      self.obj52768._setHierarchicalLink(False)

    # MT_label__
    self.obj52768.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj52768.MT_pivotOut__.setValue('')
    self.obj52768.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52768.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52768.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52768.MT_pivotIn__.setValue('')
    self.obj52768.MT_pivotIn__.setNone()

    self.obj52768.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(429.5,228.0,self.obj52768)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52768.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52768)
    self.globalAndLocalPostcondition(self.obj52768, rootNode)
    self.obj52768.postAction( rootNode.CREATE )

    self.obj52769=MT_pre__trace_link(self)
    self.obj52769.isGraphObjectVisual = True

    if(hasattr(self.obj52769, '_setHierarchicalLink')):
      self.obj52769._setHierarchicalLink(False)

    # MT_label__
    self.obj52769.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj52769.MT_pivotOut__.setValue('')
    self.obj52769.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52769.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52769.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52769.MT_pivotIn__.setValue('')
    self.obj52769.MT_pivotIn__.setNone()

    self.obj52769.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(452.0,288.0,self.obj52769)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52769.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52769)
    self.globalAndLocalPostcondition(self.obj52769, rootNode)
    self.obj52769.postAction( rootNode.CREATE )

    self.obj52770=MT_pre__trace_link(self)
    self.obj52770.isGraphObjectVisual = True

    if(hasattr(self.obj52770, '_setHierarchicalLink')):
      self.obj52770._setHierarchicalLink(False)

    # MT_label__
    self.obj52770.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj52770.MT_pivotOut__.setValue('')
    self.obj52770.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52770.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52770.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52770.MT_pivotIn__.setValue('')
    self.obj52770.MT_pivotIn__.setNone()

    self.obj52770.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(399.5,278.0,self.obj52770)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52770.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52770)
    self.globalAndLocalPostcondition(self.obj52770, rootNode)
    self.obj52770.postAction( rootNode.CREATE )

    self.obj52771=LHS(self)
    self.obj52771.isGraphObjectVisual = True

    if(hasattr(self.obj52771, '_setHierarchicalLink')):
      self.obj52771._setHierarchicalLink(False)

    # constraint
    self.obj52771.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj52771.constraint.setHeight(15)

    self.obj52771.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj52771)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52771.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52771)
    self.globalAndLocalPostcondition(self.obj52771, rootNode)
    self.obj52771.postAction( rootNode.CREATE )

    # Connections for obj52755 (graphObject_: Obj29) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj52756 (graphObject_: Obj30) of type MT_pre__Transition
    self.drawConnections(
 )
    # Connections for obj52757 (graphObject_: Obj31) of type MT_pre__State
    self.drawConnections(
(self.obj52757,self.obj52763,[357.0, 149.0, 390.5, 104.0],"true", 2),
(self.obj52757,self.obj52764,[357.0, 149.0, 318.5, 173.0],"true", 2) )
    # Connections for obj52758 (graphObject_: Obj32) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj52758,self.obj52765,[302.0, 341.0, 382.0, 258.0],"true", 2),
(self.obj52758,self.obj52766,[302.0, 341.0, 329.5, 248.0],"true", 2),
(self.obj52758,self.obj52761,[302.0, 341.0, 402.0, 321.0],"true", 2) )
    # Connections for obj52759 (graphObject_: Obj33) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj52759,self.obj52769,[442.0, 401.0, 452.0, 288.0],"true", 2),
(self.obj52759,self.obj52770,[442.0, 401.0, 399.5, 278.0],"true", 2) )
    # Connections for obj52760 (graphObject_: Obj34) of type MT_pre__Par
    self.drawConnections(
(self.obj52760,self.obj52767,[502.0, 301.0, 482.0, 238.0],"true", 2),
(self.obj52760,self.obj52768,[502.0, 301.0, 429.5, 228.0],"true", 2),
(self.obj52760,self.obj52762,[502.0, 301.0, 472.0, 351.0],"true", 2) )
    # Connections for obj52761 (graphObject_: Obj35) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj52761,self.obj52760,[402.0, 321.0, 502.0, 301.0],"true", 2) )
    # Connections for obj52762 (graphObject_: Obj36) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj52762,self.obj52759,[472.0, 351.0, 442.0, 401.0],"true", 2) )
    # Connections for obj52763 (graphObject_: Obj37) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52763,self.obj52755,[390.5, 104.0, 462.0, 175.0],"true", 2) )
    # Connections for obj52764 (graphObject_: Obj38) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52764,self.obj52756,[318.5, 173.0, 275.0, 195.0],"true", 2) )
    # Connections for obj52765 (graphObject_: Obj39) of type MT_pre__trace_link
    self.drawConnections(
(self.obj52765,self.obj52755,[382.0, 258.0, 462.0, 175.0],"true", 2) )
    # Connections for obj52766 (graphObject_: Obj40) of type MT_pre__trace_link
    self.drawConnections(
(self.obj52766,self.obj52757,[329.5, 248.0, 357.0, 149.0],"true", 2) )
    # Connections for obj52767 (graphObject_: Obj41) of type MT_pre__trace_link
    self.drawConnections(
(self.obj52767,self.obj52755,[482.0, 238.0, 462.0, 175.0],"true", 2) )
    # Connections for obj52768 (graphObject_: Obj42) of type MT_pre__trace_link
    self.drawConnections(
(self.obj52768,self.obj52757,[429.5, 228.0, 357.0, 149.0],"true", 2) )
    # Connections for obj52769 (graphObject_: Obj43) of type MT_pre__trace_link
    self.drawConnections(
(self.obj52769,self.obj52755,[452.0, 288.0, 462.0, 175.0],"true", 2) )
    # Connections for obj52770 (graphObject_: Obj44) of type MT_pre__trace_link
    self.drawConnections(
(self.obj52770,self.obj52757,[399.5, 278.0, 357.0, 149.0],"true", 2) )
    # Connections for obj52771 (graphObject_: Obj45) of type LHS
    self.drawConnections(
 )

newfunction = state2trans2exitptTrue_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
