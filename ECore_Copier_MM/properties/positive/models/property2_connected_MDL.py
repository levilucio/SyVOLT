"""
__property2_connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Wed May  6 15:00:18 2015
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__EClass import *
from MT_pre__EStructuralFeature import *
from MT_pre__MatchModel import *
from MT_pre__match_contains import *
from MT_pre__directLink_S import *
from LHS import *
from graph_LHS import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_MT_pre__EStructuralFeature import *
from graph_MT_pre__EClass import *
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

def property2_connected_MDL(self, rootNode, MT_pre__ECoreMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('property2_connected')
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
       new_obj = graph_MT_pre__EClass(340.0,180.0,self.obj38)
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

    self.obj39=MT_pre__EStructuralFeature(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # MT_label__
    self.obj39.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj39.MT_pivotOut__.setValue('')
    self.obj39.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj39.MT_subtypeMatching__.setValue(('True', 1))
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

    self.obj39.graphClass_= graph_MT_pre__EStructuralFeature
    if self.genGraphics:
       new_obj = graph_MT_pre__EStructuralFeature(500.0,180.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EStructuralFeature", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=MT_pre__MatchModel(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # MT_label__
    self.obj40.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj40.MT_pivotOut__.setValue('')
    self.obj40.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj40.MT_subtypeMatching__.setValue(('True', 0))
    self.obj40.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj40.MT_pivotIn__.setValue('')
    self.obj40.MT_pivotIn__.setNone()

    self.obj40.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(180.0,120.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.04
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=MT_pre__match_contains(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # MT_label__
    self.obj41.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj41.MT_pivotOut__.setValue('')
    self.obj41.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj41.MT_subtypeMatching__.setValue(('True', 0))
    self.obj41.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj41.MT_pivotIn__.setValue('')
    self.obj41.MT_pivotIn__.setNone()

    self.obj41.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(330.5,191.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=MT_pre__match_contains(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # MT_label__
    self.obj42.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj42.MT_pivotOut__.setValue('')
    self.obj42.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj42.MT_pivotIn__.setValue('')
    self.obj42.MT_pivotIn__.setNone()

    self.obj42.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(420.5,191.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=MT_pre__directLink_S(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # MT_label__
    self.obj43.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj43.MT_pivotOut__.setValue('')
    self.obj43.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj43.MT_subtypeMatching__.setValue(('True', 0))
    self.obj43.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj43.MT_pivotIn__.setValue('')
    self.obj43.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj43.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj43.MT_pre__associationType.setHeight(15)

    self.obj43.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(480.0,222.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=LHS(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # constraint
    self.obj44.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj44.constraint.setHeight(15)

    self.obj44.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(180.0,60.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    # Connections for obj38 (graphObject_: Obj0) of type MT_pre__EClass
    self.drawConnections(
(self.obj38,self.obj43,[400.0, 222.0, 480.0, 222.0],"true", 2) )
    # Connections for obj39 (graphObject_: Obj1) of type MT_pre__EStructuralFeature
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj2) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj40,self.obj41,[261.0, 161.0, 330.5, 191.5],"true", 2),
(self.obj40,self.obj42,[261.0, 161.0, 420.5, 191.5],"true", 2) )
    # Connections for obj41 (graphObject_: Obj3) of type MT_pre__match_contains
    self.drawConnections(
(self.obj41,self.obj38,[330.5, 191.5, 400.0, 222.0],"true", 2) )
    # Connections for obj42 (graphObject_: Obj4) of type MT_pre__match_contains
    self.drawConnections(
(self.obj42,self.obj39,[420.5, 191.5, 560.0, 222.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj5) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj43,self.obj39,[480.0, 222.0, 560.0, 222.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )

newfunction = property2_connected_MDL

loadedMMName = ['MT_pre__ECoreMM_META', 'MoTifRule_META']

atom3version = '0.3'
