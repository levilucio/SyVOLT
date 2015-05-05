"""
__ASG_MT_post__ECoreMM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Tue May  5 12:32:20 2015
______________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_MT_post__ECoreMM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'MT_post__ECoreMM', ASGroot, ['ASG_MT_post__ECoreMM' ,'MT_post__MetaModelElement_S' ,'MT_post__EClass' ,'MT_post__EReference' ,'MT_post__EStructuralFeature' ,'MT_post__MatchModel' ,'MT_post__ApplyModel' ,'MT_post__MetaModelElement_T' ,'MT_post__Attribute' ,'MT_post__Equation' ,'MT_post__Expression' ,'MT_post__Constant' ,'MT_post__Concat' ,'MT_post__GenericNode_ECoreMM' ,'MT_post__match_contains' ,'MT_post__apply_contains' ,'MT_post__backward_link' ,'MT_post__indirectLink_S' ,'MT_post__directLink_T' ,'MT_post__directLink_S' ,'MT_post__paired_with' ,'MT_post__trace_link' ,'MT_post__hasAttr_S' ,'MT_post__hasAttr_T' ,'MT_post__leftExpr' ,'MT_post__rightExpr' ,'MT_post__arg_1' ,'MT_post__arg_2' ,'MT_post__GenericEdge_ECoreMM'])

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
       a = ATOM3(topWindowParent, 'MT_post__ECoreMM', 0, 1, self)
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


