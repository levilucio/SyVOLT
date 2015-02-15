"""
__MT_post__UMLRT2Kiltera_MM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: gehan
Modified: Sun Feb 15 10:37:42 2015
________________________________________________________________________________________
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
def MT_post__UMLRT2Kiltera_MM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_post__UMLRT2Kiltera_MM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_post__UMLRT2Kiltera_MM_MM.py' )
   self.globalPrecondition(rootNode)

   self.objMT_post__MatchModel=ButtonConfig(self)
   self.objMT_post__MatchModel.Contents.Text.setValue('New MatchModel')
   self.objMT_post__MatchModel.Contents.Image.setValue('')
   self.objMT_post__MatchModel.Contents.lastSelected= 'Text'
   self.objMT_post__MatchModel.Drawing_Mode.setValue(1)
   self.objMT_post__MatchModel.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__MatchModel (self, wherex, wherey)\n'))
   self.objMT_post__MatchModel.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__MatchModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__MatchModel.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__MatchModel)
   self.globalAndLocalPostcondition(self.objMT_post__MatchModel, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ApplyModel=ButtonConfig(self)
   self.objMT_post__ApplyModel.Contents.Text.setValue('New ApplyModel')
   self.objMT_post__ApplyModel.Contents.Image.setValue('')
   self.objMT_post__ApplyModel.Contents.lastSelected= 'Text'
   self.objMT_post__ApplyModel.Drawing_Mode.setValue(1)
   self.objMT_post__ApplyModel.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ApplyModel (self, wherex, wherey)\n'))
   self.objMT_post__ApplyModel.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__ApplyModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ApplyModel.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ApplyModel)
   self.globalAndLocalPostcondition(self.objMT_post__ApplyModel, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__MetaModelElement_S=ButtonConfig(self)
   self.objMT_post__MetaModelElement_S.Contents.Text.setValue('New MetaModelElement_S')
   self.objMT_post__MetaModelElement_S.Contents.Image.setValue('')
   self.objMT_post__MetaModelElement_S.Contents.lastSelected= 'Text'
   self.objMT_post__MetaModelElement_S.Drawing_Mode.setValue(1)
   self.objMT_post__MetaModelElement_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__MetaModelElement_S (self, wherex, wherey)\n'))
   self.objMT_post__MetaModelElement_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__MetaModelElement_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__MetaModelElement_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__MetaModelElement_S)
   self.globalAndLocalPostcondition(self.objMT_post__MetaModelElement_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__MetaModelElement_T=ButtonConfig(self)
   self.objMT_post__MetaModelElement_T.Contents.Text.setValue('New MetaModelElement_T')
   self.objMT_post__MetaModelElement_T.Contents.Image.setValue('')
   self.objMT_post__MetaModelElement_T.Contents.lastSelected= 'Text'
   self.objMT_post__MetaModelElement_T.Drawing_Mode.setValue(1)
   self.objMT_post__MetaModelElement_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__MetaModelElement_T (self, wherex, wherey)\n'))
   self.objMT_post__MetaModelElement_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__MetaModelElement_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__MetaModelElement_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__MetaModelElement_T)
   self.globalAndLocalPostcondition(self.objMT_post__MetaModelElement_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Element=ButtonConfig(self)
   self.objMT_post__Element.Contents.Text.setValue('New Element')
   self.objMT_post__Element.Contents.Image.setValue('')
   self.objMT_post__Element.Contents.lastSelected= 'Text'
   self.objMT_post__Element.Drawing_Mode.setValue(1)
   self.objMT_post__Element.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Element (self, wherex, wherey)\n'))
   self.objMT_post__Element.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Element)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Element.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Element)
   self.globalAndLocalPostcondition(self.objMT_post__Element, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__NamedElement=ButtonConfig(self)
   self.objMT_post__NamedElement.Contents.Text.setValue('New NamedElement')
   self.objMT_post__NamedElement.Contents.Image.setValue('')
   self.objMT_post__NamedElement.Contents.lastSelected= 'Text'
   self.objMT_post__NamedElement.Drawing_Mode.setValue(1)
   self.objMT_post__NamedElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__NamedElement (self, wherex, wherey)\n'))
   self.objMT_post__NamedElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__NamedElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__NamedElement.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__NamedElement)
   self.globalAndLocalPostcondition(self.objMT_post__NamedElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Trigger_S=ButtonConfig(self)
   self.objMT_post__Trigger_S.Contents.Text.setValue('New Trigger_S')
   self.objMT_post__Trigger_S.Contents.Image.setValue('')
   self.objMT_post__Trigger_S.Contents.lastSelected= 'Text'
   self.objMT_post__Trigger_S.Drawing_Mode.setValue(1)
   self.objMT_post__Trigger_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Trigger_S (self, wherex, wherey)\n'))
   self.objMT_post__Trigger_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Trigger_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Trigger_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Trigger_S)
   self.globalAndLocalPostcondition(self.objMT_post__Trigger_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Action=ButtonConfig(self)
   self.objMT_post__Action.Contents.Text.setValue('New Action')
   self.objMT_post__Action.Contents.Image.setValue('')
   self.objMT_post__Action.Contents.lastSelected= 'Text'
   self.objMT_post__Action.Drawing_Mode.setValue(1)
   self.objMT_post__Action.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Action (self, wherex, wherey)\n'))
   self.objMT_post__Action.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Action)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Action.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Action)
   self.globalAndLocalPostcondition(self.objMT_post__Action, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PortRef=ButtonConfig(self)
   self.objMT_post__PortRef.Contents.Text.setValue('New PortRef')
   self.objMT_post__PortRef.Contents.Image.setValue('')
   self.objMT_post__PortRef.Contents.lastSelected= 'Text'
   self.objMT_post__PortRef.Drawing_Mode.setValue(1)
   self.objMT_post__PortRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PortRef (self, wherex, wherey)\n'))
   self.objMT_post__PortRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__PortRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PortRef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PortRef)
   self.globalAndLocalPostcondition(self.objMT_post__PortRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PortConnectorRef=ButtonConfig(self)
   self.objMT_post__PortConnectorRef.Contents.Text.setValue('New PortConnectorRef')
   self.objMT_post__PortConnectorRef.Contents.Image.setValue('')
   self.objMT_post__PortConnectorRef.Contents.lastSelected= 'Text'
   self.objMT_post__PortConnectorRef.Drawing_Mode.setValue(1)
   self.objMT_post__PortConnectorRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PortConnectorRef (self, wherex, wherey)\n'))
   self.objMT_post__PortConnectorRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__PortConnectorRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PortConnectorRef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PortConnectorRef)
   self.globalAndLocalPostcondition(self.objMT_post__PortConnectorRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__StateMachineElement=ButtonConfig(self)
   self.objMT_post__StateMachineElement.Contents.Text.setValue('New StateMachineElement')
   self.objMT_post__StateMachineElement.Contents.Image.setValue('')
   self.objMT_post__StateMachineElement.Contents.lastSelected= 'Text'
   self.objMT_post__StateMachineElement.Drawing_Mode.setValue(1)
   self.objMT_post__StateMachineElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__StateMachineElement (self, wherex, wherey)\n'))
   self.objMT_post__StateMachineElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__StateMachineElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__StateMachineElement.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__StateMachineElement)
   self.globalAndLocalPostcondition(self.objMT_post__StateMachineElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Protocol=ButtonConfig(self)
   self.objMT_post__Protocol.Contents.Text.setValue('New Protocol')
   self.objMT_post__Protocol.Contents.Image.setValue('')
   self.objMT_post__Protocol.Contents.lastSelected= 'Text'
   self.objMT_post__Protocol.Drawing_Mode.setValue(1)
   self.objMT_post__Protocol.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Protocol (self, wherex, wherey)\n'))
   self.objMT_post__Protocol.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Protocol)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Protocol.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Protocol)
   self.globalAndLocalPostcondition(self.objMT_post__Protocol, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Signal=ButtonConfig(self)
   self.objMT_post__Signal.Contents.Text.setValue('New Signal')
   self.objMT_post__Signal.Contents.Image.setValue('')
   self.objMT_post__Signal.Contents.lastSelected= 'Text'
   self.objMT_post__Signal.Drawing_Mode.setValue(1)
   self.objMT_post__Signal.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Signal (self, wherex, wherey)\n'))
   self.objMT_post__Signal.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Signal)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Signal.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Signal)
   self.globalAndLocalPostcondition(self.objMT_post__Signal, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Port=ButtonConfig(self)
   self.objMT_post__Port.Contents.Text.setValue('New Port')
   self.objMT_post__Port.Contents.Image.setValue('')
   self.objMT_post__Port.Contents.lastSelected= 'Text'
   self.objMT_post__Port.Drawing_Mode.setValue(1)
   self.objMT_post__Port.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Port (self, wherex, wherey)\n'))
   self.objMT_post__Port.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Port)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Port.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Port)
   self.globalAndLocalPostcondition(self.objMT_post__Port, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Vertex=ButtonConfig(self)
   self.objMT_post__Vertex.Contents.Text.setValue('New Vertex')
   self.objMT_post__Vertex.Contents.Image.setValue('')
   self.objMT_post__Vertex.Contents.lastSelected= 'Text'
   self.objMT_post__Vertex.Drawing_Mode.setValue(1)
   self.objMT_post__Vertex.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Vertex (self, wherex, wherey)\n'))
   self.objMT_post__Vertex.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Vertex)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Vertex.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Vertex)
   self.globalAndLocalPostcondition(self.objMT_post__Vertex, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__InitialPoint=ButtonConfig(self)
   self.objMT_post__InitialPoint.Contents.Text.setValue('New InitialPoint')
   self.objMT_post__InitialPoint.Contents.Image.setValue('')
   self.objMT_post__InitialPoint.Contents.lastSelected= 'Text'
   self.objMT_post__InitialPoint.Drawing_Mode.setValue(1)
   self.objMT_post__InitialPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__InitialPoint (self, wherex, wherey)\n'))
   self.objMT_post__InitialPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__InitialPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__InitialPoint.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__InitialPoint)
   self.globalAndLocalPostcondition(self.objMT_post__InitialPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__EntryPoint=ButtonConfig(self)
   self.objMT_post__EntryPoint.Contents.Text.setValue('New EntryPoint')
   self.objMT_post__EntryPoint.Contents.Image.setValue('')
   self.objMT_post__EntryPoint.Contents.lastSelected= 'Text'
   self.objMT_post__EntryPoint.Drawing_Mode.setValue(1)
   self.objMT_post__EntryPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__EntryPoint (self, wherex, wherey)\n'))
   self.objMT_post__EntryPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__EntryPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__EntryPoint.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__EntryPoint)
   self.globalAndLocalPostcondition(self.objMT_post__EntryPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ExitPoint=ButtonConfig(self)
   self.objMT_post__ExitPoint.Contents.Text.setValue('New ExitPoint')
   self.objMT_post__ExitPoint.Contents.Image.setValue('')
   self.objMT_post__ExitPoint.Contents.lastSelected= 'Text'
   self.objMT_post__ExitPoint.Drawing_Mode.setValue(1)
   self.objMT_post__ExitPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ExitPoint (self, wherex, wherey)\n'))
   self.objMT_post__ExitPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__ExitPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ExitPoint.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ExitPoint)
   self.globalAndLocalPostcondition(self.objMT_post__ExitPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Transition=ButtonConfig(self)
   self.objMT_post__Transition.Contents.Text.setValue('New Transition')
   self.objMT_post__Transition.Contents.Image.setValue('')
   self.objMT_post__Transition.Contents.lastSelected= 'Text'
   self.objMT_post__Transition.Drawing_Mode.setValue(1)
   self.objMT_post__Transition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Transition (self, wherex, wherey)\n'))
   self.objMT_post__Transition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Transition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Transition.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Transition)
   self.globalAndLocalPostcondition(self.objMT_post__Transition, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__StateMachine=ButtonConfig(self)
   self.objMT_post__StateMachine.Contents.Text.setValue('New StateMachine')
   self.objMT_post__StateMachine.Contents.Image.setValue('')
   self.objMT_post__StateMachine.Contents.lastSelected= 'Text'
   self.objMT_post__StateMachine.Drawing_Mode.setValue(1)
   self.objMT_post__StateMachine.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__StateMachine (self, wherex, wherey)\n'))
   self.objMT_post__StateMachine.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__StateMachine)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__StateMachine.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__StateMachine)
   self.globalAndLocalPostcondition(self.objMT_post__StateMachine, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__State=ButtonConfig(self)
   self.objMT_post__State.Contents.Text.setValue('New State')
   self.objMT_post__State.Contents.Image.setValue('')
   self.objMT_post__State.Contents.lastSelected= 'Text'
   self.objMT_post__State.Drawing_Mode.setValue(1)
   self.objMT_post__State.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__State (self, wherex, wherey)\n'))
   self.objMT_post__State.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__State)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__State.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__State)
   self.globalAndLocalPostcondition(self.objMT_post__State, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Capsule=ButtonConfig(self)
   self.objMT_post__Capsule.Contents.Text.setValue('New Capsule')
   self.objMT_post__Capsule.Contents.Image.setValue('')
   self.objMT_post__Capsule.Contents.lastSelected= 'Text'
   self.objMT_post__Capsule.Drawing_Mode.setValue(1)
   self.objMT_post__Capsule.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Capsule (self, wherex, wherey)\n'))
   self.objMT_post__Capsule.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Capsule)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Capsule.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Capsule)
   self.globalAndLocalPostcondition(self.objMT_post__Capsule, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PackageContainer=ButtonConfig(self)
   self.objMT_post__PackageContainer.Contents.Text.setValue('New PackageContainer')
   self.objMT_post__PackageContainer.Contents.Image.setValue('')
   self.objMT_post__PackageContainer.Contents.lastSelected= 'Text'
   self.objMT_post__PackageContainer.Drawing_Mode.setValue(1)
   self.objMT_post__PackageContainer.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PackageContainer (self, wherex, wherey)\n'))
   self.objMT_post__PackageContainer.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__PackageContainer)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PackageContainer.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PackageContainer)
   self.globalAndLocalPostcondition(self.objMT_post__PackageContainer, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Model_S=ButtonConfig(self)
   self.objMT_post__Model_S.Contents.Text.setValue('New Model_S')
   self.objMT_post__Model_S.Contents.Image.setValue('')
   self.objMT_post__Model_S.Contents.lastSelected= 'Text'
   self.objMT_post__Model_S.Drawing_Mode.setValue(1)
   self.objMT_post__Model_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Model_S (self, wherex, wherey)\n'))
   self.objMT_post__Model_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Model_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Model_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Model_S)
   self.globalAndLocalPostcondition(self.objMT_post__Model_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Package=ButtonConfig(self)
   self.objMT_post__Package.Contents.Text.setValue('New Package')
   self.objMT_post__Package.Contents.Image.setValue('')
   self.objMT_post__Package.Contents.lastSelected= 'Text'
   self.objMT_post__Package.Drawing_Mode.setValue(1)
   self.objMT_post__Package.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Package (self, wherex, wherey)\n'))
   self.objMT_post__Package.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Package)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Package.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Package)
   self.globalAndLocalPostcondition(self.objMT_post__Package, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__CapsuleRole=ButtonConfig(self)
   self.objMT_post__CapsuleRole.Contents.Text.setValue('New CapsuleRole')
   self.objMT_post__CapsuleRole.Contents.Image.setValue('')
   self.objMT_post__CapsuleRole.Contents.lastSelected= 'Text'
   self.objMT_post__CapsuleRole.Drawing_Mode.setValue(1)
   self.objMT_post__CapsuleRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__CapsuleRole (self, wherex, wherey)\n'))
   self.objMT_post__CapsuleRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__CapsuleRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__CapsuleRole.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__CapsuleRole)
   self.globalAndLocalPostcondition(self.objMT_post__CapsuleRole, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PortConnector=ButtonConfig(self)
   self.objMT_post__PortConnector.Contents.Text.setValue('New PortConnector')
   self.objMT_post__PortConnector.Contents.Image.setValue('')
   self.objMT_post__PortConnector.Contents.lastSelected= 'Text'
   self.objMT_post__PortConnector.Drawing_Mode.setValue(1)
   self.objMT_post__PortConnector.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PortConnector (self, wherex, wherey)\n'))
   self.objMT_post__PortConnector.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__PortConnector)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PortConnector.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PortConnector)
   self.globalAndLocalPostcondition(self.objMT_post__PortConnector, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Thread=ButtonConfig(self)
   self.objMT_post__Thread.Contents.Text.setValue('New Thread')
   self.objMT_post__Thread.Contents.Image.setValue('')
   self.objMT_post__Thread.Contents.lastSelected= 'Text'
   self.objMT_post__Thread.Drawing_Mode.setValue(1)
   self.objMT_post__Thread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Thread (self, wherex, wherey)\n'))
   self.objMT_post__Thread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Thread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Thread.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Thread)
   self.globalAndLocalPostcondition(self.objMT_post__Thread, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PhysicalThread=ButtonConfig(self)
   self.objMT_post__PhysicalThread.Contents.Text.setValue('New PhysicalThread')
   self.objMT_post__PhysicalThread.Contents.Image.setValue('')
   self.objMT_post__PhysicalThread.Contents.lastSelected= 'Text'
   self.objMT_post__PhysicalThread.Drawing_Mode.setValue(1)
   self.objMT_post__PhysicalThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PhysicalThread (self, wherex, wherey)\n'))
   self.objMT_post__PhysicalThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__PhysicalThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PhysicalThread.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PhysicalThread)
   self.globalAndLocalPostcondition(self.objMT_post__PhysicalThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__LogicalThread=ButtonConfig(self)
   self.objMT_post__LogicalThread.Contents.Text.setValue('New LogicalThread')
   self.objMT_post__LogicalThread.Contents.Image.setValue('')
   self.objMT_post__LogicalThread.Contents.lastSelected= 'Text'
   self.objMT_post__LogicalThread.Drawing_Mode.setValue(1)
   self.objMT_post__LogicalThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__LogicalThread (self, wherex, wherey)\n'))
   self.objMT_post__LogicalThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__LogicalThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__LogicalThread.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__LogicalThread)
   self.globalAndLocalPostcondition(self.objMT_post__LogicalThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PortType=ButtonConfig(self)
   self.objMT_post__PortType.Contents.Text.setValue('New PortType')
   self.objMT_post__PortType.Contents.Image.setValue('')
   self.objMT_post__PortType.Contents.lastSelected= 'Text'
   self.objMT_post__PortType.Drawing_Mode.setValue(1)
   self.objMT_post__PortType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PortType (self, wherex, wherey)\n'))
   self.objMT_post__PortType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__PortType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PortType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PortType)
   self.globalAndLocalPostcondition(self.objMT_post__PortType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__BASE0=ButtonConfig(self)
   self.objMT_post__BASE0.Contents.Text.setValue('New BASE0')
   self.objMT_post__BASE0.Contents.Image.setValue('')
   self.objMT_post__BASE0.Contents.lastSelected= 'Text'
   self.objMT_post__BASE0.Drawing_Mode.setValue(1)
   self.objMT_post__BASE0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__BASE0 (self, wherex, wherey)\n'))
   self.objMT_post__BASE0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__BASE0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__BASE0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__BASE0)
   self.globalAndLocalPostcondition(self.objMT_post__BASE0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__CONJUGATE1=ButtonConfig(self)
   self.objMT_post__CONJUGATE1.Contents.Text.setValue('New CONJUGATE1')
   self.objMT_post__CONJUGATE1.Contents.Image.setValue('')
   self.objMT_post__CONJUGATE1.Contents.lastSelected= 'Text'
   self.objMT_post__CONJUGATE1.Drawing_Mode.setValue(1)
   self.objMT_post__CONJUGATE1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__CONJUGATE1 (self, wherex, wherey)\n'))
   self.objMT_post__CONJUGATE1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__CONJUGATE1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__CONJUGATE1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__CONJUGATE1)
   self.globalAndLocalPostcondition(self.objMT_post__CONJUGATE1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__SignalType=ButtonConfig(self)
   self.objMT_post__SignalType.Contents.Text.setValue('New SignalType')
   self.objMT_post__SignalType.Contents.Image.setValue('')
   self.objMT_post__SignalType.Contents.lastSelected= 'Text'
   self.objMT_post__SignalType.Drawing_Mode.setValue(1)
   self.objMT_post__SignalType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__SignalType (self, wherex, wherey)\n'))
   self.objMT_post__SignalType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__SignalType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__SignalType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__SignalType)
   self.globalAndLocalPostcondition(self.objMT_post__SignalType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__OUT1=ButtonConfig(self)
   self.objMT_post__OUT1.Contents.Text.setValue('New OUT1')
   self.objMT_post__OUT1.Contents.Image.setValue('')
   self.objMT_post__OUT1.Contents.lastSelected= 'Text'
   self.objMT_post__OUT1.Drawing_Mode.setValue(1)
   self.objMT_post__OUT1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__OUT1 (self, wherex, wherey)\n'))
   self.objMT_post__OUT1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__OUT1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__OUT1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__OUT1)
   self.globalAndLocalPostcondition(self.objMT_post__OUT1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__IN0=ButtonConfig(self)
   self.objMT_post__IN0.Contents.Text.setValue('New IN0')
   self.objMT_post__IN0.Contents.Image.setValue('')
   self.objMT_post__IN0.Contents.lastSelected= 'Text'
   self.objMT_post__IN0.Drawing_Mode.setValue(1)
   self.objMT_post__IN0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__IN0 (self, wherex, wherey)\n'))
   self.objMT_post__IN0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__IN0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__IN0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__IN0)
   self.globalAndLocalPostcondition(self.objMT_post__IN0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__RoleType=ButtonConfig(self)
   self.objMT_post__RoleType.Contents.Text.setValue('New RoleType')
   self.objMT_post__RoleType.Contents.Image.setValue('')
   self.objMT_post__RoleType.Contents.lastSelected= 'Text'
   self.objMT_post__RoleType.Drawing_Mode.setValue(1)
   self.objMT_post__RoleType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__RoleType (self, wherex, wherey)\n'))
   self.objMT_post__RoleType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__RoleType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__RoleType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__RoleType)
   self.globalAndLocalPostcondition(self.objMT_post__RoleType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__FIXED0=ButtonConfig(self)
   self.objMT_post__FIXED0.Contents.Text.setValue('New FIXED0')
   self.objMT_post__FIXED0.Contents.Image.setValue('')
   self.objMT_post__FIXED0.Contents.lastSelected= 'Text'
   self.objMT_post__FIXED0.Drawing_Mode.setValue(1)
   self.objMT_post__FIXED0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__FIXED0 (self, wherex, wherey)\n'))
   self.objMT_post__FIXED0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__FIXED0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__FIXED0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__FIXED0)
   self.globalAndLocalPostcondition(self.objMT_post__FIXED0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__OPTIONAL1=ButtonConfig(self)
   self.objMT_post__OPTIONAL1.Contents.Text.setValue('New OPTIONAL1')
   self.objMT_post__OPTIONAL1.Contents.Image.setValue('')
   self.objMT_post__OPTIONAL1.Contents.lastSelected= 'Text'
   self.objMT_post__OPTIONAL1.Drawing_Mode.setValue(1)
   self.objMT_post__OPTIONAL1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__OPTIONAL1 (self, wherex, wherey)\n'))
   self.objMT_post__OPTIONAL1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__OPTIONAL1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__OPTIONAL1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__OPTIONAL1)
   self.globalAndLocalPostcondition(self.objMT_post__OPTIONAL1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PLUGIN2=ButtonConfig(self)
   self.objMT_post__PLUGIN2.Contents.Text.setValue('New PLUGIN2')
   self.objMT_post__PLUGIN2.Contents.Image.setValue('')
   self.objMT_post__PLUGIN2.Contents.lastSelected= 'Text'
   self.objMT_post__PLUGIN2.Drawing_Mode.setValue(1)
   self.objMT_post__PLUGIN2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PLUGIN2 (self, wherex, wherey)\n'))
   self.objMT_post__PLUGIN2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__PLUGIN2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PLUGIN2.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PLUGIN2)
   self.globalAndLocalPostcondition(self.objMT_post__PLUGIN2, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__TransitionType=ButtonConfig(self)
   self.objMT_post__TransitionType.Contents.Text.setValue('New TransitionType')
   self.objMT_post__TransitionType.Contents.Image.setValue('')
   self.objMT_post__TransitionType.Contents.lastSelected= 'Text'
   self.objMT_post__TransitionType.Drawing_Mode.setValue(1)
   self.objMT_post__TransitionType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__TransitionType (self, wherex, wherey)\n'))
   self.objMT_post__TransitionType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__TransitionType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__TransitionType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__TransitionType)
   self.globalAndLocalPostcondition(self.objMT_post__TransitionType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__SIBLING0=ButtonConfig(self)
   self.objMT_post__SIBLING0.Contents.Text.setValue('New SIBLING0')
   self.objMT_post__SIBLING0.Contents.Image.setValue('')
   self.objMT_post__SIBLING0.Contents.lastSelected= 'Text'
   self.objMT_post__SIBLING0.Drawing_Mode.setValue(1)
   self.objMT_post__SIBLING0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__SIBLING0 (self, wherex, wherey)\n'))
   self.objMT_post__SIBLING0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__SIBLING0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__SIBLING0.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__SIBLING0)
   self.globalAndLocalPostcondition(self.objMT_post__SIBLING0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__IN1=ButtonConfig(self)
   self.objMT_post__IN1.Contents.Text.setValue('New IN1')
   self.objMT_post__IN1.Contents.Image.setValue('')
   self.objMT_post__IN1.Contents.lastSelected= 'Text'
   self.objMT_post__IN1.Drawing_Mode.setValue(1)
   self.objMT_post__IN1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__IN1 (self, wherex, wherey)\n'))
   self.objMT_post__IN1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__IN1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__IN1.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__IN1)
   self.globalAndLocalPostcondition(self.objMT_post__IN1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__OUT2=ButtonConfig(self)
   self.objMT_post__OUT2.Contents.Text.setValue('New OUT2')
   self.objMT_post__OUT2.Contents.Image.setValue('')
   self.objMT_post__OUT2.Contents.lastSelected= 'Text'
   self.objMT_post__OUT2.Drawing_Mode.setValue(1)
   self.objMT_post__OUT2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__OUT2 (self, wherex, wherey)\n'))
   self.objMT_post__OUT2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__OUT2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__OUT2.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__OUT2)
   self.globalAndLocalPostcondition(self.objMT_post__OUT2, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Def=ButtonConfig(self)
   self.objMT_post__Def.Contents.Text.setValue('New Def')
   self.objMT_post__Def.Contents.Image.setValue('')
   self.objMT_post__Def.Contents.lastSelected= 'Text'
   self.objMT_post__Def.Drawing_Mode.setValue(1)
   self.objMT_post__Def.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Def (self, wherex, wherey)\n'))
   self.objMT_post__Def.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Def)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Def.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Def)
   self.globalAndLocalPostcondition(self.objMT_post__Def, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Expr=ButtonConfig(self)
   self.objMT_post__Expr.Contents.Text.setValue('New Expr')
   self.objMT_post__Expr.Contents.Image.setValue('')
   self.objMT_post__Expr.Contents.lastSelected= 'Text'
   self.objMT_post__Expr.Drawing_Mode.setValue(1)
   self.objMT_post__Expr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Expr (self, wherex, wherey)\n'))
   self.objMT_post__Expr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Expr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Expr.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Expr)
   self.globalAndLocalPostcondition(self.objMT_post__Expr, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Pattern=ButtonConfig(self)
   self.objMT_post__Pattern.Contents.Text.setValue('New Pattern')
   self.objMT_post__Pattern.Contents.Image.setValue('')
   self.objMT_post__Pattern.Contents.lastSelected= 'Text'
   self.objMT_post__Pattern.Drawing_Mode.setValue(1)
   self.objMT_post__Pattern.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Pattern (self, wherex, wherey)\n'))
   self.objMT_post__Pattern.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Pattern)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Pattern.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Pattern)
   self.globalAndLocalPostcondition(self.objMT_post__Pattern, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Proc=ButtonConfig(self)
   self.objMT_post__Proc.Contents.Text.setValue('New Proc')
   self.objMT_post__Proc.Contents.Image.setValue('')
   self.objMT_post__Proc.Contents.lastSelected= 'Text'
   self.objMT_post__Proc.Drawing_Mode.setValue(1)
   self.objMT_post__Proc.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Proc (self, wherex, wherey)\n'))
   self.objMT_post__Proc.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Proc)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Proc.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Proc)
   self.globalAndLocalPostcondition(self.objMT_post__Proc, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ProcDef=ButtonConfig(self)
   self.objMT_post__ProcDef.Contents.Text.setValue('New ProcDef')
   self.objMT_post__ProcDef.Contents.Image.setValue('')
   self.objMT_post__ProcDef.Contents.lastSelected= 'Text'
   self.objMT_post__ProcDef.Drawing_Mode.setValue(1)
   self.objMT_post__ProcDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ProcDef (self, wherex, wherey)\n'))
   self.objMT_post__ProcDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__ProcDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ProcDef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ProcDef)
   self.globalAndLocalPostcondition(self.objMT_post__ProcDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__FuncDef=ButtonConfig(self)
   self.objMT_post__FuncDef.Contents.Text.setValue('New FuncDef')
   self.objMT_post__FuncDef.Contents.Image.setValue('')
   self.objMT_post__FuncDef.Contents.lastSelected= 'Text'
   self.objMT_post__FuncDef.Drawing_Mode.setValue(1)
   self.objMT_post__FuncDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__FuncDef (self, wherex, wherey)\n'))
   self.objMT_post__FuncDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__FuncDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__FuncDef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__FuncDef)
   self.globalAndLocalPostcondition(self.objMT_post__FuncDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Name=ButtonConfig(self)
   self.objMT_post__Name.Contents.Text.setValue('New Name')
   self.objMT_post__Name.Contents.Image.setValue('')
   self.objMT_post__Name.Contents.lastSelected= 'Text'
   self.objMT_post__Name.Drawing_Mode.setValue(1)
   self.objMT_post__Name.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Name (self, wherex, wherey)\n'))
   self.objMT_post__Name.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Name)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Name.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Name)
   self.globalAndLocalPostcondition(self.objMT_post__Name, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PythonRef=ButtonConfig(self)
   self.objMT_post__PythonRef.Contents.Text.setValue('New PythonRef')
   self.objMT_post__PythonRef.Contents.Image.setValue('')
   self.objMT_post__PythonRef.Contents.lastSelected= 'Text'
   self.objMT_post__PythonRef.Drawing_Mode.setValue(1)
   self.objMT_post__PythonRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PythonRef (self, wherex, wherey)\n'))
   self.objMT_post__PythonRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__PythonRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PythonRef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PythonRef)
   self.globalAndLocalPostcondition(self.objMT_post__PythonRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Module=ButtonConfig(self)
   self.objMT_post__Module.Contents.Text.setValue('New Module')
   self.objMT_post__Module.Contents.Image.setValue('')
   self.objMT_post__Module.Contents.lastSelected= 'Text'
   self.objMT_post__Module.Drawing_Mode.setValue(1)
   self.objMT_post__Module.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Module (self, wherex, wherey)\n'))
   self.objMT_post__Module.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Module)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Module.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Module)
   self.globalAndLocalPostcondition(self.objMT_post__Module, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Null=ButtonConfig(self)
   self.objMT_post__Null.Contents.Text.setValue('New Null')
   self.objMT_post__Null.Contents.Image.setValue('')
   self.objMT_post__Null.Contents.lastSelected= 'Text'
   self.objMT_post__Null.Drawing_Mode.setValue(1)
   self.objMT_post__Null.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Null (self, wherex, wherey)\n'))
   self.objMT_post__Null.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Null)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Null.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Null)
   self.globalAndLocalPostcondition(self.objMT_post__Null, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Trigger_T=ButtonConfig(self)
   self.objMT_post__Trigger_T.Contents.Text.setValue('New Trigger_T')
   self.objMT_post__Trigger_T.Contents.Image.setValue('')
   self.objMT_post__Trigger_T.Contents.lastSelected= 'Text'
   self.objMT_post__Trigger_T.Drawing_Mode.setValue(1)
   self.objMT_post__Trigger_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Trigger_T (self, wherex, wherey)\n'))
   self.objMT_post__Trigger_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Trigger_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Trigger_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Trigger_T)
   self.globalAndLocalPostcondition(self.objMT_post__Trigger_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Listen=ButtonConfig(self)
   self.objMT_post__Listen.Contents.Text.setValue('New Listen')
   self.objMT_post__Listen.Contents.Image.setValue('')
   self.objMT_post__Listen.Contents.lastSelected= 'Text'
   self.objMT_post__Listen.Drawing_Mode.setValue(1)
   self.objMT_post__Listen.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Listen (self, wherex, wherey)\n'))
   self.objMT_post__Listen.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Listen)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Listen.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Listen)
   self.globalAndLocalPostcondition(self.objMT_post__Listen, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ConditionBranch=ButtonConfig(self)
   self.objMT_post__ConditionBranch.Contents.Text.setValue('New ConditionBranch')
   self.objMT_post__ConditionBranch.Contents.Image.setValue('')
   self.objMT_post__ConditionBranch.Contents.lastSelected= 'Text'
   self.objMT_post__ConditionBranch.Drawing_Mode.setValue(1)
   self.objMT_post__ConditionBranch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ConditionBranch (self, wherex, wherey)\n'))
   self.objMT_post__ConditionBranch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__ConditionBranch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ConditionBranch.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ConditionBranch)
   self.globalAndLocalPostcondition(self.objMT_post__ConditionBranch, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ListenBranch=ButtonConfig(self)
   self.objMT_post__ListenBranch.Contents.Text.setValue('New ListenBranch')
   self.objMT_post__ListenBranch.Contents.Image.setValue('')
   self.objMT_post__ListenBranch.Contents.lastSelected= 'Text'
   self.objMT_post__ListenBranch.Drawing_Mode.setValue(1)
   self.objMT_post__ListenBranch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ListenBranch (self, wherex, wherey)\n'))
   self.objMT_post__ListenBranch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__ListenBranch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ListenBranch.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ListenBranch)
   self.globalAndLocalPostcondition(self.objMT_post__ListenBranch, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Site=ButtonConfig(self)
   self.objMT_post__Site.Contents.Text.setValue('New Site')
   self.objMT_post__Site.Contents.Image.setValue('')
   self.objMT_post__Site.Contents.lastSelected= 'Text'
   self.objMT_post__Site.Drawing_Mode.setValue(1)
   self.objMT_post__Site.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Site (self, wherex, wherey)\n'))
   self.objMT_post__Site.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Site)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Site.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Site)
   self.globalAndLocalPostcondition(self.objMT_post__Site, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Model_T=ButtonConfig(self)
   self.objMT_post__Model_T.Contents.Text.setValue('New Model_T')
   self.objMT_post__Model_T.Contents.Image.setValue('')
   self.objMT_post__Model_T.Contents.lastSelected= 'Text'
   self.objMT_post__Model_T.Drawing_Mode.setValue(1)
   self.objMT_post__Model_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Model_T (self, wherex, wherey)\n'))
   self.objMT_post__Model_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Model_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Model_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Model_T)
   self.globalAndLocalPostcondition(self.objMT_post__Model_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__MatchCase=ButtonConfig(self)
   self.objMT_post__MatchCase.Contents.Text.setValue('New MatchCase')
   self.objMT_post__MatchCase.Contents.Image.setValue('')
   self.objMT_post__MatchCase.Contents.lastSelected= 'Text'
   self.objMT_post__MatchCase.Drawing_Mode.setValue(1)
   self.objMT_post__MatchCase.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__MatchCase (self, wherex, wherey)\n'))
   self.objMT_post__MatchCase.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__MatchCase)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__MatchCase.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__MatchCase)
   self.globalAndLocalPostcondition(self.objMT_post__MatchCase, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Condition=ButtonConfig(self)
   self.objMT_post__Condition.Contents.Text.setValue('New Condition')
   self.objMT_post__Condition.Contents.Image.setValue('')
   self.objMT_post__Condition.Contents.lastSelected= 'Text'
   self.objMT_post__Condition.Drawing_Mode.setValue(1)
   self.objMT_post__Condition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Condition (self, wherex, wherey)\n'))
   self.objMT_post__Condition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Condition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Condition.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Condition)
   self.globalAndLocalPostcondition(self.objMT_post__Condition, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__New=ButtonConfig(self)
   self.objMT_post__New.Contents.Text.setValue('New New')
   self.objMT_post__New.Contents.Image.setValue('')
   self.objMT_post__New.Contents.lastSelected= 'Text'
   self.objMT_post__New.Drawing_Mode.setValue(1)
   self.objMT_post__New.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__New (self, wherex, wherey)\n'))
   self.objMT_post__New.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__New)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__New.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__New)
   self.globalAndLocalPostcondition(self.objMT_post__New, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Delay=ButtonConfig(self)
   self.objMT_post__Delay.Contents.Text.setValue('New Delay')
   self.objMT_post__Delay.Contents.Image.setValue('')
   self.objMT_post__Delay.Contents.lastSelected= 'Text'
   self.objMT_post__Delay.Drawing_Mode.setValue(1)
   self.objMT_post__Delay.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Delay (self, wherex, wherey)\n'))
   self.objMT_post__Delay.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Delay)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Delay.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Delay)
   self.globalAndLocalPostcondition(self.objMT_post__Delay, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Par=ButtonConfig(self)
   self.objMT_post__Par.Contents.Text.setValue('New Par')
   self.objMT_post__Par.Contents.Image.setValue('')
   self.objMT_post__Par.Contents.lastSelected= 'Text'
   self.objMT_post__Par.Drawing_Mode.setValue(1)
   self.objMT_post__Par.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Par (self, wherex, wherey)\n'))
   self.objMT_post__Par.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Par)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Par.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Par)
   self.globalAndLocalPostcondition(self.objMT_post__Par, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ParIndexed=ButtonConfig(self)
   self.objMT_post__ParIndexed.Contents.Text.setValue('New ParIndexed')
   self.objMT_post__ParIndexed.Contents.Image.setValue('')
   self.objMT_post__ParIndexed.Contents.lastSelected= 'Text'
   self.objMT_post__ParIndexed.Drawing_Mode.setValue(1)
   self.objMT_post__ParIndexed.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ParIndexed (self, wherex, wherey)\n'))
   self.objMT_post__ParIndexed.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__ParIndexed)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ParIndexed.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ParIndexed)
   self.globalAndLocalPostcondition(self.objMT_post__ParIndexed, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Inst=ButtonConfig(self)
   self.objMT_post__Inst.Contents.Text.setValue('New Inst')
   self.objMT_post__Inst.Contents.Image.setValue('')
   self.objMT_post__Inst.Contents.lastSelected= 'Text'
   self.objMT_post__Inst.Drawing_Mode.setValue(1)
   self.objMT_post__Inst.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Inst (self, wherex, wherey)\n'))
   self.objMT_post__Inst.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Inst)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Inst.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Inst)
   self.globalAndLocalPostcondition(self.objMT_post__Inst, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__LocalDef=ButtonConfig(self)
   self.objMT_post__LocalDef.Contents.Text.setValue('New LocalDef')
   self.objMT_post__LocalDef.Contents.Image.setValue('')
   self.objMT_post__LocalDef.Contents.lastSelected= 'Text'
   self.objMT_post__LocalDef.Drawing_Mode.setValue(1)
   self.objMT_post__LocalDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__LocalDef (self, wherex, wherey)\n'))
   self.objMT_post__LocalDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__LocalDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__LocalDef.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__LocalDef)
   self.globalAndLocalPostcondition(self.objMT_post__LocalDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Seq=ButtonConfig(self)
   self.objMT_post__Seq.Contents.Text.setValue('New Seq')
   self.objMT_post__Seq.Contents.Image.setValue('')
   self.objMT_post__Seq.Contents.lastSelected= 'Text'
   self.objMT_post__Seq.Drawing_Mode.setValue(1)
   self.objMT_post__Seq.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Seq (self, wherex, wherey)\n'))
   self.objMT_post__Seq.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Seq)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Seq.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Seq)
   self.globalAndLocalPostcondition(self.objMT_post__Seq, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ConditionSet=ButtonConfig(self)
   self.objMT_post__ConditionSet.Contents.Text.setValue('New ConditionSet')
   self.objMT_post__ConditionSet.Contents.Image.setValue('')
   self.objMT_post__ConditionSet.Contents.lastSelected= 'Text'
   self.objMT_post__ConditionSet.Drawing_Mode.setValue(1)
   self.objMT_post__ConditionSet.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ConditionSet (self, wherex, wherey)\n'))
   self.objMT_post__ConditionSet.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__ConditionSet)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ConditionSet.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ConditionSet)
   self.globalAndLocalPostcondition(self.objMT_post__ConditionSet, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Match=ButtonConfig(self)
   self.objMT_post__Match.Contents.Text.setValue('New Match')
   self.objMT_post__Match.Contents.Image.setValue('')
   self.objMT_post__Match.Contents.lastSelected= 'Text'
   self.objMT_post__Match.Drawing_Mode.setValue(1)
   self.objMT_post__Match.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Match (self, wherex, wherey)\n'))
   self.objMT_post__Match.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Match)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Match.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Match)
   self.globalAndLocalPostcondition(self.objMT_post__Match, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Print=ButtonConfig(self)
   self.objMT_post__Print.Contents.Text.setValue('New Print')
   self.objMT_post__Print.Contents.Image.setValue('')
   self.objMT_post__Print.Contents.lastSelected= 'Text'
   self.objMT_post__Print.Drawing_Mode.setValue(1)
   self.objMT_post__Print.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Print (self, wherex, wherey)\n'))
   self.objMT_post__Print.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Print)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Print.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Print)
   self.globalAndLocalPostcondition(self.objMT_post__Print, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Attribute=ButtonConfig(self)
   self.objMT_post__Attribute.Contents.Text.setValue('New Attribute')
   self.objMT_post__Attribute.Contents.Image.setValue('')
   self.objMT_post__Attribute.Contents.lastSelected= 'Text'
   self.objMT_post__Attribute.Drawing_Mode.setValue(1)
   self.objMT_post__Attribute.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Attribute (self, wherex, wherey)\n'))
   self.objMT_post__Attribute.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Attribute)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Attribute.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Attribute)
   self.globalAndLocalPostcondition(self.objMT_post__Attribute, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Expression=ButtonConfig(self)
   self.objMT_post__Expression.Contents.Text.setValue('New Expression')
   self.objMT_post__Expression.Contents.Image.setValue('')
   self.objMT_post__Expression.Contents.lastSelected= 'Text'
   self.objMT_post__Expression.Drawing_Mode.setValue(1)
   self.objMT_post__Expression.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Expression (self, wherex, wherey)\n'))
   self.objMT_post__Expression.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Expression)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Expression.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Expression)
   self.globalAndLocalPostcondition(self.objMT_post__Expression, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Equation=ButtonConfig(self)
   self.objMT_post__Equation.Contents.Text.setValue('New Equation')
   self.objMT_post__Equation.Contents.Image.setValue('')
   self.objMT_post__Equation.Contents.lastSelected= 'Text'
   self.objMT_post__Equation.Drawing_Mode.setValue(1)
   self.objMT_post__Equation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Equation (self, wherex, wherey)\n'))
   self.objMT_post__Equation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Equation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Equation.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Equation)
   self.globalAndLocalPostcondition(self.objMT_post__Equation, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Operation=ButtonConfig(self)
   self.objMT_post__Operation.Contents.Text.setValue('New Operation')
   self.objMT_post__Operation.Contents.Image.setValue('')
   self.objMT_post__Operation.Contents.lastSelected= 'Text'
   self.objMT_post__Operation.Drawing_Mode.setValue(1)
   self.objMT_post__Operation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Operation (self, wherex, wherey)\n'))
   self.objMT_post__Operation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Operation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Operation.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Operation)
   self.globalAndLocalPostcondition(self.objMT_post__Operation, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Add=ButtonConfig(self)
   self.objMT_post__Add.Contents.Text.setValue('New Add')
   self.objMT_post__Add.Contents.Image.setValue('')
   self.objMT_post__Add.Contents.lastSelected= 'Text'
   self.objMT_post__Add.Drawing_Mode.setValue(1)
   self.objMT_post__Add.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Add (self, wherex, wherey)\n'))
   self.objMT_post__Add.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Add)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Add.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Add)
   self.globalAndLocalPostcondition(self.objMT_post__Add, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Subtract=ButtonConfig(self)
   self.objMT_post__Subtract.Contents.Text.setValue('New Subtract')
   self.objMT_post__Subtract.Contents.Image.setValue('')
   self.objMT_post__Subtract.Contents.lastSelected= 'Text'
   self.objMT_post__Subtract.Drawing_Mode.setValue(1)
   self.objMT_post__Subtract.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Subtract (self, wherex, wherey)\n'))
   self.objMT_post__Subtract.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Subtract)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Subtract.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Subtract)
   self.globalAndLocalPostcondition(self.objMT_post__Subtract, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Concat=ButtonConfig(self)
   self.objMT_post__Concat.Contents.Text.setValue('New Concat')
   self.objMT_post__Concat.Contents.Image.setValue('')
   self.objMT_post__Concat.Contents.lastSelected= 'Text'
   self.objMT_post__Concat.Drawing_Mode.setValue(1)
   self.objMT_post__Concat.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Concat (self, wherex, wherey)\n'))
   self.objMT_post__Concat.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Concat)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Concat.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Concat)
   self.globalAndLocalPostcondition(self.objMT_post__Concat, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Constant=ButtonConfig(self)
   self.objMT_post__Constant.Contents.Text.setValue('New Constant')
   self.objMT_post__Constant.Contents.Image.setValue('')
   self.objMT_post__Constant.Contents.lastSelected= 'Text'
   self.objMT_post__Constant.Drawing_Mode.setValue(1)
   self.objMT_post__Constant.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Constant (self, wherex, wherey)\n'))
   self.objMT_post__Constant.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Constant)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Constant.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Constant)
   self.globalAndLocalPostcondition(self.objMT_post__Constant, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__GenericNode_UMLRT2Kiltera_MM=ButtonConfig(self)
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.Contents.Text.setValue('New GenericNode')
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.Contents.Image.setValue('')
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.Contents.lastSelected= 'Text'
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.Drawing_Mode.setValue(1)
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__GenericNode_UMLRT2Kiltera_MM (self, wherex, wherey)\n'))
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__GenericNode_UMLRT2Kiltera_MM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__GenericNode_UMLRT2Kiltera_MM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__GenericNode_UMLRT2Kiltera_MM)
   self.globalAndLocalPostcondition(self.objMT_post__GenericNode_UMLRT2Kiltera_MM, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__paired_with=ButtonConfig(self)
   self.objMT_post__paired_with.Contents.Text.setValue('New paired_with')
   self.objMT_post__paired_with.Contents.Image.setValue('')
   self.objMT_post__paired_with.Contents.lastSelected= 'Text'
   self.objMT_post__paired_with.Drawing_Mode.setValue(1)
   self.objMT_post__paired_with.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__paired_with (self, wherex, wherey)\n'))
   self.objMT_post__paired_with.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__paired_with)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__paired_with.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__paired_with)
   self.globalAndLocalPostcondition(self.objMT_post__paired_with, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__match_contains=ButtonConfig(self)
   self.objMT_post__match_contains.Contents.Text.setValue('New match_contains')
   self.objMT_post__match_contains.Contents.Image.setValue('')
   self.objMT_post__match_contains.Contents.lastSelected= 'Text'
   self.objMT_post__match_contains.Drawing_Mode.setValue(1)
   self.objMT_post__match_contains.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__match_contains (self, wherex, wherey)\n'))
   self.objMT_post__match_contains.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__match_contains)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__match_contains.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__match_contains)
   self.globalAndLocalPostcondition(self.objMT_post__match_contains, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__apply_contains=ButtonConfig(self)
   self.objMT_post__apply_contains.Contents.Text.setValue('New apply_contains')
   self.objMT_post__apply_contains.Contents.Image.setValue('')
   self.objMT_post__apply_contains.Contents.lastSelected= 'Text'
   self.objMT_post__apply_contains.Drawing_Mode.setValue(1)
   self.objMT_post__apply_contains.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__apply_contains (self, wherex, wherey)\n'))
   self.objMT_post__apply_contains.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__apply_contains)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__apply_contains.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__apply_contains)
   self.globalAndLocalPostcondition(self.objMT_post__apply_contains, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__directLink_T=ButtonConfig(self)
   self.objMT_post__directLink_T.Contents.Text.setValue('New directLink_T')
   self.objMT_post__directLink_T.Contents.Image.setValue('')
   self.objMT_post__directLink_T.Contents.lastSelected= 'Text'
   self.objMT_post__directLink_T.Drawing_Mode.setValue(1)
   self.objMT_post__directLink_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__directLink_T (self, wherex, wherey)\n'))
   self.objMT_post__directLink_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__directLink_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__directLink_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__directLink_T)
   self.globalAndLocalPostcondition(self.objMT_post__directLink_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__directLink_S=ButtonConfig(self)
   self.objMT_post__directLink_S.Contents.Text.setValue('New directLink_S')
   self.objMT_post__directLink_S.Contents.Image.setValue('')
   self.objMT_post__directLink_S.Contents.lastSelected= 'Text'
   self.objMT_post__directLink_S.Drawing_Mode.setValue(1)
   self.objMT_post__directLink_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__directLink_S (self, wherex, wherey)\n'))
   self.objMT_post__directLink_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__directLink_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__directLink_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__directLink_S)
   self.globalAndLocalPostcondition(self.objMT_post__directLink_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__indirectLink_S=ButtonConfig(self)
   self.objMT_post__indirectLink_S.Contents.Text.setValue('New indirectLink_S')
   self.objMT_post__indirectLink_S.Contents.Image.setValue('')
   self.objMT_post__indirectLink_S.Contents.lastSelected= 'Text'
   self.objMT_post__indirectLink_S.Drawing_Mode.setValue(1)
   self.objMT_post__indirectLink_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__indirectLink_S (self, wherex, wherey)\n'))
   self.objMT_post__indirectLink_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__indirectLink_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__indirectLink_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__indirectLink_S)
   self.globalAndLocalPostcondition(self.objMT_post__indirectLink_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__backward_link=ButtonConfig(self)
   self.objMT_post__backward_link.Contents.Text.setValue('New backward_link')
   self.objMT_post__backward_link.Contents.Image.setValue('')
   self.objMT_post__backward_link.Contents.lastSelected= 'Text'
   self.objMT_post__backward_link.Drawing_Mode.setValue(1)
   self.objMT_post__backward_link.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__backward_link (self, wherex, wherey)\n'))
   self.objMT_post__backward_link.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__backward_link)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__backward_link.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__backward_link)
   self.globalAndLocalPostcondition(self.objMT_post__backward_link, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__trace_link=ButtonConfig(self)
   self.objMT_post__trace_link.Contents.Text.setValue('New trace_link')
   self.objMT_post__trace_link.Contents.Image.setValue('')
   self.objMT_post__trace_link.Contents.lastSelected= 'Text'
   self.objMT_post__trace_link.Drawing_Mode.setValue(1)
   self.objMT_post__trace_link.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__trace_link (self, wherex, wherey)\n'))
   self.objMT_post__trace_link.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__trace_link)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__trace_link.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__trace_link)
   self.globalAndLocalPostcondition(self.objMT_post__trace_link, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__hasAttribute_S=ButtonConfig(self)
   self.objMT_post__hasAttribute_S.Contents.Text.setValue('New hasAttribute_S')
   self.objMT_post__hasAttribute_S.Contents.Image.setValue('')
   self.objMT_post__hasAttribute_S.Contents.lastSelected= 'Text'
   self.objMT_post__hasAttribute_S.Drawing_Mode.setValue(1)
   self.objMT_post__hasAttribute_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__hasAttribute_S (self, wherex, wherey)\n'))
   self.objMT_post__hasAttribute_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__hasAttribute_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__hasAttribute_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__hasAttribute_S)
   self.globalAndLocalPostcondition(self.objMT_post__hasAttribute_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__hasAttribute_T=ButtonConfig(self)
   self.objMT_post__hasAttribute_T.Contents.Text.setValue('New hasAttribute_T')
   self.objMT_post__hasAttribute_T.Contents.Image.setValue('')
   self.objMT_post__hasAttribute_T.Contents.lastSelected= 'Text'
   self.objMT_post__hasAttribute_T.Drawing_Mode.setValue(1)
   self.objMT_post__hasAttribute_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__hasAttribute_T (self, wherex, wherey)\n'))
   self.objMT_post__hasAttribute_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__hasAttribute_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__hasAttribute_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__hasAttribute_T)
   self.globalAndLocalPostcondition(self.objMT_post__hasAttribute_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__leftExpr=ButtonConfig(self)
   self.objMT_post__leftExpr.Contents.Text.setValue('New leftExpr')
   self.objMT_post__leftExpr.Contents.Image.setValue('')
   self.objMT_post__leftExpr.Contents.lastSelected= 'Text'
   self.objMT_post__leftExpr.Drawing_Mode.setValue(1)
   self.objMT_post__leftExpr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__leftExpr (self, wherex, wherey)\n'))
   self.objMT_post__leftExpr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__leftExpr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__leftExpr.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__leftExpr)
   self.globalAndLocalPostcondition(self.objMT_post__leftExpr, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__rightExpr=ButtonConfig(self)
   self.objMT_post__rightExpr.Contents.Text.setValue('New rightExpr')
   self.objMT_post__rightExpr.Contents.Image.setValue('')
   self.objMT_post__rightExpr.Contents.lastSelected= 'Text'
   self.objMT_post__rightExpr.Drawing_Mode.setValue(1)
   self.objMT_post__rightExpr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__rightExpr (self, wherex, wherey)\n'))
   self.objMT_post__rightExpr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__rightExpr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__rightExpr.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__rightExpr)
   self.globalAndLocalPostcondition(self.objMT_post__rightExpr, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__hasArgs=ButtonConfig(self)
   self.objMT_post__hasArgs.Contents.Text.setValue('New hasArgs')
   self.objMT_post__hasArgs.Contents.Image.setValue('')
   self.objMT_post__hasArgs.Contents.lastSelected= 'Text'
   self.objMT_post__hasArgs.Drawing_Mode.setValue(1)
   self.objMT_post__hasArgs.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__hasArgs (self, wherex, wherey)\n'))
   self.objMT_post__hasArgs.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__hasArgs)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__hasArgs.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__hasArgs)
   self.globalAndLocalPostcondition(self.objMT_post__hasArgs, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM=ButtonConfig(self)
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.Contents.Text.setValue('New GenericEdge_UMLRT2Kiltera_MM')
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.Contents.Image.setValue('')
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.Contents.lastSelected= 'Text'
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.Drawing_Mode.setValue(1)
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__GenericEdge_UMLRT2Kiltera_MM (self, wherex, wherey)\n'))
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__GenericEdge_UMLRT2Kiltera_MM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__GenericEdge_UMLRT2Kiltera_MM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__GenericEdge_UMLRT2Kiltera_MM)
   self.globalAndLocalPostcondition(self.objMT_post__GenericEdge_UMLRT2Kiltera_MM, rootNode)

newfunction = MT_post__UMLRT2Kiltera_MM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
