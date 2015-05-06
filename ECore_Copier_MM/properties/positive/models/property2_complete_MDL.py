"""
__property2_complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Wed May  6 15:39:12 2015
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__EClass import *
from MT_pre__EStructuralFeature import *
from MT_pre__Attribute import *
from MT_pre__Equation import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from MT_pre__hasAttr_S import *
from MT_pre__hasAttr_T import *
from MT_pre__leftExpr import *
from MT_pre__rightExpr import *
from LHS import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__hasAttr_T import *
from graph_MT_pre__hasAttr_S import *
from graph_MT_pre__EStructuralFeature import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__EClass import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__leftExpr import *
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

def property2_complete_MDL(self, rootNode, MT_pre__ECoreMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__ECoreMM ---
    if( MT_pre__ECoreMMRootNode ): 
        # author
        MT_pre__ECoreMMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__ECoreMMRootNode.description.setValue('\n')
        MT_pre__ECoreMMRootNode.description.setHeight(15)

        # name
        MT_pre__ECoreMMRootNode.name.setValue('')
        MT_pre__ECoreMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('property2_complete')
    # --- ASG attributes over ---


    self.obj38=MT_pre__EClass(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # MT_label__
    self.obj38.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj38.MT_pivotOut__.setValue('')
    self.obj38.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj38.MT_subtypeMatching__.setValue(('True', 0))
    self.obj38.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj38.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj38.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj38.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj38.MT_pivotIn__.setValue('')
    self.obj38.MT_pivotIn__.setNone()

    self.obj38.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(340.0,180.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=MT_pre__EClass(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # MT_label__
    self.obj39.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj39.MT_pivotOut__.setValue('')
    self.obj39.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj39.MT_subtypeMatching__.setValue(('True', 0))
    self.obj39.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj39.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj39.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj39.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj39.MT_pivotIn__.setValue('')
    self.obj39.MT_pivotIn__.setNone()

    self.obj39.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(340.0,320.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=MT_pre__EStructuralFeature(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # MT_label__
    self.obj40.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj40.MT_pivotOut__.setValue('')
    self.obj40.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj40.MT_subtypeMatching__.setValue(('True', 1))
    self.obj40.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj40.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj40.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj40.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj40.MT_pivotIn__.setValue('')
    self.obj40.MT_pivotIn__.setNone()

    self.obj40.graphClass_= graph_MT_pre__EStructuralFeature
    if self.genGraphics:
       new_obj = graph_MT_pre__EStructuralFeature(500.0,180.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EStructuralFeature", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=MT_pre__EStructuralFeature(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # MT_label__
    self.obj41.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj41.MT_pivotOut__.setValue('')
    self.obj41.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj41.MT_subtypeMatching__.setValue(('True', 1))
    self.obj41.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj41.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj41.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj41.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj41.MT_pivotIn__.setValue('')
    self.obj41.MT_pivotIn__.setNone()

    self.obj41.graphClass_= graph_MT_pre__EStructuralFeature
    if self.genGraphics:
       new_obj = graph_MT_pre__EStructuralFeature(500.0,320.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EStructuralFeature", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj44=MT_pre__Attribute(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # MT_label__
    self.obj44.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj44.MT_pivotOut__.setValue('')
    self.obj44.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj44.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "name"\n')
    self.obj44.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj44.MT_subtypeMatching__.setValue(('True', 0))
    self.obj44.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj44.MT_pivotIn__.setValue('')
    self.obj44.MT_pivotIn__.setNone()

    self.obj44.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(420.0,100.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=MT_pre__Attribute(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # MT_label__
    self.obj45.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj45.MT_pivotOut__.setValue('')
    self.obj45.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj45.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "name"\n')
    self.obj45.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj45.MT_subtypeMatching__.setValue(('True', 0))
    self.obj45.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj45.MT_pivotIn__.setValue('')
    self.obj45.MT_pivotIn__.setNone()

    self.obj45.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(400.0,400.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=MT_pre__Equation(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # MT_label__
    self.obj46.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj46.MT_pivotOut__.setValue('')
    self.obj46.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj46.MT_subtypeMatching__.setValue(('True', 0))
    self.obj46.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj46.MT_pivotIn__.setValue('')
    self.obj46.MT_pivotIn__.setNone()

    self.obj46.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(420.0,260.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj51=MT_pre__directLink_T(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # MT_label__
    self.obj51.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj51.MT_pivotOut__.setValue('')
    self.obj51.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj51.MT_subtypeMatching__.setValue(('True', 0))
    self.obj51.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj51.MT_pivotIn__.setValue('')
    self.obj51.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj51.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj51.MT_pre__associationType.setHeight(15)

    self.obj51.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(480.0,362.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=MT_pre__directLink_S(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # MT_label__
    self.obj52.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj52.MT_pivotOut__.setValue('')
    self.obj52.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52.MT_pivotIn__.setValue('')
    self.obj52.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj52.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj52.MT_pre__associationType.setHeight(15)

    self.obj52.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(480.0,222.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=MT_pre__trace_link(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # MT_label__
    self.obj53.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj53.MT_pivotOut__.setValue('')
    self.obj53.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj53.MT_subtypeMatching__.setValue(('True', 0))
    self.obj53.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj53.MT_pivotIn__.setValue('')
    self.obj53.MT_pivotIn__.setNone()

    self.obj53.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(560.0,291.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=MT_pre__hasAttr_S(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # MT_label__
    self.obj54.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj54.MT_pivotOut__.setValue('')
    self.obj54.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj54.MT_subtypeMatching__.setValue(('True', 0))
    self.obj54.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj54.MT_pivotIn__.setValue('')
    self.obj54.MT_pivotIn__.setNone()

    self.obj54.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(436.5,176.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=MT_pre__hasAttr_T(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_label__
    self.obj55.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    self.obj55.graphClass_= graph_MT_pre__hasAttr_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_T(426.5,406.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=MT_pre__leftExpr(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_label__
    self.obj56.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    self.obj56.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(480.5,216.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=MT_pre__rightExpr(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # MT_label__
    self.obj57.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj57.MT_pivotOut__.setValue('')
    self.obj57.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj57.MT_subtypeMatching__.setValue(('True', 0))
    self.obj57.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj57.MT_pivotIn__.setValue('')
    self.obj57.MT_pivotIn__.setNone()

    self.obj57.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(470.5,376.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
       new_obj = graph_LHS(260.0,80.0,self.obj58)
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

    # Connections for obj38 (graphObject_: Obj0) of type MT_pre__EClass
    self.drawConnections(
(self.obj38,self.obj52,[400.0, 222.0, 480.0, 222.0],"true", 2),
(self.obj38,self.obj54,[400.0, 222.0, 436.5, 176.0],"true", 2) )
    # Connections for obj39 (graphObject_: Obj1) of type MT_pre__EClass
    self.drawConnections(
(self.obj39,self.obj51,[400.0, 362.0, 480.0, 362.0],"true", 2),
(self.obj39,self.obj55,[400.0, 362.0, 426.5, 406.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj2) of type MT_pre__EStructuralFeature
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj3) of type MT_pre__EStructuralFeature
    self.drawConnections(
(self.obj41,self.obj53,[560.0, 362.0, 560.0, 291.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj6) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj7) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj8) of type MT_pre__Equation
    self.drawConnections(
(self.obj46,self.obj56,[488.0, 302.0, 480.5, 216.0],"true", 2),
(self.obj46,self.obj57,[488.0, 302.0, 470.5, 376.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj13) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj51,self.obj41,[480.0, 362.0, 560.0, 362.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj14) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52,self.obj40,[480.0, 222.0, 560.0, 222.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj15) of type MT_pre__trace_link
    self.drawConnections(
(self.obj53,self.obj40,[560.0, 291.0, 560.0, 222.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj16) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj54,self.obj44,[436.5, 176.0, 473.0, 130.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj17) of type MT_pre__hasAttr_T
    self.drawConnections(
(self.obj55,self.obj45,[426.5, 406.0, 453.0, 430.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj18) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj56,self.obj44,[480.5, 216.0, 473.0, 130.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj19) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj57,self.obj45,[470.5, 376.0, 453.0, 430.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj20) of type LHS
    self.drawConnections(
 )

newfunction = property2_complete_MDL

loadedMMName = ['MT_pre__ECoreMM_META', 'MoTifRule_META']

atom3version = '0.3'
