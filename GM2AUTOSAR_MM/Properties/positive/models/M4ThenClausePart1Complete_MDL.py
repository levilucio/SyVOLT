"""
__M4ThenClausePart1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 17:15:50 2013
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

def M4ThenClausePart1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M4ThenClausePart1Complete')
    # --- ASG attributes over ---


    self.obj22614=LHS(self)
    self.obj22614.isGraphObjectVisual = True

    if(hasattr(self.obj22614, '_setHierarchicalLink')):
      self.obj22614._setHierarchicalLink(False)

    # constraint
    self.obj22614.constraint.setValue('if PreNode(\'3\')[\'associationType\']==\'ecuInstance\':\n    return True\nreturn False\n')
    self.obj22614.constraint.setHeight(15)

    self.obj22614.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(140.0,80.0,self.obj22614)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22614.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22614)
    self.globalAndLocalPostcondition(self.obj22614, rootNode)
    self.obj22614.postAction( rootNode.CREATE )

    self.obj22616=MT_pre__EcuInstance(self)
    self.obj22616.isGraphObjectVisual = True

    if(hasattr(self.obj22616, '_setHierarchicalLink')):
      self.obj22616._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj22616.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj22616.MT_subtypeMatching__.setValue(('True', 0))
    self.obj22616.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj22616.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22616.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj22616.MT_pivotIn__.setValue('')
    self.obj22616.MT_pivotIn__.setNone()

    # MT_label__
    self.obj22616.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj22616.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22616.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj22616.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22616.MT_pre__name.setHeight(15)

    self.obj22616.graphClass_= graph_MT_pre__EcuInstance
    if self.genGraphics:
       new_obj = graph_MT_pre__EcuInstance(280.0,320.0,self.obj22616)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EcuInstance", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22616.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22616)
    self.globalAndLocalPostcondition(self.obj22616, rootNode)
    self.obj22616.postAction( rootNode.CREATE )

    self.obj22617=MT_pre__directLink_T(self)
    self.obj22617.isGraphObjectVisual = True

    if(hasattr(self.obj22617, '_setHierarchicalLink')):
      self.obj22617._setHierarchicalLink(False)

    # MT_label__
    self.obj22617.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj22617.MT_pivotOut__.setValue('')
    self.obj22617.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj22617.MT_subtypeMatching__.setValue(('True', 0))
    self.obj22617.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj22617.MT_pivotIn__.setValue('')
    self.obj22617.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj22617.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22617.MT_pre__associationType.setHeight(15)

    self.obj22617.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(391.0,283.0,self.obj22617)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj22617.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22617)
    self.globalAndLocalPostcondition(self.obj22617, rootNode)
    self.obj22617.postAction( rootNode.CREATE )

    self.obj22615=MT_pre__SwcToEcuMapping(self)
    self.obj22615.isGraphObjectVisual = True

    if(hasattr(self.obj22615, '_setHierarchicalLink')):
      self.obj22615._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj22615.MT_pivotOut__.setValue('')
    self.obj22615.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj22615.MT_subtypeMatching__.setValue(('True', 0))
    self.obj22615.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj22615.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22615.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj22615.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj22615.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj22615.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22615.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj22615.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj22615.MT_pre__name.setHeight(15)

    self.obj22615.graphClass_= graph_MT_pre__SwcToEcuMapping
    if self.genGraphics:
       new_obj = graph_MT_pre__SwcToEcuMapping(160.0,100.0,self.obj22615)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SwcToEcuMapping", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22615.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22615)
    self.globalAndLocalPostcondition(self.obj22615, rootNode)
    self.obj22615.postAction( rootNode.CREATE )

    # Connections for obj22614 (graphObject_: Obj94) of type LHS
    self.drawConnections(
 )
    # Connections for obj22616 (graphObject_: Obj96) of type MT_pre__EcuInstance
    self.drawConnections(
 )
    # Connections for obj22617 (graphObject_: Obj97) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj22617,self.obj22616,[391.0, 283.0, 448.0, 393.0],"true", 2) )
    # Connections for obj22615 (graphObject_: Obj95) of type MT_pre__SwcToEcuMapping
    self.drawConnections(
(self.obj22615,self.obj22617,[334.0, 173.0, 391.0, 283.0],"true", 2) )

newfunction = M4ThenClausePart1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
