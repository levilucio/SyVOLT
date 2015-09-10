"""
__MT_post__GM2AUTOSAR_MM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Sun Aug  9 23:46:08 2015
_____________________________________________________________________________________
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
def MT_post__GM2AUTOSAR_MM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_post__GM2AUTOSAR_MM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_post__GM2AUTOSAR_MM_MM.py' )
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

   self.objMT_post__ECU=ButtonConfig(self)
   self.objMT_post__ECU.Contents.Text.setValue('New ECU')
   self.objMT_post__ECU.Contents.Image.setValue('')
   self.objMT_post__ECU.Contents.lastSelected= 'Text'
   self.objMT_post__ECU.Drawing_Mode.setValue(1)
   self.objMT_post__ECU.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ECU (self, wherex, wherey)\n'))
   self.objMT_post__ECU.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__ECU)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ECU.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ECU)
   self.globalAndLocalPostcondition(self.objMT_post__ECU, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__VirtualDevice=ButtonConfig(self)
   self.objMT_post__VirtualDevice.Contents.Text.setValue('New VirtualDevice')
   self.objMT_post__VirtualDevice.Contents.Image.setValue('')
   self.objMT_post__VirtualDevice.Contents.lastSelected= 'Text'
   self.objMT_post__VirtualDevice.Drawing_Mode.setValue(1)
   self.objMT_post__VirtualDevice.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__VirtualDevice (self, wherex, wherey)\n'))
   self.objMT_post__VirtualDevice.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__VirtualDevice)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__VirtualDevice.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__VirtualDevice)
   self.globalAndLocalPostcondition(self.objMT_post__VirtualDevice, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Distributable=ButtonConfig(self)
   self.objMT_post__Distributable.Contents.Text.setValue('New Distributable')
   self.objMT_post__Distributable.Contents.Image.setValue('')
   self.objMT_post__Distributable.Contents.lastSelected= 'Text'
   self.objMT_post__Distributable.Drawing_Mode.setValue(1)
   self.objMT_post__Distributable.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Distributable (self, wherex, wherey)\n'))
   self.objMT_post__Distributable.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Distributable)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Distributable.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Distributable)
   self.globalAndLocalPostcondition(self.objMT_post__Distributable, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ExecFrame=ButtonConfig(self)
   self.objMT_post__ExecFrame.Contents.Text.setValue('New ExecFrame')
   self.objMT_post__ExecFrame.Contents.Image.setValue('')
   self.objMT_post__ExecFrame.Contents.lastSelected= 'Text'
   self.objMT_post__ExecFrame.Drawing_Mode.setValue(1)
   self.objMT_post__ExecFrame.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ExecFrame (self, wherex, wherey)\n'))
   self.objMT_post__ExecFrame.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__ExecFrame)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ExecFrame.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ExecFrame)
   self.globalAndLocalPostcondition(self.objMT_post__ExecFrame, rootNode)
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
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Signal)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Signal.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Signal)
   self.globalAndLocalPostcondition(self.objMT_post__Signal, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__System=ButtonConfig(self)
   self.objMT_post__System.Contents.Text.setValue('New System')
   self.objMT_post__System.Contents.Image.setValue('')
   self.objMT_post__System.Contents.lastSelected= 'Text'
   self.objMT_post__System.Drawing_Mode.setValue(1)
   self.objMT_post__System.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__System (self, wherex, wherey)\n'))
   self.objMT_post__System.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__System)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__System.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__System)
   self.globalAndLocalPostcondition(self.objMT_post__System, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__SystemMapping=ButtonConfig(self)
   self.objMT_post__SystemMapping.Contents.Text.setValue('New SystemMapping')
   self.objMT_post__SystemMapping.Contents.Image.setValue('')
   self.objMT_post__SystemMapping.Contents.lastSelected= 'Text'
   self.objMT_post__SystemMapping.Drawing_Mode.setValue(1)
   self.objMT_post__SystemMapping.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__SystemMapping (self, wherex, wherey)\n'))
   self.objMT_post__SystemMapping.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__SystemMapping)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__SystemMapping.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__SystemMapping)
   self.globalAndLocalPostcondition(self.objMT_post__SystemMapping, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__SoftwareComposition=ButtonConfig(self)
   self.objMT_post__SoftwareComposition.Contents.Text.setValue('New SoftwareComposition')
   self.objMT_post__SoftwareComposition.Contents.Image.setValue('')
   self.objMT_post__SoftwareComposition.Contents.lastSelected= 'Text'
   self.objMT_post__SoftwareComposition.Drawing_Mode.setValue(1)
   self.objMT_post__SoftwareComposition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__SoftwareComposition (self, wherex, wherey)\n'))
   self.objMT_post__SoftwareComposition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__SoftwareComposition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__SoftwareComposition.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__SoftwareComposition)
   self.globalAndLocalPostcondition(self.objMT_post__SoftwareComposition, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__CompositionType=ButtonConfig(self)
   self.objMT_post__CompositionType.Contents.Text.setValue('New CompositionType')
   self.objMT_post__CompositionType.Contents.Image.setValue('')
   self.objMT_post__CompositionType.Contents.lastSelected= 'Text'
   self.objMT_post__CompositionType.Drawing_Mode.setValue(1)
   self.objMT_post__CompositionType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__CompositionType (self, wherex, wherey)\n'))
   self.objMT_post__CompositionType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__CompositionType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__CompositionType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__CompositionType)
   self.globalAndLocalPostcondition(self.objMT_post__CompositionType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ComponentPrototype=ButtonConfig(self)
   self.objMT_post__ComponentPrototype.Contents.Text.setValue('New ComponentPrototype')
   self.objMT_post__ComponentPrototype.Contents.Image.setValue('')
   self.objMT_post__ComponentPrototype.Contents.lastSelected= 'Text'
   self.objMT_post__ComponentPrototype.Drawing_Mode.setValue(1)
   self.objMT_post__ComponentPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ComponentPrototype (self, wherex, wherey)\n'))
   self.objMT_post__ComponentPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__ComponentPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ComponentPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ComponentPrototype)
   self.globalAndLocalPostcondition(self.objMT_post__ComponentPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PPortPrototype=ButtonConfig(self)
   self.objMT_post__PPortPrototype.Contents.Text.setValue('New PPortPrototype')
   self.objMT_post__PPortPrototype.Contents.Image.setValue('')
   self.objMT_post__PPortPrototype.Contents.lastSelected= 'Text'
   self.objMT_post__PPortPrototype.Drawing_Mode.setValue(1)
   self.objMT_post__PPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PPortPrototype (self, wherex, wherey)\n'))
   self.objMT_post__PPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__PPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PPortPrototype)
   self.globalAndLocalPostcondition(self.objMT_post__PPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__RPortPrototype=ButtonConfig(self)
   self.objMT_post__RPortPrototype.Contents.Text.setValue('New RPortPrototype')
   self.objMT_post__RPortPrototype.Contents.Image.setValue('')
   self.objMT_post__RPortPrototype.Contents.lastSelected= 'Text'
   self.objMT_post__RPortPrototype.Drawing_Mode.setValue(1)
   self.objMT_post__RPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__RPortPrototype (self, wherex, wherey)\n'))
   self.objMT_post__RPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__RPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__RPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__RPortPrototype)
   self.globalAndLocalPostcondition(self.objMT_post__RPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__EcuInstance=ButtonConfig(self)
   self.objMT_post__EcuInstance.Contents.Text.setValue('New EcuInstance')
   self.objMT_post__EcuInstance.Contents.Image.setValue('')
   self.objMT_post__EcuInstance.Contents.lastSelected= 'Text'
   self.objMT_post__EcuInstance.Drawing_Mode.setValue(1)
   self.objMT_post__EcuInstance.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__EcuInstance (self, wherex, wherey)\n'))
   self.objMT_post__EcuInstance.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__EcuInstance)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__EcuInstance.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__EcuInstance)
   self.globalAndLocalPostcondition(self.objMT_post__EcuInstance, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__SwcToEcuMapping=ButtonConfig(self)
   self.objMT_post__SwcToEcuMapping.Contents.Text.setValue('New SwcToEcuMapping')
   self.objMT_post__SwcToEcuMapping.Contents.Image.setValue('')
   self.objMT_post__SwcToEcuMapping.Contents.lastSelected= 'Text'
   self.objMT_post__SwcToEcuMapping.Drawing_Mode.setValue(1)
   self.objMT_post__SwcToEcuMapping.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__SwcToEcuMapping (self, wherex, wherey)\n'))
   self.objMT_post__SwcToEcuMapping.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__SwcToEcuMapping)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__SwcToEcuMapping.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__SwcToEcuMapping)
   self.globalAndLocalPostcondition(self.objMT_post__SwcToEcuMapping, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__SwCompToEcuMapping_component=ButtonConfig(self)
   self.objMT_post__SwCompToEcuMapping_component.Contents.Text.setValue('New SwCompToEcuMapping_component')
   self.objMT_post__SwCompToEcuMapping_component.Contents.Image.setValue('')
   self.objMT_post__SwCompToEcuMapping_component.Contents.lastSelected= 'Text'
   self.objMT_post__SwCompToEcuMapping_component.Drawing_Mode.setValue(1)
   self.objMT_post__SwCompToEcuMapping_component.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__SwCompToEcuMapping_component (self, wherex, wherey)\n'))
   self.objMT_post__SwCompToEcuMapping_component.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__SwCompToEcuMapping_component)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__SwCompToEcuMapping_component.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__SwCompToEcuMapping_component)
   self.globalAndLocalPostcondition(self.objMT_post__SwCompToEcuMapping_component, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__PortPrototype=ButtonConfig(self)
   self.objMT_post__PortPrototype.Contents.Text.setValue('New PortPrototype')
   self.objMT_post__PortPrototype.Contents.Image.setValue('')
   self.objMT_post__PortPrototype.Contents.lastSelected= 'Text'
   self.objMT_post__PortPrototype.Drawing_Mode.setValue(1)
   self.objMT_post__PortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__PortPrototype (self, wherex, wherey)\n'))
   self.objMT_post__PortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__PortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__PortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__PortPrototype)
   self.globalAndLocalPostcondition(self.objMT_post__PortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__ComponentType=ButtonConfig(self)
   self.objMT_post__ComponentType.Contents.Text.setValue('New ComponentType')
   self.objMT_post__ComponentType.Contents.Image.setValue('')
   self.objMT_post__ComponentType.Contents.lastSelected= 'Text'
   self.objMT_post__ComponentType.Drawing_Mode.setValue(1)
   self.objMT_post__ComponentType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__ComponentType (self, wherex, wherey)\n'))
   self.objMT_post__ComponentType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__ComponentType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ComponentType.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ComponentType)
   self.globalAndLocalPostcondition(self.objMT_post__ComponentType, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__GenericNode_GM2AUTOSAR_MM=ButtonConfig(self)
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.Contents.Text.setValue('New GenericNode')
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.Contents.Image.setValue('')
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.Contents.lastSelected= 'Text'
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.Drawing_Mode.setValue(1)
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__GenericNode_GM2AUTOSAR_MM (self, wherex, wherey)\n'))
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__GenericNode_GM2AUTOSAR_MM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__GenericNode_GM2AUTOSAR_MM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__GenericNode_GM2AUTOSAR_MM)
   self.globalAndLocalPostcondition(self.objMT_post__GenericNode_GM2AUTOSAR_MM, rootNode)

newfunction = MT_post__GM2AUTOSAR_MM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
