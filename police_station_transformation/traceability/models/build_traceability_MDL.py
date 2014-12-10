"""
__build_traceability_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Nov  6 15:07:13 2014
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from RHS import *
from LHS import *
from MT_pre__MetaModelElement_T import *
from MT_pre__MetaModelElement_S import *
from MT_post__MetaModelElement_S import *
from MT_post__trace_link import *
from MT_post__MetaModelElement_T import *
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

def build_traceability_MDL(self, rootNode, MT_post__PoliceStationMMRootNode=None, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_post__PoliceStationMM ---
    if( MT_post__PoliceStationMMRootNode ): 
        # author
        MT_post__PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        MT_post__PoliceStationMMRootNode.description.setValue('\n')
        MT_post__PoliceStationMMRootNode.description.setHeight(15)

        # name
        MT_post__PoliceStationMMRootNode.name.setValue('')
        MT_post__PoliceStationMMRootNode.name.setNone()
    # --- ASG attributes over ---


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
        MoTifRuleRootNode.name.setValue('')
        MoTifRuleRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj42=RHS(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # action
    self.obj42.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj42.action.setHeight(15)

    self.obj42.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(660.0,180.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj41=LHS(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # constraint
    self.obj41.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj41.constraint.setHeight(15)

    self.obj41.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(200.0,180.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj74=MT_pre__MetaModelElement_T(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj74.MT_subtypeMatching__.setValue(('True', 1))
    self.obj74.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj74.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj74.MT_pivotIn__.setValue('')
    self.obj74.MT_pivotIn__.setNone()

    # MT_label__
    self.obj74.MT_label__.setValue('2')

    # MT_pre__name
    self.obj74.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__name.setHeight(15)

    self.obj74.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(340.0,440.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj56=MT_pre__MetaModelElement_S(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 1))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj56.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    # MT_label__
    self.obj56.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj56.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj56.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__name.setHeight(15)

    self.obj56.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(340.0,260.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj75=MT_post__MetaModelElement_S(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_label__
    self.obj75.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj75.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj75.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj75.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj75.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj75.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj75.MT_post__name.setHeight(15)

    self.obj75.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(900.0,260.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj77=MT_post__trace_link(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_label__
    self.obj77.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    self.obj77.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(959.0,391.5,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj76=MT_post__MetaModelElement_T(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_label__
    self.obj76.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj76.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj76.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj76.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj76.MT_post__name.setHeight(15)

    self.obj76.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(900.0,440.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    # Connections for obj42 (graphObject_: Obj2) of type RHS
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj1) of type LHS
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj6) of type MT_pre__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj3) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj75 (graphObject_: Obj7) of type MT_post__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj77 (graphObject_: Obj9) of type MT_post__trace_link
    self.drawConnections(
(self.obj77,self.obj75,[959.0, 391.5, 960.0, 302.0],"true", 2) )
    # Connections for obj76 (graphObject_: Obj8) of type MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj76,self.obj77,[958.0, 481.0, 959.0, 391.5],"true", 2) )

newfunction = build_traceability_MDL

loadedMMName = ['MT_post__PoliceStationMM_META', 'MT_pre__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
