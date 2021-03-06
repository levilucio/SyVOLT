"""
__Transition2QInstOUT_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 15:12:22 2015
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


    self.obj1052=MatchModel(self)
    self.obj1052.isGraphObjectVisual = True

    if(hasattr(self.obj1052, '_setHierarchicalLink')):
      self.obj1052._setHierarchicalLink(False)

    self.obj1052.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1052)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1052.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1052)
    self.globalAndLocalPostcondition(self.obj1052, rootNode)
    self.obj1052.postAction( rootNode.CREATE )

    self.obj1053=ApplyModel(self)
    self.obj1053.isGraphObjectVisual = True

    if(hasattr(self.obj1053, '_setHierarchicalLink')):
      self.obj1053._setHierarchicalLink(False)

    self.obj1053.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,240.0,self.obj1053)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1053.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1053)
    self.globalAndLocalPostcondition(self.obj1053, rootNode)
    self.obj1053.postAction( rootNode.CREATE )

    self.obj1054=Vertex(self)
    self.obj1054.isGraphObjectVisual = True

    if(hasattr(self.obj1054, '_setHierarchicalLink')):
      self.obj1054._setHierarchicalLink(False)

    # name
    self.obj1054.name.setValue('vertex1')

    # classtype
    self.obj1054.classtype.setValue('Vertex')

    # cardinality
    self.obj1054.cardinality.setValue('1')

    self.obj1054.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,120.0,self.obj1054)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1054.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1054)
    self.globalAndLocalPostcondition(self.obj1054, rootNode)
    self.obj1054.postAction( rootNode.CREATE )

    self.obj1055=Transition(self)
    self.obj1055.isGraphObjectVisual = True

    if(hasattr(self.obj1055, '_setHierarchicalLink')):
      self.obj1055._setHierarchicalLink(False)

    # name
    self.obj1055.name.setValue('transition1')

    # classtype
    self.obj1055.classtype.setValue('Transition')

    # cardinality
    self.obj1055.cardinality.setValue('+')

    self.obj1055.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(160.0,34.0,self.obj1055)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.9699999999999989, 0.8599999999999994]
    else: new_obj = None
    self.obj1055.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1055)
    self.globalAndLocalPostcondition(self.obj1055, rootNode)
    self.obj1055.postAction( rootNode.CREATE )

    self.obj1056=StateMachine(self)
    self.obj1056.isGraphObjectVisual = True

    if(hasattr(self.obj1056, '_setHierarchicalLink')):
      self.obj1056._setHierarchicalLink(False)

    # name
    self.obj1056.name.setValue('statemachine1')

    # classtype
    self.obj1056.classtype.setValue('StateMachine')

    # cardinality
    self.obj1056.cardinality.setValue('1')

    self.obj1056.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(660.0,25.0,self.obj1056)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1056.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1056)
    self.globalAndLocalPostcondition(self.obj1056, rootNode)
    self.obj1056.postAction( rootNode.CREATE )

    self.obj1057=OUT2(self)
    self.obj1057.isGraphObjectVisual = True

    if(hasattr(self.obj1057, '_setHierarchicalLink')):
      self.obj1057._setHierarchicalLink(False)

    # classtype
    self.obj1057.classtype.setValue('OUT2')

    # cardinality
    self.obj1057.cardinality.setValue('1')

    # name
    self.obj1057.name.setValue('out2_1')

    self.obj1057.graphClass_= graph_OUT2
    if self.genGraphics:
       new_obj = graph_OUT2(160.0,121.0,self.obj1057)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1057.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1057)
    self.globalAndLocalPostcondition(self.obj1057, rootNode)
    self.obj1057.postAction( rootNode.CREATE )

    self.obj1058=Name(self)
    self.obj1058.isGraphObjectVisual = True

    if(hasattr(self.obj1058, '_setHierarchicalLink')):
      self.obj1058._setHierarchicalLink(False)

    # classtype
    self.obj1058.classtype.setValue('Name')

    # cardinality
    self.obj1058.cardinality.setValue('1')

    # name
    self.obj1058.name.setValue('name1')

    self.obj1058.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(600.0,380.0,self.obj1058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1058)
    self.globalAndLocalPostcondition(self.obj1058, rootNode)
    self.obj1058.postAction( rootNode.CREATE )

    self.obj1059=Inst(self)
    self.obj1059.isGraphObjectVisual = True

    if(hasattr(self.obj1059, '_setHierarchicalLink')):
      self.obj1059._setHierarchicalLink(False)

    # classtype
    self.obj1059.classtype.setValue('Inst')

    # cardinality
    self.obj1059.cardinality.setValue('1')

    # name
    self.obj1059.name.setValue('inst1')

    self.obj1059.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(200.0,380.0,self.obj1059)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1059.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1059)
    self.globalAndLocalPostcondition(self.obj1059, rootNode)
    self.obj1059.postAction( rootNode.CREATE )

    self.obj1060=Attribute(self)
    self.obj1060.isGraphObjectVisual = True

    if(hasattr(self.obj1060, '_setHierarchicalLink')):
      self.obj1060._setHierarchicalLink(False)

    # Type
    self.obj1060.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1060.Type.config = 0

    # name
    self.obj1060.name.setValue('name')

    self.obj1060.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(420.0,127.0,self.obj1060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1060)
    self.globalAndLocalPostcondition(self.obj1060, rootNode)
    self.obj1060.postAction( rootNode.CREATE )

    self.obj1061=Attribute(self)
    self.obj1061.isGraphObjectVisual = True

    if(hasattr(self.obj1061, '_setHierarchicalLink')):
      self.obj1061._setHierarchicalLink(False)

    # Type
    self.obj1061.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1061.Type.config = 0

    # name
    self.obj1061.name.setValue('literal')

    self.obj1061.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,372.0,self.obj1061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1061)
    self.globalAndLocalPostcondition(self.obj1061, rootNode)
    self.obj1061.postAction( rootNode.CREATE )

    self.obj1062=Attribute(self)
    self.obj1062.isGraphObjectVisual = True

    if(hasattr(self.obj1062, '_setHierarchicalLink')):
      self.obj1062._setHierarchicalLink(False)

    # Type
    self.obj1062.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1062.Type.config = 0

    # name
    self.obj1062.name.setValue('name')

    self.obj1062.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(240.0,280.0,self.obj1062)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1062.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1062)
    self.globalAndLocalPostcondition(self.obj1062, rootNode)
    self.obj1062.postAction( rootNode.CREATE )

    self.obj1063=Attribute(self)
    self.obj1063.isGraphObjectVisual = True

    if(hasattr(self.obj1063, '_setHierarchicalLink')):
      self.obj1063._setHierarchicalLink(False)

    # Type
    self.obj1063.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1063.Type.config = 0

    # name
    self.obj1063.name.setValue('pivot')

    self.obj1063.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,500.0,self.obj1063)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1063.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1063)
    self.globalAndLocalPostcondition(self.obj1063, rootNode)
    self.obj1063.postAction( rootNode.CREATE )

    self.obj1064=Equation(self)
    self.obj1064.isGraphObjectVisual = True

    if(hasattr(self.obj1064, '_setHierarchicalLink')):
      self.obj1064._setHierarchicalLink(False)

    # name
    self.obj1064.name.setValue('eq2')

    self.obj1064.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,300.0,self.obj1064)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1064.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1064)
    self.globalAndLocalPostcondition(self.obj1064, rootNode)
    self.obj1064.postAction( rootNode.CREATE )

    self.obj1065=Equation(self)
    self.obj1065.isGraphObjectVisual = True

    if(hasattr(self.obj1065, '_setHierarchicalLink')):
      self.obj1065._setHierarchicalLink(False)

    # name
    self.obj1065.name.setValue('eq1')

    self.obj1065.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(540.0,280.0,self.obj1065)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1065.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1065)
    self.globalAndLocalPostcondition(self.obj1065, rootNode)
    self.obj1065.postAction( rootNode.CREATE )

    self.obj1066=Equation(self)
    self.obj1066.isGraphObjectVisual = True

    if(hasattr(self.obj1066, '_setHierarchicalLink')):
      self.obj1066._setHierarchicalLink(False)

    # name
    self.obj1066.name.setValue('eq3')

    self.obj1066.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,520.0,self.obj1066)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1066.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1066)
    self.globalAndLocalPostcondition(self.obj1066, rootNode)
    self.obj1066.postAction( rootNode.CREATE )

    self.obj1067=Concat(self)
    self.obj1067.isGraphObjectVisual = True

    if(hasattr(self.obj1067, '_setHierarchicalLink')):
      self.obj1067._setHierarchicalLink(False)

    # Type
    self.obj1067.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1067.Type.config = 0

    # name
    self.obj1067.name.setValue('concat1')

    self.obj1067.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(520.0,200.0,self.obj1067)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1067.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1067)
    self.globalAndLocalPostcondition(self.obj1067, rootNode)
    self.obj1067.postAction( rootNode.CREATE )

    self.obj1068=Constant(self)
    self.obj1068.isGraphObjectVisual = True

    if(hasattr(self.obj1068, '_setHierarchicalLink')):
      self.obj1068._setHierarchicalLink(False)

    # Type
    self.obj1068.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1068.Type.config = 0

    # name
    self.obj1068.name.setValue('sh')

    self.obj1068.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(860.0,440.0,self.obj1068)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1068.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1068)
    self.globalAndLocalPostcondition(self.obj1068, rootNode)
    self.obj1068.postAction( rootNode.CREATE )

    self.obj1069=Constant(self)
    self.obj1069.isGraphObjectVisual = True

    if(hasattr(self.obj1069, '_setHierarchicalLink')):
      self.obj1069._setHierarchicalLink(False)

    # Type
    self.obj1069.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1069.Type.config = 0

    # name
    self.obj1069.name.setValue('B')

    self.obj1069.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(363.0,200.0,self.obj1069)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1069.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1069)
    self.globalAndLocalPostcondition(self.obj1069, rootNode)
    self.obj1069.postAction( rootNode.CREATE )

    self.obj1070=Constant(self)
    self.obj1070.isGraphObjectVisual = True

    if(hasattr(self.obj1070, '_setHierarchicalLink')):
      self.obj1070._setHierarchicalLink(False)

    # Type
    self.obj1070.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1070.Type.config = 0

    # name
    self.obj1070.name.setValue('instfortrans')

    self.obj1070.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(400.0,480.0,self.obj1070)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1070.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1070)
    self.globalAndLocalPostcondition(self.obj1070, rootNode)
    self.obj1070.postAction( rootNode.CREATE )

    self.obj1071=paired_with(self)
    self.obj1071.isGraphObjectVisual = True

    if(hasattr(self.obj1071, '_setHierarchicalLink')):
      self.obj1071._setHierarchicalLink(False)

    self.obj1071.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj1071)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1071.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1071)
    self.globalAndLocalPostcondition(self.obj1071, rootNode)
    self.obj1071.postAction( rootNode.CREATE )

    self.obj1072=match_contains(self)
    self.obj1072.isGraphObjectVisual = True

    if(hasattr(self.obj1072, '_setHierarchicalLink')):
      self.obj1072._setHierarchicalLink(False)

    self.obj1072.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(238.0,60.0,self.obj1072)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1072.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1072)
    self.globalAndLocalPostcondition(self.obj1072, rootNode)
    self.obj1072.postAction( rootNode.CREATE )

    self.obj1073=match_contains(self)
    self.obj1073.isGraphObjectVisual = True

    if(hasattr(self.obj1073, '_setHierarchicalLink')):
      self.obj1073._setHierarchicalLink(False)

    self.obj1073.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,117.0,self.obj1073)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1073.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1073)
    self.globalAndLocalPostcondition(self.obj1073, rootNode)
    self.obj1073.postAction( rootNode.CREATE )

    self.obj1074=match_contains(self)
    self.obj1074.isGraphObjectVisual = True

    if(hasattr(self.obj1074, '_setHierarchicalLink')):
      self.obj1074._setHierarchicalLink(False)

    self.obj1074.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(465.0,50.5,self.obj1074)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1074.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1074)
    self.globalAndLocalPostcondition(self.obj1074, rootNode)
    self.obj1074.postAction( rootNode.CREATE )

    self.obj1075=match_contains(self)
    self.obj1075.isGraphObjectVisual = True

    if(hasattr(self.obj1075, '_setHierarchicalLink')):
      self.obj1075._setHierarchicalLink(False)

    self.obj1075.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,107.0,self.obj1075)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1075.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1075)
    self.globalAndLocalPostcondition(self.obj1075, rootNode)
    self.obj1075.postAction( rootNode.CREATE )

    self.obj1076=apply_contains(self)
    self.obj1076.isGraphObjectVisual = True

    if(hasattr(self.obj1076, '_setHierarchicalLink')):
      self.obj1076._setHierarchicalLink(False)

    self.obj1076.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(149.5,358.0,self.obj1076)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1076.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1076)
    self.globalAndLocalPostcondition(self.obj1076, rootNode)
    self.obj1076.postAction( rootNode.CREATE )

    self.obj1077=apply_contains(self)
    self.obj1077.isGraphObjectVisual = True

    if(hasattr(self.obj1077, '_setHierarchicalLink')):
      self.obj1077._setHierarchicalLink(False)

    self.obj1077.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(179.5,347.0,self.obj1077)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1077.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1077)
    self.globalAndLocalPostcondition(self.obj1077, rootNode)
    self.obj1077.postAction( rootNode.CREATE )

    self.obj1078=directLink_T(self)
    self.obj1078.isGraphObjectVisual = True

    if(hasattr(self.obj1078, '_setHierarchicalLink')):
      self.obj1078._setHierarchicalLink(False)

    # associationType
    self.obj1078.associationType.setValue('channelNames')

    self.obj1078.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(517.0,430.0,self.obj1078)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1078.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1078)
    self.globalAndLocalPostcondition(self.obj1078, rootNode)
    self.obj1078.postAction( rootNode.CREATE )

    self.obj1079=directLink_S(self)
    self.obj1079.isGraphObjectVisual = True

    if(hasattr(self.obj1079, '_setHierarchicalLink')):
      self.obj1079._setHierarchicalLink(False)

    # associationType
    self.obj1079.associationType.setValue('type')

    self.obj1079.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(330.0,133.0,self.obj1079)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1079.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1079)
    self.globalAndLocalPostcondition(self.obj1079, rootNode)
    self.obj1079.postAction( rootNode.CREATE )

    self.obj1080=directLink_S(self)
    self.obj1080.isGraphObjectVisual = True

    if(hasattr(self.obj1080, '_setHierarchicalLink')):
      self.obj1080._setHierarchicalLink(False)

    # associationType
    self.obj1080.associationType.setValue('owningStateMachine')

    self.obj1080.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(577.242375062,73.1510372393,self.obj1080)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1080.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1080)
    self.globalAndLocalPostcondition(self.obj1080, rootNode)
    self.obj1080.postAction( rootNode.CREATE )

    self.obj1081=directLink_S(self)
    self.obj1081.isGraphObjectVisual = True

    if(hasattr(self.obj1081, '_setHierarchicalLink')):
      self.obj1081._setHierarchicalLink(False)

    # associationType
    self.obj1081.associationType.setValue('exitPoints')

    self.obj1081.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(859.0,103.5,self.obj1081)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1081.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1081)
    self.globalAndLocalPostcondition(self.obj1081, rootNode)
    self.obj1081.postAction( rootNode.CREATE )

    self.obj1082=directLink_S(self)
    self.obj1082.isGraphObjectVisual = True

    if(hasattr(self.obj1082, '_setHierarchicalLink')):
      self.obj1082._setHierarchicalLink(False)

    # associationType
    self.obj1082.associationType.setValue('dest')

    self.obj1082.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(621.242375062,102.151037239,self.obj1082)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1082.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1082)
    self.globalAndLocalPostcondition(self.obj1082, rootNode)
    self.obj1082.postAction( rootNode.CREATE )

    self.obj1083=hasAttribute_S(self)
    self.obj1083.isGraphObjectVisual = True

    if(hasattr(self.obj1083, '_setHierarchicalLink')):
      self.obj1083._setHierarchicalLink(False)

    self.obj1083.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(692.0,158.5,self.obj1083)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1083.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1083)
    self.globalAndLocalPostcondition(self.obj1083, rootNode)
    self.obj1083.postAction( rootNode.CREATE )

    self.obj1084=hasAttribute_T(self)
    self.obj1084.isGraphObjectVisual = True

    if(hasattr(self.obj1084, '_setHierarchicalLink')):
      self.obj1084._setHierarchicalLink(False)

    self.obj1084.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(843.0,418.5,self.obj1084)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1084.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1084)
    self.globalAndLocalPostcondition(self.obj1084, rootNode)
    self.obj1084.postAction( rootNode.CREATE )

    self.obj1085=hasAttribute_T(self)
    self.obj1085.isGraphObjectVisual = True

    if(hasattr(self.obj1085, '_setHierarchicalLink')):
      self.obj1085._setHierarchicalLink(False)

    self.obj1085.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(363.0,392.5,self.obj1085)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1085.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1085)
    self.globalAndLocalPostcondition(self.obj1085, rootNode)
    self.obj1085.postAction( rootNode.CREATE )

    self.obj1086=hasAttribute_T(self)
    self.obj1086.isGraphObjectVisual = True

    if(hasattr(self.obj1086, '_setHierarchicalLink')):
      self.obj1086._setHierarchicalLink(False)

    self.obj1086.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(303.0,482.5,self.obj1086)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1086.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1086)
    self.globalAndLocalPostcondition(self.obj1086, rootNode)
    self.obj1086.postAction( rootNode.CREATE )

    self.obj1087=leftExpr(self)
    self.obj1087.isGraphObjectVisual = True

    if(hasattr(self.obj1087, '_setHierarchicalLink')):
      self.obj1087._setHierarchicalLink(False)

    self.obj1087.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(936.0,372.5,self.obj1087)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1087.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1087)
    self.globalAndLocalPostcondition(self.obj1087, rootNode)
    self.obj1087.postAction( rootNode.CREATE )

    self.obj1088=leftExpr(self)
    self.obj1088.isGraphObjectVisual = True

    if(hasattr(self.obj1088, '_setHierarchicalLink')):
      self.obj1088._setHierarchicalLink(False)

    self.obj1088.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(526.0,316.5,self.obj1088)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1088.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1088)
    self.globalAndLocalPostcondition(self.obj1088, rootNode)
    self.obj1088.postAction( rootNode.CREATE )

    self.obj1089=leftExpr(self)
    self.obj1089.isGraphObjectVisual = True

    if(hasattr(self.obj1089, '_setHierarchicalLink')):
      self.obj1089._setHierarchicalLink(False)

    self.obj1089.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,549.5,self.obj1089)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1089.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1089)
    self.globalAndLocalPostcondition(self.obj1089, rootNode)
    self.obj1089.postAction( rootNode.CREATE )

    self.obj1090=rightExpr(self)
    self.obj1090.isGraphObjectVisual = True

    if(hasattr(self.obj1090, '_setHierarchicalLink')):
      self.obj1090._setHierarchicalLink(False)

    self.obj1090.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(976.0,406.5,self.obj1090)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1090.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1090)
    self.globalAndLocalPostcondition(self.obj1090, rootNode)
    self.obj1090.postAction( rootNode.CREATE )

    self.obj1091=rightExpr(self)
    self.obj1091.isGraphObjectVisual = True

    if(hasattr(self.obj1091, '_setHierarchicalLink')):
      self.obj1091._setHierarchicalLink(False)

    self.obj1091.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(666.0,276.5,self.obj1091)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1091.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1091)
    self.globalAndLocalPostcondition(self.obj1091, rootNode)
    self.obj1091.postAction( rootNode.CREATE )

    self.obj1092=rightExpr(self)
    self.obj1092.isGraphObjectVisual = True

    if(hasattr(self.obj1092, '_setHierarchicalLink')):
      self.obj1092._setHierarchicalLink(False)

    self.obj1092.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(445.0,539.0,self.obj1092)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1092.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1092)
    self.globalAndLocalPostcondition(self.obj1092, rootNode)
    self.obj1092.postAction( rootNode.CREATE )

    self.obj1093=hasArgs(self)
    self.obj1093.isGraphObjectVisual = True

    if(hasattr(self.obj1093, '_setHierarchicalLink')):
      self.obj1093._setHierarchicalLink(False)

    self.obj1093.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(584.0,234.0,self.obj1093)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1093.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1093)
    self.globalAndLocalPostcondition(self.obj1093, rootNode)
    self.obj1093.postAction( rootNode.CREATE )

    self.obj1094=hasArgs(self)
    self.obj1094.isGraphObjectVisual = True

    if(hasattr(self.obj1094, '_setHierarchicalLink')):
      self.obj1094._setHierarchicalLink(False)

    self.obj1094.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(604.0,194.0,self.obj1094)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1094.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1094)
    self.globalAndLocalPostcondition(self.obj1094, rootNode)
    self.obj1094.postAction( rootNode.CREATE )

    # Connections for obj1052 (graphObject_: Obj949) of type MatchModel
    self.drawConnections(
(self.obj1052,self.obj1071,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj1052,self.obj1072,[138.0, 51.0, 238.0, 60.0],"true", 2),
(self.obj1052,self.obj1073,[138.0, 51.0, 234.0, 117.0],"true", 2),
(self.obj1052,self.obj1074,[138.0, 51.0, 465.0, 50.5],"true", 2),
(self.obj1052,self.obj1075,[138.0, 51.0, 484.0, 107.0],"true", 2) )
    # Connections for obj1053 (graphObject_: Obj950) of type ApplyModel
    self.drawConnections(
(self.obj1053,self.obj1076,[143.0, 273.0, 149.5, 358.0],"true", 2),
(self.obj1053,self.obj1077,[143.0, 273.0, 179.5, 347.0],"true", 2) )
    # Connections for obj1054 (graphObject_: Obj951) named vertex1
    self.drawConnections(
(self.obj1054,self.obj1083,[830.0, 163.0, 692.0, 158.5],"true", 2) )
    # Connections for obj1055 (graphObject_: Obj952) named transition1
    self.drawConnections(
(self.obj1055,self.obj1079,[324.4847501237708, 71.30207447863364, 330.0, 133.0],"true", 2),
(self.obj1055,self.obj1080,[324.4847501237708, 71.30207447863364, 577.2423750618855, 73.15103723931682],"true", 2),
(self.obj1055,self.obj1082,[324.4847501237708, 71.30207447863364, 621.2423750618855, 102.15103723931682],"true", 2) )
    # Connections for obj1056 (graphObject_: Obj953) named statemachine1
    self.drawConnections(
(self.obj1056,self.obj1081,[830.0, 68.0, 859.0, 103.5],"true", 2) )
    # Connections for obj1057 (graphObject_: Obj954) named out2_1
    self.drawConnections(
 )
    # Connections for obj1058 (graphObject_: Obj955) named name1
    self.drawConnections(
(self.obj1058,self.obj1084,[772.0, 431.0, 843.0, 418.5],"true", 2) )
    # Connections for obj1059 (graphObject_: Obj956) named inst1
    self.drawConnections(
(self.obj1059,self.obj1078,[372.0, 431.0, 517.0, 430.0],"true", 2),
(self.obj1059,self.obj1085,[372.0, 431.0, 363.0, 392.5],"true", 2),
(self.obj1059,self.obj1086,[372.0, 431.0, 303.0, 482.5],"true", 2) )
    # Connections for obj1060 (graphObject_: Obj957) named name
    self.drawConnections(
 )
    # Connections for obj1061 (graphObject_: Obj958) named literal
    self.drawConnections(
 )
    # Connections for obj1062 (graphObject_: Obj959) named name
    self.drawConnections(
 )
    # Connections for obj1063 (graphObject_: Obj960) named pivot
    self.drawConnections(
 )
    # Connections for obj1064 (graphObject_: Obj961) named eq2
    self.drawConnections(
(self.obj1064,self.obj1087,[958.0, 339.0, 936.0, 372.5],"true", 2),
(self.obj1064,self.obj1090,[958.0, 339.0, 976.0, 406.5],"true", 2) )
    # Connections for obj1065 (graphObject_: Obj962) named eq1
    self.drawConnections(
(self.obj1065,self.obj1088,[678.0, 319.0, 526.0, 316.5],"true", 2),
(self.obj1065,self.obj1091,[678.0, 319.0, 666.0, 276.5],"true", 2) )
    # Connections for obj1066 (graphObject_: Obj963) named eq3
    self.drawConnections(
(self.obj1066,self.obj1089,[378.0, 559.0, 316.0, 549.5],"true", 2),
(self.obj1066,self.obj1092,[378.0, 559.0, 445.0, 539.0],"true", 2) )
    # Connections for obj1067 (graphObject_: Obj964) named concat1
    self.drawConnections(
(self.obj1067,self.obj1093,[654.0, 234.0, 584.0, 234.0],"true", 2),
(self.obj1067,self.obj1094,[654.0, 234.0, 604.0, 194.0],"true", 2) )
    # Connections for obj1068 (graphObject_: Obj965) named sh
    self.drawConnections(
 )
    # Connections for obj1069 (graphObject_: Obj966) named B
    self.drawConnections(
 )
    # Connections for obj1070 (graphObject_: Obj967) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1071 (graphObject_: Obj968) of type paired_with
    self.drawConnections(
(self.obj1071,self.obj1053,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj1072 (graphObject_: Obj969) of type match_contains
    self.drawConnections(
(self.obj1072,self.obj1055,[234.0, 67.0, 324.4847501237708, 71.30207447863364],"true", 2) )
    # Connections for obj1073 (graphObject_: Obj970) of type match_contains
    self.drawConnections(
(self.obj1073,self.obj1057,[234.0, 117.0, 330.0, 164.0],"true", 2) )
    # Connections for obj1074 (graphObject_: Obj971) of type match_contains
    self.drawConnections(
(self.obj1074,self.obj1056,[465.0, 50.5, 830.0, 68.0],"true", 2) )
    # Connections for obj1075 (graphObject_: Obj972) of type match_contains
    self.drawConnections(
(self.obj1075,self.obj1054,[484.0, 107.0, 830.0, 163.0],"true", 2) )
    # Connections for obj1076 (graphObject_: Obj973) of type apply_contains
    self.drawConnections(
(self.obj1076,self.obj1059,[149.5, 358.0, 372.0, 431.0],"true", 2) )
    # Connections for obj1077 (graphObject_: Obj974) of type apply_contains
    self.drawConnections(
(self.obj1077,self.obj1058,[179.5, 347.0, 772.0, 431.0],"true", 2) )
    # Connections for obj1078 (graphObject_: Obj975) of type directLink_T
    self.drawConnections(
(self.obj1078,self.obj1058,[517.0, 430.0, 772.0, 431.0],"true", 2) )
    # Connections for obj1079 (graphObject_: Obj976) of type directLink_S
    self.drawConnections(
(self.obj1079,self.obj1057,[330.0, 133.0, 330.0, 164.0],"true", 2) )
    # Connections for obj1080 (graphObject_: Obj977) of type directLink_S
    self.drawConnections(
(self.obj1080,self.obj1056,[577.2423750618855, 73.15103723931682, 830.0, 68.0],"true", 2) )
    # Connections for obj1081 (graphObject_: Obj978) of type directLink_S
    self.drawConnections(
(self.obj1081,self.obj1054,[859.0, 103.5, 830.0, 163.0],"true", 2) )
    # Connections for obj1082 (graphObject_: Obj979) of type directLink_S
    self.drawConnections(
(self.obj1082,self.obj1054,[621.2423750618855, 102.15103723931682, 830.0, 163.0],"true", 2) )
    # Connections for obj1083 (graphObject_: Obj980) of type hasAttribute_S
    self.drawConnections(
(self.obj1083,self.obj1060,[692.0, 158.5, 554.0, 161.0],"true", 2) )
    # Connections for obj1084 (graphObject_: Obj981) of type hasAttribute_T
    self.drawConnections(
(self.obj1084,self.obj1061,[843.0, 418.5, 914.0, 406.0],"true", 2) )
    # Connections for obj1085 (graphObject_: Obj982) of type hasAttribute_T
    self.drawConnections(
(self.obj1085,self.obj1062,[363.0, 392.5, 374.0, 314.0],"true", 2) )
    # Connections for obj1086 (graphObject_: Obj983) of type hasAttribute_T
    self.drawConnections(
(self.obj1086,self.obj1063,[303.0, 482.5, 194.0, 534.0],"true", 2) )
    # Connections for obj1087 (graphObject_: Obj984) of type leftExpr
    self.drawConnections(
(self.obj1087,self.obj1061,[936.0, 372.5, 914.0, 406.0],"true", 2) )
    # Connections for obj1088 (graphObject_: Obj985) of type leftExpr
    self.drawConnections(
(self.obj1088,self.obj1062,[526.0, 316.5, 374.0, 314.0],"true", 2) )
    # Connections for obj1089 (graphObject_: Obj986) of type leftExpr
    self.drawConnections(
(self.obj1089,self.obj1063,[316.0, 549.5, 194.0, 534.0],"true", 2) )
    # Connections for obj1090 (graphObject_: Obj987) of type rightExpr
    self.drawConnections(
(self.obj1090,self.obj1068,[976.0, 406.5, 994.0, 474.0],"true", 2) )
    # Connections for obj1091 (graphObject_: Obj988) of type rightExpr
    self.drawConnections(
(self.obj1091,self.obj1067,[666.0, 276.5, 654.0, 234.0],"true", 2) )
    # Connections for obj1092 (graphObject_: Obj989) of type rightExpr
    self.drawConnections(
(self.obj1092,self.obj1070,[445.0, 539.0, 534.0, 514.0],"true", 2) )
    # Connections for obj1093 (graphObject_: Obj990) of type hasArgs
    self.drawConnections(
(self.obj1093,self.obj1069,[584.0, 234.0, 497.0, 234.0],"true", 2) )
    # Connections for obj1094 (graphObject_: Obj991) of type hasArgs
    self.drawConnections(
(self.obj1094,self.obj1060,[604.0, 194.0, 554.0, 161.0],"true", 2) )

newfunction = Transition2QInstOUT_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
