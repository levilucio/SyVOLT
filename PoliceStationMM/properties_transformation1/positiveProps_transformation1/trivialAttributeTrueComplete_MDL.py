"""
__trivialAttributeTrueComplete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb  9 19:15:25 2015
__________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Female_T import *
from MT_pre__Female_S import *
from MT_pre__Attribute import *
from MT_pre__rightExpr import *
from MT_pre__hasAttr_T import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from MT_pre__hasAttr_S import *
from graph_MT_pre__Equation import *
from graph_MT_pre__Female_T import *
from graph_LHS import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__hasAttr_T import *
from graph_MT_pre__hasAttr_S import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__Female_S import *
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

def trivialAttributeTrueComplete_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('trivialAttributeTrueComplete')
    # --- ASG attributes over ---


    self.obj70=LHS(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # constraint
    self.obj70.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj70.constraint.setHeight(15)

    self.obj70.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,40.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj72=MT_pre__Female_T(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj72.MT_pivotOut__.setValue('')
    self.obj72.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj72.MT_subtypeMatching__.setValue(('True', 0))
    self.obj72.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj72.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj72.MT_pivotIn__.setValue('')
    self.obj72.MT_pivotIn__.setNone()

    # MT_label__
    self.obj72.MT_label__.setValue('2')

    # MT_pre__name
    self.obj72.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__name.setHeight(15)

    self.obj72.graphClass_= graph_MT_pre__Female_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_T(40.0,340.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj71=MT_pre__Female_S(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj71.MT_subtypeMatching__.setValue(('True', 0))
    self.obj71.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj71.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj71.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj71.MT_pivotIn__.setValue('')
    self.obj71.MT_pivotIn__.setNone()

    # MT_label__
    self.obj71.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj71.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj71.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj71.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj71.MT_pre__name.setHeight(15)

    self.obj71.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(40.0,60.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj78=MT_pre__Attribute(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # MT_label__
    self.obj78.MT_label__.setValue('name')

    # MT_pivotOut__
    self.obj78.MT_pivotOut__.setValue('')
    self.obj78.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj78.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj78.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj78.MT_subtypeMatching__.setValue(('True', 0))
    self.obj78.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj78.MT_pivotIn__.setValue('')
    self.obj78.MT_pivotIn__.setNone()

    self.obj78.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,60.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj83=MT_pre__Attribute(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_label__
    self.obj83.MT_label__.setValue('name')

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj83.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj83.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj83.MT_subtypeMatching__.setValue(('True', 0))
    self.obj83.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj83.MT_pivotIn__.setValue('')
    self.obj83.MT_pivotIn__.setNone()

    self.obj83.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(240.0,360.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj82=MT_pre__rightExpr(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_label__
    self.obj82.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj82.MT_subtypeMatching__.setValue(('True', 0))
    self.obj82.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj82.MT_pivotIn__.setValue('')
    self.obj82.MT_pivotIn__.setNone()

    self.obj82.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(370.5,156.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj87=MT_pre__hasAttr_T(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj87.MT_subtypeMatching__.setValue(('True', 0))
    self.obj87.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj87.MT_pivotIn__.setValue('')
    self.obj87.MT_pivotIn__.setNone()

    self.obj87.graphClass_= graph_MT_pre__hasAttr_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_T(197.0,385.5,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj86=MT_pre__leftExpr(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # MT_label__
    self.obj86.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj86.MT_pivotOut__.setValue('')
    self.obj86.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj86.MT_subtypeMatching__.setValue(('True', 0))
    self.obj86.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj86.MT_pivotIn__.setValue('')
    self.obj86.MT_pivotIn__.setNone()

    self.obj86.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(360.5,306.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj75=MT_pre__Equation(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_label__
    self.obj75.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj75.MT_subtypeMatching__.setValue(('True', 0))
    self.obj75.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj75.MT_pivotIn__.setValue('')
    self.obj75.MT_pivotIn__.setNone()

    self.obj75.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(360.0,180.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj81=MT_pre__hasAttr_S(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj81.MT_subtypeMatching__.setValue(('True', 0))
    self.obj81.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj81.MT_pivotIn__.setValue('')
    self.obj81.MT_pivotIn__.setNone()

    self.obj81.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(207.0,95.5,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    # Connections for obj70 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )
    # Connections for obj72 (graphObject_: Obj6) of type MT_pre__Female_T
    self.drawConnections(
(self.obj72,self.obj87,[101.0, 381.0, 197.0, 385.5],"true", 2) )
    # Connections for obj71 (graphObject_: Obj5) of type MT_pre__Female_S
    self.drawConnections(
(self.obj71,self.obj81,[101.0, 101.0, 207.0, 95.5],"true", 2) )
    # Connections for obj78 (graphObject_: Obj9) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj83 (graphObject_: Obj12) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj82 (graphObject_: Obj11) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj82,self.obj78,[370.5, 156.0, 313.0, 90.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj14) of type MT_pre__hasAttr_T
    self.drawConnections(
(self.obj87,self.obj83,[197.0, 385.5, 293.0, 390.0],"true", 2) )
    # Connections for obj86 (graphObject_: Obj13) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj86,self.obj83,[360.5, 306.0, 293.0, 390.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj8) of type MT_pre__Equation
    self.drawConnections(
(self.obj75,self.obj82,[428.0, 222.0, 370.5, 156.0],"true", 2),
(self.obj75,self.obj86,[428.0, 222.0, 360.5, 306.0],"true", 2) )
    # Connections for obj81 (graphObject_: Obj10) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj81,self.obj78,[207.0, 95.5, 313.0, 90.0],"true", 2) )

newfunction = trivialAttributeTrueComplete_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
