"""
__ListenBranch1ProcPart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Mar  4 23:45:32 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__directLink_T import *
from MT_pre__ListenBranch import *
from MT_pre__Proc import *
from LHS import *
from graph_MT_pre__ListenBranch import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Proc import *
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

def ListenBranch1ProcPart2_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ListenBranch1ProcPart2_Complete')
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


    self.obj84288=MT_pre__directLink_T(self)
    self.obj84288.isGraphObjectVisual = True

    if(hasattr(self.obj84288, '_setHierarchicalLink')):
      self.obj84288._setHierarchicalLink(False)

    # MT_label__
    self.obj84288.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj84288.MT_pivotOut__.setValue('')
    self.obj84288.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj84288.MT_subtypeMatching__.setValue(('True', 0))
    self.obj84288.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj84288.MT_pivotIn__.setValue('')
    self.obj84288.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj84288.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj84288.MT_pre__associationType.setHeight(15)

    self.obj84288.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(287.0,221.0,self.obj84288)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj84288.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84288)
    self.globalAndLocalPostcondition(self.obj84288, rootNode)
    self.obj84288.postAction( rootNode.CREATE )

    self.obj73770=MT_pre__ListenBranch(self)
    self.obj73770.isGraphObjectVisual = True

    if(hasattr(self.obj73770, '_setHierarchicalLink')):
      self.obj73770._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73770.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj73770.MT_subtypeMatching__.setValue(('True', 0))
    self.obj73770.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73770.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73770.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73770.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj73770.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj73770.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73770.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73770.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73770.MT_pre__name.setHeight(15)

    self.obj73770.graphClass_= graph_MT_pre__ListenBranch
    if self.genGraphics:
       new_obj = graph_MT_pre__ListenBranch(60.0,40.0,self.obj73770)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73770.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73770)
    self.globalAndLocalPostcondition(self.obj73770, rootNode)
    self.obj73770.postAction( rootNode.CREATE )

    self.obj84285=MT_pre__Proc(self)
    self.obj84285.isGraphObjectVisual = True

    if(hasattr(self.obj84285, '_setHierarchicalLink')):
      self.obj84285._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj84285.MT_pivotOut__.setValue('')
    self.obj84285.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj84285.MT_subtypeMatching__.setValue(('True', 1))
    self.obj84285.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj84285.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj84285.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj84285.MT_pivotIn__.setValue('')
    self.obj84285.MT_pivotIn__.setNone()

    # MT_label__
    self.obj84285.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj84285.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj84285.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj84285.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj84285.MT_pre__name.setHeight(15)

    self.obj84285.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(80.0,200.0,self.obj84285)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84285.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84285)
    self.globalAndLocalPostcondition(self.obj84285, rootNode)
    self.obj84285.postAction( rootNode.CREATE )

    self.obj73769=LHS(self)
    self.obj73769.isGraphObjectVisual = True

    if(hasattr(self.obj73769, '_setHierarchicalLink')):
      self.obj73769._setHierarchicalLink(False)

    # constraint
    self.obj73769.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj73769.constraint.setHeight(15)

    self.obj73769.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj73769)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73769.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73769)
    self.globalAndLocalPostcondition(self.obj73769, rootNode)
    self.obj73769.postAction( rootNode.CREATE )

    # Connections for obj84288 (graphObject_: Obj15) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj84288,self.obj84285,[287.0, 221.0, 297.0, 301.0],"true", 2) )
    # Connections for obj73770 (graphObject_: Obj13) of type MT_pre__ListenBranch
    self.drawConnections(
(self.obj73770,self.obj84288,[277.0, 141.0, 287.0, 221.0],"true", 2) )
    # Connections for obj84285 (graphObject_: Obj14) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj73769 (graphObject_: Obj12) of type LHS
    self.drawConnections(
 )

newfunction = ListenBranch1ProcPart2_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
