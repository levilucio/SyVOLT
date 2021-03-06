"""
__M5ThenClausePart2Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct 24 14:34:45 2013
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

def M5ThenClausePart2Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M5ThenClausePart2Complete')
    # --- ASG attributes over ---


    self.obj11952=LHS(self)
    self.obj11952.isGraphObjectVisual = True

    if(hasattr(self.obj11952, '_setHierarchicalLink')):
      self.obj11952._setHierarchicalLink(False)

    # constraint
    self.obj11952.constraint.setValue('if PreNode(\'4\')[\'associationType\']==\'softwareComposition\' and PreNode(\'5\')[\'associationType\']==\'softwareComposition\':\n    return True\nreturn False\n')
    self.obj11952.constraint.setHeight(15)

    self.obj11952.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(160.0,100.0,self.obj11952)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj11952.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj11952)
    self.globalAndLocalPostcondition(self.obj11952, rootNode)
    self.obj11952.postAction( rootNode.CREATE )

    self.obj11954=MT_pre__SoftwareComposition(self)
    self.obj11954.isGraphObjectVisual = True

    if(hasattr(self.obj11954, '_setHierarchicalLink')):
      self.obj11954._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj11954.MT_pivotOut__.setValue('')
    self.obj11954.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj11954.MT_subtypeMatching__.setValue(('True', 0))
    self.obj11954.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj11954.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11954.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj11954.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj11954.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj11954.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11954.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj11954.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11954.MT_pre__name.setHeight(15)

    self.obj11954.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(380.0,240.0,self.obj11954)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj11954.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj11954)
    self.globalAndLocalPostcondition(self.obj11954, rootNode)
    self.obj11954.postAction( rootNode.CREATE )

    self.obj11955=MT_pre__SoftwareComposition(self)
    self.obj11955.isGraphObjectVisual = True

    if(hasattr(self.obj11955, '_setHierarchicalLink')):
      self.obj11955._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj11955.MT_pivotOut__.setValue('')
    self.obj11955.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj11955.MT_subtypeMatching__.setValue(('True', 0))
    self.obj11955.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj11955.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11955.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj11955.MT_pivotIn__.setValue('')
    self.obj11955.MT_pivotIn__.setNone()

    # MT_label__
    self.obj11955.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj11955.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11955.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj11955.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11955.MT_pre__name.setHeight(15)

    self.obj11955.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(180.0,360.0,self.obj11955)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj11955.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj11955)
    self.globalAndLocalPostcondition(self.obj11955, rootNode)
    self.obj11955.postAction( rootNode.CREATE )

    self.obj11953=MT_pre__System(self)
    self.obj11953.isGraphObjectVisual = True

    if(hasattr(self.obj11953, '_setHierarchicalLink')):
      self.obj11953._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj11953.MT_pivotOut__.setValue('')
    self.obj11953.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj11953.MT_subtypeMatching__.setValue(('True', 0))
    self.obj11953.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj11953.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11953.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj11953.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj11953.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj11953.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11953.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj11953.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11953.MT_pre__name.setHeight(15)

    self.obj11953.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(180.0,120.0,self.obj11953)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj11953.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj11953)
    self.globalAndLocalPostcondition(self.obj11953, rootNode)
    self.obj11953.postAction( rootNode.CREATE )

    self.obj11956=MT_pre__directLink_T(self)
    self.obj11956.isGraphObjectVisual = True

    if(hasattr(self.obj11956, '_setHierarchicalLink')):
      self.obj11956._setHierarchicalLink(False)

    # MT_label__
    self.obj11956.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj11956.MT_pivotOut__.setValue('')
    self.obj11956.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj11956.MT_subtypeMatching__.setValue(('True', 0))
    self.obj11956.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj11956.MT_pivotIn__.setValue('')
    self.obj11956.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj11956.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11956.MT_pre__associationType.setHeight(15)

    self.obj11956.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(455.0,253.0,self.obj11956)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj11956.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj11956)
    self.globalAndLocalPostcondition(self.obj11956, rootNode)
    self.obj11956.postAction( rootNode.CREATE )

    self.obj11957=MT_pre__directLink_T(self)
    self.obj11957.isGraphObjectVisual = True

    if(hasattr(self.obj11957, '_setHierarchicalLink')):
      self.obj11957._setHierarchicalLink(False)

    # MT_label__
    self.obj11957.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj11957.MT_pivotOut__.setValue('')
    self.obj11957.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj11957.MT_subtypeMatching__.setValue(('True', 0))
    self.obj11957.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj11957.MT_pivotIn__.setValue('')
    self.obj11957.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj11957.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj11957.MT_pre__associationType.setHeight(15)

    self.obj11957.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(355.0,313.0,self.obj11957)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj11957.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj11957)
    self.globalAndLocalPostcondition(self.obj11957, rootNode)
    self.obj11957.postAction( rootNode.CREATE )

    # Connections for obj11952 (graphObject_: Obj12) of type LHS
    self.drawConnections(
 )
    # Connections for obj11954 (graphObject_: Obj14) of type MT_pre__SoftwareComposition
    self.drawConnections(
 )
    # Connections for obj11955 (graphObject_: Obj15) of type MT_pre__SoftwareComposition
    self.drawConnections(
 )
    # Connections for obj11953 (graphObject_: Obj13) of type MT_pre__System
    self.drawConnections(
(self.obj11953,self.obj11956,[348.0, 193.0, 455.0, 253.0],"true", 2),
(self.obj11953,self.obj11957,[348.0, 193.0, 355.0, 313.0],"true", 2) )
    # Connections for obj11956 (graphObject_: Obj16) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj11956,self.obj11954,[455.0, 253.0, 562.0, 313.0],"true", 2) )
    # Connections for obj11957 (graphObject_: Obj17) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj11957,self.obj11955,[355.0, 313.0, 362.0, 433.0],"true", 2) )

newfunction = M5ThenClausePart2Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
