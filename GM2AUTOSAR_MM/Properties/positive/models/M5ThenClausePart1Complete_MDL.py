"""
__M5ThenClausePart1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct 24 14:27:27 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__SoftwareComposition import *
from MT_pre__System import *
from MT_pre__directLink_T import *
from graph_MT_pre__System import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__SoftwareComposition import *
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

def M5ThenClausePart1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M5ThenClausePart1Complete')
    # --- ASG attributes over ---


    self.obj10450=LHS(self)
    self.obj10450.isGraphObjectVisual = True

    if(hasattr(self.obj10450, '_setHierarchicalLink')):
      self.obj10450._setHierarchicalLink(False)

    # constraint
    self.obj10450.constraint.setValue('if PreNode(\'3\')[\'associationType\']==\'softwareComposition\':\n    return True\nreturn False\n')
    self.obj10450.constraint.setHeight(15)

    self.obj10450.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,40.0,self.obj10450)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10450.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10450)
    self.globalAndLocalPostcondition(self.obj10450, rootNode)
    self.obj10450.postAction( rootNode.CREATE )

    self.obj10452=MT_pre__SoftwareComposition(self)
    self.obj10452.isGraphObjectVisual = True

    if(hasattr(self.obj10452, '_setHierarchicalLink')):
      self.obj10452._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10452.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj10452.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10452.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10452.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10452.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10452.MT_pivotIn__.setValue('')
    self.obj10452.MT_pivotIn__.setNone()

    # MT_label__
    self.obj10452.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj10452.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10452.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10452.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10452.MT_pre__name.setHeight(15)

    self.obj10452.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(140.0,240.0,self.obj10452)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10452.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10452)
    self.globalAndLocalPostcondition(self.obj10452, rootNode)
    self.obj10452.postAction( rootNode.CREATE )

    self.obj10451=MT_pre__System(self)
    self.obj10451.isGraphObjectVisual = True

    if(hasattr(self.obj10451, '_setHierarchicalLink')):
      self.obj10451._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj10451.MT_pivotOut__.setValue('')
    self.obj10451.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10451.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10451.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj10451.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10451.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj10451.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj10451.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj10451.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10451.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj10451.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10451.MT_pre__name.setHeight(15)

    self.obj10451.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(80.0,60.0,self.obj10451)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10451.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10451)
    self.globalAndLocalPostcondition(self.obj10451, rootNode)
    self.obj10451.postAction( rootNode.CREATE )

    self.obj10453=MT_pre__directLink_T(self)
    self.obj10453.isGraphObjectVisual = True

    if(hasattr(self.obj10453, '_setHierarchicalLink')):
      self.obj10453._setHierarchicalLink(False)

    # MT_label__
    self.obj10453.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj10453.MT_pivotOut__.setValue('')
    self.obj10453.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10453.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10453.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10453.MT_pivotIn__.setValue('')
    self.obj10453.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj10453.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj10453.MT_pre__associationType.setHeight(15)

    self.obj10453.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(285.0,223.0,self.obj10453)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10453.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10453)
    self.globalAndLocalPostcondition(self.obj10453, rootNode)
    self.obj10453.postAction( rootNode.CREATE )

    # Connections for obj10450 (graphObject_: Obj8) of type LHS
    self.drawConnections(
 )
    # Connections for obj10452 (graphObject_: Obj10) of type MT_pre__SoftwareComposition
    self.drawConnections(
 )
    # Connections for obj10451 (graphObject_: Obj9) of type MT_pre__System
    self.drawConnections(
(self.obj10451,self.obj10453,[248.0, 133.0, 285.0, 223.0],"true", 2) )
    # Connections for obj10453 (graphObject_: Obj11) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj10453,self.obj10452,[285.0, 223.0, 322.0, 313.0],"true", 2) )

newfunction = M5ThenClausePart1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
