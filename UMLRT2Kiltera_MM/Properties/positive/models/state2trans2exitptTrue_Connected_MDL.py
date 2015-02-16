"""
__state2trans2exitptTrue_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 16:12:52 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__Transition import *
from MT_pre__State import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__State import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__Transition import *
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

def state2trans2exitptTrue_Connected_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('state2trans2exitptTrue_Connected')
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
       new_obj = graph_MT_pre__ExitPoint(300.0,180.0,self.obj31749)
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
       new_obj = graph_MT_pre__Transition(100.0,280.0,self.obj42266)
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
       new_obj = graph_MT_pre__State(80.0,80.0,self.obj31744)
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
       new_obj = graph_MT_pre__directLink_S(289.5,255.0,self.obj52776)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52776.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52776)
    self.globalAndLocalPostcondition(self.obj52776, rootNode)
    self.obj52776.postAction( rootNode.CREATE )

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
(self.obj31744,self.obj52775,[277.0, 155.0, 389.5, 205.0],"true", 2),
(self.obj31744,self.obj52776,[277.0, 155.0, 289.5, 255.0],"true", 2) )
    # Connections for obj52775 (graphObject_: Obj100) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52775,self.obj31749,[389.5, 205.0, 502.0, 255.0],"true", 2) )
    # Connections for obj52776 (graphObject_: Obj101) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52776,self.obj42266,[289.5, 255.0, 302.0, 355.0],"true", 2) )
    # Connections for obj31743 (graphObject_: Obj90) of type LHS
    self.drawConnections(
 )

newfunction = state2trans2exitptTrue_Connected_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
