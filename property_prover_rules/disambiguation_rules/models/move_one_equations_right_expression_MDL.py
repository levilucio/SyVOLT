"""
__move_one_equations_right_expression_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Jan  8 11:53:28 2015
_________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MetaModelElement_S import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__hasAttr_S import *
from MT_pre__rightExpr import *
from MT_post__Attribute import *
from MT_post__MetaModelElement_S import *
from MT_post__Equation import *
from MT_post__hasAttr_S import *
from MT_post__rightExpr import *
from RHS import *
from LHS import *
from graph_MT_pre__Equation import *
from graph_MT_post__MetaModelElement_S import *
from graph_MT_post__Attribute import *
from graph_LHS import *
from graph_MT_post__hasAttr_S import *
from graph_MT_pre__hasAttr_S import *
from graph_MT_post__Equation import *
from graph_MT_pre__MetaModelElement_S import *
from graph_MT_pre__rightExpr import *
from graph_RHS import *
from graph_MT_post__rightExpr import *
from graph_MT_pre__Attribute import *
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

def move_one_equations_right_expression_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None, MT_post__PoliceStationMMRootNode=None):

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
        MoTifRuleRootNode.name.setValue('MoveOneEquationsRightExpression')
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


    self.obj64=MT_pre__MetaModelElement_S(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj64.MT_pivotOut__.setValue('')
    self.obj64.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj64.MT_subtypeMatching__.setValue(('True', 0))
    self.obj64.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj64.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj64.MT_pivotIn__.setValue('')
    self.obj64.MT_pivotIn__.setNone()

    # MT_label__
    self.obj64.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj64.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj64.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__name.setHeight(15)

    self.obj64.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(124.0,162.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=MT_pre__MetaModelElement_S(self)
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
    self.obj65.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj65.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj65.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj65.MT_pre__name.setHeight(15)

    self.obj65.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(124.0,302.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj97=MT_pre__Attribute(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    # MT_label__
    self.obj97.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj97.MT_pivotOut__.setValue('')
    self.obj97.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj97.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj97.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj97.MT_subtypeMatching__.setValue(('True', 0))
    self.obj97.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj97.MT_pivotIn__.setValue('')
    self.obj97.MT_pivotIn__.setNone()

    self.obj97.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(304.0,162.0,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=MT_pre__Attribute(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    # MT_label__
    self.obj98.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj98.MT_pivotOut__.setValue('')
    self.obj98.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj98.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj98.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj98.MT_subtypeMatching__.setValue(('True', 0))
    self.obj98.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj98.MT_pivotIn__.setValue('')
    self.obj98.MT_pivotIn__.setNone()

    self.obj98.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(304.0,302.0,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj101=MT_pre__Equation(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # MT_label__
    self.obj101.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj101.MT_pivotOut__.setValue('')
    self.obj101.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj101.MT_subtypeMatching__.setValue(('True', 0))
    self.obj101.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj101.MT_pivotIn__.setValue('')
    self.obj101.MT_pivotIn__.setNone()

    self.obj101.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(420.0,160.0,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj99=MT_pre__hasAttr_S(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # MT_label__
    self.obj99.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj99.MT_pivotOut__.setValue('')
    self.obj99.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj99.MT_subtypeMatching__.setValue(('True', 0))
    self.obj99.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj99.MT_pivotIn__.setValue('')
    self.obj99.MT_pivotIn__.setNone()

    self.obj99.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(270.5,198.0,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=MT_pre__hasAttr_S(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    # MT_label__
    self.obj100.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj100.MT_pivotOut__.setValue('')
    self.obj100.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj100.MT_subtypeMatching__.setValue(('True', 0))
    self.obj100.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj100.MT_pivotIn__.setValue('')
    self.obj100.MT_pivotIn__.setNone()

    self.obj100.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(270.5,338.0,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj5531=MT_pre__rightExpr(self)
    self.obj5531.isGraphObjectVisual = True

    if(hasattr(self.obj5531, '_setHierarchicalLink')):
      self.obj5531._setHierarchicalLink(False)

    # MT_label__
    self.obj5531.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj5531.MT_pivotOut__.setValue('')
    self.obj5531.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj5531.MT_subtypeMatching__.setValue(('True', 0))
    self.obj5531.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj5531.MT_pivotIn__.setValue('')
    self.obj5531.MT_pivotIn__.setNone()

    self.obj5531.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(422.5,197.0,self.obj5531)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj5531.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5531)
    self.globalAndLocalPostcondition(self.obj5531, rootNode)
    self.obj5531.postAction( rootNode.CREATE )

    self.obj105=MT_post__Attribute(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # MT_label__
    self.obj105.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj105.MT_pivotOut__.setValue('')
    self.obj105.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj105.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj105.MT_post__name.setHeight(15)

    self.obj105.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(780.0,160.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=MT_post__Attribute(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # MT_label__
    self.obj106.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj106.MT_pivotOut__.setValue('')
    self.obj106.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj106.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj106.MT_post__name.setHeight(15)

    self.obj106.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(780.0,300.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj103=MT_post__MetaModelElement_S(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # MT_label__
    self.obj103.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj103.MT_pivotOut__.setValue('')
    self.obj103.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj103.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj103.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj103.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj103.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj103.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj103.MT_post__name.setHeight(15)

    self.obj103.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(640.0,160.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=MT_post__MetaModelElement_S(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # MT_label__
    self.obj104.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj104.MT_pivotOut__.setValue('')
    self.obj104.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj104.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj104.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj104.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj104.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj104.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj104.MT_post__name.setHeight(15)

    self.obj104.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(640.0,300.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj110=MT_post__Equation(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # MT_label__
    self.obj110.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj110.MT_pivotOut__.setValue('')
    self.obj110.MT_pivotOut__.setNone()

    self.obj110.graphClass_= graph_MT_post__Equation
    if self.genGraphics:
       new_obj = graph_MT_post__Equation(900.0,160.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj108=MT_post__hasAttr_S(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # MT_label__
    self.obj108.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj108.MT_pivotOut__.setValue('')
    self.obj108.MT_pivotOut__.setNone()

    self.obj108.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(786.5,196.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=MT_post__hasAttr_S(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # MT_label__
    self.obj109.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj109.MT_pivotOut__.setValue('')
    self.obj109.MT_pivotOut__.setNone()

    self.obj109.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(786.5,336.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj5534=MT_post__rightExpr(self)
    self.obj5534.isGraphObjectVisual = True

    if(hasattr(self.obj5534, '_setHierarchicalLink')):
      self.obj5534._setHierarchicalLink(False)

    # MT_label__
    self.obj5534.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj5534.MT_pivotOut__.setValue('')
    self.obj5534.MT_pivotOut__.setNone()

    self.obj5534.graphClass_= graph_MT_post__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_post__rightExpr(902.5,266.0,self.obj5534)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj5534.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5534)
    self.globalAndLocalPostcondition(self.obj5534, rootNode)
    self.obj5534.postAction( rootNode.CREATE )

    self.obj63=RHS(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # action
    self.obj63.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj63.action.setHeight(15)

    self.obj63.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(543.0,60.0,self.obj63)
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

    self.obj62=LHS(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # constraint
    self.obj62.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj62.constraint.setHeight(15)

    self.obj62.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,60.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    # Connections for obj64 (graphObject_: Obj2) of type MT_pre__MetaModelElement_S
    self.drawConnections(
(self.obj64,self.obj99,[184.0, 204.0, 270.5, 198.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj3) of type MT_pre__MetaModelElement_S
    self.drawConnections(
(self.obj65,self.obj100,[184.0, 344.0, 270.5, 338.0],"true", 2) )
    # Connections for obj97 (graphObject_: Obj15) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj98 (graphObject_: Obj16) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj101 (graphObject_: Obj19) of type MT_pre__Equation
    self.drawConnections(
(self.obj101,self.obj5531,[488.0, 202.0, 422.5, 197.0],"true", 2) )
    # Connections for obj99 (graphObject_: Obj17) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj99,self.obj97,[270.5, 198.0, 357.0, 192.0],"true", 2) )
    # Connections for obj100 (graphObject_: Obj18) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj100,self.obj98,[270.5, 338.0, 357.0, 332.0],"true", 2) )
    # Connections for obj5531 (graphObject_: Obj31) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj5531,self.obj97,[422.5, 197.0, 357.0, 192.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj23) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj106 (graphObject_: Obj24) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj103 (graphObject_: Obj21) of type MT_post__MetaModelElement_S
    self.drawConnections(
(self.obj103,self.obj108,[700.0, 202.0, 786.5, 196.0],"true", 2) )
    # Connections for obj104 (graphObject_: Obj22) of type MT_post__MetaModelElement_S
    self.drawConnections(
(self.obj104,self.obj109,[700.0, 342.0, 786.5, 336.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj28) of type MT_post__Equation
    self.drawConnections(
(self.obj110,self.obj5534,[972.0, 202.0, 902.5, 266.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj26) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj108,self.obj105,[786.5, 196.0, 833.0, 190.0],"true", 2) )
    # Connections for obj109 (graphObject_: Obj27) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj109,self.obj106,[786.5, 336.0, 833.0, 330.0],"true", 2) )
    # Connections for obj5534 (graphObject_: Obj32) of type MT_post__rightExpr
    self.drawConnections(
(self.obj5534,self.obj106,[902.5, 266.0, 833.0, 330.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj1) of type RHS
    self.drawConnections(
 )
    # Connections for obj62 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = move_one_equations_right_expression_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META', 'MT_post__PoliceStationMM_META']

atom3version = '0.3'
