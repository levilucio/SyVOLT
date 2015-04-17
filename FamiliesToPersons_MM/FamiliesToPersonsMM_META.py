"""
__FamiliesToPersonsMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Apr 17 11:06:52 2015
__________________________________________________________________________________
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
def FamiliesToPersonsMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('FamiliesToPersonsMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'FamiliesToPersonsMM_MM.py' )


   self.globalPrecondition(rootNode)

   self.objEdit=ButtonConfig(self)
   self.objEdit.Contents.Text.setValue('Edit')
   self.objEdit.Contents.Image.setValue('')
   self.objEdit.Contents.lastSelected= 'Text'
   self.objEdit.Drawing_Mode.setValue(0)
   self.objEdit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("FamiliesToPersonsMM_META")) ') )
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
   self.objHelp.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["FamiliesToPersonsMM_METAHelp.txt"])\n ') )
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

   self.objHouseholdRoot=ButtonConfig(self)
   self.objHouseholdRoot.Contents.Text.setValue('New HouseholdRoot')
   self.objHouseholdRoot.Contents.Image.setValue('')
   self.objHouseholdRoot.Contents.lastSelected= 'Text'
   self.objHouseholdRoot.Drawing_Mode.setValue(1)
   self.objHouseholdRoot.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHouseholdRoot (self, wherex, wherey)\n'))
   self.objHouseholdRoot.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objHouseholdRoot)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objHouseholdRoot.graphObject_ = new_obj
   rootNode.addNode(self.objHouseholdRoot)
   self.globalAndLocalPostcondition(self.objHouseholdRoot, rootNode)
   self.globalPrecondition(rootNode)

   self.objFamily=ButtonConfig(self)
   self.objFamily.Contents.Text.setValue('New Family')
   self.objFamily.Contents.Image.setValue('')
   self.objFamily.Contents.lastSelected= 'Text'
   self.objFamily.Drawing_Mode.setValue(1)
   self.objFamily.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewFamily (self, wherex, wherey)\n'))
   self.objFamily.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objFamily)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objFamily.graphObject_ = new_obj
   rootNode.addNode(self.objFamily)
   self.globalAndLocalPostcondition(self.objFamily, rootNode)
   self.globalPrecondition(rootNode)

   self.objMember=ButtonConfig(self)
   self.objMember.Contents.Text.setValue('New Member')
   self.objMember.Contents.Image.setValue('')
   self.objMember.Contents.lastSelected= 'Text'
   self.objMember.Drawing_Mode.setValue(1)
   self.objMember.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMember (self, wherex, wherey)\n'))
   self.objMember.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMember)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMember.graphObject_ = new_obj
   rootNode.addNode(self.objMember)
   self.globalAndLocalPostcondition(self.objMember, rootNode)
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

   self.objCommunityRoot=ButtonConfig(self)
   self.objCommunityRoot.Contents.Text.setValue('New CommunityRoot')
   self.objCommunityRoot.Contents.Image.setValue('')
   self.objCommunityRoot.Contents.lastSelected= 'Text'
   self.objCommunityRoot.Drawing_Mode.setValue(1)
   self.objCommunityRoot.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCommunityRoot (self, wherex, wherey)\n'))
   self.objCommunityRoot.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objCommunityRoot)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objCommunityRoot.graphObject_ = new_obj
   rootNode.addNode(self.objCommunityRoot)
   self.globalAndLocalPostcondition(self.objCommunityRoot, rootNode)
   self.globalPrecondition(rootNode)

   self.objPerson=ButtonConfig(self)
   self.objPerson.Contents.Text.setValue('New Person')
   self.objPerson.Contents.Image.setValue('')
   self.objPerson.Contents.lastSelected= 'Text'
   self.objPerson.Drawing_Mode.setValue(1)
   self.objPerson.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPerson (self, wherex, wherey)\n'))
   self.objPerson.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objPerson)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objPerson.graphObject_ = new_obj
   rootNode.addNode(self.objPerson)
   self.globalAndLocalPostcondition(self.objPerson, rootNode)
   self.globalPrecondition(rootNode)

   self.objMan=ButtonConfig(self)
   self.objMan.Contents.Text.setValue('New Man')
   self.objMan.Contents.Image.setValue('')
   self.objMan.Contents.lastSelected= 'Text'
   self.objMan.Drawing_Mode.setValue(1)
   self.objMan.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMan (self, wherex, wherey)\n'))
   self.objMan.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMan)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMan.graphObject_ = new_obj
   rootNode.addNode(self.objMan)
   self.globalAndLocalPostcondition(self.objMan, rootNode)
   self.globalPrecondition(rootNode)

   self.objWoman=ButtonConfig(self)
   self.objWoman.Contents.Text.setValue('New Woman')
   self.objWoman.Contents.Image.setValue('')
   self.objWoman.Contents.lastSelected= 'Text'
   self.objWoman.Drawing_Mode.setValue(1)
   self.objWoman.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewWoman (self, wherex, wherey)\n'))
   self.objWoman.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objWoman)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objWoman.graphObject_ = new_obj
   rootNode.addNode(self.objWoman)
   self.globalAndLocalPostcondition(self.objWoman, rootNode)

newfunction = FamiliesToPersonsMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
