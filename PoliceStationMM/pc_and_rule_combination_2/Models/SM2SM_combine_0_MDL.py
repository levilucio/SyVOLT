"""
__SM2SM_combine_0_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Jan 16 17:15:43 2015
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Male_S import *
from MT_pre__Station_T import *
from MT_pre__Male_T import *
from MT_pre__Attribute import *
from MT_pre__indirectLink_S import *
from MT_pre__trace_link import *
from MT_pre__hasAttr_S import *
from NAC import *
from RHS import *
from LHS import *
from MT_post__Attribute import *
from MT_post__Equation import *
from MT_post__MatchModel import *
from MT_post__indirectLink_S import *
from MT_post__paired_with import *
from MT_post__hasAttr_S import *
from MT_post__Constant import *
from MT_post__directLink_T import *
from MT_post__Station_T import *
from MT_post__ApplyModel import *
from MT_post__trace_link import *
from MT_post__rightExpr import *
from MT_post__Station_S import *
from MT_post__Male_T import *
from MT_post__Male_S import *
from MT_post__apply_contains import *
from MT_post__leftExpr import *
from MT_post__match_contains import *
from graph_MT_post__Male_S import *
from graph_MT_post__Male_T import *
from graph_LHS import *
from graph_MT_post__ApplyModel import *
from graph_MT_pre__hasAttr_S import *
from graph_MT_post__Equation import *
from graph_MT_post__MatchModel import *
from graph_RHS import *
from graph_MT_post__Constant import *
from graph_MT_pre__trace_link import *
from graph_MT_post__rightExpr import *
from graph_MT_post__trace_link import *
from graph_MT_post__paired_with import *
from graph_MT_pre__Male_T import *
from graph_MT_pre__Male_S import *
from graph_MT_pre__indirectLink_S import *
from graph_MT_pre__Station_S import *
from graph_MT_post__apply_contains import *
from graph_MT_post__directLink_T import *
from graph_MT_pre__Station_T import *
from graph_NAC import *
from graph_MT_post__leftExpr import *
from graph_MT_post__match_contains import *
from graph_MT_post__Attribute import *
from graph_MT_post__hasAttr_S import *
from graph_MT_post__Station_T import *
from graph_MT_post__Station_S import *
from graph_MT_post__indirectLink_S import *
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

def SM2SM_combine_0_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MT_post__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('SM2SM_combine_0')
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
       new_obj = graph_MT_pre__Station_S(600.0,220.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=MT_pre__Station_S(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj60.MT_pivotOut__.setValue('')
    self.obj60.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj60.MT_subtypeMatching__.setValue(('True', 0))
    self.obj60.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj60.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj60.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj60.MT_pivotIn__.setValue('')
    self.obj60.MT_pivotIn__.setNone()

    # MT_label__
    self.obj60.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj60.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj60.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj60.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj60.MT_pre__name.setHeight(15)

    self.obj60.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(160.0,220.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=MT_pre__Male_S(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj61.MT_pivotOut__.setValue('')
    self.obj61.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj61.MT_subtypeMatching__.setValue(('True', 0))
    self.obj61.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj61.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj61.MT_pivotIn__.setValue('')
    self.obj61.MT_pivotIn__.setNone()

    # MT_label__
    self.obj61.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj61.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj61.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__name.setHeight(15)

    self.obj61.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(780.0,220.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=MT_pre__Male_S(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj62.MT_pivotOut__.setValue('')
    self.obj62.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj62.MT_subtypeMatching__.setValue(('True', 0))
    self.obj62.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj62.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj62.MT_pivotIn__.setValue('')
    self.obj62.MT_pivotIn__.setNone()

    # MT_label__
    self.obj62.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj62.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj62.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__name.setHeight(15)

    self.obj62.graphClass_= graph_MT_pre__Male_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_S(340.0,220.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=MT_pre__Station_T(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63.MT_pivotOut__.setValue('')
    self.obj63.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63.MT_pivotIn__.setValue('')
    self.obj63.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63.MT_label__.setValue('3')

    # MT_pre__name
    self.obj63.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__name.setHeight(15)

    self.obj63.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(600.0,400.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=MT_pre__Male_T(self)
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
    self.obj64.MT_label__.setValue('4')

    # MT_pre__name
    self.obj64.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj64.MT_pre__name.setHeight(15)

    self.obj64.graphClass_= graph_MT_pre__Male_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Male_T(780.0,400.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=MT_pre__Attribute(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # MT_label__
    self.obj65.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj65.MT_pivotOut__.setValue('')
    self.obj65.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj65.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nif attr_value == "name":\n    return True\n\nreturn False\n')
    self.obj65.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj65.MT_subtypeMatching__.setValue(('True', 0))
    self.obj65.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj65.MT_pivotIn__.setValue('')
    self.obj65.MT_pivotIn__.setNone()

    self.obj65.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(620.0,493.0,self.obj65)
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

    self.obj66=MT_pre__Attribute(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # MT_label__
    self.obj66.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj66.MT_pivotOut__.setValue('')
    self.obj66.MT_pivotOut__.setNone()

    # MT_pre__name
    self.obj66.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nif attr_value == "name":\n    return True\n\nreturn False\n')
    self.obj66.MT_pre__name.setHeight(15)

    # MT_subtypeMatching__
    self.obj66.MT_subtypeMatching__.setValue(('True', 0))
    self.obj66.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj66.MT_pivotIn__.setValue('')
    self.obj66.MT_pivotIn__.setNone()

    self.obj66.graphClass_= graph_MT_pre__Attribute
    if self.genGraphics:
       new_obj = graph_MT_pre__Attribute(800.0,493.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=MT_pre__indirectLink_S(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # MT_label__
    self.obj67.MT_label__.setValue('30')

    # MT_pivotOut__
    self.obj67.MT_pivotOut__.setValue('')
    self.obj67.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj67.MT_subtypeMatching__.setValue(('True', 0))
    self.obj67.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj67.MT_pivotIn__.setValue('')
    self.obj67.MT_pivotIn__.setNone()

    self.obj67.graphClass_= graph_MT_pre__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__indirectLink_S(311.0,261.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=MT_pre__trace_link(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # MT_label__
    self.obj68.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj68.MT_pivotOut__.setValue('')
    self.obj68.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj68.MT_subtypeMatching__.setValue(('True', 0))
    self.obj68.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj68.MT_pivotIn__.setValue('')
    self.obj68.MT_pivotIn__.setNone()

    self.obj68.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(661.0,351.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=MT_pre__trace_link(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # MT_label__
    self.obj69.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj69.MT_pivotOut__.setValue('')
    self.obj69.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj69.MT_subtypeMatching__.setValue(('True', 0))
    self.obj69.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj69.MT_pivotIn__.setValue('')
    self.obj69.MT_pivotIn__.setNone()

    self.obj69.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(841.0,351.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=MT_pre__hasAttr_S(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # MT_label__
    self.obj70.MT_label__.setValue('31')

    # MT_pivotOut__
    self.obj70.MT_pivotOut__.setValue('')
    self.obj70.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj70.MT_subtypeMatching__.setValue(('True', 0))
    self.obj70.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj70.MT_pivotIn__.setValue('')
    self.obj70.MT_pivotIn__.setNone()

    self.obj70.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(667.0,392.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=MT_pre__hasAttr_S(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('33')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj71.MT_subtypeMatching__.setValue(('True', 0))
    self.obj71.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj71.MT_pivotIn__.setValue('')
    self.obj71.MT_pivotIn__.setNone()

    self.obj71.graphClass_= graph_MT_pre__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_pre__hasAttr_S(847.0,395.5,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj92=NAC(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # constraint
    self.obj92.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the NAC have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True forbids the rule from being applied,\n#    returning False enables the rule to be applied.\n#===============================================================================\n\nreturn True\n')
    self.obj92.constraint.setHeight(15)

    self.obj92.graphClass_= graph_NAC
    if self.genGraphics:
       new_obj = graph_NAC(120.0,160.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("NAC", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=RHS(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # action
    self.obj93.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj93.action.setHeight(15)

    self.obj93.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(1000.0,160.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=LHS(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # constraint
    self.obj94.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn "name"\n')
    self.obj94.constraint.setHeight(15)

    self.obj94.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(560.0,160.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj72=MT_post__Attribute(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # MT_label__
    self.obj72.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj72.MT_pivotOut__.setValue('')
    self.obj72.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj72.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj72.MT_post__name.setHeight(15)

    self.obj72.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(1060.0,460.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=MT_post__Attribute(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_label__
    self.obj73.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('')
    self.obj73.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj73.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj73.MT_post__name.setHeight(15)

    self.obj73.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(1380.0,200.0,self.obj73)
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

    self.obj74=MT_post__Equation(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_label__
    self.obj74.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    self.obj74.graphClass_= graph_MT_post__Equation
    if self.genGraphics:
       new_obj = graph_MT_post__Equation(1140.0,460.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=MT_post__Equation(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_label__
    self.obj75.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    self.obj75.graphClass_= graph_MT_post__Equation
    if self.genGraphics:
       new_obj = graph_MT_post__Equation(1360.0,320.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj109=MT_post__MatchModel(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # MT_label__
    self.obj109.MT_label__.setValue('36')

    # MT_pivotOut__
    self.obj109.MT_pivotOut__.setValue('')
    self.obj109.MT_pivotOut__.setNone()

    self.obj109.graphClass_= graph_MT_post__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_post__MatchModel(1100.0,440.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj76=MT_post__indirectLink_S(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_label__
    self.obj76.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    self.obj76.graphClass_= graph_MT_post__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__indirectLink_S(1211.0,241.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj114=MT_post__paired_with(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # MT_label__
    self.obj114.MT_label__.setValue('41')

    # MT_pivotOut__
    self.obj114.MT_pivotOut__.setValue('')
    self.obj114.MT_pivotOut__.setNone()

    self.obj114.graphClass_= graph_MT_post__paired_with
    if self.genGraphics:
       new_obj = graph_MT_post__paired_with(1296.0,481.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj77=MT_post__hasAttr_S(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_label__
    self.obj77.MT_label__.setValue('31')

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    self.obj77.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(1127.0,365.5,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=MT_post__hasAttr_S(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # MT_label__
    self.obj78.MT_label__.setValue('33')

    # MT_pivotOut__
    self.obj78.MT_pivotOut__.setValue('')
    self.obj78.MT_pivotOut__.setNone()

    self.obj78.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(1357.0,235.5,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=MT_post__Constant(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # MT_label__
    self.obj79.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj79.MT_pivotOut__.setValue('')
    self.obj79.MT_pivotOut__.setNone()

    # MT_post__value
    self.obj79.MT_post__value.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "somestation"\n')
    self.obj79.MT_post__value.setHeight(15)

    self.obj79.graphClass_= graph_MT_post__Constant
    if self.genGraphics:
       new_obj = graph_MT_post__Constant(1260.0,420.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=MT_post__Constant(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # MT_label__
    self.obj80.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj80.MT_pivotOut__.setValue('')
    self.obj80.MT_pivotOut__.setNone()

    # MT_post__value
    self.obj80.MT_post__value.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "somemale"\n')
    self.obj80.MT_post__value.setHeight(15)

    self.obj80.graphClass_= graph_MT_post__Constant
    if self.genGraphics:
       new_obj = graph_MT_post__Constant(1380.0,460.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=MT_post__directLink_T(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj81.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj81.MT_post__associationType.setHeight(15)

    self.obj81.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(1251.0,361.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=MT_post__Station_T(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_label__
    self.obj82.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj82.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj82.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj82.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj82.MT_post__name.setHeight(15)

    self.obj82.graphClass_= graph_MT_post__Station_T
    if self.genGraphics:
       new_obj = graph_MT_post__Station_T(1120.0,320.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj107=MT_post__ApplyModel(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # MT_label__
    self.obj107.MT_label__.setValue('35')

    # MT_pivotOut__
    self.obj107.MT_pivotOut__.setValue('')
    self.obj107.MT_pivotOut__.setNone()

    self.obj107.graphClass_= graph_MT_post__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_post__ApplyModel(1320.0,440.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj83=MT_post__trace_link(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_label__
    self.obj83.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    self.obj83.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1161.0,301.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=MT_post__trace_link(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # MT_label__
    self.obj84.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj84.MT_pivotOut__.setValue('')
    self.obj84.MT_pivotOut__.setNone()

    self.obj84.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1301.0,301.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=MT_post__rightExpr(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # MT_label__
    self.obj85.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj85.MT_pivotOut__.setValue('')
    self.obj85.MT_pivotOut__.setNone()

    self.obj85.graphClass_= graph_MT_post__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_post__rightExpr(1263.5,480.5,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=MT_post__rightExpr(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # MT_label__
    self.obj86.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj86.MT_pivotOut__.setValue('')
    self.obj86.MT_pivotOut__.setNone()

    self.obj86.graphClass_= graph_MT_post__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_post__rightExpr(1433.5,430.5,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=MT_post__Station_S(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj87.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj87.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj87.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__name.setHeight(15)

    self.obj87.graphClass_= graph_MT_post__Station_S
    if self.genGraphics:
       new_obj = graph_MT_post__Station_S(1080.0,200.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=MT_post__Male_T(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # MT_label__
    self.obj88.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj88.MT_pivotOut__.setValue('')
    self.obj88.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj88.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj88.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj88.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj88.MT_post__name.setHeight(15)

    self.obj88.graphClass_= graph_MT_post__Male_T
    if self.genGraphics:
       new_obj = graph_MT_post__Male_T(1260.0,320.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=MT_post__Male_S(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # MT_label__
    self.obj89.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj89.MT_pivotOut__.setValue('')
    self.obj89.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj89.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj89.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj89.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj89.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj89.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj89.MT_post__name.setHeight(15)

    self.obj89.graphClass_= graph_MT_post__Male_S
    if self.genGraphics:
       new_obj = graph_MT_post__Male_S(1220.0,200.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Male_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj112=MT_post__apply_contains(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # MT_label__
    self.obj112.MT_label__.setValue('39')

    # MT_pivotOut__
    self.obj112.MT_pivotOut__.setValue('')
    self.obj112.MT_pivotOut__.setNone()

    self.obj112.graphClass_= graph_MT_post__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_post__apply_contains(1294.5,421.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=MT_post__apply_contains(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # MT_label__
    self.obj113.MT_label__.setValue('40')

    # MT_pivotOut__
    self.obj113.MT_pivotOut__.setValue('')
    self.obj113.MT_pivotOut__.setNone()

    self.obj113.graphClass_= graph_MT_post__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_post__apply_contains(1364.5,421.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj90=MT_post__leftExpr(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # MT_label__
    self.obj90.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj90.MT_pivotOut__.setValue('')
    self.obj90.MT_pivotOut__.setNone()

    self.obj90.graphClass_= graph_MT_post__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_post__leftExpr(1162.5,496.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=MT_post__leftExpr(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # MT_label__
    self.obj91.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj91.MT_pivotOut__.setValue('')
    self.obj91.MT_pivotOut__.setNone()

    self.obj91.graphClass_= graph_MT_post__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_post__leftExpr(1432.5,296.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj110=MT_post__match_contains(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # MT_label__
    self.obj110.MT_label__.setValue('37')

    # MT_pivotOut__
    self.obj110.MT_pivotOut__.setValue('')
    self.obj110.MT_pivotOut__.setNone()

    self.obj110.graphClass_= graph_MT_post__match_contains
    if self.genGraphics:
       new_obj = graph_MT_post__match_contains(1162.5,361.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=MT_post__match_contains(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # MT_label__
    self.obj111.MT_label__.setValue('38')

    # MT_pivotOut__
    self.obj111.MT_pivotOut__.setValue('')
    self.obj111.MT_pivotOut__.setNone()

    self.obj111.graphClass_= graph_MT_post__match_contains
    if self.genGraphics:
       new_obj = graph_MT_post__match_contains(1232.5,361.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    # Connections for obj59 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
(self.obj59,self.obj70,[661.0, 261.0, 667.0, 392.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj1) of type MT_pre__Station_S
    self.drawConnections(
(self.obj60,self.obj67,[221.0, 261.0, 311.0, 261.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj2) of type MT_pre__Male_S
    self.drawConnections(
(self.obj61,self.obj71,[841.0, 261.0, 847.0, 395.5],"true", 2) )
    # Connections for obj62 (graphObject_: Obj3) of type MT_pre__Male_S
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj4) of type MT_pre__Station_T
    self.drawConnections(
(self.obj63,self.obj68,[661.0, 441.0, 661.0, 351.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj5) of type MT_pre__Male_T
    self.drawConnections(
(self.obj64,self.obj69,[841.0, 441.0, 841.0, 351.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj6) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj66 (graphObject_: Obj7) of type MT_pre__Attribute
    self.drawConnections(
 )
    # Connections for obj67 (graphObject_: Obj8) of type MT_pre__indirectLink_S
    self.drawConnections(
(self.obj67,self.obj62,[311.0, 261.0, 401.0, 261.0],"true", 2) )
    # Connections for obj68 (graphObject_: Obj9) of type MT_pre__trace_link
    self.drawConnections(
(self.obj68,self.obj59,[661.0, 351.0, 661.0, 261.0],"true", 2) )
    # Connections for obj69 (graphObject_: Obj10) of type MT_pre__trace_link
    self.drawConnections(
(self.obj69,self.obj61,[841.0, 351.0, 841.0, 261.0],"true", 2) )
    # Connections for obj70 (graphObject_: Obj11) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj70,self.obj65,[667.0, 392.0, 673.0, 523.0],"true", 2) )
    # Connections for obj71 (graphObject_: Obj12) of type MT_pre__hasAttr_S
    self.drawConnections(
(self.obj71,self.obj66,[847.0, 395.5, 853.0, 523.0],"true", 2) )
    # Connections for obj92 (graphObject_: Obj33) of type NAC
    self.drawConnections(
 )
    # Connections for obj93 (graphObject_: Obj34) of type RHS
    self.drawConnections(
 )
    # Connections for obj94 (graphObject_: Obj35) of type LHS
    self.drawConnections(
 )
    # Connections for obj72 (graphObject_: Obj13) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj73 (graphObject_: Obj14) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj15) of type MT_post__Equation
    self.drawConnections(
(self.obj74,self.obj90,[1212.0, 502.0, 1162.5, 496.0],"true", 2),
(self.obj74,self.obj85,[1212.0, 502.0, 1263.5, 480.5],"true", 2) )
    # Connections for obj75 (graphObject_: Obj16) of type MT_post__Equation
    self.drawConnections(
(self.obj75,self.obj91,[1432.0, 362.0, 1432.5, 296.0],"true", 2),
(self.obj75,self.obj86,[1432.0, 362.0, 1433.5, 430.5],"true", 2) )
    # Connections for obj109 (graphObject_: Obj42) of type MT_post__MatchModel
    self.drawConnections(
(self.obj109,self.obj110,[1184.0, 481.0, 1162.5, 361.0],"true", 2),
(self.obj109,self.obj111,[1184.0, 481.0, 1232.5, 361.0],"true", 2),
(self.obj109,self.obj114,[1184.0, 481.0, 1296.0, 481.0],"true", 2) )
    # Connections for obj76 (graphObject_: Obj17) of type MT_post__indirectLink_S
    self.drawConnections(
(self.obj76,self.obj89,[1211.0, 241.0, 1281.0, 241.0],"true", 2) )
    # Connections for obj114 (graphObject_: Obj47) of type MT_post__paired_with
    self.drawConnections(
(self.obj114,self.obj107,[1296.0, 481.0, 1408.0, 481.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj18) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj77,self.obj72,[1127.0, 365.5, 1113.0, 490.0],"true", 2) )
    # Connections for obj78 (graphObject_: Obj19) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj78,self.obj73,[1357.0, 235.5, 1433.0, 230.0],"true", 2) )
    # Connections for obj79 (graphObject_: Obj20) of type MT_post__Constant
    self.drawConnections(
 )
    # Connections for obj80 (graphObject_: Obj21) of type MT_post__Constant
    self.drawConnections(
 )
    # Connections for obj81 (graphObject_: Obj22) of type MT_post__directLink_T
    self.drawConnections(
(self.obj81,self.obj88,[1251.0, 361.0, 1321.0, 361.0],"true", 2) )
    # Connections for obj82 (graphObject_: Obj23) of type MT_post__Station_T
    self.drawConnections(
(self.obj82,self.obj81,[1181.0, 361.0, 1251.0, 361.0],"true", 2),
(self.obj82,self.obj83,[1181.0, 361.0, 1161.0, 301.0],"true", 2) )
    # Connections for obj107 (graphObject_: Obj40) of type MT_post__ApplyModel
    self.drawConnections(
(self.obj107,self.obj112,[1408.0, 481.0, 1294.5, 421.0],"true", 2),
(self.obj107,self.obj113,[1408.0, 481.0, 1364.5, 421.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj24) of type MT_post__trace_link
    self.drawConnections(
(self.obj83,self.obj87,[1161.0, 301.0, 1141.0, 241.0],"true", 2) )
    # Connections for obj84 (graphObject_: Obj25) of type MT_post__trace_link
    self.drawConnections(
(self.obj84,self.obj89,[1301.0, 301.0, 1281.0, 241.0],"true", 2) )
    # Connections for obj85 (graphObject_: Obj26) of type MT_post__rightExpr
    self.drawConnections(
(self.obj85,self.obj79,[1263.5, 480.5, 1315.0, 459.0],"true", 2) )
    # Connections for obj86 (graphObject_: Obj27) of type MT_post__rightExpr
    self.drawConnections(
(self.obj86,self.obj80,[1433.5, 430.5, 1435.0, 499.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj28) of type MT_post__Station_S
    self.drawConnections(
(self.obj87,self.obj76,[1141.0, 241.0, 1211.0, 241.0],"true", 2),
(self.obj87,self.obj77,[1141.0, 241.0, 1127.0, 365.5],"true", 2) )
    # Connections for obj88 (graphObject_: Obj29) of type MT_post__Male_T
    self.drawConnections(
(self.obj88,self.obj84,[1321.0, 361.0, 1301.0, 301.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj30) of type MT_post__Male_S
    self.drawConnections(
(self.obj89,self.obj78,[1281.0, 241.0, 1357.0, 235.5],"true", 2) )
    # Connections for obj112 (graphObject_: Obj45) of type MT_post__apply_contains
    self.drawConnections(
(self.obj112,self.obj82,[1294.5, 421.0, 1181.0, 361.0],"true", 2) )
    # Connections for obj113 (graphObject_: Obj46) of type MT_post__apply_contains
    self.drawConnections(
(self.obj113,self.obj88,[1364.5, 421.0, 1321.0, 361.0],"true", 2) )
    # Connections for obj90 (graphObject_: Obj31) of type MT_post__leftExpr
    self.drawConnections(
(self.obj90,self.obj72,[1162.5, 496.0, 1113.0, 490.0],"true", 2) )
    # Connections for obj91 (graphObject_: Obj32) of type MT_post__leftExpr
    self.drawConnections(
(self.obj91,self.obj73,[1432.5, 296.0, 1433.0, 230.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj43) of type MT_post__match_contains
    self.drawConnections(
(self.obj110,self.obj87,[1162.5, 361.0, 1141.0, 241.0],"true", 2) )
    # Connections for obj111 (graphObject_: Obj44) of type MT_post__match_contains
    self.drawConnections(
(self.obj111,self.obj89,[1232.5, 361.0, 1281.0, 241.0],"true", 2) )

newfunction = SM2SM_combine_0_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MT_post__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
