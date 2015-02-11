"""
__ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:55:49 2015
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

def ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions')
    # --- ASG attributes over ---


    self.obj337=MatchModel(self)
    self.obj337.isGraphObjectVisual = True

    if(hasattr(self.obj337, '_setHierarchicalLink')):
      self.obj337._setHierarchicalLink(False)

    self.obj337.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj337)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj337.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj337)
    self.globalAndLocalPostcondition(self.obj337, rootNode)
    self.obj337.postAction( rootNode.CREATE )

    self.obj338=ApplyModel(self)
    self.obj338.isGraphObjectVisual = True

    if(hasattr(self.obj338, '_setHierarchicalLink')):
      self.obj338._setHierarchicalLink(False)

    self.obj338.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,320.0,self.obj338)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj338.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj338)
    self.globalAndLocalPostcondition(self.obj338, rootNode)
    self.obj338.postAction( rootNode.CREATE )

    self.obj339=Vertex(self)
    self.obj339.isGraphObjectVisual = True

    if(hasattr(self.obj339, '_setHierarchicalLink')):
      self.obj339._setHierarchicalLink(False)

    # name
    self.obj339.name.setValue('vertex1')

    # classtype
    self.obj339.classtype.setValue('Vertex')

    # cardinality
    self.obj339.cardinality.setValue('+')

    self.obj339.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,40.0,self.obj339)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj339.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj339)
    self.globalAndLocalPostcondition(self.obj339, rootNode)
    self.obj339.postAction( rootNode.CREATE )

    self.obj340=Transition(self)
    self.obj340.isGraphObjectVisual = True

    if(hasattr(self.obj340, '_setHierarchicalLink')):
      self.obj340._setHierarchicalLink(False)

    # name
    self.obj340.name.setValue('transition1')

    # classtype
    self.obj340.classtype.setValue('Transition')

    # cardinality
    self.obj340.cardinality.setValue('+')

    self.obj340.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(460.0,40.0,self.obj340)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj340.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj340)
    self.globalAndLocalPostcondition(self.obj340, rootNode)
    self.obj340.postAction( rootNode.CREATE )

    self.obj341=State(self)
    self.obj341.isGraphObjectVisual = True

    if(hasattr(self.obj341, '_setHierarchicalLink')):
      self.obj341._setHierarchicalLink(False)

    # name
    self.obj341.name.setValue('state1')

    # classtype
    self.obj341.classtype.setValue('State')

    # cardinality
    self.obj341.cardinality.setValue('+')

    self.obj341.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,40.0,self.obj341)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj341.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj341)
    self.globalAndLocalPostcondition(self.obj341, rootNode)
    self.obj341.postAction( rootNode.CREATE )

    self.obj342=IN1(self)
    self.obj342.isGraphObjectVisual = True

    if(hasattr(self.obj342, '_setHierarchicalLink')):
      self.obj342._setHierarchicalLink(False)

    # classtype
    self.obj342.classtype.setValue('IN1')

    # cardinality
    self.obj342.cardinality.setValue('+')

    # name
    self.obj342.name.setValue('in1_1')

    self.obj342.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(460.0,140.0,self.obj342)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj342.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj342)
    self.globalAndLocalPostcondition(self.obj342, rootNode)
    self.obj342.postAction( rootNode.CREATE )

    self.obj343=Expr(self)
    self.obj343.isGraphObjectVisual = True

    if(hasattr(self.obj343, '_setHierarchicalLink')):
      self.obj343._setHierarchicalLink(False)

    # classtype
    self.obj343.classtype.setValue('Expr')

    # cardinality
    self.obj343.cardinality.setValue('1')

    # name
    self.obj343.name.setValue('expr1')

    self.obj343.graphClass_= graph_Expr
    if self.genGraphics:
       new_obj = graph_Expr(660.0,380.0,self.obj343)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj343.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj343)
    self.globalAndLocalPostcondition(self.obj343, rootNode)
    self.obj343.postAction( rootNode.CREATE )

    self.obj344=ConditionBranch(self)
    self.obj344.isGraphObjectVisual = True

    if(hasattr(self.obj344, '_setHierarchicalLink')):
      self.obj344._setHierarchicalLink(False)

    # classtype
    self.obj344.classtype.setValue('ConditionBranch')

    # cardinality
    self.obj344.cardinality.setValue('1')

    # name
    self.obj344.name.setValue('conditionbranch1')

    self.obj344.graphClass_= graph_ConditionBranch
    if self.genGraphics:
       new_obj = graph_ConditionBranch(460.0,380.0,self.obj344)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj344.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj344)
    self.globalAndLocalPostcondition(self.obj344, rootNode)
    self.obj344.postAction( rootNode.CREATE )

    self.obj345=Inst(self)
    self.obj345.isGraphObjectVisual = True

    if(hasattr(self.obj345, '_setHierarchicalLink')):
      self.obj345._setHierarchicalLink(False)

    # classtype
    self.obj345.classtype.setValue('Inst')

    # cardinality
    self.obj345.cardinality.setValue('1')

    # name
    self.obj345.name.setValue('inst1')

    self.obj345.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(840.0,480.0,self.obj345)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj345.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj345)
    self.globalAndLocalPostcondition(self.obj345, rootNode)
    self.obj345.postAction( rootNode.CREATE )

    self.obj346=ConditionSet(self)
    self.obj346.isGraphObjectVisual = True

    if(hasattr(self.obj346, '_setHierarchicalLink')):
      self.obj346._setHierarchicalLink(False)

    # classtype
    self.obj346.classtype.setValue('ConditionSet')

    # cardinality
    self.obj346.cardinality.setValue('1')

    # name
    self.obj346.name.setValue('conditionset1')

    self.obj346.graphClass_= graph_ConditionSet
    if self.genGraphics:
       new_obj = graph_ConditionSet(180.0,380.0,self.obj346)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionSet", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj346.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj346)
    self.globalAndLocalPostcondition(self.obj346, rootNode)
    self.obj346.postAction( rootNode.CREATE )

    self.obj347=Attribute(self)
    self.obj347.isGraphObjectVisual = True

    if(hasattr(self.obj347, '_setHierarchicalLink')):
      self.obj347._setHierarchicalLink(False)

    # Type
    self.obj347.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj347.Type.config = 0

    # name
    self.obj347.name.setValue('name')

    self.obj347.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,140.0,self.obj347)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj347.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj347)
    self.globalAndLocalPostcondition(self.obj347, rootNode)
    self.obj347.postAction( rootNode.CREATE )

    self.obj348=Attribute(self)
    self.obj348.isGraphObjectVisual = True

    if(hasattr(self.obj348, '_setHierarchicalLink')):
      self.obj348._setHierarchicalLink(False)

    # Type
    self.obj348.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj348.Type.config = 0

    # name
    self.obj348.name.setValue('isComposite')

    self.obj348.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,140.0,self.obj348)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj348.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj348)
    self.globalAndLocalPostcondition(self.obj348, rootNode)
    self.obj348.postAction( rootNode.CREATE )

    self.obj349=Attribute(self)
    self.obj349.isGraphObjectVisual = True

    if(hasattr(self.obj349, '_setHierarchicalLink')):
      self.obj349._setHierarchicalLink(False)

    # Type
    self.obj349.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj349.Type.config = 0

    # name
    self.obj349.name.setValue('literal')

    self.obj349.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,380.0,self.obj349)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj349.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj349)
    self.globalAndLocalPostcondition(self.obj349, rootNode)
    self.obj349.postAction( rootNode.CREATE )

    self.obj350=Attribute(self)
    self.obj350.isGraphObjectVisual = True

    if(hasattr(self.obj350, '_setHierarchicalLink')):
      self.obj350._setHierarchicalLink(False)

    # Type
    self.obj350.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj350.Type.config = 0

    # name
    self.obj350.name.setValue('pivot')

    self.obj350.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(900.0,580.0,self.obj350)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj350.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj350)
    self.globalAndLocalPostcondition(self.obj350, rootNode)
    self.obj350.postAction( rootNode.CREATE )

    self.obj351=Attribute(self)
    self.obj351.isGraphObjectVisual = True

    if(hasattr(self.obj351, '_setHierarchicalLink')):
      self.obj351._setHierarchicalLink(False)

    # Type
    self.obj351.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj351.Type.config = 0

    # name
    self.obj351.name.setValue('pivot')

    self.obj351.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(140.0,540.0,self.obj351)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj351.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj351)
    self.globalAndLocalPostcondition(self.obj351, rootNode)
    self.obj351.postAction( rootNode.CREATE )

    self.obj352=Equation(self)
    self.obj352.isGraphObjectVisual = True

    if(hasattr(self.obj352, '_setHierarchicalLink')):
      self.obj352._setHierarchicalLink(False)

    # name
    self.obj352.name.setValue('eq1')

    self.obj352.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,220.0,self.obj352)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj352.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj352)
    self.globalAndLocalPostcondition(self.obj352, rootNode)
    self.obj352.postAction( rootNode.CREATE )

    self.obj353=Equation(self)
    self.obj353.isGraphObjectVisual = True

    if(hasattr(self.obj353, '_setHierarchicalLink')):
      self.obj353._setHierarchicalLink(False)

    # name
    self.obj353.name.setValue('eq2')

    self.obj353.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(840.0,300.0,self.obj353)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj353.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj353)
    self.globalAndLocalPostcondition(self.obj353, rootNode)
    self.obj353.postAction( rootNode.CREATE )

    self.obj354=Equation(self)
    self.obj354.isGraphObjectVisual = True

    if(hasattr(self.obj354, '_setHierarchicalLink')):
      self.obj354._setHierarchicalLink(False)

    # name
    self.obj354.name.setValue('eq3')

    self.obj354.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,660.0,self.obj354)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj354.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj354)
    self.globalAndLocalPostcondition(self.obj354, rootNode)
    self.obj354.postAction( rootNode.CREATE )

    self.obj355=Equation(self)
    self.obj355.isGraphObjectVisual = True

    if(hasattr(self.obj355, '_setHierarchicalLink')):
      self.obj355._setHierarchicalLink(False)

    # name
    self.obj355.name.setValue('eq4')

    self.obj355.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,620.0,self.obj355)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj355.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj355)
    self.globalAndLocalPostcondition(self.obj355, rootNode)
    self.obj355.postAction( rootNode.CREATE )

    self.obj356=Concat(self)
    self.obj356.isGraphObjectVisual = True

    if(hasattr(self.obj356, '_setHierarchicalLink')):
      self.obj356._setHierarchicalLink(False)

    # Type
    self.obj356.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj356.Type.config = 0

    # name
    self.obj356.name.setValue('concat1')

    self.obj356.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(680.0,300.0,self.obj356)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj356.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj356)
    self.globalAndLocalPostcondition(self.obj356, rootNode)
    self.obj356.postAction( rootNode.CREATE )

    self.obj357=Constant(self)
    self.obj357.isGraphObjectVisual = True

    if(hasattr(self.obj357, '_setHierarchicalLink')):
      self.obj357._setHierarchicalLink(False)

    # Type
    self.obj357.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj357.Type.config = 0

    # name
    self.obj357.name.setValue('true')

    self.obj357.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(320.0,140.0,self.obj357)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj357.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj357)
    self.globalAndLocalPostcondition(self.obj357, rootNode)
    self.obj357.postAction( rootNode.CREATE )

    self.obj358=Constant(self)
    self.obj358.isGraphObjectVisual = True

    if(hasattr(self.obj358, '_setHierarchicalLink')):
      self.obj358._setHierarchicalLink(False)

    # Type
    self.obj358.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj358.Type.config = 0

    # name
    self.obj358.name.setValue('enp=1')

    self.obj358.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(520.0,300.0,self.obj358)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj358.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj358)
    self.globalAndLocalPostcondition(self.obj358, rootNode)
    self.obj358.postAction( rootNode.CREATE )

    self.obj359=Constant(self)
    self.obj359.isGraphObjectVisual = True

    if(hasattr(self.obj359, '_setHierarchicalLink')):
      self.obj359._setHierarchicalLink(False)

    # Type
    self.obj359.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj359.Type.config = 0

    # name
    self.obj359.name.setValue('2')

    self.obj359.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,220.0,self.obj359)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj359.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj359)
    self.globalAndLocalPostcondition(self.obj359, rootNode)
    self.obj359.postAction( rootNode.CREATE )

    self.obj360=Constant(self)
    self.obj360.isGraphObjectVisual = True

    if(hasattr(self.obj360, '_setHierarchicalLink')):
      self.obj360._setHierarchicalLink(False)

    # Type
    self.obj360.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj360.Type.config = 0

    # name
    self.obj360.name.setValue('instForInTrans')

    self.obj360.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(740.0,580.0,self.obj360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj360.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj360)
    self.globalAndLocalPostcondition(self.obj360, rootNode)
    self.obj360.postAction( rootNode.CREATE )

    self.obj361=Constant(self)
    self.obj361.isGraphObjectVisual = True

    if(hasattr(self.obj361, '_setHierarchicalLink')):
      self.obj361._setHierarchicalLink(False)

    # Type
    self.obj361.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj361.Type.config = 0

    # name
    self.obj361.name.setValue('condsetcompstate')

    self.obj361.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(300.0,540.0,self.obj361)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj361.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj361)
    self.globalAndLocalPostcondition(self.obj361, rootNode)
    self.obj361.postAction( rootNode.CREATE )

    self.obj362=paired_with(self)
    self.obj362.isGraphObjectVisual = True

    if(hasattr(self.obj362, '_setHierarchicalLink')):
      self.obj362._setHierarchicalLink(False)

    self.obj362.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj362)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj362.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj362)
    self.globalAndLocalPostcondition(self.obj362, rootNode)
    self.obj362.postAction( rootNode.CREATE )

    self.obj363=match_contains(self)
    self.obj363.isGraphObjectVisual = True

    if(hasattr(self.obj363, '_setHierarchicalLink')):
      self.obj363._setHierarchicalLink(False)

    self.obj363.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,67.0,self.obj363)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj363.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj363)
    self.globalAndLocalPostcondition(self.obj363, rootNode)
    self.obj363.postAction( rootNode.CREATE )

    self.obj364=match_contains(self)
    self.obj364.isGraphObjectVisual = True

    if(hasattr(self.obj364, '_setHierarchicalLink')):
      self.obj364._setHierarchicalLink(False)

    self.obj364.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,67.0,self.obj364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj364.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj364)
    self.globalAndLocalPostcondition(self.obj364, rootNode)
    self.obj364.postAction( rootNode.CREATE )

    self.obj365=match_contains(self)
    self.obj365.isGraphObjectVisual = True

    if(hasattr(self.obj365, '_setHierarchicalLink')):
      self.obj365._setHierarchicalLink(False)

    self.obj365.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,67.0,self.obj365)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj365.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj365)
    self.globalAndLocalPostcondition(self.obj365, rootNode)
    self.obj365.postAction( rootNode.CREATE )

    self.obj366=match_contains(self)
    self.obj366.isGraphObjectVisual = True

    if(hasattr(self.obj366, '_setHierarchicalLink')):
      self.obj366._setHierarchicalLink(False)

    self.obj366.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,117.0,self.obj366)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj366.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj366)
    self.globalAndLocalPostcondition(self.obj366, rootNode)
    self.obj366.postAction( rootNode.CREATE )

    self.obj367=apply_contains(self)
    self.obj367.isGraphObjectVisual = True

    if(hasattr(self.obj367, '_setHierarchicalLink')):
      self.obj367._setHierarchicalLink(False)

    self.obj367.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,392.0,self.obj367)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj367.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj367)
    self.globalAndLocalPostcondition(self.obj367, rootNode)
    self.obj367.postAction( rootNode.CREATE )

    self.obj368=apply_contains(self)
    self.obj368.isGraphObjectVisual = True

    if(hasattr(self.obj368, '_setHierarchicalLink')):
      self.obj368._setHierarchicalLink(False)

    self.obj368.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(387.5,392.0,self.obj368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj368.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj368)
    self.globalAndLocalPostcondition(self.obj368, rootNode)
    self.obj368.postAction( rootNode.CREATE )

    self.obj369=apply_contains(self)
    self.obj369.isGraphObjectVisual = True

    if(hasattr(self.obj369, '_setHierarchicalLink')):
      self.obj369._setHierarchicalLink(False)

    self.obj369.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,392.0,self.obj369)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj369.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj369)
    self.globalAndLocalPostcondition(self.obj369, rootNode)
    self.obj369.postAction( rootNode.CREATE )

    self.obj370=apply_contains(self)
    self.obj370.isGraphObjectVisual = True

    if(hasattr(self.obj370, '_setHierarchicalLink')):
      self.obj370._setHierarchicalLink(False)

    self.obj370.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(140.5,529.0,self.obj370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj370.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj370)
    self.globalAndLocalPostcondition(self.obj370, rootNode)
    self.obj370.postAction( rootNode.CREATE )

    self.obj371=directLink_T(self)
    self.obj371.isGraphObjectVisual = True

    if(hasattr(self.obj371, '_setHierarchicalLink')):
      self.obj371._setHierarchicalLink(False)

    # associationType
    self.obj371.associationType.setValue('branches')

    self.obj371.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(492.0,431.0,self.obj371)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj371.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj371)
    self.globalAndLocalPostcondition(self.obj371, rootNode)
    self.obj371.postAction( rootNode.CREATE )

    self.obj372=directLink_T(self)
    self.obj372.isGraphObjectVisual = True

    if(hasattr(self.obj372, '_setHierarchicalLink')):
      self.obj372._setHierarchicalLink(False)

    # associationType
    self.obj372.associationType.setValue('if')

    self.obj372.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(732.0,431.0,self.obj372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj372.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj372)
    self.globalAndLocalPostcondition(self.obj372, rootNode)
    self.obj372.postAction( rootNode.CREATE )

    self.obj373=directLink_T(self)
    self.obj373.isGraphObjectVisual = True

    if(hasattr(self.obj373, '_setHierarchicalLink')):
      self.obj373._setHierarchicalLink(False)

    # associationType
    self.obj373.associationType.setValue('then')

    self.obj373.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(651.0,513.0,self.obj373)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj373.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj373)
    self.globalAndLocalPostcondition(self.obj373, rootNode)
    self.obj373.postAction( rootNode.CREATE )

    self.obj374=directLink_S(self)
    self.obj374.isGraphObjectVisual = True

    if(hasattr(self.obj374, '_setHierarchicalLink')):
      self.obj374._setHierarchicalLink(False)

    # associationType
    self.obj374.associationType.setValue('transitions')

    self.obj374.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,83.0,self.obj374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj374.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj374)
    self.globalAndLocalPostcondition(self.obj374, rootNode)
    self.obj374.postAction( rootNode.CREATE )

    self.obj375=directLink_S(self)
    self.obj375.isGraphObjectVisual = True

    if(hasattr(self.obj375, '_setHierarchicalLink')):
      self.obj375._setHierarchicalLink(False)

    # associationType
    self.obj375.associationType.setValue('type')

    self.obj375.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(630.0,133.0,self.obj375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj375.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj375)
    self.globalAndLocalPostcondition(self.obj375, rootNode)
    self.obj375.postAction( rootNode.CREATE )

    self.obj376=directLink_S(self)
    self.obj376.isGraphObjectVisual = True

    if(hasattr(self.obj376, '_setHierarchicalLink')):
      self.obj376._setHierarchicalLink(False)

    # associationType
    self.obj376.associationType.setValue('src')

    self.obj376.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(730.0,83.0,self.obj376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj376.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj376)
    self.globalAndLocalPostcondition(self.obj376, rootNode)
    self.obj376.postAction( rootNode.CREATE )

    self.obj377=backward_link(self)
    self.obj377.isGraphObjectVisual = True

    if(hasattr(self.obj377, '_setHierarchicalLink')):
      self.obj377._setHierarchicalLink(False)

    # type
    self.obj377.type.setValue('ruleDef')

    self.obj377.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(821.0,307.0,self.obj377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj377.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj377)
    self.globalAndLocalPostcondition(self.obj377, rootNode)
    self.obj377.postAction( rootNode.CREATE )

    self.obj378=backward_link(self)
    self.obj378.isGraphObjectVisual = True

    if(hasattr(self.obj378, '_setHierarchicalLink')):
      self.obj378._setHierarchicalLink(False)

    # type
    self.obj378.type.setValue('ruleDef')

    self.obj378.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,257.0,self.obj378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj378.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj378)
    self.globalAndLocalPostcondition(self.obj378, rootNode)
    self.obj378.postAction( rootNode.CREATE )

    self.obj379=hasAttribute_S(self)
    self.obj379.isGraphObjectVisual = True

    if(hasattr(self.obj379, '_setHierarchicalLink')):
      self.obj379._setHierarchicalLink(False)

    self.obj379.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(812.0,128.5,self.obj379)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj379.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj379)
    self.globalAndLocalPostcondition(self.obj379, rootNode)
    self.obj379.postAction( rootNode.CREATE )

    self.obj380=hasAttribute_S(self)
    self.obj380.isGraphObjectVisual = True

    if(hasattr(self.obj380, '_setHierarchicalLink')):
      self.obj380._setHierarchicalLink(False)

    self.obj380.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,128.5,self.obj380)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj380.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj380)
    self.globalAndLocalPostcondition(self.obj380, rootNode)
    self.obj380.postAction( rootNode.CREATE )

    self.obj381=hasAttribute_T(self)
    self.obj381.isGraphObjectVisual = True

    if(hasattr(self.obj381, '_setHierarchicalLink')):
      self.obj381._setHierarchicalLink(False)

    self.obj381.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(903.0,422.5,self.obj381)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj381.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj381)
    self.globalAndLocalPostcondition(self.obj381, rootNode)
    self.obj381.postAction( rootNode.CREATE )

    self.obj382=hasAttribute_T(self)
    self.obj382.isGraphObjectVisual = True

    if(hasattr(self.obj382, '_setHierarchicalLink')):
      self.obj382._setHierarchicalLink(False)

    self.obj382.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1023.0,572.5,self.obj382)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj382.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj382)
    self.globalAndLocalPostcondition(self.obj382, rootNode)
    self.obj382.postAction( rootNode.CREATE )

    self.obj383=hasAttribute_T(self)
    self.obj383.isGraphObjectVisual = True

    if(hasattr(self.obj383, '_setHierarchicalLink')):
      self.obj383._setHierarchicalLink(False)

    self.obj383.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(313.0,502.5,self.obj383)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj383.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj383)
    self.globalAndLocalPostcondition(self.obj383, rootNode)
    self.obj383.postAction( rootNode.CREATE )

    self.obj384=leftExpr(self)
    self.obj384.isGraphObjectVisual = True

    if(hasattr(self.obj384, '_setHierarchicalLink')):
      self.obj384._setHierarchicalLink(False)

    self.obj384.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(336.0,216.5,self.obj384)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj384.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj384)
    self.globalAndLocalPostcondition(self.obj384, rootNode)
    self.obj384.postAction( rootNode.CREATE )

    self.obj385=leftExpr(self)
    self.obj385.isGraphObjectVisual = True

    if(hasattr(self.obj385, '_setHierarchicalLink')):
      self.obj385._setHierarchicalLink(False)

    self.obj385.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(976.0,376.5,self.obj385)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj385.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj385)
    self.globalAndLocalPostcondition(self.obj385, rootNode)
    self.obj385.postAction( rootNode.CREATE )

    self.obj386=leftExpr(self)
    self.obj386.isGraphObjectVisual = True

    if(hasattr(self.obj386, '_setHierarchicalLink')):
      self.obj386._setHierarchicalLink(False)

    self.obj386.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(996.0,656.5,self.obj386)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj386.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj386)
    self.globalAndLocalPostcondition(self.obj386, rootNode)
    self.obj386.postAction( rootNode.CREATE )

    self.obj387=leftExpr(self)
    self.obj387.isGraphObjectVisual = True

    if(hasattr(self.obj387, '_setHierarchicalLink')):
      self.obj387._setHierarchicalLink(False)

    self.obj387.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(326.0,616.5,self.obj387)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj387.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj387)
    self.globalAndLocalPostcondition(self.obj387, rootNode)
    self.obj387.postAction( rootNode.CREATE )

    self.obj388=rightExpr(self)
    self.obj388.isGraphObjectVisual = True

    if(hasattr(self.obj388, '_setHierarchicalLink')):
      self.obj388._setHierarchicalLink(False)

    self.obj388.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(416.0,216.5,self.obj388)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj388.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj388)
    self.globalAndLocalPostcondition(self.obj388, rootNode)
    self.obj388.postAction( rootNode.CREATE )

    self.obj389=rightExpr(self)
    self.obj389.isGraphObjectVisual = True

    if(hasattr(self.obj389, '_setHierarchicalLink')):
      self.obj389._setHierarchicalLink(False)

    self.obj389.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(896.0,336.5,self.obj389)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj389.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj389)
    self.globalAndLocalPostcondition(self.obj389, rootNode)
    self.obj389.postAction( rootNode.CREATE )

    self.obj390=rightExpr(self)
    self.obj390.isGraphObjectVisual = True

    if(hasattr(self.obj390, '_setHierarchicalLink')):
      self.obj390._setHierarchicalLink(False)

    self.obj390.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(916.0,656.5,self.obj390)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj390.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj390)
    self.globalAndLocalPostcondition(self.obj390, rootNode)
    self.obj390.postAction( rootNode.CREATE )

    self.obj391=rightExpr(self)
    self.obj391.isGraphObjectVisual = True

    if(hasattr(self.obj391, '_setHierarchicalLink')):
      self.obj391._setHierarchicalLink(False)

    self.obj391.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(406.0,616.5,self.obj391)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj391.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj391)
    self.globalAndLocalPostcondition(self.obj391, rootNode)
    self.obj391.postAction( rootNode.CREATE )

    self.obj392=hasArgs(self)
    self.obj392.isGraphObjectVisual = True

    if(hasattr(self.obj392, '_setHierarchicalLink')):
      self.obj392._setHierarchicalLink(False)

    self.obj392.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(734.0,334.0,self.obj392)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj392.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj392)
    self.globalAndLocalPostcondition(self.obj392, rootNode)
    self.obj392.postAction( rootNode.CREATE )

    self.obj393=hasArgs(self)
    self.obj393.isGraphObjectVisual = True

    if(hasattr(self.obj393, '_setHierarchicalLink')):
      self.obj393._setHierarchicalLink(False)

    self.obj393.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(771.0,274.0,self.obj393)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj393.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj393)
    self.globalAndLocalPostcondition(self.obj393, rootNode)
    self.obj393.postAction( rootNode.CREATE )

    self.obj394=hasArgs(self)
    self.obj394.isGraphObjectVisual = True

    if(hasattr(self.obj394, '_setHierarchicalLink')):
      self.obj394._setHierarchicalLink(False)

    self.obj394.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(894.0,294.0,self.obj394)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj394.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj394)
    self.globalAndLocalPostcondition(self.obj394, rootNode)
    self.obj394.postAction( rootNode.CREATE )

    # Connections for obj337 (graphObject_: Obj234) of type MatchModel
    self.drawConnections(
(self.obj337,self.obj362,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj337,self.obj363,[138.0, 51.0, 234.0, 67.0],"true", 2),
(self.obj337,self.obj364,[138.0, 51.0, 384.0, 67.0],"true", 2),
(self.obj337,self.obj365,[138.0, 51.0, 484.0, 67.0],"true", 2),
(self.obj337,self.obj366,[138.0, 51.0, 384.0, 117.0],"true", 2) )
    # Connections for obj338 (graphObject_: Obj235) of type ApplyModel
    self.drawConnections(
(self.obj338,self.obj367,[143.0, 353.0, 247.5, 392.0],"true", 2),
(self.obj338,self.obj368,[143.0, 353.0, 387.5, 392.0],"true", 2),
(self.obj338,self.obj369,[143.0, 353.0, 487.5, 392.0],"true", 2),
(self.obj338,self.obj370,[143.0, 353.0, 140.5, 529.0],"true", 2) )
    # Connections for obj339 (graphObject_: Obj236) named vertex1
    self.drawConnections(
(self.obj339,self.obj379,[830.0, 83.0, 812.0, 128.5],"true", 2) )
    # Connections for obj340 (graphObject_: Obj237) named transition1
    self.drawConnections(
(self.obj340,self.obj375,[630.0, 83.0, 630.0, 133.0],"true", 2),
(self.obj340,self.obj376,[630.0, 83.0, 730.0, 83.0],"true", 2) )
    # Connections for obj341 (graphObject_: Obj238) named state1
    self.drawConnections(
(self.obj341,self.obj374,[330.0, 83.0, 480.0, 83.0],"true", 2),
(self.obj341,self.obj380,[330.0, 83.0, 312.0, 128.5],"true", 2) )
    # Connections for obj342 (graphObject_: Obj239) named in1_1
    self.drawConnections(
 )
    # Connections for obj343 (graphObject_: Obj240) named expr1
    self.drawConnections(
(self.obj343,self.obj381,[832.0, 431.0, 903.0, 422.5],"true", 2) )
    # Connections for obj344 (graphObject_: Obj241) named conditionbranch1
    self.drawConnections(
(self.obj344,self.obj372,[632.0, 431.0, 732.0, 431.0],"true", 2),
(self.obj344,self.obj373,[632.0, 431.0, 651.0, 513.0],"true", 2) )
    # Connections for obj345 (graphObject_: Obj242) named inst1
    self.drawConnections(
(self.obj345,self.obj377,[1012.0, 531.0, 821.0, 307.0],"true", 2),
(self.obj345,self.obj382,[1012.0, 531.0, 1023.0, 572.5],"true", 2) )
    # Connections for obj346 (graphObject_: Obj243) named conditionset1
    self.drawConnections(
(self.obj346,self.obj371,[352.0, 431.0, 492.0, 431.0],"true", 2),
(self.obj346,self.obj378,[352.0, 431.0, 341.0, 257.0],"true", 2),
(self.obj346,self.obj383,[352.0, 431.0, 313.0, 502.5],"true", 2) )
    # Connections for obj347 (graphObject_: Obj244) named name
    self.drawConnections(
 )
    # Connections for obj348 (graphObject_: Obj245) named isComposite
    self.drawConnections(
 )
    # Connections for obj349 (graphObject_: Obj246) named literal
    self.drawConnections(
 )
    # Connections for obj350 (graphObject_: Obj247) named pivot
    self.drawConnections(
 )
    # Connections for obj351 (graphObject_: Obj248) named pivot
    self.drawConnections(
 )
    # Connections for obj352 (graphObject_: Obj249) named eq1
    self.drawConnections(
(self.obj352,self.obj384,[378.0, 259.0, 336.0, 216.5],"true", 2),
(self.obj352,self.obj388,[378.0, 259.0, 416.0, 216.5],"true", 2) )
    # Connections for obj353 (graphObject_: Obj250) named eq2
    self.drawConnections(
(self.obj353,self.obj385,[978.0, 339.0, 976.0, 376.5],"true", 2),
(self.obj353,self.obj389,[978.0, 339.0, 896.0, 336.5],"true", 2) )
    # Connections for obj354 (graphObject_: Obj251) named eq3
    self.drawConnections(
(self.obj354,self.obj386,[958.0, 699.0, 996.0, 656.5],"true", 2),
(self.obj354,self.obj390,[958.0, 699.0, 916.0, 656.5],"true", 2) )
    # Connections for obj355 (graphObject_: Obj252) named eq4
    self.drawConnections(
(self.obj355,self.obj387,[378.0, 659.0, 326.0, 616.5],"true", 2),
(self.obj355,self.obj391,[378.0, 659.0, 406.0, 616.5],"true", 2) )
    # Connections for obj356 (graphObject_: Obj253) named concat1
    self.drawConnections(
(self.obj356,self.obj392,[814.0, 334.0, 734.0, 334.0],"true", 2),
(self.obj356,self.obj393,[814.0, 334.0, 771.0, 274.0],"true", 2),
(self.obj356,self.obj394,[814.0, 334.0, 894.0, 294.0],"true", 2) )
    # Connections for obj357 (graphObject_: Obj254) named true
    self.drawConnections(
 )
    # Connections for obj358 (graphObject_: Obj255) named enp=1
    self.drawConnections(
 )
    # Connections for obj359 (graphObject_: Obj256) named 2
    self.drawConnections(
 )
    # Connections for obj360 (graphObject_: Obj257) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj361 (graphObject_: Obj258) named condsetcompstate
    self.drawConnections(
 )
    # Connections for obj362 (graphObject_: Obj259) of type paired_with
    self.drawConnections(
(self.obj362,self.obj338,[140.5, 152.0, 143.0, 353.0],"true", 2) )
    # Connections for obj363 (graphObject_: Obj260) of type match_contains
    self.drawConnections(
(self.obj363,self.obj341,[234.0, 67.0, 330.0, 83.0],"true", 2) )
    # Connections for obj364 (graphObject_: Obj261) of type match_contains
    self.drawConnections(
(self.obj364,self.obj340,[384.0, 67.0, 630.0, 83.0],"true", 2) )
    # Connections for obj365 (graphObject_: Obj262) of type match_contains
    self.drawConnections(
(self.obj365,self.obj339,[484.0, 67.0, 830.0, 83.0],"true", 2) )
    # Connections for obj366 (graphObject_: Obj263) of type match_contains
    self.drawConnections(
(self.obj366,self.obj342,[384.0, 117.0, 630.0, 183.0],"true", 2) )
    # Connections for obj367 (graphObject_: Obj264) of type apply_contains
    self.drawConnections(
(self.obj367,self.obj346,[247.5, 392.0, 352.0, 431.0],"true", 2) )
    # Connections for obj368 (graphObject_: Obj265) of type apply_contains
    self.drawConnections(
(self.obj368,self.obj344,[387.5, 392.0, 632.0, 431.0],"true", 2) )
    # Connections for obj369 (graphObject_: Obj266) of type apply_contains
    self.drawConnections(
(self.obj369,self.obj343,[487.5, 392.0, 832.0, 431.0],"true", 2) )
    # Connections for obj370 (graphObject_: Obj267) of type apply_contains
    self.drawConnections(
(self.obj370,self.obj345,[140.5, 529.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj371 (graphObject_: Obj268) of type directLink_T
    self.drawConnections(
(self.obj371,self.obj344,[492.0, 431.0, 632.0, 431.0],"true", 2) )
    # Connections for obj372 (graphObject_: Obj269) of type directLink_T
    self.drawConnections(
(self.obj372,self.obj343,[732.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj373 (graphObject_: Obj270) of type directLink_T
    self.drawConnections(
(self.obj373,self.obj345,[651.0, 513.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj374 (graphObject_: Obj271) of type directLink_S
    self.drawConnections(
(self.obj374,self.obj340,[480.0, 83.0, 630.0, 83.0],"true", 2) )
    # Connections for obj375 (graphObject_: Obj272) of type directLink_S
    self.drawConnections(
(self.obj375,self.obj342,[630.0, 133.0, 630.0, 183.0],"true", 2) )
    # Connections for obj376 (graphObject_: Obj273) of type directLink_S
    self.drawConnections(
(self.obj376,self.obj339,[730.0, 83.0, 830.0, 83.0],"true", 2) )
    # Connections for obj377 (graphObject_: Obj274) of type backward_link
    self.drawConnections(
(self.obj377,self.obj340,[821.0, 307.0, 630.0, 83.0],"true", 2) )
    # Connections for obj378 (graphObject_: Obj275) of type backward_link
    self.drawConnections(
(self.obj378,self.obj341,[341.0, 257.0, 330.0, 83.0],"true", 2) )
    # Connections for obj379 (graphObject_: Obj276) of type hasAttribute_S
    self.drawConnections(
(self.obj379,self.obj347,[812.0, 128.5, 774.0, 174.0],"true", 2) )
    # Connections for obj380 (graphObject_: Obj277) of type hasAttribute_S
    self.drawConnections(
(self.obj380,self.obj348,[312.0, 128.5, 294.0, 174.0],"true", 2) )
    # Connections for obj381 (graphObject_: Obj278) of type hasAttribute_T
    self.drawConnections(
(self.obj381,self.obj349,[903.0, 422.5, 974.0, 414.0],"true", 2) )
    # Connections for obj382 (graphObject_: Obj279) of type hasAttribute_T
    self.drawConnections(
(self.obj382,self.obj350,[1023.0, 572.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj383 (graphObject_: Obj280) of type hasAttribute_T
    self.drawConnections(
(self.obj383,self.obj351,[313.0, 502.5, 274.0, 574.0],"true", 2) )
    # Connections for obj384 (graphObject_: Obj281) of type leftExpr
    self.drawConnections(
(self.obj384,self.obj348,[336.0, 216.5, 294.0, 174.0],"true", 2) )
    # Connections for obj385 (graphObject_: Obj282) of type leftExpr
    self.drawConnections(
(self.obj385,self.obj349,[976.0, 376.5, 974.0, 414.0],"true", 2) )
    # Connections for obj386 (graphObject_: Obj283) of type leftExpr
    self.drawConnections(
(self.obj386,self.obj350,[996.0, 656.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj387 (graphObject_: Obj284) of type leftExpr
    self.drawConnections(
(self.obj387,self.obj351,[326.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj388 (graphObject_: Obj285) of type rightExpr
    self.drawConnections(
(self.obj388,self.obj357,[416.0, 216.5, 454.0, 174.0],"true", 2) )
    # Connections for obj389 (graphObject_: Obj286) of type rightExpr
    self.drawConnections(
(self.obj389,self.obj356,[896.0, 336.5, 814.0, 334.0],"true", 2) )
    # Connections for obj390 (graphObject_: Obj287) of type rightExpr
    self.drawConnections(
(self.obj390,self.obj360,[916.0, 656.5, 874.0, 614.0],"true", 2) )
    # Connections for obj391 (graphObject_: Obj288) of type rightExpr
    self.drawConnections(
(self.obj391,self.obj361,[406.0, 616.5, 434.0, 574.0],"true", 2) )
    # Connections for obj392 (graphObject_: Obj289) of type hasArgs
    self.drawConnections(
(self.obj392,self.obj358,[734.0, 334.0, 654.0, 334.0],"true", 2) )
    # Connections for obj393 (graphObject_: Obj290) of type hasArgs
    self.drawConnections(
(self.obj393,self.obj347,[771.0, 274.0, 774.0, 174.0],"true", 2) )
    # Connections for obj394 (graphObject_: Obj291) of type hasArgs
    self.drawConnections(
(self.obj394,self.obj359,[894.0, 294.0, 934.0, 254.0],"true", 2) )

newfunction = ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
