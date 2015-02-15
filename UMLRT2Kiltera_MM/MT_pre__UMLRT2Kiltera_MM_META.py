"""
__MT_pre__UMLRT2Kiltera_MM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: gehan
Modified: Sun Feb 15 10:28:19 2015
_______________________________________________________________________________________
"""
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3Action import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *
def MT_pre__UMLRT2Kiltera_MM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_pre__UMLRT2Kiltera_MM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_pre__UMLRT2Kiltera_MM_MM.py' )
   self.globalPrecondition(rootNode)

   self.objMT_pre__MatchModel=ButtonConfig(self)
   self.objMT_pre__MatchModel.Contents.Text.setValue('New MatchModel')
   self.objMT_pre__MatchModel.Contents.Image.setValue('')
   self.objMT_pre__MatchModel.Contents.lastSelected= 'Text'
   self.objMT_pre__MatchModel.Drawing_Mode.setValue(1)
   self.objMT_pre__MatchModel.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__MatchModel (self, wherex, wherey)\n'))
   self.objMT_pre__MatchModel.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__MatchModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__MatchModel.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__MatchModel)
   self.globalAndLocalPostcondition(self.objMT_pre__MatchModel, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ApplyModel=ButtonConfig(self)
   self.objMT_pre__ApplyModel.Contents.Text.setValue('New ApplyModel')
   self.objMT_pre__ApplyModel.Contents.Image.setValue('')
   self.objMT_pre__ApplyModel.Contents.lastSelected= 'Text'
   self.objMT_pre__ApplyModel.Drawing_Mode.setValue(1)
   self.objMT_pre__ApplyModel.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ApplyModel (self, wherex, wherey)\n'))
   self.objMT_pre__ApplyModel.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__ApplyModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ApplyModel.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ApplyModel)
   self.globalAndLocalPostcondition(self.objMT_pre__ApplyModel, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__MetaModelElement_S=ButtonConfig(self)
   self.objMT_pre__MetaModelElement_S.Contents.Text.setValue('New MetaModelElement_S')
   self.objMT_pre__MetaModelElement_S.Contents.Image.setValue('')
   self.objMT_pre__MetaModelElement_S.Contents.lastSelected= 'Text'
   self.objMT_pre__MetaModelElement_S.Drawing_Mode.setValue(1)
   self.objMT_pre__MetaModelElement_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__MetaModelElement_S (self, wherex, wherey)\n'))
   self.objMT_pre__MetaModelElement_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__MetaModelElement_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__MetaModelElement_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__MetaModelElement_S)
   self.globalAndLocalPostcondition(self.objMT_pre__MetaModelElement_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__MetaModelElement_T=ButtonConfig(self)
   self.objMT_pre__MetaModelElement_T.Contents.Text.setValue('New MetaModelElement_T')
   self.objMT_pre__MetaModelElement_T.Contents.Image.setValue('')
   self.objMT_pre__MetaModelElement_T.Contents.lastSelected= 'Text'
   self.objMT_pre__MetaModelElement_T.Drawing_Mode.setValue(1)
   self.objMT_pre__MetaModelElement_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__MetaModelElement_T (self, wherex, wherey)\n'))
   self.objMT_pre__MetaModelElement_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__MetaModelElement_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__MetaModelElement_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__MetaModelElement_T)
   self.globalAndLocalPostcondition(self.objMT_pre__MetaModelElement_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Element=ButtonConfig(self)
   self.objMT_pre__Element.Contents.Text.setValue('New Element')
   self.objMT_pre__Element.Contents.Image.setValue('')
   self.objMT_pre__Element.Contents.lastSelected= 'Text'
   self.objMT_pre__Element.Drawing_Mode.setValue(1)
   self.objMT_pre__Element.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Element (self, wherex, wherey)\n'))
   self.objMT_pre__Element.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Element)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Element.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Element)
   self.globalAndLocalPostcondition(self.objMT_pre__Element, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__NamedElement=ButtonConfig(self)
   self.objMT_pre__NamedElement.Contents.Text.setValue('New NamedElement')
   self.objMT_pre__NamedElement.Contents.Image.setValue('')
   self.objMT_pre__NamedElement.Contents.lastSelected= 'Text'
   self.objMT_pre__NamedElement.Drawing_Mode.setValue(1)
   self.objMT_pre__NamedElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__NamedElement (self, wherex, wherey)\n'))
   self.objMT_pre__NamedElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__NamedElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__NamedElement.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__NamedElement)
   self.globalAndLocalPostcondition(self.objMT_pre__NamedElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Trigger_S=ButtonConfig(self)
   self.objMT_pre__Trigger_S.Contents.Text.setValue('New Trigger_S')
   self.objMT_pre__Trigger_S.Contents.Image.setValue('')
   self.objMT_pre__Trigger_S.Contents.lastSelected= 'Text'
   self.objMT_pre__Trigger_S.Drawing_Mode.setValue(1)
   self.objMT_pre__Trigger_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Trigger_S (self, wherex, wherey)\n'))
   self.objMT_pre__Trigger_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Trigger_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Trigger_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Trigger_S)
   self.globalAndLocalPostcondition(self.objMT_pre__Trigger_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Action=ButtonConfig(self)
   self.objMT_pre__Action.Contents.Text.setValue('New Action')
   self.objMT_pre__Action.Contents.Image.setValue('')
   self.objMT_pre__Action.Contents.lastSelected= 'Text'
   self.objMT_pre__Action.Drawing_Mode.setValue(1)
   self.objMT_pre__Action.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Action (self, wherex, wherey)\n'))
   self.objMT_pre__Action.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Action)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Action.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Action)
   self.globalAndLocalPostcondition(self.objMT_pre__Action, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PortRef=ButtonConfig(self)
   self.objMT_pre__PortRef.Contents.Text.setValue('New PortRef')
   self.objMT_pre__PortRef.Contents.Image.setValue('')
   self.objMT_pre__PortRef.Contents.lastSelected= 'Text'
   self.objMT_pre__PortRef.Drawing_Mode.setValue(1)
   self.objMT_pre__PortRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PortRef (self, wherex, wherey)\n'))
   self.objMT_pre__PortRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__PortRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PortRef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PortRef)
   self.globalAndLocalPostcondition(self.objMT_pre__PortRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PortConnectorRef=ButtonConfig(self)
   self.objMT_pre__PortConnectorRef.Contents.Text.setValue('New PortConnectorRef')
   self.objMT_pre__PortConnectorRef.Contents.Image.setValue('')
   self.objMT_pre__PortConnectorRef.Contents.lastSelected= 'Text'
   self.objMT_pre__PortConnectorRef.Drawing_Mode.setValue(1)
   self.objMT_pre__PortConnectorRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PortConnectorRef (self, wherex, wherey)\n'))
   self.objMT_pre__PortConnectorRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__PortConnectorRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PortConnectorRef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PortConnectorRef)
   self.globalAndLocalPostcondition(self.objMT_pre__PortConnectorRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__StateMachineElement=ButtonConfig(self)
   self.objMT_pre__StateMachineElement.Contents.Text.setValue('New StateMachineElement')
   self.objMT_pre__StateMachineElement.Contents.Image.setValue('')
   self.objMT_pre__StateMachineElement.Contents.lastSelected= 'Text'
   self.objMT_pre__StateMachineElement.Drawing_Mode.setValue(1)
   self.objMT_pre__StateMachineElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__StateMachineElement (self, wherex, wherey)\n'))
   self.objMT_pre__StateMachineElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__StateMachineElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__StateMachineElement.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__StateMachineElement)
   self.globalAndLocalPostcondition(self.objMT_pre__StateMachineElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Protocol=ButtonConfig(self)
   self.objMT_pre__Protocol.Contents.Text.setValue('New Protocol')
   self.objMT_pre__Protocol.Contents.Image.setValue('')
   self.objMT_pre__Protocol.Contents.lastSelected= 'Text'
   self.objMT_pre__Protocol.Drawing_Mode.setValue(1)
   self.objMT_pre__Protocol.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Protocol (self, wherex, wherey)\n'))
   self.objMT_pre__Protocol.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Protocol)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Protocol.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Protocol)
   self.globalAndLocalPostcondition(self.objMT_pre__Protocol, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Signal=ButtonConfig(self)
   self.objMT_pre__Signal.Contents.Text.setValue('New Signal')
   self.objMT_pre__Signal.Contents.Image.setValue('')
   self.objMT_pre__Signal.Contents.lastSelected= 'Text'
   self.objMT_pre__Signal.Drawing_Mode.setValue(1)
   self.objMT_pre__Signal.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Signal (self, wherex, wherey)\n'))
   self.objMT_pre__Signal.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Signal)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Signal.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Signal)
   self.globalAndLocalPostcondition(self.objMT_pre__Signal, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Port=ButtonConfig(self)
   self.objMT_pre__Port.Contents.Text.setValue('New Port')
   self.objMT_pre__Port.Contents.Image.setValue('')
   self.objMT_pre__Port.Contents.lastSelected= 'Text'
   self.objMT_pre__Port.Drawing_Mode.setValue(1)
   self.objMT_pre__Port.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Port (self, wherex, wherey)\n'))
   self.objMT_pre__Port.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Port)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Port.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Port)
   self.globalAndLocalPostcondition(self.objMT_pre__Port, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Vertex=ButtonConfig(self)
   self.objMT_pre__Vertex.Contents.Text.setValue('New Vertex')
   self.objMT_pre__Vertex.Contents.Image.setValue('')
   self.objMT_pre__Vertex.Contents.lastSelected= 'Text'
   self.objMT_pre__Vertex.Drawing_Mode.setValue(1)
   self.objMT_pre__Vertex.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Vertex (self, wherex, wherey)\n'))
   self.objMT_pre__Vertex.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Vertex)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Vertex.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Vertex)
   self.globalAndLocalPostcondition(self.objMT_pre__Vertex, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__InitialPoint=ButtonConfig(self)
   self.objMT_pre__InitialPoint.Contents.Text.setValue('New InitialPoint')
   self.objMT_pre__InitialPoint.Contents.Image.setValue('')
   self.objMT_pre__InitialPoint.Contents.lastSelected= 'Text'
   self.objMT_pre__InitialPoint.Drawing_Mode.setValue(1)
   self.objMT_pre__InitialPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__InitialPoint (self, wherex, wherey)\n'))
   self.objMT_pre__InitialPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__InitialPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__InitialPoint.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__InitialPoint)
   self.globalAndLocalPostcondition(self.objMT_pre__InitialPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__EntryPoint=ButtonConfig(self)
   self.objMT_pre__EntryPoint.Contents.Text.setValue('New EntryPoint')
   self.objMT_pre__EntryPoint.Contents.Image.setValue('')
   self.objMT_pre__EntryPoint.Contents.lastSelected= 'Text'
   self.objMT_pre__EntryPoint.Drawing_Mode.setValue(1)
   self.objMT_pre__EntryPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__EntryPoint (self, wherex, wherey)\n'))
   self.objMT_pre__EntryPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__EntryPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__EntryPoint.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__EntryPoint)
   self.globalAndLocalPostcondition(self.objMT_pre__EntryPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ExitPoint=ButtonConfig(self)
   self.objMT_pre__ExitPoint.Contents.Text.setValue('New ExitPoint')
   self.objMT_pre__ExitPoint.Contents.Image.setValue('')
   self.objMT_pre__ExitPoint.Contents.lastSelected= 'Text'
   self.objMT_pre__ExitPoint.Drawing_Mode.setValue(1)
   self.objMT_pre__ExitPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ExitPoint (self, wherex, wherey)\n'))
   self.objMT_pre__ExitPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__ExitPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ExitPoint.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ExitPoint)
   self.globalAndLocalPostcondition(self.objMT_pre__ExitPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Transition=ButtonConfig(self)
   self.objMT_pre__Transition.Contents.Text.setValue('New Transition')
   self.objMT_pre__Transition.Contents.Image.setValue('')
   self.objMT_pre__Transition.Contents.lastSelected= 'Text'
   self.objMT_pre__Transition.Drawing_Mode.setValue(1)
   self.objMT_pre__Transition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Transition (self, wherex, wherey)\n'))
   self.objMT_pre__Transition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Transition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Transition.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Transition)
   self.globalAndLocalPostcondition(self.objMT_pre__Transition, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__StateMachine=ButtonConfig(self)
   self.objMT_pre__StateMachine.Contents.Text.setValue('New StateMachine')
   self.objMT_pre__StateMachine.Contents.Image.setValue('')
   self.objMT_pre__StateMachine.Contents.lastSelected= 'Text'
   self.objMT_pre__StateMachine.Drawing_Mode.setValue(1)
   self.objMT_pre__StateMachine.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__StateMachine (self, wherex, wherey)\n'))
   self.objMT_pre__StateMachine.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__StateMachine)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__StateMachine.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__StateMachine)
   self.globalAndLocalPostcondition(self.objMT_pre__StateMachine, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__State=ButtonConfig(self)
   self.objMT_pre__State.Contents.Text.setValue('New State')
   self.objMT_pre__State.Contents.Image.setValue('')
   self.objMT_pre__State.Contents.lastSelected= 'Text'
   self.objMT_pre__State.Drawing_Mode.setValue(1)
   self.objMT_pre__State.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__State (self, wherex, wherey)\n'))
   self.objMT_pre__State.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__State)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__State.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__State)
   self.globalAndLocalPostcondition(self.objMT_pre__State, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Capsule=ButtonConfig(self)
   self.objMT_pre__Capsule.Contents.Text.setValue('New Capsule')
   self.objMT_pre__Capsule.Contents.Image.setValue('')
   self.objMT_pre__Capsule.Contents.lastSelected= 'Text'
   self.objMT_pre__Capsule.Drawing_Mode.setValue(1)
   self.objMT_pre__Capsule.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Capsule (self, wherex, wherey)\n'))
   self.objMT_pre__Capsule.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Capsule)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Capsule.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Capsule)
   self.globalAndLocalPostcondition(self.objMT_pre__Capsule, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PackageContainer=ButtonConfig(self)
   self.objMT_pre__PackageContainer.Contents.Text.setValue('New PackageContainer')
   self.objMT_pre__PackageContainer.Contents.Image.setValue('')
   self.objMT_pre__PackageContainer.Contents.lastSelected= 'Text'
   self.objMT_pre__PackageContainer.Drawing_Mode.setValue(1)
   self.objMT_pre__PackageContainer.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PackageContainer (self, wherex, wherey)\n'))
   self.objMT_pre__PackageContainer.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__PackageContainer)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PackageContainer.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PackageContainer)
   self.globalAndLocalPostcondition(self.objMT_pre__PackageContainer, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Model_S=ButtonConfig(self)
   self.objMT_pre__Model_S.Contents.Text.setValue('New Model_S')
   self.objMT_pre__Model_S.Contents.Image.setValue('')
   self.objMT_pre__Model_S.Contents.lastSelected= 'Text'
   self.objMT_pre__Model_S.Drawing_Mode.setValue(1)
   self.objMT_pre__Model_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Model_S (self, wherex, wherey)\n'))
   self.objMT_pre__Model_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Model_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Model_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Model_S)
   self.globalAndLocalPostcondition(self.objMT_pre__Model_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Package=ButtonConfig(self)
   self.objMT_pre__Package.Contents.Text.setValue('New Package')
   self.objMT_pre__Package.Contents.Image.setValue('')
   self.objMT_pre__Package.Contents.lastSelected= 'Text'
   self.objMT_pre__Package.Drawing_Mode.setValue(1)
   self.objMT_pre__Package.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Package (self, wherex, wherey)\n'))
   self.objMT_pre__Package.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Package)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Package.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Package)
   self.globalAndLocalPostcondition(self.objMT_pre__Package, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__CapsuleRole=ButtonConfig(self)
   self.objMT_pre__CapsuleRole.Contents.Text.setValue('New CapsuleRole')
   self.objMT_pre__CapsuleRole.Contents.Image.setValue('')
   self.objMT_pre__CapsuleRole.Contents.lastSelected= 'Text'
   self.objMT_pre__CapsuleRole.Drawing_Mode.setValue(1)
   self.objMT_pre__CapsuleRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__CapsuleRole (self, wherex, wherey)\n'))
   self.objMT_pre__CapsuleRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__CapsuleRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__CapsuleRole.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__CapsuleRole)
   self.globalAndLocalPostcondition(self.objMT_pre__CapsuleRole, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PortConnector=ButtonConfig(self)
   self.objMT_pre__PortConnector.Contents.Text.setValue('New PortConnector')
   self.objMT_pre__PortConnector.Contents.Image.setValue('')
   self.objMT_pre__PortConnector.Contents.lastSelected= 'Text'
   self.objMT_pre__PortConnector.Drawing_Mode.setValue(1)
   self.objMT_pre__PortConnector.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PortConnector (self, wherex, wherey)\n'))
   self.objMT_pre__PortConnector.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__PortConnector)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PortConnector.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PortConnector)
   self.globalAndLocalPostcondition(self.objMT_pre__PortConnector, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Thread=ButtonConfig(self)
   self.objMT_pre__Thread.Contents.Text.setValue('New Thread')
   self.objMT_pre__Thread.Contents.Image.setValue('')
   self.objMT_pre__Thread.Contents.lastSelected= 'Text'
   self.objMT_pre__Thread.Drawing_Mode.setValue(1)
   self.objMT_pre__Thread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Thread (self, wherex, wherey)\n'))
   self.objMT_pre__Thread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Thread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Thread.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Thread)
   self.globalAndLocalPostcondition(self.objMT_pre__Thread, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PhysicalThread=ButtonConfig(self)
   self.objMT_pre__PhysicalThread.Contents.Text.setValue('New PhysicalThread')
   self.objMT_pre__PhysicalThread.Contents.Image.setValue('')
   self.objMT_pre__PhysicalThread.Contents.lastSelected= 'Text'
   self.objMT_pre__PhysicalThread.Drawing_Mode.setValue(1)
   self.objMT_pre__PhysicalThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PhysicalThread (self, wherex, wherey)\n'))
   self.objMT_pre__PhysicalThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__PhysicalThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PhysicalThread.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PhysicalThread)
   self.globalAndLocalPostcondition(self.objMT_pre__PhysicalThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__LogicalThread=ButtonConfig(self)
   self.objMT_pre__LogicalThread.Contents.Text.setValue('New LogicalThread')
   self.objMT_pre__LogicalThread.Contents.Image.setValue('')
   self.objMT_pre__LogicalThread.Contents.lastSelected= 'Text'
   self.objMT_pre__LogicalThread.Drawing_Mode.setValue(1)
   self.objMT_pre__LogicalThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__LogicalThread (self, wherex, wherey)\n'))
   self.objMT_pre__LogicalThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__LogicalThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__LogicalThread.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__LogicalThread)
   self.globalAndLocalPostcondition(self.objMT_pre__LogicalThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PortType=ButtonConfig(self)
   self.objMT_pre__PortType.Contents.Text.setValue('New PortType')
   self.objMT_pre__PortType.Contents.Image.setValue('')
   self.objMT_pre__PortType.Contents.lastSelected= 'Text'
   self.objMT_pre__PortType.Drawing_Mode.setValue(1)
   self.objMT_pre__PortType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PortType (self, wherex, wherey)\n'))
   self.objMT_pre__PortType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__PortType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PortType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PortType)
   self.globalAndLocalPostcondition(self.objMT_pre__PortType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__BASE0=ButtonConfig(self)
   self.objMT_pre__BASE0.Contents.Text.setValue('New BASE0')
   self.objMT_pre__BASE0.Contents.Image.setValue('')
   self.objMT_pre__BASE0.Contents.lastSelected= 'Text'
   self.objMT_pre__BASE0.Drawing_Mode.setValue(1)
   self.objMT_pre__BASE0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__BASE0 (self, wherex, wherey)\n'))
   self.objMT_pre__BASE0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__BASE0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__BASE0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__BASE0)
   self.globalAndLocalPostcondition(self.objMT_pre__BASE0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__CONJUGATE1=ButtonConfig(self)
   self.objMT_pre__CONJUGATE1.Contents.Text.setValue('New CONJUGATE1')
   self.objMT_pre__CONJUGATE1.Contents.Image.setValue('')
   self.objMT_pre__CONJUGATE1.Contents.lastSelected= 'Text'
   self.objMT_pre__CONJUGATE1.Drawing_Mode.setValue(1)
   self.objMT_pre__CONJUGATE1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__CONJUGATE1 (self, wherex, wherey)\n'))
   self.objMT_pre__CONJUGATE1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__CONJUGATE1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__CONJUGATE1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__CONJUGATE1)
   self.globalAndLocalPostcondition(self.objMT_pre__CONJUGATE1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__SignalType=ButtonConfig(self)
   self.objMT_pre__SignalType.Contents.Text.setValue('New SignalType')
   self.objMT_pre__SignalType.Contents.Image.setValue('')
   self.objMT_pre__SignalType.Contents.lastSelected= 'Text'
   self.objMT_pre__SignalType.Drawing_Mode.setValue(1)
   self.objMT_pre__SignalType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__SignalType (self, wherex, wherey)\n'))
   self.objMT_pre__SignalType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__SignalType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__SignalType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__SignalType)
   self.globalAndLocalPostcondition(self.objMT_pre__SignalType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__OUT1=ButtonConfig(self)
   self.objMT_pre__OUT1.Contents.Text.setValue('New OUT1')
   self.objMT_pre__OUT1.Contents.Image.setValue('')
   self.objMT_pre__OUT1.Contents.lastSelected= 'Text'
   self.objMT_pre__OUT1.Drawing_Mode.setValue(1)
   self.objMT_pre__OUT1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__OUT1 (self, wherex, wherey)\n'))
   self.objMT_pre__OUT1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__OUT1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__OUT1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__OUT1)
   self.globalAndLocalPostcondition(self.objMT_pre__OUT1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__IN0=ButtonConfig(self)
   self.objMT_pre__IN0.Contents.Text.setValue('New IN0')
   self.objMT_pre__IN0.Contents.Image.setValue('')
   self.objMT_pre__IN0.Contents.lastSelected= 'Text'
   self.objMT_pre__IN0.Drawing_Mode.setValue(1)
   self.objMT_pre__IN0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__IN0 (self, wherex, wherey)\n'))
   self.objMT_pre__IN0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__IN0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__IN0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__IN0)
   self.globalAndLocalPostcondition(self.objMT_pre__IN0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__RoleType=ButtonConfig(self)
   self.objMT_pre__RoleType.Contents.Text.setValue('New RoleType')
   self.objMT_pre__RoleType.Contents.Image.setValue('')
   self.objMT_pre__RoleType.Contents.lastSelected= 'Text'
   self.objMT_pre__RoleType.Drawing_Mode.setValue(1)
   self.objMT_pre__RoleType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__RoleType (self, wherex, wherey)\n'))
   self.objMT_pre__RoleType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__RoleType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__RoleType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__RoleType)
   self.globalAndLocalPostcondition(self.objMT_pre__RoleType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__FIXED0=ButtonConfig(self)
   self.objMT_pre__FIXED0.Contents.Text.setValue('New FIXED0')
   self.objMT_pre__FIXED0.Contents.Image.setValue('')
   self.objMT_pre__FIXED0.Contents.lastSelected= 'Text'
   self.objMT_pre__FIXED0.Drawing_Mode.setValue(1)
   self.objMT_pre__FIXED0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__FIXED0 (self, wherex, wherey)\n'))
   self.objMT_pre__FIXED0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__FIXED0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__FIXED0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__FIXED0)
   self.globalAndLocalPostcondition(self.objMT_pre__FIXED0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__OPTIONAL1=ButtonConfig(self)
   self.objMT_pre__OPTIONAL1.Contents.Text.setValue('New OPTIONAL1')
   self.objMT_pre__OPTIONAL1.Contents.Image.setValue('')
   self.objMT_pre__OPTIONAL1.Contents.lastSelected= 'Text'
   self.objMT_pre__OPTIONAL1.Drawing_Mode.setValue(1)
   self.objMT_pre__OPTIONAL1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__OPTIONAL1 (self, wherex, wherey)\n'))
   self.objMT_pre__OPTIONAL1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__OPTIONAL1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__OPTIONAL1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__OPTIONAL1)
   self.globalAndLocalPostcondition(self.objMT_pre__OPTIONAL1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PLUGIN2=ButtonConfig(self)
   self.objMT_pre__PLUGIN2.Contents.Text.setValue('New PLUGIN2')
   self.objMT_pre__PLUGIN2.Contents.Image.setValue('')
   self.objMT_pre__PLUGIN2.Contents.lastSelected= 'Text'
   self.objMT_pre__PLUGIN2.Drawing_Mode.setValue(1)
   self.objMT_pre__PLUGIN2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PLUGIN2 (self, wherex, wherey)\n'))
   self.objMT_pre__PLUGIN2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__PLUGIN2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PLUGIN2.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PLUGIN2)
   self.globalAndLocalPostcondition(self.objMT_pre__PLUGIN2, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__TransitionType=ButtonConfig(self)
   self.objMT_pre__TransitionType.Contents.Text.setValue('New TransitionType')
   self.objMT_pre__TransitionType.Contents.Image.setValue('')
   self.objMT_pre__TransitionType.Contents.lastSelected= 'Text'
   self.objMT_pre__TransitionType.Drawing_Mode.setValue(1)
   self.objMT_pre__TransitionType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__TransitionType (self, wherex, wherey)\n'))
   self.objMT_pre__TransitionType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__TransitionType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__TransitionType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__TransitionType)
   self.globalAndLocalPostcondition(self.objMT_pre__TransitionType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__SIBLING0=ButtonConfig(self)
   self.objMT_pre__SIBLING0.Contents.Text.setValue('New SIBLING0')
   self.objMT_pre__SIBLING0.Contents.Image.setValue('')
   self.objMT_pre__SIBLING0.Contents.lastSelected= 'Text'
   self.objMT_pre__SIBLING0.Drawing_Mode.setValue(1)
   self.objMT_pre__SIBLING0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__SIBLING0 (self, wherex, wherey)\n'))
   self.objMT_pre__SIBLING0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__SIBLING0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__SIBLING0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__SIBLING0)
   self.globalAndLocalPostcondition(self.objMT_pre__SIBLING0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__IN1=ButtonConfig(self)
   self.objMT_pre__IN1.Contents.Text.setValue('New IN1')
   self.objMT_pre__IN1.Contents.Image.setValue('')
   self.objMT_pre__IN1.Contents.lastSelected= 'Text'
   self.objMT_pre__IN1.Drawing_Mode.setValue(1)
   self.objMT_pre__IN1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__IN1 (self, wherex, wherey)\n'))
   self.objMT_pre__IN1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__IN1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__IN1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__IN1)
   self.globalAndLocalPostcondition(self.objMT_pre__IN1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__OUT2=ButtonConfig(self)
   self.objMT_pre__OUT2.Contents.Text.setValue('New OUT2')
   self.objMT_pre__OUT2.Contents.Image.setValue('')
   self.objMT_pre__OUT2.Contents.lastSelected= 'Text'
   self.objMT_pre__OUT2.Drawing_Mode.setValue(1)
   self.objMT_pre__OUT2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__OUT2 (self, wherex, wherey)\n'))
   self.objMT_pre__OUT2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__OUT2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__OUT2.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__OUT2)
   self.globalAndLocalPostcondition(self.objMT_pre__OUT2, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Def=ButtonConfig(self)
   self.objMT_pre__Def.Contents.Text.setValue('New Def')
   self.objMT_pre__Def.Contents.Image.setValue('')
   self.objMT_pre__Def.Contents.lastSelected= 'Text'
   self.objMT_pre__Def.Drawing_Mode.setValue(1)
   self.objMT_pre__Def.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Def (self, wherex, wherey)\n'))
   self.objMT_pre__Def.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Def)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Def.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Def)
   self.globalAndLocalPostcondition(self.objMT_pre__Def, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Expr=ButtonConfig(self)
   self.objMT_pre__Expr.Contents.Text.setValue('New Expr')
   self.objMT_pre__Expr.Contents.Image.setValue('')
   self.objMT_pre__Expr.Contents.lastSelected= 'Text'
   self.objMT_pre__Expr.Drawing_Mode.setValue(1)
   self.objMT_pre__Expr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Expr (self, wherex, wherey)\n'))
   self.objMT_pre__Expr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Expr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Expr.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Expr)
   self.globalAndLocalPostcondition(self.objMT_pre__Expr, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Pattern=ButtonConfig(self)
   self.objMT_pre__Pattern.Contents.Text.setValue('New Pattern')
   self.objMT_pre__Pattern.Contents.Image.setValue('')
   self.objMT_pre__Pattern.Contents.lastSelected= 'Text'
   self.objMT_pre__Pattern.Drawing_Mode.setValue(1)
   self.objMT_pre__Pattern.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Pattern (self, wherex, wherey)\n'))
   self.objMT_pre__Pattern.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Pattern)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Pattern.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Pattern)
   self.globalAndLocalPostcondition(self.objMT_pre__Pattern, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Proc=ButtonConfig(self)
   self.objMT_pre__Proc.Contents.Text.setValue('New Proc')
   self.objMT_pre__Proc.Contents.Image.setValue('')
   self.objMT_pre__Proc.Contents.lastSelected= 'Text'
   self.objMT_pre__Proc.Drawing_Mode.setValue(1)
   self.objMT_pre__Proc.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Proc (self, wherex, wherey)\n'))
   self.objMT_pre__Proc.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Proc)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Proc.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Proc)
   self.globalAndLocalPostcondition(self.objMT_pre__Proc, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ProcDef=ButtonConfig(self)
   self.objMT_pre__ProcDef.Contents.Text.setValue('New ProcDef')
   self.objMT_pre__ProcDef.Contents.Image.setValue('')
   self.objMT_pre__ProcDef.Contents.lastSelected= 'Text'
   self.objMT_pre__ProcDef.Drawing_Mode.setValue(1)
   self.objMT_pre__ProcDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ProcDef (self, wherex, wherey)\n'))
   self.objMT_pre__ProcDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__ProcDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ProcDef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ProcDef)
   self.globalAndLocalPostcondition(self.objMT_pre__ProcDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__FuncDef=ButtonConfig(self)
   self.objMT_pre__FuncDef.Contents.Text.setValue('New FuncDef')
   self.objMT_pre__FuncDef.Contents.Image.setValue('')
   self.objMT_pre__FuncDef.Contents.lastSelected= 'Text'
   self.objMT_pre__FuncDef.Drawing_Mode.setValue(1)
   self.objMT_pre__FuncDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__FuncDef (self, wherex, wherey)\n'))
   self.objMT_pre__FuncDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__FuncDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__FuncDef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__FuncDef)
   self.globalAndLocalPostcondition(self.objMT_pre__FuncDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Name=ButtonConfig(self)
   self.objMT_pre__Name.Contents.Text.setValue('New Name')
   self.objMT_pre__Name.Contents.Image.setValue('')
   self.objMT_pre__Name.Contents.lastSelected= 'Text'
   self.objMT_pre__Name.Drawing_Mode.setValue(1)
   self.objMT_pre__Name.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Name (self, wherex, wherey)\n'))
   self.objMT_pre__Name.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Name)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Name.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Name)
   self.globalAndLocalPostcondition(self.objMT_pre__Name, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PythonRef=ButtonConfig(self)
   self.objMT_pre__PythonRef.Contents.Text.setValue('New PythonRef')
   self.objMT_pre__PythonRef.Contents.Image.setValue('')
   self.objMT_pre__PythonRef.Contents.lastSelected= 'Text'
   self.objMT_pre__PythonRef.Drawing_Mode.setValue(1)
   self.objMT_pre__PythonRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PythonRef (self, wherex, wherey)\n'))
   self.objMT_pre__PythonRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__PythonRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PythonRef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PythonRef)
   self.globalAndLocalPostcondition(self.objMT_pre__PythonRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Module=ButtonConfig(self)
   self.objMT_pre__Module.Contents.Text.setValue('New Module')
   self.objMT_pre__Module.Contents.Image.setValue('')
   self.objMT_pre__Module.Contents.lastSelected= 'Text'
   self.objMT_pre__Module.Drawing_Mode.setValue(1)
   self.objMT_pre__Module.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Module (self, wherex, wherey)\n'))
   self.objMT_pre__Module.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Module)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Module.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Module)
   self.globalAndLocalPostcondition(self.objMT_pre__Module, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Null=ButtonConfig(self)
   self.objMT_pre__Null.Contents.Text.setValue('New Null')
   self.objMT_pre__Null.Contents.Image.setValue('')
   self.objMT_pre__Null.Contents.lastSelected= 'Text'
   self.objMT_pre__Null.Drawing_Mode.setValue(1)
   self.objMT_pre__Null.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Null (self, wherex, wherey)\n'))
   self.objMT_pre__Null.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Null)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Null.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Null)
   self.globalAndLocalPostcondition(self.objMT_pre__Null, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Trigger_T=ButtonConfig(self)
   self.objMT_pre__Trigger_T.Contents.Text.setValue('New Trigger_T')
   self.objMT_pre__Trigger_T.Contents.Image.setValue('')
   self.objMT_pre__Trigger_T.Contents.lastSelected= 'Text'
   self.objMT_pre__Trigger_T.Drawing_Mode.setValue(1)
   self.objMT_pre__Trigger_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Trigger_T (self, wherex, wherey)\n'))
   self.objMT_pre__Trigger_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Trigger_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Trigger_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Trigger_T)
   self.globalAndLocalPostcondition(self.objMT_pre__Trigger_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Listen=ButtonConfig(self)
   self.objMT_pre__Listen.Contents.Text.setValue('New Listen')
   self.objMT_pre__Listen.Contents.Image.setValue('')
   self.objMT_pre__Listen.Contents.lastSelected= 'Text'
   self.objMT_pre__Listen.Drawing_Mode.setValue(1)
   self.objMT_pre__Listen.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Listen (self, wherex, wherey)\n'))
   self.objMT_pre__Listen.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Listen)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Listen.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Listen)
   self.globalAndLocalPostcondition(self.objMT_pre__Listen, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ConditionBranch=ButtonConfig(self)
   self.objMT_pre__ConditionBranch.Contents.Text.setValue('New ConditionBranch')
   self.objMT_pre__ConditionBranch.Contents.Image.setValue('')
   self.objMT_pre__ConditionBranch.Contents.lastSelected= 'Text'
   self.objMT_pre__ConditionBranch.Drawing_Mode.setValue(1)
   self.objMT_pre__ConditionBranch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ConditionBranch (self, wherex, wherey)\n'))
   self.objMT_pre__ConditionBranch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__ConditionBranch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ConditionBranch.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ConditionBranch)
   self.globalAndLocalPostcondition(self.objMT_pre__ConditionBranch, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ListenBranch=ButtonConfig(self)
   self.objMT_pre__ListenBranch.Contents.Text.setValue('New ListenBranch')
   self.objMT_pre__ListenBranch.Contents.Image.setValue('')
   self.objMT_pre__ListenBranch.Contents.lastSelected= 'Text'
   self.objMT_pre__ListenBranch.Drawing_Mode.setValue(1)
   self.objMT_pre__ListenBranch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ListenBranch (self, wherex, wherey)\n'))
   self.objMT_pre__ListenBranch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__ListenBranch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ListenBranch.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ListenBranch)
   self.globalAndLocalPostcondition(self.objMT_pre__ListenBranch, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Site=ButtonConfig(self)
   self.objMT_pre__Site.Contents.Text.setValue('New Site')
   self.objMT_pre__Site.Contents.Image.setValue('')
   self.objMT_pre__Site.Contents.lastSelected= 'Text'
   self.objMT_pre__Site.Drawing_Mode.setValue(1)
   self.objMT_pre__Site.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Site (self, wherex, wherey)\n'))
   self.objMT_pre__Site.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Site)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Site.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Site)
   self.globalAndLocalPostcondition(self.objMT_pre__Site, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Model_T=ButtonConfig(self)
   self.objMT_pre__Model_T.Contents.Text.setValue('New Model_T')
   self.objMT_pre__Model_T.Contents.Image.setValue('')
   self.objMT_pre__Model_T.Contents.lastSelected= 'Text'
   self.objMT_pre__Model_T.Drawing_Mode.setValue(1)
   self.objMT_pre__Model_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Model_T (self, wherex, wherey)\n'))
   self.objMT_pre__Model_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Model_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Model_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Model_T)
   self.globalAndLocalPostcondition(self.objMT_pre__Model_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__MatchCase=ButtonConfig(self)
   self.objMT_pre__MatchCase.Contents.Text.setValue('New MatchCase')
   self.objMT_pre__MatchCase.Contents.Image.setValue('')
   self.objMT_pre__MatchCase.Contents.lastSelected= 'Text'
   self.objMT_pre__MatchCase.Drawing_Mode.setValue(1)
   self.objMT_pre__MatchCase.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__MatchCase (self, wherex, wherey)\n'))
   self.objMT_pre__MatchCase.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__MatchCase)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__MatchCase.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__MatchCase)
   self.globalAndLocalPostcondition(self.objMT_pre__MatchCase, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Condition=ButtonConfig(self)
   self.objMT_pre__Condition.Contents.Text.setValue('New Condition')
   self.objMT_pre__Condition.Contents.Image.setValue('')
   self.objMT_pre__Condition.Contents.lastSelected= 'Text'
   self.objMT_pre__Condition.Drawing_Mode.setValue(1)
   self.objMT_pre__Condition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Condition (self, wherex, wherey)\n'))
   self.objMT_pre__Condition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Condition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Condition.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Condition)
   self.globalAndLocalPostcondition(self.objMT_pre__Condition, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__New=ButtonConfig(self)
   self.objMT_pre__New.Contents.Text.setValue('New New')
   self.objMT_pre__New.Contents.Image.setValue('')
   self.objMT_pre__New.Contents.lastSelected= 'Text'
   self.objMT_pre__New.Drawing_Mode.setValue(1)
   self.objMT_pre__New.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__New (self, wherex, wherey)\n'))
   self.objMT_pre__New.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__New)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__New.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__New)
   self.globalAndLocalPostcondition(self.objMT_pre__New, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Delay=ButtonConfig(self)
   self.objMT_pre__Delay.Contents.Text.setValue('New Delay')
   self.objMT_pre__Delay.Contents.Image.setValue('')
   self.objMT_pre__Delay.Contents.lastSelected= 'Text'
   self.objMT_pre__Delay.Drawing_Mode.setValue(1)
   self.objMT_pre__Delay.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Delay (self, wherex, wherey)\n'))
   self.objMT_pre__Delay.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Delay)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Delay.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Delay)
   self.globalAndLocalPostcondition(self.objMT_pre__Delay, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Par=ButtonConfig(self)
   self.objMT_pre__Par.Contents.Text.setValue('New Par')
   self.objMT_pre__Par.Contents.Image.setValue('')
   self.objMT_pre__Par.Contents.lastSelected= 'Text'
   self.objMT_pre__Par.Drawing_Mode.setValue(1)
   self.objMT_pre__Par.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Par (self, wherex, wherey)\n'))
   self.objMT_pre__Par.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Par)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Par.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Par)
   self.globalAndLocalPostcondition(self.objMT_pre__Par, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ParIndexed=ButtonConfig(self)
   self.objMT_pre__ParIndexed.Contents.Text.setValue('New ParIndexed')
   self.objMT_pre__ParIndexed.Contents.Image.setValue('')
   self.objMT_pre__ParIndexed.Contents.lastSelected= 'Text'
   self.objMT_pre__ParIndexed.Drawing_Mode.setValue(1)
   self.objMT_pre__ParIndexed.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ParIndexed (self, wherex, wherey)\n'))
   self.objMT_pre__ParIndexed.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__ParIndexed)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ParIndexed.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ParIndexed)
   self.globalAndLocalPostcondition(self.objMT_pre__ParIndexed, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Inst=ButtonConfig(self)
   self.objMT_pre__Inst.Contents.Text.setValue('New Inst')
   self.objMT_pre__Inst.Contents.Image.setValue('')
   self.objMT_pre__Inst.Contents.lastSelected= 'Text'
   self.objMT_pre__Inst.Drawing_Mode.setValue(1)
   self.objMT_pre__Inst.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Inst (self, wherex, wherey)\n'))
   self.objMT_pre__Inst.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Inst)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Inst.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Inst)
   self.globalAndLocalPostcondition(self.objMT_pre__Inst, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__LocalDef=ButtonConfig(self)
   self.objMT_pre__LocalDef.Contents.Text.setValue('New LocalDef')
   self.objMT_pre__LocalDef.Contents.Image.setValue('')
   self.objMT_pre__LocalDef.Contents.lastSelected= 'Text'
   self.objMT_pre__LocalDef.Drawing_Mode.setValue(1)
   self.objMT_pre__LocalDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__LocalDef (self, wherex, wherey)\n'))
   self.objMT_pre__LocalDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__LocalDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__LocalDef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__LocalDef)
   self.globalAndLocalPostcondition(self.objMT_pre__LocalDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Seq=ButtonConfig(self)
   self.objMT_pre__Seq.Contents.Text.setValue('New Seq')
   self.objMT_pre__Seq.Contents.Image.setValue('')
   self.objMT_pre__Seq.Contents.lastSelected= 'Text'
   self.objMT_pre__Seq.Drawing_Mode.setValue(1)
   self.objMT_pre__Seq.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Seq (self, wherex, wherey)\n'))
   self.objMT_pre__Seq.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Seq)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Seq.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Seq)
   self.globalAndLocalPostcondition(self.objMT_pre__Seq, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ConditionSet=ButtonConfig(self)
   self.objMT_pre__ConditionSet.Contents.Text.setValue('New ConditionSet')
   self.objMT_pre__ConditionSet.Contents.Image.setValue('')
   self.objMT_pre__ConditionSet.Contents.lastSelected= 'Text'
   self.objMT_pre__ConditionSet.Drawing_Mode.setValue(1)
   self.objMT_pre__ConditionSet.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ConditionSet (self, wherex, wherey)\n'))
   self.objMT_pre__ConditionSet.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__ConditionSet)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ConditionSet.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ConditionSet)
   self.globalAndLocalPostcondition(self.objMT_pre__ConditionSet, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Match=ButtonConfig(self)
   self.objMT_pre__Match.Contents.Text.setValue('New Match')
   self.objMT_pre__Match.Contents.Image.setValue('')
   self.objMT_pre__Match.Contents.lastSelected= 'Text'
   self.objMT_pre__Match.Drawing_Mode.setValue(1)
   self.objMT_pre__Match.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Match (self, wherex, wherey)\n'))
   self.objMT_pre__Match.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Match)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Match.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Match)
   self.globalAndLocalPostcondition(self.objMT_pre__Match, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Print=ButtonConfig(self)
   self.objMT_pre__Print.Contents.Text.setValue('New Print')
   self.objMT_pre__Print.Contents.Image.setValue('')
   self.objMT_pre__Print.Contents.lastSelected= 'Text'
   self.objMT_pre__Print.Drawing_Mode.setValue(1)
   self.objMT_pre__Print.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Print (self, wherex, wherey)\n'))
   self.objMT_pre__Print.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Print)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Print.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Print)
   self.globalAndLocalPostcondition(self.objMT_pre__Print, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Attribute=ButtonConfig(self)
   self.objMT_pre__Attribute.Contents.Text.setValue('New Attribute')
   self.objMT_pre__Attribute.Contents.Image.setValue('')
   self.objMT_pre__Attribute.Contents.lastSelected= 'Text'
   self.objMT_pre__Attribute.Drawing_Mode.setValue(1)
   self.objMT_pre__Attribute.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Attribute (self, wherex, wherey)\n'))
   self.objMT_pre__Attribute.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Attribute)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Attribute.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Attribute)
   self.globalAndLocalPostcondition(self.objMT_pre__Attribute, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Expression=ButtonConfig(self)
   self.objMT_pre__Expression.Contents.Text.setValue('New Expression')
   self.objMT_pre__Expression.Contents.Image.setValue('')
   self.objMT_pre__Expression.Contents.lastSelected= 'Text'
   self.objMT_pre__Expression.Drawing_Mode.setValue(1)
   self.objMT_pre__Expression.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Expression (self, wherex, wherey)\n'))
   self.objMT_pre__Expression.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Expression)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Expression.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Expression)
   self.globalAndLocalPostcondition(self.objMT_pre__Expression, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Equation=ButtonConfig(self)
   self.objMT_pre__Equation.Contents.Text.setValue('New Equation')
   self.objMT_pre__Equation.Contents.Image.setValue('')
   self.objMT_pre__Equation.Contents.lastSelected= 'Text'
   self.objMT_pre__Equation.Drawing_Mode.setValue(1)
   self.objMT_pre__Equation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Equation (self, wherex, wherey)\n'))
   self.objMT_pre__Equation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Equation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Equation.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Equation)
   self.globalAndLocalPostcondition(self.objMT_pre__Equation, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Operation=ButtonConfig(self)
   self.objMT_pre__Operation.Contents.Text.setValue('New Operation')
   self.objMT_pre__Operation.Contents.Image.setValue('')
   self.objMT_pre__Operation.Contents.lastSelected= 'Text'
   self.objMT_pre__Operation.Drawing_Mode.setValue(1)
   self.objMT_pre__Operation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Operation (self, wherex, wherey)\n'))
   self.objMT_pre__Operation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Operation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Operation.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Operation)
   self.globalAndLocalPostcondition(self.objMT_pre__Operation, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Add=ButtonConfig(self)
   self.objMT_pre__Add.Contents.Text.setValue('New Add')
   self.objMT_pre__Add.Contents.Image.setValue('')
   self.objMT_pre__Add.Contents.lastSelected= 'Text'
   self.objMT_pre__Add.Drawing_Mode.setValue(1)
   self.objMT_pre__Add.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Add (self, wherex, wherey)\n'))
   self.objMT_pre__Add.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Add)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Add.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Add)
   self.globalAndLocalPostcondition(self.objMT_pre__Add, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Subtract=ButtonConfig(self)
   self.objMT_pre__Subtract.Contents.Text.setValue('New Subtract')
   self.objMT_pre__Subtract.Contents.Image.setValue('')
   self.objMT_pre__Subtract.Contents.lastSelected= 'Text'
   self.objMT_pre__Subtract.Drawing_Mode.setValue(1)
   self.objMT_pre__Subtract.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Subtract (self, wherex, wherey)\n'))
   self.objMT_pre__Subtract.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Subtract)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Subtract.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Subtract)
   self.globalAndLocalPostcondition(self.objMT_pre__Subtract, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Concat=ButtonConfig(self)
   self.objMT_pre__Concat.Contents.Text.setValue('New Concat')
   self.objMT_pre__Concat.Contents.Image.setValue('')
   self.objMT_pre__Concat.Contents.lastSelected= 'Text'
   self.objMT_pre__Concat.Drawing_Mode.setValue(1)
   self.objMT_pre__Concat.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Concat (self, wherex, wherey)\n'))
   self.objMT_pre__Concat.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Concat)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Concat.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Concat)
   self.globalAndLocalPostcondition(self.objMT_pre__Concat, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Constant=ButtonConfig(self)
   self.objMT_pre__Constant.Contents.Text.setValue('New Constant')
   self.objMT_pre__Constant.Contents.Image.setValue('')
   self.objMT_pre__Constant.Contents.lastSelected= 'Text'
   self.objMT_pre__Constant.Drawing_Mode.setValue(1)
   self.objMT_pre__Constant.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Constant (self, wherex, wherey)\n'))
   self.objMT_pre__Constant.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Constant)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Constant.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Constant)
   self.globalAndLocalPostcondition(self.objMT_pre__Constant, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM=ButtonConfig(self)
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.Contents.Text.setValue('New GenericNode')
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.Contents.Image.setValue('')
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.Contents.lastSelected= 'Text'
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.Drawing_Mode.setValue(1)
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__GenericNode_UMLRT2Kiltera_MM (self, wherex, wherey)\n'))
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__GenericNode_UMLRT2Kiltera_MM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__GenericNode_UMLRT2Kiltera_MM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__GenericNode_UMLRT2Kiltera_MM)
   self.globalAndLocalPostcondition(self.objMT_pre__GenericNode_UMLRT2Kiltera_MM, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__paired_with=ButtonConfig(self)
   self.objMT_pre__paired_with.Contents.Text.setValue('New paired_with')
   self.objMT_pre__paired_with.Contents.Image.setValue('')
   self.objMT_pre__paired_with.Contents.lastSelected= 'Text'
   self.objMT_pre__paired_with.Drawing_Mode.setValue(1)
   self.objMT_pre__paired_with.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__paired_with (self, wherex, wherey)\n'))
   self.objMT_pre__paired_with.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__paired_with)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__paired_with.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__paired_with)
   self.globalAndLocalPostcondition(self.objMT_pre__paired_with, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__match_contains=ButtonConfig(self)
   self.objMT_pre__match_contains.Contents.Text.setValue('New match_contains')
   self.objMT_pre__match_contains.Contents.Image.setValue('')
   self.objMT_pre__match_contains.Contents.lastSelected= 'Text'
   self.objMT_pre__match_contains.Drawing_Mode.setValue(1)
   self.objMT_pre__match_contains.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__match_contains (self, wherex, wherey)\n'))
   self.objMT_pre__match_contains.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__match_contains)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__match_contains.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__match_contains)
   self.globalAndLocalPostcondition(self.objMT_pre__match_contains, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__apply_contains=ButtonConfig(self)
   self.objMT_pre__apply_contains.Contents.Text.setValue('New apply_contains')
   self.objMT_pre__apply_contains.Contents.Image.setValue('')
   self.objMT_pre__apply_contains.Contents.lastSelected= 'Text'
   self.objMT_pre__apply_contains.Drawing_Mode.setValue(1)
   self.objMT_pre__apply_contains.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__apply_contains (self, wherex, wherey)\n'))
   self.objMT_pre__apply_contains.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__apply_contains)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__apply_contains.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__apply_contains)
   self.globalAndLocalPostcondition(self.objMT_pre__apply_contains, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__directLink_T=ButtonConfig(self)
   self.objMT_pre__directLink_T.Contents.Text.setValue('New directLink_T')
   self.objMT_pre__directLink_T.Contents.Image.setValue('')
   self.objMT_pre__directLink_T.Contents.lastSelected= 'Text'
   self.objMT_pre__directLink_T.Drawing_Mode.setValue(1)
   self.objMT_pre__directLink_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__directLink_T (self, wherex, wherey)\n'))
   self.objMT_pre__directLink_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__directLink_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__directLink_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__directLink_T)
   self.globalAndLocalPostcondition(self.objMT_pre__directLink_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__directLink_S=ButtonConfig(self)
   self.objMT_pre__directLink_S.Contents.Text.setValue('New directLink_S')
   self.objMT_pre__directLink_S.Contents.Image.setValue('')
   self.objMT_pre__directLink_S.Contents.lastSelected= 'Text'
   self.objMT_pre__directLink_S.Drawing_Mode.setValue(1)
   self.objMT_pre__directLink_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__directLink_S (self, wherex, wherey)\n'))
   self.objMT_pre__directLink_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__directLink_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__directLink_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__directLink_S)
   self.globalAndLocalPostcondition(self.objMT_pre__directLink_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__indirectLink_S=ButtonConfig(self)
   self.objMT_pre__indirectLink_S.Contents.Text.setValue('New indirectLink_S')
   self.objMT_pre__indirectLink_S.Contents.Image.setValue('')
   self.objMT_pre__indirectLink_S.Contents.lastSelected= 'Text'
   self.objMT_pre__indirectLink_S.Drawing_Mode.setValue(1)
   self.objMT_pre__indirectLink_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__indirectLink_S (self, wherex, wherey)\n'))
   self.objMT_pre__indirectLink_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__indirectLink_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__indirectLink_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__indirectLink_S)
   self.globalAndLocalPostcondition(self.objMT_pre__indirectLink_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__backward_link=ButtonConfig(self)
   self.objMT_pre__backward_link.Contents.Text.setValue('New backward_link')
   self.objMT_pre__backward_link.Contents.Image.setValue('')
   self.objMT_pre__backward_link.Contents.lastSelected= 'Text'
   self.objMT_pre__backward_link.Drawing_Mode.setValue(1)
   self.objMT_pre__backward_link.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__backward_link (self, wherex, wherey)\n'))
   self.objMT_pre__backward_link.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__backward_link)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__backward_link.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__backward_link)
   self.globalAndLocalPostcondition(self.objMT_pre__backward_link, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__trace_link=ButtonConfig(self)
   self.objMT_pre__trace_link.Contents.Text.setValue('New trace_link')
   self.objMT_pre__trace_link.Contents.Image.setValue('')
   self.objMT_pre__trace_link.Contents.lastSelected= 'Text'
   self.objMT_pre__trace_link.Drawing_Mode.setValue(1)
   self.objMT_pre__trace_link.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__trace_link (self, wherex, wherey)\n'))
   self.objMT_pre__trace_link.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__trace_link)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__trace_link.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__trace_link)
   self.globalAndLocalPostcondition(self.objMT_pre__trace_link, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__hasAttribute_S=ButtonConfig(self)
   self.objMT_pre__hasAttribute_S.Contents.Text.setValue('New hasAttribute_S')
   self.objMT_pre__hasAttribute_S.Contents.Image.setValue('')
   self.objMT_pre__hasAttribute_S.Contents.lastSelected= 'Text'
   self.objMT_pre__hasAttribute_S.Drawing_Mode.setValue(1)
   self.objMT_pre__hasAttribute_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__hasAttribute_S (self, wherex, wherey)\n'))
   self.objMT_pre__hasAttribute_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__hasAttribute_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__hasAttribute_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__hasAttribute_S)
   self.globalAndLocalPostcondition(self.objMT_pre__hasAttribute_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__hasAttribute_T=ButtonConfig(self)
   self.objMT_pre__hasAttribute_T.Contents.Text.setValue('New hasAttribute_T')
   self.objMT_pre__hasAttribute_T.Contents.Image.setValue('')
   self.objMT_pre__hasAttribute_T.Contents.lastSelected= 'Text'
   self.objMT_pre__hasAttribute_T.Drawing_Mode.setValue(1)
   self.objMT_pre__hasAttribute_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__hasAttribute_T (self, wherex, wherey)\n'))
   self.objMT_pre__hasAttribute_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__hasAttribute_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__hasAttribute_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__hasAttribute_T)
   self.globalAndLocalPostcondition(self.objMT_pre__hasAttribute_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__leftExpr=ButtonConfig(self)
   self.objMT_pre__leftExpr.Contents.Text.setValue('New leftExpr')
   self.objMT_pre__leftExpr.Contents.Image.setValue('')
   self.objMT_pre__leftExpr.Contents.lastSelected= 'Text'
   self.objMT_pre__leftExpr.Drawing_Mode.setValue(1)
   self.objMT_pre__leftExpr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__leftExpr (self, wherex, wherey)\n'))
   self.objMT_pre__leftExpr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__leftExpr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__leftExpr.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__leftExpr)
   self.globalAndLocalPostcondition(self.objMT_pre__leftExpr, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__rightExpr=ButtonConfig(self)
   self.objMT_pre__rightExpr.Contents.Text.setValue('New rightExpr')
   self.objMT_pre__rightExpr.Contents.Image.setValue('')
   self.objMT_pre__rightExpr.Contents.lastSelected= 'Text'
   self.objMT_pre__rightExpr.Drawing_Mode.setValue(1)
   self.objMT_pre__rightExpr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__rightExpr (self, wherex, wherey)\n'))
   self.objMT_pre__rightExpr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__rightExpr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__rightExpr.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__rightExpr)
   self.globalAndLocalPostcondition(self.objMT_pre__rightExpr, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__hasArgs=ButtonConfig(self)
   self.objMT_pre__hasArgs.Contents.Text.setValue('New hasArgs')
   self.objMT_pre__hasArgs.Contents.Image.setValue('')
   self.objMT_pre__hasArgs.Contents.lastSelected= 'Text'
   self.objMT_pre__hasArgs.Drawing_Mode.setValue(1)
   self.objMT_pre__hasArgs.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__hasArgs (self, wherex, wherey)\n'))
   self.objMT_pre__hasArgs.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__hasArgs)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__hasArgs.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__hasArgs)
   self.globalAndLocalPostcondition(self.objMT_pre__hasArgs, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM=ButtonConfig(self)
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.Contents.Text.setValue('New GenericEdge_UMLRT2Kiltera_MM')
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.Contents.Image.setValue('')
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.Contents.lastSelected= 'Text'
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.Drawing_Mode.setValue(1)
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__GenericEdge_UMLRT2Kiltera_MM (self, wherex, wherey)\n'))
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM)
   self.globalAndLocalPostcondition(self.objMT_pre__GenericEdge_UMLRT2Kiltera_MM, rootNode)

newfunction = MT_pre__UMLRT2Kiltera_MM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
