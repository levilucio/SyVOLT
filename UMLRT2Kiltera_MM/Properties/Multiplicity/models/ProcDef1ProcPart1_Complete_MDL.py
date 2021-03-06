"""
__ProcDef1ProcPart1_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Mar  4 23:16:41 2015
________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ProcDef import *
from LHS import *
from graph_MT_pre__ProcDef import *
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

def ProcDef1ProcPart1_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ProcDef1ProcPart1_Complete')
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MT_pre__UMLRT2Kiltera_MM ---
    if( MT_pre__UMLRT2Kiltera_MMRootNode ): 
        # author
        MT_pre__UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setValue('')
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj42206=MT_pre__ProcDef(self)
    self.obj42206.isGraphObjectVisual = True

    if(hasattr(self.obj42206, '_setHierarchicalLink')):
      self.obj42206._setHierarchicalLink(False)

    # MT_label__
    self.obj42206.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj42206.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj42206.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42206.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42206.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42206.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj42206.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42206.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42206.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42206.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj42206.MT_pivotIn__.setValue('')
    self.obj42206.MT_pivotIn__.setNone()

    self.obj42206.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(120.0,60.0,self.obj42206)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42206.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42206)
    self.globalAndLocalPostcondition(self.obj42206, rootNode)
    self.obj42206.postAction( rootNode.CREATE )

    self.obj42205=LHS(self)
    self.obj42205.isGraphObjectVisual = True

    if(hasattr(self.obj42205, '_setHierarchicalLink')):
      self.obj42205._setHierarchicalLink(False)

    # constraint
    self.obj42205.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj42205.constraint.setHeight(15)

    self.obj42205.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj42205)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42205.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42205)
    self.globalAndLocalPostcondition(self.obj42205, rootNode)
    self.obj42205.postAction( rootNode.CREATE )

    # Connections for obj42206 (graphObject_: Obj7) of type MT_pre__ProcDef
    self.drawConnections(
 )
    # Connections for obj42205 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )

newfunction = ProcDef1ProcPart1_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
