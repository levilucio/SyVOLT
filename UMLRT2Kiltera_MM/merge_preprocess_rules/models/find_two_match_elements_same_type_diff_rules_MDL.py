"""
__find_two_match_elements_same_type_diff_rules_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Aug 22 11:40:12 2013
__________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MatchModel import *
from MT_pre__MetaModelElement_S import *
from MT_pre__match_contains import *
from LHS import *
from graph_MT_pre__MetaModelElement_S import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_LHS import *
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

def find_two_match_elements_same_type_diff_rules_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('FindTwoMatchElementsSameTypeDiffRules')
    # --- ASG attributes over ---


    self.obj71=MT_pre__MatchModel(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj71.MT_subtypeMatching__.setValue(('True', 0))
    self.obj71.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj71.MT_pivotIn__.setValue('')
    self.obj71.MT_pivotIn__.setNone()

    self.obj71.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(60.0,80.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=MT_pre__MetaModelElement_S(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj72.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj72.MT_subtypeMatching__.setValue(('True', 1))
    self.obj72.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj72.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj72.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj72.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj72.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj72.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__name.setHeight(15)

    self.obj72.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(60.0,180.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=MT_pre__MetaModelElement_S(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj73.MT_subtypeMatching__.setValue(('True', 1))
    self.obj73.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj73.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj73.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__name.setHeight(15)

    self.obj73.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(280.0,180.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=MT_pre__match_contains(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_label__
    self.obj74.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj74.MT_subtypeMatching__.setValue(('True', 0))
    self.obj74.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj74.MT_pivotIn__.setValue('')
    self.obj74.MT_pivotIn__.setNone()

    self.obj74.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(227.0,263.5,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj80=LHS(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # constraint
    self.obj80.constraint.setValue('if PreNode(\'1\')[\'classtype\'] == PreNode(\'2\')[\'classtype\']:\n    if len([i for i in graph.neighbors(PreNode(\'2\').index) if graph.vs[i][\'mm__\'] == \'match_contains\']) == 0:\n    	return True\n\nreturn False\n')
    self.obj80.constraint.setHeight(15)

    self.obj80.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    # Connections for obj71 (graphObject_: Obj0) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj71,self.obj74,[219.0, 153.0, 227.0, 263.5],"true", 2) )
    # Connections for obj72 (graphObject_: Obj1) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj73 (graphObject_: Obj2) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj3) of type MT_pre__match_contains
    self.drawConnections(
(self.obj74,self.obj72,[227.0, 263.5, 230.0, 254.0],"true", 2) )
    # Connections for obj80 (graphObject_: Obj9) of type LHS
    self.drawConnections(
 )

newfunction = find_two_match_elements_same_type_diff_rules_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
