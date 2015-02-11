"""
__Transition2QInstOUT_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:29:20 2015
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from Vertex import *
from Transition import *
from StateMachine import *
from OUT2 import *
from Name import *
from Inst import *
from Attribute import *
from Equation import *
from Concat import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from directLink_S import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from hasArgs import *
from graph_StateMachine import *
from graph_Attribute import *
from graph_Vertex import *
from graph_Transition import *
from graph_paired_with import *
from graph_Equation import *
from graph_hasArgs import *
from graph_rightExpr import *
from graph_Concat import *
from graph_Inst import *
from graph_hasAttribute_T import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_OUT2 import *
from graph_ApplyModel import *
from graph_Name import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_hasAttribute_S import *
from graph_match_contains import *
from graph_leftExpr import *
from graph_Constant import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def Transition2QInstOUT_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2QInstOUT')
    # --- ASG attributes over ---


    self.obj1138=MatchModel(self)
    self.obj1138.isGraphObjectVisual = True

    if(hasattr(self.obj1138, '_setHierarchicalLink')):
      self.obj1138._setHierarchicalLink(False)

    self.obj1138.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1138)
    self.globalAndLocalPostcondition(self.obj1138, rootNode)
    self.obj1138.postAction( rootNode.CREATE )

    self.obj1139=ApplyModel(self)
    self.obj1139.isGraphObjectVisual = True

    if(hasattr(self.obj1139, '_setHierarchicalLink')):
      self.obj1139._setHierarchicalLink(False)

    self.obj1139.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,240.0,self.obj1139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1139)
    self.globalAndLocalPostcondition(self.obj1139, rootNode)
    self.obj1139.postAction( rootNode.CREATE )

    self.obj1140=Vertex(self)
    self.obj1140.isGraphObjectVisual = True

    if(hasattr(self.obj1140, '_setHierarchicalLink')):
      self.obj1140._setHierarchicalLink(False)

    # name
    self.obj1140.name.setValue('vertex1')

    # classtype
    self.obj1140.classtype.setValue('Vertex')

    # cardinality
    self.obj1140.cardinality.setValue('1')

    self.obj1140.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,120.0,self.obj1140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1140)
    self.globalAndLocalPostcondition(self.obj1140, rootNode)
    self.obj1140.postAction( rootNode.CREATE )

    self.obj1141=Transition(self)
    self.obj1141.isGraphObjectVisual = True

    if(hasattr(self.obj1141, '_setHierarchicalLink')):
      self.obj1141._setHierarchicalLink(False)

    # name
    self.obj1141.name.setValue('transition1')

    # classtype
    self.obj1141.classtype.setValue('Transition')

    # cardinality
    self.obj1141.cardinality.setValue('+')

    self.obj1141.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(160.0,34.0,self.obj1141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.9699999999999989, 0.8599999999999994]
    else: new_obj = None
    self.obj1141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1141)
    self.globalAndLocalPostcondition(self.obj1141, rootNode)
    self.obj1141.postAction( rootNode.CREATE )

    self.obj1142=StateMachine(self)
    self.obj1142.isGraphObjectVisual = True

    if(hasattr(self.obj1142, '_setHierarchicalLink')):
      self.obj1142._setHierarchicalLink(False)

    # name
    self.obj1142.name.setValue('statemachine1')

    # classtype
    self.obj1142.classtype.setValue('StateMachine')

    # cardinality
    self.obj1142.cardinality.setValue('1')

    self.obj1142.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(660.0,25.0,self.obj1142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1142)
    self.globalAndLocalPostcondition(self.obj1142, rootNode)
    self.obj1142.postAction( rootNode.CREATE )

    self.obj1143=OUT2(self)
    self.obj1143.isGraphObjectVisual = True

    if(hasattr(self.obj1143, '_setHierarchicalLink')):
      self.obj1143._setHierarchicalLink(False)

    # classtype
    self.obj1143.classtype.setValue('OUT2')

    # cardinality
    self.obj1143.cardinality.setValue('1')

    # name
    self.obj1143.name.setValue('out2_1')

    self.obj1143.graphClass_= graph_OUT2
    if self.genGraphics:
       new_obj = graph_OUT2(160.0,121.0,self.obj1143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1143)
    self.globalAndLocalPostcondition(self.obj1143, rootNode)
    self.obj1143.postAction( rootNode.CREATE )

    self.obj1144=Name(self)
    self.obj1144.isGraphObjectVisual = True

    if(hasattr(self.obj1144, '_setHierarchicalLink')):
      self.obj1144._setHierarchicalLink(False)

    # classtype
    self.obj1144.classtype.setValue('Name')

    # cardinality
    self.obj1144.cardinality.setValue('1')

    # name
    self.obj1144.name.setValue('name1')

    self.obj1144.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(600.0,380.0,self.obj1144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1144)
    self.globalAndLocalPostcondition(self.obj1144, rootNode)
    self.obj1144.postAction( rootNode.CREATE )

    self.obj1145=Inst(self)
    self.obj1145.isGraphObjectVisual = True

    if(hasattr(self.obj1145, '_setHierarchicalLink')):
      self.obj1145._setHierarchicalLink(False)

    # classtype
    self.obj1145.classtype.setValue('Inst')

    # cardinality
    self.obj1145.cardinality.setValue('1')

    # name
    self.obj1145.name.setValue('inst1')

    self.obj1145.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(200.0,380.0,self.obj1145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1145)
    self.globalAndLocalPostcondition(self.obj1145, rootNode)
    self.obj1145.postAction( rootNode.CREATE )

    self.obj1146=Attribute(self)
    self.obj1146.isGraphObjectVisual = True

    if(hasattr(self.obj1146, '_setHierarchicalLink')):
      self.obj1146._setHierarchicalLink(False)

    # Type
    self.obj1146.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1146.Type.config = 0

    # name
    self.obj1146.name.setValue('name')

    self.obj1146.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(420.0,127.0,self.obj1146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1146)
    self.globalAndLocalPostcondition(self.obj1146, rootNode)
    self.obj1146.postAction( rootNode.CREATE )

    self.obj1147=Attribute(self)
    self.obj1147.isGraphObjectVisual = True

    if(hasattr(self.obj1147, '_setHierarchicalLink')):
      self.obj1147._setHierarchicalLink(False)

    # Type
    self.obj1147.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1147.Type.config = 0

    # name
    self.obj1147.name.setValue('literal')

    self.obj1147.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,372.0,self.obj1147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1147)
    self.globalAndLocalPostcondition(self.obj1147, rootNode)
    self.obj1147.postAction( rootNode.CREATE )

    self.obj1148=Attribute(self)
    self.obj1148.isGraphObjectVisual = True

    if(hasattr(self.obj1148, '_setHierarchicalLink')):
      self.obj1148._setHierarchicalLink(False)

    # Type
    self.obj1148.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1148.Type.config = 0

    # name
    self.obj1148.name.setValue('name')

    self.obj1148.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(240.0,280.0,self.obj1148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1148)
    self.globalAndLocalPostcondition(self.obj1148, rootNode)
    self.obj1148.postAction( rootNode.CREATE )

    self.obj1149=Attribute(self)
    self.obj1149.isGraphObjectVisual = True

    if(hasattr(self.obj1149, '_setHierarchicalLink')):
      self.obj1149._setHierarchicalLink(False)

    # Type
    self.obj1149.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1149.Type.config = 0

    # name
    self.obj1149.name.setValue('pivot')

    self.obj1149.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,500.0,self.obj1149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1149)
    self.globalAndLocalPostcondition(self.obj1149, rootNode)
    self.obj1149.postAction( rootNode.CREATE )

    self.obj1150=Equation(self)
    self.obj1150.isGraphObjectVisual = True

    if(hasattr(self.obj1150, '_setHierarchicalLink')):
      self.obj1150._setHierarchicalLink(False)

    # name
    self.obj1150.name.setValue('eq2')

    self.obj1150.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,300.0,self.obj1150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1150)
    self.globalAndLocalPostcondition(self.obj1150, rootNode)
    self.obj1150.postAction( rootNode.CREATE )

    self.obj1151=Equation(self)
    self.obj1151.isGraphObjectVisual = True

    if(hasattr(self.obj1151, '_setHierarchicalLink')):
      self.obj1151._setHierarchicalLink(False)

    # name
    self.obj1151.name.setValue('eq1')

    self.obj1151.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(540.0,280.0,self.obj1151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1151)
    self.globalAndLocalPostcondition(self.obj1151, rootNode)
    self.obj1151.postAction( rootNode.CREATE )

    self.obj1152=Equation(self)
    self.obj1152.isGraphObjectVisual = True

    if(hasattr(self.obj1152, '_setHierarchicalLink')):
      self.obj1152._setHierarchicalLink(False)

    # name
    self.obj1152.name.setValue('eq3')

    self.obj1152.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,520.0,self.obj1152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1152)
    self.globalAndLocalPostcondition(self.obj1152, rootNode)
    self.obj1152.postAction( rootNode.CREATE )

    self.obj1153=Concat(self)
    self.obj1153.isGraphObjectVisual = True

    if(hasattr(self.obj1153, '_setHierarchicalLink')):
      self.obj1153._setHierarchicalLink(False)

    # Type
    self.obj1153.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1153.Type.config = 0

    # name
    self.obj1153.name.setValue('concat1')

    self.obj1153.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(520.0,200.0,self.obj1153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1153)
    self.globalAndLocalPostcondition(self.obj1153, rootNode)
    self.obj1153.postAction( rootNode.CREATE )

    self.obj1154=Constant(self)
    self.obj1154.isGraphObjectVisual = True

    if(hasattr(self.obj1154, '_setHierarchicalLink')):
      self.obj1154._setHierarchicalLink(False)

    # Type
    self.obj1154.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1154.Type.config = 0

    # name
    self.obj1154.name.setValue('sh')

    self.obj1154.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(860.0,440.0,self.obj1154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1154)
    self.globalAndLocalPostcondition(self.obj1154, rootNode)
    self.obj1154.postAction( rootNode.CREATE )

    self.obj1155=Constant(self)
    self.obj1155.isGraphObjectVisual = True

    if(hasattr(self.obj1155, '_setHierarchicalLink')):
      self.obj1155._setHierarchicalLink(False)

    # Type
    self.obj1155.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1155.Type.config = 0

    # name
    self.obj1155.name.setValue('B')

    self.obj1155.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(363.0,200.0,self.obj1155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1155)
    self.globalAndLocalPostcondition(self.obj1155, rootNode)
    self.obj1155.postAction( rootNode.CREATE )

    self.obj1156=Constant(self)
    self.obj1156.isGraphObjectVisual = True

    if(hasattr(self.obj1156, '_setHierarchicalLink')):
      self.obj1156._setHierarchicalLink(False)

    # Type
    self.obj1156.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1156.Type.config = 0

    # name
    self.obj1156.name.setValue('instfortrans')

    self.obj1156.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(400.0,480.0,self.obj1156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1156)
    self.globalAndLocalPostcondition(self.obj1156, rootNode)
    self.obj1156.postAction( rootNode.CREATE )

    self.obj1157=paired_with(self)
    self.obj1157.isGraphObjectVisual = True

    if(hasattr(self.obj1157, '_setHierarchicalLink')):
      self.obj1157._setHierarchicalLink(False)

    self.obj1157.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj1157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1157)
    self.globalAndLocalPostcondition(self.obj1157, rootNode)
    self.obj1157.postAction( rootNode.CREATE )

    self.obj1158=match_contains(self)
    self.obj1158.isGraphObjectVisual = True

    if(hasattr(self.obj1158, '_setHierarchicalLink')):
      self.obj1158._setHierarchicalLink(False)

    self.obj1158.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(238.0,60.0,self.obj1158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1158)
    self.globalAndLocalPostcondition(self.obj1158, rootNode)
    self.obj1158.postAction( rootNode.CREATE )

    self.obj1159=match_contains(self)
    self.obj1159.isGraphObjectVisual = True

    if(hasattr(self.obj1159, '_setHierarchicalLink')):
      self.obj1159._setHierarchicalLink(False)

    self.obj1159.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,117.0,self.obj1159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1159)
    self.globalAndLocalPostcondition(self.obj1159, rootNode)
    self.obj1159.postAction( rootNode.CREATE )

    self.obj1160=match_contains(self)
    self.obj1160.isGraphObjectVisual = True

    if(hasattr(self.obj1160, '_setHierarchicalLink')):
      self.obj1160._setHierarchicalLink(False)

    self.obj1160.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(465.0,50.5,self.obj1160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1160)
    self.globalAndLocalPostcondition(self.obj1160, rootNode)
    self.obj1160.postAction( rootNode.CREATE )

    self.obj1161=match_contains(self)
    self.obj1161.isGraphObjectVisual = True

    if(hasattr(self.obj1161, '_setHierarchicalLink')):
      self.obj1161._setHierarchicalLink(False)

    self.obj1161.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,107.0,self.obj1161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1161)
    self.globalAndLocalPostcondition(self.obj1161, rootNode)
    self.obj1161.postAction( rootNode.CREATE )

    self.obj1162=apply_contains(self)
    self.obj1162.isGraphObjectVisual = True

    if(hasattr(self.obj1162, '_setHierarchicalLink')):
      self.obj1162._setHierarchicalLink(False)

    self.obj1162.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(149.5,358.0,self.obj1162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1162)
    self.globalAndLocalPostcondition(self.obj1162, rootNode)
    self.obj1162.postAction( rootNode.CREATE )

    self.obj1163=apply_contains(self)
    self.obj1163.isGraphObjectVisual = True

    if(hasattr(self.obj1163, '_setHierarchicalLink')):
      self.obj1163._setHierarchicalLink(False)

    self.obj1163.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(179.5,347.0,self.obj1163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1163)
    self.globalAndLocalPostcondition(self.obj1163, rootNode)
    self.obj1163.postAction( rootNode.CREATE )

    self.obj1164=directLink_T(self)
    self.obj1164.isGraphObjectVisual = True

    if(hasattr(self.obj1164, '_setHierarchicalLink')):
      self.obj1164._setHierarchicalLink(False)

    # associationType
    self.obj1164.associationType.setValue('channelNames')

    self.obj1164.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(517.0,430.0,self.obj1164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1164)
    self.globalAndLocalPostcondition(self.obj1164, rootNode)
    self.obj1164.postAction( rootNode.CREATE )

    self.obj1165=directLink_S(self)
    self.obj1165.isGraphObjectVisual = True

    if(hasattr(self.obj1165, '_setHierarchicalLink')):
      self.obj1165._setHierarchicalLink(False)

    # associationType
    self.obj1165.associationType.setValue('type')

    self.obj1165.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(330.0,133.0,self.obj1165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1165)
    self.globalAndLocalPostcondition(self.obj1165, rootNode)
    self.obj1165.postAction( rootNode.CREATE )

    self.obj1166=directLink_S(self)
    self.obj1166.isGraphObjectVisual = True

    if(hasattr(self.obj1166, '_setHierarchicalLink')):
      self.obj1166._setHierarchicalLink(False)

    # associationType
    self.obj1166.associationType.setValue('owningStateMachine')

    self.obj1166.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(577.242375062,73.1510372393,self.obj1166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1166)
    self.globalAndLocalPostcondition(self.obj1166, rootNode)
    self.obj1166.postAction( rootNode.CREATE )

    self.obj1167=directLink_S(self)
    self.obj1167.isGraphObjectVisual = True

    if(hasattr(self.obj1167, '_setHierarchicalLink')):
      self.obj1167._setHierarchicalLink(False)

    # associationType
    self.obj1167.associationType.setValue('exitPoints')

    self.obj1167.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(859.0,103.5,self.obj1167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1167)
    self.globalAndLocalPostcondition(self.obj1167, rootNode)
    self.obj1167.postAction( rootNode.CREATE )

    self.obj1168=directLink_S(self)
    self.obj1168.isGraphObjectVisual = True

    if(hasattr(self.obj1168, '_setHierarchicalLink')):
      self.obj1168._setHierarchicalLink(False)

    # associationType
    self.obj1168.associationType.setValue('dest')

    self.obj1168.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(621.242375062,102.151037239,self.obj1168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1168)
    self.globalAndLocalPostcondition(self.obj1168, rootNode)
    self.obj1168.postAction( rootNode.CREATE )

    self.obj1169=hasAttribute_S(self)
    self.obj1169.isGraphObjectVisual = True

    if(hasattr(self.obj1169, '_setHierarchicalLink')):
      self.obj1169._setHierarchicalLink(False)

    self.obj1169.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(692.0,158.5,self.obj1169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1169)
    self.globalAndLocalPostcondition(self.obj1169, rootNode)
    self.obj1169.postAction( rootNode.CREATE )

    self.obj1170=hasAttribute_T(self)
    self.obj1170.isGraphObjectVisual = True

    if(hasattr(self.obj1170, '_setHierarchicalLink')):
      self.obj1170._setHierarchicalLink(False)

    self.obj1170.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(843.0,418.5,self.obj1170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1170)
    self.globalAndLocalPostcondition(self.obj1170, rootNode)
    self.obj1170.postAction( rootNode.CREATE )

    self.obj1171=hasAttribute_T(self)
    self.obj1171.isGraphObjectVisual = True

    if(hasattr(self.obj1171, '_setHierarchicalLink')):
      self.obj1171._setHierarchicalLink(False)

    self.obj1171.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(363.0,392.5,self.obj1171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1171)
    self.globalAndLocalPostcondition(self.obj1171, rootNode)
    self.obj1171.postAction( rootNode.CREATE )

    self.obj1172=hasAttribute_T(self)
    self.obj1172.isGraphObjectVisual = True

    if(hasattr(self.obj1172, '_setHierarchicalLink')):
      self.obj1172._setHierarchicalLink(False)

    self.obj1172.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(303.0,482.5,self.obj1172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1172)
    self.globalAndLocalPostcondition(self.obj1172, rootNode)
    self.obj1172.postAction( rootNode.CREATE )

    self.obj1173=leftExpr(self)
    self.obj1173.isGraphObjectVisual = True

    if(hasattr(self.obj1173, '_setHierarchicalLink')):
      self.obj1173._setHierarchicalLink(False)

    self.obj1173.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(936.0,372.5,self.obj1173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1173)
    self.globalAndLocalPostcondition(self.obj1173, rootNode)
    self.obj1173.postAction( rootNode.CREATE )

    self.obj1174=leftExpr(self)
    self.obj1174.isGraphObjectVisual = True

    if(hasattr(self.obj1174, '_setHierarchicalLink')):
      self.obj1174._setHierarchicalLink(False)

    self.obj1174.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(526.0,316.5,self.obj1174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1174)
    self.globalAndLocalPostcondition(self.obj1174, rootNode)
    self.obj1174.postAction( rootNode.CREATE )

    self.obj1175=leftExpr(self)
    self.obj1175.isGraphObjectVisual = True

    if(hasattr(self.obj1175, '_setHierarchicalLink')):
      self.obj1175._setHierarchicalLink(False)

    self.obj1175.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,549.5,self.obj1175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1175)
    self.globalAndLocalPostcondition(self.obj1175, rootNode)
    self.obj1175.postAction( rootNode.CREATE )

    self.obj1176=rightExpr(self)
    self.obj1176.isGraphObjectVisual = True

    if(hasattr(self.obj1176, '_setHierarchicalLink')):
      self.obj1176._setHierarchicalLink(False)

    self.obj1176.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(976.0,406.5,self.obj1176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1176)
    self.globalAndLocalPostcondition(self.obj1176, rootNode)
    self.obj1176.postAction( rootNode.CREATE )

    self.obj1177=rightExpr(self)
    self.obj1177.isGraphObjectVisual = True

    if(hasattr(self.obj1177, '_setHierarchicalLink')):
      self.obj1177._setHierarchicalLink(False)

    self.obj1177.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(666.0,276.5,self.obj1177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1177)
    self.globalAndLocalPostcondition(self.obj1177, rootNode)
    self.obj1177.postAction( rootNode.CREATE )

    self.obj1178=rightExpr(self)
    self.obj1178.isGraphObjectVisual = True

    if(hasattr(self.obj1178, '_setHierarchicalLink')):
      self.obj1178._setHierarchicalLink(False)

    self.obj1178.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(445.0,539.0,self.obj1178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1178)
    self.globalAndLocalPostcondition(self.obj1178, rootNode)
    self.obj1178.postAction( rootNode.CREATE )

    self.obj1179=hasArgs(self)
    self.obj1179.isGraphObjectVisual = True

    if(hasattr(self.obj1179, '_setHierarchicalLink')):
      self.obj1179._setHierarchicalLink(False)

    self.obj1179.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(584.0,234.0,self.obj1179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1179)
    self.globalAndLocalPostcondition(self.obj1179, rootNode)
    self.obj1179.postAction( rootNode.CREATE )

    self.obj1180=hasArgs(self)
    self.obj1180.isGraphObjectVisual = True

    if(hasattr(self.obj1180, '_setHierarchicalLink')):
      self.obj1180._setHierarchicalLink(False)

    self.obj1180.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(604.0,194.0,self.obj1180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1180)
    self.globalAndLocalPostcondition(self.obj1180, rootNode)
    self.obj1180.postAction( rootNode.CREATE )

    # Connections for obj1138 (graphObject_: Obj949) of type MatchModel
    self.drawConnections(
(self.obj1138,self.obj1157,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj1138,self.obj1158,[138.0, 51.0, 238.0, 60.0],"true", 2),
(self.obj1138,self.obj1159,[138.0, 51.0, 234.0, 117.0],"true", 2),
(self.obj1138,self.obj1160,[138.0, 51.0, 465.0, 50.5],"true", 2),
(self.obj1138,self.obj1161,[138.0, 51.0, 484.0, 107.0],"true", 2) )
    # Connections for obj1139 (graphObject_: Obj950) of type ApplyModel
    self.drawConnections(
(self.obj1139,self.obj1162,[143.0, 273.0, 149.5, 358.0],"true", 2),
(self.obj1139,self.obj1163,[143.0, 273.0, 179.5, 347.0],"true", 2) )
    # Connections for obj1140 (graphObject_: Obj951) named vertex1
    self.drawConnections(
(self.obj1140,self.obj1169,[830.0, 163.0, 692.0, 158.5],"true", 2) )
    # Connections for obj1141 (graphObject_: Obj952) named transition1
    self.drawConnections(
(self.obj1141,self.obj1165,[324.4847501237708, 71.30207447863364, 330.0, 133.0],"true", 2),
(self.obj1141,self.obj1166,[324.4847501237708, 71.30207447863364, 577.2423750618855, 73.15103723931682],"true", 2),
(self.obj1141,self.obj1168,[324.4847501237708, 71.30207447863364, 621.2423750618855, 102.15103723931682],"true", 2) )
    # Connections for obj1142 (graphObject_: Obj953) named statemachine1
    self.drawConnections(
(self.obj1142,self.obj1167,[830.0, 68.0, 859.0, 103.5],"true", 2) )
    # Connections for obj1143 (graphObject_: Obj954) named out2_1
    self.drawConnections(
 )
    # Connections for obj1144 (graphObject_: Obj955) named name1
    self.drawConnections(
(self.obj1144,self.obj1170,[772.0, 431.0, 843.0, 418.5],"true", 2) )
    # Connections for obj1145 (graphObject_: Obj956) named inst1
    self.drawConnections(
(self.obj1145,self.obj1164,[372.0, 431.0, 517.0, 430.0],"true", 2),
(self.obj1145,self.obj1171,[372.0, 431.0, 363.0, 392.5],"true", 2),
(self.obj1145,self.obj1172,[372.0, 431.0, 303.0, 482.5],"true", 2) )
    # Connections for obj1146 (graphObject_: Obj957) named name
    self.drawConnections(
 )
    # Connections for obj1147 (graphObject_: Obj958) named literal
    self.drawConnections(
 )
    # Connections for obj1148 (graphObject_: Obj959) named name
    self.drawConnections(
 )
    # Connections for obj1149 (graphObject_: Obj960) named pivot
    self.drawConnections(
 )
    # Connections for obj1150 (graphObject_: Obj961) named eq2
    self.drawConnections(
(self.obj1150,self.obj1173,[958.0, 339.0, 936.0, 372.5],"true", 2),
(self.obj1150,self.obj1176,[958.0, 339.0, 976.0, 406.5],"true", 2) )
    # Connections for obj1151 (graphObject_: Obj962) named eq1
    self.drawConnections(
(self.obj1151,self.obj1174,[678.0, 319.0, 526.0, 316.5],"true", 2),
(self.obj1151,self.obj1177,[678.0, 319.0, 666.0, 276.5],"true", 2) )
    # Connections for obj1152 (graphObject_: Obj963) named eq3
    self.drawConnections(
(self.obj1152,self.obj1175,[378.0, 559.0, 316.0, 549.5],"true", 2),
(self.obj1152,self.obj1178,[378.0, 559.0, 445.0, 539.0],"true", 2) )
    # Connections for obj1153 (graphObject_: Obj964) named concat1
    self.drawConnections(
(self.obj1153,self.obj1179,[654.0, 234.0, 584.0, 234.0],"true", 2),
(self.obj1153,self.obj1180,[654.0, 234.0, 604.0, 194.0],"true", 2) )
    # Connections for obj1154 (graphObject_: Obj965) named sh
    self.drawConnections(
 )
    # Connections for obj1155 (graphObject_: Obj966) named B
    self.drawConnections(
 )
    # Connections for obj1156 (graphObject_: Obj967) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1157 (graphObject_: Obj968) of type paired_with
    self.drawConnections(
(self.obj1157,self.obj1139,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj1158 (graphObject_: Obj969) of type match_contains
    self.drawConnections(
(self.obj1158,self.obj1141,[234.0, 67.0, 324.4847501237708, 71.30207447863364],"true", 2) )
    # Connections for obj1159 (graphObject_: Obj970) of type match_contains
    self.drawConnections(
(self.obj1159,self.obj1143,[234.0, 117.0, 330.0, 164.0],"true", 2) )
    # Connections for obj1160 (graphObject_: Obj971) of type match_contains
    self.drawConnections(
(self.obj1160,self.obj1142,[465.0, 50.5, 830.0, 68.0],"true", 2) )
    # Connections for obj1161 (graphObject_: Obj972) of type match_contains
    self.drawConnections(
(self.obj1161,self.obj1140,[484.0, 107.0, 830.0, 163.0],"true", 2) )
    # Connections for obj1162 (graphObject_: Obj973) of type apply_contains
    self.drawConnections(
(self.obj1162,self.obj1145,[149.5, 358.0, 372.0, 431.0],"true", 2) )
    # Connections for obj1163 (graphObject_: Obj974) of type apply_contains
    self.drawConnections(
(self.obj1163,self.obj1144,[179.5, 347.0, 772.0, 431.0],"true", 2) )
    # Connections for obj1164 (graphObject_: Obj975) of type directLink_T
    self.drawConnections(
(self.obj1164,self.obj1144,[517.0, 430.0, 772.0, 431.0],"true", 2) )
    # Connections for obj1165 (graphObject_: Obj976) of type directLink_S
    self.drawConnections(
(self.obj1165,self.obj1143,[330.0, 133.0, 330.0, 164.0],"true", 2) )
    # Connections for obj1166 (graphObject_: Obj977) of type directLink_S
    self.drawConnections(
(self.obj1166,self.obj1142,[577.2423750618855, 73.15103723931682, 830.0, 68.0],"true", 2) )
    # Connections for obj1167 (graphObject_: Obj978) of type directLink_S
    self.drawConnections(
(self.obj1167,self.obj1140,[859.0, 103.5, 830.0, 163.0],"true", 2) )
    # Connections for obj1168 (graphObject_: Obj979) of type directLink_S
    self.drawConnections(
(self.obj1168,self.obj1140,[621.2423750618855, 102.15103723931682, 830.0, 163.0],"true", 2) )
    # Connections for obj1169 (graphObject_: Obj980) of type hasAttribute_S
    self.drawConnections(
(self.obj1169,self.obj1146,[692.0, 158.5, 554.0, 161.0],"true", 2) )
    # Connections for obj1170 (graphObject_: Obj981) of type hasAttribute_T
    self.drawConnections(
(self.obj1170,self.obj1147,[843.0, 418.5, 914.0, 406.0],"true", 2) )
    # Connections for obj1171 (graphObject_: Obj982) of type hasAttribute_T
    self.drawConnections(
(self.obj1171,self.obj1148,[363.0, 392.5, 374.0, 314.0],"true", 2) )
    # Connections for obj1172 (graphObject_: Obj983) of type hasAttribute_T
    self.drawConnections(
(self.obj1172,self.obj1149,[303.0, 482.5, 194.0, 534.0],"true", 2) )
    # Connections for obj1173 (graphObject_: Obj984) of type leftExpr
    self.drawConnections(
(self.obj1173,self.obj1147,[936.0, 372.5, 914.0, 406.0],"true", 2) )
    # Connections for obj1174 (graphObject_: Obj985) of type leftExpr
    self.drawConnections(
(self.obj1174,self.obj1148,[526.0, 316.5, 374.0, 314.0],"true", 2) )
    # Connections for obj1175 (graphObject_: Obj986) of type leftExpr
    self.drawConnections(
(self.obj1175,self.obj1149,[316.0, 549.5, 194.0, 534.0],"true", 2) )
    # Connections for obj1176 (graphObject_: Obj987) of type rightExpr
    self.drawConnections(
(self.obj1176,self.obj1154,[976.0, 406.5, 994.0, 474.0],"true", 2) )
    # Connections for obj1177 (graphObject_: Obj988) of type rightExpr
    self.drawConnections(
(self.obj1177,self.obj1153,[666.0, 276.5, 654.0, 234.0],"true", 2) )
    # Connections for obj1178 (graphObject_: Obj989) of type rightExpr
    self.drawConnections(
(self.obj1178,self.obj1156,[445.0, 539.0, 534.0, 514.0],"true", 2) )
    # Connections for obj1179 (graphObject_: Obj990) of type hasArgs
    self.drawConnections(
(self.obj1179,self.obj1155,[584.0, 234.0, 497.0, 234.0],"true", 2) )
    # Connections for obj1180 (graphObject_: Obj991) of type hasArgs
    self.drawConnections(
(self.obj1180,self.obj1146,[604.0, 194.0, 554.0, 161.0],"true", 2) )

newfunction = Transition2QInstOUT_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
