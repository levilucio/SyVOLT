"""
__LocalDef1orMoreDefPart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  2 14:57:51 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__LocalDef import *
from MT_pre__directLink_T import *
from MT_pre__Def import *
from graph_MT_pre__Def import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__LocalDef import *
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

def LocalDef1orMoreDefPart2_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('LocalDef1orMoreDefPart2_Complete')
    # --- ASG attributes over ---


    self.obj63227=LHS(self)
    self.obj63227.isGraphObjectVisual = True

    if(hasattr(self.obj63227, '_setHierarchicalLink')):
      self.obj63227._setHierarchicalLink(False)

    # constraint
    self.obj63227.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj63227.constraint.setHeight(15)

    self.obj63227.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,60.0,self.obj63227)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63227.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63227)
    self.globalAndLocalPostcondition(self.obj63227, rootNode)
    self.obj63227.postAction( rootNode.CREATE )

    self.obj63228=MT_pre__LocalDef(self)
    self.obj63228.isGraphObjectVisual = True

    if(hasattr(self.obj63228, '_setHierarchicalLink')):
      self.obj63228._setHierarchicalLink(False)

    # MT_label__
    self.obj63228.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj63228.MT_pivotOut__.setValue('')
    self.obj63228.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63228.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63228.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63228.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63228.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj63228.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63228.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63228.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63228.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj63228.MT_pivotIn__.setValue('element1')

    self.obj63228.graphClass_= graph_MT_pre__LocalDef
    if self.genGraphics:
       new_obj = graph_MT_pre__LocalDef(140.0,100.0,self.obj63228)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63228.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63228)
    self.globalAndLocalPostcondition(self.obj63228, rootNode)
    self.obj63228.postAction( rootNode.CREATE )

    self.obj73750=MT_pre__directLink_T(self)
    self.obj73750.isGraphObjectVisual = True

    if(hasattr(self.obj73750, '_setHierarchicalLink')):
      self.obj73750._setHierarchicalLink(False)

    # MT_label__
    self.obj73750.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj73750.MT_pivotOut__.setValue('')
    self.obj73750.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73750.MT_subtypeMatching__.setValue(('True', 0))
    self.obj73750.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj73750.MT_pivotIn__.setValue('')
    self.obj73750.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj73750.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73750.MT_pre__associationType.setHeight(15)

    self.obj73750.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(397.0,281.0,self.obj73750)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73750.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73750)
    self.globalAndLocalPostcondition(self.obj73750, rootNode)
    self.obj73750.postAction( rootNode.CREATE )

    self.obj73747=MT_pre__Def(self)
    self.obj73747.isGraphObjectVisual = True

    if(hasattr(self.obj73747, '_setHierarchicalLink')):
      self.obj73747._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73747.MT_pivotOut__.setValue('')
    self.obj73747.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73747.MT_subtypeMatching__.setValue(('True', 1))
    self.obj73747.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73747.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73747.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73747.MT_pivotIn__.setValue('')
    self.obj73747.MT_pivotIn__.setNone()

    # MT_label__
    self.obj73747.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj73747.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73747.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73747.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73747.MT_pre__name.setHeight(15)

    self.obj73747.graphClass_= graph_MT_pre__Def
    if self.genGraphics:
       new_obj = graph_MT_pre__Def(220.0,260.0,self.obj73747)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Def", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73747.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73747)
    self.globalAndLocalPostcondition(self.obj73747, rootNode)
    self.obj73747.postAction( rootNode.CREATE )

    # Connections for obj63227 (graphObject_: Obj8) of type LHS
    self.drawConnections(
 )
    # Connections for obj63228 (graphObject_: Obj9) of type MT_pre__LocalDef
    self.drawConnections(
(self.obj63228,self.obj73750,[357.0, 201.0, 397.0, 281.0],"true", 2) )
    # Connections for obj73750 (graphObject_: Obj11) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj73750,self.obj73747,[397.0, 281.0, 437.0, 361.0],"true", 2) )
    # Connections for obj73747 (graphObject_: Obj10) of type MT_pre__Def
    self.drawConnections(
 )

newfunction = LocalDef1orMoreDefPart2_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
