"""
__MT_pre__FamiliesToPersonsMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Apr 17 11:09:50 2015
__________________________________________________________________________________________
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
def MT_pre__FamiliesToPersonsMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_pre__FamiliesToPersonsMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_pre__FamiliesToPersonsMM_MM.py' )
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
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__MetaModelElement_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__MetaModelElement_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__MetaModelElement_S)
   self.globalAndLocalPostcondition(self.objMT_pre__MetaModelElement_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__HouseholdRoot=ButtonConfig(self)
   self.objMT_pre__HouseholdRoot.Contents.Text.setValue('New HouseholdRoot')
   self.objMT_pre__HouseholdRoot.Contents.Image.setValue('')
   self.objMT_pre__HouseholdRoot.Contents.lastSelected= 'Text'
   self.objMT_pre__HouseholdRoot.Drawing_Mode.setValue(1)
   self.objMT_pre__HouseholdRoot.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__HouseholdRoot (self, wherex, wherey)\n'))
   self.objMT_pre__HouseholdRoot.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__HouseholdRoot)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__HouseholdRoot.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__HouseholdRoot)
   self.globalAndLocalPostcondition(self.objMT_pre__HouseholdRoot, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Family=ButtonConfig(self)
   self.objMT_pre__Family.Contents.Text.setValue('New Family')
   self.objMT_pre__Family.Contents.Image.setValue('')
   self.objMT_pre__Family.Contents.lastSelected= 'Text'
   self.objMT_pre__Family.Drawing_Mode.setValue(1)
   self.objMT_pre__Family.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Family (self, wherex, wherey)\n'))
   self.objMT_pre__Family.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Family)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Family.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Family)
   self.globalAndLocalPostcondition(self.objMT_pre__Family, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Member=ButtonConfig(self)
   self.objMT_pre__Member.Contents.Text.setValue('New Member')
   self.objMT_pre__Member.Contents.Image.setValue('')
   self.objMT_pre__Member.Contents.lastSelected= 'Text'
   self.objMT_pre__Member.Drawing_Mode.setValue(1)
   self.objMT_pre__Member.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Member (self, wherex, wherey)\n'))
   self.objMT_pre__Member.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Member)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Member.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Member)
   self.globalAndLocalPostcondition(self.objMT_pre__Member, rootNode)
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
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__MatchModel)
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
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__ApplyModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__ApplyModel.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__ApplyModel)
   self.globalAndLocalPostcondition(self.objMT_pre__ApplyModel, rootNode)
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

   self.objMT_pre__CommunityRoot=ButtonConfig(self)
   self.objMT_pre__CommunityRoot.Contents.Text.setValue('New CommunityRoot')
   self.objMT_pre__CommunityRoot.Contents.Image.setValue('')
   self.objMT_pre__CommunityRoot.Contents.lastSelected= 'Text'
   self.objMT_pre__CommunityRoot.Drawing_Mode.setValue(1)
   self.objMT_pre__CommunityRoot.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__CommunityRoot (self, wherex, wherey)\n'))
   self.objMT_pre__CommunityRoot.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__CommunityRoot)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__CommunityRoot.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__CommunityRoot)
   self.globalAndLocalPostcondition(self.objMT_pre__CommunityRoot, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Person=ButtonConfig(self)
   self.objMT_pre__Person.Contents.Text.setValue('New Person')
   self.objMT_pre__Person.Contents.Image.setValue('')
   self.objMT_pre__Person.Contents.lastSelected= 'Text'
   self.objMT_pre__Person.Drawing_Mode.setValue(1)
   self.objMT_pre__Person.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Person (self, wherex, wherey)\n'))
   self.objMT_pre__Person.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Person)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Person.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Person)
   self.globalAndLocalPostcondition(self.objMT_pre__Person, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Man=ButtonConfig(self)
   self.objMT_pre__Man.Contents.Text.setValue('New Man')
   self.objMT_pre__Man.Contents.Image.setValue('')
   self.objMT_pre__Man.Contents.lastSelected= 'Text'
   self.objMT_pre__Man.Drawing_Mode.setValue(1)
   self.objMT_pre__Man.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Man (self, wherex, wherey)\n'))
   self.objMT_pre__Man.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Man)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Man.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Man)
   self.globalAndLocalPostcondition(self.objMT_pre__Man, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Woman=ButtonConfig(self)
   self.objMT_pre__Woman.Contents.Text.setValue('New Woman')
   self.objMT_pre__Woman.Contents.Image.setValue('')
   self.objMT_pre__Woman.Contents.lastSelected= 'Text'
   self.objMT_pre__Woman.Drawing_Mode.setValue(1)
   self.objMT_pre__Woman.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Woman (self, wherex, wherey)\n'))
   self.objMT_pre__Woman.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Woman)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Woman.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Woman)
   self.globalAndLocalPostcondition(self.objMT_pre__Woman, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__GenericNode_FamiliesToPersonsMM=ButtonConfig(self)
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.Contents.Text.setValue('New GenericNode')
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.Contents.Image.setValue('')
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.Contents.lastSelected= 'Text'
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.Drawing_Mode.setValue(1)
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__GenericNode_FamiliesToPersonsMM (self, wherex, wherey)\n'))
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__GenericNode_FamiliesToPersonsMM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__GenericNode_FamiliesToPersonsMM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__GenericNode_FamiliesToPersonsMM)
   self.globalAndLocalPostcondition(self.objMT_pre__GenericNode_FamiliesToPersonsMM, rootNode)

newfunction = MT_pre__FamiliesToPersonsMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
