"""
__property1_connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Wed May  6 14:41:19 2015
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ERModel import *
from MT_pre__EntityType import *
from MT_pre__Feature import *
from MT_pre__MatchModel import *
from MT_pre__match_contains import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__ERModel import *
from graph_LHS import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__EntityType import *
from graph_MT_pre__Feature import *
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

def property1_connected_MDL(self, rootNode, MT_pre__ERMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__ERMM ---
    if( MT_pre__ERMMRootNode ): 
        # author
        MT_pre__ERMMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__ERMMRootNode.description.setValue('\n')
        MT_pre__ERMMRootNode.description.setHeight(15)

        # name
        MT_pre__ERMMRootNode.name.setValue('')
        MT_pre__ERMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('property1_connected')
    # --- ASG attributes over ---


    self.obj56=MT_pre__ERModel(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_label__
    self.obj56.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj56.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj56.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj56.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    self.obj56.graphClass_= graph_MT_pre__ERModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ERModel(220.0,200.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ERModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=MT_pre__EntityType(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # MT_label__
    self.obj57.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj57.MT_pivotOut__.setValue('')
    self.obj57.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj57.MT_subtypeMatching__.setValue(('True', 0))
    self.obj57.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj57.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj57.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj57.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj57.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj57.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj57.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj57.MT_pivotIn__.setValue('')
    self.obj57.MT_pivotIn__.setNone()

    self.obj57.graphClass_= graph_MT_pre__EntityType
    if self.genGraphics:
       new_obj = graph_MT_pre__EntityType(380.0,200.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EntityType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=MT_pre__Feature(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # MT_label__
    self.obj58.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj58.MT_pivotOut__.setValue('')
    self.obj58.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj58.MT_subtypeMatching__.setValue(('True', 0))
    self.obj58.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj58.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj58.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj58.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj58.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj58.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj58.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj58.MT_pivotIn__.setValue('')
    self.obj58.MT_pivotIn__.setNone()

    self.obj58.graphClass_= graph_MT_pre__Feature
    if self.genGraphics:
       new_obj = graph_MT_pre__Feature(540.0,200.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Feature", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj67=MT_pre__MatchModel(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # MT_label__
    self.obj67.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj67.MT_pivotOut__.setValue('')
    self.obj67.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj67.MT_subtypeMatching__.setValue(('True', 0))
    self.obj67.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj67.MT_pivotIn__.setValue('')
    self.obj67.MT_pivotIn__.setNone()

    self.obj67.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(200.0,100.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj8404=MT_pre__match_contains(self)
    self.obj8404.isGraphObjectVisual = True

    if(hasattr(self.obj8404, '_setHierarchicalLink')):
      self.obj8404._setHierarchicalLink(False)

    # MT_label__
    self.obj8404.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj8404.MT_pivotOut__.setValue('')
    self.obj8404.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8404.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8404.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj8404.MT_pivotIn__.setValue('')
    self.obj8404.MT_pivotIn__.setNone()

    self.obj8404.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(280.5,191.5,self.obj8404)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj8404.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8404)
    self.globalAndLocalPostcondition(self.obj8404, rootNode)
    self.obj8404.postAction( rootNode.CREATE )

    self.obj8405=MT_pre__match_contains(self)
    self.obj8405.isGraphObjectVisual = True

    if(hasattr(self.obj8405, '_setHierarchicalLink')):
      self.obj8405._setHierarchicalLink(False)

    # MT_label__
    self.obj8405.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj8405.MT_pivotOut__.setValue('')
    self.obj8405.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8405.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8405.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj8405.MT_pivotIn__.setValue('')
    self.obj8405.MT_pivotIn__.setNone()

    self.obj8405.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(360.5,191.5,self.obj8405)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj8405.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8405)
    self.globalAndLocalPostcondition(self.obj8405, rootNode)
    self.obj8405.postAction( rootNode.CREATE )

    self.obj8406=MT_pre__match_contains(self)
    self.obj8406.isGraphObjectVisual = True

    if(hasattr(self.obj8406, '_setHierarchicalLink')):
      self.obj8406._setHierarchicalLink(False)

    # MT_label__
    self.obj8406.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj8406.MT_pivotOut__.setValue('')
    self.obj8406.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj8406.MT_subtypeMatching__.setValue(('True', 0))
    self.obj8406.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj8406.MT_pivotIn__.setValue('')
    self.obj8406.MT_pivotIn__.setNone()

    self.obj8406.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(440.5,191.5,self.obj8406)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj8406.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj8406)
    self.globalAndLocalPostcondition(self.obj8406, rootNode)
    self.obj8406.postAction( rootNode.CREATE )

    self.obj4233=MT_pre__directLink_S(self)
    self.obj4233.isGraphObjectVisual = True

    if(hasattr(self.obj4233, '_setHierarchicalLink')):
      self.obj4233._setHierarchicalLink(False)

    # MT_label__
    self.obj4233.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj4233.MT_pivotOut__.setValue('')
    self.obj4233.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4233.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4233.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4233.MT_pivotIn__.setValue('')
    self.obj4233.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj4233.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "entities"\n')
    self.obj4233.MT_pre__associationType.setHeight(15)

    self.obj4233.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(360.0,242.0,self.obj4233)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4233.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4233)
    self.globalAndLocalPostcondition(self.obj4233, rootNode)
    self.obj4233.postAction( rootNode.CREATE )

    self.obj4234=MT_pre__directLink_S(self)
    self.obj4234.isGraphObjectVisual = True

    if(hasattr(self.obj4234, '_setHierarchicalLink')):
      self.obj4234._setHierarchicalLink(False)

    # MT_label__
    self.obj4234.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj4234.MT_pivotOut__.setValue('')
    self.obj4234.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj4234.MT_subtypeMatching__.setValue(('True', 0))
    self.obj4234.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj4234.MT_pivotIn__.setValue('')
    self.obj4234.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj4234.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "features"\n')
    self.obj4234.MT_pre__associationType.setHeight(15)

    self.obj4234.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(520.0,242.0,self.obj4234)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj4234.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj4234)
    self.globalAndLocalPostcondition(self.obj4234, rootNode)
    self.obj4234.postAction( rootNode.CREATE )

    self.obj53=LHS(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # constraint
    self.obj53.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj53.constraint.setHeight(15)

    self.obj53.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(200.0,40.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    # Connections for obj56 (graphObject_: Obj3) of type MT_pre__ERModel
    self.drawConnections(
(self.obj56,self.obj4233,[280.0, 242.0, 360.0, 242.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj4) of type MT_pre__EntityType
    self.drawConnections(
(self.obj57,self.obj4234,[440.0, 242.0, 520.0, 242.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj5) of type MT_pre__Feature
    self.drawConnections(
 )
    # Connections for obj67 (graphObject_: Obj6) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj67,self.obj8404,[281.0, 141.0, 280.5, 191.5],"true", 2),
(self.obj67,self.obj8405,[281.0, 141.0, 360.5, 191.5],"true", 2),
(self.obj67,self.obj8406,[281.0, 141.0, 440.5, 191.5],"true", 2) )
    # Connections for obj8404 (graphObject_: Obj9) of type MT_pre__match_contains
    self.drawConnections(
(self.obj8404,self.obj56,[280.5, 191.5, 280.0, 242.0],"true", 2) )
    # Connections for obj8405 (graphObject_: Obj10) of type MT_pre__match_contains
    self.drawConnections(
(self.obj8405,self.obj57,[360.5, 191.5, 440.0, 242.0],"true", 2) )
    # Connections for obj8406 (graphObject_: Obj11) of type MT_pre__match_contains
    self.drawConnections(
(self.obj8406,self.obj58,[440.5, 191.5, 600.0, 242.0],"true", 2) )
    # Connections for obj4233 (graphObject_: Obj7) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj4233,self.obj57,[360.0, 242.0, 440.0, 242.0],"true", 2) )
    # Connections for obj4234 (graphObject_: Obj8) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj4234,self.obj58,[520.0, 242.0, 600.0, 242.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = property1_connected_MDL

loadedMMName = ['MT_pre__ERMM_META', 'MoTifRule_META']

atom3version = '0.3'
