"""
__ECUSysTrivialTrueComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Sep  9 21:32:17 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__trace_link import *
from MT_pre__System import *
from MT_pre__ECU import *
from LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__System import *
from graph_MT_pre__ECU import *
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

def ECUSysTrivialTrueComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__GM2AUTOSAR_MM ---
    if( MT_pre__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_pre__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_pre__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_pre__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_pre__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ECUSysTrivialTrueComplete')
    # --- ASG attributes over ---


    self.obj14368=MT_pre__trace_link(self)
    self.obj14368.isGraphObjectVisual = True

    if(hasattr(self.obj14368, '_setHierarchicalLink')):
      self.obj14368._setHierarchicalLink(False)

    # MT_label__
    self.obj14368.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj14368.MT_pivotOut__.setValue('')
    self.obj14368.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj14368.MT_subtypeMatching__.setValue(('True', 0))
    self.obj14368.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj14368.MT_pivotIn__.setValue('')
    self.obj14368.MT_pivotIn__.setNone()

    self.obj14368.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(349.0,273.5,self.obj14368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj14368.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14368)
    self.globalAndLocalPostcondition(self.obj14368, rootNode)
    self.obj14368.postAction( rootNode.CREATE )

    self.obj14365=MT_pre__System(self)
    self.obj14365.isGraphObjectVisual = True

    if(hasattr(self.obj14365, '_setHierarchicalLink')):
      self.obj14365._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj14365.MT_pivotOut__.setValue('')
    self.obj14365.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj14365.MT_subtypeMatching__.setValue(('True', 0))
    self.obj14365.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj14365.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14365.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj14365.MT_pivotIn__.setValue('')
    self.obj14365.MT_pivotIn__.setNone()

    # MT_label__
    self.obj14365.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj14365.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14365.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj14365.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14365.MT_pre__name.setHeight(15)

    self.obj14365.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(180.0,300.0,self.obj14365)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14365.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14365)
    self.globalAndLocalPostcondition(self.obj14365, rootNode)
    self.obj14365.postAction( rootNode.CREATE )

    self.obj14364=MT_pre__ECU(self)
    self.obj14364.isGraphObjectVisual = True

    if(hasattr(self.obj14364, '_setHierarchicalLink')):
      self.obj14364._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj14364.MT_pivotOut__.setValue('')
    self.obj14364.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj14364.MT_subtypeMatching__.setValue(('True', 0))
    self.obj14364.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj14364.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14364.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj14364.MT_pivotIn__.setValue('')
    self.obj14364.MT_pivotIn__.setNone()

    # MT_label__
    self.obj14364.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj14364.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14364.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj14364.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14364.MT_pre__name.setHeight(15)

    self.obj14364.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(180.0,100.0,self.obj14364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14364.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14364)
    self.globalAndLocalPostcondition(self.obj14364, rootNode)
    self.obj14364.postAction( rootNode.CREATE )

    self.obj14360=LHS(self)
    self.obj14360.isGraphObjectVisual = True

    if(hasattr(self.obj14360, '_setHierarchicalLink')):
      self.obj14360._setHierarchicalLink(False)

    # constraint
    self.obj14360.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj14360.constraint.setHeight(15)

    self.obj14360.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,60.0,self.obj14360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14360.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14360)
    self.globalAndLocalPostcondition(self.obj14360, rootNode)
    self.obj14360.postAction( rootNode.CREATE )

    # Connections for obj14368 (graphObject_: Obj134) of type MT_pre__trace_link
    self.drawConnections(
(self.obj14368,self.obj14364,[349.0, 273.5, 350.0, 174.0],"true", 2) )
    # Connections for obj14365 (graphObject_: Obj133) of type MT_pre__System
    self.drawConnections(
(self.obj14365,self.obj14368,[348.0, 373.0, 349.0, 273.5],"true", 2) )
    # Connections for obj14364 (graphObject_: Obj132) of type MT_pre__ECU
    self.drawConnections(
 )
    # Connections for obj14360 (graphObject_: Obj130) of type LHS
    self.drawConnections(
 )

newfunction = ECUSysTrivialTrueComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
