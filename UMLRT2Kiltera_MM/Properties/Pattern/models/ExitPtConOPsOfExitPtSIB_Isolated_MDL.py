"""
__ExitPtConOPsOfExitPtSIB_Isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 18:49:16 2015
______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__SIBLING0 import *
from MT_pre__rightExpr import *
from MT_pre__hasAttribute_S import *
from MT_pre__Transition import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
from MT_pre__ExitPoint import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from graph_MT_pre__SIBLING0 import *
from graph_MT_pre__Equation import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__Transition import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
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

def ExitPtConOPsOfExitPtSIB_Isolated_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('ExitPtConOPsOfExitPtSIB_Isolated')
    # --- ASG attributes over ---


    self.obj130=LHS(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # constraint
    self.obj130.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nif (PreNode(\'7\')[\'name\']==\'isComposite\')and (PreNode(\'5\')[\'name\']==\'true\'):\n   return True\nreturn False\n')
    self.obj130.constraint.setHeight(15)

    self.obj130.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(36.0,20.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj122=MT_pre__State(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj122.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj122.MT_subtypeMatching__.setValue(('True', 0))
    self.obj122.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj122.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj122.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj122.MT_pivotIn__.setValue('')
    self.obj122.MT_pivotIn__.setNone()

    # MT_label__
    self.obj122.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj122.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj122.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj122.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj122.MT_pre__name.setHeight(15)

    self.obj122.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(60.0,40.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj133=MT_pre__SIBLING0(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # MT_label__
    self.obj133.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj133.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj133.MT_subtypeMatching__.setValue(('True', 0))
    self.obj133.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj133.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj133.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj133.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj133.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj133.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj133.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj133.MT_pivotIn__.setValue('')
    self.obj133.MT_pivotIn__.setNone()

    self.obj133.graphClass_= graph_MT_pre__SIBLING0
    if self.genGraphics:
       new_obj = graph_MT_pre__SIBLING0(80.0,120.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj129=MT_pre__rightExpr(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_label__
    self.obj129.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('')
    self.obj129.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('')
    self.obj129.MT_pivotIn__.setNone()

    self.obj129.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(392.0,329.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj127=MT_pre__hasAttribute_S(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # MT_label__
    self.obj127.MT_label__.setValue('8')

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
       new_obj = graph_MT_pre__hasAttribute_S(258.5,220.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj121=MT_pre__Transition(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj121.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj121.MT_subtypeMatching__.setValue(('True', 0))
    self.obj121.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj121.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj121.MT_pivotIn__.setValue('')
    self.obj121.MT_pivotIn__.setNone()

    # MT_label__
    self.obj121.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj121.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj121.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__name.setHeight(15)

    self.obj121.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(277.0,128.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj124=MT_pre__Attribute(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('')
    self.obj124.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj124.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('')
    self.obj124.MT_pivotIn__.setNone()

    # MT_label__
    self.obj124.MT_label__.setValue('7')

    # MT_pre__name
    self.obj124.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__name.setHeight(15)

    self.obj124.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(80.0,220.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj126=MT_pre__Constant(self)
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
    self.obj126.MT_label__.setValue('5')

    # MT_pre__name
    self.obj126.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__name.setHeight(15)

    self.obj126.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(240.0,300.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj120=MT_pre__ExitPoint(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj120.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj120.MT_subtypeMatching__.setValue(('True', 0))
    self.obj120.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj120.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj120.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj120.MT_pivotIn__.setValue('')
    self.obj120.MT_pivotIn__.setNone()

    # MT_label__
    self.obj120.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj120.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj120.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj120.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj120.MT_pre__name.setHeight(15)

    self.obj120.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(234.0,40.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj128=MT_pre__leftExpr(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # MT_label__
    self.obj128.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj128.MT_pivotOut__.setValue('')
    self.obj128.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj128.MT_subtypeMatching__.setValue(('True', 0))
    self.obj128.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj128.MT_pivotIn__.setValue('')
    self.obj128.MT_pivotIn__.setNone()

    self.obj128.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(322.0,289.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj125=MT_pre__Equation(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_label__
    self.obj125.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('')
    self.obj125.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj125.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('')
    self.obj125.MT_pivotIn__.setNone()

    self.obj125.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(240.0,220.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    # Connections for obj130 (graphObject_: Obj10) of type LHS
    self.drawConnections(
 )
    # Connections for obj122 (graphObject_: Obj2) of type MT_pre__State
    self.drawConnections(
(self.obj122,self.obj127,[257.0, 115.0, 258.5, 220.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj11) of type MT_pre__SIBLING0
    self.drawConnections(
 )
    # Connections for obj129 (graphObject_: Obj9) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj129,self.obj126,[392.0, 329.0, 400.0, 365.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj7) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj127,self.obj124,[258.5, 220.0, 240.0, 285.0],"true", 2) )
    # Connections for obj121 (graphObject_: Obj1) of type MT_pre__Transition
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj4) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj126 (graphObject_: Obj6) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj120 (graphObject_: Obj0) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj128 (graphObject_: Obj8) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj128,self.obj124,[322.0, 289.0, 240.0, 285.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj5) of type MT_pre__Equation
    self.drawConnections(
(self.obj125,self.obj128,[404.0, 293.0, 322.0, 289.0],"true", 2),
(self.obj125,self.obj129,[404.0, 293.0, 392.0, 329.0],"true", 2) )

newfunction = ExitPtConOPsOfExitPtSIB_Isolated_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
