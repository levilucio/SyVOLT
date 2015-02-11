"""
__Transition2HListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 15:07:50 2015
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


    self.obj830=MatchModel(self)
    self.obj830.isGraphObjectVisual = True

    if(hasattr(self.obj830, '_setHierarchicalLink')):
      self.obj830._setHierarchicalLink(False)

    self.obj830.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj830)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj830.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj830)
    self.globalAndLocalPostcondition(self.obj830, rootNode)
    self.obj830.postAction( rootNode.CREATE )

    self.obj831=ApplyModel(self)
    self.obj831.isGraphObjectVisual = True

    if(hasattr(self.obj831, '_setHierarchicalLink')):
      self.obj831._setHierarchicalLink(False)

    self.obj831.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,380.0,self.obj831)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj831.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj831)
    self.globalAndLocalPostcondition(self.obj831, rootNode)
    self.obj831.postAction( rootNode.CREATE )

    self.obj832=Trigger_S(self)
    self.obj832.isGraphObjectVisual = True

    if(hasattr(self.obj832, '_setHierarchicalLink')):
      self.obj832._setHierarchicalLink(False)

    # classtype
    self.obj832.classtype.setValue('Trigger_S')

    # cardinality
    self.obj832.cardinality.setValue('1')

    # name
    self.obj832.name.setValue('triggerS1')

    self.obj832.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(480.0,140.0,self.obj832)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj832.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj832)
    self.globalAndLocalPostcondition(self.obj832, rootNode)
    self.obj832.postAction( rootNode.CREATE )

    self.obj833=Signal(self)
    self.obj833.isGraphObjectVisual = True

    if(hasattr(self.obj833, '_setHierarchicalLink')):
      self.obj833._setHierarchicalLink(False)

    # name
    self.obj833.name.setValue('signal1')

    # classtype
    self.obj833.classtype.setValue('Signal')

    # cardinality
    self.obj833.cardinality.setValue('1')

    self.obj833.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(720.0,140.0,self.obj833)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj833.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj833)
    self.globalAndLocalPostcondition(self.obj833, rootNode)
    self.obj833.postAction( rootNode.CREATE )

    self.obj834=Vertex(self)
    self.obj834.isGraphObjectVisual = True

    if(hasattr(self.obj834, '_setHierarchicalLink')):
      self.obj834._setHierarchicalLink(False)

    # name
    self.obj834.name.setValue('vertex1')

    # classtype
    self.obj834.classtype.setValue('Vertex')

    # cardinality
    self.obj834.cardinality.setValue('+')

    self.obj834.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(400.0,40.0,self.obj834)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj834.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj834)
    self.globalAndLocalPostcondition(self.obj834, rootNode)
    self.obj834.postAction( rootNode.CREATE )

    self.obj835=Transition(self)
    self.obj835.isGraphObjectVisual = True

    if(hasattr(self.obj835, '_setHierarchicalLink')):
      self.obj835._setHierarchicalLink(False)

    # name
    self.obj835.name.setValue('transition1')

    # classtype
    self.obj835.classtype.setValue('Transition')

    # cardinality
    self.obj835.cardinality.setValue('+')

    self.obj835.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(200.0,40.0,self.obj835)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj835.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj835)
    self.globalAndLocalPostcondition(self.obj835, rootNode)
    self.obj835.postAction( rootNode.CREATE )

    self.obj836=StateMachine(self)
    self.obj836.isGraphObjectVisual = True

    if(hasattr(self.obj836, '_setHierarchicalLink')):
      self.obj836._setHierarchicalLink(False)

    # name
    self.obj836.name.setValue('statemachine1')

    # classtype
    self.obj836.classtype.setValue('StateMachine')

    # cardinality
    self.obj836.cardinality.setValue('+')

    self.obj836.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(600.0,40.0,self.obj836)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj836.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj836)
    self.globalAndLocalPostcondition(self.obj836, rootNode)
    self.obj836.postAction( rootNode.CREATE )

    self.obj837=State(self)
    self.obj837.isGraphObjectVisual = True

    if(hasattr(self.obj837, '_setHierarchicalLink')):
      self.obj837._setHierarchicalLink(False)

    # name
    self.obj837.name.setValue('state1')

    # classtype
    self.obj837.classtype.setValue('State')

    # cardinality
    self.obj837.cardinality.setValue('1')

    self.obj837.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(800.0,40.0,self.obj837)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj837.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj837)
    self.globalAndLocalPostcondition(self.obj837, rootNode)
    self.obj837.postAction( rootNode.CREATE )

    self.obj838=State(self)
    self.obj838.isGraphObjectVisual = True

    if(hasattr(self.obj838, '_setHierarchicalLink')):
      self.obj838._setHierarchicalLink(False)

    # name
    self.obj838.name.setValue('state2')

    # classtype
    self.obj838.classtype.setValue('State')

    # cardinality
    self.obj838.cardinality.setValue('+')

    self.obj838.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(280.0,140.0,self.obj838)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj838.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj838)
    self.globalAndLocalPostcondition(self.obj838, rootNode)
    self.obj838.postAction( rootNode.CREATE )

    self.obj839=Trigger_T(self)
    self.obj839.isGraphObjectVisual = True

    if(hasattr(self.obj839, '_setHierarchicalLink')):
      self.obj839._setHierarchicalLink(False)

    # classtype
    self.obj839.classtype.setValue('Trigger_T')

    # cardinality
    self.obj839.cardinality.setValue('1')

    # name
    self.obj839.name.setValue('triggerT1')

    self.obj839.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(780.0,440.0,self.obj839)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj839.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj839)
    self.globalAndLocalPostcondition(self.obj839, rootNode)
    self.obj839.postAction( rootNode.CREATE )

    self.obj840=Listen(self)
    self.obj840.isGraphObjectVisual = True

    if(hasattr(self.obj840, '_setHierarchicalLink')):
      self.obj840._setHierarchicalLink(False)

    # classtype
    self.obj840.classtype.setValue('Listen')

    # cardinality
    self.obj840.cardinality.setValue('1')

    # name
    self.obj840.name.setValue('listen1')

    self.obj840.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,440.0,self.obj840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj840)
    self.globalAndLocalPostcondition(self.obj840, rootNode)
    self.obj840.postAction( rootNode.CREATE )

    self.obj841=Listen(self)
    self.obj841.isGraphObjectVisual = True

    if(hasattr(self.obj841, '_setHierarchicalLink')):
      self.obj841._setHierarchicalLink(False)

    # classtype
    self.obj841.classtype.setValue('Listen')

    # cardinality
    self.obj841.cardinality.setValue('1')

    # name
    self.obj841.name.setValue('listen2')

    self.obj841.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(780.0,540.0,self.obj841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj841)
    self.globalAndLocalPostcondition(self.obj841, rootNode)
    self.obj841.postAction( rootNode.CREATE )

    self.obj842=ListenBranch(self)
    self.obj842.isGraphObjectVisual = True

    if(hasattr(self.obj842, '_setHierarchicalLink')):
      self.obj842._setHierarchicalLink(False)

    # classtype
    self.obj842.classtype.setValue('ListenBranch')

    # cardinality
    self.obj842.cardinality.setValue('1')

    # name
    self.obj842.name.setValue('listenbranch1')

    self.obj842.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(380.0,440.0,self.obj842)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj842.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj842)
    self.globalAndLocalPostcondition(self.obj842, rootNode)
    self.obj842.postAction( rootNode.CREATE )

    self.obj843=ListenBranch(self)
    self.obj843.isGraphObjectVisual = True

    if(hasattr(self.obj843, '_setHierarchicalLink')):
      self.obj843._setHierarchicalLink(False)

    # classtype
    self.obj843.classtype.setValue('ListenBranch')

    # cardinality
    self.obj843.cardinality.setValue('1')

    # name
    self.obj843.name.setValue('listenbranch2')

    self.obj843.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(860.0,640.0,self.obj843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj843)
    self.globalAndLocalPostcondition(self.obj843, rootNode)
    self.obj843.postAction( rootNode.CREATE )

    self.obj844=Inst(self)
    self.obj844.isGraphObjectVisual = True

    if(hasattr(self.obj844, '_setHierarchicalLink')):
      self.obj844._setHierarchicalLink(False)

    # classtype
    self.obj844.classtype.setValue('Inst')

    # cardinality
    self.obj844.cardinality.setValue('1')

    # name
    self.obj844.name.setValue('inst1')

    self.obj844.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(580.0,720.0,self.obj844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj844)
    self.globalAndLocalPostcondition(self.obj844, rootNode)
    self.obj844.postAction( rootNode.CREATE )

    self.obj845=Seq(self)
    self.obj845.isGraphObjectVisual = True

    if(hasattr(self.obj845, '_setHierarchicalLink')):
      self.obj845._setHierarchicalLink(False)

    # name
    self.obj845.name.setValue('seq1')

    # classtype
    self.obj845.classtype.setValue('Seq')

    # cardinality
    self.obj845.cardinality.setValue('1')

    self.obj845.graphClass_= graph_Seq
    if self.genGraphics:
       new_obj = graph_Seq(580.0,440.0,self.obj845)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Seq", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj845.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj845)
    self.globalAndLocalPostcondition(self.obj845, rootNode)
    self.obj845.postAction( rootNode.CREATE )

    self.obj846=Attribute(self)
    self.obj846.isGraphObjectVisual = True

    if(hasattr(self.obj846, '_setHierarchicalLink')):
      self.obj846._setHierarchicalLink(False)

    # Type
    self.obj846.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj846.Type.config = 0

    # name
    self.obj846.name.setValue('name')

    self.obj846.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(920.0,140.0,self.obj846)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj846.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj846)
    self.globalAndLocalPostcondition(self.obj846, rootNode)
    self.obj846.postAction( rootNode.CREATE )

    self.obj847=Attribute(self)
    self.obj847.isGraphObjectVisual = True

    if(hasattr(self.obj847, '_setHierarchicalLink')):
      self.obj847._setHierarchicalLink(False)

    # Type
    self.obj847.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj847.Type.config = 0

    # name
    self.obj847.name.setValue('isComposite')

    self.obj847.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(300.0,240.0,self.obj847)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj847.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj847)
    self.globalAndLocalPostcondition(self.obj847, rootNode)
    self.obj847.postAction( rootNode.CREATE )

    self.obj848=Attribute(self)
    self.obj848.isGraphObjectVisual = True

    if(hasattr(self.obj848, '_setHierarchicalLink')):
      self.obj848._setHierarchicalLink(False)

    # Type
    self.obj848.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj848.Type.config = 0

    # name
    self.obj848.name.setValue('channel')

    self.obj848.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(460.0,360.0,self.obj848)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj848.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj848)
    self.globalAndLocalPostcondition(self.obj848, rootNode)
    self.obj848.postAction( rootNode.CREATE )

    self.obj849=Attribute(self)
    self.obj849.isGraphObjectVisual = True

    if(hasattr(self.obj849, '_setHierarchicalLink')):
      self.obj849._setHierarchicalLink(False)

    # Type
    self.obj849.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj849.Type.config = 0

    # name
    self.obj849.name.setValue('channel')

    self.obj849.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(840.0,360.0,self.obj849)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj849.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj849)
    self.globalAndLocalPostcondition(self.obj849, rootNode)
    self.obj849.postAction( rootNode.CREATE )

    self.obj850=Attribute(self)
    self.obj850.isGraphObjectVisual = True

    if(hasattr(self.obj850, '_setHierarchicalLink')):
      self.obj850._setHierarchicalLink(False)

    # Type
    self.obj850.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj850.Type.config = 0

    # name
    self.obj850.name.setValue('pivot')

    self.obj850.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(280.0,540.0,self.obj850)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj850.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj850)
    self.globalAndLocalPostcondition(self.obj850, rootNode)
    self.obj850.postAction( rootNode.CREATE )

    self.obj851=Attribute(self)
    self.obj851.isGraphObjectVisual = True

    if(hasattr(self.obj851, '_setHierarchicalLink')):
      self.obj851._setHierarchicalLink(False)

    # Type
    self.obj851.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj851.Type.config = 0

    # name
    self.obj851.name.setValue('channel')

    self.obj851.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(960.0,740.0,self.obj851)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj851.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj851)
    self.globalAndLocalPostcondition(self.obj851, rootNode)
    self.obj851.postAction( rootNode.CREATE )

    self.obj852=Attribute(self)
    self.obj852.isGraphObjectVisual = True

    if(hasattr(self.obj852, '_setHierarchicalLink')):
      self.obj852._setHierarchicalLink(False)

    # Type
    self.obj852.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj852.Type.config = 0

    # name
    self.obj852.name.setValue('pivot')

    self.obj852.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,820.0,self.obj852)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj852.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj852)
    self.globalAndLocalPostcondition(self.obj852, rootNode)
    self.obj852.postAction( rootNode.CREATE )

    self.obj853=Equation(self)
    self.obj853.isGraphObjectVisual = True

    if(hasattr(self.obj853, '_setHierarchicalLink')):
      self.obj853._setHierarchicalLink(False)

    # name
    self.obj853.name.setValue('eq1')

    self.obj853.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,320.0,self.obj853)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj853.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj853)
    self.globalAndLocalPostcondition(self.obj853, rootNode)
    self.obj853.postAction( rootNode.CREATE )

    self.obj854=Equation(self)
    self.obj854.isGraphObjectVisual = True

    if(hasattr(self.obj854, '_setHierarchicalLink')):
      self.obj854._setHierarchicalLink(False)

    # name
    self.obj854.name.setValue('eq2')

    self.obj854.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,284.0,self.obj854)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj854.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj854)
    self.globalAndLocalPostcondition(self.obj854, rootNode)
    self.obj854.postAction( rootNode.CREATE )

    self.obj855=Equation(self)
    self.obj855.isGraphObjectVisual = True

    if(hasattr(self.obj855, '_setHierarchicalLink')):
      self.obj855._setHierarchicalLink(False)

    # name
    self.obj855.name.setValue('eq3')

    self.obj855.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,280.0,self.obj855)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj855.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj855)
    self.globalAndLocalPostcondition(self.obj855, rootNode)
    self.obj855.postAction( rootNode.CREATE )

    self.obj856=Equation(self)
    self.obj856.isGraphObjectVisual = True

    if(hasattr(self.obj856, '_setHierarchicalLink')):
      self.obj856._setHierarchicalLink(False)

    # name
    self.obj856.name.setValue('eq4')

    self.obj856.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,620.0,self.obj856)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj856.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj856)
    self.globalAndLocalPostcondition(self.obj856, rootNode)
    self.obj856.postAction( rootNode.CREATE )

    self.obj857=Equation(self)
    self.obj857.isGraphObjectVisual = True

    if(hasattr(self.obj857, '_setHierarchicalLink')):
      self.obj857._setHierarchicalLink(False)

    # name
    self.obj857.name.setValue('eq5')

    self.obj857.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(900.0,820.0,self.obj857)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj857.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj857)
    self.globalAndLocalPostcondition(self.obj857, rootNode)
    self.obj857.postAction( rootNode.CREATE )

    self.obj858=Equation(self)
    self.obj858.isGraphObjectVisual = True

    if(hasattr(self.obj858, '_setHierarchicalLink')):
      self.obj858._setHierarchicalLink(False)

    # name
    self.obj858.name.setValue('eq6')

    self.obj858.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(571.0,820.0,self.obj858)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj858.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj858)
    self.globalAndLocalPostcondition(self.obj858, rootNode)
    self.obj858.postAction( rootNode.CREATE )

    self.obj859=Constant(self)
    self.obj859.isGraphObjectVisual = True

    if(hasattr(self.obj859, '_setHierarchicalLink')):
      self.obj859._setHierarchicalLink(False)

    # Type
    self.obj859.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj859.Type.config = 0

    # name
    self.obj859.name.setValue('true')

    self.obj859.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,240.0,self.obj859)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj859.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj859)
    self.globalAndLocalPostcondition(self.obj859, rootNode)
    self.obj859.postAction( rootNode.CREATE )

    self.obj860=Constant(self)
    self.obj860.isGraphObjectVisual = True

    if(hasattr(self.obj860, '_setHierarchicalLink')):
      self.obj860._setHierarchicalLink(False)

    # Type
    self.obj860.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj860.Type.config = 0

    # name
    self.obj860.name.setValue('exit_in')

    self.obj860.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,360.0,self.obj860)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj860.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj860)
    self.globalAndLocalPostcondition(self.obj860, rootNode)
    self.obj860.postAction( rootNode.CREATE )

    self.obj861=Constant(self)
    self.obj861.isGraphObjectVisual = True

    if(hasattr(self.obj861, '_setHierarchicalLink')):
      self.obj861._setHierarchicalLink(False)

    # Type
    self.obj861.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj861.Type.config = 0

    # name
    self.obj861.name.setValue('listenhproc')

    self.obj861.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(140.0,540.0,self.obj861)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj861.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj861)
    self.globalAndLocalPostcondition(self.obj861, rootNode)
    self.obj861.postAction( rootNode.CREATE )

    self.obj862=Constant(self)
    self.obj862.isGraphObjectVisual = True

    if(hasattr(self.obj862, '_setHierarchicalLink')):
      self.obj862._setHierarchicalLink(False)

    # Type
    self.obj862.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj862.Type.config = 0

    # name
    self.obj862.name.setValue('exack_in')

    self.obj862.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(820.0,740.0,self.obj862)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj862.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj862)
    self.globalAndLocalPostcondition(self.obj862, rootNode)
    self.obj862.postAction( rootNode.CREATE )

    self.obj863=Constant(self)
    self.obj863.isGraphObjectVisual = True

    if(hasattr(self.obj863, '_setHierarchicalLink')):
      self.obj863._setHierarchicalLink(False)

    # Type
    self.obj863.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj863.Type.config = 0

    # name
    self.obj863.name.setValue('instfortrans')

    self.obj863.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,820.0,self.obj863)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj863.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj863)
    self.globalAndLocalPostcondition(self.obj863, rootNode)
    self.obj863.postAction( rootNode.CREATE )

    self.obj864=paired_with(self)
    self.obj864.isGraphObjectVisual = True

    if(hasattr(self.obj864, '_setHierarchicalLink')):
      self.obj864._setHierarchicalLink(False)

    self.obj864.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,192.0,self.obj864)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj864.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj864)
    self.globalAndLocalPostcondition(self.obj864, rootNode)
    self.obj864.postAction( rootNode.CREATE )

    self.obj865=match_contains(self)
    self.obj865.isGraphObjectVisual = True

    if(hasattr(self.obj865, '_setHierarchicalLink')):
      self.obj865._setHierarchicalLink(False)

    self.obj865.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(254.0,67.0,self.obj865)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj865.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj865)
    self.globalAndLocalPostcondition(self.obj865, rootNode)
    self.obj865.postAction( rootNode.CREATE )

    self.obj866=match_contains(self)
    self.obj866.isGraphObjectVisual = True

    if(hasattr(self.obj866, '_setHierarchicalLink')):
      self.obj866._setHierarchicalLink(False)

    self.obj866.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,67.0,self.obj866)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj866.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj866)
    self.globalAndLocalPostcondition(self.obj866, rootNode)
    self.obj866.postAction( rootNode.CREATE )

    self.obj867=match_contains(self)
    self.obj867.isGraphObjectVisual = True

    if(hasattr(self.obj867, '_setHierarchicalLink')):
      self.obj867._setHierarchicalLink(False)

    self.obj867.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(454.0,67.0,self.obj867)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj867.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj867)
    self.globalAndLocalPostcondition(self.obj867, rootNode)
    self.obj867.postAction( rootNode.CREATE )

    self.obj868=match_contains(self)
    self.obj868.isGraphObjectVisual = True

    if(hasattr(self.obj868, '_setHierarchicalLink')):
      self.obj868._setHierarchicalLink(False)

    self.obj868.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(554.0,67.0,self.obj868)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj868.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj868)
    self.globalAndLocalPostcondition(self.obj868, rootNode)
    self.obj868.postAction( rootNode.CREATE )

    self.obj869=match_contains(self)
    self.obj869.isGraphObjectVisual = True

    if(hasattr(self.obj869, '_setHierarchicalLink')):
      self.obj869._setHierarchicalLink(False)

    self.obj869.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(294.0,117.0,self.obj869)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj869.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj869)
    self.globalAndLocalPostcondition(self.obj869, rootNode)
    self.obj869.postAction( rootNode.CREATE )

    self.obj870=match_contains(self)
    self.obj870.isGraphObjectVisual = True

    if(hasattr(self.obj870, '_setHierarchicalLink')):
      self.obj870._setHierarchicalLink(False)

    self.obj870.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,117.0,self.obj870)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj870.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj870)
    self.globalAndLocalPostcondition(self.obj870, rootNode)
    self.obj870.postAction( rootNode.CREATE )

    self.obj871=match_contains(self)
    self.obj871.isGraphObjectVisual = True

    if(hasattr(self.obj871, '_setHierarchicalLink')):
      self.obj871._setHierarchicalLink(False)

    self.obj871.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(514.0,117.0,self.obj871)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj871.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj871)
    self.globalAndLocalPostcondition(self.obj871, rootNode)
    self.obj871.postAction( rootNode.CREATE )

    self.obj872=apply_contains(self)
    self.obj872.isGraphObjectVisual = True

    if(hasattr(self.obj872, '_setHierarchicalLink')):
      self.obj872._setHierarchicalLink(False)

    self.obj872.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,452.0,self.obj872)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj872.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj872)
    self.globalAndLocalPostcondition(self.obj872, rootNode)
    self.obj872.postAction( rootNode.CREATE )

    self.obj873=apply_contains(self)
    self.obj873.isGraphObjectVisual = True

    if(hasattr(self.obj873, '_setHierarchicalLink')):
      self.obj873._setHierarchicalLink(False)

    self.obj873.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(347.5,452.0,self.obj873)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj873.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj873)
    self.globalAndLocalPostcondition(self.obj873, rootNode)
    self.obj873.postAction( rootNode.CREATE )

    self.obj874=apply_contains(self)
    self.obj874.isGraphObjectVisual = True

    if(hasattr(self.obj874, '_setHierarchicalLink')):
      self.obj874._setHierarchicalLink(False)

    self.obj874.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,452.0,self.obj874)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj874.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj874)
    self.globalAndLocalPostcondition(self.obj874, rootNode)
    self.obj874.postAction( rootNode.CREATE )

    self.obj875=apply_contains(self)
    self.obj875.isGraphObjectVisual = True

    if(hasattr(self.obj875, '_setHierarchicalLink')):
      self.obj875._setHierarchicalLink(False)

    self.obj875.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,452.0,self.obj875)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj875.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj875)
    self.globalAndLocalPostcondition(self.obj875, rootNode)
    self.obj875.postAction( rootNode.CREATE )

    self.obj876=apply_contains(self)
    self.obj876.isGraphObjectVisual = True

    if(hasattr(self.obj876, '_setHierarchicalLink')):
      self.obj876._setHierarchicalLink(False)

    self.obj876.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(547.5,502.0,self.obj876)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj876.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj876)
    self.globalAndLocalPostcondition(self.obj876, rootNode)
    self.obj876.postAction( rootNode.CREATE )

    self.obj877=apply_contains(self)
    self.obj877.isGraphObjectVisual = True

    if(hasattr(self.obj877, '_setHierarchicalLink')):
      self.obj877._setHierarchicalLink(False)

    self.obj877.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(587.5,552.0,self.obj877)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj877.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj877)
    self.globalAndLocalPostcondition(self.obj877, rootNode)
    self.obj877.postAction( rootNode.CREATE )

    self.obj878=apply_contains(self)
    self.obj878.isGraphObjectVisual = True

    if(hasattr(self.obj878, '_setHierarchicalLink')):
      self.obj878._setHierarchicalLink(False)

    self.obj878.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(447.5,592.0,self.obj878)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj878.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj878)
    self.globalAndLocalPostcondition(self.obj878, rootNode)
    self.obj878.postAction( rootNode.CREATE )

    self.obj879=directLink_T(self)
    self.obj879.isGraphObjectVisual = True

    if(hasattr(self.obj879, '_setHierarchicalLink')):
      self.obj879._setHierarchicalLink(False)

    # associationType
    self.obj879.associationType.setValue('branches')

    self.obj879.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.0,491.0,self.obj879)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj879.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj879)
    self.globalAndLocalPostcondition(self.obj879, rootNode)
    self.obj879.postAction( rootNode.CREATE )

    self.obj880=directLink_T(self)
    self.obj880.isGraphObjectVisual = True

    if(hasattr(self.obj880, '_setHierarchicalLink')):
      self.obj880._setHierarchicalLink(False)

    # associationType
    self.obj880.associationType.setValue('p')

    self.obj880.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj880)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj880.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj880)
    self.globalAndLocalPostcondition(self.obj880, rootNode)
    self.obj880.postAction( rootNode.CREATE )

    self.obj881=directLink_T(self)
    self.obj881.isGraphObjectVisual = True

    if(hasattr(self.obj881, '_setHierarchicalLink')):
      self.obj881._setHierarchicalLink(False)

    # associationType
    self.obj881.associationType.setValue('p')

    self.obj881.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,491.0,self.obj881)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj881.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj881)
    self.globalAndLocalPostcondition(self.obj881, rootNode)
    self.obj881.postAction( rootNode.CREATE )

    self.obj882=directLink_T(self)
    self.obj882.isGraphObjectVisual = True

    if(hasattr(self.obj882, '_setHierarchicalLink')):
      self.obj882._setHierarchicalLink(False)

    # associationType
    self.obj882.associationType.setValue('p')

    self.obj882.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(852.0,541.0,self.obj882)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj882.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj882)
    self.globalAndLocalPostcondition(self.obj882, rootNode)
    self.obj882.postAction( rootNode.CREATE )

    self.obj883=directLink_T(self)
    self.obj883.isGraphObjectVisual = True

    if(hasattr(self.obj883, '_setHierarchicalLink')):
      self.obj883._setHierarchicalLink(False)

    # associationType
    self.obj883.associationType.setValue('branches')

    self.obj883.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(992.0,641.0,self.obj883)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj883.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj883)
    self.globalAndLocalPostcondition(self.obj883, rootNode)
    self.obj883.postAction( rootNode.CREATE )

    self.obj884=directLink_T(self)
    self.obj884.isGraphObjectVisual = True

    if(hasattr(self.obj884, '_setHierarchicalLink')):
      self.obj884._setHierarchicalLink(False)

    # associationType
    self.obj884.associationType.setValue('p')

    self.obj884.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(806.0,693.0,self.obj884)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj884.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj884)
    self.globalAndLocalPostcondition(self.obj884, rootNode)
    self.obj884.postAction( rootNode.CREATE )

    self.obj885=directLink_S(self)
    self.obj885.isGraphObjectVisual = True

    if(hasattr(self.obj885, '_setHierarchicalLink')):
      self.obj885._setHierarchicalLink(False)

    # associationType
    self.obj885.associationType.setValue('src')

    self.obj885.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,83.0,self.obj885)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj885.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj885)
    self.globalAndLocalPostcondition(self.obj885, rootNode)
    self.obj885.postAction( rootNode.CREATE )

    self.obj886=directLink_S(self)
    self.obj886.isGraphObjectVisual = True

    if(hasattr(self.obj886, '_setHierarchicalLink')):
      self.obj886._setHierarchicalLink(False)

    # associationType
    self.obj886.associationType.setValue('owningStateMachine')

    self.obj886.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,83.0,self.obj886)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj886.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj886)
    self.globalAndLocalPostcondition(self.obj886, rootNode)
    self.obj886.postAction( rootNode.CREATE )

    self.obj887=directLink_S(self)
    self.obj887.isGraphObjectVisual = True

    if(hasattr(self.obj887, '_setHierarchicalLink')):
      self.obj887._setHierarchicalLink(False)

    # associationType
    self.obj887.associationType.setValue('states')

    self.obj887.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(870.0,83.0,self.obj887)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj887.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj887)
    self.globalAndLocalPostcondition(self.obj887, rootNode)
    self.obj887.postAction( rootNode.CREATE )

    self.obj888=directLink_S(self)
    self.obj888.isGraphObjectVisual = True

    if(hasattr(self.obj888, '_setHierarchicalLink')):
      self.obj888._setHierarchicalLink(False)

    # associationType
    self.obj888.associationType.setValue('triggers')

    self.obj888.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(489.0,128.0,self.obj888)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj888.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj888)
    self.globalAndLocalPostcondition(self.obj888, rootNode)
    self.obj888.postAction( rootNode.CREATE )

    self.obj889=directLink_S(self)
    self.obj889.isGraphObjectVisual = True

    if(hasattr(self.obj889, '_setHierarchicalLink')):
      self.obj889._setHierarchicalLink(False)

    # associationType
    self.obj889.associationType.setValue('signal')

    self.obj889.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(670.0,183.0,self.obj889)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj889.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj889)
    self.globalAndLocalPostcondition(self.obj889, rootNode)
    self.obj889.postAction( rootNode.CREATE )

    self.obj890=directLink_S(self)
    self.obj890.isGraphObjectVisual = True

    if(hasattr(self.obj890, '_setHierarchicalLink')):
      self.obj890._setHierarchicalLink(False)

    # associationType
    self.obj890.associationType.setValue('outgoingTransitions')

    self.obj890.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(430.0,148.0,self.obj890)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj890.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj890)
    self.globalAndLocalPostcondition(self.obj890, rootNode)
    self.obj890.postAction( rootNode.CREATE )

    self.obj891=backward_link(self)
    self.obj891.isGraphObjectVisual = True

    if(hasattr(self.obj891, '_setHierarchicalLink')):
      self.obj891._setHierarchicalLink(False)

    # type
    self.obj891.type.setValue('ruleDef')

    self.obj891.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(460.0,339.0,self.obj891)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj891.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj891)
    self.globalAndLocalPostcondition(self.obj891, rootNode)
    self.obj891.postAction( rootNode.CREATE )

    self.obj892=backward_link(self)
    self.obj892.isGraphObjectVisual = True

    if(hasattr(self.obj892, '_setHierarchicalLink')):
      self.obj892._setHierarchicalLink(False)

    # type
    self.obj892.type.setValue('ruleDef')

    self.obj892.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(561.0,427.0,self.obj892)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj892.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj892)
    self.globalAndLocalPostcondition(self.obj892, rootNode)
    self.obj892.postAction( rootNode.CREATE )

    self.obj893=hasAttribute_S(self)
    self.obj893.isGraphObjectVisual = True

    if(hasattr(self.obj893, '_setHierarchicalLink')):
      self.obj893._setHierarchicalLink(False)

    self.obj893.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(972.0,178.5,self.obj893)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj893.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj893)
    self.globalAndLocalPostcondition(self.obj893, rootNode)
    self.obj893.postAction( rootNode.CREATE )

    self.obj894=hasAttribute_S(self)
    self.obj894.isGraphObjectVisual = True

    if(hasattr(self.obj894, '_setHierarchicalLink')):
      self.obj894._setHierarchicalLink(False)

    self.obj894.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(440.0,231.5,self.obj894)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj894.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj894)
    self.globalAndLocalPostcondition(self.obj894, rootNode)
    self.obj894.postAction( rootNode.CREATE )

    self.obj895=hasAttribute_T(self)
    self.obj895.isGraphObjectVisual = True

    if(hasattr(self.obj895, '_setHierarchicalLink')):
      self.obj895._setHierarchicalLink(False)

    self.obj895.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(573.0,442.5,self.obj895)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj895.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj895)
    self.globalAndLocalPostcondition(self.obj895, rootNode)
    self.obj895.postAction( rootNode.CREATE )

    self.obj896=hasAttribute_T(self)
    self.obj896.isGraphObjectVisual = True

    if(hasattr(self.obj896, '_setHierarchicalLink')):
      self.obj896._setHierarchicalLink(False)

    self.obj896.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(963.0,442.5,self.obj896)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj896.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj896)
    self.globalAndLocalPostcondition(self.obj896, rootNode)
    self.obj896.postAction( rootNode.CREATE )

    self.obj897=hasAttribute_T(self)
    self.obj897.isGraphObjectVisual = True

    if(hasattr(self.obj897, '_setHierarchicalLink')):
      self.obj897._setHierarchicalLink(False)

    self.obj897.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(383.0,532.5,self.obj897)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj897.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj897)
    self.globalAndLocalPostcondition(self.obj897, rootNode)
    self.obj897.postAction( rootNode.CREATE )

    self.obj898=hasAttribute_T(self)
    self.obj898.isGraphObjectVisual = True

    if(hasattr(self.obj898, '_setHierarchicalLink')):
      self.obj898._setHierarchicalLink(False)

    self.obj898.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1063.0,732.5,self.obj898)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj898.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj898)
    self.globalAndLocalPostcondition(self.obj898, rootNode)
    self.obj898.postAction( rootNode.CREATE )

    self.obj899=hasAttribute_T(self)
    self.obj899.isGraphObjectVisual = True

    if(hasattr(self.obj899, '_setHierarchicalLink')):
      self.obj899._setHierarchicalLink(False)

    self.obj899.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(763.0,812.5,self.obj899)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj899.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj899)
    self.globalAndLocalPostcondition(self.obj899, rootNode)
    self.obj899.postAction( rootNode.CREATE )

    self.obj900=leftExpr(self)
    self.obj900.isGraphObjectVisual = True

    if(hasattr(self.obj900, '_setHierarchicalLink')):
      self.obj900._setHierarchicalLink(False)

    self.obj900.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(401.0,321.5,self.obj900)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj900.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj900)
    self.globalAndLocalPostcondition(self.obj900, rootNode)
    self.obj900.postAction( rootNode.CREATE )

    self.obj901=leftExpr(self)
    self.obj901.isGraphObjectVisual = True

    if(hasattr(self.obj901, '_setHierarchicalLink')):
      self.obj901._setHierarchicalLink(False)

    self.obj901.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(616.0,358.5,self.obj901)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj901.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj901)
    self.globalAndLocalPostcondition(self.obj901, rootNode)
    self.obj901.postAction( rootNode.CREATE )

    self.obj902=leftExpr(self)
    self.obj902.isGraphObjectVisual = True

    if(hasattr(self.obj902, '_setHierarchicalLink')):
      self.obj902._setHierarchicalLink(False)

    self.obj902.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,356.5,self.obj902)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj902.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj902)
    self.globalAndLocalPostcondition(self.obj902, rootNode)
    self.obj902.postAction( rootNode.CREATE )

    self.obj903=leftExpr(self)
    self.obj903.isGraphObjectVisual = True

    if(hasattr(self.obj903, '_setHierarchicalLink')):
      self.obj903._setHierarchicalLink(False)

    self.obj903.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(386.0,616.5,self.obj903)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj903.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj903)
    self.globalAndLocalPostcondition(self.obj903, rootNode)
    self.obj903.postAction( rootNode.CREATE )

    self.obj904=leftExpr(self)
    self.obj904.isGraphObjectVisual = True

    if(hasattr(self.obj904, '_setHierarchicalLink')):
      self.obj904._setHierarchicalLink(False)

    self.obj904.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1066.0,816.5,self.obj904)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj904.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj904)
    self.globalAndLocalPostcondition(self.obj904, rootNode)
    self.obj904.postAction( rootNode.CREATE )

    self.obj905=leftExpr(self)
    self.obj905.isGraphObjectVisual = True

    if(hasattr(self.obj905, '_setHierarchicalLink')):
      self.obj905._setHierarchicalLink(False)

    self.obj905.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(781.5,856.5,self.obj905)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj905.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj905)
    self.globalAndLocalPostcondition(self.obj905, rootNode)
    self.obj905.postAction( rootNode.CREATE )

    self.obj906=rightExpr(self)
    self.obj906.isGraphObjectVisual = True

    if(hasattr(self.obj906, '_setHierarchicalLink')):
      self.obj906._setHierarchicalLink(False)

    self.obj906.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(295.0,312.5,self.obj906)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj906.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj906)
    self.globalAndLocalPostcondition(self.obj906, rootNode)
    self.obj906.postAction( rootNode.CREATE )

    self.obj907=rightExpr(self)
    self.obj907.isGraphObjectVisual = True

    if(hasattr(self.obj907, '_setHierarchicalLink')):
      self.obj907._setHierarchicalLink(False)

    self.obj907.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(648.0,251.5,self.obj907)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj907.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj907)
    self.globalAndLocalPostcondition(self.obj907, rootNode)
    self.obj907.postAction( rootNode.CREATE )

    self.obj908=rightExpr(self)
    self.obj908.isGraphObjectVisual = True

    if(hasattr(self.obj908, '_setHierarchicalLink')):
      self.obj908._setHierarchicalLink(False)

    self.obj908.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(886.0,356.5,self.obj908)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj908.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj908)
    self.globalAndLocalPostcondition(self.obj908, rootNode)
    self.obj908.postAction( rootNode.CREATE )

    self.obj909=rightExpr(self)
    self.obj909.isGraphObjectVisual = True

    if(hasattr(self.obj909, '_setHierarchicalLink')):
      self.obj909._setHierarchicalLink(False)

    self.obj909.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(316.0,616.5,self.obj909)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj909.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj909)
    self.globalAndLocalPostcondition(self.obj909, rootNode)
    self.obj909.postAction( rootNode.CREATE )

    self.obj910=rightExpr(self)
    self.obj910.isGraphObjectVisual = True

    if(hasattr(self.obj910, '_setHierarchicalLink')):
      self.obj910._setHierarchicalLink(False)

    self.obj910.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,816.5,self.obj910)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj910.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj910)
    self.globalAndLocalPostcondition(self.obj910, rootNode)
    self.obj910.postAction( rootNode.CREATE )

    self.obj911=rightExpr(self)
    self.obj911.isGraphObjectVisual = True

    if(hasattr(self.obj911, '_setHierarchicalLink')):
      self.obj911._setHierarchicalLink(False)

    self.obj911.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(631.5,856.5,self.obj911)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj911.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj911)
    self.globalAndLocalPostcondition(self.obj911, rootNode)
    self.obj911.postAction( rootNode.CREATE )

    # Connections for obj830 (graphObject_: Obj727) of type MatchModel
    self.drawConnections(
(self.obj830,self.obj864,[138.0, 51.0, 140.5, 192.0],"true", 2),
(self.obj830,self.obj865,[138.0, 51.0, 254.0, 67.0],"true", 2),
(self.obj830,self.obj866,[138.0, 51.0, 354.0, 67.0],"true", 2),
(self.obj830,self.obj867,[138.0, 51.0, 454.0, 67.0],"true", 2),
(self.obj830,self.obj868,[138.0, 51.0, 554.0, 67.0],"true", 2),
(self.obj830,self.obj869,[138.0, 51.0, 294.0, 117.0],"true", 2),
(self.obj830,self.obj870,[138.0, 51.0, 394.0, 117.0],"true", 2),
(self.obj830,self.obj871,[138.0, 51.0, 514.0, 117.0],"true", 2) )
    # Connections for obj831 (graphObject_: Obj728) of type ApplyModel
    self.drawConnections(
(self.obj831,self.obj872,[143.0, 413.0, 247.5, 452.0],"true", 2),
(self.obj831,self.obj873,[143.0, 413.0, 347.5, 452.0],"true", 2),
(self.obj831,self.obj874,[143.0, 413.0, 447.5, 452.0],"true", 2),
(self.obj831,self.obj875,[143.0, 413.0, 547.5, 452.0],"true", 2),
(self.obj831,self.obj876,[143.0, 413.0, 547.5, 502.0],"true", 2),
(self.obj831,self.obj877,[143.0, 413.0, 587.5, 552.0],"true", 2),
(self.obj831,self.obj878,[143.0, 413.0, 447.5, 592.0],"true", 2) )
    # Connections for obj832 (graphObject_: Obj729) named triggerS1
    self.drawConnections(
(self.obj832,self.obj889,[650.0, 183.0, 670.0, 183.0],"true", 2) )
    # Connections for obj833 (graphObject_: Obj730) named signal1
    self.drawConnections(
(self.obj833,self.obj893,[890.0, 183.0, 972.0, 178.5],"true", 2) )
    # Connections for obj834 (graphObject_: Obj731) named vertex1
    self.drawConnections(
(self.obj834,self.obj886,[570.0, 83.0, 670.0, 83.0],"true", 2) )
    # Connections for obj835 (graphObject_: Obj732) named transition1
    self.drawConnections(
(self.obj835,self.obj885,[370.0, 83.0, 470.0, 83.0],"true", 2),
(self.obj835,self.obj888,[370.0, 83.0, 489.0, 128.0],"true", 2) )
    # Connections for obj836 (graphObject_: Obj733) named statemachine1
    self.drawConnections(
(self.obj836,self.obj887,[770.0, 83.0, 870.0, 83.0],"true", 2) )
    # Connections for obj837 (graphObject_: Obj734) named state1
    self.drawConnections(
 )
    # Connections for obj838 (graphObject_: Obj735) named state2
    self.drawConnections(
(self.obj838,self.obj890,[450.0, 183.0, 430.0, 148.0],"true", 2),
(self.obj838,self.obj894,[450.0, 183.0, 440.0, 231.5],"true", 2) )
    # Connections for obj839 (graphObject_: Obj736) named triggerT1
    self.drawConnections(
(self.obj839,self.obj896,[952.0, 491.0, 963.0, 442.5],"true", 2) )
    # Connections for obj840 (graphObject_: Obj737) named listen1
    self.drawConnections(
(self.obj840,self.obj879,[352.0, 491.0, 452.0, 491.0],"true", 2),
(self.obj840,self.obj897,[352.0, 491.0, 383.0, 532.5],"true", 2),
(self.obj840,self.obj891,[352.0, 491.0, 460.0, 339.0],"true", 2) )
    # Connections for obj841 (graphObject_: Obj738) named listen2
    self.drawConnections(
(self.obj841,self.obj883,[952.0, 591.0, 992.0, 641.0],"true", 2) )
    # Connections for obj842 (graphObject_: Obj739) named listenbranch1
    self.drawConnections(
(self.obj842,self.obj880,[552.0, 491.0, 652.0, 491.0],"true", 2),
(self.obj842,self.obj895,[552.0, 491.0, 573.0, 442.5],"true", 2) )
    # Connections for obj843 (graphObject_: Obj740) named listenbranch2
    self.drawConnections(
(self.obj843,self.obj898,[1032.0, 691.0, 1063.0, 732.5],"true", 2),
(self.obj843,self.obj884,[1032.0, 691.0, 806.0, 693.0],"true", 2) )
    # Connections for obj844 (graphObject_: Obj741) named inst1
    self.drawConnections(
(self.obj844,self.obj899,[752.0, 771.0, 763.0, 812.5],"true", 2),
(self.obj844,self.obj892,[752.0, 771.0, 561.0, 427.0],"true", 2) )
    # Connections for obj845 (graphObject_: Obj742) named seq1
    self.drawConnections(
(self.obj845,self.obj881,[752.0, 491.0, 852.0, 491.0],"true", 2),
(self.obj845,self.obj882,[752.0, 491.0, 852.0, 541.0],"true", 2) )
    # Connections for obj846 (graphObject_: Obj743) named name
    self.drawConnections(
 )
    # Connections for obj847 (graphObject_: Obj744) named isComposite
    self.drawConnections(
 )
    # Connections for obj848 (graphObject_: Obj745) named channel
    self.drawConnections(
 )
    # Connections for obj849 (graphObject_: Obj746) named channel
    self.drawConnections(
 )
    # Connections for obj850 (graphObject_: Obj747) named pivot
    self.drawConnections(
 )
    # Connections for obj851 (graphObject_: Obj748) named channel
    self.drawConnections(
 )
    # Connections for obj852 (graphObject_: Obj749) named pivot
    self.drawConnections(
 )
    # Connections for obj853 (graphObject_: Obj750) named eq1
    self.drawConnections(
(self.obj853,self.obj900,[358.0, 359.0, 401.0, 321.5],"true", 2),
(self.obj853,self.obj906,[358.0, 359.0, 295.0, 312.5],"true", 2) )
    # Connections for obj854 (graphObject_: Obj751) named eq2
    self.drawConnections(
(self.obj854,self.obj901,[638.0, 323.0, 616.0, 358.5],"true", 2),
(self.obj854,self.obj907,[638.0, 323.0, 648.0, 251.5],"true", 2) )
    # Connections for obj855 (graphObject_: Obj752) named eq3
    self.drawConnections(
(self.obj855,self.obj908,[938.0, 319.0, 886.0, 356.5],"true", 2),
(self.obj855,self.obj902,[938.0, 319.0, 956.0, 356.5],"true", 2) )
    # Connections for obj856 (graphObject_: Obj753) named eq4
    self.drawConnections(
(self.obj856,self.obj903,[358.0, 659.0, 386.0, 616.5],"true", 2),
(self.obj856,self.obj909,[358.0, 659.0, 316.0, 616.5],"true", 2) )
    # Connections for obj857 (graphObject_: Obj754) named eq5
    self.drawConnections(
(self.obj857,self.obj904,[1038.0, 859.0, 1066.0, 816.5],"true", 2),
(self.obj857,self.obj910,[1038.0, 859.0, 996.0, 816.5],"true", 2) )
    # Connections for obj858 (graphObject_: Obj755) named eq6
    self.drawConnections(
(self.obj858,self.obj905,[709.0, 859.0, 781.5, 856.5],"true", 2),
(self.obj858,self.obj911,[709.0, 859.0, 631.5, 856.5],"true", 2) )
    # Connections for obj859 (graphObject_: Obj756) named true
    self.drawConnections(
 )
    # Connections for obj860 (graphObject_: Obj757) named exit_in
    self.drawConnections(
 )
    # Connections for obj861 (graphObject_: Obj758) named listenhproc
    self.drawConnections(
 )
    # Connections for obj862 (graphObject_: Obj759) named exack_in
    self.drawConnections(
 )
    # Connections for obj863 (graphObject_: Obj760) named instfortrans
    self.drawConnections(
 )
    # Connections for obj864 (graphObject_: Obj761) of type paired_with
    self.drawConnections(
(self.obj864,self.obj831,[140.5, 192.0, 143.0, 413.0],"true", 2) )
    # Connections for obj865 (graphObject_: Obj762) of type match_contains
    self.drawConnections(
(self.obj865,self.obj835,[254.0, 67.0, 370.0, 83.0],"true", 2) )
    # Connections for obj866 (graphObject_: Obj763) of type match_contains
    self.drawConnections(
(self.obj866,self.obj834,[354.0, 67.0, 570.0, 83.0],"true", 2) )
    # Connections for obj867 (graphObject_: Obj764) of type match_contains
    self.drawConnections(
(self.obj867,self.obj836,[454.0, 67.0, 770.0, 83.0],"true", 2) )
    # Connections for obj868 (graphObject_: Obj765) of type match_contains
    self.drawConnections(
(self.obj868,self.obj837,[554.0, 67.0, 970.0, 83.0],"true", 2) )
    # Connections for obj869 (graphObject_: Obj766) of type match_contains
    self.drawConnections(
(self.obj869,self.obj838,[294.0, 117.0, 450.0, 183.0],"true", 2) )
    # Connections for obj870 (graphObject_: Obj767) of type match_contains
    self.drawConnections(
(self.obj870,self.obj832,[394.0, 117.0, 650.0, 183.0],"true", 2) )
    # Connections for obj871 (graphObject_: Obj768) of type match_contains
    self.drawConnections(
(self.obj871,self.obj833,[514.0, 117.0, 890.0, 183.0],"true", 2) )
    # Connections for obj872 (graphObject_: Obj769) of type apply_contains
    self.drawConnections(
(self.obj872,self.obj840,[247.5, 452.0, 352.0, 491.0],"true", 2) )
    # Connections for obj873 (graphObject_: Obj770) of type apply_contains
    self.drawConnections(
(self.obj873,self.obj842,[347.5, 452.0, 552.0, 491.0],"true", 2) )
    # Connections for obj874 (graphObject_: Obj771) of type apply_contains
    self.drawConnections(
(self.obj874,self.obj845,[447.5, 452.0, 752.0, 491.0],"true", 2) )
    # Connections for obj875 (graphObject_: Obj772) of type apply_contains
    self.drawConnections(
(self.obj875,self.obj839,[547.5, 452.0, 952.0, 491.0],"true", 2) )
    # Connections for obj876 (graphObject_: Obj773) of type apply_contains
    self.drawConnections(
(self.obj876,self.obj841,[547.5, 502.0, 952.0, 591.0],"true", 2) )
    # Connections for obj877 (graphObject_: Obj774) of type apply_contains
    self.drawConnections(
(self.obj877,self.obj843,[587.5, 552.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj878 (graphObject_: Obj775) of type apply_contains
    self.drawConnections(
(self.obj878,self.obj844,[447.5, 592.0, 752.0, 771.0],"true", 2) )
    # Connections for obj879 (graphObject_: Obj776) of type directLink_T
    self.drawConnections(
(self.obj879,self.obj842,[452.0, 491.0, 552.0, 491.0],"true", 2) )
    # Connections for obj880 (graphObject_: Obj777) of type directLink_T
    self.drawConnections(
(self.obj880,self.obj845,[652.0, 491.0, 752.0, 491.0],"true", 2) )
    # Connections for obj881 (graphObject_: Obj778) of type directLink_T
    self.drawConnections(
(self.obj881,self.obj839,[852.0, 491.0, 952.0, 491.0],"true", 2) )
    # Connections for obj882 (graphObject_: Obj779) of type directLink_T
    self.drawConnections(
(self.obj882,self.obj841,[852.0, 541.0, 952.0, 591.0],"true", 2) )
    # Connections for obj883 (graphObject_: Obj780) of type directLink_T
    self.drawConnections(
(self.obj883,self.obj843,[992.0, 641.0, 1032.0, 691.0],"true", 2) )
    # Connections for obj884 (graphObject_: Obj781) of type directLink_T
    self.drawConnections(
(self.obj884,self.obj844,[806.0, 693.0, 752.0, 771.0],"true", 2) )
    # Connections for obj885 (graphObject_: Obj782) of type directLink_S
    self.drawConnections(
(self.obj885,self.obj834,[470.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj886 (graphObject_: Obj783) of type directLink_S
    self.drawConnections(
(self.obj886,self.obj836,[670.0, 83.0, 770.0, 83.0],"true", 2) )
    # Connections for obj887 (graphObject_: Obj784) of type directLink_S
    self.drawConnections(
(self.obj887,self.obj837,[870.0, 83.0, 970.0, 83.0],"true", 2) )
    # Connections for obj888 (graphObject_: Obj785) of type directLink_S
    self.drawConnections(
(self.obj888,self.obj832,[470.0, 133.0, 650.0, 183.0],"true", 2) )
    # Connections for obj889 (graphObject_: Obj786) of type directLink_S
    self.drawConnections(
(self.obj889,self.obj833,[670.0, 183.0, 890.0, 183.0],"true", 2) )
    # Connections for obj890 (graphObject_: Obj787) of type directLink_S
    self.drawConnections(
(self.obj890,self.obj835,[400.0, 133.0, 370.0, 83.0],"true", 2) )
    # Connections for obj891 (graphObject_: Obj788) of type backward_link
    self.drawConnections(
(self.obj891,self.obj838,[401.0, 337.0, 450.0, 183.0],"true", 2) )
    # Connections for obj892 (graphObject_: Obj789) of type backward_link
    self.drawConnections(
(self.obj892,self.obj835,[561.0, 427.0, 370.0, 83.0],"true", 2) )
    # Connections for obj893 (graphObject_: Obj790) of type hasAttribute_S
    self.drawConnections(
(self.obj893,self.obj846,[972.0, 178.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj894 (graphObject_: Obj791) of type hasAttribute_S
    self.drawConnections(
(self.obj894,self.obj847,[462.0, 228.5, 434.0, 274.0],"true", 2) )
    # Connections for obj895 (graphObject_: Obj792) of type hasAttribute_T
    self.drawConnections(
(self.obj895,self.obj848,[573.0, 442.5, 594.0, 394.0],"true", 2) )
    # Connections for obj896 (graphObject_: Obj793) of type hasAttribute_T
    self.drawConnections(
(self.obj896,self.obj849,[963.0, 442.5, 974.0, 394.0],"true", 2) )
    # Connections for obj897 (graphObject_: Obj794) of type hasAttribute_T
    self.drawConnections(
(self.obj897,self.obj850,[383.0, 532.5, 414.0, 574.0],"true", 2) )
    # Connections for obj898 (graphObject_: Obj795) of type hasAttribute_T
    self.drawConnections(
(self.obj898,self.obj851,[1063.0, 732.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj899 (graphObject_: Obj796) of type hasAttribute_T
    self.drawConnections(
(self.obj899,self.obj852,[763.0, 812.5, 854.0, 854.0],"true", 2) )
    # Connections for obj900 (graphObject_: Obj797) of type leftExpr
    self.drawConnections(
(self.obj900,self.obj847,[456.0, 316.5, 434.0, 274.0],"true", 2) )
    # Connections for obj901 (graphObject_: Obj798) of type leftExpr
    self.drawConnections(
(self.obj901,self.obj848,[616.0, 358.5, 594.0, 394.0],"true", 2) )
    # Connections for obj902 (graphObject_: Obj799) of type leftExpr
    self.drawConnections(
(self.obj902,self.obj849,[956.0, 356.5, 974.0, 394.0],"true", 2) )
    # Connections for obj903 (graphObject_: Obj800) of type leftExpr
    self.drawConnections(
(self.obj903,self.obj850,[386.0, 616.5, 414.0, 574.0],"true", 2) )
    # Connections for obj904 (graphObject_: Obj801) of type leftExpr
    self.drawConnections(
(self.obj904,self.obj851,[1066.0, 816.5, 1094.0, 774.0],"true", 2) )
    # Connections for obj905 (graphObject_: Obj802) of type leftExpr
    self.drawConnections(
(self.obj905,self.obj852,[781.5, 856.5, 854.0, 854.0],"true", 2) )
    # Connections for obj906 (graphObject_: Obj803) of type rightExpr
    self.drawConnections(
(self.obj906,self.obj859,[376.0, 316.5, 294.0, 274.0],"true", 2) )
    # Connections for obj907 (graphObject_: Obj804) of type rightExpr
    self.drawConnections(
(self.obj907,self.obj846,[648.0, 251.5, 1054.0, 174.0],"true", 2) )
    # Connections for obj908 (graphObject_: Obj805) of type rightExpr
    self.drawConnections(
(self.obj908,self.obj860,[886.0, 356.5, 834.0, 394.0],"true", 2) )
    # Connections for obj909 (graphObject_: Obj806) of type rightExpr
    self.drawConnections(
(self.obj909,self.obj861,[316.0, 616.5, 274.0, 574.0],"true", 2) )
    # Connections for obj910 (graphObject_: Obj807) of type rightExpr
    self.drawConnections(
(self.obj910,self.obj862,[996.0, 816.5, 954.0, 774.0],"true", 2) )
    # Connections for obj911 (graphObject_: Obj808) of type rightExpr
    self.drawConnections(
(self.obj911,self.obj863,[631.5, 856.5, 554.0, 854.0],"true", 2) )

newfunction = Transition2HListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
