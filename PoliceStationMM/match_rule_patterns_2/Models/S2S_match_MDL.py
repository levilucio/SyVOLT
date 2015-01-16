"""
__S2S_match_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Jan 15 22:03:39 2015
_______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Attribute import *
from MT_pre__hasAttr_S import *
from MT_post__Attribute import *
from MT_post__Equation import *
from MT_post__hasAttr_S import *
from MT_post__Constant import *
from MT_post__Station_T import *
from MT_post__trace_link import *
from MT_post__rightExpr import *
from MT_post__Station_S import *
from MT_post__leftExpr import *
from RHS import *
from LHS import *
from graph_MT_post__leftExpr import *
from graph_MT_post__Attribute import *
from graph_LHS import *
from graph_MT_post__Constant import *
from graph_MT_post__hasAttr_S import *
from graph_MT_pre__hasAttr_S import *
from graph_MT_post__Equation import *
from graph_MT_post__Station_T import *
from graph_MT_pre__Station_S import *
from graph_MT_post__Station_S import *
from graph_RHS import *
from graph_MT_post__rightExpr import *
from graph_MT_pre__Attribute import *
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

def S2S_match_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None, MT_post__PoliceStationMMRootNode=None):

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
        MoTifRuleRootNode.name.setValue('S2S_match')
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


    self.obj59=MT_pre__Station_S(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj59.MT_pivotOut__.setValue('')
    self.obj59.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj59.MT_subtypeMatching__.setValue(('True', 0))
    self.obj59.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj59.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj59.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj59.MT_pivotIn__.setValue('')
    self.obj59.MT_pivotIn__.setNone()

    # MT_label__
    self.obj59.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj59.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj59.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj59.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj59.MT_pre__name.setHeight(15)

    self.obj59.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(520.0,220.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj65=MT_pre__Attribute(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # MT_label__
    self.obj65.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj65.MT_pivotOut__.setValue('')
    self.obj65.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj65.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\nif attr_value == "name":\n    return True\n\nreturn False\n')
    self.obj65.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj65.MT_subtypeMatching__.setValue(('True', 0))
    self.obj65.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj65.MT_pivotIn__.setValue('')
    self.obj65.MT_pivotIn__.setNone()

    self.obj65.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(720.0,220.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=MT_pre__hasAttr_S(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # MT_label__
    self.obj66.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj66.MT_pivotOut__.setValue('')
    self.obj66.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj66.MT_subtypeMatching__.setValue(('True', 0))
    self.obj66.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj66.MT_pivotIn__.setValue('')
    self.obj66.MT_pivotIn__.setNone()

    self.obj66.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(677.0,255.5,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj73=MT_post__Attribute(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_label__
    self.obj73.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('')
    self.obj73.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj73.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj73.MT_post__name.setHeight(15)

    self.obj73.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(1260.0,220.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj49877=MT_post__Equation(self)
    self.obj49877.isGraphObjectVisual = True

    if(hasattr(self.obj49877, '_setHierarchicalLink')):
      self.obj49877._setHierarchicalLink(False)

    # MT_label__
    self.obj49877.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj49877.MT_pivotOut__.setValue('')
    self.obj49877.MT_pivotOut__.setNone()

    self.obj49877.graphClass_= graph_MT_post__Equation
    if self.genGraphics:
       new_obj = graph_MT_post__Equation(1240.0,300.0,self.obj49877)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49877.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49877)
    self.globalAndLocalPostcondition(self.obj49877, rootNode)
    self.obj49877.postAction( rootNode.CREATE )

    self.obj76=MT_post__hasAttr_S(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_label__
    self.obj76.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    self.obj76.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(1228.0,253.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj78=MT_post__Constant(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # MT_label__
    self.obj78.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj78.MT_pivotOut__.setValue('')
    self.obj78.MT_pivotOut__.setNone()

    # MT_post__value
    self.obj78.MT_post__value.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "somestation"\n')
    self.obj78.MT_post__value.setHeight(15)

    self.obj78.graphClass_= graph_MT_post__Constant
    if self.genGraphics:
       new_obj = graph_MT_post__Constant(1260.0,400.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj62=MT_post__Station_T(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # MT_label__
    self.obj62.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj62.MT_pivotOut__.setValue('')
    self.obj62.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj62.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj62.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj62.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj62.MT_post__name.setHeight(15)

    self.obj62.graphClass_= graph_MT_post__Station_T
    if self.genGraphics:
       new_obj = graph_MT_post__Station_T(1082.0,395.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=MT_post__trace_link(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # MT_label__
    self.obj63.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj63.MT_pivotOut__.setValue('')
    self.obj63.MT_pivotOut__.setNone()

    self.obj63.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1143.0,346.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj49879=MT_post__rightExpr(self)
    self.obj49879.isGraphObjectVisual = True

    if(hasattr(self.obj49879, '_setHierarchicalLink')):
      self.obj49879._setHierarchicalLink(False)

    # MT_label__
    self.obj49879.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj49879.MT_pivotOut__.setValue('')
    self.obj49879.MT_pivotOut__.setNone()

    self.obj49879.graphClass_= graph_MT_post__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_post__rightExpr(1313.5,390.5,self.obj49879)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49879.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49879)
    self.globalAndLocalPostcondition(self.obj49879, rootNode)
    self.obj49879.postAction( rootNode.CREATE )

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
       new_obj = graph_MT_post__Station_S(1082.0,215.0,self.obj64)
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

    self.obj49878=MT_post__leftExpr(self)
    self.obj49878.isGraphObjectVisual = True

    if(hasattr(self.obj49878, '_setHierarchicalLink')):
      self.obj49878._setHierarchicalLink(False)

    # MT_label__
    self.obj49878.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj49878.MT_pivotOut__.setValue('')
    self.obj49878.MT_pivotOut__.setNone()

    self.obj49878.graphClass_= graph_MT_post__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_post__leftExpr(1312.5,296.0,self.obj49878)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49878.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49878)
    self.globalAndLocalPostcondition(self.obj49878, rootNode)
    self.obj49878.postAction( rootNode.CREATE )

    self.obj15031=RHS(self)
    self.obj15031.isGraphObjectVisual = True

    if(hasattr(self.obj15031, '_setHierarchicalLink')):
      self.obj15031._setHierarchicalLink(False)

    # action
    self.obj15031.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj15031.action.setHeight(15)

    self.obj15031.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(920.0,100.0,self.obj15031)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15031.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15031)
    self.globalAndLocalPostcondition(self.obj15031, rootNode)
    self.obj15031.postAction( rootNode.CREATE )

    self.obj15030=LHS(self)
    self.obj15030.isGraphObjectVisual = True

    if(hasattr(self.obj15030, '_setHierarchicalLink')):
      self.obj15030._setHierarchicalLink(False)

    # constraint
    self.obj15030.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj15030.constraint.setHeight(15)

    self.obj15030.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(500.0,100.0,self.obj15030)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj15030.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj15030)
    self.globalAndLocalPostcondition(self.obj15030, rootNode)
    self.obj15030.postAction( rootNode.CREATE )

    # Connections for obj59 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
(self.obj59,self.obj66,[581.0, 261.0, 677.0, 255.5],"true", 2) )
    # Connections for obj65 (graphObject_: Obj6) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj66 (graphObject_: Obj7) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj66,self.obj65,[677.0, 255.5, 773.0, 250.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj8) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj49877 (graphObject_: Obj32) of type MT_post__Equation
    self.drawConnections(
(self.obj49877,self.obj49878,[1312.0, 342.0, 1312.5, 296.0],"true", 2),
(self.obj49877,self.obj49879,[1312.0, 342.0, 1313.5, 390.5],"true", 2) )
    # Connections for obj76 (graphObject_: Obj9) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj76,self.obj73,[1228.0, 253.0, 1313.0, 250.0],"true", 2) )
    # Connections for obj78 (graphObject_: Obj11) of type MT_post__Constant
    self.drawConnections(
 )
    # Connections for obj62 (graphObject_: Obj3) of type MT_post__Station_T
    self.drawConnections(
(self.obj62,self.obj63,[1143.0, 436.0, 1143.0, 346.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj4) of type MT_post__trace_link
    self.drawConnections(
(self.obj63,self.obj64,[1143.0, 346.0, 1143.0, 256.0],"true", 2) )
    # Connections for obj49879 (graphObject_: Obj34) of type MT_post__rightExpr
    self.drawConnections(
(self.obj49879,self.obj78,[1313.5, 390.5, 1315.0, 439.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj5) of type MT_post__Station_S
    self.drawConnections(
(self.obj64,self.obj76,[1143.0, 256.0, 1228.0, 253.0],"true", 2) )
    # Connections for obj49878 (graphObject_: Obj33) of type MT_post__leftExpr
    self.drawConnections(
(self.obj49878,self.obj73,[1312.5, 296.0, 1313.0, 250.0],"true", 2) )
    # Connections for obj15031 (graphObject_: Obj29) of type RHS
    self.drawConnections(
 )
    # Connections for obj15030 (graphObject_: Obj28) of type LHS
    self.drawConnections(
 )

newfunction = S2S_match_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META', 'MT_post__PoliceStationMM_META']

atom3version = '0.3'
