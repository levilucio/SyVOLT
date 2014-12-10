"""
__rewrite_double_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Nov 28 09:14:40 2014
____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Male_S import *
from MT_pre__Station_T import *
from MT_pre__Male_T import *
from MT_pre__backward_link import *
from MT_post__directLink_S import *
from MT_post__directLink_T import *
from MT_post__backward_link import *
from MT_post__Station_S import *
from MT_post__Male_T import *
from MT_post__Male_S import *
from MT_post__Station_T import *
from RHS import *
from LHS import *
from graph_MT_pre__Male_T import *
from graph_MT_post__Male_S import *
from graph_MT_post__Male_T import *
from graph_MT_pre__Male_S import *
from graph_LHS import *
from graph_MT_post__directLink_S import *
from graph_MT_post__directLink_T import *
from graph_MT_post__Station_T import *
from graph_MT_pre__backward_link import *
from graph_MT_post__backward_link import *
from graph_MT_pre__Station_T import *
from graph_MT_post__Station_S import *
from graph_RHS import *
from graph_MT_pre__Station_S import *
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

def rewrite_double_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None, MT_post__PoliceStationMMRootNode=None):

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
        MoTifRuleRootNode.name.setValue('rewrite_double')
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


    self.obj42=MT_pre__Station_S(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42.MT_pivotOut__.setValue('')
    self.obj42.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42.MT_pivotIn__.setValue('')
    self.obj42.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj42.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj42.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42.MT_pre__name.setHeight(15)

    self.obj42.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(275.0,209.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=MT_pre__Male_S(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj43.MT_pivotOut__.setValue('')
    self.obj43.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj43.MT_subtypeMatching__.setValue(('True', 0))
    self.obj43.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj43.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj43.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj43.MT_pivotIn__.setValue('')
    self.obj43.MT_pivotIn__.setNone()

    # MT_label__
    self.obj43.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj43.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj43.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj43.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj43.MT_pre__name.setHeight(15)

    self.obj43.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(495.0,209.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=MT_pre__Station_T(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj44.MT_pivotOut__.setValue('')
    self.obj44.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj44.MT_subtypeMatching__.setValue(('True', 0))
    self.obj44.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj44.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj44.MT_pivotIn__.setValue('')
    self.obj44.MT_pivotIn__.setNone()

    # MT_label__
    self.obj44.MT_label__.setValue('3')

    # MT_pre__name
    self.obj44.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__name.setHeight(15)

    self.obj44.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(275.0,369.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=MT_pre__Male_T(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj45.MT_pivotOut__.setValue('')
    self.obj45.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj45.MT_subtypeMatching__.setValue(('True', 0))
    self.obj45.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj45.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj45.MT_pivotIn__.setValue('')
    self.obj45.MT_pivotIn__.setNone()

    # MT_label__
    self.obj45.MT_label__.setValue('4')

    # MT_pre__name
    self.obj45.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__name.setHeight(15)

    self.obj45.graphClass_= graph_MT_pre__Male_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_T(495.0,369.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj55=MT_pre__backward_link(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_label__
    self.obj55.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    self.obj55.graphClass_= graph_MT_pre__backward_link
    if self.genGraphics:
       new_obj = graph_MT_pre__backward_link(336.0,330.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=MT_pre__backward_link(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_label__
    self.obj56.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    self.obj56.graphClass_= graph_MT_pre__backward_link
    if self.genGraphics:
       new_obj = graph_MT_pre__backward_link(556.0,330.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj76=MT_post__directLink_S(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_label__
    self.obj76.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj76.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj76.MT_post__associationType.setHeight(15)

    self.obj76.graphClass_= graph_MT_post__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_S(951.0,241.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=MT_post__directLink_T(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_label__
    self.obj77.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj77.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj77.MT_post__associationType.setHeight(15)

    self.obj77.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(951.0,401.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj74=MT_post__backward_link(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_label__
    self.obj74.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    self.obj74.graphClass_= graph_MT_post__backward_link
    if self.genGraphics:
       new_obj = graph_MT_post__backward_link(841.0,321.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=MT_post__backward_link(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_label__
    self.obj75.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    self.obj75.graphClass_= graph_MT_post__backward_link
    if self.genGraphics:
       new_obj = graph_MT_post__backward_link(1061.0,321.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj69=MT_post__Station_S(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # MT_label__
    self.obj69.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj69.MT_pivotOut__.setValue('')
    self.obj69.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj69.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj69.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj69.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj69.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj69.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj69.MT_post__name.setHeight(15)

    self.obj69.graphClass_= graph_MT_post__Station_S
    if self.genGraphics:
       new_obj = graph_MT_post__Station_S(780.0,200.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj73=MT_post__Male_T(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_label__
    self.obj73.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('')
    self.obj73.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj73.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj73.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj73.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj73.MT_post__name.setHeight(15)

    self.obj73.graphClass_= graph_MT_post__Male_T
    if self.genGraphics:
       new_obj = graph_MT_post__Male_T(1000.0,360.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj71=MT_post__Male_S(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj71.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj71.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj71.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj71.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj71.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj71.MT_post__name.setHeight(15)

    self.obj71.graphClass_= graph_MT_post__Male_S
    if self.genGraphics:
       new_obj = graph_MT_post__Male_S(1000.0,200.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=MT_post__Station_T(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # MT_label__
    self.obj72.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj72.MT_pivotOut__.setValue('')
    self.obj72.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj72.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj72.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj72.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj72.MT_post__name.setHeight(15)

    self.obj72.graphClass_= graph_MT_post__Station_T
    if self.genGraphics:
       new_obj = graph_MT_post__Station_T(780.0,360.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj58=RHS(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # action
    self.obj58.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj58.action.setHeight(15)

    self.obj58.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(660.0,127.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj57=LHS(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # constraint
    self.obj57.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj57.constraint.setHeight(15)

    self.obj57.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(215.0,129.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    # Connections for obj42 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
 )
    # Connections for obj43 (graphObject_: Obj1) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj2) of type MT_pre__Station_T
    self.drawConnections(
(self.obj44,self.obj55,[336.0, 410.0, 336.0, 330.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj3) of type MT_pre__Male_T
    self.drawConnections(
(self.obj45,self.obj56,[556.0, 410.0, 556.0, 330.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj6) of type MT_pre__backward_link
    self.drawConnections(
(self.obj55,self.obj42,[336.0, 330.0, 336.0, 250.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj7) of type MT_pre__backward_link
    self.drawConnections(
(self.obj56,self.obj43,[556.0, 330.0, 556.0, 250.0],"true", 2) )
    # Connections for obj76 (graphObject_: Obj19) of type MT_post__directLink_S
    self.drawConnections(
(self.obj76,self.obj71,[951.0, 241.0, 1061.0, 241.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj20) of type MT_post__directLink_T
    self.drawConnections(
(self.obj77,self.obj73,[951.0, 401.0, 1061.0, 401.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj17) of type MT_post__backward_link
    self.drawConnections(
(self.obj74,self.obj69,[841.0, 321.0, 841.0, 241.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj18) of type MT_post__backward_link
    self.drawConnections(
(self.obj75,self.obj71,[1061.0, 321.0, 1061.0, 241.0],"true", 2) )
    # Connections for obj69 (graphObject_: Obj12) of type MT_post__Station_S
    self.drawConnections(
(self.obj69,self.obj76,[841.0, 241.0, 951.0, 241.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj16) of type MT_post__Male_T
    self.drawConnections(
(self.obj73,self.obj75,[1061.0, 401.0, 1061.0, 321.0],"true", 2) )
    # Connections for obj71 (graphObject_: Obj14) of type MT_post__Male_S
    self.drawConnections(
 )
    # Connections for obj72 (graphObject_: Obj15) of type MT_post__Station_T
    self.drawConnections(
(self.obj72,self.obj74,[841.0, 401.0, 841.0, 321.0],"true", 2),
(self.obj72,self.obj77,[841.0, 401.0, 951.0, 401.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj9) of type RHS
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj8) of type LHS
    self.drawConnections(
 )

newfunction = rewrite_double_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META', 'MT_post__PoliceStationMM_META']

atom3version = '0.3'
