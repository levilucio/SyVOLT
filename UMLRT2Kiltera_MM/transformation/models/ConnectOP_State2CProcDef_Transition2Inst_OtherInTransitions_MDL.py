"""
__ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 11:49:27 2014
_________________________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from Vertex import *
from Transition import *
from State import *
from IN1 import *
from Expr import *
from ConditionBranch import *
from Inst import *
from ConditionSet import *
from Attribute import *
from Equation import *
from Concat import *
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
from hasArgs import *
from graph_Attribute import *
from graph_Vertex import *
from graph_Transition import *
from graph_paired_with import *
from graph_State import *
from graph_Equation import *
from graph_backward_link import *
from graph_IN1 import *
from graph_hasArgs import *
from graph_rightExpr import *
from graph_Concat import *
from graph_ConditionBranch import *
from graph_Inst import *
from graph_hasAttribute_T import *
from graph_Expr import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_ApplyModel import *
from graph_ConditionSet import *
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

def ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions')
    # --- ASG attributes over ---


    self.obj220=MatchModel(self)
    self.obj220.isGraphObjectVisual = True

    if(hasattr(self.obj220, '_setHierarchicalLink')):
      self.obj220._setHierarchicalLink(False)

    self.obj220.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj220)
    self.globalAndLocalPostcondition(self.obj220, rootNode)
    self.obj220.postAction( rootNode.CREATE )

    self.obj221=ApplyModel(self)
    self.obj221.isGraphObjectVisual = True

    if(hasattr(self.obj221, '_setHierarchicalLink')):
      self.obj221._setHierarchicalLink(False)

    self.obj221.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,320.0,self.obj221)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj221.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj221)
    self.globalAndLocalPostcondition(self.obj221, rootNode)
    self.obj221.postAction( rootNode.CREATE )

    self.obj238=Vertex(self)
    self.obj238.isGraphObjectVisual = True

    if(hasattr(self.obj238, '_setHierarchicalLink')):
      self.obj238._setHierarchicalLink(False)

    # name
    self.obj238.name.setValue('vertex1')

    # classtype
    self.obj238.classtype.setValue('Vertex')

    # cardinality
    self.obj238.cardinality.setValue('+')

    self.obj238.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,40.0,self.obj238)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj238.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj238)
    self.globalAndLocalPostcondition(self.obj238, rootNode)
    self.obj238.postAction( rootNode.CREATE )

    self.obj224=Transition(self)
    self.obj224.isGraphObjectVisual = True

    if(hasattr(self.obj224, '_setHierarchicalLink')):
      self.obj224._setHierarchicalLink(False)

    # name
    self.obj224.name.setValue('transition1')

    # classtype
    self.obj224.classtype.setValue('Transition')

    # cardinality
    self.obj224.cardinality.setValue('+')

    self.obj224.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(460.0,40.0,self.obj224)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj224.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj224)
    self.globalAndLocalPostcondition(self.obj224, rootNode)
    self.obj224.postAction( rootNode.CREATE )

    self.obj223=State(self)
    self.obj223.isGraphObjectVisual = True

    if(hasattr(self.obj223, '_setHierarchicalLink')):
      self.obj223._setHierarchicalLink(False)

    # name
    self.obj223.name.setValue('state1')

    # classtype
    self.obj223.classtype.setValue('State')

    # cardinality
    self.obj223.cardinality.setValue('+')

    self.obj223.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,40.0,self.obj223)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj223.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj223)
    self.globalAndLocalPostcondition(self.obj223, rootNode)
    self.obj223.postAction( rootNode.CREATE )

    self.obj234=IN1(self)
    self.obj234.isGraphObjectVisual = True

    if(hasattr(self.obj234, '_setHierarchicalLink')):
      self.obj234._setHierarchicalLink(False)

    # classtype
    self.obj234.classtype.setValue('IN1')

    # cardinality
    self.obj234.cardinality.setValue('+')

    # name
    self.obj234.name.setValue('in1_1')

    self.obj234.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(460.0,140.0,self.obj234)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj234.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj234)
    self.globalAndLocalPostcondition(self.obj234, rootNode)
    self.obj234.postAction( rootNode.CREATE )

    self.obj277=Expr(self)
    self.obj277.isGraphObjectVisual = True

    if(hasattr(self.obj277, '_setHierarchicalLink')):
      self.obj277._setHierarchicalLink(False)

    # classtype
    self.obj277.classtype.setValue('Expr')

    # cardinality
    self.obj277.cardinality.setValue('1')

    # name
    self.obj277.name.setValue('expr1')

    self.obj277.graphClass_= graph_Expr
    if self.genGraphics:
       new_obj = graph_Expr(660.0,380.0,self.obj277)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj277.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj277)
    self.globalAndLocalPostcondition(self.obj277, rootNode)
    self.obj277.postAction( rootNode.CREATE )

    self.obj269=ConditionBranch(self)
    self.obj269.isGraphObjectVisual = True

    if(hasattr(self.obj269, '_setHierarchicalLink')):
      self.obj269._setHierarchicalLink(False)

    # classtype
    self.obj269.classtype.setValue('ConditionBranch')

    # cardinality
    self.obj269.cardinality.setValue('1')

    # name
    self.obj269.name.setValue('conditionbranch1')

    self.obj269.graphClass_= graph_ConditionBranch
    if self.genGraphics:
       new_obj = graph_ConditionBranch(460.0,380.0,self.obj269)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj269.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj269)
    self.globalAndLocalPostcondition(self.obj269, rootNode)
    self.obj269.postAction( rootNode.CREATE )

    self.obj283=Inst(self)
    self.obj283.isGraphObjectVisual = True

    if(hasattr(self.obj283, '_setHierarchicalLink')):
      self.obj283._setHierarchicalLink(False)

    # classtype
    self.obj283.classtype.setValue('Inst')

    # cardinality
    self.obj283.cardinality.setValue('1')

    # name
    self.obj283.name.setValue('inst1')

    self.obj283.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(840.0,480.0,self.obj283)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj283.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj283)
    self.globalAndLocalPostcondition(self.obj283, rootNode)
    self.obj283.postAction( rootNode.CREATE )

    self.obj268=ConditionSet(self)
    self.obj268.isGraphObjectVisual = True

    if(hasattr(self.obj268, '_setHierarchicalLink')):
      self.obj268._setHierarchicalLink(False)

    # classtype
    self.obj268.classtype.setValue('ConditionSet')

    # cardinality
    self.obj268.cardinality.setValue('1')

    # name
    self.obj268.name.setValue('conditionset1')

    self.obj268.graphClass_= graph_ConditionSet
    if self.genGraphics:
       new_obj = graph_ConditionSet(180.0,380.0,self.obj268)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionSet", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj268.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj268)
    self.globalAndLocalPostcondition(self.obj268, rootNode)
    self.obj268.postAction( rootNode.CREATE )

    self.obj246=Attribute(self)
    self.obj246.isGraphObjectVisual = True

    if(hasattr(self.obj246, '_setHierarchicalLink')):
      self.obj246._setHierarchicalLink(False)

    # Type
    self.obj246.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj246.Type.config = 0

    # name
    self.obj246.name.setValue('name')

    self.obj246.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,140.0,self.obj246)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj246.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj246)
    self.globalAndLocalPostcondition(self.obj246, rootNode)
    self.obj246.postAction( rootNode.CREATE )

    self.obj250=Attribute(self)
    self.obj250.isGraphObjectVisual = True

    if(hasattr(self.obj250, '_setHierarchicalLink')):
      self.obj250._setHierarchicalLink(False)

    # Type
    self.obj250.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj250.Type.config = 0

    # name
    self.obj250.name.setValue('isComposite')

    self.obj250.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,140.0,self.obj250)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj250.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj250)
    self.globalAndLocalPostcondition(self.obj250, rootNode)
    self.obj250.postAction( rootNode.CREATE )

    self.obj289=Attribute(self)
    self.obj289.isGraphObjectVisual = True

    if(hasattr(self.obj289, '_setHierarchicalLink')):
      self.obj289._setHierarchicalLink(False)

    # Type
    self.obj289.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj289.Type.config = 0

    # name
    self.obj289.name.setValue('literal')

    self.obj289.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,380.0,self.obj289)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj289.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj289)
    self.globalAndLocalPostcondition(self.obj289, rootNode)
    self.obj289.postAction( rootNode.CREATE )

    self.obj318=Attribute(self)
    self.obj318.isGraphObjectVisual = True

    if(hasattr(self.obj318, '_setHierarchicalLink')):
      self.obj318._setHierarchicalLink(False)

    # Type
    self.obj318.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj318.Type.config = 0

    # name
    self.obj318.name.setValue('pivotin')

    self.obj318.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(900.0,580.0,self.obj318)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj318.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj318)
    self.globalAndLocalPostcondition(self.obj318, rootNode)
    self.obj318.postAction( rootNode.CREATE )

    self.obj404=Attribute(self)
    self.obj404.isGraphObjectVisual = True

    if(hasattr(self.obj404, '_setHierarchicalLink')):
      self.obj404._setHierarchicalLink(False)

    # Type
    self.obj404.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj404.Type.config = 0

    # name
    self.obj404.name.setValue('pivotin')

    self.obj404.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(140.0,540.0,self.obj404)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj404.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj404)
    self.globalAndLocalPostcondition(self.obj404, rootNode)
    self.obj404.postAction( rootNode.CREATE )

    self.obj253=Equation(self)
    self.obj253.isGraphObjectVisual = True

    if(hasattr(self.obj253, '_setHierarchicalLink')):
      self.obj253._setHierarchicalLink(False)

    # name
    self.obj253.name.setValue('eq1')

    self.obj253.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,220.0,self.obj253)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj253.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj253)
    self.globalAndLocalPostcondition(self.obj253, rootNode)
    self.obj253.postAction( rootNode.CREATE )

    self.obj293=Equation(self)
    self.obj293.isGraphObjectVisual = True

    if(hasattr(self.obj293, '_setHierarchicalLink')):
      self.obj293._setHierarchicalLink(False)

    # name
    self.obj293.name.setValue('eq2')

    self.obj293.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(840.0,300.0,self.obj293)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj293.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj293)
    self.globalAndLocalPostcondition(self.obj293, rootNode)
    self.obj293.postAction( rootNode.CREATE )

    self.obj322=Equation(self)
    self.obj322.isGraphObjectVisual = True

    if(hasattr(self.obj322, '_setHierarchicalLink')):
      self.obj322._setHierarchicalLink(False)

    # name
    self.obj322.name.setValue('eq3')

    self.obj322.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,660.0,self.obj322)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj322.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj322)
    self.globalAndLocalPostcondition(self.obj322, rootNode)
    self.obj322.postAction( rootNode.CREATE )

    self.obj407=Equation(self)
    self.obj407.isGraphObjectVisual = True

    if(hasattr(self.obj407, '_setHierarchicalLink')):
      self.obj407._setHierarchicalLink(False)

    # name
    self.obj407.name.setValue('eq4')

    self.obj407.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,620.0,self.obj407)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj407.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj407)
    self.globalAndLocalPostcondition(self.obj407, rootNode)
    self.obj407.postAction( rootNode.CREATE )

    self.obj297=Concat(self)
    self.obj297.isGraphObjectVisual = True

    if(hasattr(self.obj297, '_setHierarchicalLink')):
      self.obj297._setHierarchicalLink(False)

    # Type
    self.obj297.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj297.Type.config = 0

    # name
    self.obj297.name.setValue('concat1')

    self.obj297.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(680.0,300.0,self.obj297)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj297.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj297)
    self.globalAndLocalPostcondition(self.obj297, rootNode)
    self.obj297.postAction( rootNode.CREATE )

    self.obj256=Constant(self)
    self.obj256.isGraphObjectVisual = True

    if(hasattr(self.obj256, '_setHierarchicalLink')):
      self.obj256._setHierarchicalLink(False)

    # Type
    self.obj256.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj256.Type.config = 0

    # name
    self.obj256.name.setValue('true')

    self.obj256.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(320.0,140.0,self.obj256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj256.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj256)
    self.globalAndLocalPostcondition(self.obj256, rootNode)
    self.obj256.postAction( rootNode.CREATE )

    self.obj300=Constant(self)
    self.obj300.isGraphObjectVisual = True

    if(hasattr(self.obj300, '_setHierarchicalLink')):
      self.obj300._setHierarchicalLink(False)

    # Type
    self.obj300.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj300.Type.config = 0

    # name
    self.obj300.name.setValue('enp="')

    self.obj300.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(520.0,300.0,self.obj300)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj300.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj300)
    self.globalAndLocalPostcondition(self.obj300, rootNode)
    self.obj300.postAction( rootNode.CREATE )

    self.obj305=Constant(self)
    self.obj305.isGraphObjectVisual = True

    if(hasattr(self.obj305, '_setHierarchicalLink')):
      self.obj305._setHierarchicalLink(False)

    # Type
    self.obj305.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj305.Type.config = 0

    # name
    self.obj305.name.setValue('"')

    self.obj305.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,220.0,self.obj305)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj305.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj305)
    self.globalAndLocalPostcondition(self.obj305, rootNode)
    self.obj305.postAction( rootNode.CREATE )

    self.obj315=Constant(self)
    self.obj315.isGraphObjectVisual = True

    if(hasattr(self.obj315, '_setHierarchicalLink')):
      self.obj315._setHierarchicalLink(False)

    # Type
    self.obj315.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj315.Type.config = 0

    # name
    self.obj315.name.setValue('instForInTrans')

    self.obj315.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(740.0,580.0,self.obj315)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj315.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj315)
    self.globalAndLocalPostcondition(self.obj315, rootNode)
    self.obj315.postAction( rootNode.CREATE )

    self.obj410=Constant(self)
    self.obj410.isGraphObjectVisual = True

    if(hasattr(self.obj410, '_setHierarchicalLink')):
      self.obj410._setHierarchicalLink(False)

    # Type
    self.obj410.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj410.Type.config = 0

    # name
    self.obj410.name.setValue('condsetcompstate')

    self.obj410.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(300.0,540.0,self.obj410)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj410.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj410)
    self.globalAndLocalPostcondition(self.obj410, rootNode)
    self.obj410.postAction( rootNode.CREATE )

    self.obj222=paired_with(self)
    self.obj222.isGraphObjectVisual = True

    if(hasattr(self.obj222, '_setHierarchicalLink')):
      self.obj222._setHierarchicalLink(False)

    self.obj222.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj222)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj222.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj222)
    self.globalAndLocalPostcondition(self.obj222, rootNode)
    self.obj222.postAction( rootNode.CREATE )

    self.obj264=match_contains(self)
    self.obj264.isGraphObjectVisual = True

    if(hasattr(self.obj264, '_setHierarchicalLink')):
      self.obj264._setHierarchicalLink(False)

    self.obj264.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,67.0,self.obj264)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj264.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj264)
    self.globalAndLocalPostcondition(self.obj264, rootNode)
    self.obj264.postAction( rootNode.CREATE )

    self.obj265=match_contains(self)
    self.obj265.isGraphObjectVisual = True

    if(hasattr(self.obj265, '_setHierarchicalLink')):
      self.obj265._setHierarchicalLink(False)

    self.obj265.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,67.0,self.obj265)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj265.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj265)
    self.globalAndLocalPostcondition(self.obj265, rootNode)
    self.obj265.postAction( rootNode.CREATE )

    self.obj266=match_contains(self)
    self.obj266.isGraphObjectVisual = True

    if(hasattr(self.obj266, '_setHierarchicalLink')):
      self.obj266._setHierarchicalLink(False)

    self.obj266.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,67.0,self.obj266)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj266.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj266)
    self.globalAndLocalPostcondition(self.obj266, rootNode)
    self.obj266.postAction( rootNode.CREATE )

    self.obj267=match_contains(self)
    self.obj267.isGraphObjectVisual = True

    if(hasattr(self.obj267, '_setHierarchicalLink')):
      self.obj267._setHierarchicalLink(False)

    self.obj267.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,117.0,self.obj267)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj267.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj267)
    self.globalAndLocalPostcondition(self.obj267, rootNode)
    self.obj267.postAction( rootNode.CREATE )

    self.obj310=apply_contains(self)
    self.obj310.isGraphObjectVisual = True

    if(hasattr(self.obj310, '_setHierarchicalLink')):
      self.obj310._setHierarchicalLink(False)

    self.obj310.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,392.0,self.obj310)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj310.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj310)
    self.globalAndLocalPostcondition(self.obj310, rootNode)
    self.obj310.postAction( rootNode.CREATE )

    self.obj311=apply_contains(self)
    self.obj311.isGraphObjectVisual = True

    if(hasattr(self.obj311, '_setHierarchicalLink')):
      self.obj311._setHierarchicalLink(False)

    self.obj311.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(387.5,392.0,self.obj311)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj311.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj311)
    self.globalAndLocalPostcondition(self.obj311, rootNode)
    self.obj311.postAction( rootNode.CREATE )

    self.obj312=apply_contains(self)
    self.obj312.isGraphObjectVisual = True

    if(hasattr(self.obj312, '_setHierarchicalLink')):
      self.obj312._setHierarchicalLink(False)

    self.obj312.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,392.0,self.obj312)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj312.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj312)
    self.globalAndLocalPostcondition(self.obj312, rootNode)
    self.obj312.postAction( rootNode.CREATE )

    self.obj313=apply_contains(self)
    self.obj313.isGraphObjectVisual = True

    if(hasattr(self.obj313, '_setHierarchicalLink')):
      self.obj313._setHierarchicalLink(False)

    self.obj313.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(140.5,529.0,self.obj313)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj313.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj313)
    self.globalAndLocalPostcondition(self.obj313, rootNode)
    self.obj313.postAction( rootNode.CREATE )

    self.obj270=directLink_T(self)
    self.obj270.isGraphObjectVisual = True

    if(hasattr(self.obj270, '_setHierarchicalLink')):
      self.obj270._setHierarchicalLink(False)

    # associationType
    self.obj270.associationType.setValue('branches')

    self.obj270.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(492.0,431.0,self.obj270)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj270.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj270)
    self.globalAndLocalPostcondition(self.obj270, rootNode)
    self.obj270.postAction( rootNode.CREATE )

    self.obj278=directLink_T(self)
    self.obj278.isGraphObjectVisual = True

    if(hasattr(self.obj278, '_setHierarchicalLink')):
      self.obj278._setHierarchicalLink(False)

    # associationType
    self.obj278.associationType.setValue('if')

    self.obj278.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(732.0,431.0,self.obj278)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj278.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj278)
    self.globalAndLocalPostcondition(self.obj278, rootNode)
    self.obj278.postAction( rootNode.CREATE )

    self.obj286=directLink_T(self)
    self.obj286.isGraphObjectVisual = True

    if(hasattr(self.obj286, '_setHierarchicalLink')):
      self.obj286._setHierarchicalLink(False)

    # associationType
    self.obj286.associationType.setValue('then')

    self.obj286.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(651.0,513.0,self.obj286)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj286.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj286)
    self.globalAndLocalPostcondition(self.obj286, rootNode)
    self.obj286.postAction( rootNode.CREATE )

    self.obj225=directLink_S(self)
    self.obj225.isGraphObjectVisual = True

    if(hasattr(self.obj225, '_setHierarchicalLink')):
      self.obj225._setHierarchicalLink(False)

    # associationType
    self.obj225.associationType.setValue('transitions')

    self.obj225.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,83.0,self.obj225)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj225.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj225)
    self.globalAndLocalPostcondition(self.obj225, rootNode)
    self.obj225.postAction( rootNode.CREATE )

    self.obj235=directLink_S(self)
    self.obj235.isGraphObjectVisual = True

    if(hasattr(self.obj235, '_setHierarchicalLink')):
      self.obj235._setHierarchicalLink(False)

    # associationType
    self.obj235.associationType.setValue('type')

    self.obj235.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(630.0,133.0,self.obj235)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj235.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj235)
    self.globalAndLocalPostcondition(self.obj235, rootNode)
    self.obj235.postAction( rootNode.CREATE )

    self.obj239=directLink_S(self)
    self.obj239.isGraphObjectVisual = True

    if(hasattr(self.obj239, '_setHierarchicalLink')):
      self.obj239._setHierarchicalLink(False)

    # associationType
    self.obj239.associationType.setValue('src')

    self.obj239.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(730.0,83.0,self.obj239)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj239.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj239)
    self.globalAndLocalPostcondition(self.obj239, rootNode)
    self.obj239.postAction( rootNode.CREATE )

    self.obj314=backward_link(self)
    self.obj314.isGraphObjectVisual = True

    if(hasattr(self.obj314, '_setHierarchicalLink')):
      self.obj314._setHierarchicalLink(False)

    # type
    self.obj314.type.setValue('ruleDef')

    self.obj314.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(821.0,307.0,self.obj314)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj314.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj314)
    self.globalAndLocalPostcondition(self.obj314, rootNode)
    self.obj314.postAction( rootNode.CREATE )

    self.obj395=backward_link(self)
    self.obj395.isGraphObjectVisual = True

    if(hasattr(self.obj395, '_setHierarchicalLink')):
      self.obj395._setHierarchicalLink(False)

    # type
    self.obj395.type.setValue('ruleDef')

    self.obj395.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,257.0,self.obj395)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj395.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj395)
    self.globalAndLocalPostcondition(self.obj395, rootNode)
    self.obj395.postAction( rootNode.CREATE )

    self.obj249=hasAttribute_S(self)
    self.obj249.isGraphObjectVisual = True

    if(hasattr(self.obj249, '_setHierarchicalLink')):
      self.obj249._setHierarchicalLink(False)

    self.obj249.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(812.0,128.5,self.obj249)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj249.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj249)
    self.globalAndLocalPostcondition(self.obj249, rootNode)
    self.obj249.postAction( rootNode.CREATE )

    self.obj259=hasAttribute_S(self)
    self.obj259.isGraphObjectVisual = True

    if(hasattr(self.obj259, '_setHierarchicalLink')):
      self.obj259._setHierarchicalLink(False)

    self.obj259.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,128.5,self.obj259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj259)
    self.globalAndLocalPostcondition(self.obj259, rootNode)
    self.obj259.postAction( rootNode.CREATE )

    self.obj292=hasAttribute_T(self)
    self.obj292.isGraphObjectVisual = True

    if(hasattr(self.obj292, '_setHierarchicalLink')):
      self.obj292._setHierarchicalLink(False)

    self.obj292.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(903.0,422.5,self.obj292)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj292.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj292)
    self.globalAndLocalPostcondition(self.obj292, rootNode)
    self.obj292.postAction( rootNode.CREATE )

    self.obj321=hasAttribute_T(self)
    self.obj321.isGraphObjectVisual = True

    if(hasattr(self.obj321, '_setHierarchicalLink')):
      self.obj321._setHierarchicalLink(False)

    self.obj321.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1023.0,572.5,self.obj321)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj321.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj321)
    self.globalAndLocalPostcondition(self.obj321, rootNode)
    self.obj321.postAction( rootNode.CREATE )

    self.obj413=hasAttribute_T(self)
    self.obj413.isGraphObjectVisual = True

    if(hasattr(self.obj413, '_setHierarchicalLink')):
      self.obj413._setHierarchicalLink(False)

    self.obj413.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(313.0,502.5,self.obj413)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj413.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj413)
    self.globalAndLocalPostcondition(self.obj413, rootNode)
    self.obj413.postAction( rootNode.CREATE )

    self.obj260=leftExpr(self)
    self.obj260.isGraphObjectVisual = True

    if(hasattr(self.obj260, '_setHierarchicalLink')):
      self.obj260._setHierarchicalLink(False)

    self.obj260.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(336.0,216.5,self.obj260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj260)
    self.globalAndLocalPostcondition(self.obj260, rootNode)
    self.obj260.postAction( rootNode.CREATE )

    self.obj296=leftExpr(self)
    self.obj296.isGraphObjectVisual = True

    if(hasattr(self.obj296, '_setHierarchicalLink')):
      self.obj296._setHierarchicalLink(False)

    self.obj296.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(976.0,376.5,self.obj296)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj296.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj296)
    self.globalAndLocalPostcondition(self.obj296, rootNode)
    self.obj296.postAction( rootNode.CREATE )

    self.obj325=leftExpr(self)
    self.obj325.isGraphObjectVisual = True

    if(hasattr(self.obj325, '_setHierarchicalLink')):
      self.obj325._setHierarchicalLink(False)

    self.obj325.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(996.0,656.5,self.obj325)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj325.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj325)
    self.globalAndLocalPostcondition(self.obj325, rootNode)
    self.obj325.postAction( rootNode.CREATE )

    self.obj414=leftExpr(self)
    self.obj414.isGraphObjectVisual = True

    if(hasattr(self.obj414, '_setHierarchicalLink')):
      self.obj414._setHierarchicalLink(False)

    self.obj414.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(326.0,616.5,self.obj414)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj414.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj414)
    self.globalAndLocalPostcondition(self.obj414, rootNode)
    self.obj414.postAction( rootNode.CREATE )

    self.obj261=rightExpr(self)
    self.obj261.isGraphObjectVisual = True

    if(hasattr(self.obj261, '_setHierarchicalLink')):
      self.obj261._setHierarchicalLink(False)

    self.obj261.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(416.0,216.5,self.obj261)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj261.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj261)
    self.globalAndLocalPostcondition(self.obj261, rootNode)
    self.obj261.postAction( rootNode.CREATE )

    self.obj309=rightExpr(self)
    self.obj309.isGraphObjectVisual = True

    if(hasattr(self.obj309, '_setHierarchicalLink')):
      self.obj309._setHierarchicalLink(False)

    self.obj309.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(896.0,336.5,self.obj309)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj309.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj309)
    self.globalAndLocalPostcondition(self.obj309, rootNode)
    self.obj309.postAction( rootNode.CREATE )

    self.obj326=rightExpr(self)
    self.obj326.isGraphObjectVisual = True

    if(hasattr(self.obj326, '_setHierarchicalLink')):
      self.obj326._setHierarchicalLink(False)

    self.obj326.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(916.0,656.5,self.obj326)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj326.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj326)
    self.globalAndLocalPostcondition(self.obj326, rootNode)
    self.obj326.postAction( rootNode.CREATE )

    self.obj415=rightExpr(self)
    self.obj415.isGraphObjectVisual = True

    if(hasattr(self.obj415, '_setHierarchicalLink')):
      self.obj415._setHierarchicalLink(False)

    self.obj415.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(406.0,616.5,self.obj415)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj415.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj415)
    self.globalAndLocalPostcondition(self.obj415, rootNode)
    self.obj415.postAction( rootNode.CREATE )

    self.obj303=hasArgs(self)
    self.obj303.isGraphObjectVisual = True

    if(hasattr(self.obj303, '_setHierarchicalLink')):
      self.obj303._setHierarchicalLink(False)

    self.obj303.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(734.0,334.0,self.obj303)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj303.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj303)
    self.globalAndLocalPostcondition(self.obj303, rootNode)
    self.obj303.postAction( rootNode.CREATE )

    self.obj304=hasArgs(self)
    self.obj304.isGraphObjectVisual = True

    if(hasattr(self.obj304, '_setHierarchicalLink')):
      self.obj304._setHierarchicalLink(False)

    self.obj304.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(771.0,274.0,self.obj304)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj304.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj304)
    self.globalAndLocalPostcondition(self.obj304, rootNode)
    self.obj304.postAction( rootNode.CREATE )

    self.obj308=hasArgs(self)
    self.obj308.isGraphObjectVisual = True

    if(hasattr(self.obj308, '_setHierarchicalLink')):
      self.obj308._setHierarchicalLink(False)

    self.obj308.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(894.0,294.0,self.obj308)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj308.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj308)
    self.globalAndLocalPostcondition(self.obj308, rootNode)
    self.obj308.postAction( rootNode.CREATE )

    # Connections for obj220 (graphObject_: Obj27) of type MatchModel
    self.drawConnections(
(self.obj220,self.obj222,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj220,self.obj264,[138.0, 51.0, 234.0, 67.0],"true", 0),
(self.obj220,self.obj265,[138.0, 51.0, 384.0, 67.0],"true", 0),
(self.obj220,self.obj266,[138.0, 51.0, 484.0, 67.0],"true", 0),
(self.obj220,self.obj267,[138.0, 51.0, 384.0, 117.0],"true", 0) )
    # Connections for obj221 (graphObject_: Obj28) of type ApplyModel
    self.drawConnections(
(self.obj221,self.obj310,[143.0, 353.0, 247.5, 392.0],"true", 0),
(self.obj221,self.obj311,[143.0, 353.0, 387.5, 392.0],"true", 0),
(self.obj221,self.obj312,[143.0, 353.0, 487.5, 392.0],"true", 0),
(self.obj221,self.obj313,[143.0, 353.0, 140.5, 529.0],"true", 0) )
    # Connections for obj238 (graphObject_: Obj35) named vertex1
    self.drawConnections(
(self.obj238,self.obj249,[830.0, 83.0, 812.0, 128.5],"true", 2) )
    # Connections for obj224 (graphObject_: Obj31) named transition1
    self.drawConnections(
(self.obj224,self.obj235,[630.0, 83.0, 630.0, 133.0],"true", 2),
(self.obj224,self.obj239,[630.0, 83.0, 730.0, 83.0],"true", 2) )
    # Connections for obj223 (graphObject_: Obj30) named state1
    self.drawConnections(
(self.obj223,self.obj225,[330.0, 83.0, 480.0, 83.0],"true", 2),
(self.obj223,self.obj259,[330.0, 83.0, 312.0, 128.5],"true", 2) )
    # Connections for obj234 (graphObject_: Obj33) named in1_1
    self.drawConnections(
 )
    # Connections for obj277 (graphObject_: Obj52) named expr1
    self.drawConnections(
(self.obj277,self.obj292,[832.0, 431.0, 903.0, 422.5],"true", 2) )
    # Connections for obj269 (graphObject_: Obj50) named conditionbranch1
    self.drawConnections(
(self.obj269,self.obj278,[632.0, 431.0, 732.0, 431.0],"true", 2),
(self.obj269,self.obj286,[632.0, 431.0, 651.0, 513.0],"true", 2) )
    # Connections for obj283 (graphObject_: Obj54) named inst1
    self.drawConnections(
(self.obj283,self.obj314,[1012.0, 531.0, 821.0, 307.0],"true", 2),
(self.obj283,self.obj321,[1012.0, 531.0, 1023.0, 572.5],"true", 2) )
    # Connections for obj268 (graphObject_: Obj49) named conditionset1
    self.drawConnections(
(self.obj268,self.obj270,[352.0, 431.0, 492.0, 431.0],"true", 2),
(self.obj268,self.obj395,[352.0, 431.0, 341.0, 257.0],"true", 0),
(self.obj268,self.obj413,[352.0, 431.0, 313.0, 502.5],"true", 0) )
    # Connections for obj246 (graphObject_: Obj37) named name
    self.drawConnections(
 )
    # Connections for obj250 (graphObject_: Obj39) named isComposite
    self.drawConnections(
 )
    # Connections for obj289 (graphObject_: Obj56) named literal
    self.drawConnections(
 )
    # Connections for obj318 (graphObject_: Obj73) named pivotin
    self.drawConnections(
 )
    # Connections for obj404 (graphObject_: Obj79) named pivotin
    self.drawConnections(
 )
    # Connections for obj253 (graphObject_: Obj40) named eq1
    self.drawConnections(
(self.obj253,self.obj260,[378.0, 259.0, 336.0, 216.5],"true", 2),
(self.obj253,self.obj261,[378.0, 259.0, 416.0, 216.5],"true", 2) )
    # Connections for obj293 (graphObject_: Obj58) named eq2
    self.drawConnections(
(self.obj293,self.obj296,[978.0, 339.0, 976.0, 376.5],"true", 2),
(self.obj293,self.obj309,[978.0, 339.0, 896.0, 336.5],"true", 2) )
    # Connections for obj322 (graphObject_: Obj75) named eq3
    self.drawConnections(
(self.obj322,self.obj325,[958.0, 699.0, 996.0, 656.5],"true", 2),
(self.obj322,self.obj326,[958.0, 699.0, 916.0, 656.5],"true", 2) )
    # Connections for obj407 (graphObject_: Obj80) named eq4
    self.drawConnections(
(self.obj407,self.obj414,[378.0, 659.0, 326.0, 616.5],"true", 2),
(self.obj407,self.obj415,[378.0, 659.0, 406.0, 616.5],"true", 2) )
    # Connections for obj297 (graphObject_: Obj60) named concat1
    self.drawConnections(
(self.obj297,self.obj303,[814.0, 334.0, 734.0, 334.0],"true", 2),
(self.obj297,self.obj304,[814.0, 334.0, 771.0, 274.0],"true", 2),
(self.obj297,self.obj308,[814.0, 334.0, 894.0, 294.0],"true", 2) )
    # Connections for obj256 (graphObject_: Obj41) named true
    self.drawConnections(
 )
    # Connections for obj300 (graphObject_: Obj61) named enp="
    self.drawConnections(
 )
    # Connections for obj305 (graphObject_: Obj64) named "
    self.drawConnections(
 )
    # Connections for obj315 (graphObject_: Obj72) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj410 (graphObject_: Obj81) named condsetcompstate
    self.drawConnections(
 )
    # Connections for obj222 (graphObject_: Obj29) of type paired_with
    self.drawConnections(
(self.obj222,self.obj221,[140.5, 152.0, 143.0, 353.0],"true", 2) )
    # Connections for obj264 (graphObject_: Obj45) of type match_contains
    self.drawConnections(
(self.obj264,self.obj223,[234.0, 67.0, 330.0, 83.0],"true", 2) )
    # Connections for obj265 (graphObject_: Obj46) of type match_contains
    self.drawConnections(
(self.obj265,self.obj224,[384.0, 67.0, 630.0, 83.0],"true", 2) )
    # Connections for obj266 (graphObject_: Obj47) of type match_contains
    self.drawConnections(
(self.obj266,self.obj238,[484.0, 67.0, 830.0, 83.0],"true", 2) )
    # Connections for obj267 (graphObject_: Obj48) of type match_contains
    self.drawConnections(
(self.obj267,self.obj234,[384.0, 117.0, 630.0, 183.0],"true", 2) )
    # Connections for obj310 (graphObject_: Obj67) of type apply_contains
    self.drawConnections(
(self.obj310,self.obj268,[247.5, 392.0, 352.0, 431.0],"true", 2) )
    # Connections for obj311 (graphObject_: Obj68) of type apply_contains
    self.drawConnections(
(self.obj311,self.obj269,[387.5, 392.0, 632.0, 431.0],"true", 2) )
    # Connections for obj312 (graphObject_: Obj69) of type apply_contains
    self.drawConnections(
(self.obj312,self.obj277,[487.5, 392.0, 832.0, 431.0],"true", 2) )
    # Connections for obj313 (graphObject_: Obj70) of type apply_contains
    self.drawConnections(
(self.obj313,self.obj283,[140.5, 529.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj270 (graphObject_: Obj51) of type directLink_T
    self.drawConnections(
(self.obj270,self.obj269,[492.0, 431.0, 632.0, 431.0],"true", 2) )
    # Connections for obj278 (graphObject_: Obj53) of type directLink_T
    self.drawConnections(
(self.obj278,self.obj277,[732.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj286 (graphObject_: Obj55) of type directLink_T
    self.drawConnections(
(self.obj286,self.obj283,[651.0, 513.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj225 (graphObject_: Obj32) of type directLink_S
    self.drawConnections(
(self.obj225,self.obj224,[480.0, 83.0, 630.0, 83.0],"true", 2) )
    # Connections for obj235 (graphObject_: Obj34) of type directLink_S
    self.drawConnections(
(self.obj235,self.obj234,[630.0, 133.0, 630.0, 183.0],"true", 2) )
    # Connections for obj239 (graphObject_: Obj36) of type directLink_S
    self.drawConnections(
(self.obj239,self.obj238,[730.0, 83.0, 830.0, 83.0],"true", 2) )
    # Connections for obj314 (graphObject_: Obj71) of type backward_link
    self.drawConnections(
(self.obj314,self.obj224,[821.0, 307.0, 630.0, 83.0],"true", 2) )
    # Connections for obj395 (graphObject_: Obj78) of type backward_link
    self.drawConnections(
(self.obj395,self.obj223,[341.0, 257.0, 330.0, 83.0],"true", 2) )
    # Connections for obj249 (graphObject_: Obj38) of type hasAttribute_S
    self.drawConnections(
(self.obj249,self.obj246,[812.0, 128.5, 774.0, 174.0],"true", 2) )
    # Connections for obj259 (graphObject_: Obj42) of type hasAttribute_S
    self.drawConnections(
(self.obj259,self.obj250,[312.0, 128.5, 294.0, 174.0],"true", 2) )
    # Connections for obj292 (graphObject_: Obj57) of type hasAttribute_T
    self.drawConnections(
(self.obj292,self.obj289,[903.0, 422.5, 974.0, 414.0],"true", 2) )
    # Connections for obj321 (graphObject_: Obj74) of type hasAttribute_T
    self.drawConnections(
(self.obj321,self.obj318,[1023.0, 572.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj413 (graphObject_: Obj82) of type hasAttribute_T
    self.drawConnections(
(self.obj413,self.obj404,[313.0, 502.5, 274.0, 574.0],"true", 2) )
    # Connections for obj260 (graphObject_: Obj43) of type leftExpr
    self.drawConnections(
(self.obj260,self.obj250,[336.0, 216.5, 294.0, 174.0],"true", 2) )
    # Connections for obj296 (graphObject_: Obj59) of type leftExpr
    self.drawConnections(
(self.obj296,self.obj289,[976.0, 376.5, 974.0, 414.0],"true", 2) )
    # Connections for obj325 (graphObject_: Obj76) of type leftExpr
    self.drawConnections(
(self.obj325,self.obj318,[996.0, 656.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj414 (graphObject_: Obj83) of type leftExpr
    self.drawConnections(
(self.obj414,self.obj404,[326.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj261 (graphObject_: Obj44) of type rightExpr
    self.drawConnections(
(self.obj261,self.obj256,[416.0, 216.5, 454.0, 174.0],"true", 2) )
    # Connections for obj309 (graphObject_: Obj66) of type rightExpr
    self.drawConnections(
(self.obj309,self.obj297,[896.0, 336.5, 814.0, 334.0],"true", 2) )
    # Connections for obj326 (graphObject_: Obj77) of type rightExpr
    self.drawConnections(
(self.obj326,self.obj315,[916.0, 656.5, 874.0, 614.0],"true", 2) )
    # Connections for obj415 (graphObject_: Obj84) of type rightExpr
    self.drawConnections(
(self.obj415,self.obj410,[406.0, 616.5, 434.0, 574.0],"true", 2) )
    # Connections for obj303 (graphObject_: Obj62) of type hasArgs
    self.drawConnections(
(self.obj303,self.obj300,[734.0, 334.0, 654.0, 334.0],"true", 2) )
    # Connections for obj304 (graphObject_: Obj63) of type hasArgs
    self.drawConnections(
(self.obj304,self.obj246,[771.0, 274.0, 774.0, 174.0],"true", 2) )
    # Connections for obj308 (graphObject_: Obj65) of type hasArgs
    self.drawConnections(
(self.obj308,self.obj305,[894.0, 294.0, 934.0, 254.0],"true", 2) )

newfunction = ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
