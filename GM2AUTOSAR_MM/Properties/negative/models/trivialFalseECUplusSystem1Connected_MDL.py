"""
__trivialFalseECUplusSystem1Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct  3 12:13:48 2013
_________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from LHS import *
from graph_MT_pre__ECU import *
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

def trivialFalseECUplusSystem1Connected_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('trivialFalseECUplusSystem1Connected')
    # --- ASG attributes over ---


    self.obj1576=MT_pre__ECU(self)
    self.obj1576.isGraphObjectVisual = True

    if(hasattr(self.obj1576, '_setHierarchicalLink')):
      self.obj1576._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1576.MT_pivotOut__.setValue('')
    self.obj1576.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1576.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1576.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1576.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1576.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1576.MT_pivotIn__.setValue('')
    self.obj1576.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1576.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj1576.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1576.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1576.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1576.MT_pre__name.setHeight(15)

    self.obj1576.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(220.0,180.0,self.obj1576)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1576.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1576)
    self.globalAndLocalPostcondition(self.obj1576, rootNode)
    self.obj1576.postAction( rootNode.CREATE )

    self.obj1577=LHS(self)
    self.obj1577.isGraphObjectVisual = True

    if(hasattr(self.obj1577, '_setHierarchicalLink')):
      self.obj1577._setHierarchicalLink(False)

    # constraint
    self.obj1577.constraint.setValue('if PreNode(\'1\')[\'cardinality\']==\'+\' :\n    return True\nreturn False\n')
    self.obj1577.constraint.setHeight(15)

    self.obj1577.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,100.0,self.obj1577)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1577.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1577)
    self.globalAndLocalPostcondition(self.obj1577, rootNode)
    self.obj1577.postAction( rootNode.CREATE )

    # Connections for obj1576 (graphObject_: Obj23) of type MT_pre__ECU
    self.drawConnections(
 )
    # Connections for obj1577 (graphObject_: Obj24) of type LHS
    self.drawConnections(
 )

newfunction = trivialFalseECUplusSystem1Connected_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
