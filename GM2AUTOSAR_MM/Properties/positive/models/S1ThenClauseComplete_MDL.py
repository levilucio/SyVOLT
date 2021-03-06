"""
__S1ThenClauseComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 16 11:56:05 2013
__________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__SoftwareComposition import *
from MT_pre__System import *
from MT_pre__ComponentPrototype import *
from MT_pre__directLink_T import *
from MT_pre__CompositionType import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__System import *
from graph_MT_pre__ComponentPrototype import *
from graph_LHS import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__SoftwareComposition import *
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

def S1ThenClauseComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('S1ThenClauseComplete')
    # --- ASG attributes over ---


    self.obj4524=LHS(self)
    self.obj4524.isGraphObjectVisual = True

    if(hasattr(self.obj4524, '_setHierarchicalLink')):
      self.obj4524._setHierarchicalLink(False)

    # constraint
    self.obj4524.constraint.setValue('if PreNode(\'1\')[\'cardinality\']==\'+\' and PreNode(\'2\')[\'cardinality\']==\'+\' and PreNode(\'3\')[\'cardinality\']==\'+\' and PreNode(\'4\')[\'cardinality\']==\'+\' and PreNode(\'5\')[\'associationType\']==\'softwareComposition\' and PreNode(\'6\')[\'associationType\']==\'softwareComposition\' and PreNode(\'7\')[\'associationType\']==\'component\':\n    return True\nreturn False\n')
    self.obj4524.constraint.setHeight(15)

    self.obj4524.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,40.0,self.obj4524)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4524.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4524)
    self.globalAndLocalPostcondition(self.obj4524, rootNode)
    self.obj4524.postAction( rootNode.CREATE )

    self.obj4525=MT_pre__SoftwareComposition(self)
    self.obj4525.isGraphObjectVisual = True

    if(hasattr(self.obj4525, '_setHierarchicalLink')):
      self.obj4525._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4525.MT_pivotOut__.setValue('')
    self.obj4525.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4525.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4525.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4525.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4525.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4525.MT_pivotIn__.setValue('')
    self.obj4525.MT_pivotIn__.setNone()

    # MT_label__
    self.obj4525.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj4525.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4525.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4525.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4525.MT_pre__name.setHeight(15)

    self.obj4525.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(256.0,135.0,self.obj4525)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4525.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4525)
    self.globalAndLocalPostcondition(self.obj4525, rootNode)
    self.obj4525.postAction( rootNode.CREATE )

    self.obj4526=MT_pre__System(self)
    self.obj4526.isGraphObjectVisual = True

    if(hasattr(self.obj4526, '_setHierarchicalLink')):
      self.obj4526._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4526.MT_pivotOut__.setValue('')
    self.obj4526.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4526.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4526.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4526.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4526.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4526.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj4526.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj4526.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4526.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4526.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4526.MT_pre__name.setHeight(15)

    self.obj4526.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(73.0,53.0,self.obj4526)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4526.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4526)
    self.globalAndLocalPostcondition(self.obj4526, rootNode)
    self.obj4526.postAction( rootNode.CREATE )

    self.obj4527=MT_pre__ComponentPrototype(self)
    self.obj4527.isGraphObjectVisual = True

    if(hasattr(self.obj4527, '_setHierarchicalLink')):
      self.obj4527._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4527.MT_pivotOut__.setValue('')
    self.obj4527.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4527.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4527.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4527.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4527.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4527.MT_pivotIn__.setValue('element5')

    # MT_label__
    self.obj4527.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj4527.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4527.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4527.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4527.MT_pre__name.setHeight(15)

    self.obj4527.graphClass_= graph_MT_pre__ComponentPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__ComponentPrototype(80.0,300.0,self.obj4527)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4527.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4527)
    self.globalAndLocalPostcondition(self.obj4527, rootNode)
    self.obj4527.postAction( rootNode.CREATE )

    self.obj4528=MT_pre__directLink_T(self)
    self.obj4528.isGraphObjectVisual = True

    if(hasattr(self.obj4528, '_setHierarchicalLink')):
      self.obj4528._setHierarchicalLink(False)

    # MT_label__
    self.obj4528.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj4528.MT_pivotOut__.setValue('')
    self.obj4528.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4528.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4528.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4528.MT_pivotIn__.setValue('')
    self.obj4528.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj4528.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4528.MT_pre__associationType.setHeight(15)

    self.obj4528.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(339.5,167.0,self.obj4528)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4528.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4528)
    self.globalAndLocalPostcondition(self.obj4528, rootNode)
    self.obj4528.postAction( rootNode.CREATE )

    self.obj4529=MT_pre__directLink_T(self)
    self.obj4529.isGraphObjectVisual = True

    if(hasattr(self.obj4529, '_setHierarchicalLink')):
      self.obj4529._setHierarchicalLink(False)

    # MT_label__
    self.obj4529.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj4529.MT_pivotOut__.setValue('')
    self.obj4529.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4529.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4529.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4529.MT_pivotIn__.setValue('')
    self.obj4529.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj4529.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4529.MT_pre__associationType.setHeight(15)

    self.obj4529.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(443.0,270.5,self.obj4529)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4529.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4529)
    self.globalAndLocalPostcondition(self.obj4529, rootNode)
    self.obj4529.postAction( rootNode.CREATE )

    self.obj4530=MT_pre__directLink_T(self)
    self.obj4530.isGraphObjectVisual = True

    if(hasattr(self.obj4530, '_setHierarchicalLink')):
      self.obj4530._setHierarchicalLink(False)

    # MT_label__
    self.obj4530.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj4530.MT_pivotOut__.setValue('')
    self.obj4530.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4530.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4530.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4530.MT_pivotIn__.setValue('')
    self.obj4530.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj4530.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4530.MT_pre__associationType.setHeight(15)

    self.obj4530.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(354.0,353.0,self.obj4530)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4530.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4530)
    self.globalAndLocalPostcondition(self.obj4530, rootNode)
    self.obj4530.postAction( rootNode.CREATE )

    self.obj4531=MT_pre__CompositionType(self)
    self.obj4531.isGraphObjectVisual = True

    if(hasattr(self.obj4531, '_setHierarchicalLink')):
      self.obj4531._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4531.MT_pivotOut__.setValue('')
    self.obj4531.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4531.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4531.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4531.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4531.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4531.MT_pivotIn__.setValue('')
    self.obj4531.MT_pivotIn__.setNone()

    # MT_label__
    self.obj4531.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj4531.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4531.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4531.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4531.MT_pre__name.setHeight(15)

    self.obj4531.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(280.0,260.0,self.obj4531)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4531.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4531)
    self.globalAndLocalPostcondition(self.obj4531, rootNode)
    self.obj4531.postAction( rootNode.CREATE )

    # Connections for obj4524 (graphObject_: Obj12) of type LHS
    self.drawConnections(
 )
    # Connections for obj4525 (graphObject_: Obj13) of type MT_pre__SoftwareComposition
    self.drawConnections(
(self.obj4525,self.obj4529,[438.0, 208.0, 443.0, 270.5],"true", 2) )
    # Connections for obj4526 (graphObject_: Obj14) of type MT_pre__System
    self.drawConnections(
(self.obj4526,self.obj4528,[241.0, 126.0, 339.5, 167.0],"true", 2) )
    # Connections for obj4527 (graphObject_: Obj15) of type MT_pre__ComponentPrototype
    self.drawConnections(
 )
    # Connections for obj4528 (graphObject_: Obj16) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj4528,self.obj4525,[339.5, 167.0, 438.0, 208.0],"true", 2) )
    # Connections for obj4529 (graphObject_: Obj17) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj4529,self.obj4531,[443.0, 270.5, 448.0, 333.0],"true", 2) )
    # Connections for obj4530 (graphObject_: Obj18) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj4530,self.obj4527,[354.0, 353.0, 260.0, 373.0],"true", 2) )
    # Connections for obj4531 (graphObject_: Obj19) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj4531,self.obj4530,[448.0, 333.0, 354.0, 353.0],"true", 2) )

newfunction = S1ThenClauseComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
