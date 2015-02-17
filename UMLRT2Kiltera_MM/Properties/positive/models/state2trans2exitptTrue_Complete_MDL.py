"""
__state2trans2exitptTrue_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 19:21:08 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__Par import *
from MT_pre__trace_link import *
from MT_pre__directLink_S import *
from MT_pre__directLink_T import *
from MT_pre__Transition import *
from MT_pre__ExitPoint import *
from MT_pre__ProcDef import *
from MT_pre__Trigger_T import *
from graph_MT_pre__Trigger_T import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Transition import *
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

def state2trans2exitptTrue_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('state2trans2exitptTrue_Complete')
    # --- ASG attributes over ---


    self.obj21190=LHS(self)
    self.obj21190.isGraphObjectVisual = True

    if(hasattr(self.obj21190, '_setHierarchicalLink')):
      self.obj21190._setHierarchicalLink(False)

    # constraint
    self.obj21190.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj21190.constraint.setHeight(15)

    self.obj21190.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj21190)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21190.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21190)
    self.globalAndLocalPostcondition(self.obj21190, rootNode)
    self.obj21190.postAction( rootNode.CREATE )

    self.obj21176=MT_pre__State(self)
    self.obj21176.isGraphObjectVisual = True

    if(hasattr(self.obj21176, '_setHierarchicalLink')):
      self.obj21176._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21176.MT_pivotOut__.setValue('')
    self.obj21176.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21176.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21176.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21176.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21176.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21176.MT_pivotIn__.setValue('')
    self.obj21176.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21176.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj21176.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21176.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21176.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21176.MT_pre__name.setHeight(15)

    self.obj21176.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(160.0,80.0,self.obj21176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21176)
    self.globalAndLocalPostcondition(self.obj21176, rootNode)
    self.obj21176.postAction( rootNode.CREATE )

    self.obj21179=MT_pre__Par(self)
    self.obj21179.isGraphObjectVisual = True

    if(hasattr(self.obj21179, '_setHierarchicalLink')):
      self.obj21179._setHierarchicalLink(False)

    # MT_label__
    self.obj21179.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj21179.MT_pivotOut__.setValue('')
    self.obj21179.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21179.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21179.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21179.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21179.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21179.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21179.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21179.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21179.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21179.MT_pivotIn__.setValue('')
    self.obj21179.MT_pivotIn__.setNone()

    self.obj21179.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(280.0,200.0,self.obj21179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21179)
    self.globalAndLocalPostcondition(self.obj21179, rootNode)
    self.obj21179.postAction( rootNode.CREATE )

    self.obj21184=MT_pre__trace_link(self)
    self.obj21184.isGraphObjectVisual = True

    if(hasattr(self.obj21184, '_setHierarchicalLink')):
      self.obj21184._setHierarchicalLink(False)

    # MT_label__
    self.obj21184.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj21184.MT_pivotOut__.setValue('')
    self.obj21184.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21184.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21184.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21184.MT_pivotIn__.setValue('')
    self.obj21184.MT_pivotIn__.setNone()

    self.obj21184.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(382.0,258.0,self.obj21184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21184)
    self.globalAndLocalPostcondition(self.obj21184, rootNode)
    self.obj21184.postAction( rootNode.CREATE )

    self.obj21185=MT_pre__trace_link(self)
    self.obj21185.isGraphObjectVisual = True

    if(hasattr(self.obj21185, '_setHierarchicalLink')):
      self.obj21185._setHierarchicalLink(False)

    # MT_label__
    self.obj21185.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj21185.MT_pivotOut__.setValue('')
    self.obj21185.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21185.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21185.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21185.MT_pivotIn__.setValue('')
    self.obj21185.MT_pivotIn__.setNone()

    self.obj21185.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(329.5,248.0,self.obj21185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21185.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21185)
    self.globalAndLocalPostcondition(self.obj21185, rootNode)
    self.obj21185.postAction( rootNode.CREATE )

    self.obj21186=MT_pre__trace_link(self)
    self.obj21186.isGraphObjectVisual = True

    if(hasattr(self.obj21186, '_setHierarchicalLink')):
      self.obj21186._setHierarchicalLink(False)

    # MT_label__
    self.obj21186.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj21186.MT_pivotOut__.setValue('')
    self.obj21186.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21186.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21186.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21186.MT_pivotIn__.setValue('')
    self.obj21186.MT_pivotIn__.setNone()

    self.obj21186.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(482.0,238.0,self.obj21186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21186)
    self.globalAndLocalPostcondition(self.obj21186, rootNode)
    self.obj21186.postAction( rootNode.CREATE )

    self.obj21187=MT_pre__trace_link(self)
    self.obj21187.isGraphObjectVisual = True

    if(hasattr(self.obj21187, '_setHierarchicalLink')):
      self.obj21187._setHierarchicalLink(False)

    # MT_label__
    self.obj21187.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj21187.MT_pivotOut__.setValue('')
    self.obj21187.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21187.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21187.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21187.MT_pivotIn__.setValue('')
    self.obj21187.MT_pivotIn__.setNone()

    self.obj21187.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(429.5,228.0,self.obj21187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21187)
    self.globalAndLocalPostcondition(self.obj21187, rootNode)
    self.obj21187.postAction( rootNode.CREATE )

    self.obj21188=MT_pre__trace_link(self)
    self.obj21188.isGraphObjectVisual = True

    if(hasattr(self.obj21188, '_setHierarchicalLink')):
      self.obj21188._setHierarchicalLink(False)

    # MT_label__
    self.obj21188.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj21188.MT_pivotOut__.setValue('')
    self.obj21188.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21188.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21188.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21188.MT_pivotIn__.setValue('')
    self.obj21188.MT_pivotIn__.setNone()

    self.obj21188.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(452.0,288.0,self.obj21188)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21188.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21188)
    self.globalAndLocalPostcondition(self.obj21188, rootNode)
    self.obj21188.postAction( rootNode.CREATE )

    self.obj21189=MT_pre__trace_link(self)
    self.obj21189.isGraphObjectVisual = True

    if(hasattr(self.obj21189, '_setHierarchicalLink')):
      self.obj21189._setHierarchicalLink(False)

    # MT_label__
    self.obj21189.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj21189.MT_pivotOut__.setValue('')
    self.obj21189.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21189.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21189.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21189.MT_pivotIn__.setValue('')
    self.obj21189.MT_pivotIn__.setNone()

    self.obj21189.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(399.5,278.0,self.obj21189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21189)
    self.globalAndLocalPostcondition(self.obj21189, rootNode)
    self.obj21189.postAction( rootNode.CREATE )

    self.obj21182=MT_pre__directLink_S(self)
    self.obj21182.isGraphObjectVisual = True

    if(hasattr(self.obj21182, '_setHierarchicalLink')):
      self.obj21182._setHierarchicalLink(False)

    # MT_label__
    self.obj21182.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj21182.MT_pivotOut__.setValue('')
    self.obj21182.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21182.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21182.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21182.MT_pivotIn__.setValue('')
    self.obj21182.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21182.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn true\n')
    self.obj21182.MT_pre__associationType.setHeight(15)

    self.obj21182.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(389.5,205.0,self.obj21182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21182)
    self.globalAndLocalPostcondition(self.obj21182, rootNode)
    self.obj21182.postAction( rootNode.CREATE )

    self.obj21183=MT_pre__directLink_S(self)
    self.obj21183.isGraphObjectVisual = True

    if(hasattr(self.obj21183, '_setHierarchicalLink')):
      self.obj21183._setHierarchicalLink(False)

    # MT_label__
    self.obj21183.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj21183.MT_pivotOut__.setValue('')
    self.obj21183.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21183.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21183.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21183.MT_pivotIn__.setValue('')
    self.obj21183.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21183.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn true\n')
    self.obj21183.MT_pre__associationType.setHeight(15)

    self.obj21183.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(318.5,173.0,self.obj21183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21183)
    self.globalAndLocalPostcondition(self.obj21183, rootNode)
    self.obj21183.postAction( rootNode.CREATE )

    self.obj21180=MT_pre__directLink_T(self)
    self.obj21180.isGraphObjectVisual = True

    if(hasattr(self.obj21180, '_setHierarchicalLink')):
      self.obj21180._setHierarchicalLink(False)

    # MT_label__
    self.obj21180.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj21180.MT_pivotOut__.setValue('')
    self.obj21180.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21180.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21180.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21180.MT_pivotIn__.setValue('')
    self.obj21180.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21180.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21180.MT_pre__associationType.setHeight(15)

    self.obj21180.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(402.0,321.0,self.obj21180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21180)
    self.globalAndLocalPostcondition(self.obj21180, rootNode)
    self.obj21180.postAction( rootNode.CREATE )

    self.obj21181=MT_pre__directLink_T(self)
    self.obj21181.isGraphObjectVisual = True

    if(hasattr(self.obj21181, '_setHierarchicalLink')):
      self.obj21181._setHierarchicalLink(False)

    # MT_label__
    self.obj21181.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj21181.MT_pivotOut__.setValue('')
    self.obj21181.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21181.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21181.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21181.MT_pivotIn__.setValue('')
    self.obj21181.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21181.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21181.MT_pre__associationType.setHeight(15)

    self.obj21181.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(472.0,351.0,self.obj21181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21181)
    self.globalAndLocalPostcondition(self.obj21181, rootNode)
    self.obj21181.postAction( rootNode.CREATE )

    self.obj21175=MT_pre__Transition(self)
    self.obj21175.isGraphObjectVisual = True

    if(hasattr(self.obj21175, '_setHierarchicalLink')):
      self.obj21175._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21175.MT_pivotOut__.setValue('')
    self.obj21175.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21175.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21175.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21175.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21175.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21175.MT_pivotIn__.setValue('')
    self.obj21175.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21175.MT_label__.setValue('13')

    # MT_pre__cardinality
    self.obj21175.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21175.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21175.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21175.MT_pre__name.setHeight(15)

    self.obj21175.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(80.0,120.0,self.obj21175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21175)
    self.globalAndLocalPostcondition(self.obj21175, rootNode)
    self.obj21175.postAction( rootNode.CREATE )

    self.obj21174=MT_pre__ExitPoint(self)
    self.obj21174.isGraphObjectVisual = True

    if(hasattr(self.obj21174, '_setHierarchicalLink')):
      self.obj21174._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21174.MT_pivotOut__.setValue('')
    self.obj21174.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21174.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21174.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21174.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21174.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21174.MT_pivotIn__.setValue('')
    self.obj21174.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21174.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj21174.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21174.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21174.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21174.MT_pre__name.setHeight(15)

    self.obj21174.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(260.0,100.0,self.obj21174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21174)
    self.globalAndLocalPostcondition(self.obj21174, rootNode)
    self.obj21174.postAction( rootNode.CREATE )

    self.obj21177=MT_pre__ProcDef(self)
    self.obj21177.isGraphObjectVisual = True

    if(hasattr(self.obj21177, '_setHierarchicalLink')):
      self.obj21177._setHierarchicalLink(False)

    # MT_label__
    self.obj21177.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj21177.MT_pivotOut__.setValue('')
    self.obj21177.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21177.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21177.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21177.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21177.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21177.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21177.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21177.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21177.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21177.MT_pivotIn__.setValue('')
    self.obj21177.MT_pivotIn__.setNone()

    self.obj21177.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(80.0,240.0,self.obj21177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21177)
    self.globalAndLocalPostcondition(self.obj21177, rootNode)
    self.obj21177.postAction( rootNode.CREATE )

    self.obj21178=MT_pre__Trigger_T(self)
    self.obj21178.isGraphObjectVisual = True

    if(hasattr(self.obj21178, '_setHierarchicalLink')):
      self.obj21178._setHierarchicalLink(False)

    # MT_label__
    self.obj21178.MT_label__.setValue('23')

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

    self.obj21178.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(220.0,300.0,self.obj21178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21178)
    self.globalAndLocalPostcondition(self.obj21178, rootNode)
    self.obj21178.postAction( rootNode.CREATE )

    # Connections for obj21190 (graphObject_: Obj37) of type LHS
    self.drawConnections(
 )
    # Connections for obj21176 (graphObject_: Obj23) of type MT_pre__State
    self.drawConnections(
(self.obj21176,self.obj21182,[357.0, 155.0, 389.5, 205.0],"true", 2),
(self.obj21176,self.obj21183,[357.0, 155.0, 318.5, 173.0],"true", 2) )
    # Connections for obj21179 (graphObject_: Obj26) of type MT_pre__Par
    self.drawConnections(
(self.obj21179,self.obj21186,[502.0, 301.0, 482.0, 238.0],"true", 2),
(self.obj21179,self.obj21187,[502.0, 301.0, 429.5, 228.0],"true", 2),
(self.obj21179,self.obj21181,[502.0, 301.0, 472.0, 351.0],"true", 2) )
    # Connections for obj21184 (graphObject_: Obj31) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21184,self.obj21174,[382.0, 258.0, 462.0, 175.0],"true", 2) )
    # Connections for obj21185 (graphObject_: Obj32) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21185,self.obj21176,[329.5, 248.0, 357.0, 155.0],"true", 2) )
    # Connections for obj21186 (graphObject_: Obj33) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21186,self.obj21174,[482.0, 238.0, 462.0, 175.0],"true", 2) )
    # Connections for obj21187 (graphObject_: Obj34) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21187,self.obj21176,[429.5, 228.0, 357.0, 155.0],"true", 2) )
    # Connections for obj21188 (graphObject_: Obj35) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21188,self.obj21174,[452.0, 288.0, 462.0, 175.0],"true", 2) )
    # Connections for obj21189 (graphObject_: Obj36) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21189,self.obj21176,[399.5, 278.0, 357.0, 155.0],"true", 2) )
    # Connections for obj21182 (graphObject_: Obj29) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj21182,self.obj21174,[389.5, 205.0, 462.0, 175.0],"true", 2) )
    # Connections for obj21183 (graphObject_: Obj30) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj21183,self.obj21175,[318.5, 173.0, 282.0, 195.0],"true", 2) )
    # Connections for obj21180 (graphObject_: Obj27) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21180,self.obj21179,[402.0, 321.0, 502.0, 301.0],"true", 2) )
    # Connections for obj21181 (graphObject_: Obj28) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21181,self.obj21178,[472.0, 351.0, 442.0, 401.0],"true", 2) )
    # Connections for obj21175 (graphObject_: Obj22) of type MT_pre__Transition
    self.drawConnections(
 )
    # Connections for obj21174 (graphObject_: Obj21) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj21177 (graphObject_: Obj24) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj21177,self.obj21184,[302.0, 341.0, 382.0, 258.0],"true", 2),
(self.obj21177,self.obj21185,[302.0, 341.0, 329.5, 248.0],"true", 2),
(self.obj21177,self.obj21180,[302.0, 341.0, 402.0, 321.0],"true", 2) )
    # Connections for obj21178 (graphObject_: Obj25) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj21178,self.obj21188,[442.0, 401.0, 452.0, 288.0],"true", 2),
(self.obj21178,self.obj21189,[442.0, 401.0, 399.5, 278.0],"true", 2) )

newfunction = state2trans2exitptTrue_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
