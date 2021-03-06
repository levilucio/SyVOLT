"""
__ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Feb  9 22:15:50 2015
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


    self.obj100=MatchModel(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    self.obj100.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=ApplyModel(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    self.obj101.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,320.0,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=Vertex(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # name
    self.obj102.name.setValue('vertex1')

    # classtype
    self.obj102.classtype.setValue('Vertex')

    # cardinality
    self.obj102.cardinality.setValue('+')

    self.obj102.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,40.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=Transition(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('transition1')

    # classtype
    self.obj103.classtype.setValue('Transition')

    # cardinality
    self.obj103.cardinality.setValue('+')

    self.obj103.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(460.0,40.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=State(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # name
    self.obj104.name.setValue('state1')

    # classtype
    self.obj104.classtype.setValue('State')

    # cardinality
    self.obj104.cardinality.setValue('+')

    self.obj104.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,40.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=IN1(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # classtype
    self.obj105.classtype.setValue('IN1')

    # cardinality
    self.obj105.cardinality.setValue('+')

    # name
    self.obj105.name.setValue('in1_1')

    self.obj105.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(460.0,140.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Expr(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # classtype
    self.obj106.classtype.setValue('Expr')

    # cardinality
    self.obj106.cardinality.setValue('1')

    # name
    self.obj106.name.setValue('expr1')

    self.obj106.graphClass_= graph_Expr
    if self.genGraphics:
       new_obj = graph_Expr(660.0,380.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Expr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=ConditionBranch(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # classtype
    self.obj107.classtype.setValue('ConditionBranch')

    # cardinality
    self.obj107.cardinality.setValue('1')

    # name
    self.obj107.name.setValue('conditionbranch1')

    self.obj107.graphClass_= graph_ConditionBranch
    if self.genGraphics:
       new_obj = graph_ConditionBranch(460.0,380.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=Inst(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # classtype
    self.obj108.classtype.setValue('Inst')

    # cardinality
    self.obj108.cardinality.setValue('1')

    # name
    self.obj108.name.setValue('inst1')

    self.obj108.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(840.0,480.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=ConditionSet(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # classtype
    self.obj109.classtype.setValue('ConditionSet')

    # cardinality
    self.obj109.cardinality.setValue('1')

    # name
    self.obj109.name.setValue('conditionset1')

    self.obj109.graphClass_= graph_ConditionSet
    if self.genGraphics:
       new_obj = graph_ConditionSet(180.0,380.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ConditionSet", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Attribute(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # Type
    self.obj110.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj110.Type.config = 0

    # name
    self.obj110.name.setValue('name')

    self.obj110.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,140.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Attribute(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # Type
    self.obj111.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj111.Type.config = 0

    # name
    self.obj111.name.setValue('isComposite')

    self.obj111.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,140.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=Attribute(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # Type
    self.obj112.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj112.Type.config = 0

    # name
    self.obj112.name.setValue('literal')

    self.obj112.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,380.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=Attribute(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # Type
    self.obj113.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj113.Type.config = 0

    # name
    self.obj113.name.setValue('pivot')

    self.obj113.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(900.0,580.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Attribute(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # Type
    self.obj114.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj114.Type.config = 0

    # name
    self.obj114.name.setValue('pivot')

    self.obj114.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(140.0,540.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Equation(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # name
    self.obj115.name.setValue('eq1')

    self.obj115.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,220.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=Equation(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # name
    self.obj116.name.setValue('eq2')

    self.obj116.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(840.0,300.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=Equation(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # name
    self.obj117.name.setValue('eq3')

    self.obj117.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,660.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=Equation(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # name
    self.obj118.name.setValue('eq4')

    self.obj118.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,620.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=Concat(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # Type
    self.obj119.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj119.Type.config = 0

    # name
    self.obj119.name.setValue('concat1')

    self.obj119.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(680.0,300.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=Constant(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # Type
    self.obj120.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj120.Type.config = 0

    # name
    self.obj120.name.setValue('true')

    self.obj120.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(320.0,140.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=Constant(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # Type
    self.obj121.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj121.Type.config = 0

    # name
    self.obj121.name.setValue('enp=1')

    self.obj121.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(520.0,300.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=Constant(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # Type
    self.obj122.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj122.Type.config = 0

    # name
    self.obj122.name.setValue('2')

    self.obj122.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,220.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=Constant(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # Type
    self.obj123.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj123.Type.config = 0

    # name
    self.obj123.name.setValue('instForInTrans')

    self.obj123.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(740.0,580.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=Constant(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # Type
    self.obj124.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj124.Type.config = 0

    # name
    self.obj124.name.setValue('condsetcompstate')

    self.obj124.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(300.0,540.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=paired_with(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    self.obj125.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=match_contains(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    self.obj126.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,67.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=match_contains(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    self.obj127.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,67.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=match_contains(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    self.obj128.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,67.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=match_contains(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    self.obj129.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,117.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=apply_contains(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    self.obj130.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,392.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=apply_contains(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    self.obj131.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(387.5,392.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=apply_contains(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    self.obj132.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,392.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=apply_contains(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    self.obj133.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(140.5,529.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=directLink_T(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # associationType
    self.obj134.associationType.setValue('branches')

    self.obj134.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(492.0,431.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=directLink_T(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # associationType
    self.obj135.associationType.setValue('if')

    self.obj135.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(732.0,431.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=directLink_T(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # associationType
    self.obj136.associationType.setValue('then')

    self.obj136.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(651.0,513.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=directLink_S(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # associationType
    self.obj137.associationType.setValue('transitions')

    self.obj137.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,83.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=directLink_S(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # associationType
    self.obj138.associationType.setValue('type')

    self.obj138.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(630.0,133.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=directLink_S(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    # associationType
    self.obj139.associationType.setValue('src')

    self.obj139.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(730.0,83.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=backward_link(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # type
    self.obj140.type.setValue('ruleDef')

    self.obj140.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(821.0,307.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=backward_link(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    # type
    self.obj141.type.setValue('ruleDef')

    self.obj141.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,257.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=hasAttribute_S(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(812.0,128.5,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=hasAttribute_S(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    self.obj143.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,128.5,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=hasAttribute_T(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    self.obj144.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(903.0,422.5,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=hasAttribute_T(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    self.obj145.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1023.0,572.5,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=hasAttribute_T(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    self.obj146.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(313.0,502.5,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=leftExpr(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    self.obj147.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(336.0,216.5,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=leftExpr(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    self.obj148.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(976.0,376.5,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj149=leftExpr(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    self.obj149.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(996.0,656.5,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=leftExpr(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    self.obj150.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(326.0,616.5,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=rightExpr(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    self.obj151.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(416.0,216.5,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=rightExpr(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    self.obj152.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(896.0,336.5,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj153=rightExpr(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    self.obj153.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(916.0,656.5,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=rightExpr(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    self.obj154.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(406.0,616.5,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=hasArgs(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    self.obj155.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(734.0,334.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=hasArgs(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    self.obj156.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(771.0,274.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=hasArgs(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    self.obj157.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(894.0,294.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj125,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj100,self.obj126,[138.0, 51.0, 234.0, 67.0],"true", 2),
(self.obj100,self.obj127,[138.0, 51.0, 384.0, 67.0],"true", 2),
(self.obj100,self.obj128,[138.0, 51.0, 484.0, 67.0],"true", 2),
(self.obj100,self.obj129,[138.0, 51.0, 384.0, 117.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj130,[143.0, 353.0, 247.5, 392.0],"true", 2),
(self.obj101,self.obj131,[143.0, 353.0, 387.5, 392.0],"true", 2),
(self.obj101,self.obj132,[143.0, 353.0, 487.5, 392.0],"true", 2),
(self.obj101,self.obj133,[143.0, 353.0, 140.5, 529.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj2) named vertex1
    self.drawConnections(
(self.obj102,self.obj142,[830.0, 83.0, 812.0, 128.5],"true", 2) )
    # Connections for obj103 (graphObject_: Obj3) named transition1
    self.drawConnections(
(self.obj103,self.obj138,[630.0, 83.0, 630.0, 133.0],"true", 2),
(self.obj103,self.obj139,[630.0, 83.0, 730.0, 83.0],"true", 2) )
    # Connections for obj104 (graphObject_: Obj4) named state1
    self.drawConnections(
(self.obj104,self.obj137,[330.0, 83.0, 480.0, 83.0],"true", 2),
(self.obj104,self.obj143,[330.0, 83.0, 312.0, 128.5],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) named in1_1
    self.drawConnections(
 )
    # Connections for obj106 (graphObject_: Obj6) named expr1
    self.drawConnections(
(self.obj106,self.obj144,[832.0, 431.0, 903.0, 422.5],"true", 2) )
    # Connections for obj107 (graphObject_: Obj7) named conditionbranch1
    self.drawConnections(
(self.obj107,self.obj135,[632.0, 431.0, 732.0, 431.0],"true", 2),
(self.obj107,self.obj136,[632.0, 431.0, 651.0, 513.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj8) named inst1
    self.drawConnections(
(self.obj108,self.obj140,[1012.0, 531.0, 821.0, 307.0],"true", 2),
(self.obj108,self.obj145,[1012.0, 531.0, 1023.0, 572.5],"true", 2) )
    # Connections for obj109 (graphObject_: Obj9) named conditionset1
    self.drawConnections(
(self.obj109,self.obj134,[352.0, 431.0, 492.0, 431.0],"true", 2),
(self.obj109,self.obj141,[352.0, 431.0, 341.0, 257.0],"true", 2),
(self.obj109,self.obj146,[352.0, 431.0, 313.0, 502.5],"true", 2) )
    # Connections for obj110 (graphObject_: Obj10) named name
    self.drawConnections(
 )
    # Connections for obj111 (graphObject_: Obj11) named isComposite
    self.drawConnections(
 )
    # Connections for obj112 (graphObject_: Obj12) named literal
    self.drawConnections(
 )
    # Connections for obj113 (graphObject_: Obj13) named pivot
    self.drawConnections(
 )
    # Connections for obj114 (graphObject_: Obj14) named pivot
    self.drawConnections(
 )
    # Connections for obj115 (graphObject_: Obj15) named eq1
    self.drawConnections(
(self.obj115,self.obj147,[378.0, 259.0, 336.0, 216.5],"true", 2),
(self.obj115,self.obj151,[378.0, 259.0, 416.0, 216.5],"true", 2) )
    # Connections for obj116 (graphObject_: Obj16) named eq2
    self.drawConnections(
(self.obj116,self.obj148,[978.0, 339.0, 976.0, 376.5],"true", 2),
(self.obj116,self.obj152,[978.0, 339.0, 896.0, 336.5],"true", 2) )
    # Connections for obj117 (graphObject_: Obj17) named eq3
    self.drawConnections(
(self.obj117,self.obj149,[958.0, 699.0, 996.0, 656.5],"true", 2),
(self.obj117,self.obj153,[958.0, 699.0, 916.0, 656.5],"true", 2) )
    # Connections for obj118 (graphObject_: Obj18) named eq4
    self.drawConnections(
(self.obj118,self.obj150,[378.0, 659.0, 326.0, 616.5],"true", 2),
(self.obj118,self.obj154,[378.0, 659.0, 406.0, 616.5],"true", 2) )
    # Connections for obj119 (graphObject_: Obj19) named concat1
    self.drawConnections(
(self.obj119,self.obj155,[814.0, 334.0, 734.0, 334.0],"true", 2),
(self.obj119,self.obj156,[814.0, 334.0, 771.0, 274.0],"true", 2),
(self.obj119,self.obj157,[814.0, 334.0, 894.0, 294.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj20) named true
    self.drawConnections(
 )
    # Connections for obj121 (graphObject_: Obj21) named enp=1
    self.drawConnections(
 )
    # Connections for obj122 (graphObject_: Obj22) named 2
    self.drawConnections(
 )
    # Connections for obj123 (graphObject_: Obj23) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj24) named condsetcompstate
    self.drawConnections(
 )
    # Connections for obj125 (graphObject_: Obj25) of type paired_with
    self.drawConnections(
(self.obj125,self.obj101,[140.5, 152.0, 143.0, 353.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj26) of type match_contains
    self.drawConnections(
(self.obj126,self.obj104,[234.0, 67.0, 330.0, 83.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj27) of type match_contains
    self.drawConnections(
(self.obj127,self.obj103,[384.0, 67.0, 630.0, 83.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj28) of type match_contains
    self.drawConnections(
(self.obj128,self.obj102,[484.0, 67.0, 830.0, 83.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj29) of type match_contains
    self.drawConnections(
(self.obj129,self.obj105,[384.0, 117.0, 630.0, 183.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj30) of type apply_contains
    self.drawConnections(
(self.obj130,self.obj109,[247.5, 392.0, 352.0, 431.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj31) of type apply_contains
    self.drawConnections(
(self.obj131,self.obj107,[387.5, 392.0, 632.0, 431.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj32) of type apply_contains
    self.drawConnections(
(self.obj132,self.obj106,[487.5, 392.0, 832.0, 431.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj33) of type apply_contains
    self.drawConnections(
(self.obj133,self.obj108,[140.5, 529.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj134 (graphObject_: Obj34) of type directLink_T
    self.drawConnections(
(self.obj134,self.obj107,[492.0, 431.0, 632.0, 431.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj35) of type directLink_T
    self.drawConnections(
(self.obj135,self.obj106,[732.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj36) of type directLink_T
    self.drawConnections(
(self.obj136,self.obj108,[651.0, 513.0, 1012.0, 531.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj37) of type directLink_S
    self.drawConnections(
(self.obj137,self.obj103,[480.0, 83.0, 630.0, 83.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj38) of type directLink_S
    self.drawConnections(
(self.obj138,self.obj105,[630.0, 133.0, 630.0, 183.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj39) of type directLink_S
    self.drawConnections(
(self.obj139,self.obj102,[730.0, 83.0, 830.0, 83.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj40) of type backward_link
    self.drawConnections(
(self.obj140,self.obj103,[821.0, 307.0, 630.0, 83.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj41) of type backward_link
    self.drawConnections(
(self.obj141,self.obj104,[341.0, 257.0, 330.0, 83.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj42) of type hasAttribute_S
    self.drawConnections(
(self.obj142,self.obj110,[812.0, 128.5, 774.0, 174.0],"true", 2) )
    # Connections for obj143 (graphObject_: Obj43) of type hasAttribute_S
    self.drawConnections(
(self.obj143,self.obj111,[312.0, 128.5, 294.0, 174.0],"true", 2) )
    # Connections for obj144 (graphObject_: Obj44) of type hasAttribute_T
    self.drawConnections(
(self.obj144,self.obj112,[903.0, 422.5, 974.0, 414.0],"true", 2) )
    # Connections for obj145 (graphObject_: Obj45) of type hasAttribute_T
    self.drawConnections(
(self.obj145,self.obj113,[1023.0, 572.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj146 (graphObject_: Obj46) of type hasAttribute_T
    self.drawConnections(
(self.obj146,self.obj114,[313.0, 502.5, 274.0, 574.0],"true", 2) )
    # Connections for obj147 (graphObject_: Obj47) of type leftExpr
    self.drawConnections(
(self.obj147,self.obj111,[336.0, 216.5, 294.0, 174.0],"true", 2) )
    # Connections for obj148 (graphObject_: Obj48) of type leftExpr
    self.drawConnections(
(self.obj148,self.obj112,[976.0, 376.5, 974.0, 414.0],"true", 2) )
    # Connections for obj149 (graphObject_: Obj49) of type leftExpr
    self.drawConnections(
(self.obj149,self.obj113,[996.0, 656.5, 1034.0, 614.0],"true", 2) )
    # Connections for obj150 (graphObject_: Obj50) of type leftExpr
    self.drawConnections(
(self.obj150,self.obj114,[326.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj151 (graphObject_: Obj51) of type rightExpr
    self.drawConnections(
(self.obj151,self.obj120,[416.0, 216.5, 454.0, 174.0],"true", 2) )
    # Connections for obj152 (graphObject_: Obj52) of type rightExpr
    self.drawConnections(
(self.obj152,self.obj119,[896.0, 336.5, 814.0, 334.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj53) of type rightExpr
    self.drawConnections(
(self.obj153,self.obj123,[916.0, 656.5, 874.0, 614.0],"true", 2) )
    # Connections for obj154 (graphObject_: Obj54) of type rightExpr
    self.drawConnections(
(self.obj154,self.obj124,[406.0, 616.5, 434.0, 574.0],"true", 2) )
    # Connections for obj155 (graphObject_: Obj55) of type hasArgs
    self.drawConnections(
(self.obj155,self.obj121,[734.0, 334.0, 654.0, 334.0],"true", 2) )
    # Connections for obj156 (graphObject_: Obj56) of type hasArgs
    self.drawConnections(
(self.obj156,self.obj110,[771.0, 274.0, 774.0, 174.0],"true", 2) )
    # Connections for obj157 (graphObject_: Obj57) of type hasArgs
    self.drawConnections(
(self.obj157,self.obj122,[894.0, 294.0, 934.0, 254.0],"true", 2) )

newfunction = ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
