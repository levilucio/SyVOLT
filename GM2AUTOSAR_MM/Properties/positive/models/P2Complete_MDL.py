"""
__P2Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Tue Sep 17 13:53:36 2013
________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__VirtualDevice import *
from MT_pre__Distributable import *
from MT_pre__trace_link import *
from MT_pre__directLink_S import *
from MT_pre__directLink_T import *
from MT_pre__RPortPrototype import *
from MT_pre__ECU import *
from MT_pre__CompositionType import *
from MT_pre__ExecFrame import *
from MT_pre__Signal import *
from graph_MT_pre__ECU import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__ExecFrame import *
from graph_MT_pre__Distributable import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__RPortPrototype import *
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

def P2Complete_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('P2Complete')
    # --- ASG attributes over ---


    self.obj3048=LHS(self)
    self.obj3048.isGraphObjectVisual = True

    if(hasattr(self.obj3048, '_setHierarchicalLink')):
      self.obj3048._setHierarchicalLink(False)

    # constraint
    self.obj3048.constraint.setValue('if PreNode(\'1\')[\'cardinality\']==\'+\' and PreNode(\'2\')[\'cardinality\']==\'+\' and PreNode(\'3\')[\'cardinality\']==\'+\' and PreNode(\'4\')[\'cardinality\']==\'+\' and PreNode(\'5\')[\'cardinality\']==\'1\' and PreNode(\'10\')[\'cardinality\']==\'+\' and PreNode(\'11\')[\'cardinality\']==\'+\' and PreNode(\'6\')[\'associationType\']==\'virtualDevice\' and PreNode(\'7\')[\'associationType\']==\'distributable\' and PreNode(\'8\')[\'associationType\']==\'execFrame\' and PreNode(\'9\')[\'associationType\']==\'required\' and PreNode(\'12\')[\'associationType\']==\'port\':\n    return True\nreturn False\n')
    self.obj3048.constraint.setHeight(15)

    self.obj3048.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj3048)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3048.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3048)
    self.globalAndLocalPostcondition(self.obj3048, rootNode)
    self.obj3048.postAction( rootNode.CREATE )

    self.obj3050=MT_pre__VirtualDevice(self)
    self.obj3050.isGraphObjectVisual = True

    if(hasattr(self.obj3050, '_setHierarchicalLink')):
      self.obj3050._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3050.MT_pivotOut__.setValue('')
    self.obj3050.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3050.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3050.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3050.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3050.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3050.MT_pivotIn__.setValue('')
    self.obj3050.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3050.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj3050.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3050.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3050.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3050.MT_pre__name.setHeight(15)

    self.obj3050.graphClass_= graph_MT_pre__VirtualDevice
    if self.genGraphics:
       new_obj = graph_MT_pre__VirtualDevice(281.0,73.0,self.obj3050)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__VirtualDevice", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3050.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3050)
    self.globalAndLocalPostcondition(self.obj3050, rootNode)
    self.obj3050.postAction( rootNode.CREATE )

    self.obj3051=MT_pre__Distributable(self)
    self.obj3051.isGraphObjectVisual = True

    if(hasattr(self.obj3051, '_setHierarchicalLink')):
      self.obj3051._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3051.MT_pivotOut__.setValue('')
    self.obj3051.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3051.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3051.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3051.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3051.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3051.MT_pivotIn__.setValue('')
    self.obj3051.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3051.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj3051.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3051.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3051.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3051.MT_pre__name.setHeight(15)

    self.obj3051.graphClass_= graph_MT_pre__Distributable
    if self.genGraphics:
       new_obj = graph_MT_pre__Distributable(351.0,205.0,self.obj3051)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Distributable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3051.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3051)
    self.globalAndLocalPostcondition(self.obj3051, rootNode)
    self.obj3051.postAction( rootNode.CREATE )

    self.obj3061=MT_pre__trace_link(self)
    self.obj3061.isGraphObjectVisual = True

    if(hasattr(self.obj3061, '_setHierarchicalLink')):
      self.obj3061._setHierarchicalLink(False)

    # MT_label__
    self.obj3061.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj3061.MT_pivotOut__.setValue('')
    self.obj3061.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3061.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3061.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3061.MT_pivotIn__.setValue('')
    self.obj3061.MT_pivotIn__.setNone()

    self.obj3061.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(247.0,190.0,self.obj3061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3061)
    self.globalAndLocalPostcondition(self.obj3061, rootNode)
    self.obj3061.postAction( rootNode.CREATE )

    self.obj3062=MT_pre__trace_link(self)
    self.obj3062.isGraphObjectVisual = True

    if(hasattr(self.obj3062, '_setHierarchicalLink')):
      self.obj3062._setHierarchicalLink(False)

    # MT_label__
    self.obj3062.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj3062.MT_pivotOut__.setValue('')
    self.obj3062.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3062.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3062.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3062.MT_pivotIn__.setValue('')
    self.obj3062.MT_pivotIn__.setNone()

    self.obj3062.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(351.0,363.5,self.obj3062)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3062.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3062)
    self.globalAndLocalPostcondition(self.obj3062, rootNode)
    self.obj3062.postAction( rootNode.CREATE )

    self.obj3054=MT_pre__directLink_S(self)
    self.obj3054.isGraphObjectVisual = True

    if(hasattr(self.obj3054, '_setHierarchicalLink')):
      self.obj3054._setHierarchicalLink(False)

    # MT_label__
    self.obj3054.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj3054.MT_pivotOut__.setValue('')
    self.obj3054.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3054.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3054.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3054.MT_pivotIn__.setValue('')
    self.obj3054.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3054.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3054.MT_pre__associationType.setHeight(15)

    self.obj3054.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(347.0,147.0,self.obj3054)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3054.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3054)
    self.globalAndLocalPostcondition(self.obj3054, rootNode)
    self.obj3054.postAction( rootNode.CREATE )

    self.obj3055=MT_pre__directLink_S(self)
    self.obj3055.isGraphObjectVisual = True

    if(hasattr(self.obj3055, '_setHierarchicalLink')):
      self.obj3055._setHierarchicalLink(False)

    # MT_label__
    self.obj3055.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj3055.MT_pivotOut__.setValue('')
    self.obj3055.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3055.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3055.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3055.MT_pivotIn__.setValue('')
    self.obj3055.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3055.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3055.MT_pre__associationType.setHeight(15)

    self.obj3055.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(486.0,213.0,self.obj3055)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3055.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3055)
    self.globalAndLocalPostcondition(self.obj3055, rootNode)
    self.obj3055.postAction( rootNode.CREATE )

    self.obj3056=MT_pre__directLink_S(self)
    self.obj3056.isGraphObjectVisual = True

    if(hasattr(self.obj3056, '_setHierarchicalLink')):
      self.obj3056._setHierarchicalLink(False)

    # MT_label__
    self.obj3056.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj3056.MT_pivotOut__.setValue('')
    self.obj3056.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3056.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3056.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3056.MT_pivotIn__.setValue('')
    self.obj3056.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3056.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3056.MT_pre__associationType.setHeight(15)

    self.obj3056.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(488.5,346.5,self.obj3056)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3056.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3056)
    self.globalAndLocalPostcondition(self.obj3056, rootNode)
    self.obj3056.postAction( rootNode.CREATE )

    self.obj3057=MT_pre__directLink_S(self)
    self.obj3057.isGraphObjectVisual = True

    if(hasattr(self.obj3057, '_setHierarchicalLink')):
      self.obj3057._setHierarchicalLink(False)

    # MT_label__
    self.obj3057.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj3057.MT_pivotOut__.setValue('')
    self.obj3057.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3057.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3057.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3057.MT_pivotIn__.setValue('')
    self.obj3057.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3057.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3057.MT_pre__associationType.setHeight(15)

    self.obj3057.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(353.0,414.0,self.obj3057)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3057.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3057)
    self.globalAndLocalPostcondition(self.obj3057, rootNode)
    self.obj3057.postAction( rootNode.CREATE )

    self.obj3060=MT_pre__directLink_T(self)
    self.obj3060.isGraphObjectVisual = True

    if(hasattr(self.obj3060, '_setHierarchicalLink')):
      self.obj3060._setHierarchicalLink(False)

    # MT_label__
    self.obj3060.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj3060.MT_pivotOut__.setValue('')
    self.obj3060.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3060.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3060.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj3060.MT_pivotIn__.setValue('')
    self.obj3060.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj3060.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3060.MT_pre__associationType.setHeight(15)

    self.obj3060.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(246.0,273.0,self.obj3060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj3060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3060)
    self.globalAndLocalPostcondition(self.obj3060, rootNode)
    self.obj3060.postAction( rootNode.CREATE )

    self.obj3059=MT_pre__RPortPrototype(self)
    self.obj3059.isGraphObjectVisual = True

    if(hasattr(self.obj3059, '_setHierarchicalLink')):
      self.obj3059._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3059.MT_pivotOut__.setValue('')
    self.obj3059.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3059.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3059.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3059.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3059.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3059.MT_pivotIn__.setValue('')
    self.obj3059.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3059.MT_label__.setValue('11')

    # MT_pre__cardinality
    self.obj3059.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3059.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3059.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3059.MT_pre__name.setHeight(15)

    self.obj3059.graphClass_= graph_MT_pre__RPortPrototype
    if self.genGraphics:
       new_obj = graph_MT_pre__RPortPrototype(73.0,240.0,self.obj3059)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__RPortPrototype", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3059.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3059)
    self.globalAndLocalPostcondition(self.obj3059, rootNode)
    self.obj3059.postAction( rootNode.CREATE )

    self.obj3049=MT_pre__ECU(self)
    self.obj3049.isGraphObjectVisual = True

    if(hasattr(self.obj3049, '_setHierarchicalLink')):
      self.obj3049._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3049.MT_pivotOut__.setValue('')
    self.obj3049.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3049.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3049.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3049.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3049.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3049.MT_pivotIn__.setValue('')
    self.obj3049.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3049.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj3049.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3049.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3049.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3049.MT_pre__name.setHeight(15)

    self.obj3049.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(78.0,73.0,self.obj3049)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3049.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3049)
    self.globalAndLocalPostcondition(self.obj3049, rootNode)
    self.obj3049.postAction( rootNode.CREATE )

    self.obj3058=MT_pre__CompositionType(self)
    self.obj3058.isGraphObjectVisual = True

    if(hasattr(self.obj3058, '_setHierarchicalLink')):
      self.obj3058._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3058.MT_pivotOut__.setValue('')
    self.obj3058.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3058.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3058.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3058.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3058.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3058.MT_pivotIn__.setValue('')
    self.obj3058.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3058.MT_label__.setValue('10')

    # MT_pre__cardinality
    self.obj3058.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3058.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3058.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3058.MT_pre__name.setHeight(15)

    self.obj3058.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(73.0,160.0,self.obj3058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3058)
    self.globalAndLocalPostcondition(self.obj3058, rootNode)
    self.obj3058.postAction( rootNode.CREATE )

    self.obj3052=MT_pre__ExecFrame(self)
    self.obj3052.isGraphObjectVisual = True

    if(hasattr(self.obj3052, '_setHierarchicalLink')):
      self.obj3052._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3052.MT_pivotOut__.setValue('')
    self.obj3052.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3052.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3052.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3052.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3052.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3052.MT_pivotIn__.setValue('')
    self.obj3052.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3052.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj3052.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3052.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3052.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3052.MT_pre__name.setHeight(15)

    self.obj3052.graphClass_= graph_MT_pre__ExecFrame
    if self.genGraphics:
       new_obj = graph_MT_pre__ExecFrame(286.0,340.0,self.obj3052)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExecFrame", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3052.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3052)
    self.globalAndLocalPostcondition(self.obj3052, rootNode)
    self.obj3052.postAction( rootNode.CREATE )

    self.obj3053=MT_pre__Signal(self)
    self.obj3053.isGraphObjectVisual = True

    if(hasattr(self.obj3053, '_setHierarchicalLink')):
      self.obj3053._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj3053.MT_pivotOut__.setValue('')
    self.obj3053.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj3053.MT_subtypeMatching__.setValue(('True', 0))
    self.obj3053.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj3053.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3053.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj3053.MT_pivotIn__.setValue('')
    self.obj3053.MT_pivotIn__.setNone()

    # MT_label__
    self.obj3053.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj3053.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3053.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj3053.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj3053.MT_pre__name.setHeight(15)

    self.obj3053.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(80.0,340.0,self.obj3053)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3053.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3053)
    self.globalAndLocalPostcondition(self.obj3053, rootNode)
    self.obj3053.postAction( rootNode.CREATE )

    # Connections for obj3048 (graphObject_: Obj16) of type LHS
    self.drawConnections(
 )
    # Connections for obj3050 (graphObject_: Obj18) of type MT_pre__VirtualDevice
    self.drawConnections(
(self.obj3050,self.obj3055,[451.0, 147.0, 486.0, 213.0],"true", 2) )
    # Connections for obj3051 (graphObject_: Obj19) of type MT_pre__Distributable
    self.drawConnections(
(self.obj3051,self.obj3056,[521.0, 279.0, 488.5, 346.5],"true", 2) )
    # Connections for obj3061 (graphObject_: Obj29) of type MT_pre__trace_link
    self.drawConnections(
(self.obj3061,self.obj3049,[247.0, 190.0, 248.0, 147.0],"true", 2) )
    # Connections for obj3062 (graphObject_: Obj30) of type MT_pre__trace_link
    self.drawConnections(
(self.obj3062,self.obj3052,[351.0, 363.5, 456.0, 414.0],"true", 2) )
    # Connections for obj3054 (graphObject_: Obj22) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj3054,self.obj3050,[347.0, 147.0, 451.0, 147.0],"true", 2) )
    # Connections for obj3055 (graphObject_: Obj23) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj3055,self.obj3051,[486.0, 213.0, 521.0, 279.0],"true", 2) )
    # Connections for obj3056 (graphObject_: Obj24) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj3056,self.obj3052,[488.5, 346.5, 456.0, 414.0],"true", 2) )
    # Connections for obj3057 (graphObject_: Obj25) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj3057,self.obj3053,[353.0, 414.0, 250.0, 414.0],"true", 2) )
    # Connections for obj3060 (graphObject_: Obj28) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj3060,self.obj3059,[246.0, 273.0, 246.0, 313.0],"true", 2) )
    # Connections for obj3059 (graphObject_: Obj27) of type MT_pre__RPortPrototype
    self.drawConnections(
(self.obj3059,self.obj3062,[246.0, 313.0, 351.0, 363.5],"true", 2) )
    # Connections for obj3049 (graphObject_: Obj17) of type MT_pre__ECU
    self.drawConnections(
(self.obj3049,self.obj3054,[248.0, 147.0, 347.0, 147.0],"true", 2) )
    # Connections for obj3058 (graphObject_: Obj26) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj3058,self.obj3060,[246.0, 233.0, 246.0, 273.0],"true", 2),
(self.obj3058,self.obj3061,[246.0, 233.0, 247.0, 190.0],"true", 2) )
    # Connections for obj3052 (graphObject_: Obj20) of type MT_pre__ExecFrame
    self.drawConnections(
(self.obj3052,self.obj3057,[456.0, 414.0, 353.0, 414.0],"true", 2) )
    # Connections for obj3053 (graphObject_: Obj21) of type MT_pre__Signal
    self.drawConnections(
 )

newfunction = P2Complete_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
