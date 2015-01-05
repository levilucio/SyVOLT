"""
__M2M_combine_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sun Jan  4 14:46:13 2015
_________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Male_S import *
from RHS import *
from LHS import *
from MT_post__trace_link import *
from MT_post__Male_T import *
from MT_post__Male_S import *
from graph_MT_post__Male_S import *
from graph_MT_post__Male_T import *
from graph_MT_pre__Male_S import *
from graph_LHS import *
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

def M2M_combine_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MT_post__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('M2M_combine')
    # --- ASG attributes over ---


    self.obj5056=MT_pre__Male_S(self)
    self.obj5056.isGraphObjectVisual = True

    if(hasattr(self.obj5056, '_setHierarchicalLink')):
      self.obj5056._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj5056.MT_pivotOut__.setValue('')
    self.obj5056.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj5056.MT_subtypeMatching__.setValue(('True', 0))
    self.obj5056.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj5056.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj5056.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj5056.MT_pivotIn__.setValue('')
    self.obj5056.MT_pivotIn__.setNone()

    # MT_label__
    self.obj5056.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj5056.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj5056.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj5056.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj5056.MT_pre__name.setHeight(15)

    self.obj5056.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(620.0,220.0,self.obj5056)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj5056.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5056)
    self.globalAndLocalPostcondition(self.obj5056, rootNode)
    self.obj5056.postAction( rootNode.CREATE )

    self.obj74=RHS(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # action
    self.obj74.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj74.action.setHeight(15)

    self.obj74.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(900.0,140.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=LHS(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # constraint
    self.obj75.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj75.constraint.setHeight(15)

    self.obj75.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(460.0,140.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj5061=MT_post__trace_link(self)
    self.obj5061.isGraphObjectVisual = True

    if(hasattr(self.obj5061, '_setHierarchicalLink')):
      self.obj5061._setHierarchicalLink(False)

    # MT_label__
    self.obj5061.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj5061.MT_pivotOut__.setValue('')
    self.obj5061.MT_pivotOut__.setNone()

    self.obj5061.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1201.0,351.0,self.obj5061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj5061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5061)
    self.globalAndLocalPostcondition(self.obj5061, rootNode)
    self.obj5061.postAction( rootNode.CREATE )

    self.obj5058=MT_post__Male_T(self)
    self.obj5058.isGraphObjectVisual = True

    if(hasattr(self.obj5058, '_setHierarchicalLink')):
      self.obj5058._setHierarchicalLink(False)

    # MT_label__
    self.obj5058.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj5058.MT_pivotOut__.setValue('')
    self.obj5058.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj5058.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj5058.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj5058.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj5058.MT_post__name.setHeight(15)

    self.obj5058.graphClass_= graph_MT_post__Male_T
    if self.genGraphics:
       new_obj = graph_MT_post__Male_T(1140.0,400.0,self.obj5058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj5058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5058)
    self.globalAndLocalPostcondition(self.obj5058, rootNode)
    self.obj5058.postAction( rootNode.CREATE )

    self.obj5057=MT_post__Male_S(self)
    self.obj5057.isGraphObjectVisual = True

    if(hasattr(self.obj5057, '_setHierarchicalLink')):
      self.obj5057._setHierarchicalLink(False)

    # MT_label__
    self.obj5057.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj5057.MT_pivotOut__.setValue('')
    self.obj5057.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj5057.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj5057.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj5057.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj5057.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj5057.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj5057.MT_post__name.setHeight(15)

    self.obj5057.graphClass_= graph_MT_post__Male_S
    if self.genGraphics:
       new_obj = graph_MT_post__Male_S(1140.0,220.0,self.obj5057)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj5057.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5057)
    self.globalAndLocalPostcondition(self.obj5057, rootNode)
    self.obj5057.postAction( rootNode.CREATE )

    # Connections for obj5056 (graphObject_: Obj18) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj15) of type RHS
    self.drawConnections(
 )
    # Connections for obj75 (graphObject_: Obj16) of type LHS
    self.drawConnections(
 )
    # Connections for obj5061 (graphObject_: Obj21) of type MT_post__trace_link
    self.drawConnections(
(self.obj5061,self.obj5057,[1201.0, 351.0, 1201.0, 261.0],"true", 2) )
    # Connections for obj5058 (graphObject_: Obj20) of type MT_post__Male_T
    self.drawConnections(
(self.obj5058,self.obj5061,[1201.0, 441.0, 1201.0, 351.0],"true", 2) )
    # Connections for obj5057 (graphObject_: Obj19) of type MT_post__Male_S
    self.drawConnections(
 )

newfunction = M2M_combine_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MT_post__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
