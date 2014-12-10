"""
__UMLRT2Kiltera_MM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: gehan
Modified: Sat Aug 30 18:25:18 2014
_______________________________________________________________________________
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
def UMLRT2Kiltera_MM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('UMLRT2Kiltera_MM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'UMLRT2Kiltera_MM_MM.py' )


   self.globalPrecondition(rootNode)

   self.objEdit=ButtonConfig(self)
   self.objEdit.Contents.Text.setValue('Edit')
   self.objEdit.Contents.Image.setValue('')
   self.objEdit.Contents.lastSelected= 'Text'
   self.objEdit.Drawing_Mode.setValue(0)
   self.objEdit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("UMLRT2Kiltera_MM_META")) ') )
   self.objEdit.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objEdit)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objEdit.graphObject_ = new_obj
   rootNode.addNode(self.objEdit)
   self.globalAndLocalPostcondition(self.objEdit, rootNode)



   self.globalPrecondition(rootNode)

   self.objHelp=ButtonConfig(self)
   self.objHelp.Contents.Text.setValue('Help')
   self.objHelp.Contents.Image.setValue('')
   self.objHelp.Contents.lastSelected= 'Text'
   self.objHelp.Drawing_Mode.setValue(0)
   self.objHelp.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["UMLRT2Kiltera_MM_METAHelp.txt"])\n ') )
   self.objHelp.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objHelp)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objHelp.graphObject_ = new_obj
   rootNode.addNode(self.objHelp)
   self.globalAndLocalPostcondition(self.objHelp, rootNode)

   self.globalPrecondition(rootNode)

   self.objMatchModel=ButtonConfig(self)
   self.objMatchModel.Contents.Text.setValue('New MatchModel')
   self.objMatchModel.Contents.Image.setValue('')
   self.objMatchModel.Contents.lastSelected= 'Text'
   self.objMatchModel.Drawing_Mode.setValue(1)
   self.objMatchModel.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMatchModel (self, wherex, wherey)\n'))
   self.objMatchModel.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMatchModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMatchModel.graphObject_ = new_obj
   rootNode.addNode(self.objMatchModel)
   self.globalAndLocalPostcondition(self.objMatchModel, rootNode)
   self.globalPrecondition(rootNode)

   self.objApplyModel=ButtonConfig(self)
   self.objApplyModel.Contents.Text.setValue('New ApplyModel')
   self.objApplyModel.Contents.Image.setValue('')
   self.objApplyModel.Contents.lastSelected= 'Text'
   self.objApplyModel.Drawing_Mode.setValue(1)
   self.objApplyModel.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewApplyModel (self, wherex, wherey)\n'))
   self.objApplyModel.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objApplyModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objApplyModel.graphObject_ = new_obj
   rootNode.addNode(self.objApplyModel)
   self.globalAndLocalPostcondition(self.objApplyModel, rootNode)
   self.globalPrecondition(rootNode)

   self.objMetaModelElement_S=ButtonConfig(self)
   self.objMetaModelElement_S.Contents.Text.setValue('New MetaModelElement_S')
   self.objMetaModelElement_S.Contents.Image.setValue('')
   self.objMetaModelElement_S.Contents.lastSelected= 'Text'
   self.objMetaModelElement_S.Drawing_Mode.setValue(1)
   self.objMetaModelElement_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMetaModelElement_S (self, wherex, wherey)\n'))
   self.objMetaModelElement_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMetaModelElement_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMetaModelElement_S.graphObject_ = new_obj
   rootNode.addNode(self.objMetaModelElement_S)
   self.globalAndLocalPostcondition(self.objMetaModelElement_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMetaModelElement_T=ButtonConfig(self)
   self.objMetaModelElement_T.Contents.Text.setValue('New MetaModelElement_T')
   self.objMetaModelElement_T.Contents.Image.setValue('')
   self.objMetaModelElement_T.Contents.lastSelected= 'Text'
   self.objMetaModelElement_T.Drawing_Mode.setValue(1)
   self.objMetaModelElement_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMetaModelElement_T (self, wherex, wherey)\n'))
   self.objMetaModelElement_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMetaModelElement_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMetaModelElement_T.graphObject_ = new_obj
   rootNode.addNode(self.objMetaModelElement_T)
   self.globalAndLocalPostcondition(self.objMetaModelElement_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objElement=ButtonConfig(self)
   self.objElement.Contents.Text.setValue('New Element')
   self.objElement.Contents.Image.setValue('')
   self.objElement.Contents.lastSelected= 'Text'
   self.objElement.Drawing_Mode.setValue(1)
   self.objElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewElement (self, wherex, wherey)\n'))
   self.objElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objElement.graphObject_ = new_obj
   rootNode.addNode(self.objElement)
   self.globalAndLocalPostcondition(self.objElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objNamedElement=ButtonConfig(self)
   self.objNamedElement.Contents.Text.setValue('New NamedElement')
   self.objNamedElement.Contents.Image.setValue('')
   self.objNamedElement.Contents.lastSelected= 'Text'
   self.objNamedElement.Drawing_Mode.setValue(1)
   self.objNamedElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewNamedElement (self, wherex, wherey)\n'))
   self.objNamedElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objNamedElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objNamedElement.graphObject_ = new_obj
   rootNode.addNode(self.objNamedElement)
   self.globalAndLocalPostcondition(self.objNamedElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objTrigger_S=ButtonConfig(self)
   self.objTrigger_S.Contents.Text.setValue('New Trigger_S')
   self.objTrigger_S.Contents.Image.setValue('')
   self.objTrigger_S.Contents.lastSelected= 'Text'
   self.objTrigger_S.Drawing_Mode.setValue(1)
   self.objTrigger_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTrigger_S (self, wherex, wherey)\n'))
   self.objTrigger_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objTrigger_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objTrigger_S.graphObject_ = new_obj
   rootNode.addNode(self.objTrigger_S)
   self.globalAndLocalPostcondition(self.objTrigger_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objAction=ButtonConfig(self)
   self.objAction.Contents.Text.setValue('New Action')
   self.objAction.Contents.Image.setValue('')
   self.objAction.Contents.lastSelected= 'Text'
   self.objAction.Drawing_Mode.setValue(1)
   self.objAction.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAction (self, wherex, wherey)\n'))
   self.objAction.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objAction)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAction.graphObject_ = new_obj
   rootNode.addNode(self.objAction)
   self.globalAndLocalPostcondition(self.objAction, rootNode)
   self.globalPrecondition(rootNode)

   self.objPortRef=ButtonConfig(self)
   self.objPortRef.Contents.Text.setValue('New PortRef')
   self.objPortRef.Contents.Image.setValue('')
   self.objPortRef.Contents.lastSelected= 'Text'
   self.objPortRef.Drawing_Mode.setValue(1)
   self.objPortRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPortRef (self, wherex, wherey)\n'))
   self.objPortRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objPortRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPortRef.graphObject_ = new_obj
   rootNode.addNode(self.objPortRef)
   self.globalAndLocalPostcondition(self.objPortRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objPortConnectorRef=ButtonConfig(self)
   self.objPortConnectorRef.Contents.Text.setValue('New PortConnectorRef')
   self.objPortConnectorRef.Contents.Image.setValue('')
   self.objPortConnectorRef.Contents.lastSelected= 'Text'
   self.objPortConnectorRef.Drawing_Mode.setValue(1)
   self.objPortConnectorRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPortConnectorRef (self, wherex, wherey)\n'))
   self.objPortConnectorRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objPortConnectorRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPortConnectorRef.graphObject_ = new_obj
   rootNode.addNode(self.objPortConnectorRef)
   self.globalAndLocalPostcondition(self.objPortConnectorRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objStateMachineElement=ButtonConfig(self)
   self.objStateMachineElement.Contents.Text.setValue('New StateMachineElement')
   self.objStateMachineElement.Contents.Image.setValue('')
   self.objStateMachineElement.Contents.lastSelected= 'Text'
   self.objStateMachineElement.Drawing_Mode.setValue(1)
   self.objStateMachineElement.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStateMachineElement (self, wherex, wherey)\n'))
   self.objStateMachineElement.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objStateMachineElement)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objStateMachineElement.graphObject_ = new_obj
   rootNode.addNode(self.objStateMachineElement)
   self.globalAndLocalPostcondition(self.objStateMachineElement, rootNode)
   self.globalPrecondition(rootNode)

   self.objProtocol=ButtonConfig(self)
   self.objProtocol.Contents.Text.setValue('New Protocol')
   self.objProtocol.Contents.Image.setValue('')
   self.objProtocol.Contents.lastSelected= 'Text'
   self.objProtocol.Drawing_Mode.setValue(1)
   self.objProtocol.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewProtocol (self, wherex, wherey)\n'))
   self.objProtocol.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objProtocol)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objProtocol.graphObject_ = new_obj
   rootNode.addNode(self.objProtocol)
   self.globalAndLocalPostcondition(self.objProtocol, rootNode)
   self.globalPrecondition(rootNode)

   self.objSignal=ButtonConfig(self)
   self.objSignal.Contents.Text.setValue('New Signal')
   self.objSignal.Contents.Image.setValue('')
   self.objSignal.Contents.lastSelected= 'Text'
   self.objSignal.Drawing_Mode.setValue(1)
   self.objSignal.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSignal (self, wherex, wherey)\n'))
   self.objSignal.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objSignal)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSignal.graphObject_ = new_obj
   rootNode.addNode(self.objSignal)
   self.globalAndLocalPostcondition(self.objSignal, rootNode)
   self.globalPrecondition(rootNode)

   self.objPort=ButtonConfig(self)
   self.objPort.Contents.Text.setValue('New Port')
   self.objPort.Contents.Image.setValue('')
   self.objPort.Contents.lastSelected= 'Text'
   self.objPort.Drawing_Mode.setValue(1)
   self.objPort.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPort (self, wherex, wherey)\n'))
   self.objPort.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objPort)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPort.graphObject_ = new_obj
   rootNode.addNode(self.objPort)
   self.globalAndLocalPostcondition(self.objPort, rootNode)
   self.globalPrecondition(rootNode)

   self.objVertex=ButtonConfig(self)
   self.objVertex.Contents.Text.setValue('New Vertex')
   self.objVertex.Contents.Image.setValue('')
   self.objVertex.Contents.lastSelected= 'Text'
   self.objVertex.Drawing_Mode.setValue(1)
   self.objVertex.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewVertex (self, wherex, wherey)\n'))
   self.objVertex.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objVertex)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objVertex.graphObject_ = new_obj
   rootNode.addNode(self.objVertex)
   self.globalAndLocalPostcondition(self.objVertex, rootNode)
   self.globalPrecondition(rootNode)

   self.objInitialPoint=ButtonConfig(self)
   self.objInitialPoint.Contents.Text.setValue('New InitialPoint')
   self.objInitialPoint.Contents.Image.setValue('')
   self.objInitialPoint.Contents.lastSelected= 'Text'
   self.objInitialPoint.Drawing_Mode.setValue(1)
   self.objInitialPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewInitialPoint (self, wherex, wherey)\n'))
   self.objInitialPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objInitialPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objInitialPoint.graphObject_ = new_obj
   rootNode.addNode(self.objInitialPoint)
   self.globalAndLocalPostcondition(self.objInitialPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objEntryPoint=ButtonConfig(self)
   self.objEntryPoint.Contents.Text.setValue('New EntryPoint')
   self.objEntryPoint.Contents.Image.setValue('')
   self.objEntryPoint.Contents.lastSelected= 'Text'
   self.objEntryPoint.Drawing_Mode.setValue(1)
   self.objEntryPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewEntryPoint (self, wherex, wherey)\n'))
   self.objEntryPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objEntryPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objEntryPoint.graphObject_ = new_obj
   rootNode.addNode(self.objEntryPoint)
   self.globalAndLocalPostcondition(self.objEntryPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objExitPoint=ButtonConfig(self)
   self.objExitPoint.Contents.Text.setValue('New ExitPoint')
   self.objExitPoint.Contents.Image.setValue('')
   self.objExitPoint.Contents.lastSelected= 'Text'
   self.objExitPoint.Drawing_Mode.setValue(1)
   self.objExitPoint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewExitPoint (self, wherex, wherey)\n'))
   self.objExitPoint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objExitPoint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objExitPoint.graphObject_ = new_obj
   rootNode.addNode(self.objExitPoint)
   self.globalAndLocalPostcondition(self.objExitPoint, rootNode)
   self.globalPrecondition(rootNode)

   self.objTransition=ButtonConfig(self)
   self.objTransition.Contents.Text.setValue('New Transition')
   self.objTransition.Contents.Image.setValue('')
   self.objTransition.Contents.lastSelected= 'Text'
   self.objTransition.Drawing_Mode.setValue(1)
   self.objTransition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTransition (self, wherex, wherey)\n'))
   self.objTransition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objTransition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objTransition.graphObject_ = new_obj
   rootNode.addNode(self.objTransition)
   self.globalAndLocalPostcondition(self.objTransition, rootNode)
   self.globalPrecondition(rootNode)

   self.objStateMachine=ButtonConfig(self)
   self.objStateMachine.Contents.Text.setValue('New StateMachine')
   self.objStateMachine.Contents.Image.setValue('')
   self.objStateMachine.Contents.lastSelected= 'Text'
   self.objStateMachine.Drawing_Mode.setValue(1)
   self.objStateMachine.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStateMachine (self, wherex, wherey)\n'))
   self.objStateMachine.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objStateMachine)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objStateMachine.graphObject_ = new_obj
   rootNode.addNode(self.objStateMachine)
   self.globalAndLocalPostcondition(self.objStateMachine, rootNode)
   self.globalPrecondition(rootNode)

   self.objState=ButtonConfig(self)
   self.objState.Contents.Text.setValue('New State')
   self.objState.Contents.Image.setValue('')
   self.objState.Contents.lastSelected= 'Text'
   self.objState.Drawing_Mode.setValue(1)
   self.objState.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewState (self, wherex, wherey)\n'))
   self.objState.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objState)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objState.graphObject_ = new_obj
   rootNode.addNode(self.objState)
   self.globalAndLocalPostcondition(self.objState, rootNode)
   self.globalPrecondition(rootNode)

   self.objCapsule=ButtonConfig(self)
   self.objCapsule.Contents.Text.setValue('New Capsule')
   self.objCapsule.Contents.Image.setValue('')
   self.objCapsule.Contents.lastSelected= 'Text'
   self.objCapsule.Drawing_Mode.setValue(1)
   self.objCapsule.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCapsule (self, wherex, wherey)\n'))
   self.objCapsule.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objCapsule)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objCapsule.graphObject_ = new_obj
   rootNode.addNode(self.objCapsule)
   self.globalAndLocalPostcondition(self.objCapsule, rootNode)
   self.globalPrecondition(rootNode)

   self.objPackageContainer=ButtonConfig(self)
   self.objPackageContainer.Contents.Text.setValue('New PackageContainer')
   self.objPackageContainer.Contents.Image.setValue('')
   self.objPackageContainer.Contents.lastSelected= 'Text'
   self.objPackageContainer.Drawing_Mode.setValue(1)
   self.objPackageContainer.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPackageContainer (self, wherex, wherey)\n'))
   self.objPackageContainer.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objPackageContainer)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPackageContainer.graphObject_ = new_obj
   rootNode.addNode(self.objPackageContainer)
   self.globalAndLocalPostcondition(self.objPackageContainer, rootNode)
   self.globalPrecondition(rootNode)

   self.objModel_S=ButtonConfig(self)
   self.objModel_S.Contents.Text.setValue('New Model_S')
   self.objModel_S.Contents.Image.setValue('')
   self.objModel_S.Contents.lastSelected= 'Text'
   self.objModel_S.Drawing_Mode.setValue(1)
   self.objModel_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewModel_S (self, wherex, wherey)\n'))
   self.objModel_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objModel_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objModel_S.graphObject_ = new_obj
   rootNode.addNode(self.objModel_S)
   self.globalAndLocalPostcondition(self.objModel_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objPackage=ButtonConfig(self)
   self.objPackage.Contents.Text.setValue('New Package')
   self.objPackage.Contents.Image.setValue('')
   self.objPackage.Contents.lastSelected= 'Text'
   self.objPackage.Drawing_Mode.setValue(1)
   self.objPackage.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPackage (self, wherex, wherey)\n'))
   self.objPackage.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objPackage)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPackage.graphObject_ = new_obj
   rootNode.addNode(self.objPackage)
   self.globalAndLocalPostcondition(self.objPackage, rootNode)
   self.globalPrecondition(rootNode)

   self.objCapsuleRole=ButtonConfig(self)
   self.objCapsuleRole.Contents.Text.setValue('New CapsuleRole')
   self.objCapsuleRole.Contents.Image.setValue('')
   self.objCapsuleRole.Contents.lastSelected= 'Text'
   self.objCapsuleRole.Drawing_Mode.setValue(1)
   self.objCapsuleRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCapsuleRole (self, wherex, wherey)\n'))
   self.objCapsuleRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objCapsuleRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objCapsuleRole.graphObject_ = new_obj
   rootNode.addNode(self.objCapsuleRole)
   self.globalAndLocalPostcondition(self.objCapsuleRole, rootNode)
   self.globalPrecondition(rootNode)

   self.objPortConnector=ButtonConfig(self)
   self.objPortConnector.Contents.Text.setValue('New PortConnector')
   self.objPortConnector.Contents.Image.setValue('')
   self.objPortConnector.Contents.lastSelected= 'Text'
   self.objPortConnector.Drawing_Mode.setValue(1)
   self.objPortConnector.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPortConnector (self, wherex, wherey)\n'))
   self.objPortConnector.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objPortConnector)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPortConnector.graphObject_ = new_obj
   rootNode.addNode(self.objPortConnector)
   self.globalAndLocalPostcondition(self.objPortConnector, rootNode)
   self.globalPrecondition(rootNode)

   self.objThread=ButtonConfig(self)
   self.objThread.Contents.Text.setValue('New Thread')
   self.objThread.Contents.Image.setValue('')
   self.objThread.Contents.lastSelected= 'Text'
   self.objThread.Drawing_Mode.setValue(1)
   self.objThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewThread (self, wherex, wherey)\n'))
   self.objThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objThread.graphObject_ = new_obj
   rootNode.addNode(self.objThread)
   self.globalAndLocalPostcondition(self.objThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objPhysicalThread=ButtonConfig(self)
   self.objPhysicalThread.Contents.Text.setValue('New PhysicalThread')
   self.objPhysicalThread.Contents.Image.setValue('')
   self.objPhysicalThread.Contents.lastSelected= 'Text'
   self.objPhysicalThread.Drawing_Mode.setValue(1)
   self.objPhysicalThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPhysicalThread (self, wherex, wherey)\n'))
   self.objPhysicalThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objPhysicalThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPhysicalThread.graphObject_ = new_obj
   rootNode.addNode(self.objPhysicalThread)
   self.globalAndLocalPostcondition(self.objPhysicalThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objLogicalThread=ButtonConfig(self)
   self.objLogicalThread.Contents.Text.setValue('New LogicalThread')
   self.objLogicalThread.Contents.Image.setValue('')
   self.objLogicalThread.Contents.lastSelected= 'Text'
   self.objLogicalThread.Drawing_Mode.setValue(1)
   self.objLogicalThread.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewLogicalThread (self, wherex, wherey)\n'))
   self.objLogicalThread.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objLogicalThread)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objLogicalThread.graphObject_ = new_obj
   rootNode.addNode(self.objLogicalThread)
   self.globalAndLocalPostcondition(self.objLogicalThread, rootNode)
   self.globalPrecondition(rootNode)

   self.objPortType=ButtonConfig(self)
   self.objPortType.Contents.Text.setValue('New PortType')
   self.objPortType.Contents.Image.setValue('')
   self.objPortType.Contents.lastSelected= 'Text'
   self.objPortType.Drawing_Mode.setValue(1)
   self.objPortType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPortType (self, wherex, wherey)\n'))
   self.objPortType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objPortType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPortType.graphObject_ = new_obj
   rootNode.addNode(self.objPortType)
   self.globalAndLocalPostcondition(self.objPortType, rootNode)
   self.globalPrecondition(rootNode)

   self.objBASE0=ButtonConfig(self)
   self.objBASE0.Contents.Text.setValue('New BASE0')
   self.objBASE0.Contents.Image.setValue('')
   self.objBASE0.Contents.lastSelected= 'Text'
   self.objBASE0.Drawing_Mode.setValue(1)
   self.objBASE0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewBASE0 (self, wherex, wherey)\n'))
   self.objBASE0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objBASE0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objBASE0.graphObject_ = new_obj
   rootNode.addNode(self.objBASE0)
   self.globalAndLocalPostcondition(self.objBASE0, rootNode)
   self.globalPrecondition(rootNode)

   self.objCONJUGATE1=ButtonConfig(self)
   self.objCONJUGATE1.Contents.Text.setValue('New CONJUGATE1')
   self.objCONJUGATE1.Contents.Image.setValue('')
   self.objCONJUGATE1.Contents.lastSelected= 'Text'
   self.objCONJUGATE1.Drawing_Mode.setValue(1)
   self.objCONJUGATE1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCONJUGATE1 (self, wherex, wherey)\n'))
   self.objCONJUGATE1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objCONJUGATE1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objCONJUGATE1.graphObject_ = new_obj
   rootNode.addNode(self.objCONJUGATE1)
   self.globalAndLocalPostcondition(self.objCONJUGATE1, rootNode)
   self.globalPrecondition(rootNode)

   self.objSignalType=ButtonConfig(self)
   self.objSignalType.Contents.Text.setValue('New SignalType')
   self.objSignalType.Contents.Image.setValue('')
   self.objSignalType.Contents.lastSelected= 'Text'
   self.objSignalType.Drawing_Mode.setValue(1)
   self.objSignalType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSignalType (self, wherex, wherey)\n'))
   self.objSignalType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objSignalType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSignalType.graphObject_ = new_obj
   rootNode.addNode(self.objSignalType)
   self.globalAndLocalPostcondition(self.objSignalType, rootNode)
   self.globalPrecondition(rootNode)

   self.objOUT1=ButtonConfig(self)
   self.objOUT1.Contents.Text.setValue('New OUT1')
   self.objOUT1.Contents.Image.setValue('')
   self.objOUT1.Contents.lastSelected= 'Text'
   self.objOUT1.Drawing_Mode.setValue(1)
   self.objOUT1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOUT1 (self, wherex, wherey)\n'))
   self.objOUT1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objOUT1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objOUT1.graphObject_ = new_obj
   rootNode.addNode(self.objOUT1)
   self.globalAndLocalPostcondition(self.objOUT1, rootNode)
   self.globalPrecondition(rootNode)

   self.objIN0=ButtonConfig(self)
   self.objIN0.Contents.Text.setValue('New IN0')
   self.objIN0.Contents.Image.setValue('')
   self.objIN0.Contents.lastSelected= 'Text'
   self.objIN0.Drawing_Mode.setValue(1)
   self.objIN0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewIN0 (self, wherex, wherey)\n'))
   self.objIN0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objIN0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objIN0.graphObject_ = new_obj
   rootNode.addNode(self.objIN0)
   self.globalAndLocalPostcondition(self.objIN0, rootNode)
   self.globalPrecondition(rootNode)

   self.objRoleType=ButtonConfig(self)
   self.objRoleType.Contents.Text.setValue('New RoleType')
   self.objRoleType.Contents.Image.setValue('')
   self.objRoleType.Contents.lastSelected= 'Text'
   self.objRoleType.Drawing_Mode.setValue(1)
   self.objRoleType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewRoleType (self, wherex, wherey)\n'))
   self.objRoleType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objRoleType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objRoleType.graphObject_ = new_obj
   rootNode.addNode(self.objRoleType)
   self.globalAndLocalPostcondition(self.objRoleType, rootNode)
   self.globalPrecondition(rootNode)

   self.objFIXED0=ButtonConfig(self)
   self.objFIXED0.Contents.Text.setValue('New FIXED0')
   self.objFIXED0.Contents.Image.setValue('')
   self.objFIXED0.Contents.lastSelected= 'Text'
   self.objFIXED0.Drawing_Mode.setValue(1)
   self.objFIXED0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewFIXED0 (self, wherex, wherey)\n'))
   self.objFIXED0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objFIXED0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objFIXED0.graphObject_ = new_obj
   rootNode.addNode(self.objFIXED0)
   self.globalAndLocalPostcondition(self.objFIXED0, rootNode)
   self.globalPrecondition(rootNode)

   self.objOPTIONAL1=ButtonConfig(self)
   self.objOPTIONAL1.Contents.Text.setValue('New OPTIONAL1')
   self.objOPTIONAL1.Contents.Image.setValue('')
   self.objOPTIONAL1.Contents.lastSelected= 'Text'
   self.objOPTIONAL1.Drawing_Mode.setValue(1)
   self.objOPTIONAL1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOPTIONAL1 (self, wherex, wherey)\n'))
   self.objOPTIONAL1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objOPTIONAL1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objOPTIONAL1.graphObject_ = new_obj
   rootNode.addNode(self.objOPTIONAL1)
   self.globalAndLocalPostcondition(self.objOPTIONAL1, rootNode)
   self.globalPrecondition(rootNode)

   self.objPLUGIN2=ButtonConfig(self)
   self.objPLUGIN2.Contents.Text.setValue('New PLUGIN2')
   self.objPLUGIN2.Contents.Image.setValue('')
   self.objPLUGIN2.Contents.lastSelected= 'Text'
   self.objPLUGIN2.Drawing_Mode.setValue(1)
   self.objPLUGIN2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPLUGIN2 (self, wherex, wherey)\n'))
   self.objPLUGIN2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objPLUGIN2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPLUGIN2.graphObject_ = new_obj
   rootNode.addNode(self.objPLUGIN2)
   self.globalAndLocalPostcondition(self.objPLUGIN2, rootNode)
   self.globalPrecondition(rootNode)

   self.objTransitionType=ButtonConfig(self)
   self.objTransitionType.Contents.Text.setValue('New TransitionType')
   self.objTransitionType.Contents.Image.setValue('')
   self.objTransitionType.Contents.lastSelected= 'Text'
   self.objTransitionType.Drawing_Mode.setValue(1)
   self.objTransitionType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTransitionType (self, wherex, wherey)\n'))
   self.objTransitionType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objTransitionType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objTransitionType.graphObject_ = new_obj
   rootNode.addNode(self.objTransitionType)
   self.globalAndLocalPostcondition(self.objTransitionType, rootNode)
   self.globalPrecondition(rootNode)

   self.objSIBLING0=ButtonConfig(self)
   self.objSIBLING0.Contents.Text.setValue('New SIBLING0')
   self.objSIBLING0.Contents.Image.setValue('')
   self.objSIBLING0.Contents.lastSelected= 'Text'
   self.objSIBLING0.Drawing_Mode.setValue(1)
   self.objSIBLING0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSIBLING0 (self, wherex, wherey)\n'))
   self.objSIBLING0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objSIBLING0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSIBLING0.graphObject_ = new_obj
   rootNode.addNode(self.objSIBLING0)
   self.globalAndLocalPostcondition(self.objSIBLING0, rootNode)
   self.globalPrecondition(rootNode)

   self.objIN1=ButtonConfig(self)
   self.objIN1.Contents.Text.setValue('New IN1')
   self.objIN1.Contents.Image.setValue('')
   self.objIN1.Contents.lastSelected= 'Text'
   self.objIN1.Drawing_Mode.setValue(1)
   self.objIN1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewIN1 (self, wherex, wherey)\n'))
   self.objIN1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objIN1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objIN1.graphObject_ = new_obj
   rootNode.addNode(self.objIN1)
   self.globalAndLocalPostcondition(self.objIN1, rootNode)
   self.globalPrecondition(rootNode)

   self.objOUT2=ButtonConfig(self)
   self.objOUT2.Contents.Text.setValue('New OUT2')
   self.objOUT2.Contents.Image.setValue('')
   self.objOUT2.Contents.lastSelected= 'Text'
   self.objOUT2.Drawing_Mode.setValue(1)
   self.objOUT2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOUT2 (self, wherex, wherey)\n'))
   self.objOUT2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objOUT2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objOUT2.graphObject_ = new_obj
   rootNode.addNode(self.objOUT2)
   self.globalAndLocalPostcondition(self.objOUT2, rootNode)
   self.globalPrecondition(rootNode)

   self.objDef=ButtonConfig(self)
   self.objDef.Contents.Text.setValue('New Def')
   self.objDef.Contents.Image.setValue('')
   self.objDef.Contents.lastSelected= 'Text'
   self.objDef.Drawing_Mode.setValue(1)
   self.objDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewDef (self, wherex, wherey)\n'))
   self.objDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objDef.graphObject_ = new_obj
   rootNode.addNode(self.objDef)
   self.globalAndLocalPostcondition(self.objDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objExpr=ButtonConfig(self)
   self.objExpr.Contents.Text.setValue('New Expr')
   self.objExpr.Contents.Image.setValue('')
   self.objExpr.Contents.lastSelected= 'Text'
   self.objExpr.Drawing_Mode.setValue(1)
   self.objExpr.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewExpr (self, wherex, wherey)\n'))
   self.objExpr.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objExpr)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objExpr.graphObject_ = new_obj
   rootNode.addNode(self.objExpr)
   self.globalAndLocalPostcondition(self.objExpr, rootNode)
   self.globalPrecondition(rootNode)

   self.objPattern=ButtonConfig(self)
   self.objPattern.Contents.Text.setValue('New Pattern')
   self.objPattern.Contents.Image.setValue('')
   self.objPattern.Contents.lastSelected= 'Text'
   self.objPattern.Drawing_Mode.setValue(1)
   self.objPattern.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPattern (self, wherex, wherey)\n'))
   self.objPattern.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objPattern)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPattern.graphObject_ = new_obj
   rootNode.addNode(self.objPattern)
   self.globalAndLocalPostcondition(self.objPattern, rootNode)
   self.globalPrecondition(rootNode)

   self.objProc=ButtonConfig(self)
   self.objProc.Contents.Text.setValue('New Proc')
   self.objProc.Contents.Image.setValue('')
   self.objProc.Contents.lastSelected= 'Text'
   self.objProc.Drawing_Mode.setValue(1)
   self.objProc.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewProc (self, wherex, wherey)\n'))
   self.objProc.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objProc)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objProc.graphObject_ = new_obj
   rootNode.addNode(self.objProc)
   self.globalAndLocalPostcondition(self.objProc, rootNode)
   self.globalPrecondition(rootNode)

   self.objProcDef=ButtonConfig(self)
   self.objProcDef.Contents.Text.setValue('New ProcDef')
   self.objProcDef.Contents.Image.setValue('')
   self.objProcDef.Contents.lastSelected= 'Text'
   self.objProcDef.Drawing_Mode.setValue(1)
   self.objProcDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewProcDef (self, wherex, wherey)\n'))
   self.objProcDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objProcDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objProcDef.graphObject_ = new_obj
   rootNode.addNode(self.objProcDef)
   self.globalAndLocalPostcondition(self.objProcDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objFuncDef=ButtonConfig(self)
   self.objFuncDef.Contents.Text.setValue('New FuncDef')
   self.objFuncDef.Contents.Image.setValue('')
   self.objFuncDef.Contents.lastSelected= 'Text'
   self.objFuncDef.Drawing_Mode.setValue(1)
   self.objFuncDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewFuncDef (self, wherex, wherey)\n'))
   self.objFuncDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objFuncDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objFuncDef.graphObject_ = new_obj
   rootNode.addNode(self.objFuncDef)
   self.globalAndLocalPostcondition(self.objFuncDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objName=ButtonConfig(self)
   self.objName.Contents.Text.setValue('New Name')
   self.objName.Contents.Image.setValue('')
   self.objName.Contents.lastSelected= 'Text'
   self.objName.Drawing_Mode.setValue(1)
   self.objName.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewName (self, wherex, wherey)\n'))
   self.objName.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objName)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objName.graphObject_ = new_obj
   rootNode.addNode(self.objName)
   self.globalAndLocalPostcondition(self.objName, rootNode)
   self.globalPrecondition(rootNode)

   self.objPythonRef=ButtonConfig(self)
   self.objPythonRef.Contents.Text.setValue('New PythonRef')
   self.objPythonRef.Contents.Image.setValue('')
   self.objPythonRef.Contents.lastSelected= 'Text'
   self.objPythonRef.Drawing_Mode.setValue(1)
   self.objPythonRef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPythonRef (self, wherex, wherey)\n'))
   self.objPythonRef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objPythonRef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPythonRef.graphObject_ = new_obj
   rootNode.addNode(self.objPythonRef)
   self.globalAndLocalPostcondition(self.objPythonRef, rootNode)
   self.globalPrecondition(rootNode)

   self.objModule=ButtonConfig(self)
   self.objModule.Contents.Text.setValue('New Module')
   self.objModule.Contents.Image.setValue('')
   self.objModule.Contents.lastSelected= 'Text'
   self.objModule.Drawing_Mode.setValue(1)
   self.objModule.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewModule (self, wherex, wherey)\n'))
   self.objModule.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objModule)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objModule.graphObject_ = new_obj
   rootNode.addNode(self.objModule)
   self.globalAndLocalPostcondition(self.objModule, rootNode)
   self.globalPrecondition(rootNode)

   self.objNull=ButtonConfig(self)
   self.objNull.Contents.Text.setValue('New Null')
   self.objNull.Contents.Image.setValue('')
   self.objNull.Contents.lastSelected= 'Text'
   self.objNull.Drawing_Mode.setValue(1)
   self.objNull.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewNull (self, wherex, wherey)\n'))
   self.objNull.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objNull)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objNull.graphObject_ = new_obj
   rootNode.addNode(self.objNull)
   self.globalAndLocalPostcondition(self.objNull, rootNode)
   self.globalPrecondition(rootNode)

   self.objTrigger_T=ButtonConfig(self)
   self.objTrigger_T.Contents.Text.setValue('New Trigger_T')
   self.objTrigger_T.Contents.Image.setValue('')
   self.objTrigger_T.Contents.lastSelected= 'Text'
   self.objTrigger_T.Drawing_Mode.setValue(1)
   self.objTrigger_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTrigger_T (self, wherex, wherey)\n'))
   self.objTrigger_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objTrigger_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objTrigger_T.graphObject_ = new_obj
   rootNode.addNode(self.objTrigger_T)
   self.globalAndLocalPostcondition(self.objTrigger_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objListen=ButtonConfig(self)
   self.objListen.Contents.Text.setValue('New Listen')
   self.objListen.Contents.Image.setValue('')
   self.objListen.Contents.lastSelected= 'Text'
   self.objListen.Drawing_Mode.setValue(1)
   self.objListen.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewListen (self, wherex, wherey)\n'))
   self.objListen.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objListen)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objListen.graphObject_ = new_obj
   rootNode.addNode(self.objListen)
   self.globalAndLocalPostcondition(self.objListen, rootNode)
   self.globalPrecondition(rootNode)

   self.objConditionBranch=ButtonConfig(self)
   self.objConditionBranch.Contents.Text.setValue('New ConditionBranch')
   self.objConditionBranch.Contents.Image.setValue('')
   self.objConditionBranch.Contents.lastSelected= 'Text'
   self.objConditionBranch.Drawing_Mode.setValue(1)
   self.objConditionBranch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewConditionBranch (self, wherex, wherey)\n'))
   self.objConditionBranch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objConditionBranch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objConditionBranch.graphObject_ = new_obj
   rootNode.addNode(self.objConditionBranch)
   self.globalAndLocalPostcondition(self.objConditionBranch, rootNode)
   self.globalPrecondition(rootNode)

   self.objListenBranch=ButtonConfig(self)
   self.objListenBranch.Contents.Text.setValue('New ListenBranch')
   self.objListenBranch.Contents.Image.setValue('')
   self.objListenBranch.Contents.lastSelected= 'Text'
   self.objListenBranch.Drawing_Mode.setValue(1)
   self.objListenBranch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewListenBranch (self, wherex, wherey)\n'))
   self.objListenBranch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objListenBranch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objListenBranch.graphObject_ = new_obj
   rootNode.addNode(self.objListenBranch)
   self.globalAndLocalPostcondition(self.objListenBranch, rootNode)
   self.globalPrecondition(rootNode)

   self.objSite=ButtonConfig(self)
   self.objSite.Contents.Text.setValue('New Site')
   self.objSite.Contents.Image.setValue('')
   self.objSite.Contents.lastSelected= 'Text'
   self.objSite.Drawing_Mode.setValue(1)
   self.objSite.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSite (self, wherex, wherey)\n'))
   self.objSite.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objSite)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSite.graphObject_ = new_obj
   rootNode.addNode(self.objSite)
   self.globalAndLocalPostcondition(self.objSite, rootNode)
   self.globalPrecondition(rootNode)

   self.objModel_T=ButtonConfig(self)
   self.objModel_T.Contents.Text.setValue('New Model_T')
   self.objModel_T.Contents.Image.setValue('')
   self.objModel_T.Contents.lastSelected= 'Text'
   self.objModel_T.Drawing_Mode.setValue(1)
   self.objModel_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewModel_T (self, wherex, wherey)\n'))
   self.objModel_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objModel_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objModel_T.graphObject_ = new_obj
   rootNode.addNode(self.objModel_T)
   self.globalAndLocalPostcondition(self.objModel_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMatchCase=ButtonConfig(self)
   self.objMatchCase.Contents.Text.setValue('New MatchCase')
   self.objMatchCase.Contents.Image.setValue('')
   self.objMatchCase.Contents.lastSelected= 'Text'
   self.objMatchCase.Drawing_Mode.setValue(1)
   self.objMatchCase.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMatchCase (self, wherex, wherey)\n'))
   self.objMatchCase.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMatchCase)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMatchCase.graphObject_ = new_obj
   rootNode.addNode(self.objMatchCase)
   self.globalAndLocalPostcondition(self.objMatchCase, rootNode)
   self.globalPrecondition(rootNode)

   self.objCondition=ButtonConfig(self)
   self.objCondition.Contents.Text.setValue('New Condition')
   self.objCondition.Contents.Image.setValue('')
   self.objCondition.Contents.lastSelected= 'Text'
   self.objCondition.Drawing_Mode.setValue(1)
   self.objCondition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCondition (self, wherex, wherey)\n'))
   self.objCondition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objCondition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objCondition.graphObject_ = new_obj
   rootNode.addNode(self.objCondition)
   self.globalAndLocalPostcondition(self.objCondition, rootNode)
   self.globalPrecondition(rootNode)

   self.objNew=ButtonConfig(self)
   self.objNew.Contents.Text.setValue('New New')
   self.objNew.Contents.Image.setValue('')
   self.objNew.Contents.lastSelected= 'Text'
   self.objNew.Drawing_Mode.setValue(1)
   self.objNew.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewNew (self, wherex, wherey)\n'))
   self.objNew.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objNew)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objNew.graphObject_ = new_obj
   rootNode.addNode(self.objNew)
   self.globalAndLocalPostcondition(self.objNew, rootNode)
   self.globalPrecondition(rootNode)

   self.objDelay=ButtonConfig(self)
   self.objDelay.Contents.Text.setValue('New Delay')
   self.objDelay.Contents.Image.setValue('')
   self.objDelay.Contents.lastSelected= 'Text'
   self.objDelay.Drawing_Mode.setValue(1)
   self.objDelay.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewDelay (self, wherex, wherey)\n'))
   self.objDelay.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objDelay)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objDelay.graphObject_ = new_obj
   rootNode.addNode(self.objDelay)
   self.globalAndLocalPostcondition(self.objDelay, rootNode)
   self.globalPrecondition(rootNode)

   self.objPar=ButtonConfig(self)
   self.objPar.Contents.Text.setValue('New Par')
   self.objPar.Contents.Image.setValue('')
   self.objPar.Contents.lastSelected= 'Text'
   self.objPar.Drawing_Mode.setValue(1)
   self.objPar.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPar (self, wherex, wherey)\n'))
   self.objPar.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objPar)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPar.graphObject_ = new_obj
   rootNode.addNode(self.objPar)
   self.globalAndLocalPostcondition(self.objPar, rootNode)
   self.globalPrecondition(rootNode)

   self.objParIndexed=ButtonConfig(self)
   self.objParIndexed.Contents.Text.setValue('New ParIndexed')
   self.objParIndexed.Contents.Image.setValue('')
   self.objParIndexed.Contents.lastSelected= 'Text'
   self.objParIndexed.Drawing_Mode.setValue(1)
   self.objParIndexed.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewParIndexed (self, wherex, wherey)\n'))
   self.objParIndexed.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objParIndexed)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objParIndexed.graphObject_ = new_obj
   rootNode.addNode(self.objParIndexed)
   self.globalAndLocalPostcondition(self.objParIndexed, rootNode)
   self.globalPrecondition(rootNode)

   self.objInst=ButtonConfig(self)
   self.objInst.Contents.Text.setValue('New Inst')
   self.objInst.Contents.Image.setValue('')
   self.objInst.Contents.lastSelected= 'Text'
   self.objInst.Drawing_Mode.setValue(1)
   self.objInst.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewInst (self, wherex, wherey)\n'))
   self.objInst.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objInst)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objInst.graphObject_ = new_obj
   rootNode.addNode(self.objInst)
   self.globalAndLocalPostcondition(self.objInst, rootNode)
   self.globalPrecondition(rootNode)

   self.objLocalDef=ButtonConfig(self)
   self.objLocalDef.Contents.Text.setValue('New LocalDef')
   self.objLocalDef.Contents.Image.setValue('')
   self.objLocalDef.Contents.lastSelected= 'Text'
   self.objLocalDef.Drawing_Mode.setValue(1)
   self.objLocalDef.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewLocalDef (self, wherex, wherey)\n'))
   self.objLocalDef.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objLocalDef)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objLocalDef.graphObject_ = new_obj
   rootNode.addNode(self.objLocalDef)
   self.globalAndLocalPostcondition(self.objLocalDef, rootNode)
   self.globalPrecondition(rootNode)

   self.objSeq=ButtonConfig(self)
   self.objSeq.Contents.Text.setValue('New Seq')
   self.objSeq.Contents.Image.setValue('')
   self.objSeq.Contents.lastSelected= 'Text'
   self.objSeq.Drawing_Mode.setValue(1)
   self.objSeq.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSeq (self, wherex, wherey)\n'))
   self.objSeq.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objSeq)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSeq.graphObject_ = new_obj
   rootNode.addNode(self.objSeq)
   self.globalAndLocalPostcondition(self.objSeq, rootNode)
   self.globalPrecondition(rootNode)

   self.objConditionSet=ButtonConfig(self)
   self.objConditionSet.Contents.Text.setValue('New ConditionSet')
   self.objConditionSet.Contents.Image.setValue('')
   self.objConditionSet.Contents.lastSelected= 'Text'
   self.objConditionSet.Drawing_Mode.setValue(1)
   self.objConditionSet.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewConditionSet (self, wherex, wherey)\n'))
   self.objConditionSet.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objConditionSet)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objConditionSet.graphObject_ = new_obj
   rootNode.addNode(self.objConditionSet)
   self.globalAndLocalPostcondition(self.objConditionSet, rootNode)
   self.globalPrecondition(rootNode)

   self.objMatch=ButtonConfig(self)
   self.objMatch.Contents.Text.setValue('New Match')
   self.objMatch.Contents.Image.setValue('')
   self.objMatch.Contents.lastSelected= 'Text'
   self.objMatch.Drawing_Mode.setValue(1)
   self.objMatch.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMatch (self, wherex, wherey)\n'))
   self.objMatch.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMatch)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMatch.graphObject_ = new_obj
   rootNode.addNode(self.objMatch)
   self.globalAndLocalPostcondition(self.objMatch, rootNode)
   self.globalPrecondition(rootNode)

   self.objPrint=ButtonConfig(self)
   self.objPrint.Contents.Text.setValue('New Print')
   self.objPrint.Contents.Image.setValue('')
   self.objPrint.Contents.lastSelected= 'Text'
   self.objPrint.Drawing_Mode.setValue(1)
   self.objPrint.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPrint (self, wherex, wherey)\n'))
   self.objPrint.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objPrint)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPrint.graphObject_ = new_obj
   rootNode.addNode(self.objPrint)
   self.globalAndLocalPostcondition(self.objPrint, rootNode)
   self.globalPrecondition(rootNode)

   self.objAttribute=ButtonConfig(self)
   self.objAttribute.Contents.Text.setValue('New Attribute')
   self.objAttribute.Contents.Image.setValue('')
   self.objAttribute.Contents.lastSelected= 'Text'
   self.objAttribute.Drawing_Mode.setValue(1)
   self.objAttribute.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAttribute (self, wherex, wherey)\n'))
   self.objAttribute.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objAttribute)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAttribute.graphObject_ = new_obj
   rootNode.addNode(self.objAttribute)
   self.globalAndLocalPostcondition(self.objAttribute, rootNode)
   self.globalPrecondition(rootNode)

   self.objExpression=ButtonConfig(self)
   self.objExpression.Contents.Text.setValue('New Expression')
   self.objExpression.Contents.Image.setValue('')
   self.objExpression.Contents.lastSelected= 'Text'
   self.objExpression.Drawing_Mode.setValue(1)
   self.objExpression.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewExpression (self, wherex, wherey)\n'))
   self.objExpression.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objExpression)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objExpression.graphObject_ = new_obj
   rootNode.addNode(self.objExpression)
   self.globalAndLocalPostcondition(self.objExpression, rootNode)
   self.globalPrecondition(rootNode)

   self.objEquation=ButtonConfig(self)
   self.objEquation.Contents.Text.setValue('New Equation')
   self.objEquation.Contents.Image.setValue('')
   self.objEquation.Contents.lastSelected= 'Text'
   self.objEquation.Drawing_Mode.setValue(1)
   self.objEquation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewEquation (self, wherex, wherey)\n'))
   self.objEquation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objEquation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objEquation.graphObject_ = new_obj
   rootNode.addNode(self.objEquation)
   self.globalAndLocalPostcondition(self.objEquation, rootNode)
   self.globalPrecondition(rootNode)

   self.objOperation=ButtonConfig(self)
   self.objOperation.Contents.Text.setValue('New Operation')
   self.objOperation.Contents.Image.setValue('')
   self.objOperation.Contents.lastSelected= 'Text'
   self.objOperation.Drawing_Mode.setValue(1)
   self.objOperation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOperation (self, wherex, wherey)\n'))
   self.objOperation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objOperation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objOperation.graphObject_ = new_obj
   rootNode.addNode(self.objOperation)
   self.globalAndLocalPostcondition(self.objOperation, rootNode)
   self.globalPrecondition(rootNode)

   self.objAdd=ButtonConfig(self)
   self.objAdd.Contents.Text.setValue('New Add')
   self.objAdd.Contents.Image.setValue('')
   self.objAdd.Contents.lastSelected= 'Text'
   self.objAdd.Drawing_Mode.setValue(1)
   self.objAdd.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAdd (self, wherex, wherey)\n'))
   self.objAdd.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objAdd)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAdd.graphObject_ = new_obj
   rootNode.addNode(self.objAdd)
   self.globalAndLocalPostcondition(self.objAdd, rootNode)
   self.globalPrecondition(rootNode)

   self.objSubtract=ButtonConfig(self)
   self.objSubtract.Contents.Text.setValue('New Subtract')
   self.objSubtract.Contents.Image.setValue('')
   self.objSubtract.Contents.lastSelected= 'Text'
   self.objSubtract.Drawing_Mode.setValue(1)
   self.objSubtract.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSubtract (self, wherex, wherey)\n'))
   self.objSubtract.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objSubtract)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSubtract.graphObject_ = new_obj
   rootNode.addNode(self.objSubtract)
   self.globalAndLocalPostcondition(self.objSubtract, rootNode)
   self.globalPrecondition(rootNode)

   self.objConcat=ButtonConfig(self)
   self.objConcat.Contents.Text.setValue('New Concat')
   self.objConcat.Contents.Image.setValue('')
   self.objConcat.Contents.lastSelected= 'Text'
   self.objConcat.Drawing_Mode.setValue(1)
   self.objConcat.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewConcat (self, wherex, wherey)\n'))
   self.objConcat.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objConcat)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objConcat.graphObject_ = new_obj
   rootNode.addNode(self.objConcat)
   self.globalAndLocalPostcondition(self.objConcat, rootNode)
   self.globalPrecondition(rootNode)

   self.objConstant=ButtonConfig(self)
   self.objConstant.Contents.Text.setValue('New Constant')
   self.objConstant.Contents.Image.setValue('')
   self.objConstant.Contents.lastSelected= 'Text'
   self.objConstant.Drawing_Mode.setValue(1)
   self.objConstant.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewConstant (self, wherex, wherey)\n'))
   self.objConstant.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objConstant)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objConstant.graphObject_ = new_obj
   rootNode.addNode(self.objConstant)
   self.globalAndLocalPostcondition(self.objConstant, rootNode)

newfunction = UMLRT2Kiltera_MM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
