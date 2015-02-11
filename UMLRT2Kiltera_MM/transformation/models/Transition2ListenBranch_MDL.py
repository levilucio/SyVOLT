"""
__Transition2ListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:27:04 2015
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from Trigger_S import *
from Signal import *
from Transition import *
from State import *
from Listen import *
from ListenBranch import *
from Inst import *
from Attribute import *
from Equation import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from directLink_S import *
from backward_link import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from graph_Attribute import *
from graph_Transition import *
from graph_Signal import *
from graph_paired_with import *
from graph_Listen import *
from graph_State import *
from graph_Equation import *
from graph_backward_link import *
from graph_rightExpr import *
from graph_Trigger_S import *
from graph_Inst import *
from graph_match_contains import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_ApplyModel import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_hasAttribute_S import *
from graph_hasAttribute_T import *
from graph_leftExpr import *
from graph_ListenBranch import *
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

def Transition2ListenBranch_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2ListenBranch')
    # --- ASG attributes over ---


    self.obj1073=MatchModel(self)
    self.obj1073.isGraphObjectVisual = True

    if(hasattr(self.obj1073, '_setHierarchicalLink')):
      self.obj1073._setHierarchicalLink(False)

    self.obj1073.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,21.0,self.obj1073)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1073.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1073)
    self.globalAndLocalPostcondition(self.obj1073, rootNode)
    self.obj1073.postAction( rootNode.CREATE )

    self.obj1074=ApplyModel(self)
    self.obj1074.isGraphObjectVisual = True

    if(hasattr(self.obj1074, '_setHierarchicalLink')):
      self.obj1074._setHierarchicalLink(False)

    self.obj1074.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(24.0,342.0,self.obj1074)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1074.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1074)
    self.globalAndLocalPostcondition(self.obj1074, rootNode)
    self.obj1074.postAction( rootNode.CREATE )

    self.obj1075=Trigger_S(self)
    self.obj1075.isGraphObjectVisual = True

    if(hasattr(self.obj1075, '_setHierarchicalLink')):
      self.obj1075._setHierarchicalLink(False)

    # classtype
    self.obj1075.classtype.setValue('Trigger_S')

    # cardinality
    self.obj1075.cardinality.setValue('1')

    # name
    self.obj1075.name.setValue('triggerS1')

    self.obj1075.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(860.0,180.0,self.obj1075)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1075.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1075)
    self.globalAndLocalPostcondition(self.obj1075, rootNode)
    self.obj1075.postAction( rootNode.CREATE )

    self.obj1076=Signal(self)
    self.obj1076.isGraphObjectVisual = True

    if(hasattr(self.obj1076, '_setHierarchicalLink')):
      self.obj1076._setHierarchicalLink(False)

    # name
    self.obj1076.name.setValue('signal1')

    # classtype
    self.obj1076.classtype.setValue('Signal')

    # cardinality
    self.obj1076.cardinality.setValue('1')

    self.obj1076.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(647.0,140.0,self.obj1076)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1076.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1076)
    self.globalAndLocalPostcondition(self.obj1076, rootNode)
    self.obj1076.postAction( rootNode.CREATE )

    self.obj1077=Transition(self)
    self.obj1077.isGraphObjectVisual = True

    if(hasattr(self.obj1077, '_setHierarchicalLink')):
      self.obj1077._setHierarchicalLink(False)

    # name
    self.obj1077.name.setValue('transition1')

    # classtype
    self.obj1077.classtype.setValue('Transition')

    # cardinality
    self.obj1077.cardinality.setValue('+')

    self.obj1077.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(834.0,80.0,self.obj1077)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1077.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1077)
    self.globalAndLocalPostcondition(self.obj1077, rootNode)
    self.obj1077.postAction( rootNode.CREATE )

    self.obj1078=State(self)
    self.obj1078.isGraphObjectVisual = True

    if(hasattr(self.obj1078, '_setHierarchicalLink')):
      self.obj1078._setHierarchicalLink(False)

    # name
    self.obj1078.name.setValue('state1')

    # classtype
    self.obj1078.classtype.setValue('State')

    # cardinality
    self.obj1078.cardinality.setValue('+')

    self.obj1078.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,80.0,self.obj1078)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1078.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1078)
    self.globalAndLocalPostcondition(self.obj1078, rootNode)
    self.obj1078.postAction( rootNode.CREATE )

    self.obj1079=Listen(self)
    self.obj1079.isGraphObjectVisual = True

    if(hasattr(self.obj1079, '_setHierarchicalLink')):
      self.obj1079._setHierarchicalLink(False)

    # classtype
    self.obj1079.classtype.setValue('Listen')

    # cardinality
    self.obj1079.cardinality.setValue('1')

    # name
    self.obj1079.name.setValue('listen1')

    self.obj1079.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,438.0,self.obj1079)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1079.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1079)
    self.globalAndLocalPostcondition(self.obj1079, rootNode)
    self.obj1079.postAction( rootNode.CREATE )

    self.obj1080=ListenBranch(self)
    self.obj1080.isGraphObjectVisual = True

    if(hasattr(self.obj1080, '_setHierarchicalLink')):
      self.obj1080._setHierarchicalLink(False)

    # classtype
    self.obj1080.classtype.setValue('ListenBranch')

    # cardinality
    self.obj1080.cardinality.setValue('1')

    # name
    self.obj1080.name.setValue('listenBranch1')

    self.obj1080.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(400.0,440.0,self.obj1080)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1080.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1080)
    self.globalAndLocalPostcondition(self.obj1080, rootNode)
    self.obj1080.postAction( rootNode.CREATE )

    self.obj1081=Inst(self)
    self.obj1081.isGraphObjectVisual = True

    if(hasattr(self.obj1081, '_setHierarchicalLink')):
      self.obj1081._setHierarchicalLink(False)

    # classtype
    self.obj1081.classtype.setValue('Inst')

    # cardinality
    self.obj1081.cardinality.setValue('1')

    # name
    self.obj1081.name.setValue('inst1')

    self.obj1081.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(760.0,437.0,self.obj1081)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1081.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1081)
    self.globalAndLocalPostcondition(self.obj1081, rootNode)
    self.obj1081.postAction( rootNode.CREATE )

    self.obj1082=Attribute(self)
    self.obj1082.isGraphObjectVisual = True

    if(hasattr(self.obj1082, '_setHierarchicalLink')):
      self.obj1082._setHierarchicalLink(False)

    # Type
    self.obj1082.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1082.Type.config = 0

    # name
    self.obj1082.name.setValue('isComposite')

    self.obj1082.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,175.0,self.obj1082)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1082.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1082)
    self.globalAndLocalPostcondition(self.obj1082, rootNode)
    self.obj1082.postAction( rootNode.CREATE )

    self.obj1083=Attribute(self)
    self.obj1083.isGraphObjectVisual = True

    if(hasattr(self.obj1083, '_setHierarchicalLink')):
      self.obj1083._setHierarchicalLink(False)

    # Type
    self.obj1083.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1083.Type.config = 0

    # name
    self.obj1083.name.setValue('hasOutgoingTransitions')

    self.obj1083.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(340.0,160.0,self.obj1083)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1083.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1083)
    self.globalAndLocalPostcondition(self.obj1083, rootNode)
    self.obj1083.postAction( rootNode.CREATE )

    self.obj1084=Attribute(self)
    self.obj1084.isGraphObjectVisual = True

    if(hasattr(self.obj1084, '_setHierarchicalLink')):
      self.obj1084._setHierarchicalLink(False)

    # Type
    self.obj1084.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1084.Type.config = 0

    # name
    self.obj1084.name.setValue('name')

    self.obj1084.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,240.0,self.obj1084)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1084.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1084)
    self.globalAndLocalPostcondition(self.obj1084, rootNode)
    self.obj1084.postAction( rootNode.CREATE )

    self.obj1085=Attribute(self)
    self.obj1085.isGraphObjectVisual = True

    if(hasattr(self.obj1085, '_setHierarchicalLink')):
      self.obj1085._setHierarchicalLink(False)

    # Type
    self.obj1085.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1085.Type.config = 0

    # name
    self.obj1085.name.setValue('channel')

    self.obj1085.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(405.0,361.0,self.obj1085)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1085.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1085)
    self.globalAndLocalPostcondition(self.obj1085, rootNode)
    self.obj1085.postAction( rootNode.CREATE )

    self.obj1086=Attribute(self)
    self.obj1086.isGraphObjectVisual = True

    if(hasattr(self.obj1086, '_setHierarchicalLink')):
      self.obj1086._setHierarchicalLink(False)

    # Type
    self.obj1086.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1086.Type.config = 0

    # name
    self.obj1086.name.setValue('pivot')

    self.obj1086.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(80.0,540.0,self.obj1086)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1086.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1086)
    self.globalAndLocalPostcondition(self.obj1086, rootNode)
    self.obj1086.postAction( rootNode.CREATE )

    self.obj1087=Attribute(self)
    self.obj1087.isGraphObjectVisual = True

    if(hasattr(self.obj1087, '_setHierarchicalLink')):
      self.obj1087._setHierarchicalLink(False)

    # Type
    self.obj1087.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1087.Type.config = 0

    # name
    self.obj1087.name.setValue('pivot')

    self.obj1087.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,540.0,self.obj1087)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1087.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1087)
    self.globalAndLocalPostcondition(self.obj1087, rootNode)
    self.obj1087.postAction( rootNode.CREATE )

    self.obj1088=Equation(self)
    self.obj1088.isGraphObjectVisual = True

    if(hasattr(self.obj1088, '_setHierarchicalLink')):
      self.obj1088._setHierarchicalLink(False)

    # name
    self.obj1088.name.setValue('eq1')

    self.obj1088.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(303.0,242.0,self.obj1088)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1088.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1088)
    self.globalAndLocalPostcondition(self.obj1088, rootNode)
    self.obj1088.postAction( rootNode.CREATE )

    self.obj1089=Equation(self)
    self.obj1089.isGraphObjectVisual = True

    if(hasattr(self.obj1089, '_setHierarchicalLink')):
      self.obj1089._setHierarchicalLink(False)

    # name
    self.obj1089.name.setValue('eq2')

    self.obj1089.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,240.0,self.obj1089)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1089.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1089)
    self.globalAndLocalPostcondition(self.obj1089, rootNode)
    self.obj1089.postAction( rootNode.CREATE )

    self.obj1090=Equation(self)
    self.obj1090.isGraphObjectVisual = True

    if(hasattr(self.obj1090, '_setHierarchicalLink')):
      self.obj1090._setHierarchicalLink(False)

    # name
    self.obj1090.name.setValue('eq3')

    self.obj1090.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(567.0,361.0,self.obj1090)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1090.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1090)
    self.globalAndLocalPostcondition(self.obj1090, rootNode)
    self.obj1090.postAction( rootNode.CREATE )

    self.obj1091=Equation(self)
    self.obj1091.isGraphObjectVisual = True

    if(hasattr(self.obj1091, '_setHierarchicalLink')):
      self.obj1091._setHierarchicalLink(False)

    # name
    self.obj1091.name.setValue('eq4')

    self.obj1091.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(200.0,620.0,self.obj1091)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1091.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1091)
    self.globalAndLocalPostcondition(self.obj1091, rootNode)
    self.obj1091.postAction( rootNode.CREATE )

    self.obj1092=Equation(self)
    self.obj1092.isGraphObjectVisual = True

    if(hasattr(self.obj1092, '_setHierarchicalLink')):
      self.obj1092._setHierarchicalLink(False)

    # name
    self.obj1092.name.setValue('eq5')

    self.obj1092.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,620.0,self.obj1092)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1092.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1092)
    self.globalAndLocalPostcondition(self.obj1092, rootNode)
    self.obj1092.postAction( rootNode.CREATE )

    self.obj1093=Constant(self)
    self.obj1093.isGraphObjectVisual = True

    if(hasattr(self.obj1093, '_setHierarchicalLink')):
      self.obj1093._setHierarchicalLink(False)

    # Type
    self.obj1093.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1093.Type.config = 0

    # name
    self.obj1093.name.setValue('false')

    self.obj1093.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,260.0,self.obj1093)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1093.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1093)
    self.globalAndLocalPostcondition(self.obj1093, rootNode)
    self.obj1093.postAction( rootNode.CREATE )

    self.obj1094=Constant(self)
    self.obj1094.isGraphObjectVisual = True

    if(hasattr(self.obj1094, '_setHierarchicalLink')):
      self.obj1094._setHierarchicalLink(False)

    # Type
    self.obj1094.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1094.Type.config = 0

    # name
    self.obj1094.name.setValue('true')

    self.obj1094.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(500.0,160.0,self.obj1094)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1094.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1094)
    self.globalAndLocalPostcondition(self.obj1094, rootNode)
    self.obj1094.postAction( rootNode.CREATE )

    self.obj1095=Constant(self)
    self.obj1095.isGraphObjectVisual = True

    if(hasattr(self.obj1095, '_setHierarchicalLink')):
      self.obj1095._setHierarchicalLink(False)

    # Type
    self.obj1095.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1095.Type.config = 0

    # name
    self.obj1095.name.setValue('listensimplestate')

    self.obj1095.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,540.0,self.obj1095)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1095.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1095)
    self.globalAndLocalPostcondition(self.obj1095, rootNode)
    self.obj1095.postAction( rootNode.CREATE )

    self.obj1096=Constant(self)
    self.obj1096.isGraphObjectVisual = True

    if(hasattr(self.obj1096, '_setHierarchicalLink')):
      self.obj1096._setHierarchicalLink(False)

    # Type
    self.obj1096.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1096.Type.config = 0

    # name
    self.obj1096.name.setValue('instfortrans')

    self.obj1096.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(920.0,540.0,self.obj1096)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1096.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1096)
    self.globalAndLocalPostcondition(self.obj1096, rootNode)
    self.obj1096.postAction( rootNode.CREATE )

    self.obj1097=paired_with(self)
    self.obj1097.isGraphObjectVisual = True

    if(hasattr(self.obj1097, '_setHierarchicalLink')):
      self.obj1097._setHierarchicalLink(False)

    self.obj1097.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(142.5,213.5,self.obj1097)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1097.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1097)
    self.globalAndLocalPostcondition(self.obj1097, rootNode)
    self.obj1097.postAction( rootNode.CREATE )

    self.obj1098=match_contains(self)
    self.obj1098.isGraphObjectVisual = True

    if(hasattr(self.obj1098, '_setHierarchicalLink')):
      self.obj1098._setHierarchicalLink(False)

    self.obj1098.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,87.5,self.obj1098)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1098.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1098)
    self.globalAndLocalPostcondition(self.obj1098, rootNode)
    self.obj1098.postAction( rootNode.CREATE )

    self.obj1099=match_contains(self)
    self.obj1099.isGraphObjectVisual = True

    if(hasattr(self.obj1099, '_setHierarchicalLink')):
      self.obj1099._setHierarchicalLink(False)

    self.obj1099.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(571.0,87.5,self.obj1099)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1099.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1099)
    self.globalAndLocalPostcondition(self.obj1099, rootNode)
    self.obj1099.postAction( rootNode.CREATE )

    self.obj1100=match_contains(self)
    self.obj1100.isGraphObjectVisual = True

    if(hasattr(self.obj1100, '_setHierarchicalLink')):
      self.obj1100._setHierarchicalLink(False)

    self.obj1100.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(477.5,117.5,self.obj1100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1100)
    self.globalAndLocalPostcondition(self.obj1100, rootNode)
    self.obj1100.postAction( rootNode.CREATE )

    self.obj1101=match_contains(self)
    self.obj1101.isGraphObjectVisual = True

    if(hasattr(self.obj1101, '_setHierarchicalLink')):
      self.obj1101._setHierarchicalLink(False)

    self.obj1101.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(582.0,107.5,self.obj1101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1101)
    self.globalAndLocalPostcondition(self.obj1101, rootNode)
    self.obj1101.postAction( rootNode.CREATE )

    self.obj1102=apply_contains(self)
    self.obj1102.isGraphObjectVisual = True

    if(hasattr(self.obj1102, '_setHierarchicalLink')):
      self.obj1102._setHierarchicalLink(False)

    self.obj1102.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,417.0,self.obj1102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1102)
    self.globalAndLocalPostcondition(self.obj1102, rootNode)
    self.obj1102.postAction( rootNode.CREATE )

    self.obj1103=apply_contains(self)
    self.obj1103.isGraphObjectVisual = True

    if(hasattr(self.obj1103, '_setHierarchicalLink')):
      self.obj1103._setHierarchicalLink(False)

    self.obj1103.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(359.5,432.0,self.obj1103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1103)
    self.globalAndLocalPostcondition(self.obj1103, rootNode)
    self.obj1103.postAction( rootNode.CREATE )

    self.obj1104=apply_contains(self)
    self.obj1104.isGraphObjectVisual = True

    if(hasattr(self.obj1104, '_setHierarchicalLink')):
      self.obj1104._setHierarchicalLink(False)

    self.obj1104.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(539.5,431.5,self.obj1104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1104)
    self.globalAndLocalPostcondition(self.obj1104, rootNode)
    self.obj1104.postAction( rootNode.CREATE )

    self.obj1105=directLink_T(self)
    self.obj1105.isGraphObjectVisual = True

    if(hasattr(self.obj1105, '_setHierarchicalLink')):
      self.obj1105._setHierarchicalLink(False)

    # associationType
    self.obj1105.associationType.setValue('branches')

    self.obj1105.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(399.0,484.0,self.obj1105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1105)
    self.globalAndLocalPostcondition(self.obj1105, rootNode)
    self.obj1105.postAction( rootNode.CREATE )

    self.obj1106=directLink_T(self)
    self.obj1106.isGraphObjectVisual = True

    if(hasattr(self.obj1106, '_setHierarchicalLink')):
      self.obj1106._setHierarchicalLink(False)

    # associationType
    self.obj1106.associationType.setValue('p')

    self.obj1106.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,490.0,self.obj1106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1106)
    self.globalAndLocalPostcondition(self.obj1106, rootNode)
    self.obj1106.postAction( rootNode.CREATE )

    self.obj1107=directLink_S(self)
    self.obj1107.isGraphObjectVisual = True

    if(hasattr(self.obj1107, '_setHierarchicalLink')):
      self.obj1107._setHierarchicalLink(False)

    # associationType
    self.obj1107.associationType.setValue('outgoingTransitions')

    self.obj1107.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,123.0,self.obj1107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1107)
    self.globalAndLocalPostcondition(self.obj1107, rootNode)
    self.obj1107.postAction( rootNode.CREATE )

    self.obj1108=directLink_S(self)
    self.obj1108.isGraphObjectVisual = True

    if(hasattr(self.obj1108, '_setHierarchicalLink')):
      self.obj1108._setHierarchicalLink(False)

    # associationType
    self.obj1108.associationType.setValue('triggers')

    self.obj1108.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(1024.5,181.0,self.obj1108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1108)
    self.globalAndLocalPostcondition(self.obj1108, rootNode)
    self.obj1108.postAction( rootNode.CREATE )

    self.obj1109=directLink_S(self)
    self.obj1109.isGraphObjectVisual = True

    if(hasattr(self.obj1109, '_setHierarchicalLink')):
      self.obj1109._setHierarchicalLink(False)

    # associationType
    self.obj1109.associationType.setValue('signal')

    self.obj1109.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(848.0,187.0,self.obj1109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1109)
    self.globalAndLocalPostcondition(self.obj1109, rootNode)
    self.obj1109.postAction( rootNode.CREATE )

    self.obj1110=backward_link(self)
    self.obj1110.isGraphObjectVisual = True

    if(hasattr(self.obj1110, '_setHierarchicalLink')):
      self.obj1110._setHierarchicalLink(False)

    # type
    self.obj1110.type.setValue('ruleDef')

    self.obj1110.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,287.0,self.obj1110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1110)
    self.globalAndLocalPostcondition(self.obj1110, rootNode)
    self.obj1110.postAction( rootNode.CREATE )

    self.obj1111=backward_link(self)
    self.obj1111.isGraphObjectVisual = True

    if(hasattr(self.obj1111, '_setHierarchicalLink')):
      self.obj1111._setHierarchicalLink(False)

    # type
    self.obj1111.type.setValue('ruleDef')

    self.obj1111.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(968.0,305.5,self.obj1111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1111)
    self.globalAndLocalPostcondition(self.obj1111, rootNode)
    self.obj1111.postAction( rootNode.CREATE )

    self.obj1112=hasAttribute_S(self)
    self.obj1112.isGraphObjectVisual = True

    if(hasattr(self.obj1112, '_setHierarchicalLink')):
      self.obj1112._setHierarchicalLink(False)

    self.obj1112.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,166.0,self.obj1112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1112)
    self.globalAndLocalPostcondition(self.obj1112, rootNode)
    self.obj1112.postAction( rootNode.CREATE )

    self.obj1113=hasAttribute_S(self)
    self.obj1113.isGraphObjectVisual = True

    if(hasattr(self.obj1113, '_setHierarchicalLink')):
      self.obj1113._setHierarchicalLink(False)

    self.obj1113.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(402.0,158.5,self.obj1113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1113)
    self.globalAndLocalPostcondition(self.obj1113, rootNode)
    self.obj1113.postAction( rootNode.CREATE )

    self.obj1114=hasAttribute_S(self)
    self.obj1114.isGraphObjectVisual = True

    if(hasattr(self.obj1114, '_setHierarchicalLink')):
      self.obj1114._setHierarchicalLink(False)

    self.obj1114.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(815.5,228.5,self.obj1114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1114)
    self.globalAndLocalPostcondition(self.obj1114, rootNode)
    self.obj1114.postAction( rootNode.CREATE )

    self.obj1115=hasAttribute_T(self)
    self.obj1115.isGraphObjectVisual = True

    if(hasattr(self.obj1115, '_setHierarchicalLink')):
      self.obj1115._setHierarchicalLink(False)

    self.obj1115.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(555.5,442.0,self.obj1115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1115)
    self.globalAndLocalPostcondition(self.obj1115, rootNode)
    self.obj1115.postAction( rootNode.CREATE )

    self.obj1116=hasAttribute_T(self)
    self.obj1116.isGraphObjectVisual = True

    if(hasattr(self.obj1116, '_setHierarchicalLink')):
      self.obj1116._setHierarchicalLink(False)

    self.obj1116.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(283.0,531.5,self.obj1116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1116)
    self.globalAndLocalPostcondition(self.obj1116, rootNode)
    self.obj1116.postAction( rootNode.CREATE )

    self.obj1117=hasAttribute_T(self)
    self.obj1117.isGraphObjectVisual = True

    if(hasattr(self.obj1117, '_setHierarchicalLink')):
      self.obj1117._setHierarchicalLink(False)

    self.obj1117.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(893.0,531.0,self.obj1117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1117)
    self.globalAndLocalPostcondition(self.obj1117, rootNode)
    self.obj1117.postAction( rootNode.CREATE )

    self.obj1118=leftExpr(self)
    self.obj1118.isGraphObjectVisual = True

    if(hasattr(self.obj1118, '_setHierarchicalLink')):
      self.obj1118._setHierarchicalLink(False)

    self.obj1118.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(367.5,245.0,self.obj1118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1118)
    self.globalAndLocalPostcondition(self.obj1118, rootNode)
    self.obj1118.postAction( rootNode.CREATE )

    self.obj1119=leftExpr(self)
    self.obj1119.isGraphObjectVisual = True

    if(hasattr(self.obj1119, '_setHierarchicalLink')):
      self.obj1119._setHierarchicalLink(False)

    self.obj1119.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(556.0,236.5,self.obj1119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1119)
    self.globalAndLocalPostcondition(self.obj1119, rootNode)
    self.obj1119.postAction( rootNode.CREATE )

    self.obj1120=leftExpr(self)
    self.obj1120.isGraphObjectVisual = True

    if(hasattr(self.obj1120, '_setHierarchicalLink')):
      self.obj1120._setHierarchicalLink(False)

    self.obj1120.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(622.0,397.5,self.obj1120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1120)
    self.globalAndLocalPostcondition(self.obj1120, rootNode)
    self.obj1120.postAction( rootNode.CREATE )

    self.obj1121=leftExpr(self)
    self.obj1121.isGraphObjectVisual = True

    if(hasattr(self.obj1121, '_setHierarchicalLink')):
      self.obj1121._setHierarchicalLink(False)

    self.obj1121.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(276.0,616.5,self.obj1121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1121)
    self.globalAndLocalPostcondition(self.obj1121, rootNode)
    self.obj1121.postAction( rootNode.CREATE )

    self.obj1122=leftExpr(self)
    self.obj1122.isGraphObjectVisual = True

    if(hasattr(self.obj1122, '_setHierarchicalLink')):
      self.obj1122._setHierarchicalLink(False)

    self.obj1122.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,616.5,self.obj1122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1122)
    self.globalAndLocalPostcondition(self.obj1122, rootNode)
    self.obj1122.postAction( rootNode.CREATE )

    self.obj1123=rightExpr(self)
    self.obj1123.isGraphObjectVisual = True

    if(hasattr(self.obj1123, '_setHierarchicalLink')):
      self.obj1123._setHierarchicalLink(False)

    self.obj1123.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(367.5,287.5,self.obj1123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1123)
    self.globalAndLocalPostcondition(self.obj1123, rootNode)
    self.obj1123.postAction( rootNode.CREATE )

    self.obj1124=rightExpr(self)
    self.obj1124.isGraphObjectVisual = True

    if(hasattr(self.obj1124, '_setHierarchicalLink')):
      self.obj1124._setHierarchicalLink(False)

    self.obj1124.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(636.0,236.5,self.obj1124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1124)
    self.globalAndLocalPostcondition(self.obj1124, rootNode)
    self.obj1124.postAction( rootNode.CREATE )

    self.obj1125=rightExpr(self)
    self.obj1125.isGraphObjectVisual = True

    if(hasattr(self.obj1125, '_setHierarchicalLink')):
      self.obj1125._setHierarchicalLink(False)

    self.obj1125.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(759.5,337.0,self.obj1125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1125)
    self.globalAndLocalPostcondition(self.obj1125, rootNode)
    self.obj1125.postAction( rootNode.CREATE )

    self.obj1126=rightExpr(self)
    self.obj1126.isGraphObjectVisual = True

    if(hasattr(self.obj1126, '_setHierarchicalLink')):
      self.obj1126._setHierarchicalLink(False)

    self.obj1126.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(356.0,616.5,self.obj1126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1126)
    self.globalAndLocalPostcondition(self.obj1126, rootNode)
    self.obj1126.postAction( rootNode.CREATE )

    self.obj1127=rightExpr(self)
    self.obj1127.isGraphObjectVisual = True

    if(hasattr(self.obj1127, '_setHierarchicalLink')):
      self.obj1127._setHierarchicalLink(False)

    self.obj1127.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,616.5,self.obj1127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1127)
    self.globalAndLocalPostcondition(self.obj1127, rootNode)
    self.obj1127.postAction( rootNode.CREATE )

    # Connections for obj1073 (graphObject_: Obj894) of type MatchModel
    self.drawConnections(
(self.obj1073,self.obj1097,[138.0, 52.0, 142.5, 213.5],"true", 2),
(self.obj1073,self.obj1098,[138.0, 52.0, 234.0, 87.5],"true", 2),
(self.obj1073,self.obj1099,[138.0, 52.0, 571.0, 87.5],"true", 2),
(self.obj1073,self.obj1100,[138.0, 52.0, 477.5, 117.5],"true", 2),
(self.obj1073,self.obj1101,[138.0, 52.0, 582.0, 107.5],"true", 2) )
    # Connections for obj1074 (graphObject_: Obj895) of type ApplyModel
    self.drawConnections(
(self.obj1074,self.obj1102,[147.0, 375.0, 219.5, 417.0],"true", 2),
(self.obj1074,self.obj1103,[147.0, 375.0, 359.5, 432.0],"true", 2),
(self.obj1074,self.obj1104,[147.0, 375.0, 539.5, 431.5],"true", 2) )
    # Connections for obj1075 (graphObject_: Obj896) named triggerS1
    self.drawConnections(
(self.obj1075,self.obj1109,[1030.0, 223.0, 848.0, 187.0],"true", 2) )
    # Connections for obj1076 (graphObject_: Obj897) named signal1
    self.drawConnections(
(self.obj1076,self.obj1114,[817.0, 183.0, 815.5, 228.5],"true", 2) )
    # Connections for obj1077 (graphObject_: Obj898) named transition1
    self.drawConnections(
(self.obj1077,self.obj1108,[1004.0, 123.0, 1024.5, 181.0],"true", 2) )
    # Connections for obj1078 (graphObject_: Obj899) named state1
    self.drawConnections(
(self.obj1078,self.obj1107,[330.0, 123.0, 480.0, 123.0],"true", 2),
(self.obj1078,self.obj1112,[330.0, 123.0, 312.0, 166.0],"true", 2),
(self.obj1078,self.obj1113,[330.0, 123.0, 402.0, 158.5],"true", 2) )
    # Connections for obj1079 (graphObject_: Obj900) named listen1
    self.drawConnections(
(self.obj1079,self.obj1110,[352.0, 489.0, 341.0, 287.0],"true", 2),
(self.obj1079,self.obj1105,[352.0, 489.0, 399.0, 484.0],"true", 2),
(self.obj1079,self.obj1116,[352.0, 489.0, 283.0, 531.5],"true", 2) )
    # Connections for obj1080 (graphObject_: Obj901) named listenBranch1
    self.drawConnections(
(self.obj1080,self.obj1115,[572.0, 491.0, 555.5, 442.0],"true", 2),
(self.obj1080,self.obj1106,[572.0, 491.0, 752.0, 490.0],"true", 2) )
    # Connections for obj1081 (graphObject_: Obj902) named inst1
    self.drawConnections(
(self.obj1081,self.obj1111,[932.0, 488.0, 968.0, 305.5],"true", 2),
(self.obj1081,self.obj1117,[932.0, 488.0, 893.0, 531.0],"true", 2) )
    # Connections for obj1082 (graphObject_: Obj903) named isComposite
    self.drawConnections(
 )
    # Connections for obj1083 (graphObject_: Obj904) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj1084 (graphObject_: Obj905) named name
    self.drawConnections(
 )
    # Connections for obj1085 (graphObject_: Obj906) named channel
    self.drawConnections(
 )
    # Connections for obj1086 (graphObject_: Obj907) named pivot
    self.drawConnections(
 )
    # Connections for obj1087 (graphObject_: Obj908) named pivot
    self.drawConnections(
 )
    # Connections for obj1088 (graphObject_: Obj909) named eq1
    self.drawConnections(
(self.obj1088,self.obj1118,[441.0, 281.0, 367.5, 245.0],"true", 2),
(self.obj1088,self.obj1123,[441.0, 281.0, 367.5, 287.5],"true", 2) )
    # Connections for obj1089 (graphObject_: Obj910) named eq2
    self.drawConnections(
(self.obj1089,self.obj1124,[638.0, 279.0, 636.0, 236.5],"true", 2),
(self.obj1089,self.obj1119,[638.0, 279.0, 556.0, 236.5],"true", 2) )
    # Connections for obj1090 (graphObject_: Obj911) named eq3
    self.drawConnections(
(self.obj1090,self.obj1125,[705.0, 400.0, 759.5, 337.0],"true", 2),
(self.obj1090,self.obj1120,[705.0, 400.0, 622.0, 397.5],"true", 2) )
    # Connections for obj1091 (graphObject_: Obj912) named eq4
    self.drawConnections(
(self.obj1091,self.obj1121,[338.0, 659.0, 276.0, 616.5],"true", 2),
(self.obj1091,self.obj1126,[338.0, 659.0, 356.0, 616.5],"true", 2) )
    # Connections for obj1092 (graphObject_: Obj913) named eq5
    self.drawConnections(
(self.obj1092,self.obj1122,[938.0, 659.0, 896.0, 616.5],"true", 2),
(self.obj1092,self.obj1127,[938.0, 659.0, 996.0, 616.5],"true", 2) )
    # Connections for obj1093 (graphObject_: Obj914) named false
    self.drawConnections(
 )
    # Connections for obj1094 (graphObject_: Obj915) named true
    self.drawConnections(
 )
    # Connections for obj1095 (graphObject_: Obj916) named listensimplestate
    self.drawConnections(
 )
    # Connections for obj1096 (graphObject_: Obj917) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1097 (graphObject_: Obj918) of type paired_with
    self.drawConnections(
(self.obj1097,self.obj1074,[142.5, 213.5, 147.0, 375.0],"true", 2) )
    # Connections for obj1098 (graphObject_: Obj919) of type match_contains
    self.drawConnections(
(self.obj1098,self.obj1078,[234.0, 87.5, 330.0, 123.0],"true", 2) )
    # Connections for obj1099 (graphObject_: Obj920) of type match_contains
    self.drawConnections(
(self.obj1099,self.obj1077,[571.0, 87.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj1100 (graphObject_: Obj921) of type match_contains
    self.drawConnections(
(self.obj1100,self.obj1076,[477.5, 117.5, 817.0, 183.0],"true", 2) )
    # Connections for obj1101 (graphObject_: Obj922) of type match_contains
    self.drawConnections(
(self.obj1101,self.obj1075,[582.0, 107.5, 1030.0, 223.0],"true", 2) )
    # Connections for obj1102 (graphObject_: Obj923) of type apply_contains
    self.drawConnections(
(self.obj1102,self.obj1079,[219.5, 417.0, 352.0, 489.0],"true", 2) )
    # Connections for obj1103 (graphObject_: Obj924) of type apply_contains
    self.drawConnections(
(self.obj1103,self.obj1080,[359.5, 432.0, 572.0, 491.0],"true", 2) )
    # Connections for obj1104 (graphObject_: Obj925) of type apply_contains
    self.drawConnections(
(self.obj1104,self.obj1081,[539.5, 431.5, 932.0, 488.0],"true", 2) )
    # Connections for obj1105 (graphObject_: Obj926) of type directLink_T
    self.drawConnections(
(self.obj1105,self.obj1080,[399.0, 484.0, 572.0, 491.0],"true", 2) )
    # Connections for obj1106 (graphObject_: Obj927) of type directLink_T
    self.drawConnections(
(self.obj1106,self.obj1081,[752.0, 490.0, 932.0, 488.0],"true", 2) )
    # Connections for obj1107 (graphObject_: Obj928) of type directLink_S
    self.drawConnections(
(self.obj1107,self.obj1077,[480.0, 123.0, 1004.0, 123.0],"true", 2) )
    # Connections for obj1108 (graphObject_: Obj929) of type directLink_S
    self.drawConnections(
(self.obj1108,self.obj1075,[984.5, 193.0, 1030.0, 223.0],"true", 2) )
    # Connections for obj1109 (graphObject_: Obj930) of type directLink_S
    self.drawConnections(
(self.obj1109,self.obj1076,[848.0, 187.0, 817.0, 183.0],"true", 2) )
    # Connections for obj1110 (graphObject_: Obj931) of type backward_link
    self.drawConnections(
(self.obj1110,self.obj1078,[341.0, 287.0, 330.0, 123.0],"true", 2) )
    # Connections for obj1111 (graphObject_: Obj932) of type backward_link
    self.drawConnections(
(self.obj1111,self.obj1077,[968.0, 305.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj1112 (graphObject_: Obj933) of type hasAttribute_S
    self.drawConnections(
(self.obj1112,self.obj1082,[312.0, 166.0, 294.0, 209.0],"true", 2) )
    # Connections for obj1113 (graphObject_: Obj934) of type hasAttribute_S
    self.drawConnections(
(self.obj1113,self.obj1083,[402.0, 158.5, 474.0, 194.0],"true", 2) )
    # Connections for obj1114 (graphObject_: Obj935) of type hasAttribute_S
    self.drawConnections(
(self.obj1114,self.obj1084,[815.5, 228.5, 814.0, 274.0],"true", 2) )
    # Connections for obj1115 (graphObject_: Obj936) of type hasAttribute_T
    self.drawConnections(
(self.obj1115,self.obj1085,[555.5, 442.0, 539.0, 395.0],"true", 2) )
    # Connections for obj1116 (graphObject_: Obj937) of type hasAttribute_T
    self.drawConnections(
(self.obj1116,self.obj1086,[283.0, 531.5, 214.0, 574.0],"true", 2) )
    # Connections for obj1117 (graphObject_: Obj938) of type hasAttribute_T
    self.drawConnections(
(self.obj1117,self.obj1087,[893.0, 531.0, 854.0, 574.0],"true", 2) )
    # Connections for obj1118 (graphObject_: Obj939) of type leftExpr
    self.drawConnections(
(self.obj1118,self.obj1082,[367.5, 245.0, 294.0, 209.0],"true", 2) )
    # Connections for obj1119 (graphObject_: Obj940) of type leftExpr
    self.drawConnections(
(self.obj1119,self.obj1083,[556.0, 236.5, 474.0, 194.0],"true", 2) )
    # Connections for obj1120 (graphObject_: Obj941) of type leftExpr
    self.drawConnections(
(self.obj1120,self.obj1085,[622.0, 397.5, 539.0, 395.0],"true", 2) )
    # Connections for obj1121 (graphObject_: Obj942) of type leftExpr
    self.drawConnections(
(self.obj1121,self.obj1086,[276.0, 616.5, 214.0, 574.0],"true", 2) )
    # Connections for obj1122 (graphObject_: Obj943) of type leftExpr
    self.drawConnections(
(self.obj1122,self.obj1087,[896.0, 616.5, 854.0, 574.0],"true", 2) )
    # Connections for obj1123 (graphObject_: Obj944) of type rightExpr
    self.drawConnections(
(self.obj1123,self.obj1093,[367.5, 287.5, 294.0, 294.0],"true", 2) )
    # Connections for obj1124 (graphObject_: Obj945) of type rightExpr
    self.drawConnections(
(self.obj1124,self.obj1094,[636.0, 236.5, 634.0, 194.0],"true", 2) )
    # Connections for obj1125 (graphObject_: Obj946) of type rightExpr
    self.drawConnections(
(self.obj1125,self.obj1084,[759.5, 337.0, 814.0, 274.0],"true", 2) )
    # Connections for obj1126 (graphObject_: Obj947) of type rightExpr
    self.drawConnections(
(self.obj1126,self.obj1095,[356.0, 616.5, 374.0, 574.0],"true", 2) )
    # Connections for obj1127 (graphObject_: Obj948) of type rightExpr
    self.drawConnections(
(self.obj1127,self.obj1096,[996.0, 616.5, 1054.0, 574.0],"true", 2) )

newfunction = Transition2ListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
