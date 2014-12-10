"""
__M4IfClauseIsolatedConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 23 16:58:03 2013
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from LHS import *
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

def M4IfClauseIsolatedConnected_MDL(self, rootNode, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('M4IfClauseIsolatedConnected')
    # --- ASG attributes over ---


    self.obj16665=LHS(self)
    self.obj16665.isGraphObjectVisual = True

    if(hasattr(self.obj16665, '_setHierarchicalLink')):
      self.obj16665._setHierarchicalLink(False)

    # constraint
    self.obj16665.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj16665.constraint.setHeight(15)

    self.obj16665.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(120.0,120.0,self.obj16665)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj16665.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj16665)
    self.globalAndLocalPostcondition(self.obj16665, rootNode)
    self.obj16665.postAction( rootNode.CREATE )

    # Connections for obj16665 (graphObject_: Obj89) of type LHS
    self.drawConnections(
 )

newfunction = M4IfClauseIsolatedConnected_MDL

loadedMMName = 'MoTifRule_META'

atom3version = '0.3'
