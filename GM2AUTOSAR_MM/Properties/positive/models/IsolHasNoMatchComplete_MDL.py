"""
__IsolHasNoMatchComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Oct 11 15:17:59 2013
____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Distributable import *
from MT_pre__trace_link import *
from MT_pre__ComponentPrototype import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Distributable import *
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

def IsolHasNoMatchComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('IsolHasNoMatchComplete')
    # --- ASG attributes over ---


    self.obj3032=LHS(self)
    self.obj3032.isGraphObjectVisual = True

    if(hasattr(self.obj3032, '_setHierarchicalLink')):
      self.obj3032._setHierarchicalLink(False)

    # constraint
    self.obj3032.constraint.setValue('if PreNode(\'1\')[\'cardinality\']==\'1\' and PreNode(\'2\')[\'cardinality\']==\'+\':\n    return True\nreturn False\n')
    self.obj3032.constraint.setHeight(15)

    self.obj3032.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,60.0,self.obj3032)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3032.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3032)
    self.globalAndLocalPostcondition(self.obj3032, rootNode)
    self.obj3032.postAction( rootNode.CREATE )

    self.obj3033=MT_pre__Distributable(self)
    self.obj3033.isGraphObjectVisual = True

    if(hasattr(self.obj3033, '_setHierarchicalLink')):
      self.obj3033._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3033.MT_pivotOut__.setValue('')
    self.obj3033.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3033.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3033.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3033.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3033.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3033.MT_pivotIn__.setValue('')
    self.obj3033.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3033.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj3033.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3033.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3033.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3033.MT_pre__name.setHeight(15)

    self.obj3033.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(160.0,80.0,self.obj3033)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3033.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3033)
    self.globalAndLocalPostcondition(self.obj3033, rootNode)
    self.obj3033.postAction( rootNode.CREATE )

    self.obj3036=MT_pre__trace_link(self)
    self.obj3036.isGraphObjectVisual = True

    if(hasattr(self.obj3036, '_setHierarchicalLink')):
      self.obj3036._setHierarchicalLink(False)

    # MT_label__
    self.obj3036.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj3036.MT_pivotOut__.setValue('')
    self.obj3036.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3036.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3036.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3036.MT_pivotIn__.setValue('')
    self.obj3036.MT_pivotIn__.setNone()

    self.obj3036.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(325.0,233.5,self.obj3036)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3036.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3036)
    self.globalAndLocalPostcondition(self.obj3036, rootNode)
    self.obj3036.postAction( rootNode.CREATE )

    self.obj3035=MT_pre__ComponentPrototype(self)
    self.obj3035.isGraphObjectVisual = True

    if(hasattr(self.obj3035, '_setHierarchicalLink')):
      self.obj3035._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3035.MT_pivotOut__.setValue('')
    self.obj3035.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3035.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3035.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3035.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3035.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3035.MT_pivotIn__.setValue('')
    self.obj3035.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3035.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj3035.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3035.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3035.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3035.MT_pre__name.setHeight(15)

    self.obj3035.graphClass_= graph_MT_pre__ComponentPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__ComponentPrototype(140.0,240.0,self.obj3035)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ComponentPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3035.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3035)
    self.globalAndLocalPostcondition(self.obj3035, rootNode)
    self.obj3035.postAction( rootNode.CREATE )

    # Connections for obj3032 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )
    # Connections for obj3033 (graphObject_: Obj5) of type MT_pre__Distributable
    self.drawConnections(
 )
    # Connections for obj3036 (graphObject_: Obj8) of type MT_pre__trace_link
    self.drawConnections(
(self.obj3036,self.obj3033,[325.0, 233.5, 330.0, 154.0],"true", 2) )
    # Connections for obj3035 (graphObject_: Obj7) of type MT_pre__ComponentPrototype
    self.drawConnections(
(self.obj3035,self.obj3036,[320.0, 313.0, 325.0, 233.5],"true", 2) )

newfunction = IsolHasNoMatchComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
