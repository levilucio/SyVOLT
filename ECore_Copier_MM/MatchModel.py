"""
__MatchModel.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Tue May  5 12:27:39 2015
____________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from graph_MatchModel import *
class MatchModel(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.superTypes = []
      self.graphClass_ = graph_MatchModel
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.generatedAttributes = {      }
      self.realOrder = []
      self.directEditing = []
   def clone(self):
      cloneObject = MatchModel( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def QOCA(self, params):
      """
      QOCA Constraint Template
      NOTE: DO NOT select a POST/PRE action trigger
      Constraints will be added/removed in a logical manner by other mechanisms.
      """
      return # <---- Remove this to use QOCA
      
      """ Get the high level constraint helper and solver """
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)
      oc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)
      
      


