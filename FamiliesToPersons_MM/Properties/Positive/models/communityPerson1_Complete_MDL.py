"""
__communityPerson1_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Apr 17 13:52:25 2015
_______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__CommunityRoot import *
from MT_pre__Person import *
from MT_pre__directLink_T import *
from LHS import *
from graph_MT_pre__CommunityRoot import *
from graph_MT_pre__Person import *
from graph_MT_pre__directLink_T import *
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

def communityPerson1_Complete_MDL(self, rootNode, MT_pre__FamiliesToPersonsMMRootNode=None, MoTifRuleRootNode=None):

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
        MoTifRuleRootNode.name.setValue('communityPerson1_Complete')
    # --- ASG attributes over ---


    self.obj43=MT_pre__CommunityRoot(self)
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
    self.obj43.MT_label__.setValue('1')

    # MT_pre__name
    self.obj43.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj43.MT_pre__name.setHeight(15)

    self.obj43.graphClass_= graph_MT_pre__CommunityRoot
    if self.genGraphics:
       new_obj = graph_MT_pre__CommunityRoot(240.0,340.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CommunityRoot", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=MT_pre__Person(self)
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
    self.obj44.MT_label__.setValue('2')

    # MT_pre__name
    self.obj44.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj44.MT_pre__name.setHeight(15)

    self.obj44.graphClass_= graph_MT_pre__Person
    if self.genGraphics:
       new_obj = graph_MT_pre__Person(440.0,340.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Person", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=MT_pre__directLink_T(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # MT_label__
    self.obj45.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj45.MT_pivotOut__.setValue('')
    self.obj45.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj45.MT_subtypeMatching__.setValue(('True', 0))
    self.obj45.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj45.MT_pivotIn__.setValue('')
    self.obj45.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj45.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj45.MT_pre__associationType.setHeight(15)

    self.obj45.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(398.0,381.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj42=LHS(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # constraint
    self.obj42.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj42.constraint.setHeight(15)

    self.obj42.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(180.0,180.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    # Connections for obj43 (graphObject_: Obj6) of type MT_pre__CommunityRoot
    self.drawConnections(
(self.obj43,self.obj45,[298.0, 381.0, 398.0, 381.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj7) of type MT_pre__Person
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj8) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj45,self.obj44,[398.0, 381.0, 498.0, 381.0],"true", 2) )
    # Connections for obj42 (graphObject_: Obj5) of type LHS
    self.drawConnections(
 )

newfunction = communityPerson1_Complete_MDL

loadedMMName = ['MT_pre__FamiliesToPersonsMM_META', 'MoTifRule_META']

atom3version = '0.3'
