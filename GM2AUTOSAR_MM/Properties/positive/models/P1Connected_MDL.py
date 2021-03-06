"""
__P1Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Sep 16 17:32:40 2013
_________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ECU import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__ExecFrame import *
from MT_pre__Signal import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__ECU import *
from graph_LHS import *
from graph_MT_pre__ExecFrame import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__VirtualDevice import *
from graph_MT_pre__Signal import *
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

def P1Connected_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('P1Connected')
    # --- ASG attributes over ---


    self.obj61=MT_pre__ECU(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj61.MT_pivotOut__.setValue('')
    self.obj61.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj61.MT_subtypeMatching__.setValue(('True', 0))
    self.obj61.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj61.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj61.MT_pivotIn__.setValue('')
    self.obj61.MT_pivotIn__.setNone()

    # MT_label__
    self.obj61.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj61.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj61.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__name.setHeight(15)

    self.obj61.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(140.0,80.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=MT_pre__VirtualDevice(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj62.MT_pivotOut__.setValue('')
    self.obj62.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj62.MT_subtypeMatching__.setValue(('True', 0))
    self.obj62.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj62.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj62.MT_pivotIn__.setValue('')
    self.obj62.MT_pivotIn__.setNone()

    # MT_label__
    self.obj62.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj62.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj62.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__name.setHeight(15)

    self.obj62.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(340.0,80.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=MT_pre__Distributable(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63.MT_pivotOut__.setValue('')
    self.obj63.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63.MT_pivotIn__.setValue('')
    self.obj63.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj63.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj63.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__name.setHeight(15)

    self.obj63.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(340.0,211.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=MT_pre__ExecFrame(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj64.MT_pivotOut__.setValue('')
    self.obj64.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj64.MT_subtypeMatching__.setValue(('True', 0))
    self.obj64.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj64.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj64.MT_pivotIn__.setValue('')
    self.obj64.MT_pivotIn__.setNone()

    # MT_label__
    self.obj64.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj64.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj64.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__name.setHeight(15)

    self.obj64.graphClass_= graph_MT_pre__ExecFrame
    if self.genGraphics:
       new_obj = graph_MT_pre__ExecFrame(340.0,338.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=MT_pre__Signal(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj65.MT_pivotOut__.setValue('')
    self.obj65.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj65.MT_subtypeMatching__.setValue(('True', 0))
    self.obj65.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj65.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj65.MT_pivotIn__.setValue('')
    self.obj65.MT_pivotIn__.setNone()

    # MT_label__
    self.obj65.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj65.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj65.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__name.setHeight(15)

    self.obj65.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(140.0,337.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj68=MT_pre__directLink_S(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # MT_label__
    self.obj68.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj68.MT_pivotOut__.setValue('')
    self.obj68.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj68.MT_subtypeMatching__.setValue(('True', 0))
    self.obj68.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj68.MT_pivotIn__.setValue('')
    self.obj68.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj68.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__associationType.setHeight(15)

    self.obj68.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(410.0,154.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=MT_pre__directLink_S(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # MT_label__
    self.obj69.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj69.MT_pivotOut__.setValue('')
    self.obj69.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj69.MT_subtypeMatching__.setValue(('True', 0))
    self.obj69.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj69.MT_pivotIn__.setValue('')
    self.obj69.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj69.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj69.MT_pre__associationType.setHeight(15)

    self.obj69.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(510.0,219.5,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=MT_pre__directLink_S(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # MT_label__
    self.obj70.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj70.MT_pivotOut__.setValue('')
    self.obj70.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj70.MT_subtypeMatching__.setValue(('True', 0))
    self.obj70.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj70.MT_pivotIn__.setValue('')
    self.obj70.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj70.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj70.MT_pre__associationType.setHeight(15)

    self.obj70.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(510.0,348.5,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=MT_pre__directLink_S(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj71.MT_subtypeMatching__.setValue(('True', 0))
    self.obj71.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj71.MT_pivotIn__.setValue('')
    self.obj71.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj71.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj71.MT_pre__associationType.setHeight(15)

    self.obj71.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(410.0,411.5,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj60=LHS(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # constraint
    self.obj60.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif PreNode(\'1\')[\'cardinality\']==\'+\' and PreNode(\'2\')[\'cardinality\']==\'+\' and PreNode(\'3\')[\'cardinality\']==\'+\' and PreNode(\'4\')[\'cardinality\']==\'+\' and PreNode(\'5\')[\'cardinality\']==\'1\' and PreNode(\'6\')[\'associationType\']==\'virtualDevice\' and PreNode(\'7\')[\'associationType\']==\'distributable\' and PreNode(\'8\')[\'associationType\']==\'execFrame\' and PreNode(\'9\')[\'associationType\']==\'provided\':\n    return True\nreturn False\n')
    self.obj60.constraint.setHeight(15)

    self.obj60.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,60.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    # Connections for obj61 (graphObject_: Obj13) of type MT_pre__ECU
    self.drawConnections(
(self.obj61,self.obj68,[310.0, 154.0, 410.0, 154.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj14) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj62,self.obj69,[510.0, 154.0, 510.0, 219.5],"true", 2) )
    # Connections for obj63 (graphObject_: Obj15) of type MT_pre__Distributable
    self.drawConnections(
(self.obj63,self.obj70,[510.0, 285.0, 510.0, 348.5],"true", 2) )
    # Connections for obj64 (graphObject_: Obj16) of type MT_pre__ExecFrame
    self.drawConnections(
(self.obj64,self.obj71,[510.0, 412.0, 410.0, 411.5],"true", 2) )
    # Connections for obj65 (graphObject_: Obj17) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj18) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj68,self.obj62,[410.0, 154.0, 510.0, 154.0],"true", 2) )
    # Connections for obj69 (graphObject_: Obj19) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj69,self.obj63,[510.0, 219.5, 510.0, 285.0],"true", 2) )
    # Connections for obj70 (graphObject_: Obj20) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj70,self.obj64,[510.0, 348.5, 510.0, 412.0],"true", 2) )
    # Connections for obj71 (graphObject_: Obj21) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj71,self.obj65,[410.0, 411.5, 310.0, 411.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj12) of type LHS
    self.drawConnections(
 )

newfunction = P1Connected_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
