"""
__MT_post__PoliceStationMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Dec 12 15:21:35 2014
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
def MT_post__PoliceStationMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_post__PoliceStationMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_post__PoliceStationMM_MM.py' )
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

   self.objMT_post__Station_S=ButtonConfig(self)
   self.objMT_post__Station_S.Contents.Text.setValue('New Station_S')
   self.objMT_post__Station_S.Contents.Image.setValue('')
   self.objMT_post__Station_S.Contents.lastSelected= 'Text'
   self.objMT_post__Station_S.Drawing_Mode.setValue(1)
   self.objMT_post__Station_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Station_S (self, wherex, wherey)\n'))
   self.objMT_post__Station_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Station_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Station_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Station_S)
   self.globalAndLocalPostcondition(self.objMT_post__Station_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Male_S=ButtonConfig(self)
   self.objMT_post__Male_S.Contents.Text.setValue('New Male_S')
   self.objMT_post__Male_S.Contents.Image.setValue('')
   self.objMT_post__Male_S.Contents.lastSelected= 'Text'
   self.objMT_post__Male_S.Drawing_Mode.setValue(1)
   self.objMT_post__Male_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Male_S (self, wherex, wherey)\n'))
   self.objMT_post__Male_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Male_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Male_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Male_S)
   self.globalAndLocalPostcondition(self.objMT_post__Male_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Female_S=ButtonConfig(self)
   self.objMT_post__Female_S.Contents.Text.setValue('New Female_S')
   self.objMT_post__Female_S.Contents.Image.setValue('')
   self.objMT_post__Female_S.Contents.lastSelected= 'Text'
   self.objMT_post__Female_S.Drawing_Mode.setValue(1)
   self.objMT_post__Female_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Female_S (self, wherex, wherey)\n'))
   self.objMT_post__Female_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Female_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Female_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Female_S)
   self.globalAndLocalPostcondition(self.objMT_post__Female_S, rootNode)
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

   self.objMT_post__Station_T=ButtonConfig(self)
   self.objMT_post__Station_T.Contents.Text.setValue('New Station_T')
   self.objMT_post__Station_T.Contents.Image.setValue('')
   self.objMT_post__Station_T.Contents.lastSelected= 'Text'
   self.objMT_post__Station_T.Drawing_Mode.setValue(1)
   self.objMT_post__Station_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Station_T (self, wherex, wherey)\n'))
   self.objMT_post__Station_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_post__Station_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Station_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Station_T)
   self.globalAndLocalPostcondition(self.objMT_post__Station_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Male_T=ButtonConfig(self)
   self.objMT_post__Male_T.Contents.Text.setValue('New Male_T')
   self.objMT_post__Male_T.Contents.Image.setValue('')
   self.objMT_post__Male_T.Contents.lastSelected= 'Text'
   self.objMT_post__Male_T.Drawing_Mode.setValue(1)
   self.objMT_post__Male_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Male_T (self, wherex, wherey)\n'))
   self.objMT_post__Male_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_post__Male_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Male_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Male_T)
   self.globalAndLocalPostcondition(self.objMT_post__Male_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_post__Female_T=ButtonConfig(self)
   self.objMT_post__Female_T.Contents.Text.setValue('New Female_T')
   self.objMT_post__Female_T.Contents.Image.setValue('')
   self.objMT_post__Female_T.Contents.lastSelected= 'Text'
   self.objMT_post__Female_T.Drawing_Mode.setValue(1)
   self.objMT_post__Female_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__Female_T (self, wherex, wherey)\n'))
   self.objMT_post__Female_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__Female_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__Female_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__Female_T)
   self.globalAndLocalPostcondition(self.objMT_post__Female_T, rootNode)
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

   self.objMT_post__GenericNode_PoliceStationMM=ButtonConfig(self)
   self.objMT_post__GenericNode_PoliceStationMM.Contents.Text.setValue('New GenericNode')
   self.objMT_post__GenericNode_PoliceStationMM.Contents.Image.setValue('')
   self.objMT_post__GenericNode_PoliceStationMM.Contents.lastSelected= 'Text'
   self.objMT_post__GenericNode_PoliceStationMM.Drawing_Mode.setValue(1)
   self.objMT_post__GenericNode_PoliceStationMM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_post__GenericNode_PoliceStationMM (self, wherex, wherey)\n'))
   self.objMT_post__GenericNode_PoliceStationMM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_post__GenericNode_PoliceStationMM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_post__GenericNode_PoliceStationMM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_post__GenericNode_PoliceStationMM)
   self.globalAndLocalPostcondition(self.objMT_post__GenericNode_PoliceStationMM, rootNode)

newfunction = MT_post__PoliceStationMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
