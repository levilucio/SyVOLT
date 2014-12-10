"""
__M2ThenClausePart1IsolatedConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Fri Oct 18 20:45:26 2013
________________________________________________________________________________________________
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

def M2ThenClausePart1IsolatedConnected_MDL(self, rootNode, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('M2ThenClausePart1IsolatedConnected')
    # --- ASG attributes over ---


    self.obj17960=LHS(self)
    self.obj17960.isGraphObjectVisual = True

    if(hasattr(self.obj17960, '_setHierarchicalLink')):
      self.obj17960._setHierarchicalLink(False)

    # constraint
    self.obj17960.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj17960.constraint.setHeight(15)

    self.obj17960.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(160.0,100.0,self.obj17960)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj17960.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj17960)
    self.globalAndLocalPostcondition(self.obj17960, rootNode)
    self.obj17960.postAction( rootNode.CREATE )

    # Connections for obj17960 (graphObject_: Obj44) of type LHS
    self.drawConnections(
 )

newfunction = M2ThenClausePart1IsolatedConnected_MDL

loadedMMName = 'MoTifRule_META'

atom3version = '0.3'
