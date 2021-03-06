"""
__M4ThenClausePart2Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 17:23:01 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__EcuInstance import *
from MT_pre__directLink_T import *
from MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SwcToEcuMapping import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__EcuInstance import *
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

def M4ThenClausePart2Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M4ThenClausePart2Complete')
    # --- ASG attributes over ---


    self.obj24116=LHS(self)
    self.obj24116.isGraphObjectVisual = True

    if(hasattr(self.obj24116, '_setHierarchicalLink')):
      self.obj24116._setHierarchicalLink(False)

    # constraint
    self.obj24116.constraint.setValue('if PreNode(\'4\')[\'associationType\']==\'ecuInstance\' and PreNode(\'5\')[\'associationType\']==\'ecuInstance\':\n    return True\nreturn False\n')
    self.obj24116.constraint.setHeight(15)

    self.obj24116.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,60.0,self.obj24116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24116)
    self.globalAndLocalPostcondition(self.obj24116, rootNode)
    self.obj24116.postAction( rootNode.CREATE )

    self.obj24118=MT_pre__EcuInstance(self)
    self.obj24118.isGraphObjectVisual = True

    if(hasattr(self.obj24118, '_setHierarchicalLink')):
      self.obj24118._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj24118.MT_pivotOut__.setValue('')
    self.obj24118.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24118.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24118.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj24118.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24118.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj24118.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj24118.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj24118.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24118.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj24118.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24118.MT_pre__name.setHeight(15)

    self.obj24118.graphClass_= graph_MT_pre__EcuInstance
    if self.genGraphics:
       new_obj = graph_MT_pre__EcuInstance(320.0,180.0,self.obj24118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EcuInstance", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24118)
    self.globalAndLocalPostcondition(self.obj24118, rootNode)
    self.obj24118.postAction( rootNode.CREATE )

    self.obj24119=MT_pre__EcuInstance(self)
    self.obj24119.isGraphObjectVisual = True

    if(hasattr(self.obj24119, '_setHierarchicalLink')):
      self.obj24119._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj24119.MT_pivotOut__.setValue('')
    self.obj24119.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24119.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24119.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj24119.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24119.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj24119.MT_pivotIn__.setValue('')
    self.obj24119.MT_pivotIn__.setNone()

    # MT_label__
    self.obj24119.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj24119.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24119.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj24119.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24119.MT_pre__name.setHeight(15)

    self.obj24119.graphClass_= graph_MT_pre__EcuInstance
    if self.genGraphics:
       new_obj = graph_MT_pre__EcuInstance(120.0,300.0,self.obj24119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EcuInstance", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24119)
    self.globalAndLocalPostcondition(self.obj24119, rootNode)
    self.obj24119.postAction( rootNode.CREATE )

    self.obj24120=MT_pre__directLink_T(self)
    self.obj24120.isGraphObjectVisual = True

    if(hasattr(self.obj24120, '_setHierarchicalLink')):
      self.obj24120._setHierarchicalLink(False)

    # MT_label__
    self.obj24120.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj24120.MT_pivotOut__.setValue('')
    self.obj24120.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24120.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24120.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj24120.MT_pivotIn__.setValue('')
    self.obj24120.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj24120.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24120.MT_pre__associationType.setHeight(15)

    self.obj24120.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(381.0,203.0,self.obj24120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj24120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24120)
    self.globalAndLocalPostcondition(self.obj24120, rootNode)
    self.obj24120.postAction( rootNode.CREATE )

    self.obj24121=MT_pre__directLink_T(self)
    self.obj24121.isGraphObjectVisual = True

    if(hasattr(self.obj24121, '_setHierarchicalLink')):
      self.obj24121._setHierarchicalLink(False)

    # MT_label__
    self.obj24121.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj24121.MT_pivotOut__.setValue('')
    self.obj24121.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24121.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24121.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj24121.MT_pivotIn__.setValue('')
    self.obj24121.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj24121.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24121.MT_pre__associationType.setHeight(15)

    self.obj24121.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(281.0,263.0,self.obj24121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj24121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24121)
    self.globalAndLocalPostcondition(self.obj24121, rootNode)
    self.obj24121.postAction( rootNode.CREATE )

    self.obj24117=MT_pre__SwcToEcuMapping(self)
    self.obj24117.isGraphObjectVisual = True

    if(hasattr(self.obj24117, '_setHierarchicalLink')):
      self.obj24117._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj24117.MT_pivotOut__.setValue('')
    self.obj24117.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj24117.MT_subtypeMatching__.setValue(('True', 0))
    self.obj24117.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj24117.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24117.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj24117.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj24117.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj24117.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24117.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj24117.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj24117.MT_pre__name.setHeight(15)

    self.obj24117.graphClass_= graph_MT_pre__SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SwcToEcuMapping(100.0,80.0,self.obj24117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24117)
    self.globalAndLocalPostcondition(self.obj24117, rootNode)
    self.obj24117.postAction( rootNode.CREATE )

    # Connections for obj24116 (graphObject_: Obj98) of type LHS
    self.drawConnections(
 )
    # Connections for obj24118 (graphObject_: Obj100) of type MT_pre__EcuInstance
    self.drawConnections(
 )
    # Connections for obj24119 (graphObject_: Obj101) of type MT_pre__EcuInstance
    self.drawConnections(
 )
    # Connections for obj24120 (graphObject_: Obj102) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj24120,self.obj24118,[381.0, 203.0, 488.0, 253.0],"true", 2) )
    # Connections for obj24121 (graphObject_: Obj103) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj24121,self.obj24119,[281.0, 263.0, 288.0, 373.0],"true", 2) )
    # Connections for obj24117 (graphObject_: Obj99) of type MT_pre__SwcToEcuMapping
    self.drawConnections(
(self.obj24117,self.obj24120,[274.0, 153.0, 381.0, 203.0],"true", 2),
(self.obj24117,self.obj24121,[274.0, 153.0, 281.0, 263.0],"true", 2) )

newfunction = M4ThenClausePart2Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
