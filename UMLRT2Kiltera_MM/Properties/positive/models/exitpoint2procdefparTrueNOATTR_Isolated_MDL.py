"""
__exitpoint2procdefparTrueNOATTR_Isolated_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Feb 16 14:14:34 2015
_____________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__ExitPoint import *
from MT_pre__State import *
from LHS import *
from graph_MT_pre__State import *
from graph_MT_pre__ExitPoint import *
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

def exitpoint2procdefparTrueNOATTR_Isolated_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('exitpoint2procdefparTrueNOATTR_Isolated')
    # --- ASG attributes over ---


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


    self.obj126=MT_pre__ExitPoint(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj126.MT_pivotOut__.setValue('')
    self.obj126.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj126.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj126.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj126.MT_pivotIn__.setValue('')
    self.obj126.MT_pivotIn__.setNone()

    # MT_label__
    self.obj126.MT_label__.setValue('12')

    # MT_pre__cardinality
    self.obj126.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj126.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__name.setHeight(15)

    self.obj126.graphClass_= graph_MT_pre__ExitPoint
    if self.genGraphics:
       new_obj = graph_MT_pre__ExitPoint(300.0,240.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj121=MT_pre__State(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj121.MT_pivotOut__.setValue('')
    self.obj121.MT_pivotOut__.setNone()

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
    self.obj121.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj121.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj121.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__name.setHeight(15)

    self.obj121.graphClass_= graph_MT_pre__State
    if self.genGraphics:
       new_obj = graph_MT_pre__State(80.0,300.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj120=LHS(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # constraint
    self.obj120.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj120.constraint.setHeight(15)

    self.obj120.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(60.0,60.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    # Connections for obj126 (graphObject_: Obj6) of type MT_pre__ExitPoint
    self.drawConnections(
 )
    # Connections for obj121 (graphObject_: Obj1) of type MT_pre__State
    self.drawConnections(
 )
    # Connections for obj120 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = exitpoint2procdefparTrueNOATTR_Isolated_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
