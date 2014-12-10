"""
__MT_post__EcuInstance.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sat Aug 24 20:17:54 2013
______________________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3Text import *
from ATOM3String import *
from graph_MT_post__EcuInstance import *
class MT_post__EcuInstance(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.superTypes = ['MT_post__MetaModelElement_T']
      self.graphClass_ = graph_MT_post__EcuInstance
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.MT_post__cardinality=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
      self.MT_post__classtype=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
      self.MT_post__name=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
      self.MT_label__=ATOM3String('', 20)
      self.MT_pivotOut__=ATOM3String('', 20)
      self.generatedAttributes = {'MT_post__cardinality': ('ATOM3Text', ),
                                  'MT_post__classtype': ('ATOM3Text', ),
                                  'MT_post__name': ('ATOM3Text', ),
                                  'MT_label__': ('ATOM3String', ),
                                  'MT_pivotOut__': ('ATOM3String', )      }
      self.realOrder = ['MT_post__cardinality','MT_post__classtype','MT_post__name','MT_label__','MT_pivotOut__']
      self.directEditing = [0,0,0,1,1]
   def clone(self):
      cloneObject = MT_post__EcuInstance( self.parent )
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
      
      

   def autoIncrLabel(self, params):
      
      #===============================================================================
      # Auto increment the label
      #===============================================================================
      
      # If there is already one, ignore
      if not self.MT_label__.isNone(): return
      
      # Get the maximum label of all MT_pre__ elements
      label = 0
      for nt in self.parent.ASGroot.listNodes:
          if nt.startswith('MT_post__'):
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
      



