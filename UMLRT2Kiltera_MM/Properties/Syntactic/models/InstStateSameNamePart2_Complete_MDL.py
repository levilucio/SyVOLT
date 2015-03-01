"""
__InstStateSameNamePart2_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sat Feb 28 23:25:27 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__rightExpr import *
from MT_pre__Concat import *
from MT_pre__hasAttribute_S import *
from MT_pre__hasArgs import *
from MT_pre__hasAttribute_T import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
from MT_pre__ProcDef import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from graph_MT_pre__Equation import *
from graph_MT_pre__hasArgs import *
from graph_LHS import *
from graph_MT_pre__hasAttribute_T import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__Concat import *
from graph_MT_pre__leftExpr import *
from graph_MT_pre__Attribute import *
from graph_MT_pre__ProcDef import *
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

def InstStateSameNamePart2_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('InstStateSameNamePart2_Complete')
    # --- ASG attributes over ---


    self.obj21180=LHS(self)
    self.obj21180.isGraphObjectVisual = True

    if(hasattr(self.obj21180, '_setHierarchicalLink')):
      self.obj21180._setHierarchicalLink(False)

    # constraint
    self.obj21180.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'14\')[\'name\']==\'name\') and (PreNode(\'11\')[\'name\']==\'S\'):\n   return True\nreturn False\n')
    self.obj21180.constraint.setHeight(15)

    self.obj21180.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,20.0,self.obj21180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21180)
    self.globalAndLocalPostcondition(self.obj21180, rootNode)
    self.obj21180.postAction( rootNode.CREATE )

    self.obj21181=MT_pre__State(self)
    self.obj21181.isGraphObjectVisual = True

    if(hasattr(self.obj21181, '_setHierarchicalLink')):
      self.obj21181._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21181.MT_pivotOut__.setValue('')
    self.obj21181.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21181.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21181.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21181.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21181.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj21181.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj21181.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj21181.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21181.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21181.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21181.MT_pre__name.setHeight(15)

    self.obj21181.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj21181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21181)
    self.globalAndLocalPostcondition(self.obj21181, rootNode)
    self.obj21181.postAction( rootNode.CREATE )

    self.obj21182=MT_pre__rightExpr(self)
    self.obj21182.isGraphObjectVisual = True

    if(hasattr(self.obj21182, '_setHierarchicalLink')):
      self.obj21182._setHierarchicalLink(False)

    # MT_label__
    self.obj21182.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj21182.MT_pivotOut__.setValue('')
    self.obj21182.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21182.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21182.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21182.MT_pivotIn__.setValue('')
    self.obj21182.MT_pivotIn__.setNone()

    self.obj21182.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(362.0,209.0,self.obj21182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21182)
    self.globalAndLocalPostcondition(self.obj21182, rootNode)
    self.obj21182.postAction( rootNode.CREATE )

    self.obj21183=MT_pre__Concat(self)
    self.obj21183.isGraphObjectVisual = True

    if(hasattr(self.obj21183, '_setHierarchicalLink')):
      self.obj21183._setHierarchicalLink(False)

    # MT_label__
    self.obj21183.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj21183.MT_pivotOut__.setValue('')
    self.obj21183.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21183.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21183.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21183.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21183.MT_pre__Type.setHeight(15)

    # MT_pre__name
    self.obj21183.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21183.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21183.MT_pivotIn__.setValue('')
    self.obj21183.MT_pivotIn__.setNone()

    self.obj21183.graphClass_= graph_MT_pre__Concat
    if self.genGraphics:
       new_obj = graph_MT_pre__Concat(300.0,120.0,self.obj21183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21183)
    self.globalAndLocalPostcondition(self.obj21183, rootNode)
    self.obj21183.postAction( rootNode.CREATE )

    self.obj21185=MT_pre__hasAttribute_S(self)
    self.obj21185.isGraphObjectVisual = True

    if(hasattr(self.obj21185, '_setHierarchicalLink')):
      self.obj21185._setHierarchicalLink(False)

    # MT_label__
    self.obj21185.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj21185.MT_pivotOut__.setValue('')
    self.obj21185.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21185.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21185.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21185.MT_pivotIn__.setValue('')
    self.obj21185.MT_pivotIn__.setNone()

    self.obj21185.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(338.5,110.0,self.obj21185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21185.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21185)
    self.globalAndLocalPostcondition(self.obj21185, rootNode)
    self.obj21185.postAction( rootNode.CREATE )

    self.obj21186=MT_pre__hasArgs(self)
    self.obj21186.isGraphObjectVisual = True

    if(hasattr(self.obj21186, '_setHierarchicalLink')):
      self.obj21186._setHierarchicalLink(False)

    # MT_label__
    self.obj21186.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj21186.MT_pivotOut__.setValue('')
    self.obj21186.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21186.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21186.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21186.MT_pivotIn__.setValue('')
    self.obj21186.MT_pivotIn__.setNone()

    self.obj21186.graphClass_= graph_MT_pre__hasArgs
    if self.genGraphics:
       new_obj = graph_MT_pre__hasArgs(462.5,225.0,self.obj21186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21186)
    self.globalAndLocalPostcondition(self.obj21186, rootNode)
    self.obj21186.postAction( rootNode.CREATE )

    self.obj21197=MT_pre__hasArgs(self)
    self.obj21197.isGraphObjectVisual = True

    if(hasattr(self.obj21197, '_setHierarchicalLink')):
      self.obj21197._setHierarchicalLink(False)

    # MT_label__
    self.obj21197.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj21197.MT_pivotOut__.setValue('')
    self.obj21197.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21197.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21197.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21197.MT_pivotIn__.setValue('')
    self.obj21197.MT_pivotIn__.setNone()

    self.obj21197.graphClass_= graph_MT_pre__hasArgs
    if self.genGraphics:
       new_obj = graph_MT_pre__hasArgs(462.5,265.0,self.obj21197)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21197.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21197)
    self.globalAndLocalPostcondition(self.obj21197, rootNode)
    self.obj21197.postAction( rootNode.CREATE )

    self.obj21196=MT_pre__hasAttribute_T(self)
    self.obj21196.isGraphObjectVisual = True

    if(hasattr(self.obj21196, '_setHierarchicalLink')):
      self.obj21196._setHierarchicalLink(False)

    # MT_label__
    self.obj21196.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj21196.MT_pivotOut__.setValue('')
    self.obj21196.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21196.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21196.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21196.MT_pivotIn__.setValue('')
    self.obj21196.MT_pivotIn__.setNone()

    self.obj21196.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(363.5,353.0,self.obj21196)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21196.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21196)
    self.globalAndLocalPostcondition(self.obj21196, rootNode)
    self.obj21196.postAction( rootNode.CREATE )

    self.obj21189=MT_pre__Attribute(self)
    self.obj21189.isGraphObjectVisual = True

    if(hasattr(self.obj21189, '_setHierarchicalLink')):
      self.obj21189._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21189.MT_pivotOut__.setValue('')
    self.obj21189.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21189.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21189.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21189.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21189.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21189.MT_pivotIn__.setValue('')
    self.obj21189.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21189.MT_label__.setValue('2')

    # MT_pre__name
    self.obj21189.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21189.MT_pre__name.setHeight(15)

    self.obj21189.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,40.0,self.obj21189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21189)
    self.globalAndLocalPostcondition(self.obj21189, rootNode)
    self.obj21189.postAction( rootNode.CREATE )

    self.obj21195=MT_pre__Attribute(self)
    self.obj21195.isGraphObjectVisual = True

    if(hasattr(self.obj21195, '_setHierarchicalLink')):
      self.obj21195._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21195.MT_pivotOut__.setValue('')
    self.obj21195.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21195.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21195.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21195.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21195.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21195.MT_pivotIn__.setValue('')
    self.obj21195.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21195.MT_label__.setValue('14')

    # MT_pre__name
    self.obj21195.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21195.MT_pre__name.setHeight(15)

    self.obj21195.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(280.0,280.0,self.obj21195)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21195.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21195)
    self.globalAndLocalPostcondition(self.obj21195, rootNode)
    self.obj21195.postAction( rootNode.CREATE )

    self.obj21191=MT_pre__Constant(self)
    self.obj21191.isGraphObjectVisual = True

    if(hasattr(self.obj21191, '_setHierarchicalLink')):
      self.obj21191._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj21191.MT_pivotOut__.setValue('')
    self.obj21191.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21191.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21191.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj21191.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21191.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj21191.MT_pivotIn__.setValue('')
    self.obj21191.MT_pivotIn__.setNone()

    # MT_label__
    self.obj21191.MT_label__.setValue('11')

    # MT_pre__name
    self.obj21191.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21191.MT_pre__name.setHeight(15)

    self.obj21191.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(280.0,200.0,self.obj21191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21191.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21191)
    self.globalAndLocalPostcondition(self.obj21191, rootNode)
    self.obj21191.postAction( rootNode.CREATE )

    self.obj21194=MT_pre__ProcDef(self)
    self.obj21194.isGraphObjectVisual = True

    if(hasattr(self.obj21194, '_setHierarchicalLink')):
      self.obj21194._setHierarchicalLink(False)

    # MT_label__
    self.obj21194.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj21194.MT_pivotOut__.setValue('')
    self.obj21194.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21194.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21194.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj21194.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21194.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj21194.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21194.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj21194.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21194.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj21194.MT_pivotIn__.setValue('')
    self.obj21194.MT_pivotIn__.setNone()

    self.obj21194.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(60.0,260.0,self.obj21194)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21194.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21194)
    self.globalAndLocalPostcondition(self.obj21194, rootNode)
    self.obj21194.postAction( rootNode.CREATE )

    self.obj21192=MT_pre__leftExpr(self)
    self.obj21192.isGraphObjectVisual = True

    if(hasattr(self.obj21192, '_setHierarchicalLink')):
      self.obj21192._setHierarchicalLink(False)

    # MT_label__
    self.obj21192.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj21192.MT_pivotOut__.setValue('')
    self.obj21192.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj21192.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21192.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21192.MT_pivotIn__.setValue('')
    self.obj21192.MT_pivotIn__.setNone()

    self.obj21192.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(297.0,172.0,self.obj21192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj21192.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21192)
    self.globalAndLocalPostcondition(self.obj21192, rootNode)
    self.obj21192.postAction( rootNode.CREATE )

    self.obj21193=MT_pre__Equation(self)
    self.obj21193.isGraphObjectVisual = True

    if(hasattr(self.obj21193, '_setHierarchicalLink')):
      self.obj21193._setHierarchicalLink(False)

    # MT_label__
    self.obj21193.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj21193.MT_pivotOut__.setValue('')
    self.obj21193.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj21193.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj21193.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj21193.MT_subtypeMatching__.setValue(('True', 0))
    self.obj21193.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj21193.MT_pivotIn__.setValue('')
    self.obj21193.MT_pivotIn__.setNone()

    self.obj21193.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(80.0,160.0,self.obj21193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21193.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21193)
    self.globalAndLocalPostcondition(self.obj21193, rootNode)
    self.obj21193.postAction( rootNode.CREATE )

    # Connections for obj21180 (graphObject_: Obj22) of type LHS
    self.drawConnections(
 )
    # Connections for obj21181 (graphObject_: Obj23) of type MT_pre__State
    self.drawConnections(
(self.obj21181,self.obj21185,[257.0, 115.0, 338.5, 110.0],"true", 2) )
    # Connections for obj21182 (graphObject_: Obj24) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj21182,self.obj21183,[362.0, 209.0, 460.0, 185.0],"true", 2) )
    # Connections for obj21183 (graphObject_: Obj25) of type MT_pre__Concat
    self.drawConnections(
(self.obj21183,self.obj21186,[460.0, 185.0, 462.5, 225.0],"true", 2),
(self.obj21183,self.obj21197,[460.0, 185.0, 462.5, 265.0],"true", 2) )
    # Connections for obj21185 (graphObject_: Obj27) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj21185,self.obj21189,[338.5, 110.0, 420.0, 105.0],"true", 2) )
    # Connections for obj21186 (graphObject_: Obj28) of type MT_pre__hasArgs
    self.drawConnections(
(self.obj21186,self.obj21191,[462.5, 225.0, 445.0, 265.0],"true", 2) )
    # Connections for obj21197 (graphObject_: Obj39) of type MT_pre__hasArgs
    self.drawConnections(
(self.obj21197,self.obj21195,[462.5, 265.0, 445.0, 345.0],"true", 2) )
    # Connections for obj21196 (graphObject_: Obj38) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj21196,self.obj21195,[363.5, 353.0, 445.0, 345.0],"true", 2) )
    # Connections for obj21189 (graphObject_: Obj31) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj21195 (graphObject_: Obj37) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj21191 (graphObject_: Obj33) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj21194 (graphObject_: Obj36) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj21194,self.obj21196,[282.0, 361.0, 363.5, 353.0],"true", 2) )
    # Connections for obj21192 (graphObject_: Obj34) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj21192,self.obj21189,[297.0, 172.0, 420.0, 105.0],"true", 2) )
    # Connections for obj21193 (graphObject_: Obj35) of type MT_pre__Equation
    self.drawConnections(
(self.obj21193,self.obj21192,[244.0, 233.0, 297.0, 172.0],"true", 2),
(self.obj21193,self.obj21182,[244.0, 233.0, 362.0, 209.0],"true", 2) )

newfunction = InstStateSameNamePart2_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
