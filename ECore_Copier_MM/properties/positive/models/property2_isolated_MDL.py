"""
__property2_isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Tue May  5 14:15:00 2015
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__EClass import *
from MT_pre__EReference import *
from MT_pre__MatchModel import *
from MT_pre__ApplyModel import *
from MT_pre__match_contains import *
from MT_pre__apply_contains import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__EReference import *
from graph_MT_pre__apply_contains import *
from graph_LHS import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_MT_pre__ApplyModel import *
from graph_MT_pre__EClass import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
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

def property2_isolated_MDL(self, rootNode, MT_pre__ECoreMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('property1_complete')
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
       new_obj = graph_MT_pre__EClass(200.0,220.0,self.obj38)
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

    self.obj49=MT_pre__EClass(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # MT_label__
    self.obj49.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj49.MT_pivotOut__.setValue('')
    self.obj49.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj49.MT_subtypeMatching__.setValue(('True', 0))
    self.obj49.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj49.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj49.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj49.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj49.MT_pivotIn__.setValue('')
    self.obj49.MT_pivotIn__.setNone()

    self.obj49.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(200.0,420.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj54=MT_pre__EClass(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # MT_label__
    self.obj54.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj54.MT_pivotOut__.setValue('')
    self.obj54.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj54.MT_subtypeMatching__.setValue(('True', 0))
    self.obj54.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj54.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj54.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj54.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj54.MT_pivotIn__.setValue('')
    self.obj54.MT_pivotIn__.setNone()

    self.obj54.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(480.0,320.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj81=MT_pre__EClass(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj81.MT_subtypeMatching__.setValue(('True', 0))
    self.obj81.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj81.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj81.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj81.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj81.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj81.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj81.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj81.MT_pivotIn__.setValue('')
    self.obj81.MT_pivotIn__.setNone()

    self.obj81.graphClass_= graph_MT_pre__EClass
    if self.genGraphics:
       new_obj = graph_MT_pre__EClass(500.0,160.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EClass", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj44=MT_pre__EReference(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # MT_label__
    self.obj44.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj44.MT_pivotOut__.setValue('')
    self.obj44.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj44.MT_subtypeMatching__.setValue(('True', 0))
    self.obj44.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj44.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj44.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj44.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj44.MT_pivotIn__.setValue('')
    self.obj44.MT_pivotIn__.setNone()

    self.obj44.graphClass_= graph_MT_pre__EReference
    if self.genGraphics:
       new_obj = graph_MT_pre__EReference(360.0,120.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EReference", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=MT_pre__EReference(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # MT_label__
    self.obj45.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj45.MT_pivotOut__.setValue('')
    self.obj45.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj45.MT_subtypeMatching__.setValue(('True', 0))
    self.obj45.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj45.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj45.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj45.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj45.MT_pivotIn__.setValue('')
    self.obj45.MT_pivotIn__.setNone()

    self.obj45.graphClass_= graph_MT_pre__EReference
    if self.genGraphics:
       new_obj = graph_MT_pre__EReference(360.0,220.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EReference", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj55=MT_pre__EReference(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_label__
    self.obj55.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj55.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj55.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj55.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    self.obj55.graphClass_= graph_MT_pre__EReference
    if self.genGraphics:
       new_obj = graph_MT_pre__EReference(340.0,320.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EReference", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=MT_pre__EReference(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_label__
    self.obj56.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj56.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj56.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj56.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    self.obj56.graphClass_= graph_MT_pre__EReference
    if self.genGraphics:
       new_obj = graph_MT_pre__EReference(360.0,420.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__EReference", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj40=MT_pre__MatchModel(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # MT_label__
    self.obj40.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj40.MT_pivotOut__.setValue('')
    self.obj40.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj40.MT_subtypeMatching__.setValue(('True', 0))
    self.obj40.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj40.MT_pivotIn__.setValue('')
    self.obj40.MT_pivotIn__.setNone()

    self.obj40.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(180.0,120.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.04
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj46=MT_pre__ApplyModel(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # MT_label__
    self.obj46.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj46.MT_pivotOut__.setValue('')
    self.obj46.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj46.MT_subtypeMatching__.setValue(('True', 0))
    self.obj46.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj46.MT_pivotIn__.setValue('')
    self.obj46.MT_pivotIn__.setNone()

    self.obj46.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(180.0,320.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj41=MT_pre__match_contains(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # MT_label__
    self.obj41.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj41.MT_pivotOut__.setValue('')
    self.obj41.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj41.MT_subtypeMatching__.setValue(('True', 0))
    self.obj41.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj41.MT_pivotIn__.setValue('')
    self.obj41.MT_pivotIn__.setNone()

    self.obj41.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(330.5,191.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj57=MT_pre__match_contains(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # MT_label__
    self.obj57.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj57.MT_pivotOut__.setValue('')
    self.obj57.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj57.MT_subtypeMatching__.setValue(('True', 0))
    self.obj57.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj57.MT_pivotIn__.setValue('')
    self.obj57.MT_pivotIn__.setNone()

    self.obj57.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(340.5,211.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=MT_pre__match_contains(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # MT_label__
    self.obj58.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj58.MT_pivotOut__.setValue('')
    self.obj58.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj58.MT_subtypeMatching__.setValue(('True', 0))
    self.obj58.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj58.MT_pivotIn__.setValue('')
    self.obj58.MT_pivotIn__.setNone()

    self.obj58.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(340.5,161.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=MT_pre__apply_contains(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # MT_label__
    self.obj59.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj59.MT_pivotOut__.setValue('')
    self.obj59.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj59.MT_subtypeMatching__.setValue(('True', 0))
    self.obj59.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj59.MT_pivotIn__.setValue('')
    self.obj59.MT_pivotIn__.setNone()

    self.obj59.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(332.5,361.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=MT_pre__apply_contains(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # MT_label__
    self.obj60.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj60.MT_pivotOut__.setValue('')
    self.obj60.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj60.MT_subtypeMatching__.setValue(('True', 0))
    self.obj60.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj60.MT_pivotIn__.setValue('')
    self.obj60.MT_pivotIn__.setNone()

    self.obj60.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(402.5,361.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=MT_pre__apply_contains(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # MT_label__
    self.obj61.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj61.MT_pivotOut__.setValue('')
    self.obj61.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj61.MT_subtypeMatching__.setValue(('True', 0))
    self.obj61.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj61.MT_pivotIn__.setValue('')
    self.obj61.MT_pivotIn__.setNone()

    self.obj61.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(262.5,411.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=MT_pre__apply_contains(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # MT_label__
    self.obj62.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj62.MT_pivotOut__.setValue('')
    self.obj62.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj62.MT_subtypeMatching__.setValue(('True', 0))
    self.obj62.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj62.MT_pivotIn__.setValue('')
    self.obj62.MT_pivotIn__.setNone()

    self.obj62.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(342.5,411.5,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj128=MT_pre__directLink_T(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # MT_label__
    self.obj128.MT_label__.setValue('27')

    # MT_pivotOut__
    self.obj128.MT_pivotOut__.setValue('')
    self.obj128.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj128.MT_subtypeMatching__.setValue(('True', 0))
    self.obj128.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj128.MT_pivotIn__.setValue('')
    self.obj128.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj128.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eType"\n')
    self.obj128.MT_pre__associationType.setHeight(15)

    self.obj128.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(470.0,362.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=MT_pre__directLink_T(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_label__
    self.obj129.MT_label__.setValue('28')

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('')
    self.obj129.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('')
    self.obj129.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj129.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj129.MT_pre__associationType.setHeight(15)

    self.obj129.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(480.0,412.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=MT_pre__directLink_T(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # MT_label__
    self.obj130.MT_label__.setValue('29')

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
    self.obj130.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eType"\n')
    self.obj130.MT_pre__associationType.setHeight(15)

    self.obj130.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(340.0,462.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=MT_pre__directLink_T(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # MT_label__
    self.obj131.MT_label__.setValue('30')

    # MT_pivotOut__
    self.obj131.MT_pivotOut__.setValue('')
    self.obj131.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj131.MT_subtypeMatching__.setValue(('True', 0))
    self.obj131.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj131.MT_pivotIn__.setValue('')
    self.obj131.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj131.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj131.MT_pre__associationType.setHeight(15)

    self.obj131.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(330.0,412.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj94=MT_pre__directLink_S(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # MT_label__
    self.obj94.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj94.MT_pivotOut__.setValue('')
    self.obj94.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj94.MT_subtypeMatching__.setValue(('True', 0))
    self.obj94.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj94.MT_pivotIn__.setValue('')
    self.obj94.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj94.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eType"\n')
    self.obj94.MT_pre__associationType.setHeight(15)

    self.obj94.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,182.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=MT_pre__directLink_S(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # MT_label__
    self.obj95.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj95.MT_pivotOut__.setValue('')
    self.obj95.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj95.MT_subtypeMatching__.setValue(('True', 0))
    self.obj95.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj95.MT_pivotIn__.setValue('')
    self.obj95.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj95.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj95.MT_pre__associationType.setHeight(15)

    self.obj95.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(490.0,232.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=MT_pre__directLink_S(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # MT_label__
    self.obj96.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj96.MT_pivotOut__.setValue('')
    self.obj96.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj96.MT_subtypeMatching__.setValue(('True', 0))
    self.obj96.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj96.MT_pivotIn__.setValue('')
    self.obj96.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj96.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eType"\n')
    self.obj96.MT_pre__associationType.setHeight(15)

    self.obj96.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(340.0,262.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=MT_pre__directLink_S(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    # MT_label__
    self.obj97.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj97.MT_pivotOut__.setValue('')
    self.obj97.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj97.MT_subtypeMatching__.setValue(('True', 0))
    self.obj97.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj97.MT_pivotIn__.setValue('')
    self.obj97.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj97.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "eStructuralFeatures"\n')
    self.obj97.MT_pre__associationType.setHeight(15)

    self.obj97.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(340.0,212.0,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj43=LHS(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # constraint
    self.obj43.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj43.constraint.setHeight(15)

    self.obj43.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(700.0,180.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    # Connections for obj38 (graphObject_: Obj0) of type MT_pre__EClass
    self.drawConnections(
(self.obj38,self.obj97,[260.0, 262.0, 340.0, 212.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj9) of type MT_pre__EClass
    self.drawConnections(
(self.obj49,self.obj131,[260.0, 462.0, 330.0, 412.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj10) of type MT_pre__EClass
    self.drawConnections(
(self.obj54,self.obj129,[540.0, 362.0, 480.0, 412.0],"true", 2) )
    # Connections for obj81 (graphObject_: Obj19) of type MT_pre__EClass
    self.drawConnections(
(self.obj81,self.obj95,[560.0, 202.0, 490.0, 232.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj6) of type MT_pre__EReference
    self.drawConnections(
(self.obj44,self.obj94,[420.0, 162.0, 490.0, 182.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj7) of type MT_pre__EReference
    self.drawConnections(
(self.obj45,self.obj96,[420.0, 262.0, 340.0, 262.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj11) of type MT_pre__EReference
    self.drawConnections(
(self.obj55,self.obj128,[400.0, 362.0, 470.0, 362.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj12) of type MT_pre__EReference
    self.drawConnections(
(self.obj56,self.obj130,[420.0, 462.0, 340.0, 462.0],"true", 2) )
    # Connections for obj40 (graphObject_: Obj2) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj40,self.obj41,[261.0, 161.0, 330.5, 191.5],"true", 2),
(self.obj40,self.obj57,[261.0, 161.0, 340.5, 211.5],"true", 2),
(self.obj40,self.obj58,[261.0, 161.0, 340.5, 161.5],"true", 2) )
    # Connections for obj46 (graphObject_: Obj8) of type MT_pre__ApplyModel
    self.drawConnections(
(self.obj46,self.obj59,[265.0, 361.0, 332.5, 361.5],"true", 2),
(self.obj46,self.obj60,[265.0, 361.0, 402.5, 361.5],"true", 2),
(self.obj46,self.obj61,[265.0, 361.0, 262.5, 411.5],"true", 2),
(self.obj46,self.obj62,[265.0, 361.0, 342.5, 411.5],"true", 2) )
    # Connections for obj41 (graphObject_: Obj3) of type MT_pre__match_contains
    self.drawConnections(
(self.obj41,self.obj38,[330.5, 191.5, 260.0, 262.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj13) of type MT_pre__match_contains
    self.drawConnections(
(self.obj57,self.obj45,[340.5, 211.5, 420.0, 262.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj14) of type MT_pre__match_contains
    self.drawConnections(
(self.obj58,self.obj44,[340.5, 161.5, 420.0, 162.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj15) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj59,self.obj55,[332.5, 361.5, 400.0, 362.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj16) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj60,self.obj54,[402.5, 361.5, 540.0, 362.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj17) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj61,self.obj49,[262.5, 411.5, 260.0, 462.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj18) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj62,self.obj56,[342.5, 411.5, 420.0, 462.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj24) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj128,self.obj54,[470.0, 362.0, 540.0, 362.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj25) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj129,self.obj56,[480.0, 412.0, 420.0, 462.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj26) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj130,self.obj49,[340.0, 462.0, 260.0, 462.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj27) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj131,self.obj55,[330.0, 412.0, 400.0, 362.0],"true", 2) )
    # Connections for obj94 (graphObject_: Obj20) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj94,self.obj81,[490.0, 182.0, 560.0, 202.0],"true", 2) )
    # Connections for obj95 (graphObject_: Obj21) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj95,self.obj45,[490.0, 232.0, 420.0, 262.0],"true", 2) )
    # Connections for obj96 (graphObject_: Obj22) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj96,self.obj38,[340.0, 262.0, 260.0, 262.0],"true", 2) )
    # Connections for obj97 (graphObject_: Obj23) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj97,self.obj44,[340.0, 212.0, 420.0, 162.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj5) of type LHS
    self.drawConnections(
 )

newfunction = property2_isolated_MDL

loadedMMName = ['MT_pre__ECoreMM_META', 'MoTifRule_META']

atom3version = '0.3'
