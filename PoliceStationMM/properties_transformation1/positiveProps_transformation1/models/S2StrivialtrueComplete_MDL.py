"""
__S2StrivialtrueComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Jan 26 16:41:34 2015
____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Station_T import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__Station_S import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Station_T import *
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

def S2StrivialtrueComplete_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('S2StrivialtrueComplete')
    # --- ASG attributes over ---


    self.obj45=MT_pre__Station_S(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj45.MT_pivotOut__.setValue('')
    self.obj45.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj45.MT_subtypeMatching__.setValue(('True', 0))
    self.obj45.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj45.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj45.MT_pivotIn__.setValue('')
    self.obj45.MT_pivotIn__.setNone()

    # MT_label__
    self.obj45.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj45.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj45.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__name.setHeight(15)

    self.obj45.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(140.0,100.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj4498=MT_pre__Station_T(self)
    self.obj4498.isGraphObjectVisual = True

    if(hasattr(self.obj4498, '_setHierarchicalLink')):
      self.obj4498._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj4498.MT_pivotOut__.setValue('')
    self.obj4498.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4498.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4498.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj4498.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4498.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj4498.MT_pivotIn__.setValue('')
    self.obj4498.MT_pivotIn__.setNone()

    # MT_label__
    self.obj4498.MT_label__.setValue('2')

    # MT_pre__name
    self.obj4498.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj4498.MT_pre__name.setHeight(15)

    self.obj4498.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(140.0,300.0,self.obj4498)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj4498.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4498)
    self.globalAndLocalPostcondition(self.obj4498, rootNode)
    self.obj4498.postAction( rootNode.CREATE )

    self.obj4499=MT_pre__trace_link(self)
    self.obj4499.isGraphObjectVisual = True

    if(hasattr(self.obj4499, '_setHierarchicalLink')):
      self.obj4499._setHierarchicalLink(False)

    # MT_label__
    self.obj4499.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj4499.MT_pivotOut__.setValue('')
    self.obj4499.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4499.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4499.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4499.MT_pivotIn__.setValue('')
    self.obj4499.MT_pivotIn__.setNone()

    self.obj4499.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(201.0,241.0,self.obj4499)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4499.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4499)
    self.globalAndLocalPostcondition(self.obj4499, rootNode)
    self.obj4499.postAction( rootNode.CREATE )

    self.obj44=LHS(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # constraint
    self.obj44.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj44.constraint.setHeight(15)

    self.obj44.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,60.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    # Connections for obj45 (graphObject_: Obj1) of type MT_pre__Station_S
    self.drawConnections(
 )
    # Connections for obj4498 (graphObject_: Obj2) of type MT_pre__Station_T
    self.drawConnections(
(self.obj4498,self.obj4499,[201.0, 341.0, 201.0, 241.0],"true", 2) )
    # Connections for obj4499 (graphObject_: Obj3) of type MT_pre__trace_link
    self.drawConnections(
(self.obj4499,self.obj45,[201.0, 241.0, 201.0, 141.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = S2StrivialtrueComplete_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
