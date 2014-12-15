"""
__ASG_MT_pre__.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Jan 25 15:24:48 2013
______________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_MT_pre__(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'MT_pre__', ASGroot, ['ASG_MT_pre__' ,'MT_pre__MetaModelElement_S' ,'MT_pre__Station_S' ,'MT_pre__Male_S' ,'MT_pre__Female_S' ,'MT_pre__MatchModel' ,'MT_pre__ApplyModel' ,'MT_pre__MetaModelElement_T' ,'MT_pre__Station_T' ,'MT_pre__Male_T' ,'MT_pre__Female_T' ,'MT_pre__GenericNode_' ,'MT_pre__match_contains' ,'MT_pre__apply_contains' ,'MT_pre__backward_link' ,'MT_pre__indirectLink_S' ,'MT_pre__directLink_T' ,'MT_pre__directLink_S' ,'MT_pre__GenericEdge_'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.name=ATOM3String('', 20)
      self.keyword_= self.name
      self.author=ATOM3String('Annonymous', 20)
      self.description=ATOM3Text('\n', 60,15 )
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'author': ('ATOM3String', ),
                                  'description': ('ATOM3Text', )      }
      self.realOrder = ['name','author','description']
      self.directEditing = [1,1,1]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'MT_pre__', 0, 1, self)
       #self.writeContents(a)
       return a
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


