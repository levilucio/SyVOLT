"""
__ExitPtConOPsOfExitPtSIB_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 19:01:45 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__Name import *
from MT_pre__State import *
from MT_pre__SIBLING0 import *
from MT_pre__Par import *
from MT_pre__rightExpr import *
from MT_pre__trace_link import *
from MT_pre__directLink_S import *
from MT_pre__Inst import *
from MT_pre__directLink_T import *
from MT_pre__hasAttribute_S import *
from MT_pre__Transition import *
from MT_pre__hasAttribute_T import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
from MT_pre__ExitPoint import *
from MT_pre__Trigger_T import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__Equation import *
from graph_MT_pre__Trigger_T import *
from graph_MT_pre__directLink_T import *
from graph_LHS import *
from graph_MT_pre__hasAttribute_T import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Name import *
from graph_MT_pre__Transition import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__Par import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__Inst import *
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

def ExitPtConOPsOfExitPtSIB_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__UMLRT2Kiltera_MM ---
    if( MT_pre__UMLRT2Kiltera_MMRootNode ): 
        # author
        MT_pre__UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setValue('')
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ExitPtConOPsOfExitPtSIB_Complete')
    # --- ASG attributes over ---


    self.obj21221=LHS(self)
    self.obj21221.isGraphObjectVisual = True

    if(hasattr(self.obj21221, '_setHierarchicalLink')):
      self.obj21221._setHierarchicalLink(False)

    # constraint
    self.obj21221.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\nif (PreNode(\'19\')[\'name\']==\'isComposite\')and (PreNode(\'22\')[\'name\']==\'true\') and (PreNode(\'25\')[\'name\']==\'channel\')and (PreNode(\'27\')[\'name\']==\'sh_in\'):\n   return True\nreturn False\n')
    self.obj21221.constraint.setHeight(15)

    self.obj21221.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(36.0,20.0,self.obj21221)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21221.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21221)
    self.globalAndLocalPostcondition(self.obj21221, rootNode)
    self.obj21221.postAction( rootNode.CREATE )

    self.obj21195=MT_pre__Name(self)
    self.obj21195.isGraphObjectVisual = True

    if(hasattr(self.obj21195, '_setHierarchicalLink')):
      self.obj21195._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21195.MT_pivotOut__.setValue('')
    self.obj21195.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21195.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21195.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21195.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21195.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21195.MT_pivotIn__.setValue('')
    self.obj21195.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21195.MT_label__.setValue('15')

    # MT_pre__cardinality
    self.obj21195.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21195.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21195.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21195.MT_pre__name.setHeight(15)

    self.obj21195.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(200.0,260.0,self.obj21195)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21195.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21195)
    self.globalAndLocalPostcondition(self.obj21195, rootNode)
    self.obj21195.postAction( rootNode.CREATE )

    self.obj21230=MT_pre__Name(self)
    self.obj21230.isGraphObjectVisual = True

    if(hasattr(self.obj21230, '_setHierarchicalLink')):
      self.obj21230._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21230.MT_pivotOut__.setValue('')
    self.obj21230.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21230.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21230.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21230.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21230.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21230.MT_pivotIn__.setValue('')
    self.obj21230.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21230.MT_label__.setValue('33')

    # MT_pre__cardinality
    self.obj21230.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21230.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21230.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21230.MT_pre__name.setHeight(15)

    self.obj21230.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(60.0,240.0,self.obj21230)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21230.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21230)
    self.globalAndLocalPostcondition(self.obj21230, rootNode)
    self.obj21230.postAction( rootNode.CREATE )

    self.obj21231=MT_pre__Name(self)
    self.obj21231.isGraphObjectVisual = True

    if(hasattr(self.obj21231, '_setHierarchicalLink')):
      self.obj21231._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21231.MT_pivotOut__.setValue('')
    self.obj21231.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21231.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21231.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21231.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21231.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21231.MT_pivotIn__.setValue('')
    self.obj21231.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21231.MT_label__.setValue('34')

    # MT_pre__cardinality
    self.obj21231.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21231.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21231.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21231.MT_pre__name.setHeight(15)

    self.obj21231.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(100.0,200.0,self.obj21231)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21231.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21231)
    self.globalAndLocalPostcondition(self.obj21231, rootNode)
    self.obj21231.postAction( rootNode.CREATE )

    self.obj21232=MT_pre__Name(self)
    self.obj21232.isGraphObjectVisual = True

    if(hasattr(self.obj21232, '_setHierarchicalLink')):
      self.obj21232._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21232.MT_pivotOut__.setValue('')
    self.obj21232.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21232.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21232.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21232.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21232.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21232.MT_pivotIn__.setValue('')
    self.obj21232.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21232.MT_label__.setValue('35')

    # MT_pre__cardinality
    self.obj21232.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21232.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21232.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21232.MT_pre__name.setHeight(15)

    self.obj21232.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(140.0,120.0,self.obj21232)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21232.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21232)
    self.globalAndLocalPostcondition(self.obj21232, rootNode)
    self.obj21232.postAction( rootNode.CREATE )

    self.obj21193=MT_pre__State(self)
    self.obj21193.isGraphObjectVisual = True

    if(hasattr(self.obj21193, '_setHierarchicalLink')):
      self.obj21193._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21193.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj21193.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21193.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21193.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21193.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21193.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj21193.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj21193.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21193.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21193.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21193.MT_pre__name.setHeight(15)

    self.obj21193.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj21193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21193.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21193)
    self.globalAndLocalPostcondition(self.obj21193, rootNode)
    self.obj21193.postAction( rootNode.CREATE )

    self.obj21224=MT_pre__SIBLING0(self)
    self.obj21224.isGraphObjectVisual = True

    if(hasattr(self.obj21224, '_setHierarchicalLink')):
      self.obj21224._setHierarchicalLink(False)

    # MT_label__
    self.obj21224.MT_label__.setValue('31')

    # MT_pivotOut__
    self.obj21224.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj21224.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21224.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21224.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21224.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21224.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21224.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21224.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21224.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21224.MT_pivotIn__.setValue('element4')

    self.obj21224.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(80.0,160.0,self.obj21224)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21224.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21224)
    self.globalAndLocalPostcondition(self.obj21224, rootNode)
    self.obj21224.postAction( rootNode.CREATE )

    self.obj21197=MT_pre__Par(self)
    self.obj21197.isGraphObjectVisual = True

    if(hasattr(self.obj21197, '_setHierarchicalLink')):
      self.obj21197._setHierarchicalLink(False)

    # MT_label__
    self.obj21197.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj21197.MT_pivotOut__.setValue('')
    self.obj21197.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21197.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21197.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21197.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21197.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21197.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21197.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21197.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21197.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21197.MT_pivotIn__.setValue('')
    self.obj21197.MT_pivotIn__.setNone()

    self.obj21197.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(60.0,200.0,self.obj21197)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21197.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21197)
    self.globalAndLocalPostcondition(self.obj21197, rootNode)
    self.obj21197.postAction( rootNode.CREATE )

    self.obj21219=MT_pre__rightExpr(self)
    self.obj21219.isGraphObjectVisual = True

    if(hasattr(self.obj21219, '_setHierarchicalLink')):
      self.obj21219._setHierarchicalLink(False)

    # MT_label__
    self.obj21219.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj21219.MT_pivotOut__.setValue('')
    self.obj21219.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21219.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21219.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21219.MT_pivotIn__.setValue('')
    self.obj21219.MT_pivotIn__.setNone()

    self.obj21219.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(350.0,331.0,self.obj21219)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21219.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21219)
    self.globalAndLocalPostcondition(self.obj21219, rootNode)
    self.obj21219.postAction( rootNode.CREATE )

    self.obj21220=MT_pre__rightExpr(self)
    self.obj21220.isGraphObjectVisual = True

    if(hasattr(self.obj21220, '_setHierarchicalLink')):
      self.obj21220._setHierarchicalLink(False)

    # MT_label__
    self.obj21220.MT_label__.setValue('30')

    # MT_pivotOut__
    self.obj21220.MT_pivotOut__.setValue('')
    self.obj21220.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21220.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21220.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21220.MT_pivotIn__.setValue('')
    self.obj21220.MT_pivotIn__.setNone()

    self.obj21220.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(441.0,174.0,self.obj21220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21220)
    self.globalAndLocalPostcondition(self.obj21220, rootNode)
    self.obj21220.postAction( rootNode.CREATE )

    self.obj21211=MT_pre__trace_link(self)
    self.obj21211.isGraphObjectVisual = True

    if(hasattr(self.obj21211, '_setHierarchicalLink')):
      self.obj21211._setHierarchicalLink(False)

    # MT_label__
    self.obj21211.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj21211.MT_pivotOut__.setValue('')
    self.obj21211.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21211.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21211.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21211.MT_pivotIn__.setValue('')
    self.obj21211.MT_pivotIn__.setNone()

    self.obj21211.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(353.5,208.0,self.obj21211)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21211.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21211)
    self.globalAndLocalPostcondition(self.obj21211, rootNode)
    self.obj21211.postAction( rootNode.CREATE )

    self.obj21212=MT_pre__trace_link(self)
    self.obj21212.isGraphObjectVisual = True

    if(hasattr(self.obj21212, '_setHierarchicalLink')):
      self.obj21212._setHierarchicalLink(False)

    # MT_label__
    self.obj21212.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj21212.MT_pivotOut__.setValue('')
    self.obj21212.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21212.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21212.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21212.MT_pivotIn__.setValue('')
    self.obj21212.MT_pivotIn__.setNone()

    self.obj21212.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(488.5,189.0,self.obj21212)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21212.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21212)
    self.globalAndLocalPostcondition(self.obj21212, rootNode)
    self.obj21212.postAction( rootNode.CREATE )

    self.obj21213=MT_pre__trace_link(self)
    self.obj21213.isGraphObjectVisual = True

    if(hasattr(self.obj21213, '_setHierarchicalLink')):
      self.obj21213._setHierarchicalLink(False)

    # MT_label__
    self.obj21213.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj21213.MT_pivotOut__.setValue('')
    self.obj21213.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21213.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21213.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21213.MT_pivotIn__.setValue('')
    self.obj21213.MT_pivotIn__.setNone()

    self.obj21213.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(369.5,288.0,self.obj21213)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21213.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21213)
    self.globalAndLocalPostcondition(self.obj21213, rootNode)
    self.obj21213.postAction( rootNode.CREATE )

    self.obj21214=MT_pre__trace_link(self)
    self.obj21214.isGraphObjectVisual = True

    if(hasattr(self.obj21214, '_setHierarchicalLink')):
      self.obj21214._setHierarchicalLink(False)

    # MT_label__
    self.obj21214.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj21214.MT_pivotOut__.setValue('')
    self.obj21214.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21214.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21214.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21214.MT_pivotIn__.setValue('')
    self.obj21214.MT_pivotIn__.setNone()

    self.obj21214.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(439.5,288.0,self.obj21214)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21214.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21214)
    self.globalAndLocalPostcondition(self.obj21214, rootNode)
    self.obj21214.postAction( rootNode.CREATE )

    self.obj21241=MT_pre__trace_link(self)
    self.obj21241.isGraphObjectVisual = True

    if(hasattr(self.obj21241, '_setHierarchicalLink')):
      self.obj21241._setHierarchicalLink(False)

    # MT_label__
    self.obj21241.MT_label__.setValue('39')

    # MT_pivotOut__
    self.obj21241.MT_pivotOut__.setValue('')
    self.obj21241.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21241.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21241.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21241.MT_pivotIn__.setValue('')
    self.obj21241.MT_pivotIn__.setNone()

    self.obj21241.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(406.5,292.0,self.obj21241)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21241.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21241)
    self.globalAndLocalPostcondition(self.obj21241, rootNode)
    self.obj21241.postAction( rootNode.CREATE )

    self.obj21242=MT_pre__trace_link(self)
    self.obj21242.isGraphObjectVisual = True

    if(hasattr(self.obj21242, '_setHierarchicalLink')):
      self.obj21242._setHierarchicalLink(False)

    # MT_label__
    self.obj21242.MT_label__.setValue('40')

    # MT_pivotOut__
    self.obj21242.MT_pivotOut__.setValue('')
    self.obj21242.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21242.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21242.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21242.MT_pivotIn__.setValue('')
    self.obj21242.MT_pivotIn__.setNone()

    self.obj21242.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(382.5,259.0,self.obj21242)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21242.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21242)
    self.globalAndLocalPostcondition(self.obj21242, rootNode)
    self.obj21242.postAction( rootNode.CREATE )

    self.obj21243=MT_pre__trace_link(self)
    self.obj21243.isGraphObjectVisual = True

    if(hasattr(self.obj21243, '_setHierarchicalLink')):
      self.obj21243._setHierarchicalLink(False)

    # MT_label__
    self.obj21243.MT_label__.setValue('41')

    # MT_pivotOut__
    self.obj21243.MT_pivotOut__.setValue('')
    self.obj21243.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21243.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21243.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21243.MT_pivotIn__.setValue('')
    self.obj21243.MT_pivotIn__.setNone()

    self.obj21243.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(402.5,224.0,self.obj21243)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21243.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21243)
    self.globalAndLocalPostcondition(self.obj21243, rootNode)
    self.obj21243.postAction( rootNode.CREATE )

    self.obj21208=MT_pre__directLink_S(self)
    self.obj21208.isGraphObjectVisual = True

    if(hasattr(self.obj21208, '_setHierarchicalLink')):
      self.obj21208._setHierarchicalLink(False)

    # MT_label__
    self.obj21208.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj21208.MT_pivotOut__.setValue('')
    self.obj21208.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21208.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21208.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21208.MT_pivotIn__.setValue('')
    self.obj21208.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21208.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21208.MT_pre__associationType.setHeight(15)

    self.obj21208.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(344.5,115.0,self.obj21208)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21208.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21208)
    self.globalAndLocalPostcondition(self.obj21208, rootNode)
    self.obj21208.postAction( rootNode.CREATE )

    self.obj21209=MT_pre__directLink_S(self)
    self.obj21209.isGraphObjectVisual = True

    if(hasattr(self.obj21209, '_setHierarchicalLink')):
      self.obj21209._setHierarchicalLink(False)

    # MT_label__
    self.obj21209.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj21209.MT_pivotOut__.setValue('')
    self.obj21209.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21209.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21209.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21209.MT_pivotIn__.setValue('')
    self.obj21209.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21209.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21209.MT_pre__associationType.setHeight(15)

    self.obj21209.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(453.0,159.0,self.obj21209)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21209.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21209)
    self.globalAndLocalPostcondition(self.obj21209, rootNode)
    self.obj21209.postAction( rootNode.CREATE )

    self.obj21227=MT_pre__directLink_S(self)
    self.obj21227.isGraphObjectVisual = True

    if(hasattr(self.obj21227, '_setHierarchicalLink')):
      self.obj21227._setHierarchicalLink(False)

    # MT_label__
    self.obj21227.MT_label__.setValue('32')

    # MT_pivotOut__
    self.obj21227.MT_pivotOut__.setValue('')
    self.obj21227.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21227.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21227.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21227.MT_pivotIn__.setValue('')
    self.obj21227.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21227.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21227.MT_pre__associationType.setHeight(15)

    self.obj21227.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(350.5,163.0,self.obj21227)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21227.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21227)
    self.globalAndLocalPostcondition(self.obj21227, rootNode)
    self.obj21227.postAction( rootNode.CREATE )

    self.obj21198=MT_pre__Inst(self)
    self.obj21198.isGraphObjectVisual = True

    if(hasattr(self.obj21198, '_setHierarchicalLink')):
      self.obj21198._setHierarchicalLink(False)

    # MT_label__
    self.obj21198.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj21198.MT_pivotOut__.setValue('')
    self.obj21198.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21198.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21198.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21198.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21198.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21198.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21198.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21198.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21198.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21198.MT_pivotIn__.setValue('')
    self.obj21198.MT_pivotIn__.setNone()

    self.obj21198.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(180.0,260.0,self.obj21198)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21198.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21198)
    self.globalAndLocalPostcondition(self.obj21198, rootNode)
    self.obj21198.postAction( rootNode.CREATE )

    self.obj21205=MT_pre__directLink_T(self)
    self.obj21205.isGraphObjectVisual = True

    if(hasattr(self.obj21205, '_setHierarchicalLink')):
      self.obj21205._setHierarchicalLink(False)

    # MT_label__
    self.obj21205.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj21205.MT_pivotOut__.setValue('')
    self.obj21205.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21205.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21205.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21205.MT_pivotIn__.setValue('')
    self.obj21205.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21205.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21205.MT_pre__associationType.setHeight(15)

    self.obj21205.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(366.0,311.0,self.obj21205)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21205.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21205)
    self.globalAndLocalPostcondition(self.obj21205, rootNode)
    self.obj21205.postAction( rootNode.CREATE )

    self.obj21206=MT_pre__directLink_T(self)
    self.obj21206.isGraphObjectVisual = True

    if(hasattr(self.obj21206, '_setHierarchicalLink')):
      self.obj21206._setHierarchicalLink(False)

    # MT_label__
    self.obj21206.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj21206.MT_pivotOut__.setValue('')
    self.obj21206.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21206.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21206.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21206.MT_pivotIn__.setValue('')
    self.obj21206.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21206.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21206.MT_pre__associationType.setHeight(15)

    self.obj21206.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(279.5,331.0,self.obj21206)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21206.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21206)
    self.globalAndLocalPostcondition(self.obj21206, rootNode)
    self.obj21206.postAction( rootNode.CREATE )

    self.obj21207=MT_pre__directLink_T(self)
    self.obj21207.isGraphObjectVisual = True

    if(hasattr(self.obj21207, '_setHierarchicalLink')):
      self.obj21207._setHierarchicalLink(False)

    # MT_label__
    self.obj21207.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj21207.MT_pivotOut__.setValue('')
    self.obj21207.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21207.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21207.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21207.MT_pivotIn__.setValue('')
    self.obj21207.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21207.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21207.MT_pre__associationType.setHeight(15)

    self.obj21207.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(352.0,361.0,self.obj21207)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21207.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21207)
    self.globalAndLocalPostcondition(self.obj21207, rootNode)
    self.obj21207.postAction( rootNode.CREATE )

    self.obj21233=MT_pre__directLink_T(self)
    self.obj21233.isGraphObjectVisual = True

    if(hasattr(self.obj21233, '_setHierarchicalLink')):
      self.obj21233._setHierarchicalLink(False)

    # MT_label__
    self.obj21233.MT_label__.setValue('36')

    # MT_pivotOut__
    self.obj21233.MT_pivotOut__.setValue('')
    self.obj21233.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21233.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21233.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21233.MT_pivotIn__.setValue('')
    self.obj21233.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21233.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21233.MT_pre__associationType.setHeight(15)

    self.obj21233.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(326.0,369.0,self.obj21233)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21233.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21233)
    self.globalAndLocalPostcondition(self.obj21233, rootNode)
    self.obj21233.postAction( rootNode.CREATE )

    self.obj21234=MT_pre__directLink_T(self)
    self.obj21234.isGraphObjectVisual = True

    if(hasattr(self.obj21234, '_setHierarchicalLink')):
      self.obj21234._setHierarchicalLink(False)

    # MT_label__
    self.obj21234.MT_label__.setValue('37')

    # MT_pivotOut__
    self.obj21234.MT_pivotOut__.setValue('')
    self.obj21234.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21234.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21234.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21234.MT_pivotIn__.setValue('')
    self.obj21234.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21234.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21234.MT_pre__associationType.setHeight(15)

    self.obj21234.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(365.0,330.0,self.obj21234)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21234.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21234)
    self.globalAndLocalPostcondition(self.obj21234, rootNode)
    self.obj21234.postAction( rootNode.CREATE )

    self.obj21235=MT_pre__directLink_T(self)
    self.obj21235.isGraphObjectVisual = True

    if(hasattr(self.obj21235, '_setHierarchicalLink')):
      self.obj21235._setHierarchicalLink(False)

    # MT_label__
    self.obj21235.MT_label__.setValue('38')

    # MT_pivotOut__
    self.obj21235.MT_pivotOut__.setValue('')
    self.obj21235.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21235.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21235.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21235.MT_pivotIn__.setValue('')
    self.obj21235.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj21235.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21235.MT_pre__associationType.setHeight(15)

    self.obj21235.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(365.0,281.0,self.obj21235)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21235.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21235)
    self.globalAndLocalPostcondition(self.obj21235, rootNode)
    self.obj21235.postAction( rootNode.CREATE )

    self.obj21215=MT_pre__hasAttribute_S(self)
    self.obj21215.isGraphObjectVisual = True

    if(hasattr(self.obj21215, '_setHierarchicalLink')):
      self.obj21215._setHierarchicalLink(False)

    # MT_label__
    self.obj21215.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj21215.MT_pivotOut__.setValue('')
    self.obj21215.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21215.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21215.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21215.MT_pivotIn__.setValue('')
    self.obj21215.MT_pivotIn__.setNone()

    self.obj21215.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(251.0,160.0,self.obj21215)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21215.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21215)
    self.globalAndLocalPostcondition(self.obj21215, rootNode)
    self.obj21215.postAction( rootNode.CREATE )

    self.obj21192=MT_pre__Transition(self)
    self.obj21192.isGraphObjectVisual = True

    if(hasattr(self.obj21192, '_setHierarchicalLink')):
      self.obj21192._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21192.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj21192.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21192.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21192.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21192.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21192.MT_pivotIn__.setValue('element3')

    # MT_label__
    self.obj21192.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj21192.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21192.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21192.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21192.MT_pre__name.setHeight(15)

    self.obj21192.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(280.0,160.0,self.obj21192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21192.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21192)
    self.globalAndLocalPostcondition(self.obj21192, rootNode)
    self.obj21192.postAction( rootNode.CREATE )

    self.obj21216=MT_pre__hasAttribute_T(self)
    self.obj21216.isGraphObjectVisual = True

    if(hasattr(self.obj21216, '_setHierarchicalLink')):
      self.obj21216._setHierarchicalLink(False)

    # MT_label__
    self.obj21216.MT_label__.setValue('28')

    # MT_pivotOut__
    self.obj21216.MT_pivotOut__.setValue('')
    self.obj21216.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21216.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21216.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21216.MT_pivotIn__.setValue('')
    self.obj21216.MT_pivotIn__.setNone()

    self.obj21216.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(360.0,223.0,self.obj21216)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21216.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21216)
    self.globalAndLocalPostcondition(self.obj21216, rootNode)
    self.obj21216.postAction( rootNode.CREATE )

    self.obj21199=MT_pre__Attribute(self)
    self.obj21199.isGraphObjectVisual = True

    if(hasattr(self.obj21199, '_setHierarchicalLink')):
      self.obj21199._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21199.MT_pivotOut__.setValue('')
    self.obj21199.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21199.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21199.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21199.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21199.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21199.MT_pivotIn__.setValue('')
    self.obj21199.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21199.MT_label__.setValue('19')

    # MT_pre__name
    self.obj21199.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21199.MT_pre__name.setHeight(15)

    self.obj21199.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(80.0,140.0,self.obj21199)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21199.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21199)
    self.globalAndLocalPostcondition(self.obj21199, rootNode)
    self.obj21199.postAction( rootNode.CREATE )

    self.obj21200=MT_pre__Attribute(self)
    self.obj21200.isGraphObjectVisual = True

    if(hasattr(self.obj21200, '_setHierarchicalLink')):
      self.obj21200._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21200.MT_pivotOut__.setValue('')
    self.obj21200.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21200.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21200.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21200.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21200.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21200.MT_pivotIn__.setValue('')
    self.obj21200.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21200.MT_label__.setValue('25')

    # MT_pre__name
    self.obj21200.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21200.MT_pre__name.setHeight(15)

    self.obj21200.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(100.0,60.0,self.obj21200)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21200.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21200)
    self.globalAndLocalPostcondition(self.obj21200, rootNode)
    self.obj21200.postAction( rootNode.CREATE )

    self.obj21203=MT_pre__Constant(self)
    self.obj21203.isGraphObjectVisual = True

    if(hasattr(self.obj21203, '_setHierarchicalLink')):
      self.obj21203._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21203.MT_pivotOut__.setValue('')
    self.obj21203.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21203.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21203.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21203.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21203.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21203.MT_pivotIn__.setValue('')
    self.obj21203.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21203.MT_label__.setValue('22')

    # MT_pre__name
    self.obj21203.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21203.MT_pre__name.setHeight(15)

    self.obj21203.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(80.0,280.0,self.obj21203)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21203.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21203)
    self.globalAndLocalPostcondition(self.obj21203, rootNode)
    self.obj21203.postAction( rootNode.CREATE )

    self.obj21204=MT_pre__Constant(self)
    self.obj21204.isGraphObjectVisual = True

    if(hasattr(self.obj21204, '_setHierarchicalLink')):
      self.obj21204._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21204.MT_pivotOut__.setValue('')
    self.obj21204.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21204.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21204.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21204.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21204.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21204.MT_pivotIn__.setValue('')
    self.obj21204.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21204.MT_label__.setValue('27')

    # MT_pre__name
    self.obj21204.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21204.MT_pre__name.setHeight(15)

    self.obj21204.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(240.0,140.0,self.obj21204)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21204.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21204)
    self.globalAndLocalPostcondition(self.obj21204, rootNode)
    self.obj21204.postAction( rootNode.CREATE )

    self.obj21191=MT_pre__ExitPoint(self)
    self.obj21191.isGraphObjectVisual = True

    if(hasattr(self.obj21191, '_setHierarchicalLink')):
      self.obj21191._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21191.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj21191.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21191.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21191.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21191.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21191.MT_pivotIn__.setValue('element2')

    # MT_label__
    self.obj21191.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj21191.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21191.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21191.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21191.MT_pre__name.setHeight(15)

    self.obj21191.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(233.0,40.0,self.obj21191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21191.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21191)
    self.globalAndLocalPostcondition(self.obj21191, rootNode)
    self.obj21191.postAction( rootNode.CREATE )

    self.obj21196=MT_pre__Trigger_T(self)
    self.obj21196.isGraphObjectVisual = True

    if(hasattr(self.obj21196, '_setHierarchicalLink')):
      self.obj21196._setHierarchicalLink(False)

    # MT_label__
    self.obj21196.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj21196.MT_pivotOut__.setValue('')
    self.obj21196.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21196.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21196.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21196.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21196.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21196.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21196.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21196.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21196.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21196.MT_pivotIn__.setValue('')
    self.obj21196.MT_pivotIn__.setNone()

    self.obj21196.graphClass_= graph_MT_pre__Trigger_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_T(238.0,220.0,self.obj21196)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21196.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21196)
    self.globalAndLocalPostcondition(self.obj21196, rootNode)
    self.obj21196.postAction( rootNode.CREATE )

    self.obj21217=MT_pre__leftExpr(self)
    self.obj21217.isGraphObjectVisual = True

    if(hasattr(self.obj21217, '_setHierarchicalLink')):
      self.obj21217._setHierarchicalLink(False)

    # MT_label__
    self.obj21217.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj21217.MT_pivotOut__.setValue('')
    self.obj21217.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21217.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21217.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21217.MT_pivotIn__.setValue('')
    self.obj21217.MT_pivotIn__.setNone()

    self.obj21217.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(281.0,226.0,self.obj21217)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21217.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21217)
    self.globalAndLocalPostcondition(self.obj21217, rootNode)
    self.obj21217.postAction( rootNode.CREATE )

    self.obj21218=MT_pre__leftExpr(self)
    self.obj21218.isGraphObjectVisual = True

    if(hasattr(self.obj21218, '_setHierarchicalLink')):
      self.obj21218._setHierarchicalLink(False)

    # MT_label__
    self.obj21218.MT_label__.setValue('29')

    # MT_pivotOut__
    self.obj21218.MT_pivotOut__.setValue('')
    self.obj21218.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21218.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21218.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21218.MT_pivotIn__.setValue('')
    self.obj21218.MT_pivotIn__.setNone()

    self.obj21218.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(317.0,127.0,self.obj21218)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21218.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21218)
    self.globalAndLocalPostcondition(self.obj21218, rootNode)
    self.obj21218.postAction( rootNode.CREATE )

    self.obj21201=MT_pre__Equation(self)
    self.obj21201.isGraphObjectVisual = True

    if(hasattr(self.obj21201, '_setHierarchicalLink')):
      self.obj21201._setHierarchicalLink(False)

    # MT_label__
    self.obj21201.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj21201.MT_pivotOut__.setValue('')
    self.obj21201.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj21201.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21201.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj21201.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21201.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21201.MT_pivotIn__.setValue('')
    self.obj21201.MT_pivotIn__.setNone()

    self.obj21201.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(100.0,220.0,self.obj21201)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21201.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21201)
    self.globalAndLocalPostcondition(self.obj21201, rootNode)
    self.obj21201.postAction( rootNode.CREATE )

    self.obj21202=MT_pre__Equation(self)
    self.obj21202.isGraphObjectVisual = True

    if(hasattr(self.obj21202, '_setHierarchicalLink')):
      self.obj21202._setHierarchicalLink(False)

    # MT_label__
    self.obj21202.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj21202.MT_pivotOut__.setValue('')
    self.obj21202.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj21202.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21202.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj21202.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21202.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21202.MT_pivotIn__.setValue('')
    self.obj21202.MT_pivotIn__.setNone()

    self.obj21202.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(260.0,40.0,self.obj21202)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21202.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21202)
    self.globalAndLocalPostcondition(self.obj21202, rootNode)
    self.obj21202.postAction( rootNode.CREATE )

    # Connections for obj21221 (graphObject_: Obj58) of type LHS
    self.drawConnections(
 )
    # Connections for obj21195 (graphObject_: Obj32) of type MT_pre__Name
    self.drawConnections(
(self.obj21195,self.obj21214,[422.0, 361.0, 439.5, 288.0],"true", 2) )
    # Connections for obj21230 (graphObject_: Obj61) of type MT_pre__Name
    self.drawConnections(
(self.obj21230,self.obj21241,[282.0, 341.0, 406.5, 292.0],"true", 2) )
    # Connections for obj21231 (graphObject_: Obj62) of type MT_pre__Name
    self.drawConnections(
(self.obj21231,self.obj21242,[322.0, 301.0, 382.5, 259.0],"true", 2) )
    # Connections for obj21232 (graphObject_: Obj63) of type MT_pre__Name
    self.drawConnections(
(self.obj21232,self.obj21243,[362.0, 221.0, 402.5, 224.0],"true", 2) )
    # Connections for obj21193 (graphObject_: Obj30) of type MT_pre__State
    self.drawConnections(
(self.obj21193,self.obj21208,[257.0, 115.0, 344.5, 115.0],"true", 2),
(self.obj21193,self.obj21215,[257.0, 115.0, 251.0, 160.0],"true", 2) )
    # Connections for obj21224 (graphObject_: Obj59) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj21197 (graphObject_: Obj34) of type MT_pre__Par
    self.drawConnections(
(self.obj21197,self.obj21205,[277.0, 301.0, 366.0, 311.0],"true", 2),
(self.obj21197,self.obj21206,[277.0, 301.0, 279.5, 331.0],"true", 2),
(self.obj21197,self.obj21211,[277.0, 301.0, 353.5, 208.0],"true", 2) )
    # Connections for obj21219 (graphObject_: Obj56) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj21219,self.obj21203,[350.0, 331.0, 245.0, 345.0],"true", 2) )
    # Connections for obj21220 (graphObject_: Obj57) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj21220,self.obj21204,[441.0, 174.0, 405.0, 205.0],"true", 2) )
    # Connections for obj21211 (graphObject_: Obj48) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21211,self.obj21191,[353.5, 208.0, 430.0, 115.0],"true", 2) )
    # Connections for obj21212 (graphObject_: Obj49) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21212,self.obj21191,[488.5, 189.0, 430.0, 115.0],"true", 2) )
    # Connections for obj21213 (graphObject_: Obj50) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21213,self.obj21192,[369.5, 288.0, 477.0, 235.0],"true", 2) )
    # Connections for obj21214 (graphObject_: Obj51) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21214,self.obj21192,[439.5, 288.0, 477.0, 235.0],"true", 2) )
    # Connections for obj21241 (graphObject_: Obj68) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21241,self.obj21192,[406.5, 292.0, 477.0, 235.0],"true", 2) )
    # Connections for obj21242 (graphObject_: Obj69) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21242,self.obj21192,[382.5, 259.0, 477.0, 235.0],"true", 2) )
    # Connections for obj21243 (graphObject_: Obj70) of type MT_pre__trace_link
    self.drawConnections(
(self.obj21243,self.obj21192,[402.5, 224.0, 477.0, 235.0],"true", 2) )
    # Connections for obj21208 (graphObject_: Obj45) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj21208,self.obj21191,[344.5, 115.0, 430.0, 115.0],"true", 2) )
    # Connections for obj21209 (graphObject_: Obj46) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj21209,self.obj21192,[453.0, 159.0, 477.0, 235.0],"true", 2) )
    # Connections for obj21227 (graphObject_: Obj60) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj21227,self.obj21224,[350.5, 163.0, 282.0, 235.0],"true", 2) )
    # Connections for obj21198 (graphObject_: Obj35) of type MT_pre__Inst
    self.drawConnections(
(self.obj21198,self.obj21207,[402.0, 361.0, 352.0, 361.0],"true", 2),
(self.obj21198,self.obj21213,[402.0, 361.0, 369.5, 288.0],"true", 2),
(self.obj21198,self.obj21233,[402.0, 361.0, 326.0, 369.0],"true", 0),
(self.obj21198,self.obj21234,[402.0, 361.0, 365.0, 330.0],"true", 0),
(self.obj21198,self.obj21235,[402.0, 361.0, 365.0, 281.0],"true", 0) )
    # Connections for obj21205 (graphObject_: Obj42) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21205,self.obj21196,[366.0, 311.0, 455.0, 321.0],"true", 2) )
    # Connections for obj21206 (graphObject_: Obj43) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21206,self.obj21198,[279.5, 331.0, 402.0, 361.0],"true", 2) )
    # Connections for obj21207 (graphObject_: Obj44) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21207,self.obj21195,[352.0, 361.0, 422.0, 361.0],"true", 2) )
    # Connections for obj21233 (graphObject_: Obj64) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21233,self.obj21230,[326.0, 369.0, 282.0, 341.0],"true", 2) )
    # Connections for obj21234 (graphObject_: Obj65) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21234,self.obj21231,[365.0, 330.0, 322.0, 301.0],"true", 2) )
    # Connections for obj21235 (graphObject_: Obj66) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj21235,self.obj21232,[365.0, 281.0, 362.0, 221.0],"true", 2) )
    # Connections for obj21215 (graphObject_: Obj52) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj21215,self.obj21199,[251.0, 160.0, 245.0, 205.0],"true", 2) )
    # Connections for obj21192 (graphObject_: Obj29) of type MT_pre__Transition
    self.drawConnections(
(self.obj21192,self.obj21227,[477.0, 235.0, 350.5, 163.0],"true", 0) )
    # Connections for obj21216 (graphObject_: Obj53) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj21216,self.obj21200,[360.0, 223.0, 265.0, 125.0],"true", 2) )
    # Connections for obj21199 (graphObject_: Obj36) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj21200 (graphObject_: Obj37) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj21203 (graphObject_: Obj40) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj21204 (graphObject_: Obj41) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj21191 (graphObject_: Obj28) of type MT_pre__ExitPoint
    self.drawConnections(
(self.obj21191,self.obj21209,[430.0, 115.0, 453.0, 159.0],"true", 2) )
    # Connections for obj21196 (graphObject_: Obj33) of type MT_pre__Trigger_T
    self.drawConnections(
(self.obj21196,self.obj21212,[455.0, 321.0, 488.5, 189.0],"true", 2),
(self.obj21196,self.obj21216,[455.0, 321.0, 360.0, 223.0],"true", 2) )
    # Connections for obj21217 (graphObject_: Obj54) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj21217,self.obj21199,[281.0, 226.0, 245.0, 205.0],"true", 2) )
    # Connections for obj21218 (graphObject_: Obj55) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj21218,self.obj21200,[317.0, 127.0, 265.0, 125.0],"true", 2) )
    # Connections for obj21201 (graphObject_: Obj38) of type MT_pre__Equation
    self.drawConnections(
(self.obj21201,self.obj21217,[269.0, 293.0, 281.0, 226.0],"true", 2),
(self.obj21201,self.obj21219,[269.0, 293.0, 350.0, 331.0],"true", 2) )
    # Connections for obj21202 (graphObject_: Obj39) of type MT_pre__Equation
    self.drawConnections(
(self.obj21202,self.obj21218,[429.0, 113.0, 317.0, 127.0],"true", 2),
(self.obj21202,self.obj21220,[429.0, 113.0, 441.0, 174.0],"true", 2) )

newfunction = ExitPtConOPsOfExitPtSIB_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
