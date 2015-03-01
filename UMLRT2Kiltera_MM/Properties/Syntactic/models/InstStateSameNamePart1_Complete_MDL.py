"""
__InstStateSameNamePart1_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sat Feb 28 23:12:09 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__rightExpr import *
from MT_pre__Concat import *
from MT_pre__Inst import *
from MT_pre__hasAttribute_S import *
from MT_pre__hasArgs import *
from MT_pre__hasAttribute_T import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
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

def InstStateSameNamePart1_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('InstStateSameNamePart1_Complete')
    # --- ASG attributes over ---


    self.obj124=LHS(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # constraint
    self.obj124.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'2\')[\'name\']==\'name\') and (PreNode(\'5\')[\'name\']==\'name\') and (PreNode(\'11\')[\'name\']==\'S\'):\n   return True\nreturn False\n')
    self.obj124.constraint.setHeight(15)

    self.obj124.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(40.0,20.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=MT_pre__State(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj125.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj125.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj125.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj125.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__name.setHeight(15)

    self.obj125.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj134=MT_pre__rightExpr(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # MT_label__
    self.obj134.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj134.MT_pivotOut__.setValue('')
    self.obj134.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj134.MT_subtypeMatching__.setValue(('True', 0))
    self.obj134.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj134.MT_pivotIn__.setValue('')
    self.obj134.MT_pivotIn__.setNone()

    self.obj134.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(362.0,209.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj133=MT_pre__Concat(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # MT_label__
    self.obj133.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj133.MT_pivotOut__.setValue('')
    self.obj133.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj133.MT_subtypeMatching__.setValue(('True', 0))
    self.obj133.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj133.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj133.MT_pre__Type.setHeight(15)

    # MT_pre__name
    self.obj133.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj133.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj133.MT_pivotIn__.setValue('')
    self.obj133.MT_pivotIn__.setNone()

    self.obj133.graphClass_= graph_MT_pre__Concat
    if self.genGraphics:
       new_obj = graph_MT_pre__Concat(320.0,120.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj128=MT_pre__Inst(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # MT_label__
    self.obj128.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj128.MT_pivotOut__.setValue('')
    self.obj128.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj128.MT_subtypeMatching__.setValue(('True', 0))
    self.obj128.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj128.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj128.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj128.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj128.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj128.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj128.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj128.MT_pivotIn__.setValue('')
    self.obj128.MT_pivotIn__.setNone()

    self.obj128.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(60.0,260.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj127=MT_pre__hasAttribute_S(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # MT_label__
    self.obj127.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj127.MT_pivotOut__.setValue('')
    self.obj127.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj127.MT_subtypeMatching__.setValue(('True', 0))
    self.obj127.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj127.MT_pivotIn__.setValue('')
    self.obj127.MT_pivotIn__.setNone()

    self.obj127.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(338.5,110.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj136=MT_pre__hasArgs(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # MT_label__
    self.obj136.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj136.MT_pivotOut__.setValue('')
    self.obj136.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj136.MT_subtypeMatching__.setValue(('True', 0))
    self.obj136.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj136.MT_pivotIn__.setValue('')
    self.obj136.MT_pivotIn__.setNone()

    self.obj136.graphClass_= graph_MT_pre__hasArgs
    if self.genGraphics:
       new_obj = graph_MT_pre__hasArgs(462.5,225.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=MT_pre__hasArgs(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # MT_label__
    self.obj137.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj137.MT_pivotOut__.setValue('')
    self.obj137.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj137.MT_subtypeMatching__.setValue(('True', 0))
    self.obj137.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj137.MT_pivotIn__.setValue('')
    self.obj137.MT_pivotIn__.setNone()

    self.obj137.graphClass_= graph_MT_pre__hasArgs
    if self.genGraphics:
       new_obj = graph_MT_pre__hasArgs(460.0,265.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj130=MT_pre__hasAttribute_T(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # MT_label__
    self.obj130.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj130.MT_pivotOut__.setValue('')
    self.obj130.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj130.MT_subtypeMatching__.setValue(('True', 0))
    self.obj130.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj130.MT_pivotIn__.setValue('')
    self.obj130.MT_pivotIn__.setNone()

    self.obj130.graphClass_= graph_MT_pre__hasAttribute_T
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_T(358.5,353.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj126=MT_pre__Attribute(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj126.MT_pivotOut__.setValue('')
    self.obj126.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj126.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj126.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj126.MT_pivotIn__.setValue('')
    self.obj126.MT_pivotIn__.setNone()

    # MT_label__
    self.obj126.MT_label__.setValue('2')

    # MT_pre__name
    self.obj126.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__name.setHeight(15)

    self.obj126.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(260.0,40.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj129=MT_pre__Attribute(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('')
    self.obj129.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj129.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('')
    self.obj129.MT_pivotIn__.setNone()

    # MT_label__
    self.obj129.MT_label__.setValue('5')

    # MT_pre__name
    self.obj129.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__name.setHeight(15)

    self.obj129.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(280.0,280.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj135=MT_pre__Constant(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj135.MT_pivotOut__.setValue('')
    self.obj135.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj135.MT_subtypeMatching__.setValue(('True', 0))
    self.obj135.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj135.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj135.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj135.MT_pivotIn__.setValue('')
    self.obj135.MT_pivotIn__.setNone()

    # MT_label__
    self.obj135.MT_label__.setValue('11')

    # MT_pre__name
    self.obj135.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj135.MT_pre__name.setHeight(15)

    self.obj135.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(280.0,200.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj132=MT_pre__leftExpr(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # MT_label__
    self.obj132.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj132.MT_pivotOut__.setValue('')
    self.obj132.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj132.MT_subtypeMatching__.setValue(('True', 0))
    self.obj132.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj132.MT_pivotIn__.setValue('')
    self.obj132.MT_pivotIn__.setNone()

    self.obj132.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(297.0,172.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj131=MT_pre__Equation(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # MT_label__
    self.obj131.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj131.MT_pivotOut__.setValue('')
    self.obj131.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj131.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj131.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj131.MT_subtypeMatching__.setValue(('True', 0))
    self.obj131.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj131.MT_pivotIn__.setValue('')
    self.obj131.MT_pivotIn__.setNone()

    self.obj131.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(80.0,160.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    # Connections for obj124 (graphObject_: Obj4) of type LHS
    self.drawConnections(
 )
    # Connections for obj125 (graphObject_: Obj5) of type MT_pre__State
    self.drawConnections(
(self.obj125,self.obj127,[257.0, 115.0, 338.5, 110.0],"true", 2) )
    # Connections for obj134 (graphObject_: Obj14) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj134,self.obj133,[362.0, 209.0, 480.0, 185.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj13) of type MT_pre__Concat
    self.drawConnections(
(self.obj133,self.obj136,[480.0, 185.0, 462.5, 225.0],"true", 2),
(self.obj133,self.obj137,[480.0, 185.0, 460.0, 265.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj8) of type MT_pre__Inst
    self.drawConnections(
(self.obj128,self.obj130,[277.0, 361.0, 358.5, 353.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj7) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj127,self.obj126,[338.5, 110.0, 420.0, 105.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj16) of type MT_pre__hasArgs
    self.drawConnections(
(self.obj136,self.obj135,[462.5, 225.0, 445.0, 265.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj17) of type MT_pre__hasArgs
    self.drawConnections(
(self.obj137,self.obj129,[460.0, 265.0, 440.0, 345.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj10) of type MT_pre__hasAttribute_T
    self.drawConnections(
(self.obj130,self.obj129,[358.5, 353.0, 440.0, 345.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj6) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj129 (graphObject_: Obj9) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj135 (graphObject_: Obj15) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj132 (graphObject_: Obj12) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj132,self.obj126,[297.0, 172.0, 420.0, 105.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj11) of type MT_pre__Equation
    self.drawConnections(
(self.obj131,self.obj132,[244.0, 233.0, 297.0, 172.0],"true", 2),
(self.obj131,self.obj134,[244.0, 233.0, 362.0, 209.0],"true", 2) )

newfunction = InstStateSameNamePart1_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
