"""
__property2_isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Wed May  6 15:37:29 2015
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__EClass import *
from MT_pre__EStructuralFeature import *
from LHS import *
from graph_MT_pre__EStructuralFeature import *
from graph_MT_pre__EClass import *
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

def property2_isolated_MDL(self, rootNode, MT_pre__ECoreMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('property2_isolated')
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

    self.obj43=LHS(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # constraint
    self.obj43.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj43.constraint.setHeight(15)

    self.obj43.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(240.0,80.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    # Connections for obj38 (graphObject_: Obj0) of type MT_pre__EClass
    self.drawConnections(
 )
    # Connections for obj39 (graphObject_: Obj1) of type MT_pre__EStructuralFeature
    self.drawConnections(
 )
    # Connections for obj43 (graphObject_: Obj5) of type LHS
    self.drawConnections(
 )

newfunction = property2_isolated_MDL

loadedMMName = ['MT_pre__ECoreMM_META', 'MoTifRule_META']

atom3version = '0.3'
