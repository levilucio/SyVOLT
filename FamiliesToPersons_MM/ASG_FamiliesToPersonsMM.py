"""
__ASG_FamiliesToPersonsMM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Apr 17 14:22:16 2015
_________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_FamiliesToPersonsMM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'FamiliesToPersonsMM', ASGroot, ['ASG_FamiliesToPersonsMM' ,'MetaModelElement_S' ,'HouseholdRoot' ,'Family' ,'Member' ,'MatchModel' ,'ApplyModel' ,'MetaModelElement_T' ,'CommunityRoot' ,'Person' ,'Man' ,'Attribute' ,'Equation' ,'Expression' ,'Constant' ,'Concat' ,'Woman' ,'match_contains' ,'apply_contains' ,'backward_link' ,'indirectLink_S' ,'directLink_T' ,'directLink_S' ,'paired_with' ,'trace_link' ,'hasAttr_S' ,'hasAttr_T' ,'leftExpr' ,'rightExpr' ,'arg_1' ,'arg_2'])

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
       a = ATOM3(topWindowParent, 'FamiliesToPersonsMM', 0, 1, self)
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


