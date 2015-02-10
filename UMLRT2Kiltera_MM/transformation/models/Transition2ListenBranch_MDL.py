"""
__Transition2ListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Feb  9 22:00:46 2015
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


    self.obj100=MatchModel(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    self.obj100.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,21.0,self.obj100)
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
       new_obj = graph_ApplyModel(24.0,342.0,self.obj101)
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
       new_obj = graph_Trigger_S(860.0,180.0,self.obj102)
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
       new_obj = graph_Signal(647.0,140.0,self.obj103)
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

    self.obj104=Transition(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # name
    self.obj104.name.setValue('transition1')

    # classtype
    self.obj104.classtype.setValue('Transition')

    # cardinality
    self.obj104.cardinality.setValue('+')

    self.obj104.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(834.0,80.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=State(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # name
    self.obj105.name.setValue('state1')

    # classtype
    self.obj105.classtype.setValue('State')

    # cardinality
    self.obj105.cardinality.setValue('+')

    self.obj105.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,80.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Listen(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # classtype
    self.obj106.classtype.setValue('Listen')

    # cardinality
    self.obj106.cardinality.setValue('1')

    # name
    self.obj106.name.setValue('listen1')

    self.obj106.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,438.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=ListenBranch(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # classtype
    self.obj107.classtype.setValue('ListenBranch')

    # cardinality
    self.obj107.cardinality.setValue('1')

    # name
    self.obj107.name.setValue('listenBranch1')

    self.obj107.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(400.0,440.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
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
       new_obj = graph_Inst(760.0,437.0,self.obj108)
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

    self.obj109=Attribute(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # Type
    self.obj109.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj109.Type.config = 0

    # name
    self.obj109.name.setValue('isComposite')

    self.obj109.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,175.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
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
    self.obj110.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj110.Type.config = 0

    # name
    self.obj110.name.setValue('hasOutgoingTransitions')

    self.obj110.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(340.0,160.0,self.obj110)
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
    self.obj111.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj111.Type.config = 0

    # name
    self.obj111.name.setValue('name')

    self.obj111.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,240.0,self.obj111)
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
    self.obj112.name.setValue('channel')

    self.obj112.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(405.0,361.0,self.obj112)
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
       new_obj = graph_Attribute(80.0,540.0,self.obj113)
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
       new_obj = graph_Attribute(720.0,540.0,self.obj114)
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
       new_obj = graph_Equation(303.0,242.0,self.obj115)
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
       new_obj = graph_Equation(500.0,240.0,self.obj116)
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
       new_obj = graph_Equation(567.0,361.0,self.obj117)
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
       new_obj = graph_Equation(200.0,620.0,self.obj118)
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

    self.obj119=Equation(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # name
    self.obj119.name.setValue('eq5')

    self.obj119.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,620.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
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
    self.obj120.name.setValue('false')

    self.obj120.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,260.0,self.obj120)
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
    self.obj121.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj121.Type.config = 0

    # name
    self.obj121.name.setValue('true')

    self.obj121.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(500.0,160.0,self.obj121)
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
    self.obj122.name.setValue('listensimplestate')

    self.obj122.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,540.0,self.obj122)
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
    self.obj123.name.setValue('instfortrans')

    self.obj123.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(920.0,540.0,self.obj123)
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

    self.obj124=paired_with(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    self.obj124.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(142.5,213.5,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=match_contains(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    self.obj125.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,87.5,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
       new_obj = graph_match_contains(571.0,87.5,self.obj126)
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
       new_obj = graph_match_contains(477.5,117.5,self.obj127)
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
       new_obj = graph_match_contains(582.0,107.5,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=apply_contains(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    self.obj129.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,417.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
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
       new_obj = graph_apply_contains(359.5,432.0,self.obj130)
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
       new_obj = graph_apply_contains(539.5,431.5,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=directLink_T(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # associationType
    self.obj132.associationType.setValue('branches')

    self.obj132.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(399.0,484.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=directLink_T(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # associationType
    self.obj133.associationType.setValue('p')

    self.obj133.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,490.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=directLink_S(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # associationType
    self.obj134.associationType.setValue('outgoingTransitions')

    self.obj134.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,123.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=directLink_S(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # associationType
    self.obj135.associationType.setValue('triggers')

    self.obj135.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(1024.5,181.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=directLink_S(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # associationType
    self.obj136.associationType.setValue('signal')

    self.obj136.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(848.0,187.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=backward_link(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # type
    self.obj137.type.setValue('ruleDef')

    self.obj137.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,287.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=backward_link(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # type
    self.obj138.type.setValue('ruleDef')

    self.obj138.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(968.0,305.5,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=hasAttribute_S(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    self.obj139.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,166.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=hasAttribute_S(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    self.obj140.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(402.0,158.5,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=hasAttribute_S(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    self.obj141.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(815.5,228.5,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=hasAttribute_T(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(555.5,442.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=hasAttribute_T(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    self.obj143.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(283.0,531.5,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
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
       new_obj = graph_hasAttribute_T(893.0,531.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=leftExpr(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    self.obj145.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(367.5,245.0,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=leftExpr(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    self.obj146.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(556.0,236.5,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
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
       new_obj = graph_leftExpr(622.0,397.5,self.obj147)
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
       new_obj = graph_leftExpr(276.0,616.5,self.obj148)
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
       new_obj = graph_leftExpr(896.0,616.5,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=rightExpr(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    self.obj150.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(367.5,287.5,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
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
       new_obj = graph_rightExpr(636.0,236.5,self.obj151)
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
       new_obj = graph_rightExpr(759.5,337.0,self.obj152)
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
       new_obj = graph_rightExpr(356.0,616.5,self.obj153)
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
       new_obj = graph_rightExpr(996.0,616.5,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj124,[138.0, 52.0, 142.5, 213.5],"true", 2),
(self.obj100,self.obj125,[138.0, 52.0, 234.0, 87.5],"true", 2),
(self.obj100,self.obj126,[138.0, 52.0, 571.0, 87.5],"true", 2),
(self.obj100,self.obj127,[138.0, 52.0, 477.5, 117.5],"true", 2),
(self.obj100,self.obj128,[138.0, 52.0, 582.0, 107.5],"true", 2) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj129,[147.0, 375.0, 219.5, 417.0],"true", 2),
(self.obj101,self.obj130,[147.0, 375.0, 359.5, 432.0],"true", 2),
(self.obj101,self.obj131,[147.0, 375.0, 539.5, 431.5],"true", 2) )
    # Connections for obj102 (graphObject_: Obj2) named triggerS1
    self.drawConnections(
(self.obj102,self.obj136,[1030.0, 223.0, 848.0, 187.0],"true", 2) )
    # Connections for obj103 (graphObject_: Obj3) named signal1
    self.drawConnections(
(self.obj103,self.obj141,[817.0, 183.0, 815.5, 228.5],"true", 2) )
    # Connections for obj104 (graphObject_: Obj4) named transition1
    self.drawConnections(
(self.obj104,self.obj135,[1004.0, 123.0, 1024.5, 181.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) named state1
    self.drawConnections(
(self.obj105,self.obj134,[330.0, 123.0, 480.0, 123.0],"true", 2),
(self.obj105,self.obj139,[330.0, 123.0, 312.0, 166.0],"true", 2),
(self.obj105,self.obj140,[330.0, 123.0, 402.0, 158.5],"true", 2) )
    # Connections for obj106 (graphObject_: Obj6) named listen1
    self.drawConnections(
(self.obj106,self.obj137,[352.0, 489.0, 341.0, 287.0],"true", 2),
(self.obj106,self.obj132,[352.0, 489.0, 399.0, 484.0],"true", 2),
(self.obj106,self.obj143,[352.0, 489.0, 283.0, 531.5],"true", 2) )
    # Connections for obj107 (graphObject_: Obj7) named listenBranch1
    self.drawConnections(
(self.obj107,self.obj142,[572.0, 491.0, 555.5, 442.0],"true", 2),
(self.obj107,self.obj133,[572.0, 491.0, 752.0, 490.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj8) named inst1
    self.drawConnections(
(self.obj108,self.obj138,[932.0, 488.0, 968.0, 305.5],"true", 2),
(self.obj108,self.obj144,[932.0, 488.0, 893.0, 531.0],"true", 2) )
    # Connections for obj109 (graphObject_: Obj9) named isComposite
    self.drawConnections(
 )
    # Connections for obj110 (graphObject_: Obj10) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj111 (graphObject_: Obj11) named name
    self.drawConnections(
 )
    # Connections for obj112 (graphObject_: Obj12) named channel
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
(self.obj115,self.obj145,[441.0, 281.0, 367.5, 245.0],"true", 2),
(self.obj115,self.obj150,[441.0, 281.0, 367.5, 287.5],"true", 2) )
    # Connections for obj116 (graphObject_: Obj16) named eq2
    self.drawConnections(
(self.obj116,self.obj151,[638.0, 279.0, 636.0, 236.5],"true", 2),
(self.obj116,self.obj146,[638.0, 279.0, 556.0, 236.5],"true", 2) )
    # Connections for obj117 (graphObject_: Obj17) named eq3
    self.drawConnections(
(self.obj117,self.obj152,[705.0, 400.0, 759.5, 337.0],"true", 2),
(self.obj117,self.obj147,[705.0, 400.0, 622.0, 397.5],"true", 2) )
    # Connections for obj118 (graphObject_: Obj18) named eq4
    self.drawConnections(
(self.obj118,self.obj148,[338.0, 659.0, 276.0, 616.5],"true", 2),
(self.obj118,self.obj153,[338.0, 659.0, 356.0, 616.5],"true", 2) )
    # Connections for obj119 (graphObject_: Obj19) named eq5
    self.drawConnections(
(self.obj119,self.obj149,[938.0, 659.0, 896.0, 616.5],"true", 2),
(self.obj119,self.obj154,[938.0, 659.0, 996.0, 616.5],"true", 2) )
    # Connections for obj120 (graphObject_: Obj20) named false
    self.drawConnections(
 )
    # Connections for obj121 (graphObject_: Obj21) named true
    self.drawConnections(
 )
    # Connections for obj122 (graphObject_: Obj22) named listensimplestate
    self.drawConnections(
 )
    # Connections for obj123 (graphObject_: Obj23) named instfortrans
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj24) of type paired_with
    self.drawConnections(
(self.obj124,self.obj101,[142.5, 213.5, 147.0, 375.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj25) of type match_contains
    self.drawConnections(
(self.obj125,self.obj105,[234.0, 87.5, 330.0, 123.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj26) of type match_contains
    self.drawConnections(
(self.obj126,self.obj104,[571.0, 87.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj27) of type match_contains
    self.drawConnections(
(self.obj127,self.obj103,[477.5, 117.5, 817.0, 183.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj28) of type match_contains
    self.drawConnections(
(self.obj128,self.obj102,[582.0, 107.5, 1030.0, 223.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj29) of type apply_contains
    self.drawConnections(
(self.obj129,self.obj106,[219.5, 417.0, 352.0, 489.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj30) of type apply_contains
    self.drawConnections(
(self.obj130,self.obj107,[359.5, 432.0, 572.0, 491.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj31) of type apply_contains
    self.drawConnections(
(self.obj131,self.obj108,[539.5, 431.5, 932.0, 488.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj32) of type directLink_T
    self.drawConnections(
(self.obj132,self.obj107,[399.0, 484.0, 572.0, 491.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj33) of type directLink_T
    self.drawConnections(
(self.obj133,self.obj108,[752.0, 490.0, 932.0, 488.0],"true", 2) )
    # Connections for obj134 (graphObject_: Obj34) of type directLink_S
    self.drawConnections(
(self.obj134,self.obj104,[480.0, 123.0, 1004.0, 123.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj35) of type directLink_S
    self.drawConnections(
(self.obj135,self.obj102,[984.5, 193.0, 1030.0, 223.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj36) of type directLink_S
    self.drawConnections(
(self.obj136,self.obj103,[848.0, 187.0, 817.0, 183.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj37) of type backward_link
    self.drawConnections(
(self.obj137,self.obj105,[341.0, 287.0, 330.0, 123.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj38) of type backward_link
    self.drawConnections(
(self.obj138,self.obj104,[968.0, 305.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj39) of type hasAttribute_S
    self.drawConnections(
(self.obj139,self.obj109,[312.0, 166.0, 294.0, 209.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj40) of type hasAttribute_S
    self.drawConnections(
(self.obj140,self.obj110,[402.0, 158.5, 474.0, 194.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj41) of type hasAttribute_S
    self.drawConnections(
(self.obj141,self.obj111,[815.5, 228.5, 814.0, 274.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj42) of type hasAttribute_T
    self.drawConnections(
(self.obj142,self.obj112,[555.5, 442.0, 539.0, 395.0],"true", 2) )
    # Connections for obj143 (graphObject_: Obj43) of type hasAttribute_T
    self.drawConnections(
(self.obj143,self.obj113,[283.0, 531.5, 214.0, 574.0],"true", 2) )
    # Connections for obj144 (graphObject_: Obj44) of type hasAttribute_T
    self.drawConnections(
(self.obj144,self.obj114,[893.0, 531.0, 854.0, 574.0],"true", 2) )
    # Connections for obj145 (graphObject_: Obj45) of type leftExpr
    self.drawConnections(
(self.obj145,self.obj109,[367.5, 245.0, 294.0, 209.0],"true", 2) )
    # Connections for obj146 (graphObject_: Obj46) of type leftExpr
    self.drawConnections(
(self.obj146,self.obj110,[556.0, 236.5, 474.0, 194.0],"true", 2) )
    # Connections for obj147 (graphObject_: Obj47) of type leftExpr
    self.drawConnections(
(self.obj147,self.obj112,[622.0, 397.5, 539.0, 395.0],"true", 2) )
    # Connections for obj148 (graphObject_: Obj48) of type leftExpr
    self.drawConnections(
(self.obj148,self.obj113,[276.0, 616.5, 214.0, 574.0],"true", 2) )
    # Connections for obj149 (graphObject_: Obj49) of type leftExpr
    self.drawConnections(
(self.obj149,self.obj114,[896.0, 616.5, 854.0, 574.0],"true", 2) )
    # Connections for obj150 (graphObject_: Obj50) of type rightExpr
    self.drawConnections(
(self.obj150,self.obj120,[367.5, 287.5, 294.0, 294.0],"true", 2) )
    # Connections for obj151 (graphObject_: Obj51) of type rightExpr
    self.drawConnections(
(self.obj151,self.obj121,[636.0, 236.5, 634.0, 194.0],"true", 2) )
    # Connections for obj152 (graphObject_: Obj52) of type rightExpr
    self.drawConnections(
(self.obj152,self.obj111,[759.5, 337.0, 814.0, 274.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj53) of type rightExpr
    self.drawConnections(
(self.obj153,self.obj122,[356.0, 616.5, 374.0, 574.0],"true", 2) )
    # Connections for obj154 (graphObject_: Obj54) of type rightExpr
    self.drawConnections(
(self.obj154,self.obj123,[996.0, 616.5, 1054.0, 574.0],"true", 2) )

newfunction = Transition2ListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
