"""
__MT_pre__indirectLink_S.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sun Aug  9 23:45:38 2015
________________________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from graph_MT_pre__indirectLink_S import *
class MT_pre__indirectLink_S(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.superTypes = []
      self.graphClass_ = graph_MT_pre__indirectLink_S
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.MT_label__=ATOM3String('', 20)
      self.MT_pivotOut__=ATOM3String('', 20)
      self.MT_pivotIn__=ATOM3String('', 20)
      self.MT_subtypeMatching__=ATOM3Boolean()
      self.MT_subtypeMatching__.setValue(('True', 0))
      self.MT_subtypeMatching__.config = 0
      self.generatedAttributes = {'MT_label__': ('ATOM3String', ),
                                  'MT_pivotOut__': ('ATOM3String', ),
                                  'MT_pivotIn__': ('ATOM3String', ),
                                  'MT_subtypeMatching__': ('ATOM3Boolean', )      }
      self.realOrder = ['MT_label__','MT_pivotOut__','MT_pivotIn__','MT_subtypeMatching__']
      self.directEditing = [1,1,1,1]
   def clone(self):
      cloneObject = MT_pre__indirectLink_S( self.parent )
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
      if actionID == self.CREATE:
         self.autoIncrLabel(params)
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
      return # <--- Remove this if you want to use QOCA
      
      # Get the high level constraint helper and solver
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      # Constraint only makes sense if there exists 2 objects connected to this link
      if(not (self.in_connections_ and self.out_connections_)): return
      
      # Get the graphical objects (subclass of graphEntity/graphLink) 
      graphicalObjectLink = self.graphObject_
      graphicalObjectSource = self.in_connections_[0].graphObject_
      graphicalObjectTarget = self.out_connections_[0].graphObject_
      objTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.LeftExactDistance(objTuple, 20)
      oc.resolve() # Resolve immediately after creating entity & constraint 
      
      

   def autoIncrLabel(self, params):
      
      #===============================================================================
      # Auto increment the label
      #===============================================================================
      
      # If there is already one, ignore
      if not self.MT_label__.isNone(): return
      
      # Get the maximum label of all MT_pre__ elements
      label = 0
      for nt in self.parent.ASGroot.listNodes:
          if nt.startswith('MT_pre__'):
              for node in self.parent.ASGroot.listNodes[nt]:
                  currLabel = 0
                  try:
                      currLabel = int(node.MT_label__.getValue())
                  except:
                      pass
                  if currLabel > label:
                      label = currLabel
      # The label of this instance will be the max label + 1
      self.MT_label__.setValue(str(label + 1))
      



