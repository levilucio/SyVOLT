"""
__state2funcdefNEG_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 13:38:32 2015
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__FuncDef import *
from MT_pre__trace_link import *
from graph_MT_pre__State import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__FuncDef import *
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

def state2funcdefNEG_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('state2funcdefNEG_Complete')
    # --- ASG attributes over ---


    self.obj21143=LHS(self)
    self.obj21143.isGraphObjectVisual = True

    if(hasattr(self.obj21143, '_setHierarchicalLink')):
      self.obj21143._setHierarchicalLink(False)

    # constraint
    self.obj21143.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj21143.constraint.setHeight(15)

    self.obj21143.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,100.0,self.obj21143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21143)
    self.globalAndLocalPostcondition(self.obj21143, rootNode)
    self.obj21143.postAction( rootNode.CREATE )

    self.obj21144=MT_pre__State(self)
    self.obj21144.isGraphObjectVisual = True

    if(hasattr(self.obj21144, '_setHierarchicalLink')):
      self.obj21144._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21144.MT_pivotOut__.setValue('')
    self.obj21144.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21144.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21144.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21144.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21144.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21144.MT_pivotIn__.setValue('')
    self.obj21144.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21144.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj21144.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21144.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21144.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21144.MT_pre__name.setHeight(15)

    self.obj21144.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(120.0,140.0,self.obj21144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21144)
    self.globalAndLocalPostcondition(self.obj21144, rootNode)
    self.obj21144.postAction( rootNode.CREATE )

    self.obj21145=MT_pre__FuncDef(self)
    self.obj21145.isGraphObjectVisual = True

    if(hasattr(self.obj21145, '_setHierarchicalLink')):
      self.obj21145._setHierarchicalLink(False)

    # MT_label__
    self.obj21145.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj21145.MT_pivotOut__.setValue('')
    self.obj21145.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21145.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21145.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21145.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21145.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21145.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21145.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21145.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21145.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21145.MT_pivotIn__.setValue('')
    self.obj21145.MT_pivotIn__.setNone()

    self.obj21145.graphClass_= graph_MT_pre__FuncDef
    if self.genGraphics:
       new_obj = graph_MT_pre__FuncDef(140.0,300.0,self.obj21145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__FuncDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21145)
    self.globalAndLocalPostcondition(self.obj21145, rootNode)
    self.obj21145.postAction( rootNode.CREATE )

    self.obj21146=MT_pre__trace_link(self)
    self.obj21146.isGraphObjectVisual = True

    if(hasattr(self.obj21146, '_setHierarchicalLink')):
      self.obj21146._setHierarchicalLink(False)

    # MT_label__
    self.obj21146.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj21146.MT_pivotOut__.setValue('')
    self.obj21146.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21146.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21146.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21146.MT_pivotIn__.setValue('')
    self.obj21146.MT_pivotIn__.setNone()

    self.obj21146.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(337.0,308.0,self.obj21146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21146)
    self.globalAndLocalPostcondition(self.obj21146, rootNode)
    self.obj21146.postAction( rootNode.CREATE )

    # Connections for obj21143 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )
    # Connections for obj21144 (graphObject_: Obj5) of type MT_pre__State
    self.drawConnections(
 )
    # Connections for obj21145 (graphObject_: Obj6) of type MT_pre__FuncDef
    self.drawConnections(
(self.obj21145,self.obj21146,[357.0, 401.0, 337.0, 308.0],"true", 2) )
    # Connections for obj21146 (graphObject_: Obj7) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21146,self.obj21144,[337.0, 308.0, 317.0, 215.0],"true", 2) )

newfunction = state2funcdefNEG_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
