"""
__M2IfClauseComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 10:50:50 2013
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__SoftwareComposition import *
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

def M2IfClauseComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M2IfClauseComplete')
    # --- ASG attributes over ---


    self.obj7559=LHS(self)
    self.obj7559.isGraphObjectVisual = True

    if(hasattr(self.obj7559, '_setHierarchicalLink')):
      self.obj7559._setHierarchicalLink(False)

    # constraint
    self.obj7559.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj7559.constraint.setHeight(15)

    self.obj7559.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,60.0,self.obj7559)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj7559.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj7559)
    self.globalAndLocalPostcondition(self.obj7559, rootNode)
    self.obj7559.postAction( rootNode.CREATE )

    self.obj7560=MT_pre__SoftwareComposition(self)
    self.obj7560.isGraphObjectVisual = True

    if(hasattr(self.obj7560, '_setHierarchicalLink')):
      self.obj7560._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj7560.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj7560.MT_subtypeMatching__.setValue(('True', 0))
    self.obj7560.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj7560.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj7560.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj7560.MT_pivotIn__.setValue('')
    self.obj7560.MT_pivotIn__.setNone()

    # MT_label__
    self.obj7560.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj7560.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj7560.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj7560.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj7560.MT_pre__name.setHeight(15)

    self.obj7560.graphClass_= graph_MT_pre__SoftwareComposition
    if self.genGraphics:
       new_obj = graph_MT_pre__SoftwareComposition(140.0,120.0,self.obj7560)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SoftwareComposition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj7560.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj7560)
    self.globalAndLocalPostcondition(self.obj7560, rootNode)
    self.obj7560.postAction( rootNode.CREATE )

    # Connections for obj7559 (graphObject_: Obj23) of type LHS
    self.drawConnections(
 )
    # Connections for obj7560 (graphObject_: Obj24) of type MT_pre__SoftwareComposition
    self.drawConnections(
 )

newfunction = M2IfClauseComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
