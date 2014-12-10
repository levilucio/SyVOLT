"""
__ASG_MT_pre__GM2AUTOSAR_MM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sat Aug 24 20:17:20 2013
___________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_MT_pre__GM2AUTOSAR_MM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'MT_pre__GM2AUTOSAR_MM', ASGroot, ['ASG_MT_pre__GM2AUTOSAR_MM' ,'MT_pre__MatchModel' ,'MT_pre__ApplyModel' ,'MT_pre__MetaModelElement_S' ,'MT_pre__MetaModelElement_T' ,'MT_pre__ECU' ,'MT_pre__VirtualDevice' ,'MT_pre__Distributable' ,'MT_pre__ExecFrame' ,'MT_pre__Signal' ,'MT_pre__System' ,'MT_pre__SystemMapping' ,'MT_pre__SoftwareComposition' ,'MT_pre__CompositionType' ,'MT_pre__ComponentPrototype' ,'MT_pre__PPortPrototype' ,'MT_pre__RPortPrototype' ,'MT_pre__EcuInstance' ,'MT_pre__SwcToEcuMapping' ,'MT_pre__SwCompToEcuMapping_component' ,'MT_pre__PortPrototype' ,'MT_pre__ComponentType' ,'MT_pre__GenericNode_GM2AUTOSAR_MM' ,'MT_pre__paired_with' ,'MT_pre__match_contains' ,'MT_pre__directLink_S' ,'MT_pre__directLink_T' ,'MT_pre__apply_contains' ,'MT_pre__indirectLink_S' ,'MT_pre__backward_link' ,'MT_pre__trace_link' ,'MT_pre__GenericEdge_GM2AUTOSAR_MM'])

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
       a = ATOM3(topWindowParent, 'MT_pre__GM2AUTOSAR_MM', 0, 1, self)
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


