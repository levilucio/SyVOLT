"""
__GM2AUTOSAR_MM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Aug  7 22:15:28 2015
____________________________________________________________________________
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
def GM2AUTOSAR_MM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('GM2AUTOSAR_MM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'GM2AUTOSAR_MM_MM.py' )


   self.globalPrecondition(rootNode)

   self.objEdit=ButtonConfig(self)
   self.objEdit.Contents.Text.setValue('Edit')
   self.objEdit.Contents.Image.setValue('')
   self.objEdit.Contents.lastSelected= 'Text'
   self.objEdit.Drawing_Mode.setValue(0)
   self.objEdit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("GM2AUTOSAR_MM_META")) ') )
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
   self.objHelp.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["GM2AUTOSAR_MM_METAHelp.txt"])\n ') )
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

   self.objECU=ButtonConfig(self)
   self.objECU.Contents.Text.setValue('New ECU')
   self.objECU.Contents.Image.setValue('')
   self.objECU.Contents.lastSelected= 'Text'
   self.objECU.Drawing_Mode.setValue(1)
   self.objECU.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewECU (self, wherex, wherey)\n'))
   self.objECU.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objECU)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objECU.graphObject_ = new_obj
   rootNode.addNode(self.objECU)
   self.globalAndLocalPostcondition(self.objECU, rootNode)
   self.globalPrecondition(rootNode)

   self.objVirtualDevice=ButtonConfig(self)
   self.objVirtualDevice.Contents.Text.setValue('New VirtualDevice')
   self.objVirtualDevice.Contents.Image.setValue('')
   self.objVirtualDevice.Contents.lastSelected= 'Text'
   self.objVirtualDevice.Drawing_Mode.setValue(1)
   self.objVirtualDevice.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewVirtualDevice (self, wherex, wherey)\n'))
   self.objVirtualDevice.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objVirtualDevice)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objVirtualDevice.graphObject_ = new_obj
   rootNode.addNode(self.objVirtualDevice)
   self.globalAndLocalPostcondition(self.objVirtualDevice, rootNode)
   self.globalPrecondition(rootNode)

   self.objDistributable=ButtonConfig(self)
   self.objDistributable.Contents.Text.setValue('New Distributable')
   self.objDistributable.Contents.Image.setValue('')
   self.objDistributable.Contents.lastSelected= 'Text'
   self.objDistributable.Drawing_Mode.setValue(1)
   self.objDistributable.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewDistributable (self, wherex, wherey)\n'))
   self.objDistributable.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objDistributable)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objDistributable.graphObject_ = new_obj
   rootNode.addNode(self.objDistributable)
   self.globalAndLocalPostcondition(self.objDistributable, rootNode)
   self.globalPrecondition(rootNode)

   self.objExecFrame=ButtonConfig(self)
   self.objExecFrame.Contents.Text.setValue('New ExecFrame')
   self.objExecFrame.Contents.Image.setValue('')
   self.objExecFrame.Contents.lastSelected= 'Text'
   self.objExecFrame.Drawing_Mode.setValue(1)
   self.objExecFrame.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewExecFrame (self, wherex, wherey)\n'))
   self.objExecFrame.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objExecFrame)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objExecFrame.graphObject_ = new_obj
   rootNode.addNode(self.objExecFrame)
   self.globalAndLocalPostcondition(self.objExecFrame, rootNode)
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
      new_obj = graph_ButtonConfig(135, 80,self.objSignal)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSignal.graphObject_ = new_obj
   rootNode.addNode(self.objSignal)
   self.globalAndLocalPostcondition(self.objSignal, rootNode)
   self.globalPrecondition(rootNode)

   self.objSystem=ButtonConfig(self)
   self.objSystem.Contents.Text.setValue('New System')
   self.objSystem.Contents.Image.setValue('')
   self.objSystem.Contents.lastSelected= 'Text'
   self.objSystem.Drawing_Mode.setValue(1)
   self.objSystem.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSystem (self, wherex, wherey)\n'))
   self.objSystem.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objSystem)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSystem.graphObject_ = new_obj
   rootNode.addNode(self.objSystem)
   self.globalAndLocalPostcondition(self.objSystem, rootNode)
   self.globalPrecondition(rootNode)

   self.objSystemMapping=ButtonConfig(self)
   self.objSystemMapping.Contents.Text.setValue('New SystemMapping')
   self.objSystemMapping.Contents.Image.setValue('')
   self.objSystemMapping.Contents.lastSelected= 'Text'
   self.objSystemMapping.Drawing_Mode.setValue(1)
   self.objSystemMapping.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSystemMapping (self, wherex, wherey)\n'))
   self.objSystemMapping.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objSystemMapping)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSystemMapping.graphObject_ = new_obj
   rootNode.addNode(self.objSystemMapping)
   self.globalAndLocalPostcondition(self.objSystemMapping, rootNode)
   self.globalPrecondition(rootNode)

   self.objSoftwareComposition=ButtonConfig(self)
   self.objSoftwareComposition.Contents.Text.setValue('New SoftwareComposition')
   self.objSoftwareComposition.Contents.Image.setValue('')
   self.objSoftwareComposition.Contents.lastSelected= 'Text'
   self.objSoftwareComposition.Drawing_Mode.setValue(1)
   self.objSoftwareComposition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSoftwareComposition (self, wherex, wherey)\n'))
   self.objSoftwareComposition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objSoftwareComposition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSoftwareComposition.graphObject_ = new_obj
   rootNode.addNode(self.objSoftwareComposition)
   self.globalAndLocalPostcondition(self.objSoftwareComposition, rootNode)
   self.globalPrecondition(rootNode)

   self.objCompositionType=ButtonConfig(self)
   self.objCompositionType.Contents.Text.setValue('New CompositionType')
   self.objCompositionType.Contents.Image.setValue('')
   self.objCompositionType.Contents.lastSelected= 'Text'
   self.objCompositionType.Drawing_Mode.setValue(1)
   self.objCompositionType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCompositionType (self, wherex, wherey)\n'))
   self.objCompositionType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objCompositionType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objCompositionType.graphObject_ = new_obj
   rootNode.addNode(self.objCompositionType)
   self.globalAndLocalPostcondition(self.objCompositionType, rootNode)
   self.globalPrecondition(rootNode)

   self.objComponentPrototype=ButtonConfig(self)
   self.objComponentPrototype.Contents.Text.setValue('New ComponentPrototype')
   self.objComponentPrototype.Contents.Image.setValue('')
   self.objComponentPrototype.Contents.lastSelected= 'Text'
   self.objComponentPrototype.Drawing_Mode.setValue(1)
   self.objComponentPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewComponentPrototype (self, wherex, wherey)\n'))
   self.objComponentPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objComponentPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objComponentPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objComponentPrototype)
   self.globalAndLocalPostcondition(self.objComponentPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objPPortPrototype=ButtonConfig(self)
   self.objPPortPrototype.Contents.Text.setValue('New PPortPrototype')
   self.objPPortPrototype.Contents.Image.setValue('')
   self.objPPortPrototype.Contents.lastSelected= 'Text'
   self.objPPortPrototype.Drawing_Mode.setValue(1)
   self.objPPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPPortPrototype (self, wherex, wherey)\n'))
   self.objPPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objPPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objPPortPrototype)
   self.globalAndLocalPostcondition(self.objPPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objRPortPrototype=ButtonConfig(self)
   self.objRPortPrototype.Contents.Text.setValue('New RPortPrototype')
   self.objRPortPrototype.Contents.Image.setValue('')
   self.objRPortPrototype.Contents.lastSelected= 'Text'
   self.objRPortPrototype.Drawing_Mode.setValue(1)
   self.objRPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewRPortPrototype (self, wherex, wherey)\n'))
   self.objRPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objRPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objRPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objRPortPrototype)
   self.globalAndLocalPostcondition(self.objRPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objEcuInstance=ButtonConfig(self)
   self.objEcuInstance.Contents.Text.setValue('New EcuInstance')
   self.objEcuInstance.Contents.Image.setValue('')
   self.objEcuInstance.Contents.lastSelected= 'Text'
   self.objEcuInstance.Drawing_Mode.setValue(1)
   self.objEcuInstance.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewEcuInstance (self, wherex, wherey)\n'))
   self.objEcuInstance.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objEcuInstance)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objEcuInstance.graphObject_ = new_obj
   rootNode.addNode(self.objEcuInstance)
   self.globalAndLocalPostcondition(self.objEcuInstance, rootNode)
   self.globalPrecondition(rootNode)

   self.objSwcToEcuMapping=ButtonConfig(self)
   self.objSwcToEcuMapping.Contents.Text.setValue('New SwcToEcuMapping')
   self.objSwcToEcuMapping.Contents.Image.setValue('')
   self.objSwcToEcuMapping.Contents.lastSelected= 'Text'
   self.objSwcToEcuMapping.Drawing_Mode.setValue(1)
   self.objSwcToEcuMapping.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSwcToEcuMapping (self, wherex, wherey)\n'))
   self.objSwcToEcuMapping.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objSwcToEcuMapping)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSwcToEcuMapping.graphObject_ = new_obj
   rootNode.addNode(self.objSwcToEcuMapping)
   self.globalAndLocalPostcondition(self.objSwcToEcuMapping, rootNode)
   self.globalPrecondition(rootNode)

   self.objSwCompToEcuMapping_component=ButtonConfig(self)
   self.objSwCompToEcuMapping_component.Contents.Text.setValue('New SwCompToEcuMapping_component')
   self.objSwCompToEcuMapping_component.Contents.Image.setValue('')
   self.objSwCompToEcuMapping_component.Contents.lastSelected= 'Text'
   self.objSwCompToEcuMapping_component.Drawing_Mode.setValue(1)
   self.objSwCompToEcuMapping_component.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewSwCompToEcuMapping_component (self, wherex, wherey)\n'))
   self.objSwCompToEcuMapping_component.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objSwCompToEcuMapping_component)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objSwCompToEcuMapping_component.graphObject_ = new_obj
   rootNode.addNode(self.objSwCompToEcuMapping_component)
   self.globalAndLocalPostcondition(self.objSwCompToEcuMapping_component, rootNode)
   self.globalPrecondition(rootNode)

   self.objPortPrototype=ButtonConfig(self)
   self.objPortPrototype.Contents.Text.setValue('New PortPrototype')
   self.objPortPrototype.Contents.Image.setValue('')
   self.objPortPrototype.Contents.lastSelected= 'Text'
   self.objPortPrototype.Drawing_Mode.setValue(1)
   self.objPortPrototype.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPortPrototype (self, wherex, wherey)\n'))
   self.objPortPrototype.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objPortPrototype)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPortPrototype.graphObject_ = new_obj
   rootNode.addNode(self.objPortPrototype)
   self.globalAndLocalPostcondition(self.objPortPrototype, rootNode)
   self.globalPrecondition(rootNode)

   self.objComponentType=ButtonConfig(self)
   self.objComponentType.Contents.Text.setValue('New ComponentType')
   self.objComponentType.Contents.Image.setValue('')
   self.objComponentType.Contents.lastSelected= 'Text'
   self.objComponentType.Drawing_Mode.setValue(1)
   self.objComponentType.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewComponentType (self, wherex, wherey)\n'))
   self.objComponentType.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objComponentType)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objComponentType.graphObject_ = new_obj
   rootNode.addNode(self.objComponentType)
   self.globalAndLocalPostcondition(self.objComponentType, rootNode)

newfunction = GM2AUTOSAR_MM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
