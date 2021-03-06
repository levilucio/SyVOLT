"""
__M5IfClauseComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct 24 14:20:45 2013
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__System import *
from graph_MT_pre__System import *
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

def M5IfClauseComplete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('M5IfClauseComplete')
    # --- ASG attributes over ---


    self.obj8960=LHS(self)
    self.obj8960.isGraphObjectVisual = True

    if(hasattr(self.obj8960, '_setHierarchicalLink')):
      self.obj8960._setHierarchicalLink(False)

    # constraint
    self.obj8960.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj8960.constraint.setHeight(15)

    self.obj8960.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj8960)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj8960.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8960)
    self.globalAndLocalPostcondition(self.obj8960, rootNode)
    self.obj8960.postAction( rootNode.CREATE )

    self.obj8961=MT_pre__System(self)
    self.obj8961.isGraphObjectVisual = True

    if(hasattr(self.obj8961, '_setHierarchicalLink')):
      self.obj8961._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj8961.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj8961.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8961.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj8961.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8961.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj8961.MT_pivotIn__.setValue('')
    self.obj8961.MT_pivotIn__.setNone()

    # MT_label__
    self.obj8961.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj8961.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8961.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj8961.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj8961.MT_pre__name.setHeight(15)

    self.obj8961.graphClass_= graph_MT_pre__System
    if self.genGraphics:
       new_obj = graph_MT_pre__System(120.0,140.0,self.obj8961)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__System", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj8961.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8961)
    self.globalAndLocalPostcondition(self.obj8961, rootNode)
    self.obj8961.postAction( rootNode.CREATE )

    # Connections for obj8960 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )
    # Connections for obj8961 (graphObject_: Obj7) of type MT_pre__System
    self.drawConnections(
 )

newfunction = M5IfClauseComplete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
