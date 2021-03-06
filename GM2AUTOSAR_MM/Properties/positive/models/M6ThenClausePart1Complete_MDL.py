"""
__M6ThenClausePart1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct 24 14:44:36 2013
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

def M6ThenClausePart1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M6ThenClausePart1Complete')
    # --- ASG attributes over ---


    self.obj14959=LHS(self)
    self.obj14959.isGraphObjectVisual = True

    if(hasattr(self.obj14959, '_setHierarchicalLink')):
      self.obj14959._setHierarchicalLink(False)

    # constraint
    self.obj14959.constraint.setValue('if PreNode(\'3\')[\'associationType\']==\'mapping\':\n    return True\nreturn False\n')
    self.obj14959.constraint.setHeight(15)

    self.obj14959.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,40.0,self.obj14959)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14959.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14959)
    self.globalAndLocalPostcondition(self.obj14959, rootNode)
    self.obj14959.postAction( rootNode.CREATE )

    self.obj14960=MT_pre__System(self)
    self.obj14960.isGraphObjectVisual = True

    if(hasattr(self.obj14960, '_setHierarchicalLink')):
      self.obj14960._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj14960.MT_pivotOut__.setValue('')
    self.obj14960.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj14960.MT_subtypeMatching__.setValue(('True', 0))
    self.obj14960.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj14960.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14960.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj14960.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj14960.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj14960.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14960.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj14960.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14960.MT_pre__name.setHeight(15)

    self.obj14960.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(140.0,80.0,self.obj14960)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14960.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14960)
    self.globalAndLocalPostcondition(self.obj14960, rootNode)
    self.obj14960.postAction( rootNode.CREATE )

    self.obj14961=MT_pre__SystemMapping(self)
    self.obj14961.isGraphObjectVisual = True

    if(hasattr(self.obj14961, '_setHierarchicalLink')):
      self.obj14961._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj14961.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj14961.MT_subtypeMatching__.setValue(('True', 0))
    self.obj14961.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj14961.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14961.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj14961.MT_pivotIn__.setValue('')
    self.obj14961.MT_pivotIn__.setNone()

    # MT_label__
    self.obj14961.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj14961.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14961.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj14961.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14961.MT_pre__name.setHeight(15)

    self.obj14961.graphClass_= graph_MT_pre__SystemMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SystemMapping(260.0,280.0,self.obj14961)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SystemMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj14961.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14961)
    self.globalAndLocalPostcondition(self.obj14961, rootNode)
    self.obj14961.postAction( rootNode.CREATE )

    self.obj14962=MT_pre__directLink_T(self)
    self.obj14962.isGraphObjectVisual = True

    if(hasattr(self.obj14962, '_setHierarchicalLink')):
      self.obj14962._setHierarchicalLink(False)

    # MT_label__
    self.obj14962.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj14962.MT_pivotOut__.setValue('')
    self.obj14962.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj14962.MT_subtypeMatching__.setValue(('True', 0))
    self.obj14962.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj14962.MT_pivotIn__.setValue('')
    self.obj14962.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj14962.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj14962.MT_pre__associationType.setHeight(15)

    self.obj14962.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(369.5,253.0,self.obj14962)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj14962.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj14962)
    self.globalAndLocalPostcondition(self.obj14962, rootNode)
    self.obj14962.postAction( rootNode.CREATE )

    # Connections for obj14959 (graphObject_: Obj20) of type LHS
    self.drawConnections(
 )
    # Connections for obj14960 (graphObject_: Obj21) of type MT_pre__System
    self.drawConnections(
(self.obj14960,self.obj14962,[308.0, 153.0, 369.5, 253.0],"true", 2) )
    # Connections for obj14961 (graphObject_: Obj22) of type MT_pre__SystemMapping
    self.drawConnections(
 )
    # Connections for obj14962 (graphObject_: Obj23) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj14962,self.obj14961,[369.5, 253.0, 431.0, 353.0],"true", 2) )

newfunction = M6ThenClausePart1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
