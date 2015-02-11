"""
__Transition2Inst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 15:09:28 2015
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from EntryPoint import *
from Transition import *
from StateMachine import *
from State import *
from IN1 import *
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
from graph_Transition import *
from graph_paired_with import *
from graph_State import *
from graph_Equation import *
from graph_IN1 import *
from graph_hasArgs import *
from graph_rightExpr import *
from graph_Concat import *
from graph_Inst import *
from graph_hasAttribute_T import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_ApplyModel import *
from graph_Name import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_hasAttribute_S import *
from graph_match_contains import *
from graph_leftExpr import *
from graph_Constant import *
from graph_EntryPoint import *
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

def Transition2Inst_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2Inst')
    # --- ASG attributes over ---


    self.obj912=MatchModel(self)
    self.obj912.isGraphObjectVisual = True

    if(hasattr(self.obj912, '_setHierarchicalLink')):
      self.obj912._setHierarchicalLink(False)

    self.obj912.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj912)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj912.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj912)
    self.globalAndLocalPostcondition(self.obj912, rootNode)
    self.obj912.postAction( rootNode.CREATE )

    self.obj913=ApplyModel(self)
    self.obj913.isGraphObjectVisual = True

    if(hasattr(self.obj913, '_setHierarchicalLink')):
      self.obj913._setHierarchicalLink(False)

    self.obj913.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,380.0,self.obj913)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj913.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj913)
    self.globalAndLocalPostcondition(self.obj913, rootNode)
    self.obj913.postAction( rootNode.CREATE )

    self.obj914=EntryPoint(self)
    self.obj914.isGraphObjectVisual = True

    if(hasattr(self.obj914, '_setHierarchicalLink')):
      self.obj914._setHierarchicalLink(False)

    # name
    self.obj914.name.setValue('entrypoint1')

    # classtype
    self.obj914.classtype.setValue('EntryPoint')

    # cardinality
    self.obj914.cardinality.setValue('1')

    self.obj914.graphClass_= graph_EntryPoint
    if self.genGraphics:
       new_obj = graph_EntryPoint(780.0,40.0,self.obj914)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("EntryPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj914.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj914)
    self.globalAndLocalPostcondition(self.obj914, rootNode)
    self.obj914.postAction( rootNode.CREATE )

    self.obj915=Transition(self)
    self.obj915.isGraphObjectVisual = True

    if(hasattr(self.obj915, '_setHierarchicalLink')):
      self.obj915._setHierarchicalLink(False)

    # name
    self.obj915.name.setValue('transition1')

    # classtype
    self.obj915.classtype.setValue('Transition')

    # cardinality
    self.obj915.cardinality.setValue('+')

    self.obj915.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,40.0,self.obj915)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj915.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj915)
    self.globalAndLocalPostcondition(self.obj915, rootNode)
    self.obj915.postAction( rootNode.CREATE )

    self.obj916=StateMachine(self)
    self.obj916.isGraphObjectVisual = True

    if(hasattr(self.obj916, '_setHierarchicalLink')):
      self.obj916._setHierarchicalLink(False)

    # name
    self.obj916.name.setValue('statemachine1')

    # classtype
    self.obj916.classtype.setValue('StateMachine')

    # cardinality
    self.obj916.cardinality.setValue('1')

    self.obj916.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(620.0,140.0,self.obj916)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj916.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj916)
    self.globalAndLocalPostcondition(self.obj916, rootNode)
    self.obj916.postAction( rootNode.CREATE )

    self.obj917=State(self)
    self.obj917.isGraphObjectVisual = True

    if(hasattr(self.obj917, '_setHierarchicalLink')):
      self.obj917._setHierarchicalLink(False)

    # name
    self.obj917.name.setValue('state1')

    # classtype
    self.obj917.classtype.setValue('State')

    # cardinality
    self.obj917.cardinality.setValue('+')

    self.obj917.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj917)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj917.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj917)
    self.globalAndLocalPostcondition(self.obj917, rootNode)
    self.obj917.postAction( rootNode.CREATE )

    self.obj918=IN1(self)
    self.obj918.isGraphObjectVisual = True

    if(hasattr(self.obj918, '_setHierarchicalLink')):
      self.obj918._setHierarchicalLink(False)

    # classtype
    self.obj918.classtype.setValue('IN1')

    # cardinality
    self.obj918.cardinality.setValue('1')

    # name
    self.obj918.name.setValue('in1_1')

    self.obj918.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(440.0,140.0,self.obj918)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj918.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj918)
    self.globalAndLocalPostcondition(self.obj918, rootNode)
    self.obj918.postAction( rootNode.CREATE )

    self.obj919=Name(self)
    self.obj919.isGraphObjectVisual = True

    if(hasattr(self.obj919, '_setHierarchicalLink')):
      self.obj919._setHierarchicalLink(False)

    # classtype
    self.obj919.classtype.setValue('Name')

    # cardinality
    self.obj919.cardinality.setValue('1')

    # name
    self.obj919.name.setValue('name1')

    self.obj919.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,280.0,self.obj919)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj919.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj919)
    self.globalAndLocalPostcondition(self.obj919, rootNode)
    self.obj919.postAction( rootNode.CREATE )

    self.obj920=Name(self)
    self.obj920.isGraphObjectVisual = True

    if(hasattr(self.obj920, '_setHierarchicalLink')):
      self.obj920._setHierarchicalLink(False)

    # classtype
    self.obj920.classtype.setValue('Name')

    # cardinality
    self.obj920.cardinality.setValue('1')

    # name
    self.obj920.name.setValue('name2')

    self.obj920.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,380.0,self.obj920)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj920.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj920)
    self.globalAndLocalPostcondition(self.obj920, rootNode)
    self.obj920.postAction( rootNode.CREATE )

    self.obj921=Name(self)
    self.obj921.isGraphObjectVisual = True

    if(hasattr(self.obj921, '_setHierarchicalLink')):
      self.obj921._setHierarchicalLink(False)

    # classtype
    self.obj921.classtype.setValue('Name')

    # cardinality
    self.obj921.cardinality.setValue('1')

    # name
    self.obj921.name.setValue('name3')

    self.obj921.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1020.0,520.0,self.obj921)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj921.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj921)
    self.globalAndLocalPostcondition(self.obj921, rootNode)
    self.obj921.postAction( rootNode.CREATE )

    self.obj922=Name(self)
    self.obj922.isGraphObjectVisual = True

    if(hasattr(self.obj922, '_setHierarchicalLink')):
      self.obj922._setHierarchicalLink(False)

    # classtype
    self.obj922.classtype.setValue('Name')

    # cardinality
    self.obj922.cardinality.setValue('1')

    # name
    self.obj922.name.setValue('name4')

    self.obj922.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(580.0,540.0,self.obj922)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj922.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj922)
    self.globalAndLocalPostcondition(self.obj922, rootNode)
    self.obj922.postAction( rootNode.CREATE )

    self.obj923=Inst(self)
    self.obj923.isGraphObjectVisual = True

    if(hasattr(self.obj923, '_setHierarchicalLink')):
      self.obj923._setHierarchicalLink(False)

    # classtype
    self.obj923.classtype.setValue('Inst')

    # cardinality
    self.obj923.cardinality.setValue('1')

    # name
    self.obj923.name.setValue('inst1')

    self.obj923.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(220.0,420.0,self.obj923)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj923.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj923)
    self.globalAndLocalPostcondition(self.obj923, rootNode)
    self.obj923.postAction( rootNode.CREATE )

    self.obj924=Attribute(self)
    self.obj924.isGraphObjectVisual = True

    if(hasattr(self.obj924, '_setHierarchicalLink')):
      self.obj924._setHierarchicalLink(False)

    # Type
    self.obj924.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj924.Type.config = 0

    # name
    self.obj924.name.setValue('name')

    self.obj924.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,220.0,self.obj924)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj924.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj924)
    self.globalAndLocalPostcondition(self.obj924, rootNode)
    self.obj924.postAction( rootNode.CREATE )

    self.obj925=Attribute(self)
    self.obj925.isGraphObjectVisual = True

    if(hasattr(self.obj925, '_setHierarchicalLink')):
      self.obj925._setHierarchicalLink(False)

    # Type
    self.obj925.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj925.Type.config = 0

    # name
    self.obj925.name.setValue('name')

    self.obj925.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(540.0,240.0,self.obj925)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj925.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj925)
    self.globalAndLocalPostcondition(self.obj925, rootNode)
    self.obj925.postAction( rootNode.CREATE )

    self.obj926=Attribute(self)
    self.obj926.isGraphObjectVisual = True

    if(hasattr(self.obj926, '_setHierarchicalLink')):
      self.obj926._setHierarchicalLink(False)

    # Type
    self.obj926.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj926.Type.config = 0

    # name
    self.obj926.name.setValue('isComposite')

    self.obj926.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(151.0,140.0,self.obj926)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj926.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj926)
    self.globalAndLocalPostcondition(self.obj926, rootNode)
    self.obj926.postAction( rootNode.CREATE )

    self.obj927=Attribute(self)
    self.obj927.isGraphObjectVisual = True

    if(hasattr(self.obj927, '_setHierarchicalLink')):
      self.obj927._setHierarchicalLink(False)

    # Type
    self.obj927.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj927.Type.config = 0

    # name
    self.obj927.name.setValue('literal')

    self.obj927.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,300.0,self.obj927)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj927.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj927)
    self.globalAndLocalPostcondition(self.obj927, rootNode)
    self.obj927.postAction( rootNode.CREATE )

    self.obj928=Attribute(self)
    self.obj928.isGraphObjectVisual = True

    if(hasattr(self.obj928, '_setHierarchicalLink')):
      self.obj928._setHierarchicalLink(False)

    # Type
    self.obj928.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj928.Type.config = 0

    # name
    self.obj928.name.setValue('literal')

    self.obj928.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,380.0,self.obj928)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj928.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj928)
    self.globalAndLocalPostcondition(self.obj928, rootNode)
    self.obj928.postAction( rootNode.CREATE )

    self.obj929=Attribute(self)
    self.obj929.isGraphObjectVisual = True

    if(hasattr(self.obj929, '_setHierarchicalLink')):
      self.obj929._setHierarchicalLink(False)

    # Type
    self.obj929.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj929.Type.config = 0

    # name
    self.obj929.name.setValue('literal')

    self.obj929.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1020.0,440.0,self.obj929)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj929.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj929)
    self.globalAndLocalPostcondition(self.obj929, rootNode)
    self.obj929.postAction( rootNode.CREATE )

    self.obj930=Attribute(self)
    self.obj930.isGraphObjectVisual = True

    if(hasattr(self.obj930, '_setHierarchicalLink')):
      self.obj930._setHierarchicalLink(False)

    # Type
    self.obj930.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj930.Type.config = 0

    # name
    self.obj930.name.setValue('literal')

    self.obj930.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,560.0,self.obj930)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj930.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj930)
    self.globalAndLocalPostcondition(self.obj930, rootNode)
    self.obj930.postAction( rootNode.CREATE )

    self.obj931=Attribute(self)
    self.obj931.isGraphObjectVisual = True

    if(hasattr(self.obj931, '_setHierarchicalLink')):
      self.obj931._setHierarchicalLink(False)

    # Type
    self.obj931.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj931.Type.config = 0

    # name
    self.obj931.name.setValue('name')

    self.obj931.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,340.0,self.obj931)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj931.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj931)
    self.globalAndLocalPostcondition(self.obj931, rootNode)
    self.obj931.postAction( rootNode.CREATE )

    self.obj932=Attribute(self)
    self.obj932.isGraphObjectVisual = True

    if(hasattr(self.obj932, '_setHierarchicalLink')):
      self.obj932._setHierarchicalLink(False)

    # Type
    self.obj932.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj932.Type.config = 0

    # name
    self.obj932.name.setValue('pivot')

    self.obj932.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,580.0,self.obj932)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj932.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj932)
    self.globalAndLocalPostcondition(self.obj932, rootNode)
    self.obj932.postAction( rootNode.CREATE )

    self.obj933=Equation(self)
    self.obj933.isGraphObjectVisual = True

    if(hasattr(self.obj933, '_setHierarchicalLink')):
      self.obj933._setHierarchicalLink(False)

    # name
    self.obj933.name.setValue('eq1')

    self.obj933.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(295.0,140.0,self.obj933)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj933.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj933)
    self.globalAndLocalPostcondition(self.obj933, rootNode)
    self.obj933.postAction( rootNode.CREATE )

    self.obj934=Equation(self)
    self.obj934.isGraphObjectVisual = True

    if(hasattr(self.obj934, '_setHierarchicalLink')):
      self.obj934._setHierarchicalLink(False)

    # name
    self.obj934.name.setValue('eq2')

    self.obj934.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,220.0,self.obj934)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj934.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj934)
    self.globalAndLocalPostcondition(self.obj934, rootNode)
    self.obj934.postAction( rootNode.CREATE )

    self.obj935=Equation(self)
    self.obj935.isGraphObjectVisual = True

    if(hasattr(self.obj935, '_setHierarchicalLink')):
      self.obj935._setHierarchicalLink(False)

    # name
    self.obj935.name.setValue('eq3')

    self.obj935.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,460.0,self.obj935)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj935.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj935)
    self.globalAndLocalPostcondition(self.obj935, rootNode)
    self.obj935.postAction( rootNode.CREATE )

    self.obj936=Equation(self)
    self.obj936.isGraphObjectVisual = True

    if(hasattr(self.obj936, '_setHierarchicalLink')):
      self.obj936._setHierarchicalLink(False)

    # name
    self.obj936.name.setValue('eq4')

    self.obj936.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(874.0,449.0,self.obj936)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj936.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj936)
    self.globalAndLocalPostcondition(self.obj936, rootNode)
    self.obj936.postAction( rootNode.CREATE )

    self.obj937=Equation(self)
    self.obj937.isGraphObjectVisual = True

    if(hasattr(self.obj937, '_setHierarchicalLink')):
      self.obj937._setHierarchicalLink(False)

    # name
    self.obj937.name.setValue('eq5')

    self.obj937.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(740.0,640.0,self.obj937)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj937.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj937)
    self.globalAndLocalPostcondition(self.obj937, rootNode)
    self.obj937.postAction( rootNode.CREATE )

    self.obj938=Equation(self)
    self.obj938.isGraphObjectVisual = True

    if(hasattr(self.obj938, '_setHierarchicalLink')):
      self.obj938._setHierarchicalLink(False)

    # name
    self.obj938.name.setValue('eq6')

    self.obj938.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,340.0,self.obj938)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj938.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj938)
    self.globalAndLocalPostcondition(self.obj938, rootNode)
    self.obj938.postAction( rootNode.CREATE )

    self.obj939=Equation(self)
    self.obj939.isGraphObjectVisual = True

    if(hasattr(self.obj939, '_setHierarchicalLink')):
      self.obj939._setHierarchicalLink(False)

    # name
    self.obj939.name.setValue('eq7')

    self.obj939.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,660.0,self.obj939)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj939.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj939)
    self.globalAndLocalPostcondition(self.obj939, rootNode)
    self.obj939.postAction( rootNode.CREATE )

    self.obj940=Concat(self)
    self.obj940.isGraphObjectVisual = True

    if(hasattr(self.obj940, '_setHierarchicalLink')):
      self.obj940._setHierarchicalLink(False)

    # Type
    self.obj940.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj940.Type.config = 0

    # name
    self.obj940.name.setValue('concat1')

    self.obj940.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(940.0,355.0,self.obj940)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj940.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj940)
    self.globalAndLocalPostcondition(self.obj940, rootNode)
    self.obj940.postAction( rootNode.CREATE )

    self.obj941=Concat(self)
    self.obj941.isGraphObjectVisual = True

    if(hasattr(self.obj941, '_setHierarchicalLink')):
      self.obj941._setHierarchicalLink(False)

    # Type
    self.obj941.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj941.Type.config = 0

    # name
    self.obj941.name.setValue('concat2')

    self.obj941.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,340.0,self.obj941)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj941.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj941)
    self.globalAndLocalPostcondition(self.obj941, rootNode)
    self.obj941.postAction( rootNode.CREATE )

    self.obj942=Constant(self)
    self.obj942.isGraphObjectVisual = True

    if(hasattr(self.obj942, '_setHierarchicalLink')):
      self.obj942._setHierarchicalLink(False)

    # Type
    self.obj942.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj942.Type.config = 0

    # name
    self.obj942.name.setValue('true')

    self.obj942.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,220.0,self.obj942)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj942.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj942)
    self.globalAndLocalPostcondition(self.obj942, rootNode)
    self.obj942.postAction( rootNode.CREATE )

    self.obj943=Constant(self)
    self.obj943.isGraphObjectVisual = True

    if(hasattr(self.obj943, '_setHierarchicalLink')):
      self.obj943._setHierarchicalLink(False)

    # Type
    self.obj943.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj943.Type.config = 0

    # name
    self.obj943.name.setValue('exit_in')

    self.obj943.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1200.0,207.0,self.obj943)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj943.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj943)
    self.globalAndLocalPostcondition(self.obj943, rootNode)
    self.obj943.postAction( rootNode.CREATE )

    self.obj944=Constant(self)
    self.obj944.isGraphObjectVisual = True

    if(hasattr(self.obj944, '_setHierarchicalLink')):
      self.obj944._setHierarchicalLink(False)

    # Type
    self.obj944.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj944.Type.config = 0

    # name
    self.obj944.name.setValue('exack_in')

    self.obj944.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1220.0,480.0,self.obj944)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj944.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj944)
    self.globalAndLocalPostcondition(self.obj944, rootNode)
    self.obj944.postAction( rootNode.CREATE )

    self.obj945=Constant(self)
    self.obj945.isGraphObjectVisual = True

    if(hasattr(self.obj945, '_setHierarchicalLink')):
      self.obj945._setHierarchicalLink(False)

    # Type
    self.obj945.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj945.Type.config = 0

    # name
    self.obj945.name.setValue('2')

    self.obj945.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1008.0,200.0,self.obj945)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj945.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj945)
    self.globalAndLocalPostcondition(self.obj945, rootNode)
    self.obj945.postAction( rootNode.CREATE )

    self.obj946=Constant(self)
    self.obj946.isGraphObjectVisual = True

    if(hasattr(self.obj946, '_setHierarchicalLink')):
      self.obj946._setHierarchicalLink(False)

    # Type
    self.obj946.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj946.Type.config = 0

    # name
    self.obj946.name.setValue('1')

    self.obj946.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(720.0,280.0,self.obj946)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj946.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj946)
    self.globalAndLocalPostcondition(self.obj946, rootNode)
    self.obj946.postAction( rootNode.CREATE )

    self.obj947=Constant(self)
    self.obj947.isGraphObjectVisual = True

    if(hasattr(self.obj947, '_setHierarchicalLink')):
      self.obj947._setHierarchicalLink(False)

    # Type
    self.obj947.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj947.Type.config = 0

    # name
    self.obj947.name.setValue('sh_in')

    self.obj947.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(580.0,640.0,self.obj947)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj947.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj947)
    self.globalAndLocalPostcondition(self.obj947, rootNode)
    self.obj947.postAction( rootNode.CREATE )

    self.obj948=Constant(self)
    self.obj948.isGraphObjectVisual = True

    if(hasattr(self.obj948, '_setHierarchicalLink')):
      self.obj948._setHierarchicalLink(False)

    # Type
    self.obj948.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj948.Type.config = 0

    # name
    self.obj948.name.setValue('S')

    self.obj948.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(380.0,260.0,self.obj948)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj948.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj948)
    self.globalAndLocalPostcondition(self.obj948, rootNode)
    self.obj948.postAction( rootNode.CREATE )

    self.obj949=Constant(self)
    self.obj949.isGraphObjectVisual = True

    if(hasattr(self.obj949, '_setHierarchicalLink')):
      self.obj949._setHierarchicalLink(False)

    # Type
    self.obj949.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj949.Type.config = 0

    # name
    self.obj949.name.setValue('instForInTrans')

    self.obj949.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(351.0,580.0,self.obj949)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj949.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj949)
    self.globalAndLocalPostcondition(self.obj949, rootNode)
    self.obj949.postAction( rootNode.CREATE )

    self.obj950=paired_with(self)
    self.obj950.isGraphObjectVisual = True

    if(hasattr(self.obj950, '_setHierarchicalLink')):
      self.obj950._setHierarchicalLink(False)

    self.obj950.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,232.0,self.obj950)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj950.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj950)
    self.globalAndLocalPostcondition(self.obj950, rootNode)
    self.obj950.postAction( rootNode.CREATE )

    self.obj951=match_contains(self)
    self.obj951.isGraphObjectVisual = True

    if(hasattr(self.obj951, '_setHierarchicalLink')):
      self.obj951._setHierarchicalLink(False)

    self.obj951.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(341.0,33.0,self.obj951)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj951.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj951)
    self.globalAndLocalPostcondition(self.obj951, rootNode)
    self.obj951.postAction( rootNode.CREATE )

    self.obj952=match_contains(self)
    self.obj952.isGraphObjectVisual = True

    if(hasattr(self.obj952, '_setHierarchicalLink')):
      self.obj952._setHierarchicalLink(False)

    self.obj952.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(370.0,21.0,self.obj952)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj952.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj952)
    self.globalAndLocalPostcondition(self.obj952, rootNode)
    self.obj952.postAction( rootNode.CREATE )

    self.obj953=match_contains(self)
    self.obj953.isGraphObjectVisual = True

    if(hasattr(self.obj953, '_setHierarchicalLink')):
      self.obj953._setHierarchicalLink(False)

    self.obj953.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(368.0,10.0,self.obj953)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj953.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj953)
    self.globalAndLocalPostcondition(self.obj953, rootNode)
    self.obj953.postAction( rootNode.CREATE )

    self.obj954=match_contains(self)
    self.obj954.isGraphObjectVisual = True

    if(hasattr(self.obj954, '_setHierarchicalLink')):
      self.obj954._setHierarchicalLink(False)

    self.obj954.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(531.0,8.0,self.obj954)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj954.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj954)
    self.globalAndLocalPostcondition(self.obj954, rootNode)
    self.obj954.postAction( rootNode.CREATE )

    self.obj955=match_contains(self)
    self.obj955.isGraphObjectVisual = True

    if(hasattr(self.obj955, '_setHierarchicalLink')):
      self.obj955._setHierarchicalLink(False)

    self.obj955.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(374.0,117.0,self.obj955)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj955.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj955)
    self.globalAndLocalPostcondition(self.obj955, rootNode)
    self.obj955.postAction( rootNode.CREATE )

    self.obj956=apply_contains(self)
    self.obj956.isGraphObjectVisual = True

    if(hasattr(self.obj956, '_setHierarchicalLink')):
      self.obj956._setHierarchicalLink(False)

    self.obj956.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(267.5,442.0,self.obj956)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj956.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj956)
    self.globalAndLocalPostcondition(self.obj956, rootNode)
    self.obj956.postAction( rootNode.CREATE )

    self.obj957=apply_contains(self)
    self.obj957.isGraphObjectVisual = True

    if(hasattr(self.obj957, '_setHierarchicalLink')):
      self.obj957._setHierarchicalLink(False)

    self.obj957.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(206.5,532.0,self.obj957)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj957.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj957)
    self.globalAndLocalPostcondition(self.obj957, rootNode)
    self.obj957.postAction( rootNode.CREATE )

    self.obj958=apply_contains(self)
    self.obj958.isGraphObjectVisual = True

    if(hasattr(self.obj958, '_setHierarchicalLink')):
      self.obj958._setHierarchicalLink(False)

    self.obj958.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(667.5,492.0,self.obj958)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj958.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj958)
    self.globalAndLocalPostcondition(self.obj958, rootNode)
    self.obj958.postAction( rootNode.CREATE )

    self.obj959=apply_contains(self)
    self.obj959.isGraphObjectVisual = True

    if(hasattr(self.obj959, '_setHierarchicalLink')):
      self.obj959._setHierarchicalLink(False)

    self.obj959.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,422.0,self.obj959)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj959.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj959)
    self.globalAndLocalPostcondition(self.obj959, rootNode)
    self.obj959.postAction( rootNode.CREATE )

    self.obj960=apply_contains(self)
    self.obj960.isGraphObjectVisual = True

    if(hasattr(self.obj960, '_setHierarchicalLink')):
      self.obj960._setHierarchicalLink(False)

    self.obj960.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,372.0,self.obj960)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj960.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj960)
    self.globalAndLocalPostcondition(self.obj960, rootNode)
    self.obj960.postAction( rootNode.CREATE )

    self.obj961=directLink_T(self)
    self.obj961.isGraphObjectVisual = True

    if(hasattr(self.obj961, '_setHierarchicalLink')):
      self.obj961._setHierarchicalLink(False)

    # associationType
    self.obj961.associationType.setValue('channelNames')

    self.obj961.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1026.0,326.0,self.obj961)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj961.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj961)
    self.globalAndLocalPostcondition(self.obj961, rootNode)
    self.obj961.postAction( rootNode.CREATE )

    self.obj962=directLink_T(self)
    self.obj962.isGraphObjectVisual = True

    if(hasattr(self.obj962, '_setHierarchicalLink')):
      self.obj962._setHierarchicalLink(False)

    # associationType
    self.obj962.associationType.setValue('channelNames')

    self.obj962.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1013.0,431.0,self.obj962)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj962.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj962)
    self.globalAndLocalPostcondition(self.obj962, rootNode)
    self.obj962.postAction( rootNode.CREATE )

    self.obj963=directLink_T(self)
    self.obj963.isGraphObjectVisual = True

    if(hasattr(self.obj963, '_setHierarchicalLink')):
      self.obj963._setHierarchicalLink(False)

    # associationType
    self.obj963.associationType.setValue('channelNames')

    self.obj963.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(792.0,521.0,self.obj963)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj963.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj963)
    self.globalAndLocalPostcondition(self.obj963, rootNode)
    self.obj963.postAction( rootNode.CREATE )

    self.obj964=directLink_T(self)
    self.obj964.isGraphObjectVisual = True

    if(hasattr(self.obj964, '_setHierarchicalLink')):
      self.obj964._setHierarchicalLink(False)

    # associationType
    self.obj964.associationType.setValue('channelNames')

    self.obj964.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(572.0,531.0,self.obj964)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj964.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj964)
    self.globalAndLocalPostcondition(self.obj964, rootNode)
    self.obj964.postAction( rootNode.CREATE )

    self.obj965=directLink_S(self)
    self.obj965.isGraphObjectVisual = True

    if(hasattr(self.obj965, '_setHierarchicalLink')):
      self.obj965._setHierarchicalLink(False)

    # associationType
    self.obj965.associationType.setValue('transitions')

    self.obj965.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,83.0,self.obj965)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj965.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj965)
    self.globalAndLocalPostcondition(self.obj965, rootNode)
    self.obj965.postAction( rootNode.CREATE )

    self.obj966=directLink_S(self)
    self.obj966.isGraphObjectVisual = True

    if(hasattr(self.obj966, '_setHierarchicalLink')):
      self.obj966._setHierarchicalLink(False)

    # associationType
    self.obj966.associationType.setValue('dest')

    self.obj966.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(760.0,83.0,self.obj966)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj966.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj966)
    self.globalAndLocalPostcondition(self.obj966, rootNode)
    self.obj966.postAction( rootNode.CREATE )

    self.obj967=directLink_S(self)
    self.obj967.isGraphObjectVisual = True

    if(hasattr(self.obj967, '_setHierarchicalLink')):
      self.obj967._setHierarchicalLink(False)

    # associationType
    self.obj967.associationType.setValue('type')

    self.obj967.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(597.0,124.0,self.obj967)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj967.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj967)
    self.globalAndLocalPostcondition(self.obj967, rootNode)
    self.obj967.postAction( rootNode.CREATE )

    self.obj968=directLink_S(self)
    self.obj968.isGraphObjectVisual = True

    if(hasattr(self.obj968, '_setHierarchicalLink')):
      self.obj968._setHierarchicalLink(False)

    # associationType
    self.obj968.associationType.setValue('owningStateMachine')

    self.obj968.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(850.5,133.0,self.obj968)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj968.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj968)
    self.globalAndLocalPostcondition(self.obj968, rootNode)
    self.obj968.postAction( rootNode.CREATE )

    self.obj969=hasAttribute_S(self)
    self.obj969.isGraphObjectVisual = True

    if(hasattr(self.obj969, '_setHierarchicalLink')):
      self.obj969._setHierarchicalLink(False)

    self.obj969.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(674.5,241.5,self.obj969)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj969.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj969)
    self.globalAndLocalPostcondition(self.obj969, rootNode)
    self.obj969.postAction( rootNode.CREATE )

    self.obj970=hasAttribute_S(self)
    self.obj970.isGraphObjectVisual = True

    if(hasattr(self.obj970, '_setHierarchicalLink')):
      self.obj970._setHierarchicalLink(False)

    self.obj970.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(912.0,206.5,self.obj970)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj970.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj970)
    self.globalAndLocalPostcondition(self.obj970, rootNode)
    self.obj970.postAction( rootNode.CREATE )

    self.obj971=hasAttribute_S(self)
    self.obj971.isGraphObjectVisual = True

    if(hasattr(self.obj971, '_setHierarchicalLink')):
      self.obj971._setHierarchicalLink(False)

    self.obj971.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(317.5,128.5,self.obj971)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj971.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj971)
    self.globalAndLocalPostcondition(self.obj971, rootNode)
    self.obj971.postAction( rootNode.CREATE )

    self.obj972=hasAttribute_T(self)
    self.obj972.isGraphObjectVisual = True

    if(hasattr(self.obj972, '_setHierarchicalLink')):
      self.obj972._setHierarchicalLink(False)

    self.obj972.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,330.5,self.obj972)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj972.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj972)
    self.globalAndLocalPostcondition(self.obj972, rootNode)
    self.obj972.postAction( rootNode.CREATE )

    self.obj973=hasAttribute_T(self)
    self.obj973.isGraphObjectVisual = True

    if(hasattr(self.obj973, '_setHierarchicalLink')):
      self.obj973._setHierarchicalLink(False)

    self.obj973.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,424.5,self.obj973)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj973.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj973)
    self.globalAndLocalPostcondition(self.obj973, rootNode)
    self.obj973.postAction( rootNode.CREATE )

    self.obj974=hasAttribute_T(self)
    self.obj974.isGraphObjectVisual = True

    if(hasattr(self.obj974, '_setHierarchicalLink')):
      self.obj974._setHierarchicalLink(False)

    self.obj974.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1201.0,519.0,self.obj974)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj974.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj974)
    self.globalAndLocalPostcondition(self.obj974, rootNode)
    self.obj974.postAction( rootNode.CREATE )

    self.obj975=hasAttribute_T(self)
    self.obj975.isGraphObjectVisual = True

    if(hasattr(self.obj975, '_setHierarchicalLink')):
      self.obj975._setHierarchicalLink(False)

    self.obj975.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(833.0,592.5,self.obj975)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj975.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj975)
    self.globalAndLocalPostcondition(self.obj975, rootNode)
    self.obj975.postAction( rootNode.CREATE )

    self.obj976=hasAttribute_T(self)
    self.obj976.isGraphObjectVisual = True

    if(hasattr(self.obj976, '_setHierarchicalLink')):
      self.obj976._setHierarchicalLink(False)

    self.obj976.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,422.5,self.obj976)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj976.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj976)
    self.globalAndLocalPostcondition(self.obj976, rootNode)
    self.obj976.postAction( rootNode.CREATE )

    self.obj977=hasAttribute_T(self)
    self.obj977.isGraphObjectVisual = True

    if(hasattr(self.obj977, '_setHierarchicalLink')):
      self.obj977._setHierarchicalLink(False)

    self.obj977.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,542.5,self.obj977)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj977.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj977)
    self.globalAndLocalPostcondition(self.obj977, rootNode)
    self.obj977.postAction( rootNode.CREATE )

    self.obj978=leftExpr(self)
    self.obj978.isGraphObjectVisual = True

    if(hasattr(self.obj978, '_setHierarchicalLink')):
      self.obj978._setHierarchicalLink(False)

    self.obj978.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,176.5,self.obj978)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj978.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj978)
    self.globalAndLocalPostcondition(self.obj978, rootNode)
    self.obj978.postAction( rootNode.CREATE )

    self.obj979=leftExpr(self)
    self.obj979.isGraphObjectVisual = True

    if(hasattr(self.obj979, '_setHierarchicalLink')):
      self.obj979._setHierarchicalLink(False)

    self.obj979.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1487.0,309.5,self.obj979)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj979.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj979)
    self.globalAndLocalPostcondition(self.obj979, rootNode)
    self.obj979.postAction( rootNode.CREATE )

    self.obj980=leftExpr(self)
    self.obj980.isGraphObjectVisual = True

    if(hasattr(self.obj980, '_setHierarchicalLink')):
      self.obj980._setHierarchicalLink(False)

    self.obj980.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1492.0,454.0,self.obj980)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj980.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj980)
    self.globalAndLocalPostcondition(self.obj980, rootNode)
    self.obj980.postAction( rootNode.CREATE )

    self.obj981=leftExpr(self)
    self.obj981.isGraphObjectVisual = True

    if(hasattr(self.obj981, '_setHierarchicalLink')):
      self.obj981._setHierarchicalLink(False)

    self.obj981.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,477.0,self.obj981)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj981.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj981)
    self.globalAndLocalPostcondition(self.obj981, rootNode)
    self.obj981.postAction( rootNode.CREATE )

    self.obj982=leftExpr(self)
    self.obj982.isGraphObjectVisual = True

    if(hasattr(self.obj982, '_setHierarchicalLink')):
      self.obj982._setHierarchicalLink(False)

    self.obj982.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,636.5,self.obj982)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj982.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj982)
    self.globalAndLocalPostcondition(self.obj982, rootNode)
    self.obj982.postAction( rootNode.CREATE )

    self.obj983=leftExpr(self)
    self.obj983.isGraphObjectVisual = True

    if(hasattr(self.obj983, '_setHierarchicalLink')):
      self.obj983._setHierarchicalLink(False)

    self.obj983.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(396.0,356.5,self.obj983)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj983.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj983)
    self.globalAndLocalPostcondition(self.obj983, rootNode)
    self.obj983.postAction( rootNode.CREATE )

    self.obj984=leftExpr(self)
    self.obj984.isGraphObjectVisual = True

    if(hasattr(self.obj984, '_setHierarchicalLink')):
      self.obj984._setHierarchicalLink(False)

    self.obj984.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(346.0,656.5,self.obj984)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj984.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj984)
    self.globalAndLocalPostcondition(self.obj984, rootNode)
    self.obj984.postAction( rootNode.CREATE )

    self.obj985=rightExpr(self)
    self.obj985.isGraphObjectVisual = True

    if(hasattr(self.obj985, '_setHierarchicalLink')):
      self.obj985._setHierarchicalLink(False)

    self.obj985.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(403.5,216.5,self.obj985)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj985.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj985)
    self.globalAndLocalPostcondition(self.obj985, rootNode)
    self.obj985.postAction( rootNode.CREATE )

    self.obj986=rightExpr(self)
    self.obj986.isGraphObjectVisual = True

    if(hasattr(self.obj986, '_setHierarchicalLink')):
      self.obj986._setHierarchicalLink(False)

    self.obj986.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1365.0,243.5,self.obj986)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj986.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj986)
    self.globalAndLocalPostcondition(self.obj986, rootNode)
    self.obj986.postAction( rootNode.CREATE )

    self.obj987=rightExpr(self)
    self.obj987.isGraphObjectVisual = True

    if(hasattr(self.obj987, '_setHierarchicalLink')):
      self.obj987._setHierarchicalLink(False)

    self.obj987.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1424.0,534.0,self.obj987)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj987.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj987)
    self.globalAndLocalPostcondition(self.obj987, rootNode)
    self.obj987.postAction( rootNode.CREATE )

    self.obj988=rightExpr(self)
    self.obj988.isGraphObjectVisual = True

    if(hasattr(self.obj988, '_setHierarchicalLink')):
      self.obj988._setHierarchicalLink(False)

    self.obj988.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1063.0,412.5,self.obj988)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj988.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj988)
    self.globalAndLocalPostcondition(self.obj988, rootNode)
    self.obj988.postAction( rootNode.CREATE )

    self.obj989=rightExpr(self)
    self.obj989.isGraphObjectVisual = True

    if(hasattr(self.obj989, '_setHierarchicalLink')):
      self.obj989._setHierarchicalLink(False)

    self.obj989.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(796.0,676.5,self.obj989)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj989.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj989)
    self.globalAndLocalPostcondition(self.obj989, rootNode)
    self.obj989.postAction( rootNode.CREATE )

    self.obj990=rightExpr(self)
    self.obj990.isGraphObjectVisual = True

    if(hasattr(self.obj990, '_setHierarchicalLink')):
      self.obj990._setHierarchicalLink(False)

    self.obj990.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(556.0,376.5,self.obj990)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj990.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj990)
    self.globalAndLocalPostcondition(self.obj990, rootNode)
    self.obj990.postAction( rootNode.CREATE )

    self.obj991=rightExpr(self)
    self.obj991.isGraphObjectVisual = True

    if(hasattr(self.obj991, '_setHierarchicalLink')):
      self.obj991._setHierarchicalLink(False)

    self.obj991.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(456.0,666.5,self.obj991)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj991.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj991)
    self.globalAndLocalPostcondition(self.obj991, rootNode)
    self.obj991.postAction( rootNode.CREATE )

    self.obj992=hasArgs(self)
    self.obj992.isGraphObjectVisual = True

    if(hasattr(self.obj992, '_setHierarchicalLink')):
      self.obj992._setHierarchicalLink(False)

    self.obj992.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(932.0,344.0,self.obj992)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj992.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj992)
    self.globalAndLocalPostcondition(self.obj992, rootNode)
    self.obj992.postAction( rootNode.CREATE )

    self.obj993=hasArgs(self)
    self.obj993.isGraphObjectVisual = True

    if(hasattr(self.obj993, '_setHierarchicalLink')):
      self.obj993._setHierarchicalLink(False)

    self.obj993.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1029.0,314.0,self.obj993)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj993.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj993)
    self.globalAndLocalPostcondition(self.obj993, rootNode)
    self.obj993.postAction( rootNode.CREATE )

    self.obj994=hasArgs(self)
    self.obj994.isGraphObjectVisual = True

    if(hasattr(self.obj994, '_setHierarchicalLink')):
      self.obj994._setHierarchicalLink(False)

    self.obj994.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1111.0,312.0,self.obj994)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj994.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj994)
    self.globalAndLocalPostcondition(self.obj994, rootNode)
    self.obj994.postAction( rootNode.CREATE )

    self.obj995=hasArgs(self)
    self.obj995.isGraphObjectVisual = True

    if(hasattr(self.obj995, '_setHierarchicalLink')):
      self.obj995._setHierarchicalLink(False)

    self.obj995.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(574.0,334.0,self.obj995)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj995.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj995)
    self.globalAndLocalPostcondition(self.obj995, rootNode)
    self.obj995.postAction( rootNode.CREATE )

    self.obj996=hasArgs(self)
    self.obj996.isGraphObjectVisual = True

    if(hasattr(self.obj996, '_setHierarchicalLink')):
      self.obj996._setHierarchicalLink(False)

    self.obj996.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(644.0,324.0,self.obj996)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj996.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj996)
    self.globalAndLocalPostcondition(self.obj996, rootNode)
    self.obj996.postAction( rootNode.CREATE )

    # Connections for obj912 (graphObject_: Obj809) of type MatchModel
    self.drawConnections(
(self.obj912,self.obj950,[138.0, 51.0, 140.5, 232.0],"true", 2),
(self.obj912,self.obj951,[138.0, 51.0, 341.0, 33.0],"true", 2),
(self.obj912,self.obj952,[138.0, 51.0, 370.0, 21.0],"true", 2),
(self.obj912,self.obj953,[138.0, 51.0, 368.0, 10.0],"true", 2),
(self.obj912,self.obj954,[138.0, 51.0, 531.0, 8.0],"true", 2),
(self.obj912,self.obj955,[138.0, 51.0, 374.0, 117.0],"true", 2) )
    # Connections for obj913 (graphObject_: Obj810) of type ApplyModel
    self.drawConnections(
(self.obj913,self.obj956,[143.0, 413.0, 267.5, 442.0],"true", 2),
(self.obj913,self.obj957,[143.0, 413.0, 206.5, 532.0],"true", 2),
(self.obj913,self.obj958,[143.0, 413.0, 667.5, 492.0],"true", 2),
(self.obj913,self.obj959,[143.0, 413.0, 747.5, 422.0],"true", 2),
(self.obj913,self.obj960,[143.0, 413.0, 747.5, 372.0],"true", 2) )
    # Connections for obj914 (graphObject_: Obj811) named entrypoint1
    self.drawConnections(
(self.obj914,self.obj968,[950.0, 83.0, 850.5, 133.0],"true", 2),
(self.obj914,self.obj970,[950.0, 83.0, 912.0, 206.5],"true", 2) )
    # Connections for obj915 (graphObject_: Obj812) named transition1
    self.drawConnections(
(self.obj915,self.obj966,[570.0, 83.0, 760.0, 83.0],"true", 2),
(self.obj915,self.obj967,[570.0, 83.0, 597.0, 124.0],"true", 2) )
    # Connections for obj916 (graphObject_: Obj813) named statemachine1
    self.drawConnections(
(self.obj916,self.obj969,[790.0, 183.0, 674.5, 241.5],"true", 2) )
    # Connections for obj917 (graphObject_: Obj814) named state1
    self.drawConnections(
(self.obj917,self.obj965,[350.0, 83.0, 460.0, 83.0],"true", 2),
(self.obj917,self.obj971,[350.0, 83.0, 317.5, 128.5],"true", 2) )
    # Connections for obj918 (graphObject_: Obj815) named in1_1
    self.drawConnections(
 )
    # Connections for obj919 (graphObject_: Obj816) named name1
    self.drawConnections(
(self.obj919,self.obj972,[1352.0, 331.0, 1400.0, 330.5],"true", 2) )
    # Connections for obj920 (graphObject_: Obj817) named name2
    self.drawConnections(
(self.obj920,self.obj973,[1352.0, 431.0, 1400.0, 424.5],"true", 2) )
    # Connections for obj921 (graphObject_: Obj818) named name3
    self.drawConnections(
(self.obj921,self.obj974,[1192.0, 571.0, 1201.0, 519.0],"true", 2) )
    # Connections for obj922 (graphObject_: Obj819) named name4
    self.drawConnections(
(self.obj922,self.obj975,[752.0, 591.0, 833.0, 592.5],"true", 2) )
    # Connections for obj923 (graphObject_: Obj820) named inst1
    self.drawConnections(
(self.obj923,self.obj961,[392.0, 471.0, 1026.0, 326.0],"true", 2),
(self.obj923,self.obj962,[392.0, 471.0, 1013.0, 431.0],"true", 2),
(self.obj923,self.obj963,[392.0, 471.0, 792.0, 521.0],"true", 2),
(self.obj923,self.obj964,[392.0, 471.0, 572.0, 531.0],"true", 2),
(self.obj923,self.obj976,[392.0, 471.0, 353.0, 422.5],"true", 2),
(self.obj923,self.obj977,[392.0, 471.0, 353.0, 542.5],"true", 2) )
    # Connections for obj924 (graphObject_: Obj821) named name
    self.drawConnections(
 )
    # Connections for obj925 (graphObject_: Obj822) named name
    self.drawConnections(
 )
    # Connections for obj926 (graphObject_: Obj823) named isComposite
    self.drawConnections(
 )
    # Connections for obj927 (graphObject_: Obj824) named literal
    self.drawConnections(
 )
    # Connections for obj928 (graphObject_: Obj825) named literal
    self.drawConnections(
 )
    # Connections for obj929 (graphObject_: Obj826) named literal
    self.drawConnections(
 )
    # Connections for obj930 (graphObject_: Obj827) named literal
    self.drawConnections(
 )
    # Connections for obj931 (graphObject_: Obj828) named name
    self.drawConnections(
 )
    # Connections for obj932 (graphObject_: Obj829) named pivot
    self.drawConnections(
 )
    # Connections for obj933 (graphObject_: Obj830) named eq1
    self.drawConnections(
(self.obj933,self.obj978,[433.0, 179.0, 359.0, 176.5],"true", 2),
(self.obj933,self.obj985,[433.0, 179.0, 403.5, 216.5],"true", 2) )
    # Connections for obj934 (graphObject_: Obj831) named eq2
    self.drawConnections(
(self.obj934,self.obj979,[1498.0, 259.0, 1487.0, 309.5],"true", 2),
(self.obj934,self.obj986,[1498.0, 259.0, 1365.0, 243.5],"true", 2) )
    # Connections for obj935 (graphObject_: Obj832) named eq3
    self.drawConnections(
(self.obj935,self.obj980,[1498.0, 499.0, 1492.0, 454.0],"true", 2),
(self.obj935,self.obj987,[1498.0, 499.0, 1424.0, 534.0],"true", 2) )
    # Connections for obj936 (graphObject_: Obj833) named eq4
    self.drawConnections(
(self.obj936,self.obj981,[1012.0, 488.0, 1100.0, 477.0],"true", 2),
(self.obj936,self.obj988,[1012.0, 488.0, 1063.0, 412.5],"true", 2) )
    # Connections for obj937 (graphObject_: Obj834) named eq5
    self.drawConnections(
(self.obj937,self.obj982,[878.0, 679.0, 896.0, 636.5],"true", 2),
(self.obj937,self.obj989,[878.0, 679.0, 796.0, 676.5],"true", 2) )
    # Connections for obj938 (graphObject_: Obj835) named eq6
    self.drawConnections(
(self.obj938,self.obj983,[478.0, 379.0, 396.0, 356.5],"true", 2),
(self.obj938,self.obj990,[478.0, 379.0, 556.0, 376.5],"true", 2) )
    # Connections for obj939 (graphObject_: Obj836) named eq7
    self.drawConnections(
(self.obj939,self.obj991,[378.0, 699.0, 456.0, 666.5],"true", 2),
(self.obj939,self.obj984,[378.0, 699.0, 346.0, 656.5],"true", 2) )
    # Connections for obj940 (graphObject_: Obj837) named concat1
    self.drawConnections(
(self.obj940,self.obj992,[1074.0, 389.0, 932.0, 344.0],"true", 2),
(self.obj940,self.obj993,[1074.0, 389.0, 1029.0, 314.0],"true", 2),
(self.obj940,self.obj994,[1074.0, 389.0, 1111.0, 312.0],"true", 2) )
    # Connections for obj941 (graphObject_: Obj838) named concat2
    self.drawConnections(
(self.obj941,self.obj995,[634.0, 374.0, 574.0, 334.0],"true", 2),
(self.obj941,self.obj996,[634.0, 374.0, 644.0, 324.0],"true", 2) )
    # Connections for obj942 (graphObject_: Obj839) named true
    self.drawConnections(
 )
    # Connections for obj943 (graphObject_: Obj840) named exit_in
    self.drawConnections(
 )
    # Connections for obj944 (graphObject_: Obj841) named exack_in
    self.drawConnections(
 )
    # Connections for obj945 (graphObject_: Obj842) named 2
    self.drawConnections(
 )
    # Connections for obj946 (graphObject_: Obj843) named 1
    self.drawConnections(
 )
    # Connections for obj947 (graphObject_: Obj844) named sh_in
    self.drawConnections(
 )
    # Connections for obj948 (graphObject_: Obj845) named S
    self.drawConnections(
 )
    # Connections for obj949 (graphObject_: Obj846) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj950 (graphObject_: Obj847) of type paired_with
    self.drawConnections(
(self.obj950,self.obj913,[140.5, 232.0, 143.0, 413.0],"true", 2) )
    # Connections for obj951 (graphObject_: Obj848) of type match_contains
    self.drawConnections(
(self.obj951,self.obj917,[341.0, 33.0, 350.0, 83.0],"true", 2) )
    # Connections for obj952 (graphObject_: Obj849) of type match_contains
    self.drawConnections(
(self.obj952,self.obj915,[370.0, 21.0, 570.0, 83.0],"true", 2) )
    # Connections for obj953 (graphObject_: Obj850) of type match_contains
    self.drawConnections(
(self.obj953,self.obj914,[368.0, 10.0, 950.0, 83.0],"true", 2) )
    # Connections for obj954 (graphObject_: Obj851) of type match_contains
    self.drawConnections(
(self.obj954,self.obj916,[531.0, 8.0, 790.0, 183.0],"true", 2) )
    # Connections for obj955 (graphObject_: Obj852) of type match_contains
    self.drawConnections(
(self.obj955,self.obj918,[374.0, 117.0, 610.0, 183.0],"true", 2) )
    # Connections for obj956 (graphObject_: Obj853) of type apply_contains
    self.drawConnections(
(self.obj956,self.obj923,[267.5, 442.0, 392.0, 471.0],"true", 2) )
    # Connections for obj957 (graphObject_: Obj854) of type apply_contains
    self.drawConnections(
(self.obj957,self.obj922,[206.5, 532.0, 752.0, 591.0],"true", 2) )
    # Connections for obj958 (graphObject_: Obj855) of type apply_contains
    self.drawConnections(
(self.obj958,self.obj921,[667.5, 492.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj959 (graphObject_: Obj856) of type apply_contains
    self.drawConnections(
(self.obj959,self.obj920,[747.5, 422.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj960 (graphObject_: Obj857) of type apply_contains
    self.drawConnections(
(self.obj960,self.obj919,[747.5, 372.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj961 (graphObject_: Obj858) of type directLink_T
    self.drawConnections(
(self.obj961,self.obj919,[1026.0, 326.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj962 (graphObject_: Obj859) of type directLink_T
    self.drawConnections(
(self.obj962,self.obj920,[1013.0, 431.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj963 (graphObject_: Obj860) of type directLink_T
    self.drawConnections(
(self.obj963,self.obj921,[792.0, 521.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj964 (graphObject_: Obj861) of type directLink_T
    self.drawConnections(
(self.obj964,self.obj922,[572.0, 531.0, 752.0, 591.0],"true", 2) )
    # Connections for obj965 (graphObject_: Obj862) of type directLink_S
    self.drawConnections(
(self.obj965,self.obj915,[460.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj966 (graphObject_: Obj863) of type directLink_S
    self.drawConnections(
(self.obj966,self.obj914,[760.0, 83.0, 950.0, 83.0],"true", 2) )
    # Connections for obj967 (graphObject_: Obj864) of type directLink_S
    self.drawConnections(
(self.obj967,self.obj918,[597.0, 124.0, 610.0, 183.0],"true", 2) )
    # Connections for obj968 (graphObject_: Obj865) of type directLink_S
    self.drawConnections(
(self.obj968,self.obj916,[850.5, 133.0, 790.0, 183.0],"true", 2) )
    # Connections for obj969 (graphObject_: Obj866) of type hasAttribute_S
    self.drawConnections(
(self.obj969,self.obj925,[674.5, 241.5, 674.0, 274.0],"true", 2) )
    # Connections for obj970 (graphObject_: Obj867) of type hasAttribute_S
    self.drawConnections(
(self.obj970,self.obj924,[912.0, 206.5, 994.0, 254.0],"true", 2) )
    # Connections for obj971 (graphObject_: Obj868) of type hasAttribute_S
    self.drawConnections(
(self.obj971,self.obj926,[317.5, 128.5, 285.0, 174.0],"true", 2) )
    # Connections for obj972 (graphObject_: Obj869) of type hasAttribute_T
    self.drawConnections(
(self.obj972,self.obj927,[1400.0, 330.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj973 (graphObject_: Obj870) of type hasAttribute_T
    self.drawConnections(
(self.obj973,self.obj928,[1400.0, 424.5, 1494.0, 414.0],"true", 2) )
    # Connections for obj974 (graphObject_: Obj871) of type hasAttribute_T
    self.drawConnections(
(self.obj974,self.obj929,[1201.0, 519.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj975 (graphObject_: Obj872) of type hasAttribute_T
    self.drawConnections(
(self.obj975,self.obj930,[833.0, 592.5, 914.0, 594.0],"true", 2) )
    # Connections for obj976 (graphObject_: Obj873) of type hasAttribute_T
    self.drawConnections(
(self.obj976,self.obj931,[353.0, 422.5, 314.0, 374.0],"true", 2) )
    # Connections for obj977 (graphObject_: Obj874) of type hasAttribute_T
    self.drawConnections(
(self.obj977,self.obj932,[353.0, 542.5, 314.0, 614.0],"true", 2) )
    # Connections for obj978 (graphObject_: Obj875) of type leftExpr
    self.drawConnections(
(self.obj978,self.obj926,[359.0, 176.5, 285.0, 174.0],"true", 2) )
    # Connections for obj979 (graphObject_: Obj876) of type leftExpr
    self.drawConnections(
(self.obj979,self.obj927,[1487.0, 309.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj980 (graphObject_: Obj877) of type leftExpr
    self.drawConnections(
(self.obj980,self.obj928,[1492.0, 454.0, 1494.0, 414.0],"true", 2) )
    # Connections for obj981 (graphObject_: Obj878) of type leftExpr
    self.drawConnections(
(self.obj981,self.obj929,[1100.0, 477.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj982 (graphObject_: Obj879) of type leftExpr
    self.drawConnections(
(self.obj982,self.obj930,[896.0, 636.5, 914.0, 594.0],"true", 2) )
    # Connections for obj983 (graphObject_: Obj880) of type leftExpr
    self.drawConnections(
(self.obj983,self.obj931,[396.0, 356.5, 314.0, 374.0],"true", 2) )
    # Connections for obj984 (graphObject_: Obj881) of type leftExpr
    self.drawConnections(
(self.obj984,self.obj932,[346.0, 656.5, 314.0, 614.0],"true", 2) )
    # Connections for obj985 (graphObject_: Obj882) of type rightExpr
    self.drawConnections(
(self.obj985,self.obj942,[403.5, 216.5, 374.0, 254.0],"true", 2) )
    # Connections for obj986 (graphObject_: Obj883) of type rightExpr
    self.drawConnections(
(self.obj986,self.obj943,[1365.0, 243.5, 1334.0, 241.0],"true", 2) )
    # Connections for obj987 (graphObject_: Obj884) of type rightExpr
    self.drawConnections(
(self.obj987,self.obj944,[1424.0, 534.0, 1354.0, 514.0],"true", 2) )
    # Connections for obj988 (graphObject_: Obj885) of type rightExpr
    self.drawConnections(
(self.obj988,self.obj940,[1063.0, 412.5, 1074.0, 389.0],"true", 2) )
    # Connections for obj989 (graphObject_: Obj886) of type rightExpr
    self.drawConnections(
(self.obj989,self.obj947,[796.0, 676.5, 714.0, 674.0],"true", 2) )
    # Connections for obj990 (graphObject_: Obj887) of type rightExpr
    self.drawConnections(
(self.obj990,self.obj941,[556.0, 376.5, 634.0, 374.0],"true", 2) )
    # Connections for obj991 (graphObject_: Obj888) of type rightExpr
    self.drawConnections(
(self.obj991,self.obj949,[456.0, 666.5, 485.0, 614.0],"true", 2) )
    # Connections for obj992 (graphObject_: Obj889) of type hasArgs
    self.drawConnections(
(self.obj992,self.obj946,[932.0, 344.0, 854.0, 314.0],"true", 2) )
    # Connections for obj993 (graphObject_: Obj890) of type hasArgs
    self.drawConnections(
(self.obj993,self.obj924,[1029.0, 314.0, 994.0, 254.0],"true", 2) )
    # Connections for obj994 (graphObject_: Obj891) of type hasArgs
    self.drawConnections(
(self.obj994,self.obj945,[1111.0, 312.0, 1142.0, 234.0],"true", 2) )
    # Connections for obj995 (graphObject_: Obj892) of type hasArgs
    self.drawConnections(
(self.obj995,self.obj948,[574.0, 334.0, 514.0, 294.0],"true", 2) )
    # Connections for obj996 (graphObject_: Obj893) of type hasArgs
    self.drawConnections(
(self.obj996,self.obj925,[644.0, 324.0, 674.0, 274.0],"true", 2) )

newfunction = Transition2Inst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
