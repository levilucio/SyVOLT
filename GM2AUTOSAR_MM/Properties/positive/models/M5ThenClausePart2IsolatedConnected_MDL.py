"""
__M5ThenClausePart2IsolatedConnected_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Thu Oct 24 13:43:45 2013
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

def M5ThenClausePart2IsolatedConnected_MDL(self, rootNode, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('M5ThenClausePart2IsolatedConnected')
    # --- ASG attributes over ---


    self.obj3020=LHS(self)
    self.obj3020.isGraphObjectVisual = True

    if(hasattr(self.obj3020, '_setHierarchicalLink')):
      self.obj3020._setHierarchicalLink(False)

    # constraint
    self.obj3020.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj3020.constraint.setHeight(15)

    self.obj3020.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(100.0,60.0,self.obj3020)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj3020.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj3020)
    self.globalAndLocalPostcondition(self.obj3020, rootNode)
    self.obj3020.postAction( rootNode.CREATE )

    # Connections for obj3020 (graphObject_: Obj2) of type LHS
    self.drawConnections(
 )

newfunction = M5ThenClausePart2IsolatedConnected_MDL

loadedMMName = 'MoTifRule_META'

atom3version = '0.3'
