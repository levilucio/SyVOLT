"""
__Capsule.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sun Jan 11 16:47:15 2015
_________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_Capsule import *
class Capsule(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.superTypes = ['NamedElement', 'MetaModelElement_S']
      self.graphClass_ = graph_Capsule
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.cardinality=ATOM3String('1', 20)
      self.cardinality=ATOM3String('1', 20)
      self.cardinality=ATOM3String('1', 20)
      self.classtype=ATOM3String('t_', 20)
      self.classtype=ATOM3String('t_', 20)
      self.classtype=ATOM3String('t_', 20)
      self.name=ATOM3String('s_', 20)
      self.name=ATOM3String('s_', 20)
      self.name=ATOM3String('s_', 20)
      self.generatedAttributes = {'cardinality': ('ATOM3String', ),
                                  'cardinality': ('ATOM3String', ),
                                  'cardinality': ('ATOM3String', ),
                                  'classtype': ('ATOM3String', ),
                                  'classtype': ('ATOM3String', ),
                                  'classtype': ('ATOM3String', ),
                                  'name': ('ATOM3String', ),
                                  'name': ('ATOM3String', ),
                                  'name': ('ATOM3String', )      }
      self.realOrder = ['cardinality','cardinality','cardinality','classtype','classtype','classtype','name','name','name']
      self.directEditing = [1,1,1,1,1,1,1,1,1]
   def clone(self):
      cloneObject = Capsule( self.parent )
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
      
      



