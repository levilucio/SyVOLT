"""
__check_for_no_backward_links_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Jan 23 12:40:18 2014
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MetaModelElement_S import *
from LHS import *
from graph_MT_pre__MetaModelElement_S import *
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

def check_for_no_backward_links_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('CheckForNoBackwardLinks')
    # --- ASG attributes over ---


    self.obj75=MT_pre__MetaModelElement_S(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj75.MT_subtypeMatching__.setValue(('True', 1))
    self.obj75.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj75.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj75.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj75.MT_pivotIn__.setValue('')
    self.obj75.MT_pivotIn__.setNone()

    # MT_label__
    self.obj75.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj75.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj75.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj75.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj75.MT_pre__name.setHeight(15)

    self.obj75.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(263.0,226.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj77=LHS(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # constraint
    self.obj77.constraint.setValue('if len([i for i in graph.neighbors(PreNode(\'1\').index) if graph.vs[i][\'mm__\'] == \'backward_link\']) == 0:\n    return True\n\nreturn False\n')
    self.obj77.constraint.setHeight(15)

    self.obj77.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(140.0,100.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    # Connections for obj75 (graphObject_: Obj4) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj77 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )

newfunction = check_for_no_backward_links_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
