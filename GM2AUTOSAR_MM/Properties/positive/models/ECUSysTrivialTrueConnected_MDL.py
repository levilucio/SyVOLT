"""
__ECUSysTrivialTrueConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Sep  9 21:27:45 2013
________________________________________________________________________________________
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

def ECUSysTrivialTrueConnected_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ECUSysTrivialTrueConnected')
    # --- ASG attributes over ---


    self.obj4963=MT_pre__ECU(self)
    self.obj4963.isGraphObjectVisual = True

    if(hasattr(self.obj4963, '_setHierarchicalLink')):
      self.obj4963._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4963.MT_pivotOut__.setValue('')
    self.obj4963.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4963.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4963.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4963.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4963.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4963.MT_pivotIn__.setValue('')
    self.obj4963.MT_pivotIn__.setNone()

    # MT_label__
    self.obj4963.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj4963.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4963.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj4963.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4963.MT_pre__name.setHeight(15)

    self.obj4963.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(180.0,140.0,self.obj4963)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4963.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4963)
    self.globalAndLocalPostcondition(self.obj4963, rootNode)
    self.obj4963.postAction( rootNode.CREATE )

    self.obj4964=LHS(self)
    self.obj4964.isGraphObjectVisual = True

    if(hasattr(self.obj4964, '_setHierarchicalLink')):
      self.obj4964._setHierarchicalLink(False)

    # constraint
    self.obj4964.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\nif PreNode(\'1\')[\'cardinality\']==\'+\':\n    return True\nreturn False\n')
    self.obj4964.constraint.setHeight(15)

    self.obj4964.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,100.0,self.obj4964)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4964.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4964)
    self.globalAndLocalPostcondition(self.obj4964, rootNode)
    self.obj4964.postAction( rootNode.CREATE )

    # Connections for obj4963 (graphObject_: Obj124) of type MT_pre__ECU
    self.drawConnections(
 )
    # Connections for obj4964 (graphObject_: Obj125) of type LHS
    self.drawConnections(
 )

newfunction = ECUSysTrivialTrueConnected_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
