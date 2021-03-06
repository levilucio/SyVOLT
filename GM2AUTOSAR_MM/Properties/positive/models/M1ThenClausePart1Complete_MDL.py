"""
__M1ThenClausePart1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 09:07:10 2013
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__ComponentPrototype import *
from MT_pre__directLink_T import *
from MT_pre__CompositionType import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__ComponentPrototype import *
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

def M1ThenClausePart1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M1ThenClausePart1Complete')
    # --- ASG attributes over ---


    self.obj1555=LHS(self)
    self.obj1555.isGraphObjectVisual = True

    if(hasattr(self.obj1555, '_setHierarchicalLink')):
      self.obj1555._setHierarchicalLink(False)

    # constraint
    self.obj1555.constraint.setValue('if  PreNode(\'3\')[\'associationType\']==\'component\':\n    return True\nreturn False\n')
    self.obj1555.constraint.setHeight(15)

    self.obj1555.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,100.0,self.obj1555)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1555.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1555)
    self.globalAndLocalPostcondition(self.obj1555, rootNode)
    self.obj1555.postAction( rootNode.CREATE )

    self.obj1556=MT_pre__ComponentPrototype(self)
    self.obj1556.isGraphObjectVisual = True

    if(hasattr(self.obj1556, '_setHierarchicalLink')):
      self.obj1556._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1556.MT_pivotOut__.setValue('')
    self.obj1556.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1556.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1556.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1556.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1556.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1556.MT_pivotIn__.setValue('')
    self.obj1556.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1556.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj1556.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1556.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1556.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1556.MT_pre__name.setHeight(15)

    self.obj1556.graphClass_= graph_MT_pre__ComponentPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__ComponentPrototype(280.0,340.0,self.obj1556)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1556.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1556)
    self.globalAndLocalPostcondition(self.obj1556, rootNode)
    self.obj1556.postAction( rootNode.CREATE )

    self.obj1557=MT_pre__directLink_T(self)
    self.obj1557.isGraphObjectVisual = True

    if(hasattr(self.obj1557, '_setHierarchicalLink')):
      self.obj1557._setHierarchicalLink(False)

    # MT_label__
    self.obj1557.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj1557.MT_pivotOut__.setValue('')
    self.obj1557.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1557.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1557.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1557.MT_pivotIn__.setValue('')
    self.obj1557.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1557.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1557.MT_pre__associationType.setHeight(15)

    self.obj1557.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(384.0,343.0,self.obj1557)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1557.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1557)
    self.globalAndLocalPostcondition(self.obj1557, rootNode)
    self.obj1557.postAction( rootNode.CREATE )

    self.obj1558=MT_pre__CompositionType(self)
    self.obj1558.isGraphObjectVisual = True

    if(hasattr(self.obj1558, '_setHierarchicalLink')):
      self.obj1558._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1558.MT_pivotOut__.setValue('')
    self.obj1558.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1558.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1558.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1558.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1558.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1558.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj1558.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj1558.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1558.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1558.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1558.MT_pre__name.setHeight(15)

    self.obj1558.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(140.0,200.0,self.obj1558)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1558.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1558)
    self.globalAndLocalPostcondition(self.obj1558, rootNode)
    self.obj1558.postAction( rootNode.CREATE )

    # Connections for obj1555 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )
    # Connections for obj1556 (graphObject_: Obj5) of type MT_pre__ComponentPrototype
    self.drawConnections(
 )
    # Connections for obj1557 (graphObject_: Obj6) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj1557,self.obj1556,[384.0, 343.0, 460.0, 413.0],"true", 2) )
    # Connections for obj1558 (graphObject_: Obj7) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj1558,self.obj1557,[308.0, 273.0, 384.0, 343.0],"true", 2) )

newfunction = M1ThenClausePart1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
