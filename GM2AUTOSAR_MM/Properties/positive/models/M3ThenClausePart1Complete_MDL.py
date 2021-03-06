"""
__M3ThenClausePart1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 09:20:04 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__directLink_T import *
from MT_pre__SwCompToEcuMapping_component import *
from MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SwCompToEcuMapping_component import *
from graph_MT_pre__directLink_T import *
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

def M3ThenClausePart1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M3ThenClausePart1Complete')
    # --- ASG attributes over ---


    self.obj4558=LHS(self)
    self.obj4558.isGraphObjectVisual = True

    if(hasattr(self.obj4558, '_setHierarchicalLink')):
      self.obj4558._setHierarchicalLink(False)

    # constraint
    self.obj4558.constraint.setValue('if PreNode(\'3\')[\'associationType\']==\'component\':\n    return True\nreturn False\n')
    self.obj4558.constraint.setHeight(15)

    self.obj4558.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj4558)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4558.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4558)
    self.globalAndLocalPostcondition(self.obj4558, rootNode)
    self.obj4558.postAction( rootNode.CREATE )

    self.obj4559=MT_pre__directLink_T(self)
    self.obj4559.isGraphObjectVisual = True

    if(hasattr(self.obj4559, '_setHierarchicalLink')):
      self.obj4559._setHierarchicalLink(False)

    # MT_label__
    self.obj4559.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj4559.MT_pivotOut__.setValue('')
    self.obj4559.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4559.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4559.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4559.MT_pivotIn__.setValue('')
    self.obj4559.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj4559.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4559.MT_pre__associationType.setHeight(15)

    self.obj4559.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(331.0,263.0,self.obj4559)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4559.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4559)
    self.globalAndLocalPostcondition(self.obj4559, rootNode)
    self.obj4559.postAction( rootNode.CREATE )

    self.obj4560=MT_pre__SwCompToEcuMapping_component(self)
    self.obj4560.isGraphObjectVisual = True

    if(hasattr(self.obj4560, '_setHierarchicalLink')):
      self.obj4560._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4560.MT_pivotOut__.setValue('')
    self.obj4560.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4560.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4560.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4560.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4560.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4560.MT_pivotIn__.setValue('')
    self.obj4560.MT_pivotIn__.setNone()

    # MT_label__
    self.obj4560.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj4560.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4560.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4560.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4560.MT_pre__name.setHeight(15)

    self.obj4560.graphClass_= graph_MT_pre__SwCompToEcuMapping_component
    if self.genGraphics:
       new_obj = graph_MT_pre__SwCompToEcuMapping_component(240.0,300.0,self.obj4560)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwCompToEcuMapping_component", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4560.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4560)
    self.globalAndLocalPostcondition(self.obj4560, rootNode)
    self.obj4560.postAction( rootNode.CREATE )

    self.obj4561=MT_pre__SwcToEcuMapping(self)
    self.obj4561.isGraphObjectVisual = True

    if(hasattr(self.obj4561, '_setHierarchicalLink')):
      self.obj4561._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4561.MT_pivotOut__.setValue('')
    self.obj4561.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4561.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4561.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4561.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4561.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4561.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj4561.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj4561.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4561.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4561.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4561.MT_pre__name.setHeight(15)

    self.obj4561.graphClass_= graph_MT_pre__SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SwcToEcuMapping(80.0,80.0,self.obj4561)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4561.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4561)
    self.globalAndLocalPostcondition(self.obj4561, rootNode)
    self.obj4561.postAction( rootNode.CREATE )

    # Connections for obj4558 (graphObject_: Obj13) of type LHS
    self.drawConnections(
 )
    # Connections for obj4559 (graphObject_: Obj14) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj4559,self.obj4560,[331.0, 263.0, 408.0, 373.0],"true", 2) )
    # Connections for obj4560 (graphObject_: Obj15) of type MT_pre__SwCompToEcuMapping_component
    self.drawConnections(
 )
    # Connections for obj4561 (graphObject_: Obj16) of type MT_pre__SwcToEcuMapping
    self.drawConnections(
(self.obj4561,self.obj4559,[254.0, 153.0, 331.0, 263.0],"true", 2) )

newfunction = M3ThenClausePart1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
