"""
__ASG_MT_post__UMLRT2Kiltera_MM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: gehan
Modified: Sun Feb 15 10:31:27 2015
_______________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_MT_post__UMLRT2Kiltera_MM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'MT_post__UMLRT2Kiltera_MM', ASGroot, ['ASG_MT_post__UMLRT2Kiltera_MM' ,'MT_post__MatchModel' ,'MT_post__ApplyModel' ,'MT_post__MetaModelElement_S' ,'MT_post__MetaModelElement_T' ,'MT_post__Element' ,'MT_post__NamedElement' ,'MT_post__Trigger_S' ,'MT_post__Action' ,'MT_post__PortRef' ,'MT_post__PortConnectorRef' ,'MT_post__StateMachineElement' ,'MT_post__Protocol' ,'MT_post__Signal' ,'MT_post__Port' ,'MT_post__Vertex' ,'MT_post__InitialPoint' ,'MT_post__EntryPoint' ,'MT_post__ExitPoint' ,'MT_post__Transition' ,'MT_post__StateMachine' ,'MT_post__State' ,'MT_post__Capsule' ,'MT_post__PackageContainer' ,'MT_post__Model_S' ,'MT_post__Package' ,'MT_post__CapsuleRole' ,'MT_post__PortConnector' ,'MT_post__Thread' ,'MT_post__PhysicalThread' ,'MT_post__LogicalThread' ,'MT_post__PortType' ,'MT_post__BASE0' ,'MT_post__CONJUGATE1' ,'MT_post__SignalType' ,'MT_post__OUT1' ,'MT_post__IN0' ,'MT_post__RoleType' ,'MT_post__FIXED0' ,'MT_post__OPTIONAL1' ,'MT_post__PLUGIN2' ,'MT_post__TransitionType' ,'MT_post__SIBLING0' ,'MT_post__IN1' ,'MT_post__OUT2' ,'MT_post__Def' ,'MT_post__Expr' ,'MT_post__Pattern' ,'MT_post__Proc' ,'MT_post__ProcDef' ,'MT_post__FuncDef' ,'MT_post__Name' ,'MT_post__PythonRef' ,'MT_post__Module' ,'MT_post__Null' ,'MT_post__Trigger_T' ,'MT_post__Listen' ,'MT_post__ConditionBranch' ,'MT_post__ListenBranch' ,'MT_post__Site' ,'MT_post__Model_T' ,'MT_post__MatchCase' ,'MT_post__Condition' ,'MT_post__New' ,'MT_post__Delay' ,'MT_post__Par' ,'MT_post__ParIndexed' ,'MT_post__Inst' ,'MT_post__LocalDef' ,'MT_post__Seq' ,'MT_post__ConditionSet' ,'MT_post__Match' ,'MT_post__Print' ,'MT_post__Attribute' ,'MT_post__Expression' ,'MT_post__Equation' ,'MT_post__Operation' ,'MT_post__Add' ,'MT_post__Subtract' ,'MT_post__Concat' ,'MT_post__Constant' ,'MT_post__GenericNode_UMLRT2Kiltera_MM' ,'MT_post__paired_with' ,'MT_post__match_contains' ,'MT_post__apply_contains' ,'MT_post__directLink_T' ,'MT_post__directLink_S' ,'MT_post__indirectLink_S' ,'MT_post__backward_link' ,'MT_post__trace_link' ,'MT_post__hasAttribute_S' ,'MT_post__hasAttribute_T' ,'MT_post__leftExpr' ,'MT_post__rightExpr' ,'MT_post__hasArgs' ,'MT_post__GenericEdge_UMLRT2Kiltera_MM'])

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
       a = ATOM3(topWindowParent, 'MT_post__UMLRT2Kiltera_MM', 0, 1, self)
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


