"""
__M2ThenClausePart1Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 11:27:05 2013
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

def M2ThenClausePart1Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M2ThenClausePart1Complete')
    # --- ASG attributes over ---


    self.obj12114=LHS(self)
    self.obj12114.isGraphObjectVisual = True

    if(hasattr(self.obj12114, '_setHierarchicalLink')):
      self.obj12114._setHierarchicalLink(False)

    # constraint
    self.obj12114.constraint.setValue('if PreNode(\'3\')[\'associationType\']==\'softwareComposition\':\n    return True\nreturn False\n')
    self.obj12114.constraint.setHeight(15)

    self.obj12114.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(160.0,100.0,self.obj12114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj12114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj12114)
    self.globalAndLocalPostcondition(self.obj12114, rootNode)
    self.obj12114.postAction( rootNode.CREATE )

    self.obj12115=MT_pre__SoftwareComposition(self)
    self.obj12115.isGraphObjectVisual = True

    if(hasattr(self.obj12115, '_setHierarchicalLink')):
      self.obj12115._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj12115.MT_pivotOut__.setValue('')
    self.obj12115.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj12115.MT_subtypeMatching__.setValue(('True', 0))
    self.obj12115.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj12115.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12115.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj12115.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj12115.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj12115.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12115.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj12115.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12115.MT_pre__name.setHeight(15)

    self.obj12115.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(220.0,120.0,self.obj12115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj12115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj12115)
    self.globalAndLocalPostcondition(self.obj12115, rootNode)
    self.obj12115.postAction( rootNode.CREATE )

    self.obj12116=MT_pre__directLink_T(self)
    self.obj12116.isGraphObjectVisual = True

    if(hasattr(self.obj12116, '_setHierarchicalLink')):
      self.obj12116._setHierarchicalLink(False)

    # MT_label__
    self.obj12116.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj12116.MT_pivotOut__.setValue('')
    self.obj12116.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj12116.MT_subtypeMatching__.setValue(('True', 0))
    self.obj12116.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj12116.MT_pivotIn__.setValue('')
    self.obj12116.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj12116.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12116.MT_pre__associationType.setHeight(15)

    self.obj12116.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(405.0,293.0,self.obj12116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj12116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj12116)
    self.globalAndLocalPostcondition(self.obj12116, rootNode)
    self.obj12116.postAction( rootNode.CREATE )

    self.obj12117=MT_pre__CompositionType(self)
    self.obj12117.isGraphObjectVisual = True

    if(hasattr(self.obj12117, '_setHierarchicalLink')):
      self.obj12117._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj12117.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj12117.MT_subtypeMatching__.setValue(('True', 0))
    self.obj12117.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj12117.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12117.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj12117.MT_pivotIn__.setValue('')
    self.obj12117.MT_pivotIn__.setNone()

    # MT_label__
    self.obj12117.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj12117.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12117.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj12117.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj12117.MT_pre__name.setHeight(15)

    self.obj12117.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(240.0,320.0,self.obj12117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj12117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj12117)
    self.globalAndLocalPostcondition(self.obj12117, rootNode)
    self.obj12117.postAction( rootNode.CREATE )

    # Connections for obj12114 (graphObject_: Obj51) of type LHS
    self.drawConnections(
 )
    # Connections for obj12115 (graphObject_: Obj52) of type MT_pre__SoftwareComposition
    self.drawConnections(
(self.obj12115,self.obj12116,[402.0, 193.0, 405.0, 293.0],"true", 2) )
    # Connections for obj12116 (graphObject_: Obj53) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj12116,self.obj12117,[405.0, 293.0, 408.0, 393.0],"true", 2) )
    # Connections for obj12117 (graphObject_: Obj54) of type MT_pre__CompositionType
    self.drawConnections(
 )

newfunction = M2ThenClausePart1Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
