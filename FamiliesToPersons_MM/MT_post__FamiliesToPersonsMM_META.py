"""
__MT_post__FamiliesToPersonsMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Apr 17 14:23:57 2015
___________________________________________________________________________________________
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
def MT_post__FamiliesToPersonsMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_post__FamiliesToPersonsMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_post__FamiliesToPersonsMM_MM.py' )
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
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__MetaModelElement_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__MetaModelElement_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__MetaModelElement_S)
   self.globalAndLocalPostcondition(self.objMT_post__MetaModelElement_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__HouseholdRoot=ButtonConfig(self)
   self.objMT_post__HouseholdRoot.Contents.Text.setValue('New HouseholdRoot')
   self.objMT_post__HouseholdRoot.Contents.Image.setValue('')
   self.objMT_post__HouseholdRoot.Contents.lastSelected= 'Text'
   self.objMT_post__HouseholdRoot.Drawing_Mode.setValue(1)
   self.objMT_post__HouseholdRoot.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__HouseholdRoot (self, wherex, wherey)\n'))
   self.objMT_post__HouseholdRoot.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__HouseholdRoot)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__HouseholdRoot.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__HouseholdRoot)
   self.globalAndLocalPostcondition(self.objMT_post__HouseholdRoot, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Family=ButtonConfig(self)
   self.objMT_post__Family.Contents.Text.setValue('New Family')
   self.objMT_post__Family.Contents.Image.setValue('')
   self.objMT_post__Family.Contents.lastSelected= 'Text'
   self.objMT_post__Family.Drawing_Mode.setValue(1)
   self.objMT_post__Family.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Family (self, wherex, wherey)\n'))
   self.objMT_post__Family.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Family)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Family.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Family)
   self.globalAndLocalPostcondition(self.objMT_post__Family, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Member=ButtonConfig(self)
   self.objMT_post__Member.Contents.Text.setValue('New Member')
   self.objMT_post__Member.Contents.Image.setValue('')
   self.objMT_post__Member.Contents.lastSelected= 'Text'
   self.objMT_post__Member.Drawing_Mode.setValue(1)
   self.objMT_post__Member.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Member (self, wherex, wherey)\n'))
   self.objMT_post__Member.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Member)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Member.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Member)
   self.globalAndLocalPostcondition(self.objMT_post__Member, rootNode)
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
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__MatchModel)
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
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__ApplyModel)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__ApplyModel.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__ApplyModel)
   self.globalAndLocalPostcondition(self.objMT_post__ApplyModel, rootNode)
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

   self.objMT_post__CommunityRoot=ButtonConfig(self)
   self.objMT_post__CommunityRoot.Contents.Text.setValue('New CommunityRoot')
   self.objMT_post__CommunityRoot.Contents.Image.setValue('')
   self.objMT_post__CommunityRoot.Contents.lastSelected= 'Text'
   self.objMT_post__CommunityRoot.Drawing_Mode.setValue(1)
   self.objMT_post__CommunityRoot.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__CommunityRoot (self, wherex, wherey)\n'))
   self.objMT_post__CommunityRoot.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__CommunityRoot)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__CommunityRoot.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__CommunityRoot)
   self.globalAndLocalPostcondition(self.objMT_post__CommunityRoot, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Person=ButtonConfig(self)
   self.objMT_post__Person.Contents.Text.setValue('New Person')
   self.objMT_post__Person.Contents.Image.setValue('')
   self.objMT_post__Person.Contents.lastSelected= 'Text'
   self.objMT_post__Person.Drawing_Mode.setValue(1)
   self.objMT_post__Person.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Person (self, wherex, wherey)\n'))
   self.objMT_post__Person.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Person)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Person.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Person)
   self.globalAndLocalPostcondition(self.objMT_post__Person, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Man=ButtonConfig(self)
   self.objMT_post__Man.Contents.Text.setValue('New Man')
   self.objMT_post__Man.Contents.Image.setValue('')
   self.objMT_post__Man.Contents.lastSelected= 'Text'
   self.objMT_post__Man.Drawing_Mode.setValue(1)
   self.objMT_post__Man.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Man (self, wherex, wherey)\n'))
   self.objMT_post__Man.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Man)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Man.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Man)
   self.globalAndLocalPostcondition(self.objMT_post__Man, rootNode)
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
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Attribute)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Attribute.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Attribute)
   self.globalAndLocalPostcondition(self.objMT_post__Attribute, rootNode)
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

   self.objMT_post__Expression=ButtonConfig(self)
   self.objMT_post__Expression.Contents.Text.setValue('New Expression')
   self.objMT_post__Expression.Contents.Image.setValue('')
   self.objMT_post__Expression.Contents.lastSelected= 'Text'
   self.objMT_post__Expression.Drawing_Mode.setValue(1)
   self.objMT_post__Expression.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Expression (self, wherex, wherey)\n'))
   self.objMT_post__Expression.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Expression)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Expression.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Expression)
   self.globalAndLocalPostcondition(self.objMT_post__Expression, rootNode)
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

   self.objMT_post__Concat=ButtonConfig(self)
   self.objMT_post__Concat.Contents.Text.setValue('New Concat')
   self.objMT_post__Concat.Contents.Image.setValue('')
   self.objMT_post__Concat.Contents.lastSelected= 'Text'
   self.objMT_post__Concat.Drawing_Mode.setValue(1)
   self.objMT_post__Concat.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Concat (self, wherex, wherey)\n'))
   self.objMT_post__Concat.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Concat)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Concat.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Concat)
   self.globalAndLocalPostcondition(self.objMT_post__Concat, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Woman=ButtonConfig(self)
   self.objMT_post__Woman.Contents.Text.setValue('New Woman')
   self.objMT_post__Woman.Contents.Image.setValue('')
   self.objMT_post__Woman.Contents.lastSelected= 'Text'
   self.objMT_post__Woman.Drawing_Mode.setValue(1)
   self.objMT_post__Woman.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Woman (self, wherex, wherey)\n'))
   self.objMT_post__Woman.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Woman)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Woman.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Woman)
   self.globalAndLocalPostcondition(self.objMT_post__Woman, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__GenericNode_FamiliesToPersonsMM=ButtonConfig(self)
   self.objMT_post__GenericNode_FamiliesToPersonsMM.Contents.Text.setValue('New GenericNode')
   self.objMT_post__GenericNode_FamiliesToPersonsMM.Contents.Image.setValue('')
   self.objMT_post__GenericNode_FamiliesToPersonsMM.Contents.lastSelected= 'Text'
   self.objMT_post__GenericNode_FamiliesToPersonsMM.Drawing_Mode.setValue(1)
   self.objMT_post__GenericNode_FamiliesToPersonsMM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__GenericNode_FamiliesToPersonsMM (self, wherex, wherey)\n'))
   self.objMT_post__GenericNode_FamiliesToPersonsMM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__GenericNode_FamiliesToPersonsMM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__GenericNode_FamiliesToPersonsMM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__GenericNode_FamiliesToPersonsMM)
   self.globalAndLocalPostcondition(self.objMT_post__GenericNode_FamiliesToPersonsMM, rootNode)

newfunction = MT_post__FamiliesToPersonsMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
