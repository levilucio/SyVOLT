"""
__FF2FF_combine_1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 11:12:57 2014
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Female_S import *
from MT_pre__Female_T import *
from MT_pre__indirectLink_S import *
from MT_pre__trace_link import *
from MT_post__indirectLink_S import *
from MT_post__directLink_T import *
from MT_post__Female_S import *
from MT_post__Female_T import *
from MT_post__trace_link import *
from RHS import *
from LHS import *
from graph_LHS import *
from graph_MT_pre__indirectLink_S import *
from graph_MT_post__trace_link import *
from graph_MT_pre__trace_link import *
from graph_MT_post__directLink_T import *
from graph_RHS import *
from graph_MT_post__Female_T import *
from graph_MT_post__indirectLink_S import *
from graph_MT_pre__Female_T import *
from graph_MT_pre__Female_S import *
from graph_MT_post__Female_S import *
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

def FF2FF_combine_1_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None, MT_post__PoliceStationMMRootNode=None):

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
        MoTifRuleRootNode.name.setValue('FF2FF_combine_1')
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


    self.obj68=MT_pre__Female_S(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj68.MT_pivotOut__.setValue('')
    self.obj68.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj68.MT_subtypeMatching__.setValue(('True', 0))
    self.obj68.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj68.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj68.MT_pivotIn__.setValue('')
    self.obj68.MT_pivotIn__.setNone()

    # MT_label__
    self.obj68.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj68.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj68.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj68.MT_pre__name.setHeight(15)

    self.obj68.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(560.0,280.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=MT_pre__Female_S(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj69.MT_pivotOut__.setValue('')
    self.obj69.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj69.MT_subtypeMatching__.setValue(('True', 0))
    self.obj69.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj69.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj69.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj69.MT_pivotIn__.setValue('')
    self.obj69.MT_pivotIn__.setNone()

    # MT_label__
    self.obj69.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj69.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj69.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj69.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj69.MT_pre__name.setHeight(15)

    self.obj69.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(760.0,280.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj82=MT_pre__Female_T(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj82.MT_subtypeMatching__.setValue(('True', 0))
    self.obj82.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj82.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj82.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj82.MT_pivotIn__.setValue('')
    self.obj82.MT_pivotIn__.setNone()

    # MT_label__
    self.obj82.MT_label__.setValue('3')

    # MT_pre__name
    self.obj82.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj82.MT_pre__name.setHeight(15)

    self.obj82.graphClass_= graph_MT_pre__Female_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_T(560.0,460.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=MT_pre__Female_T(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj83.MT_subtypeMatching__.setValue(('True', 0))
    self.obj83.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj83.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj83.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj83.MT_pivotIn__.setValue('')
    self.obj83.MT_pivotIn__.setNone()

    # MT_label__
    self.obj83.MT_label__.setValue('4')

    # MT_pre__name
    self.obj83.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj83.MT_pre__name.setHeight(15)

    self.obj83.graphClass_= graph_MT_pre__Female_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_T(760.0,460.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj10074=MT_pre__indirectLink_S(self)
    self.obj10074.isGraphObjectVisual = True

    if(hasattr(self.obj10074, '_setHierarchicalLink')):
      self.obj10074._setHierarchicalLink(False)

    # MT_label__
    self.obj10074.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj10074.MT_pivotOut__.setValue('')
    self.obj10074.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj10074.MT_subtypeMatching__.setValue(('True', 0))
    self.obj10074.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj10074.MT_pivotIn__.setValue('')
    self.obj10074.MT_pivotIn__.setNone()

    self.obj10074.graphClass_= graph_MT_pre__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__indirectLink_S(721.0,321.0,self.obj10074)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj10074.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj10074)
    self.globalAndLocalPostcondition(self.obj10074, rootNode)
    self.obj10074.postAction( rootNode.CREATE )

    self.obj88=MT_pre__trace_link(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # MT_label__
    self.obj88.MT_label__.setValue('5')

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
       new_obj = graph_MT_pre__trace_link(621.0,411.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=MT_pre__trace_link(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # MT_label__
    self.obj89.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj89.MT_pivotOut__.setValue('')
    self.obj89.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj89.MT_subtypeMatching__.setValue(('True', 0))
    self.obj89.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj89.MT_pivotIn__.setValue('')
    self.obj89.MT_pivotIn__.setNone()

    self.obj89.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(821.0,411.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj114=MT_post__indirectLink_S(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # MT_label__
    self.obj114.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj114.MT_pivotOut__.setValue('')
    self.obj114.MT_pivotOut__.setNone()

    self.obj114.graphClass_= graph_MT_post__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__indirectLink_S(1231.0,321.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj121=MT_post__directLink_T(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # MT_label__
    self.obj121.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj121.MT_pivotOut__.setValue('')
    self.obj121.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj121.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj121.MT_post__associationType.setHeight(15)

    self.obj121.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(1231.0,501.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj84=MT_post__Female_S(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # MT_label__
    self.obj84.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj84.MT_pivotOut__.setValue('')
    self.obj84.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj84.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj84.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj84.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj84.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj84.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj84.MT_post__name.setHeight(15)

    self.obj84.graphClass_= graph_MT_post__Female_S
    if self.genGraphics:
       new_obj = graph_MT_post__Female_S(1080.0,280.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=MT_post__Female_S(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # MT_label__
    self.obj85.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj85.MT_pivotOut__.setValue('')
    self.obj85.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj85.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj85.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj85.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj85.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj85.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj85.MT_post__name.setHeight(15)

    self.obj85.graphClass_= graph_MT_post__Female_S
    if self.genGraphics:
       new_obj = graph_MT_post__Female_S(1260.0,280.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=MT_post__Female_T(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # MT_label__
    self.obj86.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj86.MT_pivotOut__.setValue('')
    self.obj86.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj86.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj86.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj86.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj86.MT_post__name.setHeight(15)

    self.obj86.graphClass_= graph_MT_post__Female_T
    if self.genGraphics:
       new_obj = graph_MT_post__Female_T(1080.0,460.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=MT_post__Female_T(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj87.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj87.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__name.setHeight(15)

    self.obj87.graphClass_= graph_MT_post__Female_T
    if self.genGraphics:
       new_obj = graph_MT_post__Female_T(1260.0,460.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj104=MT_post__trace_link(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # MT_label__
    self.obj104.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj104.MT_pivotOut__.setValue('')
    self.obj104.MT_pivotOut__.setNone()

    self.obj104.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1141.0,411.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=MT_post__trace_link(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # MT_label__
    self.obj105.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj105.MT_pivotOut__.setValue('')
    self.obj105.MT_pivotOut__.setNone()

    self.obj105.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1321.0,411.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj65=RHS(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # action
    self.obj65.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj65.action.setHeight(15)

    self.obj65.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(940.0,200.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj63=LHS(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # constraint
    self.obj63.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj63.constraint.setHeight(15)

    self.obj63.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(500.0,200.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    # Connections for obj68 (graphObject_: Obj6) of type MT_pre__Female_S
    self.drawConnections(
(self.obj68,self.obj10074,[621.0, 321.0, 721.0, 321.0],"true", 2) )
    # Connections for obj69 (graphObject_: Obj7) of type MT_pre__Female_S
    self.drawConnections(
 )
    # Connections for obj82 (graphObject_: Obj12) of type MT_pre__Female_T
    self.drawConnections(
(self.obj82,self.obj88,[621.0, 501.0, 621.0, 411.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj13) of type MT_pre__Female_T
    self.drawConnections(
(self.obj83,self.obj89,[821.0, 501.0, 821.0, 411.0],"true", 2) )
    # Connections for obj10074 (graphObject_: Obj26) of type MT_pre__indirectLink_S
    self.drawConnections(
(self.obj10074,self.obj69,[721.0, 321.0, 821.0, 321.0],"true", 2) )
    # Connections for obj88 (graphObject_: Obj18) of type MT_pre__trace_link
    self.drawConnections(
(self.obj88,self.obj68,[621.0, 411.0, 621.0, 321.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj19) of type MT_pre__trace_link
    self.drawConnections(
(self.obj89,self.obj69,[821.0, 411.0, 821.0, 321.0],"true", 2) )
    # Connections for obj114 (graphObject_: Obj24) of type MT_post__indirectLink_S
    self.drawConnections(
(self.obj114,self.obj85,[1231.0, 321.0, 1321.0, 321.0],"true", 2) )
    # Connections for obj121 (graphObject_: Obj25) of type MT_post__directLink_T
    self.drawConnections(
(self.obj121,self.obj87,[1231.0, 501.0, 1321.0, 501.0],"true", 2) )
    # Connections for obj84 (graphObject_: Obj14) of type MT_post__Female_S
    self.drawConnections(
(self.obj84,self.obj114,[1141.0, 321.0, 1231.0, 321.0],"true", 2) )
    # Connections for obj85 (graphObject_: Obj15) of type MT_post__Female_S
    self.drawConnections(
 )
    # Connections for obj86 (graphObject_: Obj16) of type MT_post__Female_T
    self.drawConnections(
(self.obj86,self.obj104,[1141.0, 501.0, 1141.0, 411.0],"true", 2),
(self.obj86,self.obj121,[1141.0, 501.0, 1231.0, 501.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj17) of type MT_post__Female_T
    self.drawConnections(
(self.obj87,self.obj105,[1321.0, 501.0, 1321.0, 411.0],"true", 2) )
    # Connections for obj104 (graphObject_: Obj22) of type MT_post__trace_link
    self.drawConnections(
(self.obj104,self.obj84,[1141.0, 411.0, 1141.0, 321.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj23) of type MT_post__trace_link
    self.drawConnections(
(self.obj105,self.obj85,[1321.0, 411.0, 1321.0, 321.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj3) of type RHS
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj1) of type LHS
    self.drawConnections(
 )

newfunction = FF2FF_combine_1_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META', 'MT_post__PoliceStationMM_META']

atom3version = '0.3'
