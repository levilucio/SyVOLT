"""
__MT_pre__PoliceStationMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Dec 12 15:21:01 2014
______________________________________________________________________________________
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
def MT_pre__PoliceStationMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('MT_pre__PoliceStationMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'MT_pre__PoliceStationMM_MM.py' )
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

   self.objMT_pre__Station_S=ButtonConfig(self)
   self.objMT_pre__Station_S.Contents.Text.setValue('New Station_S')
   self.objMT_pre__Station_S.Contents.Image.setValue('')
   self.objMT_pre__Station_S.Contents.lastSelected= 'Text'
   self.objMT_pre__Station_S.Drawing_Mode.setValue(1)
   self.objMT_pre__Station_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Station_S (self, wherex, wherey)\n'))
   self.objMT_pre__Station_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Station_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Station_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Station_S)
   self.globalAndLocalPostcondition(self.objMT_pre__Station_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Male_S=ButtonConfig(self)
   self.objMT_pre__Male_S.Contents.Text.setValue('New Male_S')
   self.objMT_pre__Male_S.Contents.Image.setValue('')
   self.objMT_pre__Male_S.Contents.lastSelected= 'Text'
   self.objMT_pre__Male_S.Drawing_Mode.setValue(1)
   self.objMT_pre__Male_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Male_S (self, wherex, wherey)\n'))
   self.objMT_pre__Male_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Male_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Male_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Male_S)
   self.globalAndLocalPostcondition(self.objMT_pre__Male_S, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Female_S=ButtonConfig(self)
   self.objMT_pre__Female_S.Contents.Text.setValue('New Female_S')
   self.objMT_pre__Female_S.Contents.Image.setValue('')
   self.objMT_pre__Female_S.Contents.lastSelected= 'Text'
   self.objMT_pre__Female_S.Drawing_Mode.setValue(1)
   self.objMT_pre__Female_S.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Female_S (self, wherex, wherey)\n'))
   self.objMT_pre__Female_S.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Female_S)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Female_S.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Female_S)
   self.globalAndLocalPostcondition(self.objMT_pre__Female_S, rootNode)
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

   self.objMT_pre__Station_T=ButtonConfig(self)
   self.objMT_pre__Station_T.Contents.Text.setValue('New Station_T')
   self.objMT_pre__Station_T.Contents.Image.setValue('')
   self.objMT_pre__Station_T.Contents.lastSelected= 'Text'
   self.objMT_pre__Station_T.Drawing_Mode.setValue(1)
   self.objMT_pre__Station_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Station_T (self, wherex, wherey)\n'))
   self.objMT_pre__Station_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Station_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Station_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Station_T)
   self.globalAndLocalPostcondition(self.objMT_pre__Station_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Male_T=ButtonConfig(self)
   self.objMT_pre__Male_T.Contents.Text.setValue('New Male_T')
   self.objMT_pre__Male_T.Contents.Image.setValue('')
   self.objMT_pre__Male_T.Contents.lastSelected= 'Text'
   self.objMT_pre__Male_T.Drawing_Mode.setValue(1)
   self.objMT_pre__Male_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Male_T (self, wherex, wherey)\n'))
   self.objMT_pre__Male_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Male_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Male_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Male_T)
   self.globalAndLocalPostcondition(self.objMT_pre__Male_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Female_T=ButtonConfig(self)
   self.objMT_pre__Female_T.Contents.Text.setValue('New Female_T')
   self.objMT_pre__Female_T.Contents.Image.setValue('')
   self.objMT_pre__Female_T.Contents.lastSelected= 'Text'
   self.objMT_pre__Female_T.Drawing_Mode.setValue(1)
   self.objMT_pre__Female_T.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Female_T (self, wherex, wherey)\n'))
   self.objMT_pre__Female_T.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Female_T)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Female_T.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Female_T)
   self.globalAndLocalPostcondition(self.objMT_pre__Female_T, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Attribute=ButtonConfig(self)
   self.objMT_pre__Attribute.Contents.Text.setValue('New Attribute')
   self.objMT_pre__Attribute.Contents.Image.setValue('')
   self.objMT_pre__Attribute.Contents.lastSelected= 'Text'
   self.objMT_pre__Attribute.Drawing_Mode.setValue(1)
   self.objMT_pre__Attribute.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Attribute (self, wherex, wherey)\n'))
   self.objMT_pre__Attribute.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Attribute)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Attribute.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Attribute)
   self.globalAndLocalPostcondition(self.objMT_pre__Attribute, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Equation=ButtonConfig(self)
   self.objMT_pre__Equation.Contents.Text.setValue('New Equation')
   self.objMT_pre__Equation.Contents.Image.setValue('')
   self.objMT_pre__Equation.Contents.lastSelected= 'Text'
   self.objMT_pre__Equation.Drawing_Mode.setValue(1)
   self.objMT_pre__Equation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Equation (self, wherex, wherey)\n'))
   self.objMT_pre__Equation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Equation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Equation.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Equation)
   self.globalAndLocalPostcondition(self.objMT_pre__Equation, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Expression=ButtonConfig(self)
   self.objMT_pre__Expression.Contents.Text.setValue('New Expression')
   self.objMT_pre__Expression.Contents.Image.setValue('')
   self.objMT_pre__Expression.Contents.lastSelected= 'Text'
   self.objMT_pre__Expression.Drawing_Mode.setValue(1)
   self.objMT_pre__Expression.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Expression (self, wherex, wherey)\n'))
   self.objMT_pre__Expression.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__Expression)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Expression.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Expression)
   self.globalAndLocalPostcondition(self.objMT_pre__Expression, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Constant=ButtonConfig(self)
   self.objMT_pre__Constant.Contents.Text.setValue('New Constant')
   self.objMT_pre__Constant.Contents.Image.setValue('')
   self.objMT_pre__Constant.Contents.lastSelected= 'Text'
   self.objMT_pre__Constant.Drawing_Mode.setValue(1)
   self.objMT_pre__Constant.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Constant (self, wherex, wherey)\n'))
   self.objMT_pre__Constant.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objMT_pre__Constant)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Constant.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Constant)
   self.globalAndLocalPostcondition(self.objMT_pre__Constant, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__Concat=ButtonConfig(self)
   self.objMT_pre__Concat.Contents.Text.setValue('New Concat')
   self.objMT_pre__Concat.Contents.Image.setValue('')
   self.objMT_pre__Concat.Contents.lastSelected= 'Text'
   self.objMT_pre__Concat.Drawing_Mode.setValue(1)
   self.objMT_pre__Concat.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__Concat (self, wherex, wherey)\n'))
   self.objMT_pre__Concat.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objMT_pre__Concat)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__Concat.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__Concat)
   self.globalAndLocalPostcondition(self.objMT_pre__Concat, rootNode)
   self.globalPrecondition(rootNode)

   self.objMT_pre__GenericNode_PoliceStationMM=ButtonConfig(self)
   self.objMT_pre__GenericNode_PoliceStationMM.Contents.Text.setValue('New GenericNode')
   self.objMT_pre__GenericNode_PoliceStationMM.Contents.Image.setValue('')
   self.objMT_pre__GenericNode_PoliceStationMM.Contents.lastSelected= 'Text'
   self.objMT_pre__GenericNode_PoliceStationMM.Drawing_Mode.setValue(1)
   self.objMT_pre__GenericNode_PoliceStationMM.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMT_pre__GenericNode_PoliceStationMM (self, wherex, wherey)\n'))
   self.objMT_pre__GenericNode_PoliceStationMM.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMT_pre__GenericNode_PoliceStationMM)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMT_pre__GenericNode_PoliceStationMM.graphObject_ = new_obj
   rootNode.addNode(self.objMT_pre__GenericNode_PoliceStationMM)
   self.globalAndLocalPostcondition(self.objMT_pre__GenericNode_PoliceStationMM, rootNode)

newfunction = MT_pre__PoliceStationMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
