"""
__SM2SM_trace_check_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 10:19:12 2014
_______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Male_S import *
from MT_pre__Station_T import *
from MT_pre__Male_T import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__Male_T import *
from graph_MT_pre__Male_S import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Station_S import *
from graph_MT_pre__Station_T import *
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

def SM2SM_trace_check_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__PoliceStationMM ---
    if( MT_pre__PoliceStationMMRootNode ): 
        # author
        MT_pre__PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__PoliceStationMMRootNode.description.setValue('\n')
        MT_pre__PoliceStationMMRootNode.description.setHeight(15)

        # name
        MT_pre__PoliceStationMMRootNode.name.setValue('')
        MT_pre__PoliceStationMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('SM2SM_trace_check')
    # --- ASG attributes over ---


    self.obj67=MT_pre__Station_S(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj67.MT_pivotOut__.setValue('')
    self.obj67.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj67.MT_subtypeMatching__.setValue(('True', 0))
    self.obj67.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj67.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj67.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj67.MT_pivotIn__.setValue('')
    self.obj67.MT_pivotIn__.setNone()

    # MT_label__
    self.obj67.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj67.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj67.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj67.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj67.MT_pre__name.setHeight(15)

    self.obj67.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(600.0,220.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=MT_pre__Male_S(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj68.MT_pivotOut__.setValue('')
    self.obj68.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj68.MT_subtypeMatching__.setValue(('True', 0))
    self.obj68.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj68.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj68.MT_pivotIn__.setValue('')
    self.obj68.MT_pivotIn__.setNone()

    # MT_label__
    self.obj68.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj68.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj68.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__name.setHeight(15)

    self.obj68.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(780.0,220.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj76=MT_pre__Station_T(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj76.MT_subtypeMatching__.setValue(('True', 0))
    self.obj76.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj76.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj76.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj76.MT_pivotIn__.setValue('')
    self.obj76.MT_pivotIn__.setNone()

    # MT_label__
    self.obj76.MT_label__.setValue('4')

    # MT_pre__name
    self.obj76.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj76.MT_pre__name.setHeight(15)

    self.obj76.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(600.0,400.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=MT_pre__Male_T(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj77.MT_subtypeMatching__.setValue(('True', 0))
    self.obj77.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj77.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj77.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj77.MT_pivotIn__.setValue('')
    self.obj77.MT_pivotIn__.setNone()

    # MT_label__
    self.obj77.MT_label__.setValue('5')

    # MT_pre__name
    self.obj77.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj77.MT_pre__name.setHeight(15)

    self.obj77.graphClass_= graph_MT_pre__Male_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_T(780.0,400.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj80=MT_pre__trace_link(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # MT_label__
    self.obj80.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj80.MT_pivotOut__.setValue('')
    self.obj80.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj80.MT_subtypeMatching__.setValue(('True', 0))
    self.obj80.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj80.MT_pivotIn__.setValue('')
    self.obj80.MT_pivotIn__.setNone()

    self.obj80.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(661.0,351.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=MT_pre__trace_link(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj81.MT_subtypeMatching__.setValue(('True', 0))
    self.obj81.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj81.MT_pivotIn__.setValue('')
    self.obj81.MT_pivotIn__.setNone()

    self.obj81.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(841.0,351.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj66=LHS(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # constraint
    self.obj66.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj66.constraint.setHeight(15)

    self.obj66.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(560.0,160.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    # Connections for obj67 (graphObject_: Obj5) of type MT_pre__Station_S
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj6) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj76 (graphObject_: Obj10) of type MT_pre__Station_T
    self.drawConnections(
(self.obj76,self.obj80,[661.0, 441.0, 661.0, 351.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj11) of type MT_pre__Male_T
    self.drawConnections(
(self.obj77,self.obj81,[841.0, 441.0, 841.0, 351.0],"true", 2) )
    # Connections for obj80 (graphObject_: Obj12) of type MT_pre__trace_link
    self.drawConnections(
(self.obj80,self.obj67,[661.0, 351.0, 661.0, 261.0],"true", 2) )
    # Connections for obj81 (graphObject_: Obj13) of type MT_pre__trace_link
    self.drawConnections(
(self.obj81,self.obj68,[841.0, 351.0, 841.0, 261.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )

newfunction = SM2SM_trace_check_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
