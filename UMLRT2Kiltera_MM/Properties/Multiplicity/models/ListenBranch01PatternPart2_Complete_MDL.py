"""
__ListenBranch01PatternPart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  2 20:09:14 2015
_________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__directLink_T import *
from MT_pre__Pattern import *
from MT_pre__ListenBranch import *
from graph_MT_pre__ListenBranch import *
from graph_MT_pre__Pattern import *
from graph_MT_pre__directLink_T import *
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

def ListenBranch01PatternPart2_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ListenBranch01PatternPart2_Complete')
    # --- ASG attributes over ---


    self.obj31667=LHS(self)
    self.obj31667.isGraphObjectVisual = True

    if(hasattr(self.obj31667, '_setHierarchicalLink')):
      self.obj31667._setHierarchicalLink(False)

    # constraint
    self.obj31667.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj31667.constraint.setHeight(15)

    self.obj31667.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,20.0,self.obj31667)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31667.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31667)
    self.globalAndLocalPostcondition(self.obj31667, rootNode)
    self.obj31667.postAction( rootNode.CREATE )

    self.obj42182=MT_pre__directLink_T(self)
    self.obj42182.isGraphObjectVisual = True

    if(hasattr(self.obj42182, '_setHierarchicalLink')):
      self.obj42182._setHierarchicalLink(False)

    # MT_label__
    self.obj42182.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj42182.MT_pivotOut__.setValue('')
    self.obj42182.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42182.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42182.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42182.MT_pivotIn__.setValue('')
    self.obj42182.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj42182.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42182.MT_pre__associationType.setHeight(15)

    self.obj42182.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(347.0,241.0,self.obj42182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42182)
    self.globalAndLocalPostcondition(self.obj42182, rootNode)
    self.obj42182.postAction( rootNode.CREATE )

    self.obj42181=MT_pre__Pattern(self)
    self.obj42181.isGraphObjectVisual = True

    if(hasattr(self.obj42181, '_setHierarchicalLink')):
      self.obj42181._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42181.MT_pivotOut__.setValue('')
    self.obj42181.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42181.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42181.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42181.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42181.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42181.MT_pivotIn__.setValue('')
    self.obj42181.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42181.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj42181.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42181.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42181.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42181.MT_pre__name.setHeight(15)

    self.obj42181.graphClass_= graph_MT_pre__Pattern
    if self.genGraphics:
       new_obj = graph_MT_pre__Pattern(180.0,220.0,self.obj42181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Pattern", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42181)
    self.globalAndLocalPostcondition(self.obj42181, rootNode)
    self.obj42181.postAction( rootNode.CREATE )

    self.obj31668=MT_pre__ListenBranch(self)
    self.obj31668.isGraphObjectVisual = True

    if(hasattr(self.obj31668, '_setHierarchicalLink')):
      self.obj31668._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj31668.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj31668.MT_subtypeMatching__.setValue(('True', 0))
    self.obj31668.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj31668.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31668.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj31668.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj31668.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj31668.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31668.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj31668.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj31668.MT_pre__name.setHeight(15)

    self.obj31668.graphClass_= graph_MT_pre__ListenBranch
    if self.genGraphics:
       new_obj = graph_MT_pre__ListenBranch(80.0,60.0,self.obj31668)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31668.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31668)
    self.globalAndLocalPostcondition(self.obj31668, rootNode)
    self.obj31668.postAction( rootNode.CREATE )

    # Connections for obj31667 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )
    # Connections for obj42182 (graphObject_: Obj9) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj42182,self.obj42181,[347.0, 241.0, 397.0, 321.0],"true", 2) )
    # Connections for obj42181 (graphObject_: Obj8) of type MT_pre__Pattern
    self.drawConnections(
 )
    # Connections for obj31668 (graphObject_: Obj7) of type MT_pre__ListenBranch
    self.drawConnections(
(self.obj31668,self.obj42182,[297.0, 161.0, 347.0, 241.0],"true", 2) )

newfunction = ListenBranch01PatternPart2_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
