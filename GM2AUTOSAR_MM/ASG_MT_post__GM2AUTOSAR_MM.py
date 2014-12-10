"""
__ASG_MT_post__GM2AUTOSAR_MM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sat Aug 24 20:17:54 2013
____________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_MT_post__GM2AUTOSAR_MM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'MT_post__GM2AUTOSAR_MM', ASGroot, ['ASG_MT_post__GM2AUTOSAR_MM' ,'MT_post__MatchModel' ,'MT_post__ApplyModel' ,'MT_post__MetaModelElement_S' ,'MT_post__MetaModelElement_T' ,'MT_post__ECU' ,'MT_post__VirtualDevice' ,'MT_post__Distributable' ,'MT_post__ExecFrame' ,'MT_post__Signal' ,'MT_post__System' ,'MT_post__SystemMapping' ,'MT_post__SoftwareComposition' ,'MT_post__CompositionType' ,'MT_post__ComponentPrototype' ,'MT_post__PPortPrototype' ,'MT_post__RPortPrototype' ,'MT_post__EcuInstance' ,'MT_post__SwcToEcuMapping' ,'MT_post__SwCompToEcuMapping_component' ,'MT_post__PortPrototype' ,'MT_post__ComponentType' ,'MT_post__GenericNode_GM2AUTOSAR_MM' ,'MT_post__paired_with' ,'MT_post__match_contains' ,'MT_post__directLink_S' ,'MT_post__directLink_T' ,'MT_post__apply_contains' ,'MT_post__indirectLink_S' ,'MT_post__backward_link' ,'MT_post__trace_link' ,'MT_post__GenericEdge_GM2AUTOSAR_MM'])

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
       a = ATOM3(topWindowParent, 'MT_post__GM2AUTOSAR_MM', 0, 1, self)
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


