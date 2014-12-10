"""
__S1IfClauseComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 16 11:52:33 2013
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__System import *
from MT_pre__SystemMapping import *
from MT_pre__ComponentPrototype import *
from MT_pre__directLink_T import *
from MT_pre__SwCompToEcuMapping_component import *
from MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SwcToEcuMapping import *
from graph_MT_pre__SystemMapping import *
from graph_LHS import *
from graph_MT_pre__System import *
from graph_MT_pre__ComponentPrototype import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__SwCompToEcuMapping_component import *
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

def S1IfClauseComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('S1IfClauseComplete')
    # --- ASG attributes over ---


    self.obj3020=LHS(self)
    self.obj3020.isGraphObjectVisual = True

    if(hasattr(self.obj3020, '_setHierarchicalLink')):
      self.obj3020._setHierarchicalLink(False)

    # constraint
    self.obj3020.constraint.setValue('if PreNode(\'1\')[\'cardinality\']==\'+\' and PreNode(\'2\')[\'cardinality\']==\'+\' and PreNode(\'3\')[\'cardinality\']==\'+\' and PreNode(\'4\')[\'cardinality\']==\'+\' and PreNode(\'5\')[\'cardinality\']==\'+\' and PreNode(\'6\')[\'associationType\']==\'mapping\' and PreNode(\'7\')[\'associationType\']==\'swMapping\' and PreNode(\'8\')[\'associationType\']==\'component\' and PreNode(\'9\')[\'associationType\']==\'componentPrototype\':\n    return True\nreturn False\n')
    self.obj3020.constraint.setHeight(15)

    self.obj3020.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,320.0,self.obj3020)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3020.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3020)
    self.globalAndLocalPostcondition(self.obj3020, rootNode)
    self.obj3020.postAction( rootNode.CREATE )

    self.obj3021=MT_pre__System(self)
    self.obj3021.isGraphObjectVisual = True

    if(hasattr(self.obj3021, '_setHierarchicalLink')):
      self.obj3021._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3021.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj3021.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3021.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3021.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3021.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3021.MT_pivotIn__.setValue('')
    self.obj3021.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3021.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj3021.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3021.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3021.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3021.MT_pre__name.setHeight(15)

    self.obj3021.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(80.0,340.0,self.obj3021)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3021.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3021)
    self.globalAndLocalPostcondition(self.obj3021, rootNode)
    self.obj3021.postAction( rootNode.CREATE )

    self.obj3022=MT_pre__SystemMapping(self)
    self.obj3022.isGraphObjectVisual = True

    if(hasattr(self.obj3022, '_setHierarchicalLink')):
      self.obj3022._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3022.MT_pivotOut__.setValue('')
    self.obj3022.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3022.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3022.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3022.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3022.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3022.MT_pivotIn__.setValue('')
    self.obj3022.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3022.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj3022.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3022.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3022.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3022.MT_pre__name.setHeight(15)

    self.obj3022.graphClass_= graph_MT_pre__SystemMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SystemMapping(266.0,340.0,self.obj3022)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SystemMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3022.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3022)
    self.globalAndLocalPostcondition(self.obj3022, rootNode)
    self.obj3022.postAction( rootNode.CREATE )

    self.obj3023=MT_pre__ComponentPrototype(self)
    self.obj3023.isGraphObjectVisual = True

    if(hasattr(self.obj3023, '_setHierarchicalLink')):
      self.obj3023._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3023.MT_pivotOut__.setValue('element5')

    # MT_subtypeMatching__
    self.obj3023.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3023.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3023.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3023.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3023.MT_pivotIn__.setValue('')
    self.obj3023.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3023.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj3023.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3023.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3023.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3023.MT_pre__name.setHeight(15)

    self.obj3023.graphClass_= graph_MT_pre__ComponentPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__ComponentPrototype(75.0,481.0,self.obj3023)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3023.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3023)
    self.globalAndLocalPostcondition(self.obj3023, rootNode)
    self.obj3023.postAction( rootNode.CREATE )

    self.obj3024=MT_pre__directLink_T(self)
    self.obj3024.isGraphObjectVisual = True

    if(hasattr(self.obj3024, '_setHierarchicalLink')):
      self.obj3024._setHierarchicalLink(False)

    # MT_label__
    self.obj3024.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj3024.MT_pivotOut__.setValue('')
    self.obj3024.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3024.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3024.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3024.MT_pivotIn__.setValue('')
    self.obj3024.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3024.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3024.MT_pre__associationType.setHeight(15)

    self.obj3024.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(342.5,413.0,self.obj3024)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3024.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3024)
    self.globalAndLocalPostcondition(self.obj3024, rootNode)
    self.obj3024.postAction( rootNode.CREATE )

    self.obj3025=MT_pre__directLink_T(self)
    self.obj3025.isGraphObjectVisual = True

    if(hasattr(self.obj3025, '_setHierarchicalLink')):
      self.obj3025._setHierarchicalLink(False)

    # MT_label__
    self.obj3025.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj3025.MT_pivotOut__.setValue('')
    self.obj3025.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3025.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3025.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3025.MT_pivotIn__.setValue('')
    self.obj3025.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3025.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3025.MT_pre__associationType.setHeight(15)

    self.obj3025.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(459.0,476.5,self.obj3025)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3025.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3025)
    self.globalAndLocalPostcondition(self.obj3025, rootNode)
    self.obj3025.postAction( rootNode.CREATE )

    self.obj3026=MT_pre__directLink_T(self)
    self.obj3026.isGraphObjectVisual = True

    if(hasattr(self.obj3026, '_setHierarchicalLink')):
      self.obj3026._setHierarchicalLink(False)

    # MT_label__
    self.obj3026.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj3026.MT_pivotOut__.setValue('')
    self.obj3026.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3026.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3026.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3026.MT_pivotIn__.setValue('')
    self.obj3026.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3026.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3026.MT_pre__associationType.setHeight(15)

    self.obj3026.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(464.5,604.5,self.obj3026)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3026.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3026)
    self.globalAndLocalPostcondition(self.obj3026, rootNode)
    self.obj3026.postAction( rootNode.CREATE )

    self.obj3027=MT_pre__directLink_T(self)
    self.obj3027.isGraphObjectVisual = True

    if(hasattr(self.obj3027, '_setHierarchicalLink')):
      self.obj3027._setHierarchicalLink(False)

    # MT_label__
    self.obj3027.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj3027.MT_pivotOut__.setValue('')
    self.obj3027.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3027.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3027.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3027.MT_pivotIn__.setValue('')
    self.obj3027.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3027.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3027.MT_pre__associationType.setHeight(15)

    self.obj3027.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(351.5,611.5,self.obj3027)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3027.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3027)
    self.globalAndLocalPostcondition(self.obj3027, rootNode)
    self.obj3027.postAction( rootNode.CREATE )

    self.obj3028=MT_pre__SwCompToEcuMapping_component(self)
    self.obj3028.isGraphObjectVisual = True

    if(hasattr(self.obj3028, '_setHierarchicalLink')):
      self.obj3028._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3028.MT_pivotOut__.setValue('')
    self.obj3028.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3028.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3028.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3028.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3028.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3028.MT_pivotIn__.setValue('')
    self.obj3028.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3028.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj3028.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3028.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3028.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3028.MT_pre__name.setHeight(15)

    self.obj3028.graphClass_= graph_MT_pre__SwCompToEcuMapping_component
    if self.genGraphics:
       new_obj = graph_MT_pre__SwCompToEcuMapping_component(280.0,596.0,self.obj3028)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwCompToEcuMapping_component", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3028.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3028)
    self.globalAndLocalPostcondition(self.obj3028, rootNode)
    self.obj3028.postAction( rootNode.CREATE )

    self.obj3029=MT_pre__SwcToEcuMapping(self)
    self.obj3029.isGraphObjectVisual = True

    if(hasattr(self.obj3029, '_setHierarchicalLink')):
      self.obj3029._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3029.MT_pivotOut__.setValue('')
    self.obj3029.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3029.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3029.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3029.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3029.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3029.MT_pivotIn__.setValue('')
    self.obj3029.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3029.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj3029.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3029.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3029.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3029.MT_pre__name.setHeight(15)

    self.obj3029.graphClass_= graph_MT_pre__SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SwcToEcuMapping(307.0,467.0,self.obj3029)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3029.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3029)
    self.globalAndLocalPostcondition(self.obj3029, rootNode)
    self.obj3029.postAction( rootNode.CREATE )

    # Connections for obj3020 (graphObject_: Obj2) of type LHS
    self.drawConnections(
 )
    # Connections for obj3021 (graphObject_: Obj3) of type MT_pre__System
    self.drawConnections(
(self.obj3021,self.obj3024,[248.0, 413.0, 342.5, 413.0],"true", 2) )
    # Connections for obj3022 (graphObject_: Obj4) of type MT_pre__SystemMapping
    self.drawConnections(
(self.obj3022,self.obj3025,[437.0, 413.0, 459.0, 476.5],"true", 2) )
    # Connections for obj3023 (graphObject_: Obj5) of type MT_pre__ComponentPrototype
    self.drawConnections(
 )
    # Connections for obj3024 (graphObject_: Obj6) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj3024,self.obj3022,[342.5, 413.0, 437.0, 413.0],"true", 2) )
    # Connections for obj3025 (graphObject_: Obj7) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj3025,self.obj3029,[459.0, 476.5, 481.0, 540.0],"true", 2) )
    # Connections for obj3026 (graphObject_: Obj8) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj3026,self.obj3028,[464.5, 604.5, 448.0, 669.0],"true", 2) )
    # Connections for obj3027 (graphObject_: Obj9) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj3027,self.obj3023,[351.5, 611.5, 255.0, 554.0],"true", 2) )
    # Connections for obj3028 (graphObject_: Obj10) of type MT_pre__SwCompToEcuMapping_component
    self.drawConnections(
(self.obj3028,self.obj3027,[448.0, 669.0, 351.5, 611.5],"true", 2) )
    # Connections for obj3029 (graphObject_: Obj11) of type MT_pre__SwcToEcuMapping
    self.drawConnections(
(self.obj3029,self.obj3026,[481.0, 540.0, 464.5, 604.5],"true", 2) )

newfunction = S1IfClauseComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
