"""
__ASG_MT_pre__UMLRT2Kiltera_MM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: gehan
Modified: Sun Feb 15 10:22:15 2015
______________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_MT_pre__UMLRT2Kiltera_MM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'MT_pre__UMLRT2Kiltera_MM', ASGroot, ['ASG_MT_pre__UMLRT2Kiltera_MM' ,'MT_pre__MatchModel' ,'MT_pre__ApplyModel' ,'MT_pre__MetaModelElement_S' ,'MT_pre__MetaModelElement_T' ,'MT_pre__Element' ,'MT_pre__NamedElement' ,'MT_pre__Trigger_S' ,'MT_pre__Action' ,'MT_pre__PortRef' ,'MT_pre__PortConnectorRef' ,'MT_pre__StateMachineElement' ,'MT_pre__Protocol' ,'MT_pre__Signal' ,'MT_pre__Port' ,'MT_pre__Vertex' ,'MT_pre__InitialPoint' ,'MT_pre__EntryPoint' ,'MT_pre__ExitPoint' ,'MT_pre__Transition' ,'MT_pre__StateMachine' ,'MT_pre__State' ,'MT_pre__Capsule' ,'MT_pre__PackageContainer' ,'MT_pre__Model_S' ,'MT_pre__Package' ,'MT_pre__CapsuleRole' ,'MT_pre__PortConnector' ,'MT_pre__Thread' ,'MT_pre__PhysicalThread' ,'MT_pre__LogicalThread' ,'MT_pre__PortType' ,'MT_pre__BASE0' ,'MT_pre__CONJUGATE1' ,'MT_pre__SignalType' ,'MT_pre__OUT1' ,'MT_pre__IN0' ,'MT_pre__RoleType' ,'MT_pre__FIXED0' ,'MT_pre__OPTIONAL1' ,'MT_pre__PLUGIN2' ,'MT_pre__TransitionType' ,'MT_pre__SIBLING0' ,'MT_pre__IN1' ,'MT_pre__OUT2' ,'MT_pre__Def' ,'MT_pre__Expr' ,'MT_pre__Pattern' ,'MT_pre__Proc' ,'MT_pre__ProcDef' ,'MT_pre__FuncDef' ,'MT_pre__Name' ,'MT_pre__PythonRef' ,'MT_pre__Module' ,'MT_pre__Null' ,'MT_pre__Trigger_T' ,'MT_pre__Listen' ,'MT_pre__ConditionBranch' ,'MT_pre__ListenBranch' ,'MT_pre__Site' ,'MT_pre__Model_T' ,'MT_pre__MatchCase' ,'MT_pre__Condition' ,'MT_pre__New' ,'MT_pre__Delay' ,'MT_pre__Par' ,'MT_pre__ParIndexed' ,'MT_pre__Inst' ,'MT_pre__LocalDef' ,'MT_pre__Seq' ,'MT_pre__ConditionSet' ,'MT_pre__Match' ,'MT_pre__Print' ,'MT_pre__Attribute' ,'MT_pre__Expression' ,'MT_pre__Equation' ,'MT_pre__Operation' ,'MT_pre__Add' ,'MT_pre__Subtract' ,'MT_pre__Concat' ,'MT_pre__Constant' ,'MT_pre__GenericNode_UMLRT2Kiltera_MM' ,'MT_pre__paired_with' ,'MT_pre__match_contains' ,'MT_pre__apply_contains' ,'MT_pre__directLink_T' ,'MT_pre__directLink_S' ,'MT_pre__indirectLink_S' ,'MT_pre__backward_link' ,'MT_pre__trace_link' ,'MT_pre__hasAttribute_S' ,'MT_pre__hasAttribute_T' ,'MT_pre__leftExpr' ,'MT_pre__rightExpr' ,'MT_pre__hasArgs' ,'MT_pre__GenericEdge_UMLRT2Kiltera_MM'])

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
       a = ATOM3(topWindowParent, 'MT_pre__UMLRT2Kiltera_MM', 0, 1, self)
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


