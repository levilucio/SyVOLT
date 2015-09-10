"""
__MT_pre__GM2AUTOSAR_MM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sun Aug  9 23:45:41 2015
____________________________________________________________________________________
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
def MT_pre__GM2AUTOSAR_MM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_pre__GM2AUTOSAR_MM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_pre__GM2AUTOSAR_MM_MM.py' )
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

   self.objMT_pre__ECU=ButtonConfig(self)
   self.objMT_pre__ECU.Contents.Text.setValue('New ECU')
   self.objMT_pre__ECU.Contents.Image.setValue('')
   self.objMT_pre__ECU.Contents.lastSelected= 'Text'
   self.objMT_pre__ECU.Drawing_Mode.setValue(1)
   self.objMT_pre__ECU.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ECU (self, wherex, wherey)\n'))
   self.objMT_pre__ECU.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__ECU)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ECU.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ECU)
   self.globalAndLocalPostcondition(self.objMT_pre__ECU, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__VirtualDevice=ButtonConfig(self)
   self.objMT_pre__VirtualDevice.Contents.Text.setValue('New VirtualDevice')
   self.objMT_pre__VirtualDevice.Contents.Image.setValue('')
   self.objMT_pre__VirtualDevice.Contents.lastSelected= 'Text'
   self.objMT_pre__VirtualDevice.Drawing_Mode.setValue(1)
   self.objMT_pre__VirtualDevice.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__VirtualDevice (self, wherex, wherey)\n'))
   self.objMT_pre__VirtualDevice.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__VirtualDevice)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__VirtualDevice.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__VirtualDevice)
   self.globalAndLocalPostcondition(self.objMT_pre__VirtualDevice, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Distributable=ButtonConfig(self)
   self.objMT_pre__Distributable.Contents.Text.setValue('New Distributable')
   self.objMT_pre__Distributable.Contents.Image.setValue('')
   self.objMT_pre__Distributable.Contents.lastSelected= 'Text'
   self.objMT_pre__Distributable.Drawing_Mode.setValue(1)
   self.objMT_pre__Distributable.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Distributable (self, wherex, wherey)\n'))
   self.objMT_pre__Distributable.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Distributable)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Distributable.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Distributable)
   self.globalAndLocalPostcondition(self.objMT_pre__Distributable, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ExecFrame=ButtonConfig(self)
   self.objMT_pre__ExecFrame.Contents.Text.setValue('New ExecFrame')
   self.objMT_pre__ExecFrame.Contents.Image.setValue('')
   self.objMT_pre__ExecFrame.Contents.lastSelected= 'Text'
   self.objMT_pre__ExecFrame.Drawing_Mode.setValue(1)
   self.objMT_pre__ExecFrame.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ExecFrame (self, wherex, wherey)\n'))
   self.objMT_pre__ExecFrame.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__ExecFrame)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ExecFrame.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ExecFrame)
   self.globalAndLocalPostcondition(self.objMT_pre__ExecFrame, rootNode)
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
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Signal)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Signal.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Signal)
   self.globalAndLocalPostcondition(self.objMT_pre__Signal, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__System=ButtonConfig(self)
   self.objMT_pre__System.Contents.Text.setValue('New System')
   self.objMT_pre__System.Contents.Image.setValue('')
   self.objMT_pre__System.Contents.lastSelected= 'Text'
   self.objMT_pre__System.Drawing_Mode.setValue(1)
   self.objMT_pre__System.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__System (self, wherex, wherey)\n'))
   self.objMT_pre__System.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__System)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__System.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__System)
   self.globalAndLocalPostcondition(self.objMT_pre__System, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__SystemMapping=ButtonConfig(self)
   self.objMT_pre__SystemMapping.Contents.Text.setValue('New SystemMapping')
   self.objMT_pre__SystemMapping.Contents.Image.setValue('')
   self.objMT_pre__SystemMapping.Contents.lastSelected= 'Text'
   self.objMT_pre__SystemMapping.Drawing_Mode.setValue(1)
   self.objMT_pre__SystemMapping.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__SystemMapping (self, wherex, wherey)\n'))
   self.objMT_pre__SystemMapping.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__SystemMapping)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__SystemMapping.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__SystemMapping)
   self.globalAndLocalPostcondition(self.objMT_pre__SystemMapping, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__SoftwareComposition=ButtonConfig(self)
   self.objMT_pre__SoftwareComposition.Contents.Text.setValue('New SoftwareComposition')
   self.objMT_pre__SoftwareComposition.Contents.Image.setValue('')
   self.objMT_pre__SoftwareComposition.Contents.lastSelected= 'Text'
   self.objMT_pre__SoftwareComposition.Drawing_Mode.setValue(1)
   self.objMT_pre__SoftwareComposition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__SoftwareComposition (self, wherex, wherey)\n'))
   self.objMT_pre__SoftwareComposition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__SoftwareComposition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__SoftwareComposition.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__SoftwareComposition)
   self.globalAndLocalPostcondition(self.objMT_pre__SoftwareComposition, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__CompositionType=ButtonConfig(self)
   self.objMT_pre__CompositionType.Contents.Text.setValue('New CompositionType')
   self.objMT_pre__CompositionType.Contents.Image.setValue('')
   self.objMT_pre__CompositionType.Contents.lastSelected= 'Text'
   self.objMT_pre__CompositionType.Drawing_Mode.setValue(1)
   self.objMT_pre__CompositionType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__CompositionType (self, wherex, wherey)\n'))
   self.objMT_pre__CompositionType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__CompositionType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__CompositionType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__CompositionType)
   self.globalAndLocalPostcondition(self.objMT_pre__CompositionType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ComponentPrototype=ButtonConfig(self)
   self.objMT_pre__ComponentPrototype.Contents.Text.setValue('New ComponentPrototype')
   self.objMT_pre__ComponentPrototype.Contents.Image.setValue('')
   self.objMT_pre__ComponentPrototype.Contents.lastSelected= 'Text'
   self.objMT_pre__ComponentPrototype.Drawing_Mode.setValue(1)
   self.objMT_pre__ComponentPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ComponentPrototype (self, wherex, wherey)\n'))
   self.objMT_pre__ComponentPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__ComponentPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ComponentPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ComponentPrototype)
   self.globalAndLocalPostcondition(self.objMT_pre__ComponentPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PPortPrototype=ButtonConfig(self)
   self.objMT_pre__PPortPrototype.Contents.Text.setValue('New PPortPrototype')
   self.objMT_pre__PPortPrototype.Contents.Image.setValue('')
   self.objMT_pre__PPortPrototype.Contents.lastSelected= 'Text'
   self.objMT_pre__PPortPrototype.Drawing_Mode.setValue(1)
   self.objMT_pre__PPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PPortPrototype (self, wherex, wherey)\n'))
   self.objMT_pre__PPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__PPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PPortPrototype)
   self.globalAndLocalPostcondition(self.objMT_pre__PPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__RPortPrototype=ButtonConfig(self)
   self.objMT_pre__RPortPrototype.Contents.Text.setValue('New RPortPrototype')
   self.objMT_pre__RPortPrototype.Contents.Image.setValue('')
   self.objMT_pre__RPortPrototype.Contents.lastSelected= 'Text'
   self.objMT_pre__RPortPrototype.Drawing_Mode.setValue(1)
   self.objMT_pre__RPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__RPortPrototype (self, wherex, wherey)\n'))
   self.objMT_pre__RPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__RPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__RPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__RPortPrototype)
   self.globalAndLocalPostcondition(self.objMT_pre__RPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__EcuInstance=ButtonConfig(self)
   self.objMT_pre__EcuInstance.Contents.Text.setValue('New EcuInstance')
   self.objMT_pre__EcuInstance.Contents.Image.setValue('')
   self.objMT_pre__EcuInstance.Contents.lastSelected= 'Text'
   self.objMT_pre__EcuInstance.Drawing_Mode.setValue(1)
   self.objMT_pre__EcuInstance.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__EcuInstance (self, wherex, wherey)\n'))
   self.objMT_pre__EcuInstance.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__EcuInstance)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__EcuInstance.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__EcuInstance)
   self.globalAndLocalPostcondition(self.objMT_pre__EcuInstance, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__SwcToEcuMapping=ButtonConfig(self)
   self.objMT_pre__SwcToEcuMapping.Contents.Text.setValue('New SwcToEcuMapping')
   self.objMT_pre__SwcToEcuMapping.Contents.Image.setValue('')
   self.objMT_pre__SwcToEcuMapping.Contents.lastSelected= 'Text'
   self.objMT_pre__SwcToEcuMapping.Drawing_Mode.setValue(1)
   self.objMT_pre__SwcToEcuMapping.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__SwcToEcuMapping (self, wherex, wherey)\n'))
   self.objMT_pre__SwcToEcuMapping.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__SwcToEcuMapping)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__SwcToEcuMapping.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__SwcToEcuMapping)
   self.globalAndLocalPostcondition(self.objMT_pre__SwcToEcuMapping, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__SwCompToEcuMapping_component=ButtonConfig(self)
   self.objMT_pre__SwCompToEcuMapping_component.Contents.Text.setValue('New SwCompToEcuMapping_component')
   self.objMT_pre__SwCompToEcuMapping_component.Contents.Image.setValue('')
   self.objMT_pre__SwCompToEcuMapping_component.Contents.lastSelected= 'Text'
   self.objMT_pre__SwCompToEcuMapping_component.Drawing_Mode.setValue(1)
   self.objMT_pre__SwCompToEcuMapping_component.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__SwCompToEcuMapping_component (self, wherex, wherey)\n'))
   self.objMT_pre__SwCompToEcuMapping_component.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__SwCompToEcuMapping_component)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__SwCompToEcuMapping_component.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__SwCompToEcuMapping_component)
   self.globalAndLocalPostcondition(self.objMT_pre__SwCompToEcuMapping_component, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__PortPrototype=ButtonConfig(self)
   self.objMT_pre__PortPrototype.Contents.Text.setValue('New PortPrototype')
   self.objMT_pre__PortPrototype.Contents.Image.setValue('')
   self.objMT_pre__PortPrototype.Contents.lastSelected= 'Text'
   self.objMT_pre__PortPrototype.Drawing_Mode.setValue(1)
   self.objMT_pre__PortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__PortPrototype (self, wherex, wherey)\n'))
   self.objMT_pre__PortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__PortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__PortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__PortPrototype)
   self.globalAndLocalPostcondition(self.objMT_pre__PortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__ComponentType=ButtonConfig(self)
   self.objMT_pre__ComponentType.Contents.Text.setValue('New ComponentType')
   self.objMT_pre__ComponentType.Contents.Image.setValue('')
   self.objMT_pre__ComponentType.Contents.lastSelected= 'Text'
   self.objMT_pre__ComponentType.Drawing_Mode.setValue(1)
   self.objMT_pre__ComponentType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__ComponentType (self, wherex, wherey)\n'))
   self.objMT_pre__ComponentType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__ComponentType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ComponentType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ComponentType)
   self.globalAndLocalPostcondition(self.objMT_pre__ComponentType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__GenericNode_GM2AUTOSAR_MM=ButtonConfig(self)
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.Contents.Text.setValue('New GenericNode')
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.Contents.Image.setValue('')
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.Contents.lastSelected= 'Text'
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.Drawing_Mode.setValue(1)
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__GenericNode_GM2AUTOSAR_MM (self, wherex, wherey)\n'))
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__GenericNode_GM2AUTOSAR_MM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__GenericNode_GM2AUTOSAR_MM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__GenericNode_GM2AUTOSAR_MM)
   self.globalAndLocalPostcondition(self.objMT_pre__GenericNode_GM2AUTOSAR_MM, rootNode)

newfunction = MT_pre__GM2AUTOSAR_MM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
