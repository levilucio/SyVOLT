"""
__MM2MM_combine_1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 11:01:38 2014
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_post__Male_S import *
from MT_post__Male_T import *
from MT_post__indirectLink_S import *
from MT_post__directLink_T import *
from MT_post__trace_link import *
from MT_pre__trace_link import *
from MT_pre__indirectLink_S import *
from MT_pre__Male_T import *
from MT_pre__Male_S import *
from RHS import *
from LHS import *
from graph_MT_pre__Male_T import *
from graph_MT_post__Male_S import *
from graph_MT_post__Male_T import *
from graph_MT_pre__Male_S import *
from graph_LHS import *
from graph_MT_pre__indirectLink_S import *
from graph_MT_pre__trace_link import *
from graph_MT_post__directLink_T import *
from graph_RHS import *
from graph_MT_post__indirectLink_S import *
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

def MM2MM_combine_1_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None, MT_post__PoliceStationMMRootNode=None):

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
        MoTifRuleRootNode.name.setValue('MM2MM_combine_1')
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


    self.obj10058=MT_post__Male_S(self)
    self.obj10058.isGraphObjectVisual = True

    if(hasattr(self.obj10058, '_setHierarchicalLink')):
      self.obj10058._setHierarchicalLink(False)

    # MT_label__
    self.obj10058.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj10058.MT_pivotOut__.setValue('')
    self.obj10058.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj10058.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10058.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj10058.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10058.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj10058.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10058.MT_post__name.setHeight(15)

    self.obj10058.graphClass_= graph_MT_post__Male_S
    if self.genGraphics:
       new_obj = graph_MT_post__Male_S(1100.0,260.0,self.obj10058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10058)
    self.globalAndLocalPostcondition(self.obj10058, rootNode)
    self.obj10058.postAction( rootNode.CREATE )

    self.obj10059=MT_post__Male_S(self)
    self.obj10059.isGraphObjectVisual = True

    if(hasattr(self.obj10059, '_setHierarchicalLink')):
      self.obj10059._setHierarchicalLink(False)

    # MT_label__
    self.obj10059.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj10059.MT_pivotOut__.setValue('')
    self.obj10059.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj10059.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10059.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj10059.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10059.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj10059.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10059.MT_post__name.setHeight(15)

    self.obj10059.graphClass_= graph_MT_post__Male_S
    if self.genGraphics:
       new_obj = graph_MT_post__Male_S(1280.0,260.0,self.obj10059)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10059.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10059)
    self.globalAndLocalPostcondition(self.obj10059, rootNode)
    self.obj10059.postAction( rootNode.CREATE )

    self.obj10060=MT_post__Male_T(self)
    self.obj10060.isGraphObjectVisual = True

    if(hasattr(self.obj10060, '_setHierarchicalLink')):
      self.obj10060._setHierarchicalLink(False)

    # MT_label__
    self.obj10060.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj10060.MT_pivotOut__.setValue('')
    self.obj10060.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj10060.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10060.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj10060.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10060.MT_post__name.setHeight(15)

    self.obj10060.graphClass_= graph_MT_post__Male_T
    if self.genGraphics:
       new_obj = graph_MT_post__Male_T(1100.0,440.0,self.obj10060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10060)
    self.globalAndLocalPostcondition(self.obj10060, rootNode)
    self.obj10060.postAction( rootNode.CREATE )

    self.obj10061=MT_post__Male_T(self)
    self.obj10061.isGraphObjectVisual = True

    if(hasattr(self.obj10061, '_setHierarchicalLink')):
      self.obj10061._setHierarchicalLink(False)

    # MT_label__
    self.obj10061.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj10061.MT_pivotOut__.setValue('')
    self.obj10061.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj10061.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10061.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj10061.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10061.MT_post__name.setHeight(15)

    self.obj10061.graphClass_= graph_MT_post__Male_T
    if self.genGraphics:
       new_obj = graph_MT_post__Male_T(1280.0,440.0,self.obj10061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj10061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10061)
    self.globalAndLocalPostcondition(self.obj10061, rootNode)
    self.obj10061.postAction( rootNode.CREATE )

    self.obj10073=MT_post__indirectLink_S(self)
    self.obj10073.isGraphObjectVisual = True

    if(hasattr(self.obj10073, '_setHierarchicalLink')):
      self.obj10073._setHierarchicalLink(False)

    # MT_label__
    self.obj10073.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj10073.MT_pivotOut__.setValue('')
    self.obj10073.MT_pivotOut__.setNone()

    self.obj10073.graphClass_= graph_MT_post__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__indirectLink_S(1251.0,301.0,self.obj10073)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10073.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10073)
    self.globalAndLocalPostcondition(self.obj10073, rootNode)
    self.obj10073.postAction( rootNode.CREATE )

    self.obj10078=MT_post__directLink_T(self)
    self.obj10078.isGraphObjectVisual = True

    if(hasattr(self.obj10078, '_setHierarchicalLink')):
      self.obj10078._setHierarchicalLink(False)

    # MT_label__
    self.obj10078.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj10078.MT_pivotOut__.setValue('')
    self.obj10078.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj10078.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj10078.MT_post__associationType.setHeight(15)

    self.obj10078.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(1251.0,481.0,self.obj10078)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10078.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10078)
    self.globalAndLocalPostcondition(self.obj10078, rootNode)
    self.obj10078.postAction( rootNode.CREATE )

    self.obj10063=MT_post__trace_link(self)
    self.obj10063.isGraphObjectVisual = True

    if(hasattr(self.obj10063, '_setHierarchicalLink')):
      self.obj10063._setHierarchicalLink(False)

    # MT_label__
    self.obj10063.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj10063.MT_pivotOut__.setValue('')
    self.obj10063.MT_pivotOut__.setNone()

    self.obj10063.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1161.0,391.0,self.obj10063)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10063.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10063)
    self.globalAndLocalPostcondition(self.obj10063, rootNode)
    self.obj10063.postAction( rootNode.CREATE )

    self.obj10064=MT_post__trace_link(self)
    self.obj10064.isGraphObjectVisual = True

    if(hasattr(self.obj10064, '_setHierarchicalLink')):
      self.obj10064._setHierarchicalLink(False)

    # MT_label__
    self.obj10064.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj10064.MT_pivotOut__.setValue('')
    self.obj10064.MT_pivotOut__.setNone()

    self.obj10064.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1341.0,391.0,self.obj10064)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10064.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10064)
    self.globalAndLocalPostcondition(self.obj10064, rootNode)
    self.obj10064.postAction( rootNode.CREATE )

    self.obj87=MT_pre__trace_link(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj87.MT_subtypeMatching__.setValue(('True', 0))
    self.obj87.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj87.MT_pivotIn__.setValue('')
    self.obj87.MT_pivotIn__.setNone()

    self.obj87.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(661.0,391.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=MT_pre__trace_link(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # MT_label__
    self.obj88.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj88.MT_pivotOut__.setValue('')
    self.obj88.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj88.MT_subtypeMatching__.setValue(('True', 0))
    self.obj88.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj88.MT_pivotIn__.setValue('')
    self.obj88.MT_pivotIn__.setNone()

    self.obj88.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(841.0,391.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj15060=MT_pre__indirectLink_S(self)
    self.obj15060.isGraphObjectVisual = True

    if(hasattr(self.obj15060, '_setHierarchicalLink')):
      self.obj15060._setHierarchicalLink(False)

    # MT_label__
    self.obj15060.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj15060.MT_pivotOut__.setValue('')
    self.obj15060.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj15060.MT_subtypeMatching__.setValue(('True', 0))
    self.obj15060.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj15060.MT_pivotIn__.setValue('')
    self.obj15060.MT_pivotIn__.setNone()

    self.obj15060.graphClass_= graph_MT_pre__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__indirectLink_S(751.0,301.0,self.obj15060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj15060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15060)
    self.globalAndLocalPostcondition(self.obj15060, rootNode)
    self.obj15060.postAction( rootNode.CREATE )

    self.obj73=MT_pre__Male_T(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('')
    self.obj73.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj73.MT_subtypeMatching__.setValue(('True', 0))
    self.obj73.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73.MT_pivotIn__.setValue('')
    self.obj73.MT_pivotIn__.setNone()

    # MT_label__
    self.obj73.MT_label__.setValue('3')

    # MT_pre__name
    self.obj73.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__name.setHeight(15)

    self.obj73.graphClass_= graph_MT_pre__Male_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_T(600.0,440.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=MT_pre__Male_T(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj74.MT_subtypeMatching__.setValue(('True', 0))
    self.obj74.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj74.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj74.MT_pivotIn__.setValue('')
    self.obj74.MT_pivotIn__.setNone()

    # MT_label__
    self.obj74.MT_label__.setValue('4')

    # MT_pre__name
    self.obj74.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__name.setHeight(15)

    self.obj74.graphClass_= graph_MT_pre__Male_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_T(780.0,440.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj65=MT_pre__Male_S(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj65.MT_pivotOut__.setValue('')
    self.obj65.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj65.MT_subtypeMatching__.setValue(('True', 0))
    self.obj65.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj65.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj65.MT_pivotIn__.setValue('')
    self.obj65.MT_pivotIn__.setNone()

    # MT_label__
    self.obj65.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj65.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj65.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__name.setHeight(15)

    self.obj65.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(600.0,260.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=MT_pre__Male_S(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj66.MT_pivotOut__.setValue('')
    self.obj66.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj66.MT_subtypeMatching__.setValue(('True', 0))
    self.obj66.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj66.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj66.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj66.MT_pivotIn__.setValue('')
    self.obj66.MT_pivotIn__.setNone()

    # MT_label__
    self.obj66.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj66.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj66.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj66.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj66.MT_pre__name.setHeight(15)

    self.obj66.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(780.0,260.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj63=RHS(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # action
    self.obj63.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj63.action.setHeight(15)

    self.obj63.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(960.0,200.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=LHS(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # constraint
    self.obj64.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj64.constraint.setHeight(15)

    self.obj64.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(520.0,200.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    # Connections for obj10058 (graphObject_: Obj20) of type MT_post__Male_S
    self.drawConnections(
(self.obj10058,self.obj10073,[1161.0, 301.0, 1251.0, 301.0],"true", 2) )
    # Connections for obj10059 (graphObject_: Obj21) of type MT_post__Male_S
    self.drawConnections(
 )
    # Connections for obj10060 (graphObject_: Obj22) of type MT_post__Male_T
    self.drawConnections(
(self.obj10060,self.obj10063,[1161.0, 481.0, 1161.0, 391.0],"true", 2),
(self.obj10060,self.obj10078,[1161.0, 481.0, 1251.0, 481.0],"true", 2) )
    # Connections for obj10061 (graphObject_: Obj23) of type MT_post__Male_T
    self.drawConnections(
(self.obj10061,self.obj10064,[1341.0, 481.0, 1341.0, 391.0],"true", 2) )
    # Connections for obj10073 (graphObject_: Obj27) of type MT_post__indirectLink_S
    self.drawConnections(
(self.obj10073,self.obj10059,[1251.0, 301.0, 1341.0, 301.0],"true", 2) )
    # Connections for obj10078 (graphObject_: Obj28) of type MT_post__directLink_T
    self.drawConnections(
(self.obj10078,self.obj10061,[1251.0, 481.0, 1341.0, 481.0],"true", 2) )
    # Connections for obj10063 (graphObject_: Obj25) of type MT_post__trace_link
    self.drawConnections(
(self.obj10063,self.obj10058,[1161.0, 391.0, 1161.0, 301.0],"true", 2) )
    # Connections for obj10064 (graphObject_: Obj26) of type MT_post__trace_link
    self.drawConnections(
(self.obj10064,self.obj10059,[1341.0, 391.0, 1341.0, 301.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj13) of type MT_pre__trace_link
    self.drawConnections(
(self.obj87,self.obj65,[661.0, 391.0, 661.0, 301.0],"true", 2) )
    # Connections for obj88 (graphObject_: Obj14) of type MT_pre__trace_link
    self.drawConnections(
(self.obj88,self.obj66,[841.0, 391.0, 841.0, 301.0],"true", 2) )
    # Connections for obj15060 (graphObject_: Obj29) of type MT_pre__indirectLink_S
    self.drawConnections(
(self.obj15060,self.obj66,[751.0, 301.0, 841.0, 301.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj7) of type MT_pre__Male_T
    self.drawConnections(
(self.obj73,self.obj87,[661.0, 481.0, 661.0, 391.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj8) of type MT_pre__Male_T
    self.drawConnections(
(self.obj74,self.obj88,[841.0, 481.0, 841.0, 391.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj3) of type MT_pre__Male_S
    self.drawConnections(
(self.obj65,self.obj15060,[661.0, 301.0, 751.0, 301.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj4) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj1) of type RHS
    self.drawConnections(
 )
    # Connections for obj64 (graphObject_: Obj2) of type LHS
    self.drawConnections(
 )

newfunction = MM2MM_combine_1_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META', 'MT_post__PoliceStationMM_META']

atom3version = '0.3'
