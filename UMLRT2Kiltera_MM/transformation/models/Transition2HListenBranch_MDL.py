"""
__Transition2HListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:22:12 2015
______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from Trigger_S import *
from Signal import *
from Vertex import *
from Transition import *
from StateMachine import *
from State import *
from Trigger_T import *
from Listen import *
from ListenBranch import *
from Inst import *
from Seq import *
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
from graph_Vertex import *
from graph_Seq import *
from graph_Transition import *
from graph_Signal import *
from graph_paired_with import *
from graph_Listen import *
from graph_State import *
from graph_Equation import *
from graph_backward_link import *
from graph_StateMachine import *
from graph_rightExpr import *
from graph_Trigger_T import *
from graph_Trigger_S import *
from graph_Inst import *
from graph_hasAttribute_T import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_ApplyModel import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_hasAttribute_S import *
from graph_match_contains import *
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

def Transition2HListenBranch_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2HListenBranch')
    # --- ASG attributes over ---


    self.obj894=MatchModel(self)
    self.obj894.isGraphObjectVisual = True

    if(hasattr(self.obj894, '_setHierarchicalLink')):
      self.obj894._setHierarchicalLink(False)

    self.obj894.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj894)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj894.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj894)
    self.globalAndLocalPostcondition(self.obj894, rootNode)
    self.obj894.postAction( rootNode.CREATE )

    self.obj895=ApplyModel(self)
    self.obj895.isGraphObjectVisual = True

    if(hasattr(self.obj895, '_setHierarchicalLink')):
      self.obj895._setHierarchicalLink(False)

    self.obj895.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,380.0,self.obj895)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj895.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj895)
    self.globalAndLocalPostcondition(self.obj895, rootNode)
    self.obj895.postAction( rootNode.CREATE )

    self.obj896=Trigger_S(self)
    self.obj896.isGraphObjectVisual = True

    if(hasattr(self.obj896, '_setHierarchicalLink')):
      self.obj896._setHierarchicalLink(False)

    # classtype
    self.obj896.classtype.setValue('Trigger_S')

    # cardinality
    self.obj896.cardinality.setValue('1')

    # name
    self.obj896.name.setValue('triggerS1')

    self.obj896.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(480.0,140.0,self.obj896)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj896.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj896)
    self.globalAndLocalPostcondition(self.obj896, rootNode)
    self.obj896.postAction( rootNode.CREATE )

    self.obj897=Signal(self)
    self.obj897.isGraphObjectVisual = True

    if(hasattr(self.obj897, '_setHierarchicalLink')):
      self.obj897._setHierarchicalLink(False)

    # name
    self.obj897.name.setValue('signal1')

    # classtype
    self.obj897.classtype.setValue('Signal')

    # cardinality
    self.obj897.cardinality.setValue('1')

    self.obj897.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(720.0,140.0,self.obj897)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj897.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj897)
    self.globalAndLocalPostcondition(self.obj897, rootNode)
    self.obj897.postAction( rootNode.CREATE )

    self.obj898=Vertex(self)
    self.obj898.isGraphObjectVisual = True

    if(hasattr(self.obj898, '_setHierarchicalLink')):
      self.obj898._setHierarchicalLink(False)

    # name
    self.obj898.name.setValue('vertex1')

    # classtype
    self.obj898.classtype.setValue('Vertex')

    # cardinality
    self.obj898.cardinality.setValue('+')

    self.obj898.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(400.0,40.0,self.obj898)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj898.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj898)
    self.globalAndLocalPostcondition(self.obj898, rootNode)
    self.obj898.postAction( rootNode.CREATE )

    self.obj899=Transition(self)
    self.obj899.isGraphObjectVisual = True

    if(hasattr(self.obj899, '_setHierarchicalLink')):
      self.obj899._setHierarchicalLink(False)

    # name
    self.obj899.name.setValue('transition1')

    # classtype
    self.obj899.classtype.setValue('Transition')

    # cardinality
    self.obj899.cardinality.setValue('+')

    self.obj899.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(200.0,40.0,self.obj899)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj899.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj899)
    self.globalAndLocalPostcondition(self.obj899, rootNode)
    self.obj899.postAction( rootNode.CREATE )

    self.obj900=StateMachine(self)
    self.obj900.isGraphObjectVisual = True

    if(hasattr(self.obj900, '_setHierarchicalLink')):
      self.obj900._setHierarchicalLink(False)

    # name
    self.obj900.name.setValue('statemachine1')

    # classtype
    self.obj900.classtype.setValue('StateMachine')

    # cardinality
    self.obj900.cardinality.setValue('+')

    self.obj900.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(600.0,40.0,self.obj900)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj900.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj900)
    self.globalAndLocalPostcondition(self.obj900, rootNode)
    self.obj900.postAction( rootNode.CREATE )

    self.obj901=State(self)
    self.obj901.isGraphObjectVisual = True

    if(hasattr(self.obj901, '_setHierarchicalLink')):
      self.obj901._setHierarchicalLink(False)

    # name
    self.obj901.name.setValue('state1')

    # classtype
    self.obj901.classtype.setValue('State')

    # cardinality
    self.obj901.cardinality.setValue('1')

    self.obj901.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(800.0,40.0,self.obj901)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj901.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj901)
    self.globalAndLocalPostcondition(self.obj901, rootNode)
    self.obj901.postAction( rootNode.CREATE )

    self.obj902=State(self)
    self.obj902.isGraphObjectVisual = True

    if(hasattr(self.obj902, '_setHierarchicalLink')):
      self.obj902._setHierarchicalLink(False)

    # name
    self.obj902.name.setValue('state2')

    # classtype
    self.obj902.classtype.setValue('State')

    # cardinality
    self.obj902.cardinality.setValue('+')

    self.obj902.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(280.0,140.0,self.obj902)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj902.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj902)
    self.globalAndLocalPostcondition(self.obj902, rootNode)
    self.obj902.postAction( rootNode.CREATE )

    self.obj903=Trigger_T(self)
    self.obj903.isGraphObjectVisual = True

    if(hasattr(self.obj903, '_setHierarchicalLink')):
      self.obj903._setHierarchicalLink(False)

    # classtype
    self.obj903.classtype.setValue('Trigger_T')

    # cardinality
    self.obj903.cardinality.setValue('1')

    # name
    self.obj903.name.setValue('triggerT1')

    self.obj903.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(780.0,440.0,self.obj903)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj903.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj903)
    self.globalAndLocalPostcondition(self.obj903, rootNode)
    self.obj903.postAction( rootNode.CREATE )

    self.obj904=Listen(self)
    self.obj904.isGraphObjectVisual = True

    if(hasattr(self.obj904, '_setHierarchicalLink')):
      self.obj904._setHierarchicalLink(False)

    # classtype
    self.obj904.classtype.setValue('Listen')

    # cardinality
    self.obj904.cardinality.setValue('1')

    # name
    self.obj904.name.setValue('listen1')

    self.obj904.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,440.0,self.obj904)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj904.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj904)
    self.globalAndLocalPostcondition(self.obj904, rootNode)
    self.obj904.postAction( rootNode.CREATE )

    self.obj905=Listen(self)
    self.obj905.isGraphObjectVisual = True

    if(hasattr(self.obj905, '_setHierarchicalLink')):
      self.obj905._setHierarchicalLink(False)

    # classtype
    self.obj905.classtype.setValue('Listen')

    # cardinality
    self.obj905.cardinality.setValue('1')

    # name
    self.obj905.name.setValue('listen2')

    self.obj905.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(780.0,540.0,self.obj905)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj905.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj905)
    self.globalAndLocalPostcondition(self.obj905, rootNode)
    self.obj905.postAction( rootNode.CREATE )

    self.obj906=ListenBranch(self)
    self.obj906.isGraphObjectVisual = True

    if(hasattr(self.obj906, '_setHierarchicalLink')):
      self.obj906._setHierarchicalLink(False)

    # classtype
    self.obj906.classtype.setValue('ListenBranch')

    # cardinality
    self.obj906.cardinality.setValue('1')

    # name
    self.obj906.name.setValue('listenbranch1')

    self.obj906.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(380.0,440.0,self.obj906)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj906.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj906)
    self.globalAndLocalPostcondition(self.obj906, rootNode)
    self.obj906.postAction( rootNode.CREATE )

    self.obj907=ListenBranch(self)
    self.obj907.isGraphObjectVisual = True

    if(hasattr(self.obj907, '_setHierarchicalLink')):
      self.obj907._setHierarchicalLink(False)

    # classtype
    self.obj907.classtype.setValue('ListenBranch')

    # cardinality
    self.obj907.cardinality.setValue('1')

    # name
    self.obj907.name.setValue('listenbranch2')

    self.obj907.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(860.0,640.0,self.obj907)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj907.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj907)
    self.globalAndLocalPostcondition(self.obj907, rootNode)
    self.obj907.postAction( rootNode.CREATE )

    self.obj908=Inst(self)
    self.obj908.isGraphObjectVisual = True

    if(hasattr(self.obj908, '_setHierarchicalLink')):
      self.obj908._setHierarchicalLink(False)

    # classtype
    self.obj908.classtype.setValue('Inst')

    # cardinality
    self.obj908.cardinality.setValue('1')

    # name
    self.obj908.name.setValue('inst1')

    self.obj908.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(580.0,720.0,self.obj908)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj908.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj908)
    self.globalAndLocalPostcondition(self.obj908, rootNode)
    self.obj908.postAction( rootNode.CREATE )

    self.obj909=Seq(self)
    self.obj909.isGraphObjectVisual = True

    if(hasattr(self.obj909, '_setHierarchicalLink')):
      self.obj909._setHierarchicalLink(False)

    # name
    self.obj909.name.setValue('seq1')

    # classtype
    self.obj909.classtype.setValue('Seq')

    # cardinality
    self.obj909.cardinality.setValue('1')

    self.obj909.graphClass_= graph_Seq
    if self.genGraphics:
       new_obj = graph_Seq(580.0,440.0,self.obj909)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Seq", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj909.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj909)
    self.globalAndLocalPostcondition(self.obj909, rootNode)
    self.obj909.postAction( rootNode.CREATE )

    self.obj910=Attribute(self)
    self.obj910.isGraphObjectVisual = True

    if(hasattr(self.obj910, '_setHierarchicalLink')):
      self.obj910._setHierarchicalLink(False)

    # Type
    self.obj910.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj910.Type.config = 0

    # name
    self.obj910.name.setValue('name')

    self.obj910.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(920.0,140.0,self.obj910)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj910.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj910)
    self.globalAndLocalPostcondition(self.obj910, rootNode)
    self.obj910.postAction( rootNode.CREATE )

    self.obj911=Attribute(self)
    self.obj911.isGraphObjectVisual = True

    if(hasattr(self.obj911, '_setHierarchicalLink')):
      self.obj911._setHierarchicalLink(False)

    # Type
    self.obj911.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj911.Type.config = 0

    # name
    self.obj911.name.setValue('isComposite')

    self.obj911.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(300.0,240.0,self.obj911)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj911.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj911)
    self.globalAndLocalPostcondition(self.obj911, rootNode)
    self.obj911.postAction( rootNode.CREATE )

    self.obj912=Attribute(self)
    self.obj912.isGraphObjectVisual = True

    if(hasattr(self.obj912, '_setHierarchicalLink')):
      self.obj912._setHierarchicalLink(False)

    # Type
    self.obj912.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj912.Type.config = 0

    # name
    self.obj912.name.setValue('channel')

    self.obj912.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(460.0,360.0,self.obj912)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj912.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj912)
    self.globalAndLocalPostcondition(self.obj912, rootNode)
    self.obj912.postAction( rootNode.CREATE )

    self.obj913=Attribute(self)
    self.obj913.isGraphObjectVisual = True

    if(hasattr(self.obj913, '_setHierarchicalLink')):
      self.obj913._setHierarchicalLink(False)

    # Type
    self.obj913.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj913.Type.config = 0

    # name
    self.obj913.name.setValue('channel')

    self.obj913.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,360.0,self.obj913)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj913.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj913)
    self.globalAndLocalPostcondition(self.obj913, rootNode)
    self.obj913.postAction( rootNode.CREATE )

    self.obj914=Attribute(self)
    self.obj914.isGraphObjectVisual = True

    if(hasattr(self.obj914, '_setHierarchicalLink')):
      self.obj914._setHierarchicalLink(False)

    # Type
    self.obj914.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj914.Type.config = 0

    # name
    self.obj914.name.setValue('pivot')

    self.obj914.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(280.0,540.0,self.obj914)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj914.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj914)
    self.globalAndLocalPostcondition(self.obj914, rootNode)
    self.obj914.postAction( rootNode.CREATE )

    self.obj915=Attribute(self)
    self.obj915.isGraphObjectVisual = True

    if(hasattr(self.obj915, '_setHierarchicalLink')):
      self.obj915._setHierarchicalLink(False)

    # Type
    self.obj915.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj915.Type.config = 0

    # name
    self.obj915.name.setValue('channel')

    self.obj915.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(960.0,740.0,self.obj915)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj915.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj915)
    self.globalAndLocalPostcondition(self.obj915, rootNode)
    self.obj915.postAction( rootNode.CREATE )

    self.obj916=Attribute(self)
    self.obj916.isGraphObjectVisual = True

    if(hasattr(self.obj916, '_setHierarchicalLink')):
      self.obj916._setHierarchicalLink(False)

    # Type
    self.obj916.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj916.Type.config = 0

    # name
    self.obj916.name.setValue('pivot')

    self.obj916.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,820.0,self.obj916)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj916.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj916)
    self.globalAndLocalPostcondition(self.obj916, rootNode)
    self.obj916.postAction( rootNode.CREATE )

    self.obj917=Equation(self)
    self.obj917.isGraphObjectVisual = True

    if(hasattr(self.obj917, '_setHierarchicalLink')):
      self.obj917._setHierarchicalLink(False)

    # name
    self.obj917.name.setValue('eq1')

    self.obj917.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,320.0,self.obj917)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj917.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj917)
    self.globalAndLocalPostcondition(self.obj917, rootNode)
    self.obj917.postAction( rootNode.CREATE )

    self.obj918=Equation(self)
    self.obj918.isGraphObjectVisual = True

    if(hasattr(self.obj918, '_setHierarchicalLink')):
      self.obj918._setHierarchicalLink(False)

    # name
    self.obj918.name.setValue('eq2')

    self.obj918.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,284.0,self.obj918)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj918.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj918)
    self.globalAndLocalPostcondition(self.obj918, rootNode)
    self.obj918.postAction( rootNode.CREATE )

    self.obj919=Equation(self)
    self.obj919.isGraphObjectVisual = True

    if(hasattr(self.obj919, '_setHierarchicalLink')):
      self.obj919._setHierarchicalLink(False)

    # name
    self.obj919.name.setValue('eq3')

    self.obj919.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,280.0,self.obj919)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj919.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj919)
    self.globalAndLocalPostcondition(self.obj919, rootNode)
    self.obj919.postAction( rootNode.CREATE )

    self.obj920=Equation(self)
    self.obj920.isGraphObjectVisual = True

    if(hasattr(self.obj920, '_setHierarchicalLink')):
      self.obj920._setHierarchicalLink(False)

    # name
    self.obj920.name.setValue('eq4')

    self.obj920.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,620.0,self.obj920)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj920.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj920)
    self.globalAndLocalPostcondition(self.obj920, rootNode)
    self.obj920.postAction( rootNode.CREATE )

    self.obj921=Equation(self)
    self.obj921.isGraphObjectVisual = True

    if(hasattr(self.obj921, '_setHierarchicalLink')):
      self.obj921._setHierarchicalLink(False)

    # name
    self.obj921.name.setValue('eq5')

    self.obj921.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(900.0,820.0,self.obj921)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj921.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj921)
    self.globalAndLocalPostcondition(self.obj921, rootNode)
    self.obj921.postAction( rootNode.CREATE )

    self.obj922=Equation(self)
    self.obj922.isGraphObjectVisual = True

    if(hasattr(self.obj922, '_setHierarchicalLink')):
      self.obj922._setHierarchicalLink(False)

    # name
    self.obj922.name.setValue('eq6')

    self.obj922.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(571.0,820.0,self.obj922)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj922.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj922)
    self.globalAndLocalPostcondition(self.obj922, rootNode)
    self.obj922.postAction( rootNode.CREATE )

    self.obj923=Constant(self)
    self.obj923.isGraphObjectVisual = True

    if(hasattr(self.obj923, '_setHierarchicalLink')):
      self.obj923._setHierarchicalLink(False)

    # Type
    self.obj923.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj923.Type.config = 0

    # name
    self.obj923.name.setValue('true')

    self.obj923.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,240.0,self.obj923)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj923.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj923)
    self.globalAndLocalPostcondition(self.obj923, rootNode)
    self.obj923.postAction( rootNode.CREATE )

    self.obj924=Constant(self)
    self.obj924.isGraphObjectVisual = True

    if(hasattr(self.obj924, '_setHierarchicalLink')):
      self.obj924._setHierarchicalLink(False)

    # Type
    self.obj924.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj924.Type.config = 0

    # name
    self.obj924.name.setValue('exit_in')

    self.obj924.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,360.0,self.obj924)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj924.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj924)
    self.globalAndLocalPostcondition(self.obj924, rootNode)
    self.obj924.postAction( rootNode.CREATE )

    self.obj925=Constant(self)
    self.obj925.isGraphObjectVisual = True

    if(hasattr(self.obj925, '_setHierarchicalLink')):
      self.obj925._setHierarchicalLink(False)

    # Type
    self.obj925.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj925.Type.config = 0

    # name
    self.obj925.name.setValue('listenhproc')

    self.obj925.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(140.0,540.0,self.obj925)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj925.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj925)
    self.globalAndLocalPostcondition(self.obj925, rootNode)
    self.obj925.postAction( rootNode.CREATE )

    self.obj926=Constant(self)
    self.obj926.isGraphObjectVisual = True

    if(hasattr(self.obj926, '_setHierarchicalLink')):
      self.obj926._setHierarchicalLink(False)

    # Type
    self.obj926.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj926.Type.config = 0

    # name
    self.obj926.name.setValue('exack_in')

    self.obj926.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(820.0,740.0,self.obj926)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj926.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj926)
    self.globalAndLocalPostcondition(self.obj926, rootNode)
    self.obj926.postAction( rootNode.CREATE )

    self.obj927=Constant(self)
    self.obj927.isGraphObjectVisual = True

    if(hasattr(self.obj927, '_setHierarchicalLink')):
      self.obj927._setHierarchicalLink(False)

    # Type
    self.obj927.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj927.Type.config = 0

    # name
    self.obj927.name.setValue('instfortrans')

    self.obj927.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,820.0,self.obj927)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj927.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj927)
    self.globalAndLocalPostcondition(self.obj927, rootNode)
    self.obj927.postAction( rootNode.CREATE )

    self.obj928=paired_with(self)
    self.obj928.isGraphObjectVisual = True

    if(hasattr(self.obj928, '_setHierarchicalLink')):
      self.obj928._setHierarchicalLink(False)

    self.obj928.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,192.0,self.obj928)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj928.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj928)
    self.globalAndLocalPostcondition(self.obj928, rootNode)
    self.obj928.postAction( rootNode.CREATE )

    self.obj929=match_contains(self)
    self.obj929.isGraphObjectVisual = True

    if(hasattr(self.obj929, '_setHierarchicalLink')):
      self.obj929._setHierarchicalLink(False)

    self.obj929.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(254.0,67.0,self.obj929)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj929.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj929)
    self.globalAndLocalPostcondition(self.obj929, rootNode)
    self.obj929.postAction( rootNode.CREATE )

    self.obj930=match_contains(self)
    self.obj930.isGraphObjectVisual = True

    if(hasattr(self.obj930, '_setHierarchicalLink')):
      self.obj930._setHierarchicalLink(False)

    self.obj930.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,67.0,self.obj930)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj930.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj930)
    self.globalAndLocalPostcondition(self.obj930, rootNode)
    self.obj930.postAction( rootNode.CREATE )

    self.obj931=match_contains(self)
    self.obj931.isGraphObjectVisual = True

    if(hasattr(self.obj931, '_setHierarchicalLink')):
      self.obj931._setHierarchicalLink(False)

    self.obj931.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(454.0,67.0,self.obj931)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj931.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj931)
    self.globalAndLocalPostcondition(self.obj931, rootNode)
    self.obj931.postAction( rootNode.CREATE )

    self.obj932=match_contains(self)
    self.obj932.isGraphObjectVisual = True

    if(hasattr(self.obj932, '_setHierarchicalLink')):
      self.obj932._setHierarchicalLink(False)

    self.obj932.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(554.0,67.0,self.obj932)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj932.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj932)
    self.globalAndLocalPostcondition(self.obj932, rootNode)
    self.obj932.postAction( rootNode.CREATE )

    self.obj933=match_contains(self)
    self.obj933.isGraphObjectVisual = True

    if(hasattr(self.obj933, '_setHierarchicalLink')):
      self.obj933._setHierarchicalLink(False)

    self.obj933.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(294.0,117.0,self.obj933)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj933.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj933)
    self.globalAndLocalPostcondition(self.obj933, rootNode)
    self.obj933.postAction( rootNode.CREATE )

    self.obj934=match_contains(self)
    self.obj934.isGraphObjectVisual = True

    if(hasattr(self.obj934, '_setHierarchicalLink')):
      self.obj934._setHierarchicalLink(False)

    self.obj934.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,117.0,self.obj934)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj934.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj934)
    self.globalAndLocalPostcondition(self.obj934, rootNode)
    self.obj934.postAction( rootNode.CREATE )

    self.obj935=match_contains(self)
    self.obj935.isGraphObjectVisual = True

    if(hasattr(self.obj935, '_setHierarchicalLink')):
      self.obj935._setHierarchicalLink(False)

    self.obj935.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(514.0,117.0,self.obj935)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj935.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj935)
    self.globalAndLocalPostcondition(self.obj935, rootNode)
    self.obj935.postAction( rootNode.CREATE )

    self.obj936=apply_contains(self)
    self.obj936.isGraphObjectVisual = True

    if(hasattr(self.obj936, '_setHierarchicalLink')):
      self.obj936._setHierarchicalLink(False)

    self.obj936.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,452.0,self.obj936)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj936.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj936)
    self.globalAndLocalPostcondition(self.obj936, rootNode)
    self.obj936.postAction( rootNode.CREATE )

    self.obj937=apply_contains(self)
    self.obj937.isGraphObjectVisual = True

    if(hasattr(self.obj937, '_setHierarchicalLink')):
      self.obj937._setHierarchicalLink(False)

    self.obj937.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(347.5,452.0,self.obj937)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj937.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj937)
    self.globalAndLocalPostcondition(self.obj937, rootNode)
    self.obj937.postAction( rootNode.CREATE )

    self.obj938=apply_contains(self)
    self.obj938.isGraphObjectVisual = True

    if(hasattr(self.obj938, '_setHierarchicalLink')):
      self.obj938._setHierarchicalLink(False)

    self.obj938.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,452.0,self.obj938)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj938.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj938)
    self.globalAndLocalPostcondition(self.obj938, rootNode)
    self.obj938.postAction( rootNode.CREATE )

    self.obj939=apply_contains(self)
    self.obj939.isGraphObjectVisual = True

    if(hasattr(self.obj939, '_setHierarchicalLink')):
      self.obj939._setHierarchicalLink(False)

    self.obj939.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,452.0,self.obj939)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj939.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj939)
    self.globalAndLocalPostcondition(self.obj939, rootNode)
    self.obj939.postAction( rootNode.CREATE )

    self.obj940=apply_contains(self)
    self.obj940.isGraphObjectVisual = True

    if(hasattr(self.obj940, '_setHierarchicalLink')):
      self.obj940._setHierarchicalLink(False)

    self.obj940.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,502.0,self.obj940)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj940.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj940)
    self.globalAndLocalPostcondition(self.obj940, rootNode)
    self.obj940.postAction( rootNode.CREATE )

    self.obj941=apply_contains(self)
    self.obj941.isGraphObjectVisual = True

    if(hasattr(self.obj941, '_setHierarchicalLink')):
      self.obj941._setHierarchicalLink(False)

    self.obj941.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(587.5,552.0,self.obj941)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj941.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj941)
    self.globalAndLocalPostcondition(self.obj941, rootNode)
    self.obj941.postAction( rootNode.CREATE )

    self.obj942=apply_contains(self)
    self.obj942.isGraphObjectVisual = True

    if(hasattr(self.obj942, '_setHierarchicalLink')):
      self.obj942._setHierarchicalLink(False)

    self.obj942.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,592.0,self.obj942)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj942.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj942)
    self.globalAndLocalPostcondition(self.obj942, rootNode)
    self.obj942.postAction( rootNode.CREATE )

    self.obj943=directLink_T(self)
    self.obj943.isGraphObjectVisual = True

    if(hasattr(self.obj943, '_setHierarchicalLink')):
      self.obj943._setHierarchicalLink(False)

    # associationType
    self.obj943.associationType.setValue('branches')

    self.obj943.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.0,491.0,self.obj943)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj943.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj943)
    self.globalAndLocalPostcondition(self.obj943, rootNode)
    self.obj943.postAction( rootNode.CREATE )

    self.obj944=directLink_T(self)
    self.obj944.isGraphObjectVisual = True

    if(hasattr(self.obj944, '_setHierarchicalLink')):
      self.obj944._setHierarchicalLink(False)

    # associationType
    self.obj944.associationType.setValue('p')

    self.obj944.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj944)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj944.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj944)
    self.globalAndLocalPostcondition(self.obj944, rootNode)
    self.obj944.postAction( rootNode.CREATE )

    self.obj945=directLink_T(self)
    self.obj945.isGraphObjectVisual = True

    if(hasattr(self.obj945, '_setHierarchicalLink')):
      self.obj945._setHierarchicalLink(False)

    # associationType
    self.obj945.associationType.setValue('p')

    self.obj945.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,491.0,self.obj945)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj945.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj945)
    self.globalAndLocalPostcondition(self.obj945, rootNode)
    self.obj945.postAction( rootNode.CREATE )

    self.obj946=directLink_T(self)
    self.obj946.isGraphObjectVisual = True

    if(hasattr(self.obj946, '_setHierarchicalLink')):
      self.obj946._setHierarchicalLink(False)

    # associationType
    self.obj946.associationType.setValue('p')

    self.obj946.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,541.0,self.obj946)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj946.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj946)
    self.globalAndLocalPostcondition(self.obj946, rootNode)
    self.obj946.postAction( rootNode.CREATE )

    self.obj947=directLink_T(self)
    self.obj947.isGraphObjectVisual = True

    if(hasattr(self.obj947, '_setHierarchicalLink')):
      self.obj947._setHierarchicalLink(False)

    # associationType
    self.obj947.associationType.setValue('branches')

    self.obj947.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(992.0,641.0,self.obj947)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj947.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj947)
    self.globalAndLocalPostcondition(self.obj947, rootNode)
    self.obj947.postAction( rootNode.CREATE )

    self.obj948=directLink_T(self)
    self.obj948.isGraphObjectVisual = True

    if(hasattr(self.obj948, '_setHierarchicalLink')):
      self.obj948._setHierarchicalLink(False)

    # associationType
    self.obj948.associationType.setValue('p')

    self.obj948.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(806.0,693.0,self.obj948)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj948.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj948)
    self.globalAndLocalPostcondition(self.obj948, rootNode)
    self.obj948.postAction( rootNode.CREATE )

    self.obj949=directLink_S(self)
    self.obj949.isGraphObjectVisual = True

    if(hasattr(self.obj949, '_setHierarchicalLink')):
      self.obj949._setHierarchicalLink(False)

    # associationType
    self.obj949.associationType.setValue('src')

    self.obj949.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,83.0,self.obj949)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj949.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj949)
    self.globalAndLocalPostcondition(self.obj949, rootNode)
    self.obj949.postAction( rootNode.CREATE )

    self.obj950=directLink_S(self)
    self.obj950.isGraphObjectVisual = True

    if(hasattr(self.obj950, '_setHierarchicalLink')):
      self.obj950._setHierarchicalLink(False)

    # associationType
    self.obj950.associationType.setValue('owningStateMachine')

    self.obj950.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,83.0,self.obj950)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj950.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj950)
    self.globalAndLocalPostcondition(self.obj950, rootNode)
    self.obj950.postAction( rootNode.CREATE )

    self.obj951=directLink_S(self)
    self.obj951.isGraphObjectVisual = True

    if(hasattr(self.obj951, '_setHierarchicalLink')):
      self.obj951._setHierarchicalLink(False)

    # associationType
    self.obj951.associationType.setValue('states')

    self.obj951.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(870.0,83.0,self.obj951)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj951.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj951)
    self.globalAndLocalPostcondition(self.obj951, rootNode)
    self.obj951.postAction( rootNode.CREATE )

    self.obj952=directLink_S(self)
    self.obj952.isGraphObjectVisual = True

    if(hasattr(self.obj952, '_setHierarchicalLink')):
      self.obj952._setHierarchicalLink(False)

    # associationType
    self.obj952.associationType.setValue('triggers')

    self.obj952.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(489.0,128.0,self.obj952)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj952.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj952)
    self.globalAndLocalPostcondition(self.obj952, rootNode)
    self.obj952.postAction( rootNode.CREATE )

    self.obj953=directLink_S(self)
    self.obj953.isGraphObjectVisual = True

    if(hasattr(self.obj953, '_setHierarchicalLink')):
      self.obj953._setHierarchicalLink(False)

    # associationType
    self.obj953.associationType.setValue('signal')

    self.obj953.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,183.0,self.obj953)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj953.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj953)
    self.globalAndLocalPostcondition(self.obj953, rootNode)
    self.obj953.postAction( rootNode.CREATE )

    self.obj954=directLink_S(self)
    self.obj954.isGraphObjectVisual = True

    if(hasattr(self.obj954, '_setHierarchicalLink')):
      self.obj954._setHierarchicalLink(False)

    # associationType
    self.obj954.associationType.setValue('outgoingTransitions')

    self.obj954.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(430.0,148.0,self.obj954)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj954.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj954)
    self.globalAndLocalPostcondition(self.obj954, rootNode)
    self.obj954.postAction( rootNode.CREATE )

    self.obj955=backward_link(self)
    self.obj955.isGraphObjectVisual = True

    if(hasattr(self.obj955, '_setHierarchicalLink')):
      self.obj955._setHierarchicalLink(False)

    # type
    self.obj955.type.setValue('ruleDef')

    self.obj955.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(460.0,339.0,self.obj955)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj955.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj955)
    self.globalAndLocalPostcondition(self.obj955, rootNode)
    self.obj955.postAction( rootNode.CREATE )

    self.obj956=backward_link(self)
    self.obj956.isGraphObjectVisual = True

    if(hasattr(self.obj956, '_setHierarchicalLink')):
      self.obj956._setHierarchicalLink(False)

    # type
    self.obj956.type.setValue('ruleDef')

    self.obj956.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(561.0,427.0,self.obj956)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj956.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj956)
    self.globalAndLocalPostcondition(self.obj956, rootNode)
    self.obj956.postAction( rootNode.CREATE )

    self.obj957=hasAttribute_S(self)
    self.obj957.isGraphObjectVisual = True

    if(hasattr(self.obj957, '_setHierarchicalLink')):
      self.obj957._setHierarchicalLink(False)

    self.obj957.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(972.0,178.5,self.obj957)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj957.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj957)
    self.globalAndLocalPostcondition(self.obj957, rootNode)
    self.obj957.postAction( rootNode.CREATE )

    self.obj958=hasAttribute_S(self)
    self.obj958.isGraphObjectVisual = True

    if(hasattr(self.obj958, '_setHierarchicalLink')):
      self.obj958._setHierarchicalLink(False)

    self.obj958.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(440.0,231.5,self.obj958)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj958.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj958)
    self.globalAndLocalPostcondition(self.obj958, rootNode)
    self.obj958.postAction( rootNode.CREATE )

    self.obj959=hasAttribute_T(self)
    self.obj959.isGraphObjectVisual = True

    if(hasattr(self.obj959, '_setHierarchicalLink')):
      self.obj959._setHierarchicalLink(False)

    self.obj959.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(573.0,442.5,self.obj959)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj959.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj959)
    self.globalAndLocalPostcondition(self.obj959, rootNode)
    self.obj959.postAction( rootNode.CREATE )

    self.obj960=hasAttribute_T(self)
    self.obj960.isGraphObjectVisual = True

    if(hasattr(self.obj960, '_setHierarchicalLink')):
      self.obj960._setHierarchicalLink(False)

    self.obj960.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(963.0,442.5,self.obj960)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj960.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj960)
    self.globalAndLocalPostcondition(self.obj960, rootNode)
    self.obj960.postAction( rootNode.CREATE )

    self.obj961=hasAttribute_T(self)
    self.obj961.isGraphObjectVisual = True

    if(hasattr(self.obj961, '_setHierarchicalLink')):
      self.obj961._setHierarchicalLink(False)

    self.obj961.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(383.0,532.5,self.obj961)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj961.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj961)
    self.globalAndLocalPostcondition(self.obj961, rootNode)
    self.obj961.postAction( rootNode.CREATE )

    self.obj962=hasAttribute_T(self)
    self.obj962.isGraphObjectVisual = True

    if(hasattr(self.obj962, '_setHierarchicalLink')):
      self.obj962._setHierarchicalLink(False)

    self.obj962.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1063.0,732.5,self.obj962)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj962.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj962)
    self.globalAndLocalPostcondition(self.obj962, rootNode)
    self.obj962.postAction( rootNode.CREATE )

    self.obj963=hasAttribute_T(self)
    self.obj963.isGraphObjectVisual = True

    if(hasattr(self.obj963, '_setHierarchicalLink')):
      self.obj963._setHierarchicalLink(False)

    self.obj963.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(763.0,812.5,self.obj963)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj963.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj963)
    self.globalAndLocalPostcondition(self.obj963, rootNode)
    self.obj963.postAction( rootNode.CREATE )

    self.obj964=leftExpr(self)
    self.obj964.isGraphObjectVisual = True

    if(hasattr(self.obj964, '_setHierarchicalLink')):
      self.obj964._setHierarchicalLink(False)

    self.obj964.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(401.0,321.5,self.obj964)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj964.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj964)
    self.globalAndLocalPostcondition(self.obj964, rootNode)
    self.obj964.postAction( rootNode.CREATE )

    self.obj965=leftExpr(self)
    self.obj965.isGraphObjectVisual = True

    if(hasattr(self.obj965, '_setHierarchicalLink')):
      self.obj965._setHierarchicalLink(False)

    self.obj965.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(616.0,358.5,self.obj965)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj965.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj965)
    self.globalAndLocalPostcondition(self.obj965, rootNode)
    self.obj965.postAction( rootNode.CREATE )

    self.obj966=leftExpr(self)
    self.obj966.isGraphObjectVisual = True

    if(hasattr(self.obj966, '_setHierarchicalLink')):
      self.obj966._setHierarchicalLink(False)

    self.obj966.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,356.5,self.obj966)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj966.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj966)
    self.globalAndLocalPostcondition(self.obj966, rootNode)
    self.obj966.postAction( rootNode.CREATE )

    self.obj967=leftExpr(self)
    self.obj967.isGraphObjectVisual = True

    if(hasattr(self.obj967, '_setHierarchicalLink')):
      self.obj967._setHierarchicalLink(False)

    self.obj967.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(386.0,616.5,self.obj967)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj967.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj967)
    self.globalAndLocalPostcondition(self.obj967, rootNode)
    self.obj967.postAction( rootNode.CREATE )

    self.obj968=leftExpr(self)
    self.obj968.isGraphObjectVisual = True

    if(hasattr(self.obj968, '_setHierarchicalLink')):
      self.obj968._setHierarchicalLink(False)

    self.obj968.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1066.0,816.5,self.obj968)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj968.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj968)
    self.globalAndLocalPostcondition(self.obj968, rootNode)
    self.obj968.postAction( rootNode.CREATE )

    self.obj969=leftExpr(self)
    self.obj969.isGraphObjectVisual = True

    if(hasattr(self.obj969, '_setHierarchicalLink')):
      self.obj969._setHierarchicalLink(False)

    self.obj969.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(781.5,856.5,self.obj969)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj969.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj969)
    self.globalAndLocalPostcondition(self.obj969, rootNode)
    self.obj969.postAction( rootNode.CREATE )

    self.obj970=rightExpr(self)
    self.obj970.isGraphObjectVisual = True

    if(hasattr(self.obj970, '_setHierarchicalLink')):
      self.obj970._setHierarchicalLink(False)

    self.obj970.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(295.0,312.5,self.obj970)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj970.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj970)
    self.globalAndLocalPostcondition(self.obj970, rootNode)
    self.obj970.postAction( rootNode.CREATE )

    self.obj971=rightExpr(self)
    self.obj971.isGraphObjectVisual = True

    if(hasattr(self.obj971, '_setHierarchicalLink')):
      self.obj971._setHierarchicalLink(False)

    self.obj971.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(648.0,251.5,self.obj971)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj971.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj971)
    self.globalAndLocalPostcondition(self.obj971, rootNode)
    self.obj971.postAction( rootNode.CREATE )

    self.obj972=rightExpr(self)
    self.obj972.isGraphObjectVisual = True

    if(hasattr(self.obj972, '_setHierarchicalLink')):
      self.obj972._setHierarchicalLink(False)

    self.obj972.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(886.0,356.5,self.obj972)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj972.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj972)
    self.globalAndLocalPostcondition(self.obj972, rootNode)
    self.obj972.postAction( rootNode.CREATE )

    self.obj973=rightExpr(self)
    self.obj973.isGraphObjectVisual = True

    if(hasattr(self.obj973, '_setHierarchicalLink')):
      self.obj973._setHierarchicalLink(False)

    self.obj973.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(316.0,616.5,self.obj973)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj973.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj973)
    self.globalAndLocalPostcondition(self.obj973, rootNode)
    self.obj973.postAction( rootNode.CREATE )

    self.obj974=rightExpr(self)
    self.obj974.isGraphObjectVisual = True

    if(hasattr(self.obj974, '_setHierarchicalLink')):
      self.obj974._setHierarchicalLink(False)

    self.obj974.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,816.5,self.obj974)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj974.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj974)
    self.globalAndLocalPostcondition(self.obj974, rootNode)
    self.obj974.postAction( rootNode.CREATE )

    self.obj975=rightExpr(self)
    self.obj975.isGraphObjectVisual = True

    if(hasattr(self.obj975, '_setHierarchicalLink')):
      self.obj975._setHierarchicalLink(False)

    self.obj975.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(631.5,856.5,self.obj975)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj975.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj975)
    self.globalAndLocalPostcondition(self.obj975, rootNode)
    self.obj975.postAction( rootNode.CREATE )

    # Connections for obj894 (graphObject_: Obj727) of type MatchModel
    self.drawConnections(
(self.obj894,self.obj928,[138.0, 51.0, 140.5, 192.0],"true", 2),
(self.obj894,self.obj929,[138.0, 51.0, 254.0, 67.0],"true", 2),
(self.obj894,self.obj930,[138.0, 51.0, 354.0, 67.0],"true", 2),
(self.obj894,self.obj931,[138.0, 51.0, 454.0, 67.0],"true", 2),
(self.obj894,self.obj932,[138.0, 51.0, 554.0, 67.0],"true", 2),
(self.obj894,self.obj933,[138.0, 51.0, 294.0, 117.0],"true", 2),
(self.obj894,self.obj934,[138.0, 51.0, 394.0, 117.0],"true", 2),
(self.obj894,self.obj935,[138.0, 51.0, 514.0, 117.0],"true", 2) )
    # Connections for obj895 (graphObject_: Obj728) of type ApplyModel
    self.drawConnections(
(self.obj895,self.obj936,[143.0, 413.0, 247.5, 452.0],"true", 2),
(self.obj895,self.obj937,[143.0, 413.0, 347.5, 452.0],"true", 2),
(self.obj895,self.obj938,[143.0, 413.0, 447.5, 452.0],"true", 2),
(self.obj895,self.obj939,[143.0, 413.0, 547.5, 452.0],"true", 2),
(self.obj895,self.obj940,[143.0, 413.0, 547.5, 502.0],"true", 2),
(self.obj895,self.obj941,[143.0, 413.0, 587.5, 552.0],"true", 2),
(self.obj895,self.obj942,[143.0, 413.0, 447.5, 592.0],"true", 2) )
    # Connections for obj896 (graphObject_: Obj729) named triggerS1
    self.drawConnections(
(self.obj896,self.obj953,[650.0, 183.0, 670.0, 183.0],"true", 2) )
    # Connections for obj897 (graphObject_: Obj730) named signal1
    self.drawConnections(
(self.obj897,self.obj957,[890.0, 183.0, 972.0, 178.5],"true", 2) )
    # Connections for obj898 (graphObject_: Obj731) named vertex1
    self.drawConnections(
(self.obj898,self.obj950,[570.0, 83.0, 670.0, 83.0],"true", 2) )
    # Connections for obj899 (graphObject_: Obj732) named transition1
    self.drawConnections(
(self.obj899,self.obj949,[370.0, 83.0, 470.0, 83.0],"true", 2),
(self.obj899,self.obj952,[370.0, 83.0, 489.0, 128.0],"true", 2) )
    # Connections for obj900 (graphObject_: Obj733) named statemachine1
    self.drawConnections(
(self.obj900,self.obj951,[770.0, 83.0, 870.0, 83.0],"true", 2) )
    # Connections for obj901 (graphObject_: Obj734) named state1
    self.drawConnections(
 )
    # Connections for obj902 (graphObject_: Obj735) named state2
    self.drawConnections(
(self.obj902,self.obj954,[450.0, 183.0, 430.0, 148.0],"true", 2),
(self.obj902,self.obj958,[450.0, 183.0, 440.0, 231.5],"true", 2) )
    # Connections for obj903 (graphObject_: Obj736) named triggerT1
    self.drawConnections(
(self.obj903,self.obj960,[952.0, 491.0, 963.0, 442.5],"true", 2) )
    # Connections for obj904 (graphObject_: Obj737) named listen1
    self.drawConnections(
(self.obj904,self.obj943,[352.0, 491.0, 452.0, 491.0],"true", 2),
(self.obj904,self.obj961,[352.0, 491.0, 383.0, 532.5],"true", 2),
(self.obj904,self.obj955,[352.0, 491.0, 460.0, 339.0],"true", 2) )
    # Connections for obj905 (graphObject_: Obj738) named listen2
    self.drawConnections(
(self.obj905,self.obj947,[952.0, 591.0, 992.0, 641.0],"true", 2) )
    # Connections for obj906 (graphObject_: Obj739) named listenbranch1
    self.drawConnections(
(self.obj906,self.obj944,[552.0, 491.0, 652.0, 491.0],"true", 2),
(self.obj906,self.obj959,[552.0, 491.0, 573.0, 442.5],"true", 2) )
    # Connections for obj907 (graphObject_: Obj740) named listenbranch2
    self.drawConnections(
(self.obj907,self.obj962,[1032.0, 691.0, 1063.0, 732.5],"true", 2),
(self.obj907,self.obj948,[1032.0, 691.0, 806.0, 693.0],"true", 2) )
    # Connections for obj908 (graphObject_: Obj741) named inst1
    self.drawConnections(
(self.obj908,self.obj963,[752.0, 771.0, 763.0, 812.5],"true", 2),
(self.obj908,self.obj956,[752.0, 771.0, 561.0, 427.0],"true", 2) )
    # Connections for obj909 (graphObject_: Obj742) named seq1
    self.drawConnections(
(self.obj909,self.obj945,[752.0, 491.0, 852.0, 491.0],"true", 2),
(self.obj909,self.obj946,[752.0, 491.0, 852.0, 541.0],"true", 2) )
    # Connections for obj910 (graphObject_: Obj743) named name
    self.drawConnections(
 )
    # Connections for obj911 (graphObject_: Obj744) named isComposite
    self.drawConnections(
 )
    # Connections for obj912 (graphObject_: Obj745) named channel
    self.drawConnections(
 )
    # Connections for obj913 (graphObject_: Obj746) named channel
    self.drawConnections(
 )
    # Connections for obj914 (graphObject_: Obj747) named pivot
    self.drawConnections(
 )
    # Connections for obj915 (graphObject_: Obj748) named channel
    self.drawConnections(
 )
    # Connections for obj916 (graphObject_: Obj749) named pivot
    self.drawConnections(
 )
    # Connections for obj917 (graphObject_: Obj750) named eq1
    self.drawConnections(
(self.obj917,self.obj964,[358.0, 359.0, 401.0, 321.5],"true", 2),
(self.obj917,self.obj970,[358.0, 359.0, 295.0, 312.5],"true", 2) )
    # Connections for obj918 (graphObject_: Obj751) named eq2
    self.drawConnections(
(self.obj918,self.obj965,[638.0, 323.0, 616.0, 358.5],"true", 2),
(self.obj918,self.obj971,[638.0, 323.0, 648.0, 251.5],"true", 2) )
    # Connections for obj919 (graphObject_: Obj752) named eq3
    self.drawConnections(
(self.obj919,self.obj972,[938.0, 319.0, 886.0, 356.5],"true", 2),
(self.obj919,self.obj966,[938.0, 319.0, 956.0, 356.5],"true", 2) )
    # Connections for obj920 (graphObject_: Obj753) named eq4
    self.drawConnections(
(self.obj920,self.obj967,[358.0, 659.0, 386.0, 616.5],"true", 2),
(self.obj920,self.obj973,[358.0, 659.0, 316.0, 616.5],"true", 2) )
    # Connections for obj921 (graphObject_: Obj754) named eq5
    self.drawConnections(
(self.obj921,self.obj968,[1038.0, 859.0, 1066.0, 816.5],"true", 2),
(self.obj921,self.obj974,[1038.0, 859.0, 996.0, 816.5],"true", 2) )
    # Connections for obj922 (graphObject_: Obj755) named eq6
    self.drawConnections(
(self.obj922,self.obj969,[709.0, 859.0, 781.5, 856.5],"true", 2),
(self.obj922,self.obj975,[709.0, 859.0, 631.5, 856.5],"true", 2) )
    # Connections for obj923 (graphObject_: Obj756) named true
    self.drawConnections(
 )
    # Connections for obj924 (graphObject_: Obj757) named exit_in
    self.drawConnections(
 )
    # Connections for obj925 (graphObject_: Obj758) named listenhproc
    self.drawConnections(
 )
    # Connections for obj926 (graphObject_: Obj759) named exack_in
    self.drawConnections(
 )
    # Connections for obj927 (graphObject_: Obj760) named instfortrans
    self.drawConnections(
 )
    # Connections for obj928 (graphObject_: Obj761) of type paired_with
    self.drawConnections(
(self.obj928,self.obj895,[140.5, 192.0, 143.0, 413.0],"true", 2) )
    # Connections for obj929 (graphObject_: Obj762) of type match_contains
    self.drawConnections(
(self.obj929,self.obj899,[254.0, 67.0, 370.0, 83.0],"true", 2) )
    # Connections for obj930 (graphObject_: Obj763) of type match_contains
    self.drawConnections(
(self.obj930,self.obj898,[354.0, 67.0, 570.0, 83.0],"true", 2) )
    # Connections for obj931 (graphObject_: Obj764) of type match_contains
    self.drawConnections(
(self.obj931,self.obj900,[454.0, 67.0, 770.0, 83.0],"true", 2) )
    # Connections for obj932 (graphObject_: Obj765) of type match_contains
    self.drawConnections(
(self.obj932,self.obj901,[554.0, 67.0, 970.0, 83.0],"true", 2) )
    # Connections for obj933 (graphObject_: Obj766) of type match_contains
    self.drawConnections(
(self.obj933,self.obj902,[294.0, 117.0, 450.0, 183.0],"true", 2) )
    # Connections for obj934 (graphObject_: Obj767) of type match_contains
    self.drawConnections(
(self.obj934,self.obj896,[394.0, 117.0, 650.0, 183.0],"true", 2) )
    # Connections for obj935 (graphObject_: Obj768) of type match_contains
    self.drawConnections(
(self.obj935,self.obj897,[514.0, 117.0, 890.0, 183.0],"true", 2) )
    # Connections for obj936 (graphObject_: Obj769) of type apply_contains
    self.drawConnections(
(self.obj936,self.obj904,[247.5, 452.0, 352.0, 491.0],"true", 2) )
    # Connections for obj937 (graphObject_: Obj770) of type apply_contains
    self.drawConnections(
(self.obj937,self.obj906,[347.5, 452.0, 552.0, 491.0],"true", 2) )
    # Connections for obj938 (graphObject_: Obj771) of type apply_contains
    self.drawConnections(
(self.obj938,self.obj909,[447.5, 452.0, 752.0, 491.0],"true", 2) )
    # Connections for obj939 (graphObject_: Obj772) of type apply_contains
    self.drawConnections(
(self.obj939,self.obj903,[547.5, 452.0, 952.0, 491.0],"true", 2) )
    # Connections for obj940 (graphObject_: Obj773) of type apply_contains
    self.drawConnections(
(self.obj940,self.obj905,[547.5, 502.0, 952.0, 591.0],"true", 2) )
    # Connections for obj941 (graphObject_: Obj774) of type apply_contains
    self.drawConnections(
(self.obj941,self.obj907,[587.5, 552.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj942 (graphObject_: Obj775) of type apply_contains
    self.drawConnections(
(self.obj942,self.obj908,[447.5, 592.0, 752.0, 771.0],"true", 2) )
    # Connections for obj943 (graphObject_: Obj776) of type directLink_T
    self.drawConnections(
(self.obj943,self.obj906,[452.0, 491.0, 552.0, 491.0],"true", 2) )
    # Connections for obj944 (graphObject_: Obj777) of type directLink_T
    self.drawConnections(
(self.obj944,self.obj909,[652.0, 491.0, 752.0, 491.0],"true", 2) )
    # Connections for obj945 (graphObject_: Obj778) of type directLink_T
    self.drawConnections(
(self.obj945,self.obj903,[852.0, 491.0, 952.0, 491.0],"true", 2) )
    # Connections for obj946 (graphObject_: Obj779) of type directLink_T
    self.drawConnections(
(self.obj946,self.obj905,[852.0, 541.0, 952.0, 591.0],"true", 2) )
    # Connections for obj947 (graphObject_: Obj780) of type directLink_T
    self.drawConnections(
(self.obj947,self.obj907,[992.0, 641.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj948 (graphObject_: Obj781) of type directLink_T
    self.drawConnections(
(self.obj948,self.obj908,[806.0, 693.0, 752.0, 771.0],"true", 2) )
    # Connections for obj949 (graphObject_: Obj782) of type directLink_S
    self.drawConnections(
(self.obj949,self.obj898,[470.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj950 (graphObject_: Obj783) of type directLink_S
    self.drawConnections(
(self.obj950,self.obj900,[670.0, 83.0, 770.0, 83.0],"true", 2) )
    # Connections for obj951 (graphObject_: Obj784) of type directLink_S
    self.drawConnections(
(self.obj951,self.obj901,[870.0, 83.0, 970.0, 83.0],"true", 2) )
    # Connections for obj952 (graphObject_: Obj785) of type directLink_S
    self.drawConnections(
(self.obj952,self.obj896,[470.0, 133.0, 650.0, 183.0],"true", 2) )
    # Connections for obj953 (graphObject_: Obj786) of type directLink_S
    self.drawConnections(
(self.obj953,self.obj897,[670.0, 183.0, 890.0, 183.0],"true", 2) )
    # Connections for obj954 (graphObject_: Obj787) of type directLink_S
    self.drawConnections(
(self.obj954,self.obj899,[400.0, 133.0, 370.0, 83.0],"true", 2) )
    # Connections for obj955 (graphObject_: Obj788) of type backward_link
    self.drawConnections(
(self.obj955,self.obj902,[401.0, 337.0, 450.0, 183.0],"true", 2) )
    # Connections for obj956 (graphObject_: Obj789) of type backward_link
    self.drawConnections(
(self.obj956,self.obj899,[561.0, 427.0, 370.0, 83.0],"true", 2) )
    # Connections for obj957 (graphObject_: Obj790) of type hasAttribute_S
    self.drawConnections(
(self.obj957,self.obj910,[972.0, 178.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj958 (graphObject_: Obj791) of type hasAttribute_S
    self.drawConnections(
(self.obj958,self.obj911,[462.0, 228.5, 434.0, 274.0],"true", 2) )
    # Connections for obj959 (graphObject_: Obj792) of type hasAttribute_T
    self.drawConnections(
(self.obj959,self.obj912,[573.0, 442.5, 594.0, 394.0],"true", 2) )
    # Connections for obj960 (graphObject_: Obj793) of type hasAttribute_T
    self.drawConnections(
(self.obj960,self.obj913,[963.0, 442.5, 974.0, 394.0],"true", 2) )
    # Connections for obj961 (graphObject_: Obj794) of type hasAttribute_T
    self.drawConnections(
(self.obj961,self.obj914,[383.0, 532.5, 414.0, 574.0],"true", 2) )
    # Connections for obj962 (graphObject_: Obj795) of type hasAttribute_T
    self.drawConnections(
(self.obj962,self.obj915,[1063.0, 732.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj963 (graphObject_: Obj796) of type hasAttribute_T
    self.drawConnections(
(self.obj963,self.obj916,[763.0, 812.5, 854.0, 854.0],"true", 2) )
    # Connections for obj964 (graphObject_: Obj797) of type leftExpr
    self.drawConnections(
(self.obj964,self.obj911,[456.0, 316.5, 434.0, 274.0],"true", 2) )
    # Connections for obj965 (graphObject_: Obj798) of type leftExpr
    self.drawConnections(
(self.obj965,self.obj912,[616.0, 358.5, 594.0, 394.0],"true", 2) )
    # Connections for obj966 (graphObject_: Obj799) of type leftExpr
    self.drawConnections(
(self.obj966,self.obj913,[956.0, 356.5, 974.0, 394.0],"true", 2) )
    # Connections for obj967 (graphObject_: Obj800) of type leftExpr
    self.drawConnections(
(self.obj967,self.obj914,[386.0, 616.5, 414.0, 574.0],"true", 2) )
    # Connections for obj968 (graphObject_: Obj801) of type leftExpr
    self.drawConnections(
(self.obj968,self.obj915,[1066.0, 816.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj969 (graphObject_: Obj802) of type leftExpr
    self.drawConnections(
(self.obj969,self.obj916,[781.5, 856.5, 854.0, 854.0],"true", 2) )
    # Connections for obj970 (graphObject_: Obj803) of type rightExpr
    self.drawConnections(
(self.obj970,self.obj923,[376.0, 316.5, 294.0, 274.0],"true", 2) )
    # Connections for obj971 (graphObject_: Obj804) of type rightExpr
    self.drawConnections(
(self.obj971,self.obj910,[648.0, 251.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj972 (graphObject_: Obj805) of type rightExpr
    self.drawConnections(
(self.obj972,self.obj924,[886.0, 356.5, 834.0, 394.0],"true", 2) )
    # Connections for obj973 (graphObject_: Obj806) of type rightExpr
    self.drawConnections(
(self.obj973,self.obj925,[316.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj974 (graphObject_: Obj807) of type rightExpr
    self.drawConnections(
(self.obj974,self.obj926,[996.0, 816.5, 954.0, 774.0],"true", 2) )
    # Connections for obj975 (graphObject_: Obj808) of type rightExpr
    self.drawConnections(
(self.obj975,self.obj927,[631.5, 856.5, 554.0, 854.0],"true", 2) )

newfunction = Transition2HListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
