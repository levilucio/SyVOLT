"""
__strip_matchmodel_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sat Jun  1 13:29:30 2013
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MatchModel import *
from MT_pre__MetaModelElement_S import *
from MT_pre__match_contains import *
from MT_post__MetaModelElement_S import *
from MT_post__MatchModel import *
from RHS import *
from LHS import *
from graph_MT_pre__MetaModelElement_S import *
from graph_MT_post__MetaModelElement_S import *
from graph_LHS import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_MT_post__MatchModel import *
from graph_RHS import *
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

def strip_matchmodel_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MT_post__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MT_post__GM2AUTOSAR_MM ---
    if( MT_post__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_post__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_post__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_post__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_post__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_post__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('StripMatchModel')
    # --- ASG attributes over ---


    self.obj87=MT_pre__MatchModel(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj87.MT_subtypeMatching__.setValue(('True', 0))
    self.obj87.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj87.MT_pivotIn__.setValue('')
    self.obj87.MT_pivotIn__.setNone()

    self.obj87.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(281.0,192.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=MT_pre__MetaModelElement_S(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj88.MT_pivotOut__.setValue('')
    self.obj88.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj88.MT_subtypeMatching__.setValue(('True', 1))
    self.obj88.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj88.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj88.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj88.MT_pivotIn__.setValue('')
    self.obj88.MT_pivotIn__.setNone()

    # MT_label__
    self.obj88.MT_label__.setValue('2')

    # MT_pre__name
    self.obj88.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj88.MT_pre__name.setHeight(15)

    self.obj88.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(281.0,332.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=MT_pre__match_contains(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # MT_label__
    self.obj89.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj89.MT_pivotOut__.setValue('')
    self.obj89.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj89.MT_subtypeMatching__.setValue(('True', 0))
    self.obj89.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj89.MT_pivotIn__.setValue('')
    self.obj89.MT_pivotIn__.setNone()

    self.obj89.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(445.5,335.5,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj95=MT_post__MetaModelElement_S(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # MT_label__
    self.obj95.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj95.MT_pivotOut__.setValue('')
    self.obj95.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj95.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj95.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj95.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj95.MT_post__name.setHeight(15)

    self.obj95.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(780.0,320.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj90=MT_post__MatchModel(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # MT_label__
    self.obj90.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj90.MT_pivotOut__.setValue('')
    self.obj90.MT_pivotOut__.setNone()

    self.obj90.graphClass_= graph_MT_post__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_post__MatchModel(780.0,180.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=RHS(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # action
    self.obj91.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj91.action.setHeight(15)

    self.obj91.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(580.0,120.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=LHS(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # constraint
    self.obj92.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj92.constraint.setHeight(15)

    self.obj92.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(160.0,120.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    # Connections for obj87 (graphObject_: Obj0) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj87,self.obj89,[440.0, 265.0, 445.5, 335.5],"true", 2) )
    # Connections for obj88 (graphObject_: Obj1) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj89 (graphObject_: Obj2) of type MT_pre__match_contains
    self.drawConnections(
(self.obj89,self.obj88,[445.5, 335.5, 451.0, 406.0],"true", 2) )
    # Connections for obj95 (graphObject_: Obj7) of type MT_post__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj90 (graphObject_: Obj3) of type MT_post__MatchModel
    self.drawConnections(
 )
    # Connections for obj91 (graphObject_: Obj4) of type RHS
    self.drawConnections(
 )
    # Connections for obj92 (graphObject_: Obj5) of type LHS
    self.drawConnections(
 )

newfunction = strip_matchmodel_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MT_post__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
