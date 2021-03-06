"""
__LocalDef1ProcPart3_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Mar  5 02:03:31 2015
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__LocalDef import *
from MT_pre__directLink_T import *
from MT_pre__Proc import *
from LHS import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__LocalDef import *
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

def LocalDef1ProcPart3_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('LocalDef1ProcPart3_Complete')
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


    self.obj136892=MT_pre__LocalDef(self)
    self.obj136892.isGraphObjectVisual = True

    if(hasattr(self.obj136892, '_setHierarchicalLink')):
      self.obj136892._setHierarchicalLink(False)

    # MT_label__
    self.obj136892.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj136892.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj136892.MT_subtypeMatching__.setValue(('True', 0))
    self.obj136892.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj136892.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj136892.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj136892.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj136892.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj136892.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj136892.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj136892.MT_pivotIn__.setValue('element1')

    self.obj136892.graphClass_= graph_MT_pre__LocalDef
    if self.genGraphics:
       new_obj = graph_MT_pre__LocalDef(60.0,40.0,self.obj136892)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj136892.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136892)
    self.globalAndLocalPostcondition(self.obj136892, rootNode)
    self.obj136892.postAction( rootNode.CREATE )

    self.obj147408=MT_pre__directLink_T(self)
    self.obj147408.isGraphObjectVisual = True

    if(hasattr(self.obj147408, '_setHierarchicalLink')):
      self.obj147408._setHierarchicalLink(False)

    # MT_label__
    self.obj147408.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj147408.MT_pivotOut__.setValue('')
    self.obj147408.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj147408.MT_subtypeMatching__.setValue(('True', 0))
    self.obj147408.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj147408.MT_pivotIn__.setValue('')
    self.obj147408.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj147408.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj147408.MT_pre__associationType.setHeight(15)

    self.obj147408.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(277.0,241.0,self.obj147408)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj147408.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147408)
    self.globalAndLocalPostcondition(self.obj147408, rootNode)
    self.obj147408.postAction( rootNode.CREATE )

    self.obj157934=MT_pre__directLink_T(self)
    self.obj157934.isGraphObjectVisual = True

    if(hasattr(self.obj157934, '_setHierarchicalLink')):
      self.obj157934._setHierarchicalLink(False)

    # MT_label__
    self.obj157934.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj157934.MT_pivotOut__.setValue('')
    self.obj157934.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj157934.MT_subtypeMatching__.setValue(('True', 0))
    self.obj157934.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj157934.MT_pivotIn__.setValue('')
    self.obj157934.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj157934.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj157934.MT_pre__associationType.setHeight(15)

    self.obj157934.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(367.0,191.0,self.obj157934)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157934.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157934)
    self.globalAndLocalPostcondition(self.obj157934, rootNode)
    self.obj157934.postAction( rootNode.CREATE )

    self.obj147405=MT_pre__Proc(self)
    self.obj147405.isGraphObjectVisual = True

    if(hasattr(self.obj147405, '_setHierarchicalLink')):
      self.obj147405._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj147405.MT_pivotOut__.setValue('')
    self.obj147405.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj147405.MT_subtypeMatching__.setValue(('True', 1))
    self.obj147405.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj147405.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj147405.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj147405.MT_pivotIn__.setValue('')
    self.obj147405.MT_pivotIn__.setNone()

    # MT_label__
    self.obj147405.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj147405.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj147405.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj147405.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj147405.MT_pre__name.setHeight(15)

    self.obj147405.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(60.0,240.0,self.obj147405)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj147405.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147405)
    self.globalAndLocalPostcondition(self.obj147405, rootNode)
    self.obj147405.postAction( rootNode.CREATE )

    self.obj157931=MT_pre__Proc(self)
    self.obj157931.isGraphObjectVisual = True

    if(hasattr(self.obj157931, '_setHierarchicalLink')):
      self.obj157931._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj157931.MT_pivotOut__.setValue('')
    self.obj157931.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj157931.MT_subtypeMatching__.setValue(('True', 1))
    self.obj157931.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj157931.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj157931.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj157931.MT_pivotIn__.setValue('')
    self.obj157931.MT_pivotIn__.setNone()

    # MT_label__
    self.obj157931.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj157931.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj157931.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj157931.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj157931.MT_pre__name.setHeight(15)

    self.obj157931.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(240.0,140.0,self.obj157931)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj157931.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157931)
    self.globalAndLocalPostcondition(self.obj157931, rootNode)
    self.obj157931.postAction( rootNode.CREATE )

    self.obj136891=LHS(self)
    self.obj136891.isGraphObjectVisual = True

    if(hasattr(self.obj136891, '_setHierarchicalLink')):
      self.obj136891._setHierarchicalLink(False)

    # constraint
    self.obj136891.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj136891.constraint.setHeight(15)

    self.obj136891.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,20.0,self.obj136891)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj136891.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136891)
    self.globalAndLocalPostcondition(self.obj136891, rootNode)
    self.obj136891.postAction( rootNode.CREATE )

    # Connections for obj136892 (graphObject_: Obj25) of type MT_pre__LocalDef
    self.drawConnections(
(self.obj136892,self.obj147408,[277.0, 141.0, 277.0, 241.0],"true", 2),
(self.obj136892,self.obj157934,[277.0, 141.0, 367.0, 191.0],"true", 2) )
    # Connections for obj147408 (graphObject_: Obj27) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj147408,self.obj147405,[277.0, 241.0, 277.0, 341.0],"true", 2) )
    # Connections for obj157934 (graphObject_: Obj29) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj157934,self.obj157931,[367.0, 191.0, 457.0, 241.0],"true", 2) )
    # Connections for obj147405 (graphObject_: Obj26) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj157931 (graphObject_: Obj28) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj136891 (graphObject_: Obj24) of type LHS
    self.drawConnections(
 )

newfunction = LocalDef1ProcPart3_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
