"""
__Transition2HListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Feb  9 22:23:39 2015
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
       new_obj = graph_ApplyModel(20.0,380.0,self.obj101)
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

    self.obj102=Trigger_S(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # classtype
    self.obj102.classtype.setValue('Trigger_S')

    # cardinality
    self.obj102.cardinality.setValue('1')

    # name
    self.obj102.name.setValue('triggerS1')

    self.obj102.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(480.0,140.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=Signal(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('signal1')

    # classtype
    self.obj103.classtype.setValue('Signal')

    # cardinality
    self.obj103.cardinality.setValue('1')

    self.obj103.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(720.0,140.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=Vertex(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # name
    self.obj104.name.setValue('vertex1')

    # classtype
    self.obj104.classtype.setValue('Vertex')

    # cardinality
    self.obj104.cardinality.setValue('+')

    self.obj104.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(400.0,40.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=Transition(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # name
    self.obj105.name.setValue('transition1')

    # classtype
    self.obj105.classtype.setValue('Transition')

    # cardinality
    self.obj105.cardinality.setValue('+')

    self.obj105.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(200.0,40.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=StateMachine(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # name
    self.obj106.name.setValue('statemachine1')

    # classtype
    self.obj106.classtype.setValue('StateMachine')

    # cardinality
    self.obj106.cardinality.setValue('+')

    self.obj106.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(600.0,40.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=State(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # name
    self.obj107.name.setValue('state1')

    # classtype
    self.obj107.classtype.setValue('State')

    # cardinality
    self.obj107.cardinality.setValue('1')

    self.obj107.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(800.0,40.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=State(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # name
    self.obj108.name.setValue('state2')

    # classtype
    self.obj108.classtype.setValue('State')

    # cardinality
    self.obj108.cardinality.setValue('+')

    self.obj108.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(280.0,140.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=Trigger_T(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # classtype
    self.obj109.classtype.setValue('Trigger_T')

    # cardinality
    self.obj109.cardinality.setValue('1')

    # name
    self.obj109.name.setValue('triggerT1')

    self.obj109.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(780.0,440.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Listen(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # classtype
    self.obj110.classtype.setValue('Listen')

    # cardinality
    self.obj110.cardinality.setValue('1')

    # name
    self.obj110.name.setValue('listen1')

    self.obj110.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,440.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Listen(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # classtype
    self.obj111.classtype.setValue('Listen')

    # cardinality
    self.obj111.cardinality.setValue('1')

    # name
    self.obj111.name.setValue('listen2')

    self.obj111.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(780.0,540.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=ListenBranch(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # classtype
    self.obj112.classtype.setValue('ListenBranch')

    # cardinality
    self.obj112.cardinality.setValue('1')

    # name
    self.obj112.name.setValue('listenbranch1')

    self.obj112.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(380.0,440.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=ListenBranch(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # classtype
    self.obj113.classtype.setValue('ListenBranch')

    # cardinality
    self.obj113.cardinality.setValue('1')

    # name
    self.obj113.name.setValue('listenbranch2')

    self.obj113.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(860.0,640.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Inst(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # classtype
    self.obj114.classtype.setValue('Inst')

    # cardinality
    self.obj114.cardinality.setValue('1')

    # name
    self.obj114.name.setValue('inst1')

    self.obj114.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(580.0,720.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Seq(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # name
    self.obj115.name.setValue('seq1')

    # classtype
    self.obj115.classtype.setValue('Seq')

    # cardinality
    self.obj115.cardinality.setValue('1')

    self.obj115.graphClass_= graph_Seq
    if self.genGraphics:
       new_obj = graph_Seq(580.0,440.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Seq", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=Attribute(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # Type
    self.obj116.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj116.Type.config = 0

    # name
    self.obj116.name.setValue('name')

    self.obj116.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(920.0,140.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=Attribute(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # Type
    self.obj117.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj117.Type.config = 0

    # name
    self.obj117.name.setValue('isComposite')

    self.obj117.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(300.0,240.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=Attribute(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # Type
    self.obj118.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj118.Type.config = 0

    # name
    self.obj118.name.setValue('channel')

    self.obj118.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(460.0,360.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=Attribute(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # Type
    self.obj119.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj119.Type.config = 0

    # name
    self.obj119.name.setValue('channel')

    self.obj119.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,360.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=Attribute(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # Type
    self.obj120.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj120.Type.config = 0

    # name
    self.obj120.name.setValue('pivot')

    self.obj120.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(280.0,540.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=Attribute(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # Type
    self.obj121.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj121.Type.config = 0

    # name
    self.obj121.name.setValue('channel')

    self.obj121.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(960.0,740.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=Attribute(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # Type
    self.obj122.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj122.Type.config = 0

    # name
    self.obj122.name.setValue('pivot')

    self.obj122.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,820.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=Equation(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # name
    self.obj123.name.setValue('eq1')

    self.obj123.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,320.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=Equation(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # name
    self.obj124.name.setValue('eq2')

    self.obj124.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,284.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=Equation(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # name
    self.obj125.name.setValue('eq3')

    self.obj125.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,280.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=Equation(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # name
    self.obj126.name.setValue('eq4')

    self.obj126.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,620.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=Equation(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # name
    self.obj127.name.setValue('eq5')

    self.obj127.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(900.0,820.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=Equation(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # name
    self.obj128.name.setValue('eq6')

    self.obj128.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(571.0,820.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=Constant(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # Type
    self.obj129.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj129.Type.config = 0

    # name
    self.obj129.name.setValue('true')

    self.obj129.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,240.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=Constant(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # Type
    self.obj130.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj130.Type.config = 0

    # name
    self.obj130.name.setValue('exit_in')

    self.obj130.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,360.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=Constant(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # Type
    self.obj131.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj131.Type.config = 0

    # name
    self.obj131.name.setValue('listenhproc')

    self.obj131.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(140.0,540.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=Constant(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # Type
    self.obj132.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj132.Type.config = 0

    # name
    self.obj132.name.setValue('exack_in')

    self.obj132.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(820.0,740.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=Constant(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # Type
    self.obj133.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj133.Type.config = 0

    # name
    self.obj133.name.setValue('instfortrans')

    self.obj133.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,820.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=paired_with(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    self.obj134.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,192.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=match_contains(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    self.obj135.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(254.0,67.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=match_contains(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    self.obj136.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,67.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=match_contains(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    self.obj137.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(454.0,67.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=match_contains(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    self.obj138.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(554.0,67.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=match_contains(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    self.obj139.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(294.0,117.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=match_contains(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    self.obj140.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,117.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=match_contains(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    self.obj141.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(514.0,117.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=apply_contains(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,452.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=apply_contains(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    self.obj143.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(347.5,452.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=apply_contains(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    self.obj144.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,452.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=apply_contains(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    self.obj145.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,452.0,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=apply_contains(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    self.obj146.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,502.0,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=apply_contains(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    self.obj147.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(587.5,552.0,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=apply_contains(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    self.obj148.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,592.0,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj149=directLink_T(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    # associationType
    self.obj149.associationType.setValue('branches')

    self.obj149.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.0,491.0,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=directLink_T(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    # associationType
    self.obj150.associationType.setValue('p')

    self.obj150.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=directLink_T(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    # associationType
    self.obj151.associationType.setValue('p')

    self.obj151.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,491.0,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=directLink_T(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    # associationType
    self.obj152.associationType.setValue('p')

    self.obj152.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,541.0,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj153=directLink_T(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    # associationType
    self.obj153.associationType.setValue('branches')

    self.obj153.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(992.0,641.0,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=directLink_T(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # associationType
    self.obj154.associationType.setValue('p')

    self.obj154.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(806.0,693.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=directLink_S(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    # associationType
    self.obj155.associationType.setValue('src')

    self.obj155.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,83.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=directLink_S(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # associationType
    self.obj156.associationType.setValue('owningStateMachine')

    self.obj156.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,83.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=directLink_S(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # associationType
    self.obj157.associationType.setValue('states')

    self.obj157.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(870.0,83.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=directLink_S(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # associationType
    self.obj158.associationType.setValue('triggers')

    self.obj158.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(489.0,128.0,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=directLink_S(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # associationType
    self.obj159.associationType.setValue('signal')

    self.obj159.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,183.0,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=directLink_S(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # associationType
    self.obj160.associationType.setValue('outgoingTransitions')

    self.obj160.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(430.0,148.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=backward_link(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # type
    self.obj161.type.setValue('ruleDef')

    self.obj161.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(460.0,339.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=backward_link(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    # type
    self.obj162.type.setValue('ruleDef')

    self.obj162.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(561.0,427.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj163=hasAttribute_S(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    self.obj163.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(972.0,178.5,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=hasAttribute_S(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    self.obj164.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(440.0,231.5,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=hasAttribute_T(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    self.obj165.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(573.0,442.5,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=hasAttribute_T(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    self.obj166.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(963.0,442.5,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=hasAttribute_T(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    self.obj167.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(383.0,532.5,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=hasAttribute_T(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    self.obj168.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1063.0,732.5,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=hasAttribute_T(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    self.obj169.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(763.0,812.5,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=leftExpr(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    self.obj170.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(401.0,321.5,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj171=leftExpr(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    self.obj171.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(616.0,358.5,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=leftExpr(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(False)

    self.obj172.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,356.5,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=leftExpr(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(False)

    self.obj173.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(386.0,616.5,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=leftExpr(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    self.obj174.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1066.0,816.5,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=leftExpr(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    self.obj175.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(781.5,856.5,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=rightExpr(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    self.obj176.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(295.0,312.5,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    self.obj177=rightExpr(self)
    self.obj177.isGraphObjectVisual = True

    if(hasattr(self.obj177, '_setHierarchicalLink')):
      self.obj177._setHierarchicalLink(False)

    self.obj177.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(648.0,251.5,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)
    self.obj177.postAction( rootNode.CREATE )

    self.obj178=rightExpr(self)
    self.obj178.isGraphObjectVisual = True

    if(hasattr(self.obj178, '_setHierarchicalLink')):
      self.obj178._setHierarchicalLink(False)

    self.obj178.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(886.0,356.5,self.obj178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj178)
    self.globalAndLocalPostcondition(self.obj178, rootNode)
    self.obj178.postAction( rootNode.CREATE )

    self.obj179=rightExpr(self)
    self.obj179.isGraphObjectVisual = True

    if(hasattr(self.obj179, '_setHierarchicalLink')):
      self.obj179._setHierarchicalLink(False)

    self.obj179.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(316.0,616.5,self.obj179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj179)
    self.globalAndLocalPostcondition(self.obj179, rootNode)
    self.obj179.postAction( rootNode.CREATE )

    self.obj180=rightExpr(self)
    self.obj180.isGraphObjectVisual = True

    if(hasattr(self.obj180, '_setHierarchicalLink')):
      self.obj180._setHierarchicalLink(False)

    self.obj180.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,816.5,self.obj180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj180)
    self.globalAndLocalPostcondition(self.obj180, rootNode)
    self.obj180.postAction( rootNode.CREATE )

    self.obj181=rightExpr(self)
    self.obj181.isGraphObjectVisual = True

    if(hasattr(self.obj181, '_setHierarchicalLink')):
      self.obj181._setHierarchicalLink(False)

    self.obj181.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(631.5,856.5,self.obj181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj181)
    self.globalAndLocalPostcondition(self.obj181, rootNode)
    self.obj181.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj134,[138.0, 51.0, 140.5, 192.0],"true", 2),
(self.obj100,self.obj135,[138.0, 51.0, 254.0, 67.0],"true", 2),
(self.obj100,self.obj136,[138.0, 51.0, 354.0, 67.0],"true", 2),
(self.obj100,self.obj137,[138.0, 51.0, 454.0, 67.0],"true", 2),
(self.obj100,self.obj138,[138.0, 51.0, 554.0, 67.0],"true", 2),
(self.obj100,self.obj139,[138.0, 51.0, 294.0, 117.0],"true", 2),
(self.obj100,self.obj140,[138.0, 51.0, 394.0, 117.0],"true", 2),
(self.obj100,self.obj141,[138.0, 51.0, 514.0, 117.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj142,[143.0, 413.0, 247.5, 452.0],"true", 2),
(self.obj101,self.obj143,[143.0, 413.0, 347.5, 452.0],"true", 2),
(self.obj101,self.obj144,[143.0, 413.0, 447.5, 452.0],"true", 2),
(self.obj101,self.obj145,[143.0, 413.0, 547.5, 452.0],"true", 2),
(self.obj101,self.obj146,[143.0, 413.0, 547.5, 502.0],"true", 2),
(self.obj101,self.obj147,[143.0, 413.0, 587.5, 552.0],"true", 2),
(self.obj101,self.obj148,[143.0, 413.0, 447.5, 592.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj2) named triggerS1
    self.drawConnections(
(self.obj102,self.obj159,[650.0, 183.0, 670.0, 183.0],"true", 2) )
    # Connections for obj103 (graphObject_: Obj3) named signal1
    self.drawConnections(
(self.obj103,self.obj163,[890.0, 183.0, 972.0, 178.5],"true", 2) )
    # Connections for obj104 (graphObject_: Obj4) named vertex1
    self.drawConnections(
(self.obj104,self.obj156,[570.0, 83.0, 670.0, 83.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) named transition1
    self.drawConnections(
(self.obj105,self.obj155,[370.0, 83.0, 470.0, 83.0],"true", 2),
(self.obj105,self.obj158,[370.0, 83.0, 489.0, 128.0],"true", 2) )
    # Connections for obj106 (graphObject_: Obj6) named statemachine1
    self.drawConnections(
(self.obj106,self.obj157,[770.0, 83.0, 870.0, 83.0],"true", 2) )
    # Connections for obj107 (graphObject_: Obj7) named state1
    self.drawConnections(
 )
    # Connections for obj108 (graphObject_: Obj8) named state2
    self.drawConnections(
(self.obj108,self.obj160,[450.0, 183.0, 430.0, 148.0],"true", 2),
(self.obj108,self.obj164,[450.0, 183.0, 440.0, 231.5],"true", 2) )
    # Connections for obj109 (graphObject_: Obj9) named triggerT1
    self.drawConnections(
(self.obj109,self.obj166,[952.0, 491.0, 963.0, 442.5],"true", 2) )
    # Connections for obj110 (graphObject_: Obj10) named listen1
    self.drawConnections(
(self.obj110,self.obj149,[352.0, 491.0, 452.0, 491.0],"true", 2),
(self.obj110,self.obj167,[352.0, 491.0, 383.0, 532.5],"true", 2),
(self.obj110,self.obj161,[352.0, 491.0, 460.0, 339.0],"true", 2) )
    # Connections for obj111 (graphObject_: Obj11) named listen2
    self.drawConnections(
(self.obj111,self.obj153,[952.0, 591.0, 992.0, 641.0],"true", 2) )
    # Connections for obj112 (graphObject_: Obj12) named listenbranch1
    self.drawConnections(
(self.obj112,self.obj150,[552.0, 491.0, 652.0, 491.0],"true", 2),
(self.obj112,self.obj165,[552.0, 491.0, 573.0, 442.5],"true", 2) )
    # Connections for obj113 (graphObject_: Obj13) named listenbranch2
    self.drawConnections(
(self.obj113,self.obj168,[1032.0, 691.0, 1063.0, 732.5],"true", 2),
(self.obj113,self.obj154,[1032.0, 691.0, 806.0, 693.0],"true", 2) )
    # Connections for obj114 (graphObject_: Obj14) named inst1
    self.drawConnections(
(self.obj114,self.obj169,[752.0, 771.0, 763.0, 812.5],"true", 2),
(self.obj114,self.obj162,[752.0, 771.0, 561.0, 427.0],"true", 2) )
    # Connections for obj115 (graphObject_: Obj15) named seq1
    self.drawConnections(
(self.obj115,self.obj151,[752.0, 491.0, 852.0, 491.0],"true", 2),
(self.obj115,self.obj152,[752.0, 491.0, 852.0, 541.0],"true", 2) )
    # Connections for obj116 (graphObject_: Obj16) named name
    self.drawConnections(
 )
    # Connections for obj117 (graphObject_: Obj17) named isComposite
    self.drawConnections(
 )
    # Connections for obj118 (graphObject_: Obj18) named channel
    self.drawConnections(
 )
    # Connections for obj119 (graphObject_: Obj19) named channel
    self.drawConnections(
 )
    # Connections for obj120 (graphObject_: Obj20) named pivot
    self.drawConnections(
 )
    # Connections for obj121 (graphObject_: Obj21) named channel
    self.drawConnections(
 )
    # Connections for obj122 (graphObject_: Obj22) named pivot
    self.drawConnections(
 )
    # Connections for obj123 (graphObject_: Obj23) named eq1
    self.drawConnections(
(self.obj123,self.obj170,[358.0, 359.0, 401.0, 321.5],"true", 2),
(self.obj123,self.obj176,[358.0, 359.0, 295.0, 312.5],"true", 2) )
    # Connections for obj124 (graphObject_: Obj24) named eq2
    self.drawConnections(
(self.obj124,self.obj171,[638.0, 323.0, 616.0, 358.5],"true", 2),
(self.obj124,self.obj177,[638.0, 323.0, 648.0, 251.5],"true", 2) )
    # Connections for obj125 (graphObject_: Obj25) named eq3
    self.drawConnections(
(self.obj125,self.obj178,[938.0, 319.0, 886.0, 356.5],"true", 2),
(self.obj125,self.obj172,[938.0, 319.0, 956.0, 356.5],"true", 2) )
    # Connections for obj126 (graphObject_: Obj26) named eq4
    self.drawConnections(
(self.obj126,self.obj173,[358.0, 659.0, 386.0, 616.5],"true", 2),
(self.obj126,self.obj179,[358.0, 659.0, 316.0, 616.5],"true", 2) )
    # Connections for obj127 (graphObject_: Obj27) named eq5
    self.drawConnections(
(self.obj127,self.obj174,[1038.0, 859.0, 1066.0, 816.5],"true", 2),
(self.obj127,self.obj180,[1038.0, 859.0, 996.0, 816.5],"true", 2) )
    # Connections for obj128 (graphObject_: Obj28) named eq6
    self.drawConnections(
(self.obj128,self.obj175,[709.0, 859.0, 781.5, 856.5],"true", 2),
(self.obj128,self.obj181,[709.0, 859.0, 631.5, 856.5],"true", 2) )
    # Connections for obj129 (graphObject_: Obj29) named true
    self.drawConnections(
 )
    # Connections for obj130 (graphObject_: Obj30) named exit_in
    self.drawConnections(
 )
    # Connections for obj131 (graphObject_: Obj31) named listenhproc
    self.drawConnections(
 )
    # Connections for obj132 (graphObject_: Obj32) named exack_in
    self.drawConnections(
 )
    # Connections for obj133 (graphObject_: Obj33) named instfortrans
    self.drawConnections(
 )
    # Connections for obj134 (graphObject_: Obj34) of type paired_with
    self.drawConnections(
(self.obj134,self.obj101,[140.5, 192.0, 143.0, 413.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj35) of type match_contains
    self.drawConnections(
(self.obj135,self.obj105,[254.0, 67.0, 370.0, 83.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj36) of type match_contains
    self.drawConnections(
(self.obj136,self.obj104,[354.0, 67.0, 570.0, 83.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj37) of type match_contains
    self.drawConnections(
(self.obj137,self.obj106,[454.0, 67.0, 770.0, 83.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj38) of type match_contains
    self.drawConnections(
(self.obj138,self.obj107,[554.0, 67.0, 970.0, 83.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj39) of type match_contains
    self.drawConnections(
(self.obj139,self.obj108,[294.0, 117.0, 450.0, 183.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj40) of type match_contains
    self.drawConnections(
(self.obj140,self.obj102,[394.0, 117.0, 650.0, 183.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj41) of type match_contains
    self.drawConnections(
(self.obj141,self.obj103,[514.0, 117.0, 890.0, 183.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj42) of type apply_contains
    self.drawConnections(
(self.obj142,self.obj110,[247.5, 452.0, 352.0, 491.0],"true", 2) )
    # Connections for obj143 (graphObject_: Obj43) of type apply_contains
    self.drawConnections(
(self.obj143,self.obj112,[347.5, 452.0, 552.0, 491.0],"true", 2) )
    # Connections for obj144 (graphObject_: Obj44) of type apply_contains
    self.drawConnections(
(self.obj144,self.obj115,[447.5, 452.0, 752.0, 491.0],"true", 2) )
    # Connections for obj145 (graphObject_: Obj45) of type apply_contains
    self.drawConnections(
(self.obj145,self.obj109,[547.5, 452.0, 952.0, 491.0],"true", 2) )
    # Connections for obj146 (graphObject_: Obj46) of type apply_contains
    self.drawConnections(
(self.obj146,self.obj111,[547.5, 502.0, 952.0, 591.0],"true", 2) )
    # Connections for obj147 (graphObject_: Obj47) of type apply_contains
    self.drawConnections(
(self.obj147,self.obj113,[587.5, 552.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj148 (graphObject_: Obj48) of type apply_contains
    self.drawConnections(
(self.obj148,self.obj114,[447.5, 592.0, 752.0, 771.0],"true", 2) )
    # Connections for obj149 (graphObject_: Obj49) of type directLink_T
    self.drawConnections(
(self.obj149,self.obj112,[452.0, 491.0, 552.0, 491.0],"true", 2) )
    # Connections for obj150 (graphObject_: Obj50) of type directLink_T
    self.drawConnections(
(self.obj150,self.obj115,[652.0, 491.0, 752.0, 491.0],"true", 2) )
    # Connections for obj151 (graphObject_: Obj51) of type directLink_T
    self.drawConnections(
(self.obj151,self.obj109,[852.0, 491.0, 952.0, 491.0],"true", 2) )
    # Connections for obj152 (graphObject_: Obj52) of type directLink_T
    self.drawConnections(
(self.obj152,self.obj111,[852.0, 541.0, 952.0, 591.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj53) of type directLink_T
    self.drawConnections(
(self.obj153,self.obj113,[992.0, 641.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj154 (graphObject_: Obj54) of type directLink_T
    self.drawConnections(
(self.obj154,self.obj114,[806.0, 693.0, 752.0, 771.0],"true", 2) )
    # Connections for obj155 (graphObject_: Obj55) of type directLink_S
    self.drawConnections(
(self.obj155,self.obj104,[470.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj156 (graphObject_: Obj56) of type directLink_S
    self.drawConnections(
(self.obj156,self.obj106,[670.0, 83.0, 770.0, 83.0],"true", 2) )
    # Connections for obj157 (graphObject_: Obj57) of type directLink_S
    self.drawConnections(
(self.obj157,self.obj107,[870.0, 83.0, 970.0, 83.0],"true", 2) )
    # Connections for obj158 (graphObject_: Obj58) of type directLink_S
    self.drawConnections(
(self.obj158,self.obj102,[470.0, 133.0, 650.0, 183.0],"true", 2) )
    # Connections for obj159 (graphObject_: Obj59) of type directLink_S
    self.drawConnections(
(self.obj159,self.obj103,[670.0, 183.0, 890.0, 183.0],"true", 2) )
    # Connections for obj160 (graphObject_: Obj60) of type directLink_S
    self.drawConnections(
(self.obj160,self.obj105,[400.0, 133.0, 370.0, 83.0],"true", 2) )
    # Connections for obj161 (graphObject_: Obj61) of type backward_link
    self.drawConnections(
(self.obj161,self.obj108,[401.0, 337.0, 450.0, 183.0],"true", 2) )
    # Connections for obj162 (graphObject_: Obj62) of type backward_link
    self.drawConnections(
(self.obj162,self.obj105,[561.0, 427.0, 370.0, 83.0],"true", 2) )
    # Connections for obj163 (graphObject_: Obj63) of type hasAttribute_S
    self.drawConnections(
(self.obj163,self.obj116,[972.0, 178.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj164 (graphObject_: Obj64) of type hasAttribute_S
    self.drawConnections(
(self.obj164,self.obj117,[462.0, 228.5, 434.0, 274.0],"true", 2) )
    # Connections for obj165 (graphObject_: Obj65) of type hasAttribute_T
    self.drawConnections(
(self.obj165,self.obj118,[573.0, 442.5, 594.0, 394.0],"true", 2) )
    # Connections for obj166 (graphObject_: Obj66) of type hasAttribute_T
    self.drawConnections(
(self.obj166,self.obj119,[963.0, 442.5, 974.0, 394.0],"true", 2) )
    # Connections for obj167 (graphObject_: Obj67) of type hasAttribute_T
    self.drawConnections(
(self.obj167,self.obj120,[383.0, 532.5, 414.0, 574.0],"true", 2) )
    # Connections for obj168 (graphObject_: Obj68) of type hasAttribute_T
    self.drawConnections(
(self.obj168,self.obj121,[1063.0, 732.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj169 (graphObject_: Obj69) of type hasAttribute_T
    self.drawConnections(
(self.obj169,self.obj122,[763.0, 812.5, 854.0, 854.0],"true", 2) )
    # Connections for obj170 (graphObject_: Obj70) of type leftExpr
    self.drawConnections(
(self.obj170,self.obj117,[456.0, 316.5, 434.0, 274.0],"true", 2) )
    # Connections for obj171 (graphObject_: Obj71) of type leftExpr
    self.drawConnections(
(self.obj171,self.obj118,[616.0, 358.5, 594.0, 394.0],"true", 2) )
    # Connections for obj172 (graphObject_: Obj72) of type leftExpr
    self.drawConnections(
(self.obj172,self.obj119,[956.0, 356.5, 974.0, 394.0],"true", 2) )
    # Connections for obj173 (graphObject_: Obj73) of type leftExpr
    self.drawConnections(
(self.obj173,self.obj120,[386.0, 616.5, 414.0, 574.0],"true", 2) )
    # Connections for obj174 (graphObject_: Obj74) of type leftExpr
    self.drawConnections(
(self.obj174,self.obj121,[1066.0, 816.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj175 (graphObject_: Obj75) of type leftExpr
    self.drawConnections(
(self.obj175,self.obj122,[781.5, 856.5, 854.0, 854.0],"true", 2) )
    # Connections for obj176 (graphObject_: Obj76) of type rightExpr
    self.drawConnections(
(self.obj176,self.obj129,[376.0, 316.5, 294.0, 274.0],"true", 2) )
    # Connections for obj177 (graphObject_: Obj77) of type rightExpr
    self.drawConnections(
(self.obj177,self.obj116,[648.0, 251.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj178 (graphObject_: Obj78) of type rightExpr
    self.drawConnections(
(self.obj178,self.obj130,[886.0, 356.5, 834.0, 394.0],"true", 2) )
    # Connections for obj179 (graphObject_: Obj79) of type rightExpr
    self.drawConnections(
(self.obj179,self.obj131,[316.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj180 (graphObject_: Obj80) of type rightExpr
    self.drawConnections(
(self.obj180,self.obj132,[996.0, 816.5, 954.0, 774.0],"true", 2) )
    # Connections for obj181 (graphObject_: Obj81) of type rightExpr
    self.drawConnections(
(self.obj181,self.obj133,[631.5, 856.5, 554.0, 854.0],"true", 2) )

newfunction = Transition2HListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
