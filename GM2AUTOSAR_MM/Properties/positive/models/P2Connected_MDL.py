"""
__P2Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Tue Sep 17 13:41:35 2013
_________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__directLink_S import *
from MT_pre__ECU import *
from MT_pre__ExecFrame import *
from MT_pre__Signal import *
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

def P2Connected_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('P2Connected')
    # --- ASG attributes over ---


    self.obj1544=LHS(self)
    self.obj1544.isGraphObjectVisual = True

    if(hasattr(self.obj1544, '_setHierarchicalLink')):
      self.obj1544._setHierarchicalLink(False)

    # constraint
    self.obj1544.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif PreNode(\'1\')[\'cardinality\']==\'+\' and PreNode(\'2\')[\'cardinality\']==\'+\' and PreNode(\'3\')[\'cardinality\']==\'+\' and PreNode(\'4\')[\'cardinality\']==\'+\' and PreNode(\'5\')[\'cardinality\']==\'1\' and PreNode(\'6\')[\'associationType\']==\'virtualDevice\' and PreNode(\'7\')[\'associationType\']==\'distributable\' and PreNode(\'8\')[\'associationType\']==\'execFrame\' and PreNode(\'9\')[\'associationType\']==\'required\':\n    return True\nreturn False\n')
    self.obj1544.constraint.setHeight(15)

    self.obj1544.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,60.0,self.obj1544)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1544.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1544)
    self.globalAndLocalPostcondition(self.obj1544, rootNode)
    self.obj1544.postAction( rootNode.CREATE )

    self.obj1546=MT_pre__VirtualDevice(self)
    self.obj1546.isGraphObjectVisual = True

    if(hasattr(self.obj1546, '_setHierarchicalLink')):
      self.obj1546._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1546.MT_pivotOut__.setValue('')
    self.obj1546.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1546.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1546.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1546.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1546.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1546.MT_pivotIn__.setValue('')
    self.obj1546.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1546.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj1546.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1546.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1546.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1546.MT_pre__name.setHeight(15)

    self.obj1546.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(320.0,80.0,self.obj1546)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1546.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1546)
    self.globalAndLocalPostcondition(self.obj1546, rootNode)
    self.obj1546.postAction( rootNode.CREATE )

    self.obj1547=MT_pre__Distributable(self)
    self.obj1547.isGraphObjectVisual = True

    if(hasattr(self.obj1547, '_setHierarchicalLink')):
      self.obj1547._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1547.MT_pivotOut__.setValue('')
    self.obj1547.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1547.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1547.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1547.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1547.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1547.MT_pivotIn__.setValue('')
    self.obj1547.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1547.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj1547.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1547.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1547.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1547.MT_pre__name.setHeight(15)

    self.obj1547.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(320.0,215.0,self.obj1547)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1547.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1547)
    self.globalAndLocalPostcondition(self.obj1547, rootNode)
    self.obj1547.postAction( rootNode.CREATE )

    self.obj1550=MT_pre__directLink_S(self)
    self.obj1550.isGraphObjectVisual = True

    if(hasattr(self.obj1550, '_setHierarchicalLink')):
      self.obj1550._setHierarchicalLink(False)

    # MT_label__
    self.obj1550.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj1550.MT_pivotOut__.setValue('')
    self.obj1550.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1550.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1550.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1550.MT_pivotIn__.setValue('')
    self.obj1550.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1550.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1550.MT_pre__associationType.setHeight(15)

    self.obj1550.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(390.0,154.0,self.obj1550)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1550.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1550)
    self.globalAndLocalPostcondition(self.obj1550, rootNode)
    self.obj1550.postAction( rootNode.CREATE )

    self.obj1551=MT_pre__directLink_S(self)
    self.obj1551.isGraphObjectVisual = True

    if(hasattr(self.obj1551, '_setHierarchicalLink')):
      self.obj1551._setHierarchicalLink(False)

    # MT_label__
    self.obj1551.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj1551.MT_pivotOut__.setValue('')
    self.obj1551.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1551.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1551.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1551.MT_pivotIn__.setValue('')
    self.obj1551.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1551.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1551.MT_pre__associationType.setHeight(15)

    self.obj1551.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,221.5,self.obj1551)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1551.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1551)
    self.globalAndLocalPostcondition(self.obj1551, rootNode)
    self.obj1551.postAction( rootNode.CREATE )

    self.obj1552=MT_pre__directLink_S(self)
    self.obj1552.isGraphObjectVisual = True

    if(hasattr(self.obj1552, '_setHierarchicalLink')):
      self.obj1552._setHierarchicalLink(False)

    # MT_label__
    self.obj1552.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj1552.MT_pivotOut__.setValue('')
    self.obj1552.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1552.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1552.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1552.MT_pivotIn__.setValue('')
    self.obj1552.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1552.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1552.MT_pre__associationType.setHeight(15)

    self.obj1552.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,351.5,self.obj1552)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1552.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1552)
    self.globalAndLocalPostcondition(self.obj1552, rootNode)
    self.obj1552.postAction( rootNode.CREATE )

    self.obj1553=MT_pre__directLink_S(self)
    self.obj1553.isGraphObjectVisual = True

    if(hasattr(self.obj1553, '_setHierarchicalLink')):
      self.obj1553._setHierarchicalLink(False)

    # MT_label__
    self.obj1553.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj1553.MT_pivotOut__.setValue('')
    self.obj1553.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1553.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1553.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj1553.MT_pivotIn__.setValue('')
    self.obj1553.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj1553.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1553.MT_pre__associationType.setHeight(15)

    self.obj1553.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(390.0,414.0,self.obj1553)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1553.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1553)
    self.globalAndLocalPostcondition(self.obj1553, rootNode)
    self.obj1553.postAction( rootNode.CREATE )

    self.obj1545=MT_pre__ECU(self)
    self.obj1545.isGraphObjectVisual = True

    if(hasattr(self.obj1545, '_setHierarchicalLink')):
      self.obj1545._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1545.MT_pivotOut__.setValue('')
    self.obj1545.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1545.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1545.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1545.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1545.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1545.MT_pivotIn__.setValue('')
    self.obj1545.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1545.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj1545.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1545.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1545.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1545.MT_pre__name.setHeight(15)

    self.obj1545.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(120.0,80.0,self.obj1545)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1545.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1545)
    self.globalAndLocalPostcondition(self.obj1545, rootNode)
    self.obj1545.postAction( rootNode.CREATE )

    self.obj1548=MT_pre__ExecFrame(self)
    self.obj1548.isGraphObjectVisual = True

    if(hasattr(self.obj1548, '_setHierarchicalLink')):
      self.obj1548._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1548.MT_pivotOut__.setValue('')
    self.obj1548.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1548.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1548.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1548.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1548.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1548.MT_pivotIn__.setValue('')
    self.obj1548.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1548.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj1548.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1548.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1548.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1548.MT_pre__name.setHeight(15)

    self.obj1548.graphClass_= graph_MT_pre__ExecFrame
    if self.genGraphics:
       new_obj = graph_MT_pre__ExecFrame(320.0,340.0,self.obj1548)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1548.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1548)
    self.globalAndLocalPostcondition(self.obj1548, rootNode)
    self.obj1548.postAction( rootNode.CREATE )

    self.obj1549=MT_pre__Signal(self)
    self.obj1549.isGraphObjectVisual = True

    if(hasattr(self.obj1549, '_setHierarchicalLink')):
      self.obj1549._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj1549.MT_pivotOut__.setValue('')
    self.obj1549.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj1549.MT_subtypeMatching__.setValue(('True', 0))
    self.obj1549.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj1549.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1549.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj1549.MT_pivotIn__.setValue('')
    self.obj1549.MT_pivotIn__.setNone()

    # MT_label__
    self.obj1549.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj1549.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1549.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj1549.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj1549.MT_pre__name.setHeight(15)

    self.obj1549.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(120.0,340.0,self.obj1549)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1549.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1549)
    self.globalAndLocalPostcondition(self.obj1549, rootNode)
    self.obj1549.postAction( rootNode.CREATE )

    # Connections for obj1544 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )
    # Connections for obj1546 (graphObject_: Obj8) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj1546,self.obj1551,[490.0, 154.0, 490.0, 221.5],"true", 2) )
    # Connections for obj1547 (graphObject_: Obj9) of type MT_pre__Distributable
    self.drawConnections(
(self.obj1547,self.obj1552,[490.0, 289.0, 490.0, 351.5],"true", 2) )
    # Connections for obj1550 (graphObject_: Obj12) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1550,self.obj1546,[390.0, 154.0, 490.0, 154.0],"true", 2) )
    # Connections for obj1551 (graphObject_: Obj13) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1551,self.obj1547,[490.0, 221.5, 490.0, 289.0],"true", 2) )
    # Connections for obj1552 (graphObject_: Obj14) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1552,self.obj1548,[490.0, 351.5, 490.0, 414.0],"true", 2) )
    # Connections for obj1553 (graphObject_: Obj15) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj1553,self.obj1549,[390.0, 414.0, 290.0, 414.0],"true", 2) )
    # Connections for obj1545 (graphObject_: Obj7) of type MT_pre__ECU
    self.drawConnections(
(self.obj1545,self.obj1550,[290.0, 154.0, 390.0, 154.0],"true", 2) )
    # Connections for obj1548 (graphObject_: Obj10) of type MT_pre__ExecFrame
    self.drawConnections(
(self.obj1548,self.obj1553,[490.0, 414.0, 390.0, 414.0],"true", 2) )
    # Connections for obj1549 (graphObject_: Obj11) of type MT_pre__Signal
    self.drawConnections(
 )

newfunction = P2Connected_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
