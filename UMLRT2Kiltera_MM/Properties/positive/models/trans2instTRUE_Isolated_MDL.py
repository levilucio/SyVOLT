"""
__trans2instTRUE_Isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Tue Feb 17 16:20:26 2015
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__SIBLING0 import *
from MT_pre__Transition import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__State import *
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

def trans2instTRUE_Isolated_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('trans2instTRUE_Isolated')
    # --- ASG attributes over ---


    self.obj42180=LHS(self)
    self.obj42180.isGraphObjectVisual = True

    if(hasattr(self.obj42180, '_setHierarchicalLink')):
      self.obj42180._setHierarchicalLink(False)

    # constraint
    self.obj42180.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj42180.constraint.setHeight(15)

    self.obj42180.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,40.0,self.obj42180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42180)
    self.globalAndLocalPostcondition(self.obj42180, rootNode)
    self.obj42180.postAction( rootNode.CREATE )

    self.obj42181=MT_pre__State(self)
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

    self.obj42181.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(40.0,80.0,self.obj42181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42181)
    self.globalAndLocalPostcondition(self.obj42181, rootNode)
    self.obj42181.postAction( rootNode.CREATE )

    self.obj42187=MT_pre__SIBLING0(self)
    self.obj42187.isGraphObjectVisual = True

    if(hasattr(self.obj42187, '_setHierarchicalLink')):
      self.obj42187._setHierarchicalLink(False)

    # MT_label__
    self.obj42187.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj42187.MT_pivotOut__.setValue('')
    self.obj42187.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42187.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42187.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42187.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42187.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj42187.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42187.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42187.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42187.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj42187.MT_pivotIn__.setValue('')
    self.obj42187.MT_pivotIn__.setNone()

    self.obj42187.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(240.0,140.0,self.obj42187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42187)
    self.globalAndLocalPostcondition(self.obj42187, rootNode)
    self.obj42187.postAction( rootNode.CREATE )

    self.obj42186=MT_pre__Transition(self)
    self.obj42186.isGraphObjectVisual = True

    if(hasattr(self.obj42186, '_setHierarchicalLink')):
      self.obj42186._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42186.MT_pivotOut__.setValue('')
    self.obj42186.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42186.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42186.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42186.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42186.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42186.MT_pivotIn__.setValue('')
    self.obj42186.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42186.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj42186.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42186.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42186.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42186.MT_pre__name.setHeight(15)

    self.obj42186.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(100.0,260.0,self.obj42186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42186)
    self.globalAndLocalPostcondition(self.obj42186, rootNode)
    self.obj42186.postAction( rootNode.CREATE )

    # Connections for obj42180 (graphObject_: Obj17) of type LHS
    self.drawConnections(
 )
    # Connections for obj42181 (graphObject_: Obj18) of type MT_pre__State
    self.drawConnections(
 )
    # Connections for obj42187 (graphObject_: Obj24) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj42186 (graphObject_: Obj23) of type MT_pre__Transition
    self.drawConnections(
 )

newfunction = trans2instTRUE_Isolated_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
