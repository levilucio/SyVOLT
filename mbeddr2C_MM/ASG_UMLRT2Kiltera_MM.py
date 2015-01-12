"""
__ASG_UMLRT2Kiltera_MM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sun Jan 11 16:43:16 2015
______________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_UMLRT2Kiltera_MM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'UMLRT2Kiltera_MM', ASGroot, ['ASG_UMLRT2Kiltera_MM' ,'MatchModel' ,'ApplyModel' ,'MetaModelElement_S' ,'MetaModelElement_T' ,'Element' ,'NamedElement' ,'ImplementationModule_S' ,'Function' ,'PortRef' ,'Int32Type' ,'StateMachineElement' ,'Protocol' ,'Signal' ,'Port' ,'Vertex' ,'InitialPoint' ,'EntryPoint' ,'ExitPoint' ,'Transition' ,'StateMachine' ,'State' ,'Capsule' ,'PackageContainer' ,'Model_S' ,'Package' ,'CapsuleRole' ,'PortConnector' ,'Thread' ,'PhysicalThread' ,'LogicalThread' ,'PortType' ,'BASE0' ,'CONJUGATE1' ,'SignalType' ,'OUT1' ,'IN0' ,'RoleType' ,'FIXED0' ,'OPTIONAL1' ,'PLUGIN2' ,'TransitionType' ,'SIBLING0' ,'IN1' ,'OUT2' ,'Def' ,'ImplementationModule_T' ,'VoidType' ,'Proc' ,'ProcDef' ,'FuncDef' ,'FunctionPrototype' ,'PythonRef' ,'Module' ,'Null' ,'Trigger_T' ,'Listen' ,'ConditionBranch' ,'ListenBranch' ,'Site' ,'Model_T' ,'MatchCase' ,'Condition' ,'New' ,'Delay' ,'Par' ,'ParIndexed' ,'Inst' ,'LocalDef' ,'Seq' ,'ConditionSet' ,'Match' ,'Print' ,'Attribute' ,'Expression' ,'Equation' ,'Operation' ,'Add' ,'Subtract' ,'Concat' ,'Constant' ,'paired_with' ,'match_contains' ,'apply_contains' ,'directLink_T' ,'directLink_S' ,'indirectLink_S' ,'backward_link' ,'trace_link' ,'hasAttribute_S' ,'hasAttribute_T' ,'leftExpr' ,'rightExpr' ,'hasArgs'])

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
       a = ATOM3(topWindowParent, 'UMLRT2Kiltera_MM', 0, 1, self)
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


