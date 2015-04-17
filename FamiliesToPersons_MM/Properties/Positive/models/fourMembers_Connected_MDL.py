"""
__fourMembers_Connected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Apr 17 11:35:05 2015
___________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Family import *
from MT_pre__Member import *
from MT_pre__directLink_S import *
from LHS import *
from graph_MT_pre__Family import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__Member import *
from graph_LHS import *
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

def fourMembers_Connected_MDL(self, rootNode, MT_pre__FamiliesToPersonsMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('fourMembers_Connected')
    # --- ASG attributes over ---


    self.obj52=MT_pre__Family(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52.MT_pivotOut__.setValue('')
    self.obj52.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52.MT_pivotIn__.setValue('')
    self.obj52.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj52.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj52.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__name.setHeight(15)

    self.obj52.graphClass_= graph_MT_pre__Family
    if self.genGraphics:
       new_obj = graph_MT_pre__Family(560.0,360.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Family", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=MT_pre__Member(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj53.MT_pivotOut__.setValue('')
    self.obj53.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj53.MT_subtypeMatching__.setValue(('True', 0))
    self.obj53.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj53.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj53.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj53.MT_pivotIn__.setValue('')
    self.obj53.MT_pivotIn__.setNone()

    # MT_label__
    self.obj53.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj53.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj53.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj53.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj53.MT_pre__name.setHeight(15)

    self.obj53.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(420.0,280.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=MT_pre__Member(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj54.MT_pivotOut__.setValue('')
    self.obj54.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj54.MT_subtypeMatching__.setValue(('True', 0))
    self.obj54.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj54.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj54.MT_pivotIn__.setValue('')
    self.obj54.MT_pivotIn__.setNone()

    # MT_label__
    self.obj54.MT_label__.setValue('3')

    # MT_pre__cardinality
    self.obj54.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj54.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj54.MT_pre__name.setHeight(15)

    self.obj54.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(660.0,260.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=MT_pre__Member(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj55.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    # MT_label__
    self.obj55.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj55.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj55.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj55.MT_pre__name.setHeight(15)

    self.obj55.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(420.0,420.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=MT_pre__Member(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj56.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    # MT_label__
    self.obj56.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj56.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj56.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj56.MT_pre__name.setHeight(15)

    self.obj56.graphClass_= graph_MT_pre__Member
    if self.genGraphics:
       new_obj = graph_MT_pre__Member(680.0,460.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj2614=MT_pre__directLink_S(self)
    self.obj2614.isGraphObjectVisual = True

    if(hasattr(self.obj2614, '_setHierarchicalLink')):
      self.obj2614._setHierarchicalLink(False)

    # MT_label__
    self.obj2614.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj2614.MT_pivotOut__.setValue('')
    self.obj2614.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2614.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2614.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2614.MT_pivotIn__.setValue('')
    self.obj2614.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2614.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "father"\n')
    self.obj2614.MT_pre__associationType.setHeight(15)

    self.obj2614.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(670.0,352.0,self.obj2614)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2614.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2614)
    self.globalAndLocalPostcondition(self.obj2614, rootNode)
    self.obj2614.postAction( rootNode.CREATE )

    self.obj2615=MT_pre__directLink_S(self)
    self.obj2615.isGraphObjectVisual = True

    if(hasattr(self.obj2615, '_setHierarchicalLink')):
      self.obj2615._setHierarchicalLink(False)

    # MT_label__
    self.obj2615.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj2615.MT_pivotOut__.setValue('')
    self.obj2615.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2615.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2615.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2615.MT_pivotIn__.setValue('')
    self.obj2615.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2615.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "mother"\n')
    self.obj2615.MT_pre__associationType.setHeight(15)

    self.obj2615.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(550.0,362.0,self.obj2615)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2615.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2615)
    self.globalAndLocalPostcondition(self.obj2615, rootNode)
    self.obj2615.postAction( rootNode.CREATE )

    self.obj2616=MT_pre__directLink_S(self)
    self.obj2616.isGraphObjectVisual = True

    if(hasattr(self.obj2616, '_setHierarchicalLink')):
      self.obj2616._setHierarchicalLink(False)

    # MT_label__
    self.obj2616.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj2616.MT_pivotOut__.setValue('')
    self.obj2616.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2616.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2616.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2616.MT_pivotIn__.setValue('')
    self.obj2616.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2616.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn attr_value == "son"\n')
    self.obj2616.MT_pre__associationType.setHeight(15)

    self.obj2616.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(550.0,432.0,self.obj2616)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2616.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2616)
    self.globalAndLocalPostcondition(self.obj2616, rootNode)
    self.obj2616.postAction( rootNode.CREATE )

    self.obj2617=MT_pre__directLink_S(self)
    self.obj2617.isGraphObjectVisual = True

    if(hasattr(self.obj2617, '_setHierarchicalLink')):
      self.obj2617._setHierarchicalLink(False)

    # MT_label__
    self.obj2617.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj2617.MT_pivotOut__.setValue('')
    self.obj2617.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj2617.MT_subtypeMatching__.setValue(('True', 0))
    self.obj2617.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj2617.MT_pivotIn__.setValue('')
    self.obj2617.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj2617.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn return attr_value == "daughter"\n')
    self.obj2617.MT_pre__associationType.setHeight(15)

    self.obj2617.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(680.0,452.0,self.obj2617)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj2617.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj2617)
    self.globalAndLocalPostcondition(self.obj2617, rootNode)
    self.obj2617.postAction( rootNode.CREATE )

    self.obj51=LHS(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # constraint
    self.obj51.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj51.constraint.setHeight(15)

    self.obj51.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(380.0,240.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    # Connections for obj52 (graphObject_: Obj1) of type MT_pre__Family
    self.drawConnections(
(self.obj52,self.obj2614,[620.0, 402.0, 670.0, 352.0],"true", 2),
(self.obj52,self.obj2615,[620.0, 402.0, 550.0, 362.0],"true", 2),
(self.obj52,self.obj2616,[620.0, 402.0, 550.0, 432.0],"true", 2),
(self.obj52,self.obj2617,[620.0, 402.0, 680.0, 452.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj2) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj54 (graphObject_: Obj3) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj4) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj5) of type MT_pre__Member
    self.drawConnections(
 )
    # Connections for obj2614 (graphObject_: Obj6) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj2614,self.obj54,[670.0, 352.0, 720.0, 302.0],"true", 2) )
    # Connections for obj2615 (graphObject_: Obj7) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj2615,self.obj53,[550.0, 362.0, 480.0, 322.0],"true", 2) )
    # Connections for obj2616 (graphObject_: Obj8) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj2616,self.obj55,[550.0, 432.0, 480.0, 462.0],"true", 2) )
    # Connections for obj2617 (graphObject_: Obj9) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj2617,self.obj56,[680.0, 452.0, 740.0, 502.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = fourMembers_Connected_MDL

loadedMMName = ['MT_pre__FamiliesToPersonsMM_META', 'MoTifRule_META']

atom3version = '0.3'
