"""
__M6ThenClausePart2Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct 24 14:51:32 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__System import *
from MT_pre__SystemMapping import *
from MT_pre__directLink_T import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__System import *
from graph_MT_pre__SystemMapping import *
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

def M6ThenClausePart2Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M6ThenClausePart2Complete')
    # --- ASG attributes over ---


    self.obj16467=LHS(self)
    self.obj16467.isGraphObjectVisual = True

    if(hasattr(self.obj16467, '_setHierarchicalLink')):
      self.obj16467._setHierarchicalLink(False)

    # constraint
    self.obj16467.constraint.setValue('if PreNode(\'4\')[\'associationType\']==\'mapping\' and PreNode(\'5\')[\'associationType\']==\'mapping\':\n    return True\nreturn False\n')
    self.obj16467.constraint.setHeight(15)

    self.obj16467.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,40.0,self.obj16467)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj16467.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16467)
    self.globalAndLocalPostcondition(self.obj16467, rootNode)
    self.obj16467.postAction( rootNode.CREATE )

    self.obj16468=MT_pre__System(self)
    self.obj16468.isGraphObjectVisual = True

    if(hasattr(self.obj16468, '_setHierarchicalLink')):
      self.obj16468._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj16468.MT_pivotOut__.setValue('')
    self.obj16468.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj16468.MT_subtypeMatching__.setValue(('True', 0))
    self.obj16468.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj16468.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16468.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj16468.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj16468.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj16468.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16468.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj16468.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16468.MT_pre__name.setHeight(15)

    self.obj16468.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(100.0,60.0,self.obj16468)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj16468.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16468)
    self.globalAndLocalPostcondition(self.obj16468, rootNode)
    self.obj16468.postAction( rootNode.CREATE )

    self.obj16469=MT_pre__SystemMapping(self)
    self.obj16469.isGraphObjectVisual = True

    if(hasattr(self.obj16469, '_setHierarchicalLink')):
      self.obj16469._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj16469.MT_pivotOut__.setValue('')
    self.obj16469.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj16469.MT_subtypeMatching__.setValue(('True', 0))
    self.obj16469.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj16469.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16469.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj16469.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj16469.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj16469.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16469.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj16469.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16469.MT_pre__name.setHeight(15)

    self.obj16469.graphClass_= graph_MT_pre__SystemMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SystemMapping(340.0,180.0,self.obj16469)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SystemMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj16469.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16469)
    self.globalAndLocalPostcondition(self.obj16469, rootNode)
    self.obj16469.postAction( rootNode.CREATE )

    self.obj16470=MT_pre__SystemMapping(self)
    self.obj16470.isGraphObjectVisual = True

    if(hasattr(self.obj16470, '_setHierarchicalLink')):
      self.obj16470._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj16470.MT_pivotOut__.setValue('')
    self.obj16470.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj16470.MT_subtypeMatching__.setValue(('True', 0))
    self.obj16470.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj16470.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16470.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj16470.MT_pivotIn__.setValue('')
    self.obj16470.MT_pivotIn__.setNone()

    # MT_label__
    self.obj16470.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj16470.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16470.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj16470.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16470.MT_pre__name.setHeight(15)

    self.obj16470.graphClass_= graph_MT_pre__SystemMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SystemMapping(120.0,300.0,self.obj16470)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SystemMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj16470.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16470)
    self.globalAndLocalPostcondition(self.obj16470, rootNode)
    self.obj16470.postAction( rootNode.CREATE )

    self.obj16471=MT_pre__directLink_T(self)
    self.obj16471.isGraphObjectVisual = True

    if(hasattr(self.obj16471, '_setHierarchicalLink')):
      self.obj16471._setHierarchicalLink(False)

    # MT_label__
    self.obj16471.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj16471.MT_pivotOut__.setValue('')
    self.obj16471.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj16471.MT_subtypeMatching__.setValue(('True', 0))
    self.obj16471.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj16471.MT_pivotIn__.setValue('')
    self.obj16471.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj16471.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16471.MT_pre__associationType.setHeight(15)

    self.obj16471.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(389.5,193.0,self.obj16471)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj16471.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16471)
    self.globalAndLocalPostcondition(self.obj16471, rootNode)
    self.obj16471.postAction( rootNode.CREATE )

    self.obj16472=MT_pre__directLink_T(self)
    self.obj16472.isGraphObjectVisual = True

    if(hasattr(self.obj16472, '_setHierarchicalLink')):
      self.obj16472._setHierarchicalLink(False)

    # MT_label__
    self.obj16472.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj16472.MT_pivotOut__.setValue('')
    self.obj16472.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj16472.MT_subtypeMatching__.setValue(('True', 0))
    self.obj16472.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj16472.MT_pivotIn__.setValue('')
    self.obj16472.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj16472.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj16472.MT_pre__associationType.setHeight(15)

    self.obj16472.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(279.5,253.0,self.obj16472)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj16472.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16472)
    self.globalAndLocalPostcondition(self.obj16472, rootNode)
    self.obj16472.postAction( rootNode.CREATE )

    # Connections for obj16467 (graphObject_: Obj24) of type LHS
    self.drawConnections(
 )
    # Connections for obj16468 (graphObject_: Obj25) of type MT_pre__System
    self.drawConnections(
(self.obj16468,self.obj16471,[268.0, 133.0, 389.5, 193.0],"true", 2),
(self.obj16468,self.obj16472,[268.0, 133.0, 279.5, 253.0],"true", 2) )
    # Connections for obj16469 (graphObject_: Obj26) of type MT_pre__SystemMapping
    self.drawConnections(
 )
    # Connections for obj16470 (graphObject_: Obj27) of type MT_pre__SystemMapping
    self.drawConnections(
 )
    # Connections for obj16471 (graphObject_: Obj28) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj16471,self.obj16469,[389.5, 193.0, 511.0, 253.0],"true", 2) )
    # Connections for obj16472 (graphObject_: Obj29) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj16472,self.obj16470,[279.5, 253.0, 291.0, 373.0],"true", 2) )

newfunction = M6ThenClausePart2Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
