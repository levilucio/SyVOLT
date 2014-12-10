"""
__M2ThenClausePart2Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 13:20:42 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__SoftwareComposition import *
from MT_pre__directLink_T import *
from MT_pre__CompositionType import *
from graph_MT_pre__CompositionType import *
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

def M2ThenClausePart2Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M2ThenClausePart2Complete')
    # --- ASG attributes over ---


    self.obj15157=LHS(self)
    self.obj15157.isGraphObjectVisual = True

    if(hasattr(self.obj15157, '_setHierarchicalLink')):
      self.obj15157._setHierarchicalLink(False)

    # constraint
    self.obj15157.constraint.setValue('if PreNode(\'4\')[\'associationType\']==\'softwareComposition\' and PreNode(\'5\')[\'associationType\']==\'softwareComposition\' :\n    return True\nreturn False\n')
    self.obj15157.constraint.setHeight(15)

    self.obj15157.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,80.0,self.obj15157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15157)
    self.globalAndLocalPostcondition(self.obj15157, rootNode)
    self.obj15157.postAction( rootNode.CREATE )

    self.obj15158=MT_pre__SoftwareComposition(self)
    self.obj15158.isGraphObjectVisual = True

    if(hasattr(self.obj15158, '_setHierarchicalLink')):
      self.obj15158._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj15158.MT_pivotOut__.setValue('')
    self.obj15158.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15158.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15158.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj15158.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15158.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj15158.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj15158.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj15158.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15158.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj15158.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15158.MT_pre__name.setHeight(15)

    self.obj15158.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(140.0,100.0,self.obj15158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15158)
    self.globalAndLocalPostcondition(self.obj15158, rootNode)
    self.obj15158.postAction( rootNode.CREATE )

    self.obj15159=MT_pre__directLink_T(self)
    self.obj15159.isGraphObjectVisual = True

    if(hasattr(self.obj15159, '_setHierarchicalLink')):
      self.obj15159._setHierarchicalLink(False)

    # MT_label__
    self.obj15159.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj15159.MT_pivotOut__.setValue('')
    self.obj15159.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15159.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15159.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj15159.MT_pivotIn__.setValue('')
    self.obj15159.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj15159.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15159.MT_pre__associationType.setHeight(15)

    self.obj15159.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(425.0,233.0,self.obj15159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj15159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15159)
    self.globalAndLocalPostcondition(self.obj15159, rootNode)
    self.obj15159.postAction( rootNode.CREATE )

    self.obj15160=MT_pre__directLink_T(self)
    self.obj15160.isGraphObjectVisual = True

    if(hasattr(self.obj15160, '_setHierarchicalLink')):
      self.obj15160._setHierarchicalLink(False)

    # MT_label__
    self.obj15160.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj15160.MT_pivotOut__.setValue('')
    self.obj15160.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15160.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15160.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj15160.MT_pivotIn__.setValue('')
    self.obj15160.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj15160.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15160.MT_pre__associationType.setHeight(15)

    self.obj15160.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(318.0,293.0,self.obj15160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj15160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15160)
    self.globalAndLocalPostcondition(self.obj15160, rootNode)
    self.obj15160.postAction( rootNode.CREATE )

    self.obj15161=MT_pre__CompositionType(self)
    self.obj15161.isGraphObjectVisual = True

    if(hasattr(self.obj15161, '_setHierarchicalLink')):
      self.obj15161._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj15161.MT_pivotOut__.setValue('')
    self.obj15161.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15161.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15161.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj15161.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15161.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj15161.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj15161.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj15161.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15161.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj15161.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15161.MT_pre__name.setHeight(15)

    self.obj15161.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(360.0,220.0,self.obj15161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15161)
    self.globalAndLocalPostcondition(self.obj15161, rootNode)
    self.obj15161.postAction( rootNode.CREATE )

    self.obj15162=MT_pre__CompositionType(self)
    self.obj15162.isGraphObjectVisual = True

    if(hasattr(self.obj15162, '_setHierarchicalLink')):
      self.obj15162._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj15162.MT_pivotOut__.setValue('')
    self.obj15162.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15162.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15162.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj15162.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15162.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj15162.MT_pivotIn__.setValue('')
    self.obj15162.MT_pivotIn__.setNone()

    # MT_label__
    self.obj15162.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj15162.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15162.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj15162.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj15162.MT_pre__name.setHeight(15)

    self.obj15162.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(146.0,340.0,self.obj15162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15162)
    self.globalAndLocalPostcondition(self.obj15162, rootNode)
    self.obj15162.postAction( rootNode.CREATE )

    # Connections for obj15157 (graphObject_: Obj77) of type LHS
    self.drawConnections(
 )
    # Connections for obj15158 (graphObject_: Obj78) of type MT_pre__SoftwareComposition
    self.drawConnections(
(self.obj15158,self.obj15159,[322.0, 173.0, 425.0, 233.0],"true", 2),
(self.obj15158,self.obj15160,[322.0, 173.0, 318.0, 293.0],"true", 2) )
    # Connections for obj15159 (graphObject_: Obj79) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj15159,self.obj15161,[425.0, 233.0, 528.0, 293.0],"true", 2) )
    # Connections for obj15160 (graphObject_: Obj80) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj15160,self.obj15162,[318.0, 293.0, 314.0, 413.0],"true", 2) )
    # Connections for obj15161 (graphObject_: Obj81) of type MT_pre__CompositionType
    self.drawConnections(
 )
    # Connections for obj15162 (graphObject_: Obj82) of type MT_pre__CompositionType
    self.drawConnections(
 )

newfunction = M2ThenClausePart2Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
