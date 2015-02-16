"""
__exitpoint2procdefparTrueNOATTR_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 14:20:53 2015
_____________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__State import *
from MT_pre__ProcDef import *
from MT_pre__Par import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from LHS import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Par import *
from graph_MT_pre__ProcDef import *
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

def exitpoint2procdefparTrueNOATTR_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('exitpoint2procdefparTrueNOATTR_Complete')
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


    self.obj21177=MT_pre__ExitPoint(self)
    self.obj21177.isGraphObjectVisual = True

    if(hasattr(self.obj21177, '_setHierarchicalLink')):
      self.obj21177._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21177.MT_pivotOut__.setValue('')
    self.obj21177.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21177.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21177.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21177.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21177.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21177.MT_pivotIn__.setValue('')
    self.obj21177.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21177.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj21177.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21177.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21177.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21177.MT_pre__name.setHeight(15)

    self.obj21177.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(280.0,180.0,self.obj21177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21177)
    self.globalAndLocalPostcondition(self.obj21177, rootNode)
    self.obj21177.postAction( rootNode.CREATE )

    self.obj21165=MT_pre__State(self)
    self.obj21165.isGraphObjectVisual = True

    if(hasattr(self.obj21165, '_setHierarchicalLink')):
      self.obj21165._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21165.MT_pivotOut__.setValue('')
    self.obj21165.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21165.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21165.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21165.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21165.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21165.MT_pivotIn__.setValue('')
    self.obj21165.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21165.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj21165.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21165.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21165.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21165.MT_pre__name.setHeight(15)

    self.obj21165.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(80.0,180.0,self.obj21165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21165)
    self.globalAndLocalPostcondition(self.obj21165, rootNode)
    self.obj21165.postAction( rootNode.CREATE )

    self.obj21178=MT_pre__ProcDef(self)
    self.obj21178.isGraphObjectVisual = True

    if(hasattr(self.obj21178, '_setHierarchicalLink')):
      self.obj21178._setHierarchicalLink(False)

    # MT_label__
    self.obj21178.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj21178.MT_pivotOut__.setValue('')
    self.obj21178.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21178.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21178.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21178.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21178.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21178.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21178.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21178.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21178.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21178.MT_pivotIn__.setValue('')
    self.obj21178.MT_pivotIn__.setNone()

    self.obj21178.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(73.0,300.0,self.obj21178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21178)
    self.globalAndLocalPostcondition(self.obj21178, rootNode)
    self.obj21178.postAction( rootNode.CREATE )

    self.obj21166=MT_pre__Par(self)
    self.obj21166.isGraphObjectVisual = True

    if(hasattr(self.obj21166, '_setHierarchicalLink')):
      self.obj21166._setHierarchicalLink(False)

    # MT_label__
    self.obj21166.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj21166.MT_pivotOut__.setValue('')
    self.obj21166.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21166.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21166.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21166.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21166.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21166.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21166.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21166.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21166.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21166.MT_pivotIn__.setValue('')
    self.obj21166.MT_pivotIn__.setNone()

    self.obj21166.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(256.0,278.0,self.obj21166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21166)
    self.globalAndLocalPostcondition(self.obj21166, rootNode)
    self.obj21166.postAction( rootNode.CREATE )

    self.obj21173=MT_pre__directLink_T(self)
    self.obj21173.isGraphObjectVisual = True

    if(hasattr(self.obj21173, '_setHierarchicalLink')):
      self.obj21173._setHierarchicalLink(False)

    # MT_label__
    self.obj21173.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj21173.MT_pivotOut__.setValue('')
    self.obj21173.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21173.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21173.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21173.MT_pivotIn__.setValue('')
    self.obj21173.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21173.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21173.MT_pre__associationType.setHeight(15)

    self.obj21173.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(387.0,381.0,self.obj21173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21173)
    self.globalAndLocalPostcondition(self.obj21173, rootNode)
    self.obj21173.postAction( rootNode.CREATE )

    self.obj21172=MT_pre__directLink_S(self)
    self.obj21172.isGraphObjectVisual = True

    if(hasattr(self.obj21172, '_setHierarchicalLink')):
      self.obj21172._setHierarchicalLink(False)

    # MT_label__
    self.obj21172.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj21172.MT_pivotOut__.setValue('')
    self.obj21172.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21172.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21172.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21172.MT_pivotIn__.setValue('')
    self.obj21172.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21172.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21172.MT_pre__associationType.setHeight(15)

    self.obj21172.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(299.0,257.0,self.obj21172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21172)
    self.globalAndLocalPostcondition(self.obj21172, rootNode)
    self.obj21172.postAction( rootNode.CREATE )

    self.obj21168=MT_pre__trace_link(self)
    self.obj21168.isGraphObjectVisual = True

    if(hasattr(self.obj21168, '_setHierarchicalLink')):
      self.obj21168._setHierarchicalLink(False)

    # MT_label__
    self.obj21168.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj21168.MT_pivotOut__.setValue('')
    self.obj21168.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21168.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21168.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21168.MT_pivotIn__.setValue('')
    self.obj21168.MT_pivotIn__.setNone()

    self.obj21168.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(387.0,328.0,self.obj21168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21168)
    self.globalAndLocalPostcondition(self.obj21168, rootNode)
    self.obj21168.postAction( rootNode.CREATE )

    self.obj21169=MT_pre__trace_link(self)
    self.obj21169.isGraphObjectVisual = True

    if(hasattr(self.obj21169, '_setHierarchicalLink')):
      self.obj21169._setHierarchicalLink(False)

    # MT_label__
    self.obj21169.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj21169.MT_pivotOut__.setValue('')
    self.obj21169.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21169.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21169.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21169.MT_pivotIn__.setValue('')
    self.obj21169.MT_pivotIn__.setNone()

    self.obj21169.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(287.0,328.0,self.obj21169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21169)
    self.globalAndLocalPostcondition(self.obj21169, rootNode)
    self.obj21169.postAction( rootNode.CREATE )

    self.obj21170=MT_pre__trace_link(self)
    self.obj21170.isGraphObjectVisual = True

    if(hasattr(self.obj21170, '_setHierarchicalLink')):
      self.obj21170._setHierarchicalLink(False)

    # MT_label__
    self.obj21170.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj21170.MT_pivotOut__.setValue('')
    self.obj21170.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21170.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21170.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21170.MT_pivotIn__.setValue('')
    self.obj21170.MT_pivotIn__.setNone()

    self.obj21170.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(477.0,308.0,self.obj21170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21170)
    self.globalAndLocalPostcondition(self.obj21170, rootNode)
    self.obj21170.postAction( rootNode.CREATE )

    self.obj21171=MT_pre__trace_link(self)
    self.obj21171.isGraphObjectVisual = True

    if(hasattr(self.obj21171, '_setHierarchicalLink')):
      self.obj21171._setHierarchicalLink(False)

    # MT_label__
    self.obj21171.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj21171.MT_pivotOut__.setValue('')
    self.obj21171.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21171.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21171.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21171.MT_pivotIn__.setValue('')
    self.obj21171.MT_pivotIn__.setNone()

    self.obj21171.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(377.0,308.0,self.obj21171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21171)
    self.globalAndLocalPostcondition(self.obj21171, rootNode)
    self.obj21171.postAction( rootNode.CREATE )

    self.obj21164=LHS(self)
    self.obj21164.isGraphObjectVisual = True

    if(hasattr(self.obj21164, '_setHierarchicalLink')):
      self.obj21164._setHierarchicalLink(False)

    # constraint
    self.obj21164.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj21164.constraint.setHeight(15)

    self.obj21164.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj21164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21164)
    self.globalAndLocalPostcondition(self.obj21164, rootNode)
    self.obj21164.postAction( rootNode.CREATE )

    # Connections for obj21177 (graphObject_: Obj32) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj21165 (graphObject_: Obj20) of type MT_pre__State
    self.drawConnections(
(self.obj21165,self.obj21172,[277.0, 255.0, 299.0, 257.0],"true", 2) )
    # Connections for obj21178 (graphObject_: Obj33) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj21178,self.obj21173,[290.0, 401.0, 387.0, 381.0],"true", 2),
(self.obj21178,self.obj21168,[290.0, 401.0, 387.0, 328.0],"true", 2),
(self.obj21178,self.obj21169,[290.0, 401.0, 287.0, 328.0],"true", 2) )
    # Connections for obj21166 (graphObject_: Obj21) of type MT_pre__Par
    self.drawConnections(
(self.obj21166,self.obj21170,[473.0, 379.0, 477.0, 308.0],"true", 2),
(self.obj21166,self.obj21171,[473.0, 379.0, 377.0, 308.0],"true", 2) )
    # Connections for obj21173 (graphObject_: Obj28) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21173,self.obj21166,[387.0, 381.0, 473.0, 379.0],"true", 2) )
    # Connections for obj21172 (graphObject_: Obj27) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj21172,self.obj21177,[299.0, 257.0, 477.0, 255.0],"true", 2) )
    # Connections for obj21168 (graphObject_: Obj23) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21168,self.obj21177,[387.0, 328.0, 477.0, 255.0],"true", 2) )
    # Connections for obj21169 (graphObject_: Obj24) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21169,self.obj21165,[287.0, 328.0, 277.0, 255.0],"true", 2) )
    # Connections for obj21170 (graphObject_: Obj25) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21170,self.obj21177,[477.0, 308.0, 477.0, 255.0],"true", 2) )
    # Connections for obj21171 (graphObject_: Obj26) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21171,self.obj21165,[377.0, 308.0, 277.0, 255.0],"true", 2) )
    # Connections for obj21164 (graphObject_: Obj19) of type LHS
    self.drawConnections(
 )

newfunction = exitpoint2procdefparTrueNOATTR_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
