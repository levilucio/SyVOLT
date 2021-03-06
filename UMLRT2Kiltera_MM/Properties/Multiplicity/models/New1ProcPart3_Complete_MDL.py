"""
__New1ProcPart3_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Mar  5 01:20:56 2015
____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__New import *
from MT_pre__directLink_T import *
from MT_pre__Proc import *
from LHS import *
from graph_MT_pre__New import *
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

def New1ProcPart3_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('New1ProcPart3_Complete')
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


    self.obj105330=MT_pre__New(self)
    self.obj105330.isGraphObjectVisual = True

    if(hasattr(self.obj105330, '_setHierarchicalLink')):
      self.obj105330._setHierarchicalLink(False)

    # MT_label__
    self.obj105330.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj105330.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj105330.MT_subtypeMatching__.setValue(('True', 0))
    self.obj105330.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj105330.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj105330.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj105330.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj105330.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj105330.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj105330.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj105330.MT_pivotIn__.setValue('element1')

    self.obj105330.graphClass_= graph_MT_pre__New
    if self.genGraphics:
       new_obj = graph_MT_pre__New(40.0,40.0,self.obj105330)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__New", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105330.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105330)
    self.globalAndLocalPostcondition(self.obj105330, rootNode)
    self.obj105330.postAction( rootNode.CREATE )

    self.obj115844=MT_pre__directLink_T(self)
    self.obj115844.isGraphObjectVisual = True

    if(hasattr(self.obj115844, '_setHierarchicalLink')):
      self.obj115844._setHierarchicalLink(False)

    # MT_label__
    self.obj115844.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj115844.MT_pivotOut__.setValue('')
    self.obj115844.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj115844.MT_subtypeMatching__.setValue(('True', 0))
    self.obj115844.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj115844.MT_pivotIn__.setValue('')
    self.obj115844.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj115844.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj115844.MT_pre__associationType.setHeight(15)

    self.obj115844.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(257.0,231.0,self.obj115844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj115844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115844)
    self.globalAndLocalPostcondition(self.obj115844, rootNode)
    self.obj115844.postAction( rootNode.CREATE )

    self.obj126370=MT_pre__directLink_T(self)
    self.obj126370.isGraphObjectVisual = True

    if(hasattr(self.obj126370, '_setHierarchicalLink')):
      self.obj126370._setHierarchicalLink(False)

    # MT_label__
    self.obj126370.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj126370.MT_pivotOut__.setValue('')
    self.obj126370.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj126370.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126370.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj126370.MT_pivotIn__.setValue('')
    self.obj126370.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj126370.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126370.MT_pre__associationType.setHeight(15)

    self.obj126370.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(347.0,191.0,self.obj126370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126370.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126370)
    self.globalAndLocalPostcondition(self.obj126370, rootNode)
    self.obj126370.postAction( rootNode.CREATE )

    self.obj115843=MT_pre__Proc(self)
    self.obj115843.isGraphObjectVisual = True

    if(hasattr(self.obj115843, '_setHierarchicalLink')):
      self.obj115843._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj115843.MT_pivotOut__.setValue('')
    self.obj115843.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj115843.MT_subtypeMatching__.setValue(('True', 1))
    self.obj115843.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj115843.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj115843.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj115843.MT_pivotIn__.setValue('')
    self.obj115843.MT_pivotIn__.setNone()

    # MT_label__
    self.obj115843.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj115843.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj115843.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj115843.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj115843.MT_pre__name.setHeight(15)

    self.obj115843.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(40.0,220.0,self.obj115843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115843)
    self.globalAndLocalPostcondition(self.obj115843, rootNode)
    self.obj115843.postAction( rootNode.CREATE )

    self.obj126367=MT_pre__Proc(self)
    self.obj126367.isGraphObjectVisual = True

    if(hasattr(self.obj126367, '_setHierarchicalLink')):
      self.obj126367._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj126367.MT_pivotOut__.setValue('')
    self.obj126367.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj126367.MT_subtypeMatching__.setValue(('True', 1))
    self.obj126367.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj126367.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126367.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj126367.MT_pivotIn__.setValue('')
    self.obj126367.MT_pivotIn__.setNone()

    # MT_label__
    self.obj126367.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj126367.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126367.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj126367.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126367.MT_pre__name.setHeight(15)

    self.obj126367.graphClass_= graph_MT_pre__Proc
    if self.genGraphics:
       new_obj = graph_MT_pre__Proc(220.0,140.0,self.obj126367)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Proc", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126367.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126367)
    self.globalAndLocalPostcondition(self.obj126367, rootNode)
    self.obj126367.postAction( rootNode.CREATE )

    self.obj105329=LHS(self)
    self.obj105329.isGraphObjectVisual = True

    if(hasattr(self.obj105329, '_setHierarchicalLink')):
      self.obj105329._setHierarchicalLink(False)

    # constraint
    self.obj105329.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj105329.constraint.setHeight(15)

    self.obj105329.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj105329)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105329.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105329)
    self.globalAndLocalPostcondition(self.obj105329, rootNode)
    self.obj105329.postAction( rootNode.CREATE )

    # Connections for obj105330 (graphObject_: Obj19) of type MT_pre__New
    self.drawConnections(
(self.obj105330,self.obj115844,[257.0, 141.0, 257.0, 231.0],"true", 2),
(self.obj105330,self.obj126370,[257.0, 141.0, 347.0, 191.0],"true", 2) )
    # Connections for obj115844 (graphObject_: Obj21) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj115844,self.obj115843,[257.0, 231.0, 257.0, 321.0],"true", 2) )
    # Connections for obj126370 (graphObject_: Obj23) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj126370,self.obj126367,[347.0, 191.0, 437.0, 241.0],"true", 2) )
    # Connections for obj115843 (graphObject_: Obj20) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj126367 (graphObject_: Obj22) of type MT_pre__Proc
    self.drawConnections(
 )
    # Connections for obj105329 (graphObject_: Obj18) of type LHS
    self.drawConnections(
 )

newfunction = New1ProcPart3_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
