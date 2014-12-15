"""
__PoliceStationMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Dec 12 15:16:09 2014
______________________________________________________________________________
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
def PoliceStationMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('PoliceStationMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'PoliceStationMM_MM.py' )


   self.globalPrecondition(rootNode)

   self.objEdit=ButtonConfig(self)
   self.objEdit.Contents.Text.setValue('Edit')
   self.objEdit.Contents.Image.setValue('')
   self.objEdit.Contents.lastSelected= 'Text'
   self.objEdit.Drawing_Mode.setValue(0)
   self.objEdit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("PoliceStationMM_META")) ') )
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
   self.objHelp.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["PoliceStationMM_METAHelp.txt"])\n ') )
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

   self.objMetaModelElement_S=ButtonConfig(self)
   self.objMetaModelElement_S.Contents.Text.setValue('New MetaModelElement_S')
   self.objMetaModelElement_S.Contents.Image.setValue('')
   self.objMetaModelElement_S.Contents.lastSelected= 'Text'
   self.objMetaModelElement_S.Drawing_Mode.setValue(1)
   self.objMetaModelElement_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMetaModelElement_S (self, wherex, wherey)\n'))
   self.objMetaModelElement_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMetaModelElement_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMetaModelElement_S.graphObject_ = new_obj
   rootNode.addNode(self.objMetaModelElement_S)
   self.globalAndLocalPostcondition(self.objMetaModelElement_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objStation_S=ButtonConfig(self)
   self.objStation_S.Contents.Text.setValue('New Station_S')
   self.objStation_S.Contents.Image.setValue('')
   self.objStation_S.Contents.lastSelected= 'Text'
   self.objStation_S.Drawing_Mode.setValue(1)
   self.objStation_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStation_S (self, wherex, wherey)\n'))
   self.objStation_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objStation_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objStation_S.graphObject_ = new_obj
   rootNode.addNode(self.objStation_S)
   self.globalAndLocalPostcondition(self.objStation_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMale_S=ButtonConfig(self)
   self.objMale_S.Contents.Text.setValue('New Male_S')
   self.objMale_S.Contents.Image.setValue('')
   self.objMale_S.Contents.lastSelected= 'Text'
   self.objMale_S.Drawing_Mode.setValue(1)
   self.objMale_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMale_S (self, wherex, wherey)\n'))
   self.objMale_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMale_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMale_S.graphObject_ = new_obj
   rootNode.addNode(self.objMale_S)
   self.globalAndLocalPostcondition(self.objMale_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objFemale_S=ButtonConfig(self)
   self.objFemale_S.Contents.Text.setValue('New Female_S')
   self.objFemale_S.Contents.Image.setValue('')
   self.objFemale_S.Contents.lastSelected= 'Text'
   self.objFemale_S.Drawing_Mode.setValue(1)
   self.objFemale_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewFemale_S (self, wherex, wherey)\n'))
   self.objFemale_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objFemale_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objFemale_S.graphObject_ = new_obj
   rootNode.addNode(self.objFemale_S)
   self.globalAndLocalPostcondition(self.objFemale_S, rootNode)
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
      new_obj = graph_ButtonConfig(10, 10,self.objMatchModel)
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
      new_obj = graph_ButtonConfig(135, 80,self.objApplyModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objApplyModel.graphObject_ = new_obj
   rootNode.addNode(self.objApplyModel)
   self.globalAndLocalPostcondition(self.objApplyModel, rootNode)
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

   self.objStation_T=ButtonConfig(self)
   self.objStation_T.Contents.Text.setValue('New Station_T')
   self.objStation_T.Contents.Image.setValue('')
   self.objStation_T.Contents.lastSelected= 'Text'
   self.objStation_T.Drawing_Mode.setValue(1)
   self.objStation_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStation_T (self, wherex, wherey)\n'))
   self.objStation_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objStation_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objStation_T.graphObject_ = new_obj
   rootNode.addNode(self.objStation_T)
   self.globalAndLocalPostcondition(self.objStation_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMale_T=ButtonConfig(self)
   self.objMale_T.Contents.Text.setValue('New Male_T')
   self.objMale_T.Contents.Image.setValue('')
   self.objMale_T.Contents.lastSelected= 'Text'
   self.objMale_T.Drawing_Mode.setValue(1)
   self.objMale_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMale_T (self, wherex, wherey)\n'))
   self.objMale_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMale_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMale_T.graphObject_ = new_obj
   rootNode.addNode(self.objMale_T)
   self.globalAndLocalPostcondition(self.objMale_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objFemale_T=ButtonConfig(self)
   self.objFemale_T.Contents.Text.setValue('New Female_T')
   self.objFemale_T.Contents.Image.setValue('')
   self.objFemale_T.Contents.lastSelected= 'Text'
   self.objFemale_T.Drawing_Mode.setValue(1)
   self.objFemale_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewFemale_T (self, wherex, wherey)\n'))
   self.objFemale_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objFemale_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objFemale_T.graphObject_ = new_obj
   rootNode.addNode(self.objFemale_T)
   self.globalAndLocalPostcondition(self.objFemale_T, rootNode)
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
      new_obj = graph_ButtonConfig(10, 10,self.objAttribute)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAttribute.graphObject_ = new_obj
   rootNode.addNode(self.objAttribute)
   self.globalAndLocalPostcondition(self.objAttribute, rootNode)
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

   self.objExpression=ButtonConfig(self)
   self.objExpression.Contents.Text.setValue('New Expression')
   self.objExpression.Contents.Image.setValue('')
   self.objExpression.Contents.lastSelected= 'Text'
   self.objExpression.Drawing_Mode.setValue(1)
   self.objExpression.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewExpression (self, wherex, wherey)\n'))
   self.objExpression.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objExpression)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objExpression.graphObject_ = new_obj
   rootNode.addNode(self.objExpression)
   self.globalAndLocalPostcondition(self.objExpression, rootNode)
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
      new_obj = graph_ButtonConfig(135, 80,self.objConcat)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objConcat.graphObject_ = new_obj
   rootNode.addNode(self.objConcat)
   self.globalAndLocalPostcondition(self.objConcat, rootNode)

newfunction = PoliceStationMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
