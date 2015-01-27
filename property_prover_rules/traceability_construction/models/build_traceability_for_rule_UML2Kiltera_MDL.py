"""
__build_traceability_for_rule_UML2Kiltera_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Tue Jan 27 11:24:24 2015
_____________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MetaModelElement_S import *
from MT_pre__MetaModelElement_T import *
from MT_post__trace_link import *
from MT_post__MetaModelElement_S import *
from MT_post__MetaModelElement_T import *
from RHS import *
from LHS import *
from graph_MT_post__MetaModelElement_S import *
from graph_MT_post__MetaModelElement_T import *
from graph_LHS import *
from graph_MT_pre__MetaModelElement_S import *
from graph_MT_pre__MetaModelElement_T import *
from graph_RHS import *
from graph_MT_post__trace_link import *
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

def build_traceability_for_rule_UML2Kiltera_MDL(self, rootNode, MT_post__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MT_post__UMLRT2Kiltera_MM ---
    if( MT_post__UMLRT2Kiltera_MMRootNode ): 
        # author
        MT_post__UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        MT_post__UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        MT_post__UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        MT_post__UMLRT2Kiltera_MMRootNode.name.setValue('')
        MT_post__UMLRT2Kiltera_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('build_traceability_for_rule_UML2Kiltera')
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


    self.obj191=MT_pre__MetaModelElement_S(self)
    self.obj191.isGraphObjectVisual = True

    if(hasattr(self.obj191, '_setHierarchicalLink')):
      self.obj191._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj191.MT_pivotOut__.setValue('')
    self.obj191.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj191.MT_subtypeMatching__.setValue(('True', 1))
    self.obj191.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj191.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj191.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj191.MT_pivotIn__.setValue('')
    self.obj191.MT_pivotIn__.setNone()

    # MT_label__
    self.obj191.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj191.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj191.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj191.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj191.MT_pre__name.setHeight(15)

    self.obj191.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(240.0,80.0,self.obj191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj191.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj191)
    self.globalAndLocalPostcondition(self.obj191, rootNode)
    self.obj191.postAction( rootNode.CREATE )

    self.obj192=MT_pre__MetaModelElement_T(self)
    self.obj192.isGraphObjectVisual = True

    if(hasattr(self.obj192, '_setHierarchicalLink')):
      self.obj192._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj192.MT_pivotOut__.setValue('')
    self.obj192.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj192.MT_subtypeMatching__.setValue(('True', 1))
    self.obj192.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj192.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj192.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj192.MT_pivotIn__.setValue('')
    self.obj192.MT_pivotIn__.setNone()

    # MT_label__
    self.obj192.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj192.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj192.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj192.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj192.MT_pre__name.setHeight(15)

    self.obj192.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(220.0,260.0,self.obj192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj192.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj192)
    self.globalAndLocalPostcondition(self.obj192, rootNode)
    self.obj192.postAction( rootNode.CREATE )

    self.obj195=MT_post__trace_link(self)
    self.obj195.isGraphObjectVisual = True

    if(hasattr(self.obj195, '_setHierarchicalLink')):
      self.obj195._setHierarchicalLink(False)

    # MT_label__
    self.obj195.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj195.MT_pivotOut__.setValue('')
    self.obj195.MT_pivotOut__.setNone()

    self.obj195.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(937.0,258.0,self.obj195)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj195.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj195)
    self.globalAndLocalPostcondition(self.obj195, rootNode)
    self.obj195.postAction( rootNode.CREATE )

    self.obj193=MT_post__MetaModelElement_S(self)
    self.obj193.isGraphObjectVisual = True

    if(hasattr(self.obj193, '_setHierarchicalLink')):
      self.obj193._setHierarchicalLink(False)

    # MT_label__
    self.obj193.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj193.MT_pivotOut__.setValue('')
    self.obj193.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj193.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj193.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj193.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj193.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj193.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj193.MT_post__name.setHeight(15)

    self.obj193.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(740.0,80.0,self.obj193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj193.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj193)
    self.globalAndLocalPostcondition(self.obj193, rootNode)
    self.obj193.postAction( rootNode.CREATE )

    self.obj194=MT_post__MetaModelElement_T(self)
    self.obj194.isGraphObjectVisual = True

    if(hasattr(self.obj194, '_setHierarchicalLink')):
      self.obj194._setHierarchicalLink(False)

    # MT_label__
    self.obj194.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj194.MT_pivotOut__.setValue('')
    self.obj194.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj194.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj194.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj194.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj194.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj194.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj194.MT_post__name.setHeight(15)

    self.obj194.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(720.0,260.0,self.obj194)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj194.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj194)
    self.globalAndLocalPostcondition(self.obj194, rootNode)
    self.obj194.postAction( rootNode.CREATE )

    self.obj190=RHS(self)
    self.obj190.isGraphObjectVisual = True

    if(hasattr(self.obj190, '_setHierarchicalLink')):
      self.obj190._setHierarchicalLink(False)

    # action
    self.obj190.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj190.action.setHeight(15)

    self.obj190.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(560.0,40.0,self.obj190)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj190.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj190)
    self.globalAndLocalPostcondition(self.obj190, rootNode)
    self.obj190.postAction( rootNode.CREATE )

    self.obj189=LHS(self)
    self.obj189.isGraphObjectVisual = True

    if(hasattr(self.obj189, '_setHierarchicalLink')):
      self.obj189._setHierarchicalLink(False)

    # constraint
    self.obj189.constraint.setValue('return True\n')
    self.obj189.constraint.setHeight(15)

    self.obj189.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,40.0,self.obj189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj189)
    self.globalAndLocalPostcondition(self.obj189, rootNode)
    self.obj189.postAction( rootNode.CREATE )

    # Connections for obj191 (graphObject_: Obj2) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj192 (graphObject_: Obj3) of type MT_pre__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj195 (graphObject_: Obj6) of type MT_post__trace_link
    self.drawConnections(
(self.obj195,self.obj193,[937.0, 258.0, 937.0, 155.0],"true", 2) )
    # Connections for obj193 (graphObject_: Obj4) of type MT_post__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj194 (graphObject_: Obj5) of type MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj194,self.obj195,[937.0, 361.0, 937.0, 258.0],"true", 2) )
    # Connections for obj190 (graphObject_: Obj1) of type RHS
    self.drawConnections(
 )
    # Connections for obj189 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = build_traceability_for_rule_UML2Kiltera_MDL

loadedMMName = ['MT_post__UMLRT2Kiltera_MM_META', 'MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
