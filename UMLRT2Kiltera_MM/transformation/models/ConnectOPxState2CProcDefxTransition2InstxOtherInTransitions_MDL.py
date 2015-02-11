"""
__ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 13:55:18 2015
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


    self.obj359=MatchModel(self)
    self.obj359.isGraphObjectVisual = True

    if(hasattr(self.obj359, '_setHierarchicalLink')):
      self.obj359._setHierarchicalLink(False)

    self.obj359.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj359)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj359.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj359)
    self.globalAndLocalPostcondition(self.obj359, rootNode)
    self.obj359.postAction( rootNode.CREATE )

    self.obj360=ApplyModel(self)
    self.obj360.isGraphObjectVisual = True

    if(hasattr(self.obj360, '_setHierarchicalLink')):
      self.obj360._setHierarchicalLink(False)

    self.obj360.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,320.0,self.obj360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj360.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj360)
    self.globalAndLocalPostcondition(self.obj360, rootNode)
    self.obj360.postAction( rootNode.CREATE )

    self.obj361=Vertex(self)
    self.obj361.isGraphObjectVisual = True

    if(hasattr(self.obj361, '_setHierarchicalLink')):
      self.obj361._setHierarchicalLink(False)

    # name
    self.obj361.name.setValue('vertex1')

    # classtype
    self.obj361.classtype.setValue('Vertex')

    # cardinality
    self.obj361.cardinality.setValue('+')

    self.obj361.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,40.0,self.obj361)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj361.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj361)
    self.globalAndLocalPostcondition(self.obj361, rootNode)
    self.obj361.postAction( rootNode.CREATE )

    self.obj362=Transition(self)
    self.obj362.isGraphObjectVisual = True

    if(hasattr(self.obj362, '_setHierarchicalLink')):
      self.obj362._setHierarchicalLink(False)

    # name
    self.obj362.name.setValue('transition1')

    # classtype
    self.obj362.classtype.setValue('Transition')

    # cardinality
    self.obj362.cardinality.setValue('+')

    self.obj362.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(460.0,40.0,self.obj362)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj362.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj362)
    self.globalAndLocalPostcondition(self.obj362, rootNode)
    self.obj362.postAction( rootNode.CREATE )

    self.obj363=State(self)
    self.obj363.isGraphObjectVisual = True

    if(hasattr(self.obj363, '_setHierarchicalLink')):
      self.obj363._setHierarchicalLink(False)

    # name
    self.obj363.name.setValue('state1')

    # classtype
    self.obj363.classtype.setValue('State')

    # cardinality
    self.obj363.cardinality.setValue('+')

    self.obj363.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,40.0,self.obj363)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj363.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj363)
    self.globalAndLocalPostcondition(self.obj363, rootNode)
    self.obj363.postAction( rootNode.CREATE )

    self.obj364=IN1(self)
    self.obj364.isGraphObjectVisual = True

    if(hasattr(self.obj364, '_setHierarchicalLink')):
      self.obj364._setHierarchicalLink(False)

    # classtype
    self.obj364.classtype.setValue('IN1')

    # cardinality
    self.obj364.cardinality.setValue('+')

    # name
    self.obj364.name.setValue('in1_1')

    self.obj364.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(460.0,140.0,self.obj364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj364.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj364)
    self.globalAndLocalPostcondition(self.obj364, rootNode)
    self.obj364.postAction( rootNode.CREATE )

    self.obj365=Expr(self)
    self.obj365.isGraphObjectVisual = True

    if(hasattr(self.obj365, '_setHierarchicalLink')):
      self.obj365._setHierarchicalLink(False)

    # classtype
    self.obj365.classtype.setValue('Expr')

    # cardinality
    self.obj365.cardinality.setValue('1')

    # name
    self.obj365.name.setValue('expr1')

    self.obj365.graphClass_= graph_Expr
    if self.genGraphics:
       new_obj = graph_Expr(660.0,380.0,self.obj365)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj365.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj365)
    self.globalAndLocalPostcondition(self.obj365, rootNode)
    self.obj365.postAction( rootNode.CREATE )

    self.obj366=ConditionBranch(self)
    self.obj366.isGraphObjectVisual = True

    if(hasattr(self.obj366, '_setHierarchicalLink')):
      self.obj366._setHierarchicalLink(False)

    # classtype
    self.obj366.classtype.setValue('ConditionBranch')

    # cardinality
    self.obj366.cardinality.setValue('1')

    # name
    self.obj366.name.setValue('conditionbranch1')

    self.obj366.graphClass_= graph_ConditionBranch
    if self.genGraphics:
       new_obj = graph_ConditionBranch(460.0,380.0,self.obj366)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj366.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj366)
    self.globalAndLocalPostcondition(self.obj366, rootNode)
    self.obj366.postAction( rootNode.CREATE )

    self.obj367=Inst(self)
    self.obj367.isGraphObjectVisual = True

    if(hasattr(self.obj367, '_setHierarchicalLink')):
      self.obj367._setHierarchicalLink(False)

    # classtype
    self.obj367.classtype.setValue('Inst')

    # cardinality
    self.obj367.cardinality.setValue('1')

    # name
    self.obj367.name.setValue('inst1')

    self.obj367.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(840.0,480.0,self.obj367)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj367.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj367)
    self.globalAndLocalPostcondition(self.obj367, rootNode)
    self.obj367.postAction( rootNode.CREATE )

    self.obj368=ConditionSet(self)
    self.obj368.isGraphObjectVisual = True

    if(hasattr(self.obj368, '_setHierarchicalLink')):
      self.obj368._setHierarchicalLink(False)

    # classtype
    self.obj368.classtype.setValue('ConditionSet')

    # cardinality
    self.obj368.cardinality.setValue('1')

    # name
    self.obj368.name.setValue('conditionset1')

    self.obj368.graphClass_= graph_ConditionSet
    if self.genGraphics:
       new_obj = graph_ConditionSet(180.0,380.0,self.obj368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionSet", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj368.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj368)
    self.globalAndLocalPostcondition(self.obj368, rootNode)
    self.obj368.postAction( rootNode.CREATE )

    self.obj369=Attribute(self)
    self.obj369.isGraphObjectVisual = True

    if(hasattr(self.obj369, '_setHierarchicalLink')):
      self.obj369._setHierarchicalLink(False)

    # Type
    self.obj369.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj369.Type.config = 0

    # name
    self.obj369.name.setValue('name')

    self.obj369.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,140.0,self.obj369)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj369.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj369)
    self.globalAndLocalPostcondition(self.obj369, rootNode)
    self.obj369.postAction( rootNode.CREATE )

    self.obj370=Attribute(self)
    self.obj370.isGraphObjectVisual = True

    if(hasattr(self.obj370, '_setHierarchicalLink')):
      self.obj370._setHierarchicalLink(False)

    # Type
    self.obj370.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj370.Type.config = 0

    # name
    self.obj370.name.setValue('isComposite')

    self.obj370.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,140.0,self.obj370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj370.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj370)
    self.globalAndLocalPostcondition(self.obj370, rootNode)
    self.obj370.postAction( rootNode.CREATE )

    self.obj371=Attribute(self)
    self.obj371.isGraphObjectVisual = True

    if(hasattr(self.obj371, '_setHierarchicalLink')):
      self.obj371._setHierarchicalLink(False)

    # Type
    self.obj371.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj371.Type.config = 0

    # name
    self.obj371.name.setValue('literal')

    self.obj371.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,380.0,self.obj371)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj371.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj371)
    self.globalAndLocalPostcondition(self.obj371, rootNode)
    self.obj371.postAction( rootNode.CREATE )

    self.obj372=Attribute(self)
    self.obj372.isGraphObjectVisual = True

    if(hasattr(self.obj372, '_setHierarchicalLink')):
      self.obj372._setHierarchicalLink(False)

    # Type
    self.obj372.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj372.Type.config = 0

    # name
    self.obj372.name.setValue('pivot')

    self.obj372.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(900.0,580.0,self.obj372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj372.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj372)
    self.globalAndLocalPostcondition(self.obj372, rootNode)
    self.obj372.postAction( rootNode.CREATE )

    self.obj373=Attribute(self)
    self.obj373.isGraphObjectVisual = True

    if(hasattr(self.obj373, '_setHierarchicalLink')):
      self.obj373._setHierarchicalLink(False)

    # Type
    self.obj373.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj373.Type.config = 0

    # name
    self.obj373.name.setValue('pivot')

    self.obj373.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(140.0,540.0,self.obj373)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj373.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj373)
    self.globalAndLocalPostcondition(self.obj373, rootNode)
    self.obj373.postAction( rootNode.CREATE )

    self.obj374=Equation(self)
    self.obj374.isGraphObjectVisual = True

    if(hasattr(self.obj374, '_setHierarchicalLink')):
      self.obj374._setHierarchicalLink(False)

    # name
    self.obj374.name.setValue('eq1')

    self.obj374.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,220.0,self.obj374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj374.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj374)
    self.globalAndLocalPostcondition(self.obj374, rootNode)
    self.obj374.postAction( rootNode.CREATE )

    self.obj375=Equation(self)
    self.obj375.isGraphObjectVisual = True

    if(hasattr(self.obj375, '_setHierarchicalLink')):
      self.obj375._setHierarchicalLink(False)

    # name
    self.obj375.name.setValue('eq2')

    self.obj375.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(840.0,300.0,self.obj375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj375.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj375)
    self.globalAndLocalPostcondition(self.obj375, rootNode)
    self.obj375.postAction( rootNode.CREATE )

    self.obj376=Equation(self)
    self.obj376.isGraphObjectVisual = True

    if(hasattr(self.obj376, '_setHierarchicalLink')):
      self.obj376._setHierarchicalLink(False)

    # name
    self.obj376.name.setValue('eq3')

    self.obj376.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,660.0,self.obj376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj376.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj376)
    self.globalAndLocalPostcondition(self.obj376, rootNode)
    self.obj376.postAction( rootNode.CREATE )

    self.obj377=Equation(self)
    self.obj377.isGraphObjectVisual = True

    if(hasattr(self.obj377, '_setHierarchicalLink')):
      self.obj377._setHierarchicalLink(False)

    # name
    self.obj377.name.setValue('eq4')

    self.obj377.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,620.0,self.obj377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj377.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj377)
    self.globalAndLocalPostcondition(self.obj377, rootNode)
    self.obj377.postAction( rootNode.CREATE )

    self.obj378=Concat(self)
    self.obj378.isGraphObjectVisual = True

    if(hasattr(self.obj378, '_setHierarchicalLink')):
      self.obj378._setHierarchicalLink(False)

    # Type
    self.obj378.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj378.Type.config = 0

    # name
    self.obj378.name.setValue('concat1')

    self.obj378.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(680.0,300.0,self.obj378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj378.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj378)
    self.globalAndLocalPostcondition(self.obj378, rootNode)
    self.obj378.postAction( rootNode.CREATE )

    self.obj379=Constant(self)
    self.obj379.isGraphObjectVisual = True

    if(hasattr(self.obj379, '_setHierarchicalLink')):
      self.obj379._setHierarchicalLink(False)

    # Type
    self.obj379.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj379.Type.config = 0

    # name
    self.obj379.name.setValue('true')

    self.obj379.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(320.0,140.0,self.obj379)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj379.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj379)
    self.globalAndLocalPostcondition(self.obj379, rootNode)
    self.obj379.postAction( rootNode.CREATE )

    self.obj380=Constant(self)
    self.obj380.isGraphObjectVisual = True

    if(hasattr(self.obj380, '_setHierarchicalLink')):
      self.obj380._setHierarchicalLink(False)

    # Type
    self.obj380.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj380.Type.config = 0

    # name
    self.obj380.name.setValue('enp=1')

    self.obj380.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(520.0,300.0,self.obj380)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj380.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj380)
    self.globalAndLocalPostcondition(self.obj380, rootNode)
    self.obj380.postAction( rootNode.CREATE )

    self.obj381=Constant(self)
    self.obj381.isGraphObjectVisual = True

    if(hasattr(self.obj381, '_setHierarchicalLink')):
      self.obj381._setHierarchicalLink(False)

    # Type
    self.obj381.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj381.Type.config = 0

    # name
    self.obj381.name.setValue('2')

    self.obj381.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,220.0,self.obj381)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj381.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj381)
    self.globalAndLocalPostcondition(self.obj381, rootNode)
    self.obj381.postAction( rootNode.CREATE )

    self.obj382=Constant(self)
    self.obj382.isGraphObjectVisual = True

    if(hasattr(self.obj382, '_setHierarchicalLink')):
      self.obj382._setHierarchicalLink(False)

    # Type
    self.obj382.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj382.Type.config = 0

    # name
    self.obj382.name.setValue('instForInTrans')

    self.obj382.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(740.0,580.0,self.obj382)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj382.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj382)
    self.globalAndLocalPostcondition(self.obj382, rootNode)
    self.obj382.postAction( rootNode.CREATE )

    self.obj383=Constant(self)
    self.obj383.isGraphObjectVisual = True

    if(hasattr(self.obj383, '_setHierarchicalLink')):
      self.obj383._setHierarchicalLink(False)

    # Type
    self.obj383.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj383.Type.config = 0

    # name
    self.obj383.name.setValue('condsetcompstate')

    self.obj383.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(300.0,540.0,self.obj383)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj383.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj383)
    self.globalAndLocalPostcondition(self.obj383, rootNode)
    self.obj383.postAction( rootNode.CREATE )

    self.obj384=paired_with(self)
    self.obj384.isGraphObjectVisual = True

    if(hasattr(self.obj384, '_setHierarchicalLink')):
      self.obj384._setHierarchicalLink(False)

    self.obj384.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj384)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj384.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj384)
    self.globalAndLocalPostcondition(self.obj384, rootNode)
    self.obj384.postAction( rootNode.CREATE )

    self.obj385=match_contains(self)
    self.obj385.isGraphObjectVisual = True

    if(hasattr(self.obj385, '_setHierarchicalLink')):
      self.obj385._setHierarchicalLink(False)

    self.obj385.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,67.0,self.obj385)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj385.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj385)
    self.globalAndLocalPostcondition(self.obj385, rootNode)
    self.obj385.postAction( rootNode.CREATE )

    self.obj386=match_contains(self)
    self.obj386.isGraphObjectVisual = True

    if(hasattr(self.obj386, '_setHierarchicalLink')):
      self.obj386._setHierarchicalLink(False)

    self.obj386.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,67.0,self.obj386)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj386.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj386)
    self.globalAndLocalPostcondition(self.obj386, rootNode)
    self.obj386.postAction( rootNode.CREATE )

    self.obj387=match_contains(self)
    self.obj387.isGraphObjectVisual = True

    if(hasattr(self.obj387, '_setHierarchicalLink')):
      self.obj387._setHierarchicalLink(False)

    self.obj387.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,67.0,self.obj387)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj387.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj387)
    self.globalAndLocalPostcondition(self.obj387, rootNode)
    self.obj387.postAction( rootNode.CREATE )

    self.obj388=match_contains(self)
    self.obj388.isGraphObjectVisual = True

    if(hasattr(self.obj388, '_setHierarchicalLink')):
      self.obj388._setHierarchicalLink(False)

    self.obj388.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,117.0,self.obj388)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj388.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj388)
    self.globalAndLocalPostcondition(self.obj388, rootNode)
    self.obj388.postAction( rootNode.CREATE )

    self.obj389=apply_contains(self)
    self.obj389.isGraphObjectVisual = True

    if(hasattr(self.obj389, '_setHierarchicalLink')):
      self.obj389._setHierarchicalLink(False)

    self.obj389.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,392.0,self.obj389)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj389.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj389)
    self.globalAndLocalPostcondition(self.obj389, rootNode)
    self.obj389.postAction( rootNode.CREATE )

    self.obj390=apply_contains(self)
    self.obj390.isGraphObjectVisual = True

    if(hasattr(self.obj390, '_setHierarchicalLink')):
      self.obj390._setHierarchicalLink(False)

    self.obj390.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(387.5,392.0,self.obj390)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj390.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj390)
    self.globalAndLocalPostcondition(self.obj390, rootNode)
    self.obj390.postAction( rootNode.CREATE )

    self.obj391=apply_contains(self)
    self.obj391.isGraphObjectVisual = True

    if(hasattr(self.obj391, '_setHierarchicalLink')):
      self.obj391._setHierarchicalLink(False)

    self.obj391.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,392.0,self.obj391)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj391.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj391)
    self.globalAndLocalPostcondition(self.obj391, rootNode)
    self.obj391.postAction( rootNode.CREATE )

    self.obj392=apply_contains(self)
    self.obj392.isGraphObjectVisual = True

    if(hasattr(self.obj392, '_setHierarchicalLink')):
      self.obj392._setHierarchicalLink(False)

    self.obj392.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(140.5,529.0,self.obj392)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj392.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj392)
    self.globalAndLocalPostcondition(self.obj392, rootNode)
    self.obj392.postAction( rootNode.CREATE )

    self.obj393=directLink_T(self)
    self.obj393.isGraphObjectVisual = True

    if(hasattr(self.obj393, '_setHierarchicalLink')):
      self.obj393._setHierarchicalLink(False)

    # associationType
    self.obj393.associationType.setValue('branches')

    self.obj393.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(492.0,431.0,self.obj393)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj393.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj393)
    self.globalAndLocalPostcondition(self.obj393, rootNode)
    self.obj393.postAction( rootNode.CREATE )

    self.obj394=directLink_T(self)
    self.obj394.isGraphObjectVisual = True

    if(hasattr(self.obj394, '_setHierarchicalLink')):
      self.obj394._setHierarchicalLink(False)

    # associationType
    self.obj394.associationType.setValue('if')

    self.obj394.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(732.0,431.0,self.obj394)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj394.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj394)
    self.globalAndLocalPostcondition(self.obj394, rootNode)
    self.obj394.postAction( rootNode.CREATE )

    self.obj395=directLink_T(self)
    self.obj395.isGraphObjectVisual = True

    if(hasattr(self.obj395, '_setHierarchicalLink')):
      self.obj395._setHierarchicalLink(False)

    # associationType
    self.obj395.associationType.setValue('then')

    self.obj395.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(651.0,513.0,self.obj395)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj395.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj395)
    self.globalAndLocalPostcondition(self.obj395, rootNode)
    self.obj395.postAction( rootNode.CREATE )

    self.obj396=directLink_S(self)
    self.obj396.isGraphObjectVisual = True

    if(hasattr(self.obj396, '_setHierarchicalLink')):
      self.obj396._setHierarchicalLink(False)

    # associationType
    self.obj396.associationType.setValue('transitions')

    self.obj396.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,83.0,self.obj396)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj396.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj396)
    self.globalAndLocalPostcondition(self.obj396, rootNode)
    self.obj396.postAction( rootNode.CREATE )

    self.obj397=directLink_S(self)
    self.obj397.isGraphObjectVisual = True

    if(hasattr(self.obj397, '_setHierarchicalLink')):
      self.obj397._setHierarchicalLink(False)

    # associationType
    self.obj397.associationType.setValue('type')

    self.obj397.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(630.0,133.0,self.obj397)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj397.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj397)
    self.globalAndLocalPostcondition(self.obj397, rootNode)
    self.obj397.postAction( rootNode.CREATE )

    self.obj398=directLink_S(self)
    self.obj398.isGraphObjectVisual = True

    if(hasattr(self.obj398, '_setHierarchicalLink')):
      self.obj398._setHierarchicalLink(False)

    # associationType
    self.obj398.associationType.setValue('src')

    self.obj398.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(730.0,83.0,self.obj398)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj398.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj398)
    self.globalAndLocalPostcondition(self.obj398, rootNode)
    self.obj398.postAction( rootNode.CREATE )

    self.obj399=backward_link(self)
    self.obj399.isGraphObjectVisual = True

    if(hasattr(self.obj399, '_setHierarchicalLink')):
      self.obj399._setHierarchicalLink(False)

    # type
    self.obj399.type.setValue('ruleDef')

    self.obj399.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(821.0,307.0,self.obj399)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj399.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj399)
    self.globalAndLocalPostcondition(self.obj399, rootNode)
    self.obj399.postAction( rootNode.CREATE )

    self.obj400=backward_link(self)
    self.obj400.isGraphObjectVisual = True

    if(hasattr(self.obj400, '_setHierarchicalLink')):
      self.obj400._setHierarchicalLink(False)

    # type
    self.obj400.type.setValue('ruleDef')

    self.obj400.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,257.0,self.obj400)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj400.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj400)
    self.globalAndLocalPostcondition(self.obj400, rootNode)
    self.obj400.postAction( rootNode.CREATE )

    self.obj401=hasAttribute_S(self)
    self.obj401.isGraphObjectVisual = True

    if(hasattr(self.obj401, '_setHierarchicalLink')):
      self.obj401._setHierarchicalLink(False)

    self.obj401.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(812.0,128.5,self.obj401)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj401.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj401)
    self.globalAndLocalPostcondition(self.obj401, rootNode)
    self.obj401.postAction( rootNode.CREATE )

    self.obj402=hasAttribute_S(self)
    self.obj402.isGraphObjectVisual = True

    if(hasattr(self.obj402, '_setHierarchicalLink')):
      self.obj402._setHierarchicalLink(False)

    self.obj402.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,128.5,self.obj402)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj402.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj402)
    self.globalAndLocalPostcondition(self.obj402, rootNode)
    self.obj402.postAction( rootNode.CREATE )

    self.obj403=hasAttribute_T(self)
    self.obj403.isGraphObjectVisual = True

    if(hasattr(self.obj403, '_setHierarchicalLink')):
      self.obj403._setHierarchicalLink(False)

    self.obj403.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(903.0,422.5,self.obj403)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj403.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj403)
    self.globalAndLocalPostcondition(self.obj403, rootNode)
    self.obj403.postAction( rootNode.CREATE )

    self.obj404=hasAttribute_T(self)
    self.obj404.isGraphObjectVisual = True

    if(hasattr(self.obj404, '_setHierarchicalLink')):
      self.obj404._setHierarchicalLink(False)

    self.obj404.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1023.0,572.5,self.obj404)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj404.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj404)
    self.globalAndLocalPostcondition(self.obj404, rootNode)
    self.obj404.postAction( rootNode.CREATE )

    self.obj405=hasAttribute_T(self)
    self.obj405.isGraphObjectVisual = True

    if(hasattr(self.obj405, '_setHierarchicalLink')):
      self.obj405._setHierarchicalLink(False)

    self.obj405.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(313.0,502.5,self.obj405)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj405.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj405)
    self.globalAndLocalPostcondition(self.obj405, rootNode)
    self.obj405.postAction( rootNode.CREATE )

    self.obj406=leftExpr(self)
    self.obj406.isGraphObjectVisual = True

    if(hasattr(self.obj406, '_setHierarchicalLink')):
      self.obj406._setHierarchicalLink(False)

    self.obj406.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(336.0,216.5,self.obj406)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj406.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj406)
    self.globalAndLocalPostcondition(self.obj406, rootNode)
    self.obj406.postAction( rootNode.CREATE )

    self.obj407=leftExpr(self)
    self.obj407.isGraphObjectVisual = True

    if(hasattr(self.obj407, '_setHierarchicalLink')):
      self.obj407._setHierarchicalLink(False)

    self.obj407.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(976.0,376.5,self.obj407)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj407.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj407)
    self.globalAndLocalPostcondition(self.obj407, rootNode)
    self.obj407.postAction( rootNode.CREATE )

    self.obj408=leftExpr(self)
    self.obj408.isGraphObjectVisual = True

    if(hasattr(self.obj408, '_setHierarchicalLink')):
      self.obj408._setHierarchicalLink(False)

    self.obj408.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(996.0,656.5,self.obj408)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj408.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj408)
    self.globalAndLocalPostcondition(self.obj408, rootNode)
    self.obj408.postAction( rootNode.CREATE )

    self.obj409=leftExpr(self)
    self.obj409.isGraphObjectVisual = True

    if(hasattr(self.obj409, '_setHierarchicalLink')):
      self.obj409._setHierarchicalLink(False)

    self.obj409.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(326.0,616.5,self.obj409)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj409.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj409)
    self.globalAndLocalPostcondition(self.obj409, rootNode)
    self.obj409.postAction( rootNode.CREATE )

    self.obj410=rightExpr(self)
    self.obj410.isGraphObjectVisual = True

    if(hasattr(self.obj410, '_setHierarchicalLink')):
      self.obj410._setHierarchicalLink(False)

    self.obj410.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(416.0,216.5,self.obj410)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj410.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj410)
    self.globalAndLocalPostcondition(self.obj410, rootNode)
    self.obj410.postAction( rootNode.CREATE )

    self.obj411=rightExpr(self)
    self.obj411.isGraphObjectVisual = True

    if(hasattr(self.obj411, '_setHierarchicalLink')):
      self.obj411._setHierarchicalLink(False)

    self.obj411.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(896.0,336.5,self.obj411)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj411.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj411)
    self.globalAndLocalPostcondition(self.obj411, rootNode)
    self.obj411.postAction( rootNode.CREATE )

    self.obj412=rightExpr(self)
    self.obj412.isGraphObjectVisual = True

    if(hasattr(self.obj412, '_setHierarchicalLink')):
      self.obj412._setHierarchicalLink(False)

    self.obj412.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(916.0,656.5,self.obj412)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj412.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj412)
    self.globalAndLocalPostcondition(self.obj412, rootNode)
    self.obj412.postAction( rootNode.CREATE )

    self.obj413=rightExpr(self)
    self.obj413.isGraphObjectVisual = True

    if(hasattr(self.obj413, '_setHierarchicalLink')):
      self.obj413._setHierarchicalLink(False)

    self.obj413.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(406.0,616.5,self.obj413)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj413.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj413)
    self.globalAndLocalPostcondition(self.obj413, rootNode)
    self.obj413.postAction( rootNode.CREATE )

    self.obj414=hasArgs(self)
    self.obj414.isGraphObjectVisual = True

    if(hasattr(self.obj414, '_setHierarchicalLink')):
      self.obj414._setHierarchicalLink(False)

    self.obj414.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(734.0,334.0,self.obj414)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj414.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj414)
    self.globalAndLocalPostcondition(self.obj414, rootNode)
    self.obj414.postAction( rootNode.CREATE )

    self.obj415=hasArgs(self)
    self.obj415.isGraphObjectVisual = True

    if(hasattr(self.obj415, '_setHierarchicalLink')):
      self.obj415._setHierarchicalLink(False)

    self.obj415.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(771.0,274.0,self.obj415)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj415.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj415)
    self.globalAndLocalPostcondition(self.obj415, rootNode)
    self.obj415.postAction( rootNode.CREATE )

    self.obj416=hasArgs(self)
    self.obj416.isGraphObjectVisual = True

    if(hasattr(self.obj416, '_setHierarchicalLink')):
      self.obj416._setHierarchicalLink(False)

    self.obj416.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(894.0,294.0,self.obj416)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj416.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj416)
    self.globalAndLocalPostcondition(self.obj416, rootNode)
    self.obj416.postAction( rootNode.CREATE )

    # Connections for obj359 (graphObject_: Obj234) of type MatchModel
    self.drawConnections(
(self.obj359,self.obj384,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj359,self.obj385,[138.0, 51.0, 234.0, 67.0],"true", 2),
(self.obj359,self.obj386,[138.0, 51.0, 384.0, 67.0],"true", 2),
(self.obj359,self.obj387,[138.0, 51.0, 484.0, 67.0],"true", 2),
(self.obj359,self.obj388,[138.0, 51.0, 384.0, 117.0],"true", 2) )
    # Connections for obj360 (graphObject_: Obj235) of type ApplyModel
    self.drawConnections(
(self.obj360,self.obj389,[143.0, 353.0, 247.5, 392.0],"true", 2),
(self.obj360,self.obj390,[143.0, 353.0, 387.5, 392.0],"true", 2),
(self.obj360,self.obj391,[143.0, 353.0, 487.5, 392.0],"true", 2),
(self.obj360,self.obj392,[143.0, 353.0, 140.5, 529.0],"true", 2) )
    # Connections for obj361 (graphObject_: Obj236) named vertex1
    self.drawConnections(
(self.obj361,self.obj401,[830.0, 83.0, 812.0, 128.5],"true", 2) )
    # Connections for obj362 (graphObject_: Obj237) named transition1
    self.drawConnections(
(self.obj362,self.obj397,[630.0, 83.0, 630.0, 133.0],"true", 2),
(self.obj362,self.obj398,[630.0, 83.0, 730.0, 83.0],"true", 2) )
    # Connections for obj363 (graphObject_: Obj238) named state1
    self.drawConnections(
(self.obj363,self.obj396,[330.0, 83.0, 480.0, 83.0],"true", 2),
(self.obj363,self.obj402,[330.0, 83.0, 312.0, 128.5],"true", 2) )
    # Connections for obj364 (graphObject_: Obj239) named in1_1
    self.drawConnections(
 )
    # Connections for obj365 (graphObject_: Obj240) named expr1
    self.drawConnections(
(self.obj365,self.obj403,[832.0, 431.0, 903.0, 422.5],"true", 2) )
    # Connections for obj366 (graphObject_: Obj241) named conditionbranch1
    self.drawConnections(
(self.obj366,self.obj394,[632.0, 431.0, 732.0, 431.0],"true", 2),
(self.obj366,self.obj395,[632.0, 431.0, 651.0, 513.0],"true", 2) )
    # Connections for obj367 (graphObject_: Obj242) named inst1
    self.drawConnections(
(self.obj367,self.obj399,[1012.0, 531.0, 821.0, 307.0],"true", 2),
(self.obj367,self.obj404,[1012.0, 531.0, 1023.0, 572.5],"true", 2) )
    # Connections for obj368 (graphObject_: Obj243) named conditionset1
    self.drawConnections(
(self.obj368,self.obj393,[352.0, 431.0, 492.0, 431.0],"true", 2),
(self.obj368,self.obj400,[352.0, 431.0, 341.0, 257.0],"true", 2),
(self.obj368,self.obj405,[352.0, 431.0, 313.0, 502.5],"true", 2) )
    # Connections for obj369 (graphObject_: Obj244) named name
    self.drawConnections(
 )
    # Connections for obj370 (graphObject_: Obj245) named isComposite
    self.drawConnections(
 )
    # Connections for obj371 (graphObject_: Obj246) named literal
    self.drawConnections(
 )
    # Connections for obj372 (graphObject_: Obj247) named pivot
    self.drawConnections(
 )
    # Connections for obj373 (graphObject_: Obj248) named pivot
    self.drawConnections(
 )
    # Connections for obj374 (graphObject_: Obj249) named eq1
    self.drawConnections(
(self.obj374,self.obj406,[378.0, 259.0, 336.0, 216.5],"true", 2),
(self.obj374,self.obj410,[378.0, 259.0, 416.0, 216.5],"true", 2) )
    # Connections for obj375 (graphObject_: Obj250) named eq2
    self.drawConnections(
(self.obj375,self.obj407,[978.0, 339.0, 976.0, 376.5],"true", 2),
(self.obj375,self.obj411,[978.0, 339.0, 896.0, 336.5],"true", 2) )
    # Connections for obj376 (graphObject_: Obj251) named eq3
    self.drawConnections(
(self.obj376,self.obj408,[958.0, 699.0, 996.0, 656.5],"true", 2),
(self.obj376,self.obj412,[958.0, 699.0, 916.0, 656.5],"true", 2) )
    # Connections for obj377 (graphObject_: Obj252) named eq4
    self.drawConnections(
(self.obj377,self.obj409,[378.0, 659.0, 326.0, 616.5],"true", 2),
(self.obj377,self.obj413,[378.0, 659.0, 406.0, 616.5],"true", 2) )
    # Connections for obj378 (graphObject_: Obj253) named concat1
    self.drawConnections(
(self.obj378,self.obj414,[814.0, 334.0, 734.0, 334.0],"true", 2),
(self.obj378,self.obj415,[814.0, 334.0, 771.0, 274.0],"true", 2),
(self.obj378,self.obj416,[814.0, 334.0, 894.0, 294.0],"true", 2) )
    # Connections for obj379 (graphObject_: Obj254) named true
    self.drawConnections(
 )
    # Connections for obj380 (graphObject_: Obj255) named enp=1
    self.drawConnections(
 )
    # Connections for obj381 (graphObject_: Obj256) named 2
    self.drawConnections(
 )
    # Connections for obj382 (graphObject_: Obj257) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj383 (graphObject_: Obj258) named condsetcompstate
    self.drawConnections(
 )
    # Connections for obj384 (graphObject_: Obj259) of type paired_with
    self.drawConnections(
(self.obj384,self.obj360,[140.5, 152.0, 143.0, 353.0],"true", 2) )
    # Connections for obj385 (graphObject_: Obj260) of type match_contains
    self.drawConnections(
(self.obj385,self.obj363,[234.0, 67.0, 330.0, 83.0],"true", 2) )
    # Connections for obj386 (graphObject_: Obj261) of type match_contains
    self.drawConnections(
(self.obj386,self.obj362,[384.0, 67.0, 630.0, 83.0],"true", 2) )
    # Connections for obj387 (graphObject_: Obj262) of type match_contains
    self.drawConnections(
(self.obj387,self.obj361,[484.0, 67.0, 830.0, 83.0],"true", 2) )
    # Connections for obj388 (graphObject_: Obj263) of type match_contains
    self.drawConnections(
(self.obj388,self.obj364,[384.0, 117.0, 630.0, 183.0],"true", 2) )
    # Connections for obj389 (graphObject_: Obj264) of type apply_contains
    self.drawConnections(
(self.obj389,self.obj368,[247.5, 392.0, 352.0, 431.0],"true", 2) )
    # Connections for obj390 (graphObject_: Obj265) of type apply_contains
    self.drawConnections(
(self.obj390,self.obj366,[387.5, 392.0, 632.0, 431.0],"true", 2) )
    # Connections for obj391 (graphObject_: Obj266) of type apply_contains
    self.drawConnections(
(self.obj391,self.obj365,[487.5, 392.0, 832.0, 431.0],"true", 2) )
    # Connections for obj392 (graphObject_: Obj267) of type apply_contains
    self.drawConnections(
(self.obj392,self.obj367,[140.5, 529.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj393 (graphObject_: Obj268) of type directLink_T
    self.drawConnections(
(self.obj393,self.obj366,[492.0, 431.0, 632.0, 431.0],"true", 2) )
    # Connections for obj394 (graphObject_: Obj269) of type directLink_T
    self.drawConnections(
(self.obj394,self.obj365,[732.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj395 (graphObject_: Obj270) of type directLink_T
    self.drawConnections(
(self.obj395,self.obj367,[651.0, 513.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj396 (graphObject_: Obj271) of type directLink_S
    self.drawConnections(
(self.obj396,self.obj362,[480.0, 83.0, 630.0, 83.0],"true", 2) )
    # Connections for obj397 (graphObject_: Obj272) of type directLink_S
    self.drawConnections(
(self.obj397,self.obj364,[630.0, 133.0, 630.0, 183.0],"true", 2) )
    # Connections for obj398 (graphObject_: Obj273) of type directLink_S
    self.drawConnections(
(self.obj398,self.obj361,[730.0, 83.0, 830.0, 83.0],"true", 2) )
    # Connections for obj399 (graphObject_: Obj274) of type backward_link
    self.drawConnections(
(self.obj399,self.obj362,[821.0, 307.0, 630.0, 83.0],"true", 2) )
    # Connections for obj400 (graphObject_: Obj275) of type backward_link
    self.drawConnections(
(self.obj400,self.obj363,[341.0, 257.0, 330.0, 83.0],"true", 2) )
    # Connections for obj401 (graphObject_: Obj276) of type hasAttribute_S
    self.drawConnections(
(self.obj401,self.obj369,[812.0, 128.5, 774.0, 174.0],"true", 2) )
    # Connections for obj402 (graphObject_: Obj277) of type hasAttribute_S
    self.drawConnections(
(self.obj402,self.obj370,[312.0, 128.5, 294.0, 174.0],"true", 2) )
    # Connections for obj403 (graphObject_: Obj278) of type hasAttribute_T
    self.drawConnections(
(self.obj403,self.obj371,[903.0, 422.5, 974.0, 414.0],"true", 2) )
    # Connections for obj404 (graphObject_: Obj279) of type hasAttribute_T
    self.drawConnections(
(self.obj404,self.obj372,[1023.0, 572.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj405 (graphObject_: Obj280) of type hasAttribute_T
    self.drawConnections(
(self.obj405,self.obj373,[313.0, 502.5, 274.0, 574.0],"true", 2) )
    # Connections for obj406 (graphObject_: Obj281) of type leftExpr
    self.drawConnections(
(self.obj406,self.obj370,[336.0, 216.5, 294.0, 174.0],"true", 2) )
    # Connections for obj407 (graphObject_: Obj282) of type leftExpr
    self.drawConnections(
(self.obj407,self.obj371,[976.0, 376.5, 974.0, 414.0],"true", 2) )
    # Connections for obj408 (graphObject_: Obj283) of type leftExpr
    self.drawConnections(
(self.obj408,self.obj372,[996.0, 656.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj409 (graphObject_: Obj284) of type leftExpr
    self.drawConnections(
(self.obj409,self.obj373,[326.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj410 (graphObject_: Obj285) of type rightExpr
    self.drawConnections(
(self.obj410,self.obj379,[416.0, 216.5, 454.0, 174.0],"true", 2) )
    # Connections for obj411 (graphObject_: Obj286) of type rightExpr
    self.drawConnections(
(self.obj411,self.obj378,[896.0, 336.5, 814.0, 334.0],"true", 2) )
    # Connections for obj412 (graphObject_: Obj287) of type rightExpr
    self.drawConnections(
(self.obj412,self.obj382,[916.0, 656.5, 874.0, 614.0],"true", 2) )
    # Connections for obj413 (graphObject_: Obj288) of type rightExpr
    self.drawConnections(
(self.obj413,self.obj383,[406.0, 616.5, 434.0, 574.0],"true", 2) )
    # Connections for obj414 (graphObject_: Obj289) of type hasArgs
    self.drawConnections(
(self.obj414,self.obj380,[734.0, 334.0, 654.0, 334.0],"true", 2) )
    # Connections for obj415 (graphObject_: Obj290) of type hasArgs
    self.drawConnections(
(self.obj415,self.obj369,[771.0, 274.0, 774.0, 174.0],"true", 2) )
    # Connections for obj416 (graphObject_: Obj291) of type hasArgs
    self.drawConnections(
(self.obj416,self.obj381,[894.0, 294.0, 934.0, 254.0],"true", 2) )

newfunction = ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'