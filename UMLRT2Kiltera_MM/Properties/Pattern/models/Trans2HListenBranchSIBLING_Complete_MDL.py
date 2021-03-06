"""
__Trans2HListenBranchSIBLING_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 11:06:07 2015
_________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Name import *
from MT_pre__Signal import *
from MT_pre__SIBLING0 import *
from MT_pre__trace_link import *
from MT_pre__directLink_S import *
from MT_pre__Inst import *
from MT_pre__directLink_T import *
from MT_pre__Transition import *
from MT_pre__ListenBranch import *
from MT_pre__Trigger_S import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__Trigger_S import *
from graph_MT_pre__Signal import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Name import *
from graph_MT_pre__Transition import *
from graph_MT_pre__ListenBranch import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Inst import *
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

def Trans2HListenBranchSIBLING_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('Trans2HListenBranchSIBLING_Complete')
    # --- ASG attributes over ---


    self.obj123=LHS(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # constraint
    self.obj123.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj123.constraint.setHeight(15)

    self.obj123.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj42275=MT_pre__Name(self)
    self.obj42275.isGraphObjectVisual = True

    if(hasattr(self.obj42275, '_setHierarchicalLink')):
      self.obj42275._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42275.MT_pivotOut__.setValue('')
    self.obj42275.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42275.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42275.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42275.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42275.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42275.MT_pivotIn__.setValue('')
    self.obj42275.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42275.MT_label__.setValue('25')

    # MT_pre__cardinality
    self.obj42275.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42275.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42275.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42275.MT_pre__name.setHeight(15)

    self.obj42275.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(38.0,120.0,self.obj42275)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42275.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42275)
    self.globalAndLocalPostcondition(self.obj42275, rootNode)
    self.obj42275.postAction( rootNode.CREATE )

    self.obj42277=MT_pre__Name(self)
    self.obj42277.isGraphObjectVisual = True

    if(hasattr(self.obj42277, '_setHierarchicalLink')):
      self.obj42277._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42277.MT_pivotOut__.setValue('')
    self.obj42277.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42277.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42277.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42277.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42277.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42277.MT_pivotIn__.setValue('')
    self.obj42277.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42277.MT_label__.setValue('27')

    # MT_pre__cardinality
    self.obj42277.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42277.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42277.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42277.MT_pre__name.setHeight(15)

    self.obj42277.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(40.0,100.0,self.obj42277)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42277.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42277)
    self.globalAndLocalPostcondition(self.obj42277, rootNode)
    self.obj42277.postAction( rootNode.CREATE )

    self.obj42279=MT_pre__Name(self)
    self.obj42279.isGraphObjectVisual = True

    if(hasattr(self.obj42279, '_setHierarchicalLink')):
      self.obj42279._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42279.MT_pivotOut__.setValue('')
    self.obj42279.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42279.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42279.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42279.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42279.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42279.MT_pivotIn__.setValue('')
    self.obj42279.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42279.MT_label__.setValue('29')

    # MT_pre__cardinality
    self.obj42279.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42279.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42279.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42279.MT_pre__name.setHeight(15)

    self.obj42279.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(40.0,240.0,self.obj42279)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42279.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42279)
    self.globalAndLocalPostcondition(self.obj42279, rootNode)
    self.obj42279.postAction( rootNode.CREATE )

    self.obj42281=MT_pre__Name(self)
    self.obj42281.isGraphObjectVisual = True

    if(hasattr(self.obj42281, '_setHierarchicalLink')):
      self.obj42281._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42281.MT_pivotOut__.setValue('')
    self.obj42281.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42281.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42281.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42281.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42281.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42281.MT_pivotIn__.setValue('')
    self.obj42281.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42281.MT_label__.setValue('31')

    # MT_pre__cardinality
    self.obj42281.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42281.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42281.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42281.MT_pre__name.setHeight(15)

    self.obj42281.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(40.0,265.0,self.obj42281)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42281.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42281)
    self.globalAndLocalPostcondition(self.obj42281, rootNode)
    self.obj42281.postAction( rootNode.CREATE )

    self.obj129=MT_pre__Signal(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_label__
    self.obj129.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj129.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj129.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj129.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('element4')

    self.obj129.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(265.0,121.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj125=MT_pre__SIBLING0(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_label__
    self.obj125.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj125.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj125.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj125.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('element2')

    self.obj125.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(35.0,121.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj21220=MT_pre__trace_link(self)
    self.obj21220.isGraphObjectVisual = True

    if(hasattr(self.obj21220, '_setHierarchicalLink')):
      self.obj21220._setHierarchicalLink(False)

    # MT_label__
    self.obj21220.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj21220.MT_pivotOut__.setValue('')
    self.obj21220.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21220.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21220.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21220.MT_pivotIn__.setValue('')
    self.obj21220.MT_pivotIn__.setNone()

    self.obj21220.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(339.5,205.0,self.obj21220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21220)
    self.globalAndLocalPostcondition(self.obj21220, rootNode)
    self.obj21220.postAction( rootNode.CREATE )

    self.obj10672=MT_pre__directLink_S(self)
    self.obj10672.isGraphObjectVisual = True

    if(hasattr(self.obj10672, '_setHierarchicalLink')):
      self.obj10672._setHierarchicalLink(False)

    # MT_label__
    self.obj10672.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10672.MT_pivotOut__.setValue('')
    self.obj10672.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10672.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10672.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10672.MT_pivotIn__.setValue('')
    self.obj10672.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10672.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10672.MT_pre__associationType.setHeight(15)

    self.obj10672.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(247.0,205.0,self.obj10672)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10672.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10672)
    self.globalAndLocalPostcondition(self.obj10672, rootNode)
    self.obj10672.postAction( rootNode.CREATE )

    self.obj10673=MT_pre__directLink_S(self)
    self.obj10673.isGraphObjectVisual = True

    if(hasattr(self.obj10673, '_setHierarchicalLink')):
      self.obj10673._setHierarchicalLink(False)

    # MT_label__
    self.obj10673.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj10673.MT_pivotOut__.setValue('')
    self.obj10673.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10673.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10673.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10673.MT_pivotIn__.setValue('')
    self.obj10673.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10673.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10673.MT_pre__associationType.setHeight(15)

    self.obj10673.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(327.0,135.0,self.obj10673)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10673.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10673)
    self.globalAndLocalPostcondition(self.obj10673, rootNode)
    self.obj10673.postAction( rootNode.CREATE )

    self.obj10674=MT_pre__directLink_S(self)
    self.obj10674.isGraphObjectVisual = True

    if(hasattr(self.obj10674, '_setHierarchicalLink')):
      self.obj10674._setHierarchicalLink(False)

    # MT_label__
    self.obj10674.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj10674.MT_pivotOut__.setValue('')
    self.obj10674.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10674.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10674.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10674.MT_pivotIn__.setValue('')
    self.obj10674.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10674.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10674.MT_pre__associationType.setHeight(15)

    self.obj10674.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(427.0,215.0,self.obj10674)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10674.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10674)
    self.globalAndLocalPostcondition(self.obj10674, rootNode)
    self.obj10674.postAction( rootNode.CREATE )

    self.obj21216=MT_pre__Inst(self)
    self.obj21216.isGraphObjectVisual = True

    if(hasattr(self.obj21216, '_setHierarchicalLink')):
      self.obj21216._setHierarchicalLink(False)

    # MT_label__
    self.obj21216.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj21216.MT_pivotOut__.setValue('')
    self.obj21216.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21216.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21216.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21216.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21216.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21216.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21216.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21216.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21216.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21216.MT_pivotIn__.setValue('')
    self.obj21216.MT_pivotIn__.setNone()

    self.obj21216.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(225.0,200.0,self.obj21216)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21216.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21216)
    self.globalAndLocalPostcondition(self.obj21216, rootNode)
    self.obj21216.postAction( rootNode.CREATE )

    self.obj42274=MT_pre__directLink_T(self)
    self.obj42274.isGraphObjectVisual = True

    if(hasattr(self.obj42274, '_setHierarchicalLink')):
      self.obj42274._setHierarchicalLink(False)

    # MT_label__
    self.obj42274.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj42274.MT_pivotOut__.setValue('')
    self.obj42274.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42274.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42274.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42274.MT_pivotIn__.setValue('')
    self.obj42274.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42274.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42274.MT_pre__associationType.setHeight(15)

    self.obj42274.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(354.5,301.0,self.obj42274)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42274.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42274)
    self.globalAndLocalPostcondition(self.obj42274, rootNode)
    self.obj42274.postAction( rootNode.CREATE )

    self.obj42276=MT_pre__directLink_T(self)
    self.obj42276.isGraphObjectVisual = True

    if(hasattr(self.obj42276, '_setHierarchicalLink')):
      self.obj42276._setHierarchicalLink(False)

    # MT_label__
    self.obj42276.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj42276.MT_pivotOut__.setValue('')
    self.obj42276.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42276.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42276.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42276.MT_pivotIn__.setValue('')
    self.obj42276.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42276.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42276.MT_pre__associationType.setHeight(15)

    self.obj42276.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(353.5,261.0,self.obj42276)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42276.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42276)
    self.globalAndLocalPostcondition(self.obj42276, rootNode)
    self.obj42276.postAction( rootNode.CREATE )

    self.obj42278=MT_pre__directLink_T(self)
    self.obj42278.isGraphObjectVisual = True

    if(hasattr(self.obj42278, '_setHierarchicalLink')):
      self.obj42278._setHierarchicalLink(False)

    # MT_label__
    self.obj42278.MT_label__.setValue('28')

    # MT_pivotOut__
    self.obj42278.MT_pivotOut__.setValue('')
    self.obj42278.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42278.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42278.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42278.MT_pivotIn__.setValue('')
    self.obj42278.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42278.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42278.MT_pre__associationType.setHeight(15)

    self.obj42278.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(354.5,251.0,self.obj42278)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42278.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42278)
    self.globalAndLocalPostcondition(self.obj42278, rootNode)
    self.obj42278.postAction( rootNode.CREATE )

    self.obj42280=MT_pre__directLink_T(self)
    self.obj42280.isGraphObjectVisual = True

    if(hasattr(self.obj42280, '_setHierarchicalLink')):
      self.obj42280._setHierarchicalLink(False)

    # MT_label__
    self.obj42280.MT_label__.setValue('30')

    # MT_pivotOut__
    self.obj42280.MT_pivotOut__.setValue('')
    self.obj42280.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42280.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42280.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42280.MT_pivotIn__.setValue('')
    self.obj42280.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42280.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42280.MT_pre__associationType.setHeight(15)

    self.obj42280.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(354.5,321.0,self.obj42280)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42280.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42280)
    self.globalAndLocalPostcondition(self.obj42280, rootNode)
    self.obj42280.postAction( rootNode.CREATE )

    self.obj42282=MT_pre__directLink_T(self)
    self.obj42282.isGraphObjectVisual = True

    if(hasattr(self.obj42282, '_setHierarchicalLink')):
      self.obj42282._setHierarchicalLink(False)

    # MT_label__
    self.obj42282.MT_label__.setValue('32')

    # MT_pivotOut__
    self.obj42282.MT_pivotOut__.setValue('')
    self.obj42282.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42282.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42282.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42282.MT_pivotIn__.setValue('')
    self.obj42282.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42282.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42282.MT_pre__associationType.setHeight(15)

    self.obj42282.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(354.5,331.0,self.obj42282)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42282.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42282)
    self.globalAndLocalPostcondition(self.obj42282, rootNode)
    self.obj42282.postAction( rootNode.CREATE )

    self.obj124=MT_pre__Transition(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj124.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj124.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj124.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj124.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__name.setHeight(15)

    self.obj124.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(35.0,34.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj42271=MT_pre__ListenBranch(self)
    self.obj42271.isGraphObjectVisual = True

    if(hasattr(self.obj42271, '_setHierarchicalLink')):
      self.obj42271._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42271.MT_pivotOut__.setValue('')
    self.obj42271.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42271.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42271.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42271.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42271.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42271.MT_pivotIn__.setValue('')
    self.obj42271.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42271.MT_label__.setValue('23')

    # MT_pre__cardinality
    self.obj42271.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42271.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42271.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42271.MT_pre__name.setHeight(15)

    self.obj42271.graphClass_= graph_MT_pre__ListenBranch
    if self.genGraphics:
       new_obj = graph_MT_pre__ListenBranch(40.0,200.0,self.obj42271)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42271.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42271)
    self.globalAndLocalPostcondition(self.obj42271, rootNode)
    self.obj42271.postAction( rootNode.CREATE )

    self.obj126=MT_pre__Trigger_S(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # MT_label__
    self.obj126.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj126.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj126.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj126.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj126.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj126.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj126.MT_pivotIn__.setValue('element3')

    self.obj126.graphClass_= graph_MT_pre__Trigger_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_S(216.0,34.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )
    # Connections for obj42275 (graphObject_: Obj39) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj42277 (graphObject_: Obj41) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj42279 (graphObject_: Obj43) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj42281 (graphObject_: Obj45) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj129 (graphObject_: Obj4) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj125 (graphObject_: Obj2) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj21220 (graphObject_: Obj13) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21220,self.obj124,[339.5, 205.0, 232.0, 109.0],"true", 2) )
    # Connections for obj10672 (graphObject_: Obj5) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10672,self.obj125,[247.0, 205.0, 232.0, 196.0],"true", 2) )
    # Connections for obj10673 (graphObject_: Obj6) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10673,self.obj126,[327.0, 135.0, 413.0, 109.0],"true", 2) )
    # Connections for obj10674 (graphObject_: Obj7) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10674,self.obj129,[427.0, 215.0, 462.0, 196.0],"true", 2) )
    # Connections for obj21216 (graphObject_: Obj11) of type MT_pre__Inst
    self.drawConnections(
(self.obj21216,self.obj21220,[447.0, 301.0, 339.5, 205.0],"true", 2),
(self.obj21216,self.obj42276,[447.0, 301.0, 353.5, 261.0],"true", 2),
(self.obj21216,self.obj42278,[447.0, 301.0, 354.5, 251.0],"true", 2),
(self.obj21216,self.obj42280,[447.0, 301.0, 354.5, 321.0],"true", 2),
(self.obj21216,self.obj42282,[447.0, 301.0, 354.5, 331.0],"true", 2) )
    # Connections for obj42274 (graphObject_: Obj38) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42274,self.obj21216,[354.5, 301.0, 447.0, 301.0],"true", 2) )
    # Connections for obj42276 (graphObject_: Obj40) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42276,self.obj42275,[353.5, 261.0, 260.0, 221.0],"true", 2) )
    # Connections for obj42278 (graphObject_: Obj42) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42278,self.obj42277,[354.5, 251.0, 262.0, 201.0],"true", 2) )
    # Connections for obj42280 (graphObject_: Obj44) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42280,self.obj42279,[354.5, 321.0, 262.0, 341.0],"true", 2) )
    # Connections for obj42282 (graphObject_: Obj46) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42282,self.obj42281,[354.5, 331.0, 262.0, 366.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__Transition
    self.drawConnections(
(self.obj124,self.obj10672,[232.0, 109.0, 247.0, 205.0],"true", 2),
(self.obj124,self.obj10673,[232.0, 109.0, 327.0, 135.0],"true", 2) )
    # Connections for obj42271 (graphObject_: Obj35) of type MT_pre__ListenBranch
    self.drawConnections(
(self.obj42271,self.obj42274,[262.0, 301.0, 354.5, 301.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj3) of type MT_pre__Trigger_S
    self.drawConnections(
(self.obj126,self.obj10674,[413.0, 109.0, 427.0, 215.0],"true", 2) )

newfunction = Trans2HListenBranchSIBLING_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
