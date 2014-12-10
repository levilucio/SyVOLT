"""
__Transition2HListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 14:22:48 2014
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


    self.obj456=MatchModel(self)
    self.obj456.isGraphObjectVisual = True

    if(hasattr(self.obj456, '_setHierarchicalLink')):
      self.obj456._setHierarchicalLink(False)

    self.obj456.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj456)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj456.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj456)
    self.globalAndLocalPostcondition(self.obj456, rootNode)
    self.obj456.postAction( rootNode.CREATE )

    self.obj457=ApplyModel(self)
    self.obj457.isGraphObjectVisual = True

    if(hasattr(self.obj457, '_setHierarchicalLink')):
      self.obj457._setHierarchicalLink(False)

    self.obj457.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,380.0,self.obj457)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj457.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj457)
    self.globalAndLocalPostcondition(self.obj457, rootNode)
    self.obj457.postAction( rootNode.CREATE )

    self.obj463=Trigger_S(self)
    self.obj463.isGraphObjectVisual = True

    if(hasattr(self.obj463, '_setHierarchicalLink')):
      self.obj463._setHierarchicalLink(False)

    # classtype
    self.obj463.classtype.setValue('Trigger_S')

    # cardinality
    self.obj463.cardinality.setValue('1')

    # name
    self.obj463.name.setValue('triggerS1')

    self.obj463.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(480.0,140.0,self.obj463)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj463.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj463)
    self.globalAndLocalPostcondition(self.obj463, rootNode)
    self.obj463.postAction( rootNode.CREATE )

    self.obj464=Signal(self)
    self.obj464.isGraphObjectVisual = True

    if(hasattr(self.obj464, '_setHierarchicalLink')):
      self.obj464._setHierarchicalLink(False)

    # name
    self.obj464.name.setValue('signal1')

    # classtype
    self.obj464.classtype.setValue('Signal')

    # cardinality
    self.obj464.cardinality.setValue('1')

    self.obj464.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(720.0,140.0,self.obj464)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj464.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj464)
    self.globalAndLocalPostcondition(self.obj464, rootNode)
    self.obj464.postAction( rootNode.CREATE )

    self.obj459=Vertex(self)
    self.obj459.isGraphObjectVisual = True

    if(hasattr(self.obj459, '_setHierarchicalLink')):
      self.obj459._setHierarchicalLink(False)

    # name
    self.obj459.name.setValue('vertex1')

    # classtype
    self.obj459.classtype.setValue('Vertex')

    # cardinality
    self.obj459.cardinality.setValue('+')

    self.obj459.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(400.0,40.0,self.obj459)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj459.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj459)
    self.globalAndLocalPostcondition(self.obj459, rootNode)
    self.obj459.postAction( rootNode.CREATE )

    self.obj460=Transition(self)
    self.obj460.isGraphObjectVisual = True

    if(hasattr(self.obj460, '_setHierarchicalLink')):
      self.obj460._setHierarchicalLink(False)

    # name
    self.obj460.name.setValue('transition1')

    # classtype
    self.obj460.classtype.setValue('Transition')

    # cardinality
    self.obj460.cardinality.setValue('+')

    self.obj460.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(200.0,40.0,self.obj460)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj460.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj460)
    self.globalAndLocalPostcondition(self.obj460, rootNode)
    self.obj460.postAction( rootNode.CREATE )

    self.obj461=StateMachine(self)
    self.obj461.isGraphObjectVisual = True

    if(hasattr(self.obj461, '_setHierarchicalLink')):
      self.obj461._setHierarchicalLink(False)

    # name
    self.obj461.name.setValue('statemachine1')

    # classtype
    self.obj461.classtype.setValue('StateMachine')

    # cardinality
    self.obj461.cardinality.setValue('+')

    self.obj461.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(600.0,40.0,self.obj461)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj461.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj461)
    self.globalAndLocalPostcondition(self.obj461, rootNode)
    self.obj461.postAction( rootNode.CREATE )

    self.obj462=State(self)
    self.obj462.isGraphObjectVisual = True

    if(hasattr(self.obj462, '_setHierarchicalLink')):
      self.obj462._setHierarchicalLink(False)

    # name
    self.obj462.name.setValue('state1')

    # classtype
    self.obj462.classtype.setValue('State')

    # cardinality
    self.obj462.cardinality.setValue('1')

    self.obj462.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(800.0,40.0,self.obj462)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj462.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj462)
    self.globalAndLocalPostcondition(self.obj462, rootNode)
    self.obj462.postAction( rootNode.CREATE )

    self.obj483=State(self)
    self.obj483.isGraphObjectVisual = True

    if(hasattr(self.obj483, '_setHierarchicalLink')):
      self.obj483._setHierarchicalLink(False)

    # name
    self.obj483.name.setValue('state2')

    # classtype
    self.obj483.classtype.setValue('State')

    # cardinality
    self.obj483.cardinality.setValue('+')

    self.obj483.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(280.0,140.0,self.obj483)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj483.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj483)
    self.globalAndLocalPostcondition(self.obj483, rootNode)
    self.obj483.postAction( rootNode.CREATE )

    self.obj535=Trigger_T(self)
    self.obj535.isGraphObjectVisual = True

    if(hasattr(self.obj535, '_setHierarchicalLink')):
      self.obj535._setHierarchicalLink(False)

    # classtype
    self.obj535.classtype.setValue('Trigger_T')

    # cardinality
    self.obj535.cardinality.setValue('1')

    # name
    self.obj535.name.setValue('triggerT1')

    self.obj535.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(780.0,440.0,self.obj535)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj535.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj535)
    self.globalAndLocalPostcondition(self.obj535, rootNode)
    self.obj535.postAction( rootNode.CREATE )

    self.obj519=Listen(self)
    self.obj519.isGraphObjectVisual = True

    if(hasattr(self.obj519, '_setHierarchicalLink')):
      self.obj519._setHierarchicalLink(False)

    # classtype
    self.obj519.classtype.setValue('Listen')

    # cardinality
    self.obj519.cardinality.setValue('1')

    # name
    self.obj519.name.setValue('listen1')

    self.obj519.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,440.0,self.obj519)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj519.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj519)
    self.globalAndLocalPostcondition(self.obj519, rootNode)
    self.obj519.postAction( rootNode.CREATE )

    self.obj536=Listen(self)
    self.obj536.isGraphObjectVisual = True

    if(hasattr(self.obj536, '_setHierarchicalLink')):
      self.obj536._setHierarchicalLink(False)

    # classtype
    self.obj536.classtype.setValue('Listen')

    # cardinality
    self.obj536.cardinality.setValue('1')

    # name
    self.obj536.name.setValue('listen2')

    self.obj536.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(780.0,540.0,self.obj536)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj536.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj536)
    self.globalAndLocalPostcondition(self.obj536, rootNode)
    self.obj536.postAction( rootNode.CREATE )

    self.obj520=ListenBranch(self)
    self.obj520.isGraphObjectVisual = True

    if(hasattr(self.obj520, '_setHierarchicalLink')):
      self.obj520._setHierarchicalLink(False)

    # classtype
    self.obj520.classtype.setValue('ListenBranch')

    # cardinality
    self.obj520.cardinality.setValue('1')

    # name
    self.obj520.name.setValue('listenbranch1')

    self.obj520.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(380.0,440.0,self.obj520)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj520.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj520)
    self.globalAndLocalPostcondition(self.obj520, rootNode)
    self.obj520.postAction( rootNode.CREATE )

    self.obj583=ListenBranch(self)
    self.obj583.isGraphObjectVisual = True

    if(hasattr(self.obj583, '_setHierarchicalLink')):
      self.obj583._setHierarchicalLink(False)

    # classtype
    self.obj583.classtype.setValue('ListenBranch')

    # cardinality
    self.obj583.cardinality.setValue('1')

    # name
    self.obj583.name.setValue('listenbranch2')

    self.obj583.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(860.0,640.0,self.obj583)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj583.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj583)
    self.globalAndLocalPostcondition(self.obj583, rootNode)
    self.obj583.postAction( rootNode.CREATE )

    self.obj601=Inst(self)
    self.obj601.isGraphObjectVisual = True

    if(hasattr(self.obj601, '_setHierarchicalLink')):
      self.obj601._setHierarchicalLink(False)

    # classtype
    self.obj601.classtype.setValue('Inst')

    # cardinality
    self.obj601.cardinality.setValue('1')

    # name
    self.obj601.name.setValue('inst1')

    self.obj601.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(580.0,720.0,self.obj601)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj601.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj601)
    self.globalAndLocalPostcondition(self.obj601, rootNode)
    self.obj601.postAction( rootNode.CREATE )

    self.obj529=Seq(self)
    self.obj529.isGraphObjectVisual = True

    if(hasattr(self.obj529, '_setHierarchicalLink')):
      self.obj529._setHierarchicalLink(False)

    # name
    self.obj529.name.setValue('seq1')

    # classtype
    self.obj529.classtype.setValue('Seq')

    # cardinality
    self.obj529.cardinality.setValue('1')

    self.obj529.graphClass_= graph_Seq
    if self.genGraphics:
       new_obj = graph_Seq(580.0,440.0,self.obj529)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Seq", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj529.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj529)
    self.globalAndLocalPostcondition(self.obj529, rootNode)
    self.obj529.postAction( rootNode.CREATE )

    self.obj503=Attribute(self)
    self.obj503.isGraphObjectVisual = True

    if(hasattr(self.obj503, '_setHierarchicalLink')):
      self.obj503._setHierarchicalLink(False)

    # Type
    self.obj503.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj503.Type.config = 0

    # name
    self.obj503.name.setValue('name')

    self.obj503.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(920.0,140.0,self.obj503)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj503.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj503)
    self.globalAndLocalPostcondition(self.obj503, rootNode)
    self.obj503.postAction( rootNode.CREATE )

    self.obj507=Attribute(self)
    self.obj507.isGraphObjectVisual = True

    if(hasattr(self.obj507, '_setHierarchicalLink')):
      self.obj507._setHierarchicalLink(False)

    # Type
    self.obj507.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj507.Type.config = 0

    # name
    self.obj507.name.setValue('isComposite')

    self.obj507.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(300.0,240.0,self.obj507)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj507.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj507)
    self.globalAndLocalPostcondition(self.obj507, rootNode)
    self.obj507.postAction( rootNode.CREATE )

    self.obj547=Attribute(self)
    self.obj547.isGraphObjectVisual = True

    if(hasattr(self.obj547, '_setHierarchicalLink')):
      self.obj547._setHierarchicalLink(False)

    # Type
    self.obj547.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj547.Type.config = 0

    # name
    self.obj547.name.setValue('channel')

    self.obj547.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(460.0,360.0,self.obj547)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj547.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj547)
    self.globalAndLocalPostcondition(self.obj547, rootNode)
    self.obj547.postAction( rootNode.CREATE )

    self.obj559=Attribute(self)
    self.obj559.isGraphObjectVisual = True

    if(hasattr(self.obj559, '_setHierarchicalLink')):
      self.obj559._setHierarchicalLink(False)

    # Type
    self.obj559.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj559.Type.config = 0

    # name
    self.obj559.name.setValue('channel')

    self.obj559.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,360.0,self.obj559)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj559.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj559)
    self.globalAndLocalPostcondition(self.obj559, rootNode)
    self.obj559.postAction( rootNode.CREATE )

    self.obj573=Attribute(self)
    self.obj573.isGraphObjectVisual = True

    if(hasattr(self.obj573, '_setHierarchicalLink')):
      self.obj573._setHierarchicalLink(False)

    # Type
    self.obj573.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj573.Type.config = 0

    # name
    self.obj573.name.setValue('pivotin')

    self.obj573.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(280.0,540.0,self.obj573)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj573.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj573)
    self.globalAndLocalPostcondition(self.obj573, rootNode)
    self.obj573.postAction( rootNode.CREATE )

    self.obj592=Attribute(self)
    self.obj592.isGraphObjectVisual = True

    if(hasattr(self.obj592, '_setHierarchicalLink')):
      self.obj592._setHierarchicalLink(False)

    # Type
    self.obj592.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj592.Type.config = 0

    # name
    self.obj592.name.setValue('channel')

    self.obj592.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(960.0,740.0,self.obj592)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj592.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj592)
    self.globalAndLocalPostcondition(self.obj592, rootNode)
    self.obj592.postAction( rootNode.CREATE )

    self.obj610=Attribute(self)
    self.obj610.isGraphObjectVisual = True

    if(hasattr(self.obj610, '_setHierarchicalLink')):
      self.obj610._setHierarchicalLink(False)

    # Type
    self.obj610.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj610.Type.config = 0

    # name
    self.obj610.name.setValue('pivotin')

    self.obj610.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,820.0,self.obj610)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj610.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj610)
    self.globalAndLocalPostcondition(self.obj610, rootNode)
    self.obj610.postAction( rootNode.CREATE )

    self.obj514=Equation(self)
    self.obj514.isGraphObjectVisual = True

    if(hasattr(self.obj514, '_setHierarchicalLink')):
      self.obj514._setHierarchicalLink(False)

    # name
    self.obj514.name.setValue('eq1')

    self.obj514.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,320.0,self.obj514)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj514.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj514)
    self.globalAndLocalPostcondition(self.obj514, rootNode)
    self.obj514.postAction( rootNode.CREATE )

    self.obj551=Equation(self)
    self.obj551.isGraphObjectVisual = True

    if(hasattr(self.obj551, '_setHierarchicalLink')):
      self.obj551._setHierarchicalLink(False)

    # name
    self.obj551.name.setValue('eq2')

    self.obj551.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,284.0,self.obj551)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj551.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj551)
    self.globalAndLocalPostcondition(self.obj551, rootNode)
    self.obj551.postAction( rootNode.CREATE )

    self.obj556=Equation(self)
    self.obj556.isGraphObjectVisual = True

    if(hasattr(self.obj556, '_setHierarchicalLink')):
      self.obj556._setHierarchicalLink(False)

    # name
    self.obj556.name.setValue('eq3')

    self.obj556.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,280.0,self.obj556)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj556.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj556)
    self.globalAndLocalPostcondition(self.obj556, rootNode)
    self.obj556.postAction( rootNode.CREATE )

    self.obj576=Equation(self)
    self.obj576.isGraphObjectVisual = True

    if(hasattr(self.obj576, '_setHierarchicalLink')):
      self.obj576._setHierarchicalLink(False)

    # name
    self.obj576.name.setValue('eq4')

    self.obj576.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,620.0,self.obj576)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj576.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj576)
    self.globalAndLocalPostcondition(self.obj576, rootNode)
    self.obj576.postAction( rootNode.CREATE )

    self.obj596=Equation(self)
    self.obj596.isGraphObjectVisual = True

    if(hasattr(self.obj596, '_setHierarchicalLink')):
      self.obj596._setHierarchicalLink(False)

    # name
    self.obj596.name.setValue('eq5')

    self.obj596.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(900.0,820.0,self.obj596)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj596.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj596)
    self.globalAndLocalPostcondition(self.obj596, rootNode)
    self.obj596.postAction( rootNode.CREATE )

    self.obj614=Equation(self)
    self.obj614.isGraphObjectVisual = True

    if(hasattr(self.obj614, '_setHierarchicalLink')):
      self.obj614._setHierarchicalLink(False)

    # name
    self.obj614.name.setValue('eq6')

    self.obj614.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(571.0,820.0,self.obj614)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj614.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj614)
    self.globalAndLocalPostcondition(self.obj614, rootNode)
    self.obj614.postAction( rootNode.CREATE )

    self.obj510=Constant(self)
    self.obj510.isGraphObjectVisual = True

    if(hasattr(self.obj510, '_setHierarchicalLink')):
      self.obj510._setHierarchicalLink(False)

    # Type
    self.obj510.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj510.Type.config = 0

    # name
    self.obj510.name.setValue('true')

    self.obj510.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,240.0,self.obj510)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj510.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj510)
    self.globalAndLocalPostcondition(self.obj510, rootNode)
    self.obj510.postAction( rootNode.CREATE )

    self.obj562=Constant(self)
    self.obj562.isGraphObjectVisual = True

    if(hasattr(self.obj562, '_setHierarchicalLink')):
      self.obj562._setHierarchicalLink(False)

    # Type
    self.obj562.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj562.Type.config = 0

    # name
    self.obj562.name.setValue('exit_in')

    self.obj562.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,360.0,self.obj562)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj562.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj562)
    self.globalAndLocalPostcondition(self.obj562, rootNode)
    self.obj562.postAction( rootNode.CREATE )

    self.obj568=Constant(self)
    self.obj568.isGraphObjectVisual = True

    if(hasattr(self.obj568, '_setHierarchicalLink')):
      self.obj568._setHierarchicalLink(False)

    # Type
    self.obj568.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj568.Type.config = 0

    # name
    self.obj568.name.setValue('listenhproc')

    self.obj568.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(140.0,540.0,self.obj568)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj568.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj568)
    self.globalAndLocalPostcondition(self.obj568, rootNode)
    self.obj568.postAction( rootNode.CREATE )

    self.obj587=Constant(self)
    self.obj587.isGraphObjectVisual = True

    if(hasattr(self.obj587, '_setHierarchicalLink')):
      self.obj587._setHierarchicalLink(False)

    # Type
    self.obj587.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj587.Type.config = 0

    # name
    self.obj587.name.setValue('exack_in')

    self.obj587.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(820.0,740.0,self.obj587)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj587.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj587)
    self.globalAndLocalPostcondition(self.obj587, rootNode)
    self.obj587.postAction( rootNode.CREATE )

    self.obj607=Constant(self)
    self.obj607.isGraphObjectVisual = True

    if(hasattr(self.obj607, '_setHierarchicalLink')):
      self.obj607._setHierarchicalLink(False)

    # Type
    self.obj607.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj607.Type.config = 0

    # name
    self.obj607.name.setValue('instfortrans')

    self.obj607.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,820.0,self.obj607)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj607.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj607)
    self.globalAndLocalPostcondition(self.obj607, rootNode)
    self.obj607.postAction( rootNode.CREATE )

    self.obj458=paired_with(self)
    self.obj458.isGraphObjectVisual = True

    if(hasattr(self.obj458, '_setHierarchicalLink')):
      self.obj458._setHierarchicalLink(False)

    self.obj458.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,192.0,self.obj458)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj458.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj458)
    self.globalAndLocalPostcondition(self.obj458, rootNode)
    self.obj458.postAction( rootNode.CREATE )

    self.obj482=match_contains(self)
    self.obj482.isGraphObjectVisual = True

    if(hasattr(self.obj482, '_setHierarchicalLink')):
      self.obj482._setHierarchicalLink(False)

    self.obj482.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(254.0,67.0,self.obj482)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj482.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj482)
    self.globalAndLocalPostcondition(self.obj482, rootNode)
    self.obj482.postAction( rootNode.CREATE )

    self.obj619=match_contains(self)
    self.obj619.isGraphObjectVisual = True

    if(hasattr(self.obj619, '_setHierarchicalLink')):
      self.obj619._setHierarchicalLink(False)

    self.obj619.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,67.0,self.obj619)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj619.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj619)
    self.globalAndLocalPostcondition(self.obj619, rootNode)
    self.obj619.postAction( rootNode.CREATE )

    self.obj620=match_contains(self)
    self.obj620.isGraphObjectVisual = True

    if(hasattr(self.obj620, '_setHierarchicalLink')):
      self.obj620._setHierarchicalLink(False)

    self.obj620.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(454.0,67.0,self.obj620)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj620.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj620)
    self.globalAndLocalPostcondition(self.obj620, rootNode)
    self.obj620.postAction( rootNode.CREATE )

    self.obj621=match_contains(self)
    self.obj621.isGraphObjectVisual = True

    if(hasattr(self.obj621, '_setHierarchicalLink')):
      self.obj621._setHierarchicalLink(False)

    self.obj621.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(554.0,67.0,self.obj621)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj621.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj621)
    self.globalAndLocalPostcondition(self.obj621, rootNode)
    self.obj621.postAction( rootNode.CREATE )

    self.obj622=match_contains(self)
    self.obj622.isGraphObjectVisual = True

    if(hasattr(self.obj622, '_setHierarchicalLink')):
      self.obj622._setHierarchicalLink(False)

    self.obj622.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(294.0,117.0,self.obj622)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj622.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj622)
    self.globalAndLocalPostcondition(self.obj622, rootNode)
    self.obj622.postAction( rootNode.CREATE )

    self.obj623=match_contains(self)
    self.obj623.isGraphObjectVisual = True

    if(hasattr(self.obj623, '_setHierarchicalLink')):
      self.obj623._setHierarchicalLink(False)

    self.obj623.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,117.0,self.obj623)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj623.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj623)
    self.globalAndLocalPostcondition(self.obj623, rootNode)
    self.obj623.postAction( rootNode.CREATE )

    self.obj624=match_contains(self)
    self.obj624.isGraphObjectVisual = True

    if(hasattr(self.obj624, '_setHierarchicalLink')):
      self.obj624._setHierarchicalLink(False)

    self.obj624.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(514.0,117.0,self.obj624)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj624.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj624)
    self.globalAndLocalPostcondition(self.obj624, rootNode)
    self.obj624.postAction( rootNode.CREATE )

    self.obj524=apply_contains(self)
    self.obj524.isGraphObjectVisual = True

    if(hasattr(self.obj524, '_setHierarchicalLink')):
      self.obj524._setHierarchicalLink(False)

    self.obj524.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,452.0,self.obj524)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj524.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj524)
    self.globalAndLocalPostcondition(self.obj524, rootNode)
    self.obj524.postAction( rootNode.CREATE )

    self.obj625=apply_contains(self)
    self.obj625.isGraphObjectVisual = True

    if(hasattr(self.obj625, '_setHierarchicalLink')):
      self.obj625._setHierarchicalLink(False)

    self.obj625.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(347.5,452.0,self.obj625)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj625.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj625)
    self.globalAndLocalPostcondition(self.obj625, rootNode)
    self.obj625.postAction( rootNode.CREATE )

    self.obj626=apply_contains(self)
    self.obj626.isGraphObjectVisual = True

    if(hasattr(self.obj626, '_setHierarchicalLink')):
      self.obj626._setHierarchicalLink(False)

    self.obj626.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,452.0,self.obj626)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj626.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj626)
    self.globalAndLocalPostcondition(self.obj626, rootNode)
    self.obj626.postAction( rootNode.CREATE )

    self.obj627=apply_contains(self)
    self.obj627.isGraphObjectVisual = True

    if(hasattr(self.obj627, '_setHierarchicalLink')):
      self.obj627._setHierarchicalLink(False)

    self.obj627.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,452.0,self.obj627)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj627.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj627)
    self.globalAndLocalPostcondition(self.obj627, rootNode)
    self.obj627.postAction( rootNode.CREATE )

    self.obj628=apply_contains(self)
    self.obj628.isGraphObjectVisual = True

    if(hasattr(self.obj628, '_setHierarchicalLink')):
      self.obj628._setHierarchicalLink(False)

    self.obj628.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,502.0,self.obj628)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj628.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj628)
    self.globalAndLocalPostcondition(self.obj628, rootNode)
    self.obj628.postAction( rootNode.CREATE )

    self.obj629=apply_contains(self)
    self.obj629.isGraphObjectVisual = True

    if(hasattr(self.obj629, '_setHierarchicalLink')):
      self.obj629._setHierarchicalLink(False)

    self.obj629.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(587.5,552.0,self.obj629)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj629.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj629)
    self.globalAndLocalPostcondition(self.obj629, rootNode)
    self.obj629.postAction( rootNode.CREATE )

    self.obj630=apply_contains(self)
    self.obj630.isGraphObjectVisual = True

    if(hasattr(self.obj630, '_setHierarchicalLink')):
      self.obj630._setHierarchicalLink(False)

    self.obj630.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,592.0,self.obj630)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj630.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj630)
    self.globalAndLocalPostcondition(self.obj630, rootNode)
    self.obj630.postAction( rootNode.CREATE )

    self.obj521=directLink_T(self)
    self.obj521.isGraphObjectVisual = True

    if(hasattr(self.obj521, '_setHierarchicalLink')):
      self.obj521._setHierarchicalLink(False)

    # associationType
    self.obj521.associationType.setValue('branches')

    self.obj521.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.0,491.0,self.obj521)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj521.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj521)
    self.globalAndLocalPostcondition(self.obj521, rootNode)
    self.obj521.postAction( rootNode.CREATE )

    self.obj532=directLink_T(self)
    self.obj532.isGraphObjectVisual = True

    if(hasattr(self.obj532, '_setHierarchicalLink')):
      self.obj532._setHierarchicalLink(False)

    # associationType
    self.obj532.associationType.setValue('p')

    self.obj532.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj532)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj532.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj532)
    self.globalAndLocalPostcondition(self.obj532, rootNode)
    self.obj532.postAction( rootNode.CREATE )

    self.obj537=directLink_T(self)
    self.obj537.isGraphObjectVisual = True

    if(hasattr(self.obj537, '_setHierarchicalLink')):
      self.obj537._setHierarchicalLink(False)

    # associationType
    self.obj537.associationType.setValue('p')

    self.obj537.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,491.0,self.obj537)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj537.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj537)
    self.globalAndLocalPostcondition(self.obj537, rootNode)
    self.obj537.postAction( rootNode.CREATE )

    self.obj540=directLink_T(self)
    self.obj540.isGraphObjectVisual = True

    if(hasattr(self.obj540, '_setHierarchicalLink')):
      self.obj540._setHierarchicalLink(False)

    # associationType
    self.obj540.associationType.setValue('p')

    self.obj540.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,541.0,self.obj540)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj540.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj540)
    self.globalAndLocalPostcondition(self.obj540, rootNode)
    self.obj540.postAction( rootNode.CREATE )

    self.obj586=directLink_T(self)
    self.obj586.isGraphObjectVisual = True

    if(hasattr(self.obj586, '_setHierarchicalLink')):
      self.obj586._setHierarchicalLink(False)

    # associationType
    self.obj586.associationType.setValue('branches')

    self.obj586.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(992.0,641.0,self.obj586)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj586.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj586)
    self.globalAndLocalPostcondition(self.obj586, rootNode)
    self.obj586.postAction( rootNode.CREATE )

    self.obj602=directLink_T(self)
    self.obj602.isGraphObjectVisual = True

    if(hasattr(self.obj602, '_setHierarchicalLink')):
      self.obj602._setHierarchicalLink(False)

    # associationType
    self.obj602.associationType.setValue('p')

    self.obj602.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(806.0,693.0,self.obj602)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj602.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj602)
    self.globalAndLocalPostcondition(self.obj602, rootNode)
    self.obj602.postAction( rootNode.CREATE )

    self.obj467=directLink_S(self)
    self.obj467.isGraphObjectVisual = True

    if(hasattr(self.obj467, '_setHierarchicalLink')):
      self.obj467._setHierarchicalLink(False)

    # associationType
    self.obj467.associationType.setValue('src')

    self.obj467.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,83.0,self.obj467)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj467.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj467)
    self.globalAndLocalPostcondition(self.obj467, rootNode)
    self.obj467.postAction( rootNode.CREATE )

    self.obj468=directLink_S(self)
    self.obj468.isGraphObjectVisual = True

    if(hasattr(self.obj468, '_setHierarchicalLink')):
      self.obj468._setHierarchicalLink(False)

    # associationType
    self.obj468.associationType.setValue('owningStateMachine')

    self.obj468.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,83.0,self.obj468)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj468.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj468)
    self.globalAndLocalPostcondition(self.obj468, rootNode)
    self.obj468.postAction( rootNode.CREATE )

    self.obj469=directLink_S(self)
    self.obj469.isGraphObjectVisual = True

    if(hasattr(self.obj469, '_setHierarchicalLink')):
      self.obj469._setHierarchicalLink(False)

    # associationType
    self.obj469.associationType.setValue('states')

    self.obj469.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(870.0,83.0,self.obj469)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj469.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj469)
    self.globalAndLocalPostcondition(self.obj469, rootNode)
    self.obj469.postAction( rootNode.CREATE )

    self.obj476=directLink_S(self)
    self.obj476.isGraphObjectVisual = True

    if(hasattr(self.obj476, '_setHierarchicalLink')):
      self.obj476._setHierarchicalLink(False)

    # associationType
    self.obj476.associationType.setValue('triggers')

    self.obj476.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(489.0,128.0,self.obj476)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj476.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj476)
    self.globalAndLocalPostcondition(self.obj476, rootNode)
    self.obj476.postAction( rootNode.CREATE )

    self.obj479=directLink_S(self)
    self.obj479.isGraphObjectVisual = True

    if(hasattr(self.obj479, '_setHierarchicalLink')):
      self.obj479._setHierarchicalLink(False)

    # associationType
    self.obj479.associationType.setValue('signal')

    self.obj479.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,183.0,self.obj479)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj479.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj479)
    self.globalAndLocalPostcondition(self.obj479, rootNode)
    self.obj479.postAction( rootNode.CREATE )

    self.obj484=directLink_S(self)
    self.obj484.isGraphObjectVisual = True

    if(hasattr(self.obj484, '_setHierarchicalLink')):
      self.obj484._setHierarchicalLink(False)

    # associationType
    self.obj484.associationType.setValue('outgoingTransitions')

    self.obj484.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(430.0,148.0,self.obj484)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj484.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj484)
    self.globalAndLocalPostcondition(self.obj484, rootNode)
    self.obj484.postAction( rootNode.CREATE )

    self.obj582=backward_link(self)
    self.obj582.isGraphObjectVisual = True

    if(hasattr(self.obj582, '_setHierarchicalLink')):
      self.obj582._setHierarchicalLink(False)

    # type
    self.obj582.type.setValue('ruleDef')

    self.obj582.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(460.0,339.0,self.obj582)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj582.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj582)
    self.globalAndLocalPostcondition(self.obj582, rootNode)
    self.obj582.postAction( rootNode.CREATE )

    self.obj631=backward_link(self)
    self.obj631.isGraphObjectVisual = True

    if(hasattr(self.obj631, '_setHierarchicalLink')):
      self.obj631._setHierarchicalLink(False)

    # type
    self.obj631.type.setValue('ruleDef')

    self.obj631.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(561.0,427.0,self.obj631)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj631.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj631)
    self.globalAndLocalPostcondition(self.obj631, rootNode)
    self.obj631.postAction( rootNode.CREATE )

    self.obj506=hasAttribute_S(self)
    self.obj506.isGraphObjectVisual = True

    if(hasattr(self.obj506, '_setHierarchicalLink')):
      self.obj506._setHierarchicalLink(False)

    self.obj506.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(972.0,178.5,self.obj506)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj506.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj506)
    self.globalAndLocalPostcondition(self.obj506, rootNode)
    self.obj506.postAction( rootNode.CREATE )

    self.obj513=hasAttribute_S(self)
    self.obj513.isGraphObjectVisual = True

    if(hasattr(self.obj513, '_setHierarchicalLink')):
      self.obj513._setHierarchicalLink(False)

    self.obj513.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(440.0,231.5,self.obj513)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj513.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj513)
    self.globalAndLocalPostcondition(self.obj513, rootNode)
    self.obj513.postAction( rootNode.CREATE )

    self.obj548=hasAttribute_T(self)
    self.obj548.isGraphObjectVisual = True

    if(hasattr(self.obj548, '_setHierarchicalLink')):
      self.obj548._setHierarchicalLink(False)

    self.obj548.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(573.0,442.5,self.obj548)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj548.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj548)
    self.globalAndLocalPostcondition(self.obj548, rootNode)
    self.obj548.postAction( rootNode.CREATE )

    self.obj565=hasAttribute_T(self)
    self.obj565.isGraphObjectVisual = True

    if(hasattr(self.obj565, '_setHierarchicalLink')):
      self.obj565._setHierarchicalLink(False)

    self.obj565.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(963.0,442.5,self.obj565)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj565.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj565)
    self.globalAndLocalPostcondition(self.obj565, rootNode)
    self.obj565.postAction( rootNode.CREATE )

    self.obj579=hasAttribute_T(self)
    self.obj579.isGraphObjectVisual = True

    if(hasattr(self.obj579, '_setHierarchicalLink')):
      self.obj579._setHierarchicalLink(False)

    self.obj579.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(383.0,532.5,self.obj579)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj579.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj579)
    self.globalAndLocalPostcondition(self.obj579, rootNode)
    self.obj579.postAction( rootNode.CREATE )

    self.obj595=hasAttribute_T(self)
    self.obj595.isGraphObjectVisual = True

    if(hasattr(self.obj595, '_setHierarchicalLink')):
      self.obj595._setHierarchicalLink(False)

    self.obj595.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1063.0,732.5,self.obj595)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj595.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj595)
    self.globalAndLocalPostcondition(self.obj595, rootNode)
    self.obj595.postAction( rootNode.CREATE )

    self.obj613=hasAttribute_T(self)
    self.obj613.isGraphObjectVisual = True

    if(hasattr(self.obj613, '_setHierarchicalLink')):
      self.obj613._setHierarchicalLink(False)

    self.obj613.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(763.0,812.5,self.obj613)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj613.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj613)
    self.globalAndLocalPostcondition(self.obj613, rootNode)
    self.obj613.postAction( rootNode.CREATE )

    self.obj517=leftExpr(self)
    self.obj517.isGraphObjectVisual = True

    if(hasattr(self.obj517, '_setHierarchicalLink')):
      self.obj517._setHierarchicalLink(False)

    self.obj517.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(401.0,321.5,self.obj517)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj517.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj517)
    self.globalAndLocalPostcondition(self.obj517, rootNode)
    self.obj517.postAction( rootNode.CREATE )

    self.obj554=leftExpr(self)
    self.obj554.isGraphObjectVisual = True

    if(hasattr(self.obj554, '_setHierarchicalLink')):
      self.obj554._setHierarchicalLink(False)

    self.obj554.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(616.0,358.5,self.obj554)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj554.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj554)
    self.globalAndLocalPostcondition(self.obj554, rootNode)
    self.obj554.postAction( rootNode.CREATE )

    self.obj567=leftExpr(self)
    self.obj567.isGraphObjectVisual = True

    if(hasattr(self.obj567, '_setHierarchicalLink')):
      self.obj567._setHierarchicalLink(False)

    self.obj567.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,356.5,self.obj567)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj567.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj567)
    self.globalAndLocalPostcondition(self.obj567, rootNode)
    self.obj567.postAction( rootNode.CREATE )

    self.obj580=leftExpr(self)
    self.obj580.isGraphObjectVisual = True

    if(hasattr(self.obj580, '_setHierarchicalLink')):
      self.obj580._setHierarchicalLink(False)

    self.obj580.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(386.0,616.5,self.obj580)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj580.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj580)
    self.globalAndLocalPostcondition(self.obj580, rootNode)
    self.obj580.postAction( rootNode.CREATE )

    self.obj599=leftExpr(self)
    self.obj599.isGraphObjectVisual = True

    if(hasattr(self.obj599, '_setHierarchicalLink')):
      self.obj599._setHierarchicalLink(False)

    self.obj599.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1066.0,816.5,self.obj599)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj599.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj599)
    self.globalAndLocalPostcondition(self.obj599, rootNode)
    self.obj599.postAction( rootNode.CREATE )

    self.obj617=leftExpr(self)
    self.obj617.isGraphObjectVisual = True

    if(hasattr(self.obj617, '_setHierarchicalLink')):
      self.obj617._setHierarchicalLink(False)

    self.obj617.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(781.5,856.5,self.obj617)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj617.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj617)
    self.globalAndLocalPostcondition(self.obj617, rootNode)
    self.obj617.postAction( rootNode.CREATE )

    self.obj518=rightExpr(self)
    self.obj518.isGraphObjectVisual = True

    if(hasattr(self.obj518, '_setHierarchicalLink')):
      self.obj518._setHierarchicalLink(False)

    self.obj518.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(295.0,312.5,self.obj518)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj518.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj518)
    self.globalAndLocalPostcondition(self.obj518, rootNode)
    self.obj518.postAction( rootNode.CREATE )

    self.obj555=rightExpr(self)
    self.obj555.isGraphObjectVisual = True

    if(hasattr(self.obj555, '_setHierarchicalLink')):
      self.obj555._setHierarchicalLink(False)

    self.obj555.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(648.0,251.5,self.obj555)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj555.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj555)
    self.globalAndLocalPostcondition(self.obj555, rootNode)
    self.obj555.postAction( rootNode.CREATE )

    self.obj566=rightExpr(self)
    self.obj566.isGraphObjectVisual = True

    if(hasattr(self.obj566, '_setHierarchicalLink')):
      self.obj566._setHierarchicalLink(False)

    self.obj566.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(886.0,356.5,self.obj566)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj566.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj566)
    self.globalAndLocalPostcondition(self.obj566, rootNode)
    self.obj566.postAction( rootNode.CREATE )

    self.obj581=rightExpr(self)
    self.obj581.isGraphObjectVisual = True

    if(hasattr(self.obj581, '_setHierarchicalLink')):
      self.obj581._setHierarchicalLink(False)

    self.obj581.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(316.0,616.5,self.obj581)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj581.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj581)
    self.globalAndLocalPostcondition(self.obj581, rootNode)
    self.obj581.postAction( rootNode.CREATE )

    self.obj600=rightExpr(self)
    self.obj600.isGraphObjectVisual = True

    if(hasattr(self.obj600, '_setHierarchicalLink')):
      self.obj600._setHierarchicalLink(False)

    self.obj600.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,816.5,self.obj600)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj600.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj600)
    self.globalAndLocalPostcondition(self.obj600, rootNode)
    self.obj600.postAction( rootNode.CREATE )

    self.obj618=rightExpr(self)
    self.obj618.isGraphObjectVisual = True

    if(hasattr(self.obj618, '_setHierarchicalLink')):
      self.obj618._setHierarchicalLink(False)

    self.obj618.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(631.5,856.5,self.obj618)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj618.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj618)
    self.globalAndLocalPostcondition(self.obj618, rootNode)
    self.obj618.postAction( rootNode.CREATE )

    # Connections for obj456 (graphObject_: Obj85) of type MatchModel
    self.drawConnections(
(self.obj456,self.obj458,[138.0, 51.0, 140.5, 192.0],"true", 2),
(self.obj456,self.obj482,[138.0, 51.0, 254.0, 67.0],"true", 0),
(self.obj456,self.obj619,[138.0, 51.0, 354.0, 67.0],"true", 0),
(self.obj456,self.obj620,[138.0, 51.0, 454.0, 67.0],"true", 0),
(self.obj456,self.obj621,[138.0, 51.0, 554.0, 67.0],"true", 0),
(self.obj456,self.obj622,[138.0, 51.0, 294.0, 117.0],"true", 0),
(self.obj456,self.obj623,[138.0, 51.0, 394.0, 117.0],"true", 0),
(self.obj456,self.obj624,[138.0, 51.0, 514.0, 117.0],"true", 0) )
    # Connections for obj457 (graphObject_: Obj86) of type ApplyModel
    self.drawConnections(
(self.obj457,self.obj524,[143.0, 413.0, 247.5, 452.0],"true", 0),
(self.obj457,self.obj625,[143.0, 413.0, 347.5, 452.0],"true", 0),
(self.obj457,self.obj626,[143.0, 413.0, 447.5, 452.0],"true", 0),
(self.obj457,self.obj627,[143.0, 413.0, 547.5, 452.0],"true", 0),
(self.obj457,self.obj628,[143.0, 413.0, 547.5, 502.0],"true", 0),
(self.obj457,self.obj629,[143.0, 413.0, 587.5, 552.0],"true", 0),
(self.obj457,self.obj630,[143.0, 413.0, 447.5, 592.0],"true", 0) )
    # Connections for obj463 (graphObject_: Obj92) named triggerS1
    self.drawConnections(
(self.obj463,self.obj479,[650.0, 183.0, 670.0, 183.0],"true", 2) )
    # Connections for obj464 (graphObject_: Obj93) named signal1
    self.drawConnections(
(self.obj464,self.obj506,[890.0, 183.0, 972.0, 178.5],"true", 2) )
    # Connections for obj459 (graphObject_: Obj88) named vertex1
    self.drawConnections(
(self.obj459,self.obj468,[570.0, 83.0, 670.0, 83.0],"true", 2) )
    # Connections for obj460 (graphObject_: Obj89) named transition1
    self.drawConnections(
(self.obj460,self.obj467,[370.0, 83.0, 470.0, 83.0],"true", 2),
(self.obj460,self.obj476,[370.0, 83.0, 489.0, 128.0],"true", 2) )
    # Connections for obj461 (graphObject_: Obj90) named statemachine1
    self.drawConnections(
(self.obj461,self.obj469,[770.0, 83.0, 870.0, 83.0],"true", 2) )
    # Connections for obj462 (graphObject_: Obj91) named state1
    self.drawConnections(
 )
    # Connections for obj483 (graphObject_: Obj100) named state2
    self.drawConnections(
(self.obj483,self.obj484,[450.0, 183.0, 430.0, 148.0],"true", 2),
(self.obj483,self.obj513,[450.0, 183.0, 440.0, 231.5],"true", 0) )
    # Connections for obj535 (graphObject_: Obj116) named triggerT1
    self.drawConnections(
(self.obj535,self.obj565,[952.0, 491.0, 963.0, 442.5],"true", 2) )
    # Connections for obj519 (graphObject_: Obj110) named listen1
    self.drawConnections(
(self.obj519,self.obj521,[352.0, 491.0, 452.0, 491.0],"true", 2),
(self.obj519,self.obj579,[352.0, 491.0, 383.0, 532.5],"true", 2),
(self.obj519,self.obj582,[352.0, 491.0, 460.0, 339.0],"true", 2) )
    # Connections for obj536 (graphObject_: Obj117) named listen2
    self.drawConnections(
(self.obj536,self.obj586,[952.0, 591.0, 992.0, 641.0],"true", 2) )
    # Connections for obj520 (graphObject_: Obj111) named listenbranch1
    self.drawConnections(
(self.obj520,self.obj532,[552.0, 491.0, 652.0, 491.0],"true", 2),
(self.obj520,self.obj548,[552.0, 491.0, 573.0, 442.5],"true", 2) )
    # Connections for obj583 (graphObject_: Obj138) named listenbranch2
    self.drawConnections(
(self.obj583,self.obj595,[1032.0, 691.0, 1063.0, 732.5],"true", 2),
(self.obj583,self.obj602,[1032.0, 691.0, 806.0, 693.0],"true", 2) )
    # Connections for obj601 (graphObject_: Obj146) named inst1
    self.drawConnections(
(self.obj601,self.obj613,[752.0, 771.0, 763.0, 812.5],"true", 2),
(self.obj601,self.obj631,[752.0, 771.0, 561.0, 427.0],"true", 2) )
    # Connections for obj529 (graphObject_: Obj114) named seq1
    self.drawConnections(
(self.obj529,self.obj537,[752.0, 491.0, 852.0, 491.0],"true", 2),
(self.obj529,self.obj540,[752.0, 491.0, 852.0, 541.0],"true", 2) )
    # Connections for obj503 (graphObject_: Obj102) named name
    self.drawConnections(
 )
    # Connections for obj507 (graphObject_: Obj104) named isComposite
    self.drawConnections(
 )
    # Connections for obj547 (graphObject_: Obj120) named channel
    self.drawConnections(
 )
    # Connections for obj559 (graphObject_: Obj126) named channel
    self.drawConnections(
 )
    # Connections for obj573 (graphObject_: Obj132) named pivotin
    self.drawConnections(
 )
    # Connections for obj592 (graphObject_: Obj141) named channel
    self.drawConnections(
 )
    # Connections for obj610 (graphObject_: Obj149) named pivotin
    self.drawConnections(
 )
    # Connections for obj514 (graphObject_: Obj107) named eq1
    self.drawConnections(
(self.obj514,self.obj517,[358.0, 359.0, 401.0, 321.5],"true", 2),
(self.obj514,self.obj518,[358.0, 359.0, 295.0, 312.5],"true", 2) )
    # Connections for obj551 (graphObject_: Obj122) named eq2
    self.drawConnections(
(self.obj551,self.obj554,[638.0, 323.0, 616.0, 358.5],"true", 2),
(self.obj551,self.obj555,[638.0, 323.0, 648.0, 251.5],"true", 2) )
    # Connections for obj556 (graphObject_: Obj125) named eq3
    self.drawConnections(
(self.obj556,self.obj566,[938.0, 319.0, 886.0, 356.5],"true", 2),
(self.obj556,self.obj567,[938.0, 319.0, 956.0, 356.5],"true", 2) )
    # Connections for obj576 (graphObject_: Obj133) named eq4
    self.drawConnections(
(self.obj576,self.obj580,[358.0, 659.0, 386.0, 616.5],"true", 2),
(self.obj576,self.obj581,[358.0, 659.0, 316.0, 616.5],"true", 2) )
    # Connections for obj596 (graphObject_: Obj143) named eq5
    self.drawConnections(
(self.obj596,self.obj599,[1038.0, 859.0, 1066.0, 816.5],"true", 2),
(self.obj596,self.obj600,[1038.0, 859.0, 996.0, 816.5],"true", 2) )
    # Connections for obj614 (graphObject_: Obj151) named eq6
    self.drawConnections(
(self.obj614,self.obj617,[709.0, 859.0, 781.5, 856.5],"true", 2),
(self.obj614,self.obj618,[709.0, 859.0, 631.5, 856.5],"true", 2) )
    # Connections for obj510 (graphObject_: Obj105) named true
    self.drawConnections(
 )
    # Connections for obj562 (graphObject_: Obj127) named exit_in
    self.drawConnections(
 )
    # Connections for obj568 (graphObject_: Obj131) named listenhproc
    self.drawConnections(
 )
    # Connections for obj587 (graphObject_: Obj140) named exack_in
    self.drawConnections(
 )
    # Connections for obj607 (graphObject_: Obj148) named instfortrans
    self.drawConnections(
 )
    # Connections for obj458 (graphObject_: Obj87) of type paired_with
    self.drawConnections(
(self.obj458,self.obj457,[140.5, 192.0, 143.0, 413.0],"true", 2) )
    # Connections for obj482 (graphObject_: Obj99) of type match_contains
    self.drawConnections(
(self.obj482,self.obj460,[254.0, 67.0, 370.0, 83.0],"true", 2) )
    # Connections for obj619 (graphObject_: Obj154) of type match_contains
    self.drawConnections(
(self.obj619,self.obj459,[354.0, 67.0, 570.0, 83.0],"true", 2) )
    # Connections for obj620 (graphObject_: Obj155) of type match_contains
    self.drawConnections(
(self.obj620,self.obj461,[454.0, 67.0, 770.0, 83.0],"true", 2) )
    # Connections for obj621 (graphObject_: Obj156) of type match_contains
    self.drawConnections(
(self.obj621,self.obj462,[554.0, 67.0, 970.0, 83.0],"true", 2) )
    # Connections for obj622 (graphObject_: Obj157) of type match_contains
    self.drawConnections(
(self.obj622,self.obj483,[294.0, 117.0, 450.0, 183.0],"true", 2) )
    # Connections for obj623 (graphObject_: Obj158) of type match_contains
    self.drawConnections(
(self.obj623,self.obj463,[394.0, 117.0, 650.0, 183.0],"true", 2) )
    # Connections for obj624 (graphObject_: Obj159) of type match_contains
    self.drawConnections(
(self.obj624,self.obj464,[514.0, 117.0, 890.0, 183.0],"true", 2) )
    # Connections for obj524 (graphObject_: Obj113) of type apply_contains
    self.drawConnections(
(self.obj524,self.obj519,[247.5, 452.0, 352.0, 491.0],"true", 2) )
    # Connections for obj625 (graphObject_: Obj160) of type apply_contains
    self.drawConnections(
(self.obj625,self.obj520,[347.5, 452.0, 552.0, 491.0],"true", 2) )
    # Connections for obj626 (graphObject_: Obj161) of type apply_contains
    self.drawConnections(
(self.obj626,self.obj529,[447.5, 452.0, 752.0, 491.0],"true", 2) )
    # Connections for obj627 (graphObject_: Obj162) of type apply_contains
    self.drawConnections(
(self.obj627,self.obj535,[547.5, 452.0, 952.0, 491.0],"true", 2) )
    # Connections for obj628 (graphObject_: Obj163) of type apply_contains
    self.drawConnections(
(self.obj628,self.obj536,[547.5, 502.0, 952.0, 591.0],"true", 2) )
    # Connections for obj629 (graphObject_: Obj164) of type apply_contains
    self.drawConnections(
(self.obj629,self.obj583,[587.5, 552.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj630 (graphObject_: Obj165) of type apply_contains
    self.drawConnections(
(self.obj630,self.obj601,[447.5, 592.0, 752.0, 771.0],"true", 2) )
    # Connections for obj521 (graphObject_: Obj112) of type directLink_T
    self.drawConnections(
(self.obj521,self.obj520,[452.0, 491.0, 552.0, 491.0],"true", 2) )
    # Connections for obj532 (graphObject_: Obj115) of type directLink_T
    self.drawConnections(
(self.obj532,self.obj529,[652.0, 491.0, 752.0, 491.0],"true", 2) )
    # Connections for obj537 (graphObject_: Obj118) of type directLink_T
    self.drawConnections(
(self.obj537,self.obj535,[852.0, 491.0, 952.0, 491.0],"true", 2) )
    # Connections for obj540 (graphObject_: Obj119) of type directLink_T
    self.drawConnections(
(self.obj540,self.obj536,[852.0, 541.0, 952.0, 591.0],"true", 2) )
    # Connections for obj586 (graphObject_: Obj139) of type directLink_T
    self.drawConnections(
(self.obj586,self.obj583,[992.0, 641.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj602 (graphObject_: Obj147) of type directLink_T
    self.drawConnections(
(self.obj602,self.obj601,[806.0, 693.0, 752.0, 771.0],"true", 2) )
    # Connections for obj467 (graphObject_: Obj94) of type directLink_S
    self.drawConnections(
(self.obj467,self.obj459,[470.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj468 (graphObject_: Obj95) of type directLink_S
    self.drawConnections(
(self.obj468,self.obj461,[670.0, 83.0, 770.0, 83.0],"true", 2) )
    # Connections for obj469 (graphObject_: Obj96) of type directLink_S
    self.drawConnections(
(self.obj469,self.obj462,[870.0, 83.0, 970.0, 83.0],"true", 2) )
    # Connections for obj476 (graphObject_: Obj97) of type directLink_S
    self.drawConnections(
(self.obj476,self.obj463,[470.0, 133.0, 650.0, 183.0],"true", 2) )
    # Connections for obj479 (graphObject_: Obj98) of type directLink_S
    self.drawConnections(
(self.obj479,self.obj464,[670.0, 183.0, 890.0, 183.0],"true", 2) )
    # Connections for obj484 (graphObject_: Obj101) of type directLink_S
    self.drawConnections(
(self.obj484,self.obj460,[400.0, 133.0, 370.0, 83.0],"true", 2) )
    # Connections for obj582 (graphObject_: Obj137) of type backward_link
    self.drawConnections(
(self.obj582,self.obj483,[401.0, 337.0, 450.0, 183.0],"true", 2) )
    # Connections for obj631 (graphObject_: Obj166) of type backward_link
    self.drawConnections(
(self.obj631,self.obj460,[561.0, 427.0, 370.0, 83.0],"true", 2) )
    # Connections for obj506 (graphObject_: Obj103) of type hasAttribute_S
    self.drawConnections(
(self.obj506,self.obj503,[972.0, 178.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj513 (graphObject_: Obj106) of type hasAttribute_S
    self.drawConnections(
(self.obj513,self.obj507,[462.0, 228.5, 434.0, 274.0],"true", 2) )
    # Connections for obj548 (graphObject_: Obj121) of type hasAttribute_T
    self.drawConnections(
(self.obj548,self.obj547,[573.0, 442.5, 594.0, 394.0],"true", 2) )
    # Connections for obj565 (graphObject_: Obj128) of type hasAttribute_T
    self.drawConnections(
(self.obj565,self.obj559,[963.0, 442.5, 974.0, 394.0],"true", 2) )
    # Connections for obj579 (graphObject_: Obj134) of type hasAttribute_T
    self.drawConnections(
(self.obj579,self.obj573,[383.0, 532.5, 414.0, 574.0],"true", 2) )
    # Connections for obj595 (graphObject_: Obj142) of type hasAttribute_T
    self.drawConnections(
(self.obj595,self.obj592,[1063.0, 732.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj613 (graphObject_: Obj150) of type hasAttribute_T
    self.drawConnections(
(self.obj613,self.obj610,[763.0, 812.5, 854.0, 854.0],"true", 2) )
    # Connections for obj517 (graphObject_: Obj108) of type leftExpr
    self.drawConnections(
(self.obj517,self.obj507,[456.0, 316.5, 434.0, 274.0],"true", 2) )
    # Connections for obj554 (graphObject_: Obj123) of type leftExpr
    self.drawConnections(
(self.obj554,self.obj547,[616.0, 358.5, 594.0, 394.0],"true", 2) )
    # Connections for obj567 (graphObject_: Obj130) of type leftExpr
    self.drawConnections(
(self.obj567,self.obj559,[956.0, 356.5, 974.0, 394.0],"true", 2) )
    # Connections for obj580 (graphObject_: Obj135) of type leftExpr
    self.drawConnections(
(self.obj580,self.obj573,[386.0, 616.5, 414.0, 574.0],"true", 2) )
    # Connections for obj599 (graphObject_: Obj144) of type leftExpr
    self.drawConnections(
(self.obj599,self.obj592,[1066.0, 816.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj617 (graphObject_: Obj152) of type leftExpr
    self.drawConnections(
(self.obj617,self.obj610,[781.5, 856.5, 854.0, 854.0],"true", 2) )
    # Connections for obj518 (graphObject_: Obj109) of type rightExpr
    self.drawConnections(
(self.obj518,self.obj510,[376.0, 316.5, 294.0, 274.0],"true", 2) )
    # Connections for obj555 (graphObject_: Obj124) of type rightExpr
    self.drawConnections(
(self.obj555,self.obj503,[648.0, 251.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj566 (graphObject_: Obj129) of type rightExpr
    self.drawConnections(
(self.obj566,self.obj562,[886.0, 356.5, 834.0, 394.0],"true", 2) )
    # Connections for obj581 (graphObject_: Obj136) of type rightExpr
    self.drawConnections(
(self.obj581,self.obj568,[316.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj600 (graphObject_: Obj145) of type rightExpr
    self.drawConnections(
(self.obj600,self.obj587,[996.0, 816.5, 954.0, 774.0],"true", 2) )
    # Connections for obj618 (graphObject_: Obj153) of type rightExpr
    self.drawConnections(
(self.obj618,self.obj607,[631.5, 856.5, 554.0, 854.0],"true", 2) )

newfunction = Transition2HListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
