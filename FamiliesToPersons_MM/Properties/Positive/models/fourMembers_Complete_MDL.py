"""
__fourMembers_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Apr 17 13:27:09 2015
__________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Family import *
from MT_pre__Member import *
from MT_pre__CommunityRoot import *
from MT_pre__Man import *
from MT_pre__Woman import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__Family import *
from graph_LHS import *
from graph_MT_pre__CommunityRoot import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Man import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__Member import *
from graph_MT_pre__Woman import *
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

def fourMembers_Complete_MDL(self, rootNode, MT_pre__FamiliesToPersonsMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__FamiliesToPersonsMM ---
    if( MT_pre__FamiliesToPersonsMMRootNode ): 
        # author
        MT_pre__FamiliesToPersonsMMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__FamiliesToPersonsMMRootNode.description.setValue('\n')
        MT_pre__FamiliesToPersonsMMRootNode.description.setHeight(15)

        # name
        MT_pre__FamiliesToPersonsMMRootNode.name.setValue('')
        MT_pre__FamiliesToPersonsMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('fourMembers_Complete')
    # --- ASG attributes over ---


    self.obj37=MT_pre__Family(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj37.MT_pivotOut__.setValue('')
    self.obj37.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj37.MT_subtypeMatching__.setValue(('True', 0))
    self.obj37.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj37.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj37.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj37.MT_pivotIn__.setValue('')
    self.obj37.MT_pivotIn__.setNone()

    # MT_label__
    self.obj37.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj37.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj37.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj37.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj37.MT_pre__name.setHeight(15)

    self.obj37.graphClass_= graph_MT_pre__Family
    if self.genGraphics:
       new_obj = graph_MT_pre__Family(540.0,340.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Family", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=MT_pre__Member(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj38.MT_pivotOut__.setValue('')
    self.obj38.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj38.MT_subtypeMatching__.setValue(('True', 0))
    self.obj38.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj38.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj38.MT_pivotIn__.setValue('')
    self.obj38.MT_pivotIn__.setNone()

    # MT_label__
    self.obj38.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj38.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj38.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj38.MT_pre__name.setHeight(15)

    self.obj38.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(420.0,260.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=MT_pre__Member(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj39.MT_pivotOut__.setValue('')
    self.obj39.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj39.MT_subtypeMatching__.setValue(('True', 0))
    self.obj39.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj39.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj39.MT_pivotIn__.setValue('')
    self.obj39.MT_pivotIn__.setNone()

    # MT_label__
    self.obj39.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj39.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj39.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj39.MT_pre__name.setHeight(15)

    self.obj39.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(660.0,260.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=MT_pre__Member(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj40.MT_pivotOut__.setValue('')
    self.obj40.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj40.MT_subtypeMatching__.setValue(('True', 0))
    self.obj40.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj40.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj40.MT_pivotIn__.setValue('')
    self.obj40.MT_pivotIn__.setNone()

    # MT_label__
    self.obj40.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj40.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj40.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj40.MT_pre__name.setHeight(15)

    self.obj40.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(400.0,380.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=MT_pre__Member(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj41.MT_pivotOut__.setValue('')
    self.obj41.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj41.MT_subtypeMatching__.setValue(('True', 0))
    self.obj41.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj41.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj41.MT_pivotIn__.setValue('')
    self.obj41.MT_pivotIn__.setNone()

    # MT_label__
    self.obj41.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj41.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj41.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj41.MT_pre__name.setHeight(15)

    self.obj41.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(680.0,380.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=MT_pre__CommunityRoot(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj42.MT_pivotOut__.setValue('')
    self.obj42.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj42.MT_subtypeMatching__.setValue(('True', 0))
    self.obj42.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj42.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj42.MT_pivotIn__.setValue('')
    self.obj42.MT_pivotIn__.setNone()

    # MT_label__
    self.obj42.MT_label__.setValue('10')

    # MT_pre__name
    self.obj42.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj42.MT_pre__name.setHeight(15)

    self.obj42.graphClass_= graph_MT_pre__CommunityRoot
    if self.genGraphics:
       new_obj = graph_MT_pre__CommunityRoot(540.0,460.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CommunityRoot", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=MT_pre__Man(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj43.MT_pivotOut__.setValue('')
    self.obj43.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj43.MT_subtypeMatching__.setValue(('True', 0))
    self.obj43.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj43.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj43.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj43.MT_pivotIn__.setValue('')
    self.obj43.MT_pivotIn__.setNone()

    # MT_label__
    self.obj43.MT_label__.setValue('11')

    # MT_pre__name
    self.obj43.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj43.MT_pre__name.setHeight(15)

    self.obj43.graphClass_= graph_MT_pre__Man
    if self.genGraphics:
       new_obj = graph_MT_pre__Man(400.0,480.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Man", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=MT_pre__Man(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj44.MT_pivotOut__.setValue('')
    self.obj44.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj44.MT_subtypeMatching__.setValue(('True', 0))
    self.obj44.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj44.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj44.MT_pivotIn__.setValue('')
    self.obj44.MT_pivotIn__.setNone()

    # MT_label__
    self.obj44.MT_label__.setValue('12')

    # MT_pre__name
    self.obj44.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__name.setHeight(15)

    self.obj44.graphClass_= graph_MT_pre__Man
    if self.genGraphics:
       new_obj = graph_MT_pre__Man(400.0,560.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Man", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=MT_pre__Woman(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj45.MT_pivotOut__.setValue('')
    self.obj45.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj45.MT_subtypeMatching__.setValue(('True', 0))
    self.obj45.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj45.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj45.MT_pivotIn__.setValue('')
    self.obj45.MT_pivotIn__.setNone()

    # MT_label__
    self.obj45.MT_label__.setValue('13')

    # MT_pre__name
    self.obj45.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__name.setHeight(15)

    self.obj45.graphClass_= graph_MT_pre__Woman
    if self.genGraphics:
       new_obj = graph_MT_pre__Woman(680.0,480.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Woman", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=MT_pre__Woman(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj46.MT_pivotOut__.setValue('')
    self.obj46.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj46.MT_subtypeMatching__.setValue(('True', 0))
    self.obj46.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj46.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj46.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj46.MT_pivotIn__.setValue('')
    self.obj46.MT_pivotIn__.setNone()

    # MT_label__
    self.obj46.MT_label__.setValue('14')

    # MT_pre__name
    self.obj46.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj46.MT_pre__name.setHeight(15)

    self.obj46.graphClass_= graph_MT_pre__Woman
    if self.genGraphics:
       new_obj = graph_MT_pre__Woman(560.0,560.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Woman", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=MT_pre__directLink_T(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # MT_label__
    self.obj47.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj47.MT_pivotOut__.setValue('')
    self.obj47.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj47.MT_subtypeMatching__.setValue(('True', 0))
    self.obj47.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj47.MT_pivotIn__.setValue('')
    self.obj47.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj47.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj47.MT_pre__associationType.setHeight(15)

    self.obj47.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(528.0,511.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=MT_pre__directLink_T(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # MT_label__
    self.obj48.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj48.MT_pivotOut__.setValue('')
    self.obj48.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj48.MT_subtypeMatching__.setValue(('True', 0))
    self.obj48.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj48.MT_pivotIn__.setValue('')
    self.obj48.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj48.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj48.MT_pre__associationType.setHeight(15)

    self.obj48.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(528.0,551.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=MT_pre__directLink_T(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # MT_label__
    self.obj49.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj49.MT_pivotOut__.setValue('')
    self.obj49.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj49.MT_subtypeMatching__.setValue(('True', 0))
    self.obj49.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj49.MT_pivotIn__.setValue('')
    self.obj49.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj49.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__associationType.setHeight(15)

    self.obj49.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(608.0,551.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=MT_pre__directLink_T(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # MT_label__
    self.obj50.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj50.MT_pivotOut__.setValue('')
    self.obj50.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj50.MT_subtypeMatching__.setValue(('True', 0))
    self.obj50.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj50.MT_pivotIn__.setValue('')
    self.obj50.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj50.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__associationType.setHeight(15)

    self.obj50.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(668.0,511.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=MT_pre__directLink_S(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # MT_label__
    self.obj51.MT_label__.setValue('6')

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
    self.obj51.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "father"\n')
    self.obj51.MT_pre__associationType.setHeight(15)

    self.obj51.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(670.0,352.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
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
    self.obj52.MT_label__.setValue('7')

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
    self.obj52.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "mother"\n')
    self.obj52.MT_pre__associationType.setHeight(15)

    self.obj52.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(550.0,362.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=MT_pre__directLink_S(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # MT_label__
    self.obj53.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj53.MT_pivotOut__.setValue('')
    self.obj53.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj53.MT_subtypeMatching__.setValue(('True', 0))
    self.obj53.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj53.MT_pivotIn__.setValue('')
    self.obj53.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj53.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "son"\n')
    self.obj53.MT_pre__associationType.setHeight(15)

    self.obj53.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(550.0,432.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=MT_pre__directLink_S(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # MT_label__
    self.obj54.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj54.MT_pivotOut__.setValue('')
    self.obj54.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj54.MT_subtypeMatching__.setValue(('True', 0))
    self.obj54.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj54.MT_pivotIn__.setValue('')
    self.obj54.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj54.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn return attr_value == "daughter"\n')
    self.obj54.MT_pre__associationType.setHeight(15)

    self.obj54.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(680.0,452.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=MT_pre__trace_link(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_label__
    self.obj55.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    self.obj55.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(599.0,441.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj63=MT_pre__trace_link(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # MT_label__
    self.obj63.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj63.MT_pivotOut__.setValue('')
    self.obj63.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj63.MT_pivotIn__.setValue('')
    self.obj63.MT_pivotIn__.setNone()

    self.obj63.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(609.0,411.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj77=MT_pre__trace_link(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_label__
    self.obj77.MT_label__.setValue('21')

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj77.MT_subtypeMatching__.setValue(('True', 0))
    self.obj77.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj77.MT_pivotIn__.setValue('')
    self.obj77.MT_pivotIn__.setNone()

    self.obj77.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(679.0,511.5,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj79=MT_pre__trace_link(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # MT_label__
    self.obj79.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj79.MT_pivotOut__.setValue('')
    self.obj79.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj79.MT_subtypeMatching__.setValue(('True', 0))
    self.obj79.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj79.MT_pivotIn__.setValue('')
    self.obj79.MT_pivotIn__.setNone()

    self.obj79.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(459.0,471.5,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=MT_pre__trace_link(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # MT_label__
    self.obj80.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj80.MT_pivotOut__.setValue('')
    self.obj80.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj80.MT_subtypeMatching__.setValue(('True', 0))
    self.obj80.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj80.MT_pivotIn__.setValue('')
    self.obj80.MT_pivotIn__.setNone()

    self.obj80.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(469.0,451.5,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj56=LHS(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # constraint
    self.obj56.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj56.constraint.setHeight(15)

    self.obj56.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(380.0,240.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    # Connections for obj37 (graphObject_: Obj0) of type MT_pre__Family
    self.drawConnections(
(self.obj37,self.obj51,[600.0, 382.0, 670.0, 352.0],"true", 2),
(self.obj37,self.obj52,[600.0, 382.0, 550.0, 362.0],"true", 2),
(self.obj37,self.obj53,[600.0, 382.0, 550.0, 432.0],"true", 2),
(self.obj37,self.obj54,[600.0, 382.0, 680.0, 452.0],"true", 2) )
    # Connections for obj38 (graphObject_: Obj1) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj39 (graphObject_: Obj2) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj3) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj4) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj5) of type MT_pre__CommunityRoot
    self.drawConnections(
(self.obj42,self.obj47,[598.0, 501.0, 528.0, 511.0],"true", 2),
(self.obj42,self.obj48,[598.0, 501.0, 528.0, 551.0],"true", 2),
(self.obj42,self.obj49,[598.0, 501.0, 608.0, 551.0],"true", 2),
(self.obj42,self.obj50,[598.0, 501.0, 668.0, 511.0],"true", 2),
(self.obj42,self.obj55,[598.0, 501.0, 599.0, 441.5],"true", 2) )
    # Connections for obj43 (graphObject_: Obj6) of type MT_pre__Man
    self.drawConnections(
(self.obj43,self.obj79,[458.0, 521.0, 459.0, 471.5],"true", 2) )
    # Connections for obj44 (graphObject_: Obj7) of type MT_pre__Man
    self.drawConnections(
(self.obj44,self.obj80,[458.0, 601.0, 469.0, 451.5],"true", 2) )
    # Connections for obj45 (graphObject_: Obj8) of type MT_pre__Woman
    self.drawConnections(
(self.obj45,self.obj63,[738.0, 521.0, 609.0, 411.5],"true", 2) )
    # Connections for obj46 (graphObject_: Obj9) of type MT_pre__Woman
    self.drawConnections(
(self.obj46,self.obj77,[618.0, 601.0, 679.0, 511.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj10) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj47,self.obj43,[528.0, 511.0, 458.0, 521.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj11) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj48,self.obj44,[528.0, 551.0, 458.0, 601.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj12) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj49,self.obj46,[608.0, 551.0, 618.0, 601.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj13) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj50,self.obj45,[668.0, 511.0, 738.0, 521.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj14) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj51,self.obj39,[670.0, 352.0, 720.0, 302.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj15) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj52,self.obj38,[550.0, 362.0, 480.0, 302.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj16) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj53,self.obj40,[550.0, 432.0, 460.0, 422.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj17) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj54,self.obj41,[680.0, 452.0, 740.0, 422.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj18) of type MT_pre__trace_link
    self.drawConnections(
(self.obj55,self.obj37,[599.0, 441.5, 600.0, 382.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj20) of type MT_pre__trace_link
    self.drawConnections(
(self.obj63,self.obj38,[609.0, 411.5, 480.0, 302.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj21) of type MT_pre__trace_link
    self.drawConnections(
(self.obj77,self.obj41,[679.0, 511.5, 740.0, 422.0],"true", 2) )
    # Connections for obj79 (graphObject_: Obj23) of type MT_pre__trace_link
    self.drawConnections(
(self.obj79,self.obj40,[459.0, 471.5, 460.0, 422.0],"true", 2) )
    # Connections for obj80 (graphObject_: Obj24) of type MT_pre__trace_link
    self.drawConnections(
(self.obj80,self.obj38,[469.0, 451.5, 480.0, 302.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj19) of type LHS
    self.drawConnections(
 )

newfunction = fourMembers_Complete_MDL

loadedMMName = ['MT_pre__FamiliesToPersonsMM_META', 'MoTifRule_META']

atom3version = '0.3'
