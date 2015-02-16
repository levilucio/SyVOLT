"""
__exitpoint2procdefparTrue_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 09:51:18 2015
_______________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
from MT_pre__State import *
from MT_pre__Par import *
from MT_pre__rightExpr import *
from MT_pre__trace_link import *
from MT_pre__directLink_S import *
from MT_pre__directLink_T import *
from MT_pre__hasAttribute_S import *
from MT_pre__Attribute import *
from MT_pre__Constant import *
from MT_pre__ExitPoint import *
from MT_pre__ProcDef import *
from MT_pre__leftExpr import *
from MT_pre__Equation import *
from graph_MT_pre__Equation import *
from graph_MT_pre__directLink_T import *
from graph_LHS import *
from graph_MT_pre__ExitPoint import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__hasAttribute_S import *
from graph_MT_pre__State import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__rightExpr import *
from graph_MT_pre__Constant import *
from graph_MT_pre__Par import *
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

def exitpoint2procdefparTrue_Complete_MDL(self, rootNode, MT_pre__UMLRT2Kiltera_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('exitpoint2procdefparTrue_Complete')
    # --- ASG attributes over ---


    self.obj123=LHS(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # constraint
    self.obj123.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj123.constraint.setHeight(15)

    self.obj123.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=MT_pre__State(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj124.MT_pivotOut__.setValue('')
    self.obj124.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj124.MT_subtypeMatching__.setValue(('True', 0))
    self.obj124.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj124.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj124.MT_pivotIn__.setValue('')
    self.obj124.MT_pivotIn__.setNone()

    # MT_label__
    self.obj124.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj124.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj124.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj124.MT_pre__name.setHeight(15)

    self.obj124.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(80.0,180.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj129=MT_pre__Par(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_label__
    self.obj129.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('')
    self.obj129.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj129.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj129.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj129.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('')
    self.obj129.MT_pivotIn__.setNone()

    self.obj129.graphClass_= graph_MT_pre__Par
    if self.genGraphics:
       new_obj = graph_MT_pre__Par(256.0,278.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj157=MT_pre__rightExpr(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # MT_label__
    self.obj157.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj157.MT_pivotOut__.setValue('')
    self.obj157.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj157.MT_subtypeMatching__.setValue(('True', 0))
    self.obj157.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj157.MT_pivotIn__.setValue('')
    self.obj157.MT_pivotIn__.setNone()

    self.obj157.graphClass_= graph_MT_pre__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__rightExpr(412.0,164.5,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj159=MT_pre__trace_link(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # MT_label__
    self.obj159.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj159.MT_pivotOut__.setValue('')
    self.obj159.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj159.MT_subtypeMatching__.setValue(('True', 0))
    self.obj159.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj159.MT_pivotIn__.setValue('')
    self.obj159.MT_pivotIn__.setNone()

    self.obj159.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(387.0,328.0,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=MT_pre__trace_link(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # MT_label__
    self.obj160.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj160.MT_pivotOut__.setValue('')
    self.obj160.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj160.MT_subtypeMatching__.setValue(('True', 0))
    self.obj160.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj160.MT_pivotIn__.setValue('')
    self.obj160.MT_pivotIn__.setNone()

    self.obj160.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(287.0,328.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=MT_pre__trace_link(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # MT_label__
    self.obj161.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj161.MT_pivotOut__.setValue('')
    self.obj161.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj161.MT_subtypeMatching__.setValue(('True', 0))
    self.obj161.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj161.MT_pivotIn__.setValue('')
    self.obj161.MT_pivotIn__.setNone()

    self.obj161.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(477.0,308.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=MT_pre__trace_link(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    # MT_label__
    self.obj162.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj162.MT_pivotOut__.setValue('')
    self.obj162.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj162.MT_subtypeMatching__.setValue(('True', 0))
    self.obj162.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj162.MT_pivotIn__.setValue('')
    self.obj162.MT_pivotIn__.setNone()

    self.obj162.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(377.0,308.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj126=MT_pre__directLink_S(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # MT_label__
    self.obj126.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj126.MT_pivotOut__.setValue('')
    self.obj126.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj126.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj126.MT_pivotIn__.setValue('')
    self.obj126.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj126.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__associationType.setHeight(15)

    self.obj126.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(299.0,257.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj130=MT_pre__directLink_T(self)
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

    # MT_pre__associationType
    self.obj130.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj130.MT_pre__associationType.setHeight(15)

    self.obj130.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(387.0,381.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj158=MT_pre__hasAttribute_S(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # MT_label__
    self.obj158.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj158.MT_pivotOut__.setValue('')
    self.obj158.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj158.MT_subtypeMatching__.setValue(('True', 0))
    self.obj158.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj158.MT_pivotIn__.setValue('')
    self.obj158.MT_pivotIn__.setNone()

    self.obj158.graphClass_= graph_MT_pre__hasAttribute_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttribute_S(278.5,215.5,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj131=MT_pre__Attribute(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj131.MT_pivotOut__.setValue('')
    self.obj131.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj131.MT_subtypeMatching__.setValue(('True', 0))
    self.obj131.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj131.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==Bool\n')
    self.obj131.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj131.MT_pivotIn__.setValue('')
    self.obj131.MT_pivotIn__.setNone()

    # MT_label__
    self.obj131.MT_label__.setValue('isComposite')

    # MT_pre__name
    self.obj131.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==isComposite\n')
    self.obj131.MT_pre__name.setHeight(15)

    self.obj131.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(120.0,111.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj140=MT_pre__Constant(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj140.MT_pivotOut__.setValue('')
    self.obj140.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj140.MT_subtypeMatching__.setValue(('True', 0))
    self.obj140.MT_subtypeMatching__.config = 0

    # MT_pre__Type
    self.obj140.MT_pre__Type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==Bool\n')
    self.obj140.MT_pre__Type.setHeight(15)

    # MT_pivotIn__
    self.obj140.MT_pivotIn__.setValue('')
    self.obj140.MT_pivotIn__.setNone()

    # MT_label__
    self.obj140.MT_label__.setValue('7')

    # MT_pre__name
    self.obj140.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value==true\n')
    self.obj140.MT_pre__name.setHeight(15)

    self.obj140.graphClass_= graph_MT_pre__Constant
    if self.genGraphics:
       new_obj = graph_MT_pre__Constant(300.0,111.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj125=MT_pre__ExitPoint(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('')
    self.obj125.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj125.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('')
    self.obj125.MT_pivotIn__.setNone()

    # MT_label__
    self.obj125.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj125.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj125.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__name.setHeight(15)

    self.obj125.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(280.0,180.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj128=MT_pre__ProcDef(self)
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

    self.obj128.graphClass_= graph_MT_pre__ProcDef
    if self.genGraphics:
       new_obj = graph_MT_pre__ProcDef(73.0,300.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj156=MT_pre__leftExpr(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # MT_label__
    self.obj156.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj156.MT_pivotOut__.setValue('')
    self.obj156.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj156.MT_subtypeMatching__.setValue(('True', 0))
    self.obj156.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj156.MT_pivotIn__.setValue('')
    self.obj156.MT_pivotIn__.setNone()

    self.obj156.graphClass_= graph_MT_pre__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_pre__leftExpr(322.0,164.5,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj149=MT_pre__Equation(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    # MT_label__
    self.obj149.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj149.MT_pivotOut__.setValue('')
    self.obj149.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj149.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj149.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj149.MT_subtypeMatching__.setValue(('True', 0))
    self.obj149.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj149.MT_pivotIn__.setValue('')
    self.obj149.MT_pivotIn__.setNone()

    self.obj149.graphClass_= graph_MT_pre__Equation
    if self.genGraphics:
       new_obj = graph_MT_pre__Equation(220.0,80.0,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    # Connections for obj123 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj1) of type MT_pre__State
    self.drawConnections(
(self.obj124,self.obj126,[277.0, 255.0, 299.0, 257.0],"true", 2),
(self.obj124,self.obj158,[277.0, 255.0, 278.5, 215.5],"true", 2) )
    # Connections for obj129 (graphObject_: Obj5) of type MT_pre__Par
    self.drawConnections(
(self.obj129,self.obj161,[473.0, 379.0, 477.0, 308.0],"true", 2),
(self.obj129,self.obj162,[473.0, 379.0, 377.0, 308.0],"true", 2) )
    # Connections for obj157 (graphObject_: Obj11) of type MT_pre__rightExpr
    self.drawConnections(
(self.obj157,self.obj140,[412.0, 164.5, 460.0, 176.0],"true", 2) )
    # Connections for obj159 (graphObject_: Obj13) of type MT_pre__trace_link
    self.drawConnections(
(self.obj159,self.obj125,[387.0, 328.0, 477.0, 255.0],"true", 2) )
    # Connections for obj160 (graphObject_: Obj14) of type MT_pre__trace_link
    self.drawConnections(
(self.obj160,self.obj124,[287.0, 328.0, 277.0, 255.0],"true", 2) )
    # Connections for obj161 (graphObject_: Obj15) of type MT_pre__trace_link
    self.drawConnections(
(self.obj161,self.obj125,[477.0, 308.0, 477.0, 255.0],"true", 2) )
    # Connections for obj162 (graphObject_: Obj16) of type MT_pre__trace_link
    self.drawConnections(
(self.obj162,self.obj124,[377.0, 308.0, 277.0, 255.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj3) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj126,self.obj125,[299.0, 257.0, 477.0, 255.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj6) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj130,self.obj129,[387.0, 381.0, 473.0, 379.0],"true", 2) )
    # Connections for obj158 (graphObject_: Obj12) of type MT_pre__hasAttribute_S
    self.drawConnections(
(self.obj158,self.obj131,[278.5, 215.5, 280.0, 176.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj7) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj140 (graphObject_: Obj8) of type MT_pre__Constant
    self.drawConnections(
 )
    # Connections for obj125 (graphObject_: Obj2) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj128 (graphObject_: Obj4) of type MT_pre__ProcDef
    self.drawConnections(
(self.obj128,self.obj130,[290.0, 401.0, 387.0, 381.0],"true", 2),
(self.obj128,self.obj159,[290.0, 401.0, 387.0, 328.0],"true", 2),
(self.obj128,self.obj160,[290.0, 401.0, 287.0, 328.0],"true", 2) )
    # Connections for obj156 (graphObject_: Obj10) of type MT_pre__leftExpr
    self.drawConnections(
(self.obj156,self.obj131,[322.0, 164.5, 280.0, 176.0],"true", 2) )
    # Connections for obj149 (graphObject_: Obj9) of type MT_pre__Equation
    self.drawConnections(
(self.obj149,self.obj156,[384.0, 153.0, 322.0, 164.5],"true", 2),
(self.obj149,self.obj157,[384.0, 153.0, 412.0, 164.5],"true", 2) )

newfunction = exitpoint2procdefparTrue_Complete_MDL

loadedMMName = ['MT_pre__UMLRT2Kiltera_MM_META', 'MoTifRule_META']

atom3version = '0.3'
