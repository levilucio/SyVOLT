"""
__nacExampleRule_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Dec  5 11:39:28 2014
____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Male_S import *
from MT_pre__Female_S import *
from MT_pre__directLink_S import *
from NAC import *
from RHS import *
from LHS import *
from MT_post__Station_S import *
from graph_MT_pre__Male_S import *
from graph_LHS import *
from graph_MT_pre__Station_S import *
from graph_MT_pre__directLink_S import *
from graph_MT_post__Station_S import *
from graph_RHS import *
from graph_MT_pre__Female_S import *
from graph_NAC import *
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

def nacExampleRule_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MT_post__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('nacExampleRule')
    # --- ASG attributes over ---


    self.obj49=MT_pre__Station_S(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj49.MT_pivotOut__.setValue('')
    self.obj49.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj49.MT_subtypeMatching__.setValue(('True', 0))
    self.obj49.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj49.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj49.MT_pivotIn__.setValue('')
    self.obj49.MT_pivotIn__.setNone()

    # MT_label__
    self.obj49.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj49.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj49.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__name.setHeight(15)

    self.obj49.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(480.0,480.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=MT_pre__Station_S(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj50.MT_pivotOut__.setValue('')
    self.obj50.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj50.MT_subtypeMatching__.setValue(('True', 0))
    self.obj50.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj50.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj50.MT_pivotIn__.setValue('')
    self.obj50.MT_pivotIn__.setNone()

    # MT_label__
    self.obj50.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj50.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj50.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__name.setHeight(15)

    self.obj50.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(60.0,480.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=MT_pre__Male_S(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj51.MT_pivotOut__.setValue('')
    self.obj51.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj51.MT_subtypeMatching__.setValue(('True', 0))
    self.obj51.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj51.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj51.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj51.MT_pivotIn__.setValue('')
    self.obj51.MT_pivotIn__.setNone()

    # MT_label__
    self.obj51.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj51.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj51.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj51.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj51.MT_pre__name.setHeight(15)

    self.obj51.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(680.0,480.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=MT_pre__Female_S(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52.MT_pivotOut__.setValue('')
    self.obj52.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52.MT_pivotIn__.setValue('')
    self.obj52.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj52.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__name.setHeight(15)

    self.obj52.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(280.0,480.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=MT_pre__directLink_S(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # MT_label__
    self.obj53.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj53.MT_pivotOut__.setValue('')
    self.obj53.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj53.MT_subtypeMatching__.setValue(('True', 0))
    self.obj53.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj53.MT_pivotIn__.setValue('')
    self.obj53.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj53.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj53.MT_pre__associationType.setHeight(15)

    self.obj53.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(641.0,521.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=MT_pre__directLink_S(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # MT_label__
    self.obj54.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj54.MT_pivotOut__.setValue('')
    self.obj54.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj54.MT_subtypeMatching__.setValue(('True', 0))
    self.obj54.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj54.MT_pivotIn__.setValue('')
    self.obj54.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj54.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__associationType.setHeight(15)

    self.obj54.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(231.0,521.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj56=NAC(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # constraint
    self.obj56.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the NAC have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True forbids the rule from being applied,\n#    returning False enables the rule to be applied.\n#===============================================================================\n\nreturn True\n')
    self.obj56.constraint.setHeight(15)

    self.obj56.graphClass_= graph_NAC
    if self.genGraphics:
       new_obj = graph_NAC(20.0,340,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("NAC", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0098039215686274, 0.9828431372549019]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=RHS(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # action
    self.obj57.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj57.action.setHeight(15)

    self.obj57.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(880.0,340.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=LHS(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # constraint
    self.obj58.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj58.constraint.setHeight(15)

    self.obj58.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(440.0,340.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj64=MT_post__Station_S(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # MT_label__
    self.obj64.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj64.MT_pivotOut__.setValue('')
    self.obj64.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj64.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj64.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj64.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj64.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj64.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj64.MT_post__name.setHeight(15)

    self.obj64.graphClass_= graph_MT_post__Station_S
    if self.genGraphics:
       new_obj = graph_MT_post__Station_S(1040.0,480.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    # Connections for obj49 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
(self.obj49,self.obj53,[541.0, 521.0, 641.0, 521.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj1) of type MT_pre__Station_S
    self.drawConnections(
(self.obj50,self.obj54,[121.0, 521.0, 231.0, 521.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj2) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj52 (graphObject_: Obj3) of type MT_pre__Female_S
    self.drawConnections(
 )
    # Connections for obj53 (graphObject_: Obj4) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj53,self.obj51,[641.0, 521.0, 741.0, 521.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj5) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj54,self.obj52,[231.0, 521.0, 341.0, 521.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj7) of type NAC
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj8) of type RHS
    self.drawConnections(
 )
    # Connections for obj58 (graphObject_: Obj9) of type LHS
    self.drawConnections(
 )
    # Connections for obj64 (graphObject_: Obj10) of type MT_post__Station_S
    self.drawConnections(
 )

newfunction = nacExampleRule_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MT_post__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
