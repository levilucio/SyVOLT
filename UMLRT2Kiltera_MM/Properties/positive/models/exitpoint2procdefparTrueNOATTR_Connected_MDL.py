"""
__exitpoint2procdefparTrueNOATTR_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 14:18:18 2015
______________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__State import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__State import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__directLink_S import *
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

def exitpoint2procdefparTrueNOATTR_Connected_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('exitpoint2procdefparTrueNOATTR_Connected')
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


    self.obj10653=MT_pre__ExitPoint(self)
    self.obj10653.isGraphObjectVisual = True

    if(hasattr(self.obj10653, '_setHierarchicalLink')):
      self.obj10653._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10653.MT_pivotOut__.setValue('')
    self.obj10653.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10653.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10653.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10653.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10653.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10653.MT_pivotIn__.setValue('')
    self.obj10653.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10653.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10653.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10653.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10653.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10653.MT_pre__name.setHeight(15)

    self.obj10653.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(300.0,220.0,self.obj10653)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10653.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10653)
    self.globalAndLocalPostcondition(self.obj10653, rootNode)
    self.obj10653.postAction( rootNode.CREATE )

    self.obj10647=MT_pre__State(self)
    self.obj10647.isGraphObjectVisual = True

    if(hasattr(self.obj10647, '_setHierarchicalLink')):
      self.obj10647._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10647.MT_pivotOut__.setValue('')
    self.obj10647.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10647.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10647.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10647.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10647.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10647.MT_pivotIn__.setValue('')
    self.obj10647.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10647.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj10647.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10647.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10647.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10647.MT_pre__name.setHeight(15)

    self.obj10647.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(80.0,300.0,self.obj10647)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10647.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10647)
    self.globalAndLocalPostcondition(self.obj10647, rootNode)
    self.obj10647.postAction( rootNode.CREATE )

    self.obj10649=MT_pre__directLink_S(self)
    self.obj10649.isGraphObjectVisual = True

    if(hasattr(self.obj10649, '_setHierarchicalLink')):
      self.obj10649._setHierarchicalLink(False)

    # MT_label__
    self.obj10649.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj10649.MT_pivotOut__.setValue('')
    self.obj10649.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10649.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10649.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10649.MT_pivotIn__.setValue('')
    self.obj10649.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10649.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10649.MT_pre__associationType.setHeight(15)

    self.obj10649.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(361.0,359.0,self.obj10649)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10649.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10649)
    self.globalAndLocalPostcondition(self.obj10649, rootNode)
    self.obj10649.postAction( rootNode.CREATE )

    self.obj10646=LHS(self)
    self.obj10646.isGraphObjectVisual = True

    if(hasattr(self.obj10646, '_setHierarchicalLink')):
      self.obj10646._setHierarchicalLink(False)

    # constraint
    self.obj10646.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj10646.constraint.setHeight(15)

    self.obj10646.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj10646)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10646.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10646)
    self.globalAndLocalPostcondition(self.obj10646, rootNode)
    self.obj10646.postAction( rootNode.CREATE )

    # Connections for obj10653 (graphObject_: Obj16) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj10647 (graphObject_: Obj10) of type MT_pre__State
    self.drawConnections(
(self.obj10647,self.obj10649,[277.0, 375.0, 361.0, 359.0],"true", 2) )
    # Connections for obj10649 (graphObject_: Obj12) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj10649,self.obj10653,[361.0, 359.0, 497.0, 295.0],"true", 2) )
    # Connections for obj10646 (graphObject_: Obj9) of type LHS
    self.drawConnections(
 )

newfunction = exitpoint2procdefparTrueNOATTR_Connected_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
