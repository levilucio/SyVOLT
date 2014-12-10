"""
__BasicState2ProcDef_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 14:28:50 2014
________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from State import *
from ProcDef import *
from Trigger_T import *
from Listen import *
from ListenBranch import *
from Attribute import *
from Equation import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from backward_link import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from graph_Equation import *
from graph_hasAttribute_T import *
from graph_Attribute import *
from graph_hasAttribute_S import *
from graph_backward_link import *
from graph_ListenBranch import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_Trigger_T import *
from graph_match_contains import *
from graph_leftExpr import *
from graph_ProcDef import *
from graph_Listen import *
from graph_ApplyModel import *
from graph_State import *
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

def BasicState2ProcDef_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('BasicState2ProcDef')
    # --- ASG attributes over ---


    self.obj802=MatchModel(self)
    self.obj802.isGraphObjectVisual = True

    if(hasattr(self.obj802, '_setHierarchicalLink')):
      self.obj802._setHierarchicalLink(False)

    self.obj802.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,60.0,self.obj802)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj802.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj802)
    self.globalAndLocalPostcondition(self.obj802, rootNode)
    self.obj802.postAction( rootNode.CREATE )

    self.obj803=ApplyModel(self)
    self.obj803.isGraphObjectVisual = True

    if(hasattr(self.obj803, '_setHierarchicalLink')):
      self.obj803._setHierarchicalLink(False)

    self.obj803.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,260.0,self.obj803)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj803.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj803)
    self.globalAndLocalPostcondition(self.obj803, rootNode)
    self.obj803.postAction( rootNode.CREATE )

    self.obj804=State(self)
    self.obj804.isGraphObjectVisual = True

    if(hasattr(self.obj804, '_setHierarchicalLink')):
      self.obj804._setHierarchicalLink(False)

    # name
    self.obj804.name.setValue('state1')

    # classtype
    self.obj804.classtype.setValue('State')

    # cardinality
    self.obj804.cardinality.setValue('+')

    self.obj804.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(260.0,60.0,self.obj804)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj804.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj804)
    self.globalAndLocalPostcondition(self.obj804, rootNode)
    self.obj804.postAction( rootNode.CREATE )

    self.obj805=ProcDef(self)
    self.obj805.isGraphObjectVisual = True

    if(hasattr(self.obj805, '_setHierarchicalLink')):
      self.obj805._setHierarchicalLink(False)

    # classtype
    self.obj805.classtype.setValue('ProcDef')

    # cardinality
    self.obj805.cardinality.setValue('1')

    # name
    self.obj805.name.setValue('procdef1')

    self.obj805.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(220.0,300.0,self.obj805)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj805.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj805)
    self.globalAndLocalPostcondition(self.obj805, rootNode)
    self.obj805.postAction( rootNode.CREATE )

    self.obj806=Trigger_T(self)
    self.obj806.isGraphObjectVisual = True

    if(hasattr(self.obj806, '_setHierarchicalLink')):
      self.obj806._setHierarchicalLink(False)

    # classtype
    self.obj806.classtype.setValue('Trigger_T')

    # cardinality
    self.obj806.cardinality.setValue('1')

    # name
    self.obj806.name.setValue('triggerT1')

    self.obj806.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(840.0,300.0,self.obj806)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj806.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj806)
    self.globalAndLocalPostcondition(self.obj806, rootNode)
    self.obj806.postAction( rootNode.CREATE )

    self.obj807=Listen(self)
    self.obj807.isGraphObjectVisual = True

    if(hasattr(self.obj807, '_setHierarchicalLink')):
      self.obj807._setHierarchicalLink(False)

    # classtype
    self.obj807.classtype.setValue('Listen')

    # cardinality
    self.obj807.cardinality.setValue('1')

    # name
    self.obj807.name.setValue('listen1')

    self.obj807.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(440.0,300.0,self.obj807)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj807.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj807)
    self.globalAndLocalPostcondition(self.obj807, rootNode)
    self.obj807.postAction( rootNode.CREATE )

    self.obj808=ListenBranch(self)
    self.obj808.isGraphObjectVisual = True

    if(hasattr(self.obj808, '_setHierarchicalLink')):
      self.obj808._setHierarchicalLink(False)

    # classtype
    self.obj808.classtype.setValue('ListenBranch')

    # cardinality
    self.obj808.cardinality.setValue('1')

    # name
    self.obj808.name.setValue('listenbranch1')

    self.obj808.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(640.0,300.0,self.obj808)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj808.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj808)
    self.globalAndLocalPostcondition(self.obj808, rootNode)
    self.obj808.postAction( rootNode.CREATE )

    self.obj809=Attribute(self)
    self.obj809.isGraphObjectVisual = True

    if(hasattr(self.obj809, '_setHierarchicalLink')):
      self.obj809._setHierarchicalLink(False)

    # Type
    self.obj809.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj809.Type.config = 0

    # name
    self.obj809.name.setValue('isComposite')

    self.obj809.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,7.0,self.obj809)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj809.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj809)
    self.globalAndLocalPostcondition(self.obj809, rootNode)
    self.obj809.postAction( rootNode.CREATE )

    self.obj810=Attribute(self)
    self.obj810.isGraphObjectVisual = True

    if(hasattr(self.obj810, '_setHierarchicalLink')):
      self.obj810._setHierarchicalLink(False)

    # Type
    self.obj810.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj810.Type.config = 0

    # name
    self.obj810.name.setValue('hasOutgoingTransitions')

    self.obj810.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,80.0,self.obj810)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj810.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj810)
    self.globalAndLocalPostcondition(self.obj810, rootNode)
    self.obj810.postAction( rootNode.CREATE )

    self.obj811=Attribute(self)
    self.obj811.isGraphObjectVisual = True

    if(hasattr(self.obj811, '_setHierarchicalLink')):
      self.obj811._setHierarchicalLink(False)

    # Type
    self.obj811.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj811.Type.config = 0

    # name
    self.obj811.name.setValue('channel')

    self.obj811.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(560.0,420.0,self.obj811)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj811.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj811)
    self.globalAndLocalPostcondition(self.obj811, rootNode)
    self.obj811.postAction( rootNode.CREATE )

    self.obj812=Attribute(self)
    self.obj812.isGraphObjectVisual = True

    if(hasattr(self.obj812, '_setHierarchicalLink')):
      self.obj812._setHierarchicalLink(False)

    # Type
    self.obj812.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj812.Type.config = 0

    # name
    self.obj812.name.setValue('channel')

    self.obj812.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(900.0,420.0,self.obj812)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj812.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj812)
    self.globalAndLocalPostcondition(self.obj812, rootNode)
    self.obj812.postAction( rootNode.CREATE )

    self.obj813=Attribute(self)
    self.obj813.isGraphObjectVisual = True

    if(hasattr(self.obj813, '_setHierarchicalLink')):
      self.obj813._setHierarchicalLink(False)

    # Type
    self.obj813.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj813.Type.config = 0

    # name
    self.obj813.name.setValue('pivotin')

    self.obj813.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(220.0,420.0,self.obj813)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj813.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj813)
    self.globalAndLocalPostcondition(self.obj813, rootNode)
    self.obj813.postAction( rootNode.CREATE )

    self.obj814=Attribute(self)
    self.obj814.isGraphObjectVisual = True

    if(hasattr(self.obj814, '_setHierarchicalLink')):
      self.obj814._setHierarchicalLink(False)

    # Type
    self.obj814.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj814.Type.config = 0

    # name
    self.obj814.name.setValue('pivotout')

    self.obj814.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,226.0,self.obj814)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj814.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj814)
    self.globalAndLocalPostcondition(self.obj814, rootNode)
    self.obj814.postAction( rootNode.CREATE )

    self.obj815=Equation(self)
    self.obj815.isGraphObjectVisual = True

    if(hasattr(self.obj815, '_setHierarchicalLink')):
      self.obj815._setHierarchicalLink(False)

    # name
    self.obj815.name.setValue('eq1')

    self.obj815.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(720.0,7.0,self.obj815)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj815.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj815)
    self.globalAndLocalPostcondition(self.obj815, rootNode)
    self.obj815.postAction( rootNode.CREATE )

    self.obj816=Equation(self)
    self.obj816.isGraphObjectVisual = True

    if(hasattr(self.obj816, '_setHierarchicalLink')):
      self.obj816._setHierarchicalLink(False)

    # name
    self.obj816.name.setValue('eq2')

    self.obj816.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(720.0,80.0,self.obj816)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj816.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj816)
    self.globalAndLocalPostcondition(self.obj816, rootNode)
    self.obj816.postAction( rootNode.CREATE )

    self.obj817=Equation(self)
    self.obj817.isGraphObjectVisual = True

    if(hasattr(self.obj817, '_setHierarchicalLink')):
      self.obj817._setHierarchicalLink(False)

    # name
    self.obj817.name.setValue('eq3')

    self.obj817.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(400.0,460.0,self.obj817)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj817.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj817)
    self.globalAndLocalPostcondition(self.obj817, rootNode)
    self.obj817.postAction( rootNode.CREATE )

    self.obj818=Equation(self)
    self.obj818.isGraphObjectVisual = True

    if(hasattr(self.obj818, '_setHierarchicalLink')):
      self.obj818._setHierarchicalLink(False)

    # name
    self.obj818.name.setValue('eq4')

    self.obj818.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(740.0,460.0,self.obj818)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj818.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj818)
    self.globalAndLocalPostcondition(self.obj818, rootNode)
    self.obj818.postAction( rootNode.CREATE )

    self.obj819=Equation(self)
    self.obj819.isGraphObjectVisual = True

    if(hasattr(self.obj819, '_setHierarchicalLink')):
      self.obj819._setHierarchicalLink(False)

    # name
    self.obj819.name.setValue('eq5')

    self.obj819.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(80.0,480.0,self.obj819)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj819.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj819)
    self.globalAndLocalPostcondition(self.obj819, rootNode)
    self.obj819.postAction( rootNode.CREATE )

    self.obj820=Equation(self)
    self.obj820.isGraphObjectVisual = True

    if(hasattr(self.obj820, '_setHierarchicalLink')):
      self.obj820._setHierarchicalLink(False)

    # name
    self.obj820.name.setValue('eq6')

    self.obj820.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(520.0,151.0,self.obj820)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj820.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj820)
    self.globalAndLocalPostcondition(self.obj820, rootNode)
    self.obj820.postAction( rootNode.CREATE )

    self.obj821=Constant(self)
    self.obj821.isGraphObjectVisual = True

    if(hasattr(self.obj821, '_setHierarchicalLink')):
      self.obj821._setHierarchicalLink(False)

    # Type
    self.obj821.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj821.Type.config = 0

    # name
    self.obj821.name.setValue('false')

    self.obj821.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(920.0,7.0,self.obj821)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj821.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj821)
    self.globalAndLocalPostcondition(self.obj821, rootNode)
    self.obj821.postAction( rootNode.CREATE )

    self.obj822=Constant(self)
    self.obj822.isGraphObjectVisual = True

    if(hasattr(self.obj822, '_setHierarchicalLink')):
      self.obj822._setHierarchicalLink(False)

    # Type
    self.obj822.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj822.Type.config = 0

    # name
    self.obj822.name.setValue('true')

    self.obj822.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(920.0,80.0,self.obj822)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj822.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj822)
    self.globalAndLocalPostcondition(self.obj822, rootNode)
    self.obj822.postAction( rootNode.CREATE )

    self.obj823=Constant(self)
    self.obj823.isGraphObjectVisual = True

    if(hasattr(self.obj823, '_setHierarchicalLink')):
      self.obj823._setHierarchicalLink(False)

    # Type
    self.obj823.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj823.Type.config = 0

    # name
    self.obj823.name.setValue('exit')

    self.obj823.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(560.0,500.0,self.obj823)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj823.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj823)
    self.globalAndLocalPostcondition(self.obj823, rootNode)
    self.obj823.postAction( rootNode.CREATE )

    self.obj824=Constant(self)
    self.obj824.isGraphObjectVisual = True

    if(hasattr(self.obj824, '_setHierarchicalLink')):
      self.obj824._setHierarchicalLink(False)

    # Type
    self.obj824.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj824.Type.config = 0

    # name
    self.obj824.name.setValue('exack')

    self.obj824.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(900.0,500.0,self.obj824)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj824.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj824)
    self.globalAndLocalPostcondition(self.obj824, rootNode)
    self.obj824.postAction( rootNode.CREATE )

    self.obj825=Constant(self)
    self.obj825.isGraphObjectVisual = True

    if(hasattr(self.obj825, '_setHierarchicalLink')):
      self.obj825._setHierarchicalLink(False)

    # Type
    self.obj825.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj825.Type.config = 0

    # name
    self.obj825.name.setValue('procdef')

    self.obj825.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,500.0,self.obj825)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj825.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj825)
    self.globalAndLocalPostcondition(self.obj825, rootNode)
    self.obj825.postAction( rootNode.CREATE )

    self.obj826=Constant(self)
    self.obj826.isGraphObjectVisual = True

    if(hasattr(self.obj826, '_setHierarchicalLink')):
      self.obj826._setHierarchicalLink(False)

    # Type
    self.obj826.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj826.Type.config = 0

    # name
    self.obj826.name.setValue('listensimplestate')

    self.obj826.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,226.0,self.obj826)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj826.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj826)
    self.globalAndLocalPostcondition(self.obj826, rootNode)
    self.obj826.postAction( rootNode.CREATE )

    self.obj827=paired_with(self)
    self.obj827.isGraphObjectVisual = True

    if(hasattr(self.obj827, '_setHierarchicalLink')):
      self.obj827._setHierarchicalLink(False)

    self.obj827.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(126.5,213.0,self.obj827)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj827.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj827)
    self.globalAndLocalPostcondition(self.obj827, rootNode)
    self.obj827.postAction( rootNode.CREATE )

    self.obj828=match_contains(self)
    self.obj828.isGraphObjectVisual = True

    if(hasattr(self.obj828, '_setHierarchicalLink')):
      self.obj828._setHierarchicalLink(False)

    self.obj828.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(364.0,107.0,self.obj828)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj828.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj828)
    self.globalAndLocalPostcondition(self.obj828, rootNode)
    self.obj828.postAction( rootNode.CREATE )

    self.obj829=apply_contains(self)
    self.obj829.isGraphObjectVisual = True

    if(hasattr(self.obj829, '_setHierarchicalLink')):
      self.obj829._setHierarchicalLink(False)

    self.obj829.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(367.5,342.0,self.obj829)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj829.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj829)
    self.globalAndLocalPostcondition(self.obj829, rootNode)
    self.obj829.postAction( rootNode.CREATE )

    self.obj830=apply_contains(self)
    self.obj830.isGraphObjectVisual = True

    if(hasattr(self.obj830, '_setHierarchicalLink')):
      self.obj830._setHierarchicalLink(False)

    self.obj830.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(377.5,322.0,self.obj830)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj830.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj830)
    self.globalAndLocalPostcondition(self.obj830, rootNode)
    self.obj830.postAction( rootNode.CREATE )

    self.obj831=apply_contains(self)
    self.obj831.isGraphObjectVisual = True

    if(hasattr(self.obj831, '_setHierarchicalLink')):
      self.obj831._setHierarchicalLink(False)

    self.obj831.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(477.5,322.0,self.obj831)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj831.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj831)
    self.globalAndLocalPostcondition(self.obj831, rootNode)
    self.obj831.postAction( rootNode.CREATE )

    self.obj832=apply_contains(self)
    self.obj832.isGraphObjectVisual = True

    if(hasattr(self.obj832, '_setHierarchicalLink')):
      self.obj832._setHierarchicalLink(False)

    self.obj832.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(577.5,322.0,self.obj832)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj832.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj832)
    self.globalAndLocalPostcondition(self.obj832, rootNode)
    self.obj832.postAction( rootNode.CREATE )

    self.obj833=directLink_T(self)
    self.obj833.isGraphObjectVisual = True

    if(hasattr(self.obj833, '_setHierarchicalLink')):
      self.obj833._setHierarchicalLink(False)

    # associationType
    self.obj833.associationType.setValue('p')

    self.obj833.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(552.0,351.0,self.obj833)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj833.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj833)
    self.globalAndLocalPostcondition(self.obj833, rootNode)
    self.obj833.postAction( rootNode.CREATE )

    self.obj834=directLink_T(self)
    self.obj834.isGraphObjectVisual = True

    if(hasattr(self.obj834, '_setHierarchicalLink')):
      self.obj834._setHierarchicalLink(False)

    # associationType
    self.obj834.associationType.setValue('branches')

    self.obj834.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,351.0,self.obj834)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj834.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj834)
    self.globalAndLocalPostcondition(self.obj834, rootNode)
    self.obj834.postAction( rootNode.CREATE )

    self.obj835=directLink_T(self)
    self.obj835.isGraphObjectVisual = True

    if(hasattr(self.obj835, '_setHierarchicalLink')):
      self.obj835._setHierarchicalLink(False)

    # associationType
    self.obj835.associationType.setValue('p')

    self.obj835.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(952.0,351.0,self.obj835)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj835.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj835)
    self.globalAndLocalPostcondition(self.obj835, rootNode)
    self.obj835.postAction( rootNode.CREATE )

    self.obj836=backward_link(self)
    self.obj836.isGraphObjectVisual = True

    if(hasattr(self.obj836, '_setHierarchicalLink')):
      self.obj836._setHierarchicalLink(False)

    # type
    self.obj836.type.setValue('ruleDef')

    self.obj836.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(411.0,227.0,self.obj836)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj836.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj836)
    self.globalAndLocalPostcondition(self.obj836, rootNode)
    self.obj836.postAction( rootNode.CREATE )

    self.obj837=hasAttribute_S(self)
    self.obj837.isGraphObjectVisual = True

    if(hasattr(self.obj837, '_setHierarchicalLink')):
      self.obj837._setHierarchicalLink(False)

    self.obj837.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(532.0,78.5,self.obj837)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj837.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj837)
    self.globalAndLocalPostcondition(self.obj837, rootNode)
    self.obj837.postAction( rootNode.CREATE )

    self.obj838=hasAttribute_S(self)
    self.obj838.isGraphObjectVisual = True

    if(hasattr(self.obj838, '_setHierarchicalLink')):
      self.obj838._setHierarchicalLink(False)

    self.obj838.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(489.0,113.5,self.obj838)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj838.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj838)
    self.globalAndLocalPostcondition(self.obj838, rootNode)
    self.obj838.postAction( rootNode.CREATE )

    self.obj839=hasAttribute_T(self)
    self.obj839.isGraphObjectVisual = True

    if(hasattr(self.obj839, '_setHierarchicalLink')):
      self.obj839._setHierarchicalLink(False)

    self.obj839.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(753.0,402.5,self.obj839)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj839.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj839)
    self.globalAndLocalPostcondition(self.obj839, rootNode)
    self.obj839.postAction( rootNode.CREATE )

    self.obj840=hasAttribute_T(self)
    self.obj840.isGraphObjectVisual = True

    if(hasattr(self.obj840, '_setHierarchicalLink')):
      self.obj840._setHierarchicalLink(False)

    self.obj840.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1018.0,416.5,self.obj840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj840)
    self.globalAndLocalPostcondition(self.obj840, rootNode)
    self.obj840.postAction( rootNode.CREATE )

    self.obj841=hasAttribute_T(self)
    self.obj841.isGraphObjectVisual = True

    if(hasattr(self.obj841, '_setHierarchicalLink')):
      self.obj841._setHierarchicalLink(False)

    self.obj841.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(373.0,402.5,self.obj841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj841)
    self.globalAndLocalPostcondition(self.obj841, rootNode)
    self.obj841.postAction( rootNode.CREATE )

    self.obj842=hasAttribute_T(self)
    self.obj842.isGraphObjectVisual = True

    if(hasattr(self.obj842, '_setHierarchicalLink')):
      self.obj842._setHierarchicalLink(False)

    self.obj842.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(593.0,305.5,self.obj842)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj842.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj842)
    self.globalAndLocalPostcondition(self.obj842, rootNode)
    self.obj842.postAction( rootNode.CREATE )

    self.obj843=leftExpr(self)
    self.obj843.isGraphObjectVisual = True

    if(hasattr(self.obj843, '_setHierarchicalLink')):
      self.obj843._setHierarchicalLink(False)

    self.obj843.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(746.0,56.5,self.obj843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj843)
    self.globalAndLocalPostcondition(self.obj843, rootNode)
    self.obj843.postAction( rootNode.CREATE )

    self.obj844=leftExpr(self)
    self.obj844.isGraphObjectVisual = True

    if(hasattr(self.obj844, '_setHierarchicalLink')):
      self.obj844._setHierarchicalLink(False)

    self.obj844.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(703.0,112.5,self.obj844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj844)
    self.globalAndLocalPostcondition(self.obj844, rootNode)
    self.obj844.postAction( rootNode.CREATE )

    self.obj845=leftExpr(self)
    self.obj845.isGraphObjectVisual = True

    if(hasattr(self.obj845, '_setHierarchicalLink')):
      self.obj845._setHierarchicalLink(False)

    self.obj845.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(616.0,476.5,self.obj845)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj845.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj845)
    self.globalAndLocalPostcondition(self.obj845, rootNode)
    self.obj845.postAction( rootNode.CREATE )

    self.obj846=leftExpr(self)
    self.obj846.isGraphObjectVisual = True

    if(hasattr(self.obj846, '_setHierarchicalLink')):
      self.obj846._setHierarchicalLink(False)

    self.obj846.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,476.5,self.obj846)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj846.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj846)
    self.globalAndLocalPostcondition(self.obj846, rootNode)
    self.obj846.postAction( rootNode.CREATE )

    self.obj847=leftExpr(self)
    self.obj847.isGraphObjectVisual = True

    if(hasattr(self.obj847, '_setHierarchicalLink')):
      self.obj847._setHierarchicalLink(False)

    self.obj847.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(286.0,486.5,self.obj847)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj847.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj847)
    self.globalAndLocalPostcondition(self.obj847, rootNode)
    self.obj847.postAction( rootNode.CREATE )

    self.obj848=leftExpr(self)
    self.obj848.isGraphObjectVisual = True

    if(hasattr(self.obj848, '_setHierarchicalLink')):
      self.obj848._setHierarchicalLink(False)

    self.obj848.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(616.0,225.0,self.obj848)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj848.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj848)
    self.globalAndLocalPostcondition(self.obj848, rootNode)
    self.obj848.postAction( rootNode.CREATE )

    self.obj849=rightExpr(self)
    self.obj849.isGraphObjectVisual = True

    if(hasattr(self.obj849, '_setHierarchicalLink')):
      self.obj849._setHierarchicalLink(False)

    self.obj849.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(956.0,56.5,self.obj849)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj849.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj849)
    self.globalAndLocalPostcondition(self.obj849, rootNode)
    self.obj849.postAction( rootNode.CREATE )

    self.obj850=rightExpr(self)
    self.obj850.isGraphObjectVisual = True

    if(hasattr(self.obj850, '_setHierarchicalLink')):
      self.obj850._setHierarchicalLink(False)

    self.obj850.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(907.0,114.5,self.obj850)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj850.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj850)
    self.globalAndLocalPostcondition(self.obj850, rootNode)
    self.obj850.postAction( rootNode.CREATE )

    self.obj851=rightExpr(self)
    self.obj851.isGraphObjectVisual = True

    if(hasattr(self.obj851, '_setHierarchicalLink')):
      self.obj851._setHierarchicalLink(False)

    self.obj851.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(616.0,516.5,self.obj851)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj851.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj851)
    self.globalAndLocalPostcondition(self.obj851, rootNode)
    self.obj851.postAction( rootNode.CREATE )

    self.obj852=rightExpr(self)
    self.obj852.isGraphObjectVisual = True

    if(hasattr(self.obj852, '_setHierarchicalLink')):
      self.obj852._setHierarchicalLink(False)

    self.obj852.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(956.0,516.5,self.obj852)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj852.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj852)
    self.globalAndLocalPostcondition(self.obj852, rootNode)
    self.obj852.postAction( rootNode.CREATE )

    self.obj853=rightExpr(self)
    self.obj853.isGraphObjectVisual = True

    if(hasattr(self.obj853, '_setHierarchicalLink')):
      self.obj853._setHierarchicalLink(False)

    self.obj853.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(296.0,526.5,self.obj853)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj853.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj853)
    self.globalAndLocalPostcondition(self.obj853, rootNode)
    self.obj853.postAction( rootNode.CREATE )

    self.obj854=rightExpr(self)
    self.obj854.isGraphObjectVisual = True

    if(hasattr(self.obj854, '_setHierarchicalLink')):
      self.obj854._setHierarchicalLink(False)

    self.obj854.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(696.0,225.0,self.obj854)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj854.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj854)
    self.globalAndLocalPostcondition(self.obj854, rootNode)
    self.obj854.postAction( rootNode.CREATE )

    # Connections for obj802 (graphObject_: Obj167) of type MatchModel
    self.drawConnections(
(self.obj802,self.obj827,[138.0, 91.0, 126.5, 213.0],"true", 2),
(self.obj802,self.obj828,[138.0, 91.0, 364.0, 107.0],"true", 2) )
    # Connections for obj803 (graphObject_: Obj168) of type ApplyModel
    self.drawConnections(
(self.obj803,self.obj829,[143.0, 293.0, 367.5, 342.0],"true", 2),
(self.obj803,self.obj830,[143.0, 293.0, 377.5, 322.0],"true", 2),
(self.obj803,self.obj831,[143.0, 293.0, 477.5, 322.0],"true", 2),
(self.obj803,self.obj832,[143.0, 293.0, 577.5, 322.0],"true", 2) )
    # Connections for obj804 (graphObject_: Obj169) named state1
    self.drawConnections(
(self.obj804,self.obj837,[430.0, 103.0, 532.0, 78.5],"true", 2),
(self.obj804,self.obj838,[430.0, 103.0, 489.0, 113.5],"true", 2) )
    # Connections for obj805 (graphObject_: Obj170) named procdef1
    self.drawConnections(
(self.obj805,self.obj833,[392.0, 351.0, 552.0, 351.0],"true", 2),
(self.obj805,self.obj836,[392.0, 351.0, 411.0, 227.0],"true", 2),
(self.obj805,self.obj841,[392.0, 351.0, 373.0, 402.5],"true", 2) )
    # Connections for obj806 (graphObject_: Obj171) named triggerT1
    self.drawConnections(
(self.obj806,self.obj840,[1012.0, 351.0, 1018.0, 416.5],"true", 2) )
    # Connections for obj807 (graphObject_: Obj172) named listen1
    self.drawConnections(
(self.obj807,self.obj834,[612.0, 351.0, 752.0, 351.0],"true", 2),
(self.obj807,self.obj842,[612.0, 351.0, 593.0, 305.5],"true", 2) )
    # Connections for obj808 (graphObject_: Obj173) named listenbranch1
    self.drawConnections(
(self.obj808,self.obj835,[812.0, 351.0, 952.0, 351.0],"true", 2),
(self.obj808,self.obj839,[812.0, 351.0, 753.0, 402.5],"true", 2) )
    # Connections for obj809 (graphObject_: Obj174) named isComposite
    self.drawConnections(
 )
    # Connections for obj810 (graphObject_: Obj175) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj811 (graphObject_: Obj176) named channel
    self.drawConnections(
 )
    # Connections for obj812 (graphObject_: Obj177) named channel
    self.drawConnections(
 )
    # Connections for obj813 (graphObject_: Obj178) named pivotin
    self.drawConnections(
 )
    # Connections for obj814 (graphObject_: Obj179) named pivotout
    self.drawConnections(
 )
    # Connections for obj815 (graphObject_: Obj180) named eq1
    self.drawConnections(
(self.obj815,self.obj843,[858.0, 46.0, 746.0, 56.5],"true", 2),
(self.obj815,self.obj849,[858.0, 46.0, 956.0, 56.5],"true", 2) )
    # Connections for obj816 (graphObject_: Obj181) named eq2
    self.drawConnections(
(self.obj816,self.obj844,[858.0, 119.0, 703.0, 112.5],"true", 2),
(self.obj816,self.obj850,[858.0, 119.0, 907.0, 114.5],"true", 2) )
    # Connections for obj817 (graphObject_: Obj182) named eq3
    self.drawConnections(
(self.obj817,self.obj845,[538.0, 499.0, 616.0, 476.5],"true", 2),
(self.obj817,self.obj851,[538.0, 499.0, 616.0, 516.5],"true", 2) )
    # Connections for obj818 (graphObject_: Obj183) named eq4
    self.drawConnections(
(self.obj818,self.obj846,[878.0, 499.0, 956.0, 476.5],"true", 2),
(self.obj818,self.obj852,[878.0, 499.0, 956.0, 516.5],"true", 2) )
    # Connections for obj819 (graphObject_: Obj184) named eq5
    self.drawConnections(
(self.obj819,self.obj847,[218.0, 519.0, 286.0, 486.5],"true", 2),
(self.obj819,self.obj853,[218.0, 519.0, 296.0, 526.5],"true", 2) )
    # Connections for obj820 (graphObject_: Obj185) named eq6
    self.drawConnections(
(self.obj820,self.obj848,[658.0, 190.0, 616.0, 225.0],"true", 2),
(self.obj820,self.obj854,[658.0, 190.0, 696.0, 225.0],"true", 2) )
    # Connections for obj821 (graphObject_: Obj186) named false
    self.drawConnections(
 )
    # Connections for obj822 (graphObject_: Obj187) named true
    self.drawConnections(
 )
    # Connections for obj823 (graphObject_: Obj188) named exit
    self.drawConnections(
 )
    # Connections for obj824 (graphObject_: Obj189) named exack
    self.drawConnections(
 )
    # Connections for obj825 (graphObject_: Obj190) named procdef
    self.drawConnections(
 )
    # Connections for obj826 (graphObject_: Obj191) named listensimplestate
    self.drawConnections(
 )
    # Connections for obj827 (graphObject_: Obj192) of type paired_with
    self.drawConnections(
(self.obj827,self.obj803,[126.5, 213.0, 143.0, 293.0],"true", 2) )
    # Connections for obj828 (graphObject_: Obj193) of type match_contains
    self.drawConnections(
(self.obj828,self.obj804,[364.0, 107.0, 430.0, 103.0],"true", 2) )
    # Connections for obj829 (graphObject_: Obj194) of type apply_contains
    self.drawConnections(
(self.obj829,self.obj805,[367.5, 342.0, 392.0, 351.0],"true", 2) )
    # Connections for obj830 (graphObject_: Obj195) of type apply_contains
    self.drawConnections(
(self.obj830,self.obj807,[377.5, 322.0, 612.0, 351.0],"true", 2) )
    # Connections for obj831 (graphObject_: Obj196) of type apply_contains
    self.drawConnections(
(self.obj831,self.obj808,[477.5, 322.0, 812.0, 351.0],"true", 2) )
    # Connections for obj832 (graphObject_: Obj197) of type apply_contains
    self.drawConnections(
(self.obj832,self.obj806,[577.5, 322.0, 1012.0, 351.0],"true", 2) )
    # Connections for obj833 (graphObject_: Obj198) of type directLink_T
    self.drawConnections(
(self.obj833,self.obj807,[552.0, 351.0, 612.0, 351.0],"true", 2) )
    # Connections for obj834 (graphObject_: Obj199) of type directLink_T
    self.drawConnections(
(self.obj834,self.obj808,[752.0, 351.0, 812.0, 351.0],"true", 2) )
    # Connections for obj835 (graphObject_: Obj200) of type directLink_T
    self.drawConnections(
(self.obj835,self.obj806,[952.0, 351.0, 1012.0, 351.0],"true", 2) )
    # Connections for obj836 (graphObject_: Obj201) of type backward_link
    self.drawConnections(
(self.obj836,self.obj804,[411.0, 227.0, 430.0, 103.0],"true", 2) )
    # Connections for obj837 (graphObject_: Obj202) of type hasAttribute_S
    self.drawConnections(
(self.obj837,self.obj809,[532.0, 78.5, 634.0, 41.0],"true", 2) )
    # Connections for obj838 (graphObject_: Obj203) of type hasAttribute_S
    self.drawConnections(
(self.obj838,self.obj810,[532.0, 128.5, 634.0, 114.0],"true", 2) )
    # Connections for obj839 (graphObject_: Obj204) of type hasAttribute_T
    self.drawConnections(
(self.obj839,self.obj811,[753.0, 402.5, 694.0, 454.0],"true", 2) )
    # Connections for obj840 (graphObject_: Obj205) of type hasAttribute_T
    self.drawConnections(
(self.obj840,self.obj812,[1018.0, 416.5, 1034.0, 454.0],"true", 2) )
    # Connections for obj841 (graphObject_: Obj206) of type hasAttribute_T
    self.drawConnections(
(self.obj841,self.obj813,[373.0, 402.5, 354.0, 454.0],"true", 2) )
    # Connections for obj842 (graphObject_: Obj207) of type hasAttribute_T
    self.drawConnections(
(self.obj842,self.obj814,[593.0, 305.5, 574.0, 260.0],"true", 2) )
    # Connections for obj843 (graphObject_: Obj208) of type leftExpr
    self.drawConnections(
(self.obj843,self.obj809,[746.0, 56.5, 634.0, 41.0],"true", 2) )
    # Connections for obj844 (graphObject_: Obj209) of type leftExpr
    self.drawConnections(
(self.obj844,self.obj810,[746.0, 156.5, 634.0, 114.0],"true", 2) )
    # Connections for obj845 (graphObject_: Obj210) of type leftExpr
    self.drawConnections(
(self.obj845,self.obj811,[616.0, 476.5, 694.0, 454.0],"true", 2) )
    # Connections for obj846 (graphObject_: Obj211) of type leftExpr
    self.drawConnections(
(self.obj846,self.obj812,[956.0, 476.5, 1034.0, 454.0],"true", 2) )
    # Connections for obj847 (graphObject_: Obj212) of type leftExpr
    self.drawConnections(
(self.obj847,self.obj813,[286.0, 486.5, 354.0, 454.0],"true", 2) )
    # Connections for obj848 (graphObject_: Obj213) of type leftExpr
    self.drawConnections(
(self.obj848,self.obj814,[616.0, 225.0, 574.0, 260.0],"true", 2) )
    # Connections for obj849 (graphObject_: Obj214) of type rightExpr
    self.drawConnections(
(self.obj849,self.obj821,[956.0, 56.5, 1054.0, 41.0],"true", 2) )
    # Connections for obj850 (graphObject_: Obj215) of type rightExpr
    self.drawConnections(
(self.obj850,self.obj822,[956.0, 156.5, 1054.0, 114.0],"true", 2) )
    # Connections for obj851 (graphObject_: Obj216) of type rightExpr
    self.drawConnections(
(self.obj851,self.obj823,[616.0, 516.5, 694.0, 534.0],"true", 2) )
    # Connections for obj852 (graphObject_: Obj217) of type rightExpr
    self.drawConnections(
(self.obj852,self.obj824,[956.0, 516.5, 1034.0, 534.0],"true", 2) )
    # Connections for obj853 (graphObject_: Obj218) of type rightExpr
    self.drawConnections(
(self.obj853,self.obj825,[296.0, 526.5, 374.0, 534.0],"true", 2) )
    # Connections for obj854 (graphObject_: Obj219) of type rightExpr
    self.drawConnections(
(self.obj854,self.obj826,[696.0, 225.0, 734.0, 260.0],"true", 2) )

newfunction = BasicState2ProcDef_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
