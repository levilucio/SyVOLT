"""
__property1_connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Wed May  6 15:40:19 2015
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__EClass import *
from MT_pre__EReference import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__EReference import *
from graph_MT_pre__EClass import *
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

def property1_connected_MDL(self, rootNode, MT_pre__ECoreMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__ECoreMM ---
    if( MT_pre__ECoreMMRootNode ): 
        # author
        MT_pre__ECoreMMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__ECoreMMRootNode.description.setValue('\n')
        MT_pre__ECoreMMRootNode.description.setHeight(15)

        # name
        MT_pre__ECoreMMRootNode.name.setValue('')
        MT_pre__ECoreMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('property1_connected')
    # --- ASG attributes over ---


    self.obj38=MT_pre__EClass(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # MT_label__
    self.obj38.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj38.MT_pivotOut__.setValue('')
    self.obj38.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj38.MT_subtypeMatching__.setValue(('True', 0))
    self.obj38.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj38.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj38.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj38.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj38.MT_pivotIn__.setValue('')
    self.obj38.MT_pivotIn__.setNone()

    self.obj38.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(200.0,220.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=MT_pre__EClass(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # MT_label__
    self.obj39.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj39.MT_pivotOut__.setValue('')
    self.obj39.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj39.MT_subtypeMatching__.setValue(('True', 0))
    self.obj39.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj39.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj39.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj39.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj39.MT_pivotIn__.setValue('')
    self.obj39.MT_pivotIn__.setNone()

    self.obj39.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(480.0,160.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=MT_pre__EReference(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # MT_label__
    self.obj40.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj40.MT_pivotOut__.setValue('')
    self.obj40.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj40.MT_subtypeMatching__.setValue(('True', 0))
    self.obj40.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj40.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj40.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj40.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj40.MT_pivotIn__.setValue('')
    self.obj40.MT_pivotIn__.setNone()

    self.obj40.graphClass_= graph_MT_pre__EReference
    if self.genGraphics:
       new_obj = graph_MT_pre__EReference(360.0,120.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EReference", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=MT_pre__EReference(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # MT_label__
    self.obj41.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj41.MT_pivotOut__.setValue('')
    self.obj41.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj41.MT_subtypeMatching__.setValue(('True', 0))
    self.obj41.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj41.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj41.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj41.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj41.MT_pivotIn__.setValue('')
    self.obj41.MT_pivotIn__.setNone()

    self.obj41.graphClass_= graph_MT_pre__EReference
    if self.genGraphics:
       new_obj = graph_MT_pre__EReference(360.0,220.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EReference", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj47=MT_pre__directLink_S(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # MT_label__
    self.obj47.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj47.MT_pivotOut__.setValue('')
    self.obj47.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj47.MT_subtypeMatching__.setValue(('True', 0))
    self.obj47.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj47.MT_pivotIn__.setValue('')
    self.obj47.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj47.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eType"\n')
    self.obj47.MT_pre__associationType.setHeight(15)

    self.obj47.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,182.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=MT_pre__directLink_S(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # MT_label__
    self.obj48.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj48.MT_pivotOut__.setValue('')
    self.obj48.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj48.MT_subtypeMatching__.setValue(('True', 0))
    self.obj48.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj48.MT_pivotIn__.setValue('')
    self.obj48.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj48.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj48.MT_pre__associationType.setHeight(15)

    self.obj48.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,232.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=MT_pre__directLink_S(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # MT_label__
    self.obj49.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj49.MT_pivotOut__.setValue('')
    self.obj49.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj49.MT_subtypeMatching__.setValue(('True', 0))
    self.obj49.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj49.MT_pivotIn__.setValue('')
    self.obj49.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj49.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eType"\n')
    self.obj49.MT_pre__associationType.setHeight(15)

    self.obj49.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(340.0,262.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=MT_pre__directLink_S(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # MT_label__
    self.obj50.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj50.MT_pivotOut__.setValue('')
    self.obj50.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj50.MT_subtypeMatching__.setValue(('True', 0))
    self.obj50.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj50.MT_pivotIn__.setValue('')
    self.obj50.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj50.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj50.MT_pre__associationType.setHeight(15)

    self.obj50.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(340.0,212.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=LHS(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # constraint
    self.obj51.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj51.constraint.setHeight(15)

    self.obj51.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(160.0,60.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    # Connections for obj38 (graphObject_: Obj0) of type MT_pre__EClass
    self.drawConnections(
(self.obj38,self.obj50,[260.0, 262.0, 340.0, 212.0],"true", 2) )
    # Connections for obj39 (graphObject_: Obj1) of type MT_pre__EClass
    self.drawConnections(
(self.obj39,self.obj48,[540.0, 202.0, 490.0, 232.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj2) of type MT_pre__EReference
    self.drawConnections(
(self.obj40,self.obj47,[420.0, 162.0, 490.0, 182.0],"true", 2) )
    # Connections for obj41 (graphObject_: Obj3) of type MT_pre__EReference
    self.drawConnections(
(self.obj41,self.obj49,[420.0, 262.0, 340.0, 262.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj9) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj47,self.obj39,[490.0, 182.0, 540.0, 202.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj10) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj48,self.obj41,[490.0, 232.0, 420.0, 262.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj11) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj49,self.obj38,[340.0, 262.0, 260.0, 262.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj12) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj50,self.obj40,[340.0, 212.0, 420.0, 162.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj13) of type LHS
    self.drawConnections(
 )

newfunction = property1_connected_MDL

loadedMMName = ['MT_pre__ECoreMM_META', 'MoTifRule_META']

atom3version = '0.3'
