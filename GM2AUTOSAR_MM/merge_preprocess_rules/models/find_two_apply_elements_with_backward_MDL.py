"""
__find_two_apply_elements_with_backward_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Aug 22 13:55:35 2013
___________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ApplyModel import *
from MT_pre__MetaModelElement_S import *
from MT_pre__MetaModelElement_T import *
from MT_pre__apply_contains import *
from MT_pre__backward_link import *
from MT_post__MetaModelElement_S import *
from MT_post__MetaModelElement_T import *
from MT_post__ApplyModel import *
from MT_post__apply_contains import *
from MT_post__backward_link import *
from RHS import *
from LHS import *
from graph_MT_post__MetaModelElement_S import *
from graph_MT_post__backward_link import *
from graph_MT_pre__apply_contains import *
from graph_MT_post__MetaModelElement_T import *
from graph_LHS import *
from graph_MT_post__ApplyModel import *
from graph_MT_pre__ApplyModel import *
from graph_MT_pre__MetaModelElement_S import *
from graph_MT_pre__backward_link import *
from graph_MT_post__apply_contains import *
from graph_MT_pre__MetaModelElement_T import *
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

def find_two_apply_elements_with_backward_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MT_post__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('FindTwoApplyElementsWithBackward')
    # --- ASG attributes over ---


    self.obj71=MT_pre__ApplyModel(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj71.MT_subtypeMatching__.setValue(('True', 0))
    self.obj71.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj71.MT_pivotIn__.setValue('')
    self.obj71.MT_pivotIn__.setNone()

    self.obj71.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(100.0,460.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=MT_pre__MetaModelElement_S(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj72.MT_pivotOut__.setValue('')
    self.obj72.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj72.MT_subtypeMatching__.setValue(('True', 1))
    self.obj72.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj72.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj72.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj72.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj72.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj72.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj72.MT_pre__name.setHeight(15)

    self.obj72.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(260.0,200.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=MT_pre__MetaModelElement_T(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj73.MT_subtypeMatching__.setValue(('True', 1))
    self.obj73.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj73.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj73.MT_pivotIn__.setValue('')
    self.obj73.MT_pivotIn__.setNone()

    # MT_label__
    self.obj73.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj73.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj73.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj73.MT_pre__name.setHeight(15)

    self.obj73.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(107.0,324.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=MT_pre__MetaModelElement_T(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj74.MT_subtypeMatching__.setValue(('True', 1))
    self.obj74.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj74.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj74.MT_pivotIn__.setValue('')
    self.obj74.MT_pivotIn__.setNone()

    # MT_label__
    self.obj74.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj74.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj74.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__name.setHeight(15)

    self.obj74.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(327.0,324.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=MT_pre__apply_contains(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_label__
    self.obj75.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj75.MT_subtypeMatching__.setValue(('True', 0))
    self.obj75.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj75.MT_pivotIn__.setValue('')
    self.obj75.MT_pivotIn__.setNone()

    self.obj75.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(274.0,465.5,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=MT_pre__backward_link(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_label__
    self.obj76.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj76.MT_subtypeMatching__.setValue(('True', 0))
    self.obj76.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj76.MT_pivotIn__.setValue('')
    self.obj76.MT_pivotIn__.setNone()

    # MT_pre__type
    self.obj76.MT_pre__type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj76.MT_pre__type.setHeight(15)

    self.obj76.graphClass_= graph_MT_pre__backward_link
    if self.genGraphics:
       new_obj = graph_MT_pre__backward_link(337.0,347.5,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=MT_pre__backward_link(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_label__
    self.obj77.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj77.MT_subtypeMatching__.setValue(('True', 0))
    self.obj77.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj77.MT_pivotIn__.setValue('')
    self.obj77.MT_pivotIn__.setNone()

    # MT_pre__type
    self.obj77.MT_pre__type.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj77.MT_pre__type.setHeight(15)

    self.obj77.graphClass_= graph_MT_pre__backward_link
    if self.genGraphics:
       new_obj = graph_MT_pre__backward_link(456.0,327.5,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=MT_post__MetaModelElement_S(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # MT_label__
    self.obj78.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj78.MT_pivotOut__.setValue('')
    self.obj78.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj78.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj78.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj78.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj78.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj78.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj78.MT_post__name.setHeight(15)

    self.obj78.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(740.0,200.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=MT_post__MetaModelElement_T(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # MT_label__
    self.obj79.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj79.MT_pivotOut__.setValue('element1')

    # MT_post__cardinality
    self.obj79.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj79.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj79.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj79.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj79.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj79.MT_post__name.setHeight(15)

    self.obj79.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(600.0,320.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=MT_post__MetaModelElement_T(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # MT_label__
    self.obj80.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj80.MT_pivotOut__.setValue('element2')

    # MT_post__cardinality
    self.obj80.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj80.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj80.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj80.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj80.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj80.MT_post__name.setHeight(15)

    self.obj80.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(800.0,320.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=MT_post__ApplyModel(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    self.obj81.graphClass_= graph_MT_post__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_post__ApplyModel(600.0,460.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=MT_post__apply_contains(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_label__
    self.obj82.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    self.obj82.graphClass_= graph_MT_post__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_post__apply_contains(768.0,463.5,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=MT_post__backward_link(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_label__
    self.obj83.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    # MT_post__type
    self.obj83.MT_post__type.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj83.MT_post__type.setHeight(15)

    self.obj83.graphClass_= graph_MT_post__backward_link
    if self.genGraphics:
       new_obj = graph_MT_post__backward_link(839.0,333.5,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=RHS(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # action
    self.obj84.action.setValue('cardinality1 = PostNode(\'3\')[\'cardinality\']\ncardinality2 = PostNode(\'4\')[\'cardinality\']\n\nif cardinality1 != cardinality2:\n    PostNode(\'3\')[\'cardinality\'] = \'+\'\n')
    self.obj84.action.setHeight(15)

    self.obj84.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(500.0,180.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=LHS(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # constraint
    self.obj85.constraint.setValue('if PreNode(\'4\')[\'classtype\'] == PreNode(\'3\')[\'classtype\']:\n    if len([i for i in graph.neighbors(PreNode(\'4\').index) if graph.vs[i][\'mm__\'] == \'apply_contains\']) == 0:\n    	return True\n\nreturn False\n')
    self.obj85.constraint.setHeight(15)

    self.obj85.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(80.0,180.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    # Connections for obj71 (graphObject_: Obj0) of type MT_pre__ApplyModel
    self.drawConnections(
(self.obj71,self.obj75,[273.0, 534.0, 274.0, 465.5],"true", 2) )
    # Connections for obj72 (graphObject_: Obj1) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj73 (graphObject_: Obj2) of type MT_pre__MetaModelElement_T
    self.drawConnections(
(self.obj73,self.obj76,[275.0, 397.0, 337.0, 347.5],"true", 2) )
    # Connections for obj74 (graphObject_: Obj3) of type MT_pre__MetaModelElement_T
    self.drawConnections(
(self.obj74,self.obj77,[495.0, 397.0, 456.0, 327.5],"true", 2) )
    # Connections for obj75 (graphObject_: Obj4) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj75,self.obj73,[274.0, 465.5, 275.0, 397.0],"true", 2) )
    # Connections for obj76 (graphObject_: Obj5) of type MT_pre__backward_link
    self.drawConnections(
(self.obj76,self.obj72,[337.0, 347.5, 430.0, 274.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj6) of type MT_pre__backward_link
    self.drawConnections(
(self.obj77,self.obj72,[456.0, 327.5, 430.0, 274.0],"true", 2) )
    # Connections for obj78 (graphObject_: Obj7) of type MT_post__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj79 (graphObject_: Obj8) of type MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj79,self.obj83,[768.0, 393.0, 839.0, 333.5],"true", 2) )
    # Connections for obj80 (graphObject_: Obj9) of type MT_post__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj81 (graphObject_: Obj10) of type MT_post__ApplyModel
    self.drawConnections(
(self.obj81,self.obj82,[768.0, 534.0, 768.0, 463.5],"true", 2) )
    # Connections for obj82 (graphObject_: Obj11) of type MT_post__apply_contains
    self.drawConnections(
(self.obj82,self.obj79,[768.0, 463.5, 768.0, 393.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj12) of type MT_post__backward_link
    self.drawConnections(
(self.obj83,self.obj78,[839.0, 333.5, 910.0, 274.0],"true", 2) )
    # Connections for obj84 (graphObject_: Obj13) of type RHS
    self.drawConnections(
 )
    # Connections for obj85 (graphObject_: Obj14) of type LHS
    self.drawConnections(
 )

newfunction = find_two_apply_elements_with_backward_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MT_post__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
