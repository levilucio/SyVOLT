"""
__test_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Nov 28 12:41:34 2013
__________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Male_S import *
from MT_pre__Female_S import *
from LHS import *
from graph_MT_pre__Station_S import *
from graph_MT_pre__Female_S import *
from graph_MT_pre__Male_S import *
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

def test_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('test')
    # --- ASG attributes over ---


    self.obj46=MT_pre__Station_S(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj46.MT_pivotOut__.setValue('')
    self.obj46.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj46.MT_subtypeMatching__.setValue(('True', 0))
    self.obj46.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj46.MT_pre__classtype.setValue('if attr_value == \'station1\':\n    return True\nelse:\n    return False\n')
    self.obj46.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj46.MT_pivotIn__.setValue('')
    self.obj46.MT_pivotIn__.setNone()

    # MT_label__
    self.obj46.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj46.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj46.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj46.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj46.MT_pre__name.setHeight(15)

    self.obj46.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(260.0,200.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj3109=MT_pre__Male_S(self)
    self.obj3109.isGraphObjectVisual = True

    if(hasattr(self.obj3109, '_setHierarchicalLink')):
      self.obj3109._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3109.MT_pivotOut__.setValue('')
    self.obj3109.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3109.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3109.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3109.MT_pre__classtype.setValue('if attr_value == \'male1\':\n    return True\nelse:\n    return False\n')
    self.obj3109.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3109.MT_pivotIn__.setValue('')
    self.obj3109.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3109.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj3109.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3109.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3109.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3109.MT_pre__name.setHeight(15)

    self.obj3109.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(360.0,320.0,self.obj3109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3109)
    self.globalAndLocalPostcondition(self.obj3109, rootNode)
    self.obj3109.postAction( rootNode.CREATE )

    self.obj3868=MT_pre__Female_S(self)
    self.obj3868.isGraphObjectVisual = True

    if(hasattr(self.obj3868, '_setHierarchicalLink')):
      self.obj3868._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3868.MT_pivotOut__.setValue('')
    self.obj3868.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3868.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3868.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3868.MT_pre__classtype.setValue('if attr_value == \'female1\':\n    return True\nelse:\n    return False\n')
    self.obj3868.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3868.MT_pivotIn__.setValue('')
    self.obj3868.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3868.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj3868.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3868.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3868.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3868.MT_pre__name.setHeight(15)

    self.obj3868.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(160.0,320.0,self.obj3868)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3868.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3868)
    self.globalAndLocalPostcondition(self.obj3868, rootNode)
    self.obj3868.postAction( rootNode.CREATE )

    self.obj49=LHS(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # constraint
    self.obj49.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj49.constraint.setHeight(15)

    self.obj49.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,120.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    # Connections for obj46 (graphObject_: Obj4) of type MT_pre__Station_S
    self.drawConnections(
 )
    # Connections for obj3109 (graphObject_: Obj10) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj3868 (graphObject_: Obj11) of type MT_pre__Female_S
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj7) of type LHS
    self.drawConnections(
 )

newfunction = test_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
