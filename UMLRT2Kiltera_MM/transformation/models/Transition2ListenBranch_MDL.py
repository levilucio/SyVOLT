"""
__Transition2ListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 15:19:50 2014
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


    self.obj1787=MatchModel(self)
    self.obj1787.isGraphObjectVisual = True

    if(hasattr(self.obj1787, '_setHierarchicalLink')):
      self.obj1787._setHierarchicalLink(False)

    self.obj1787.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,21.0,self.obj1787)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1787.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1787)
    self.globalAndLocalPostcondition(self.obj1787, rootNode)
    self.obj1787.postAction( rootNode.CREATE )

    self.obj1788=ApplyModel(self)
    self.obj1788.isGraphObjectVisual = True

    if(hasattr(self.obj1788, '_setHierarchicalLink')):
      self.obj1788._setHierarchicalLink(False)

    self.obj1788.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(24.0,342.0,self.obj1788)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1788.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1788)
    self.globalAndLocalPostcondition(self.obj1788, rootNode)
    self.obj1788.postAction( rootNode.CREATE )

    self.obj1789=Trigger_S(self)
    self.obj1789.isGraphObjectVisual = True

    if(hasattr(self.obj1789, '_setHierarchicalLink')):
      self.obj1789._setHierarchicalLink(False)

    # classtype
    self.obj1789.classtype.setValue('Trigger_S')

    # cardinality
    self.obj1789.cardinality.setValue('1')

    # name
    self.obj1789.name.setValue('triggerS1')

    self.obj1789.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(860.0,180.0,self.obj1789)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1789.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1789)
    self.globalAndLocalPostcondition(self.obj1789, rootNode)
    self.obj1789.postAction( rootNode.CREATE )

    self.obj1790=Signal(self)
    self.obj1790.isGraphObjectVisual = True

    if(hasattr(self.obj1790, '_setHierarchicalLink')):
      self.obj1790._setHierarchicalLink(False)

    # name
    self.obj1790.name.setValue('signal1')

    # classtype
    self.obj1790.classtype.setValue('Signal')

    # cardinality
    self.obj1790.cardinality.setValue('1')

    self.obj1790.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(647.0,140.0,self.obj1790)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1790.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1790)
    self.globalAndLocalPostcondition(self.obj1790, rootNode)
    self.obj1790.postAction( rootNode.CREATE )

    self.obj1791=Transition(self)
    self.obj1791.isGraphObjectVisual = True

    if(hasattr(self.obj1791, '_setHierarchicalLink')):
      self.obj1791._setHierarchicalLink(False)

    # name
    self.obj1791.name.setValue('transition1')

    # classtype
    self.obj1791.classtype.setValue('Transition')

    # cardinality
    self.obj1791.cardinality.setValue('+')

    self.obj1791.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(834.0,80.0,self.obj1791)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1791.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1791)
    self.globalAndLocalPostcondition(self.obj1791, rootNode)
    self.obj1791.postAction( rootNode.CREATE )

    self.obj1792=State(self)
    self.obj1792.isGraphObjectVisual = True

    if(hasattr(self.obj1792, '_setHierarchicalLink')):
      self.obj1792._setHierarchicalLink(False)

    # name
    self.obj1792.name.setValue('state1')

    # classtype
    self.obj1792.classtype.setValue('State')

    # cardinality
    self.obj1792.cardinality.setValue('+')

    self.obj1792.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,80.0,self.obj1792)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1792.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1792)
    self.globalAndLocalPostcondition(self.obj1792, rootNode)
    self.obj1792.postAction( rootNode.CREATE )

    self.obj1793=Listen(self)
    self.obj1793.isGraphObjectVisual = True

    if(hasattr(self.obj1793, '_setHierarchicalLink')):
      self.obj1793._setHierarchicalLink(False)

    # classtype
    self.obj1793.classtype.setValue('Listen')

    # cardinality
    self.obj1793.cardinality.setValue('1')

    # name
    self.obj1793.name.setValue('listen1')

    self.obj1793.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,438.0,self.obj1793)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1793.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1793)
    self.globalAndLocalPostcondition(self.obj1793, rootNode)
    self.obj1793.postAction( rootNode.CREATE )

    self.obj1794=ListenBranch(self)
    self.obj1794.isGraphObjectVisual = True

    if(hasattr(self.obj1794, '_setHierarchicalLink')):
      self.obj1794._setHierarchicalLink(False)

    # classtype
    self.obj1794.classtype.setValue('ListenBranch')

    # cardinality
    self.obj1794.cardinality.setValue('1')

    # name
    self.obj1794.name.setValue('listenBranch1')

    self.obj1794.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(400.0,440.0,self.obj1794)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1794.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1794)
    self.globalAndLocalPostcondition(self.obj1794, rootNode)
    self.obj1794.postAction( rootNode.CREATE )

    self.obj1795=Inst(self)
    self.obj1795.isGraphObjectVisual = True

    if(hasattr(self.obj1795, '_setHierarchicalLink')):
      self.obj1795._setHierarchicalLink(False)

    # classtype
    self.obj1795.classtype.setValue('Inst')

    # cardinality
    self.obj1795.cardinality.setValue('1')

    # name
    self.obj1795.name.setValue('inst1')

    self.obj1795.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(760.0,437.0,self.obj1795)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1795.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1795)
    self.globalAndLocalPostcondition(self.obj1795, rootNode)
    self.obj1795.postAction( rootNode.CREATE )

    self.obj1796=Attribute(self)
    self.obj1796.isGraphObjectVisual = True

    if(hasattr(self.obj1796, '_setHierarchicalLink')):
      self.obj1796._setHierarchicalLink(False)

    # Type
    self.obj1796.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1796.Type.config = 0

    # name
    self.obj1796.name.setValue('isComposite')

    self.obj1796.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,175.0,self.obj1796)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1796.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1796)
    self.globalAndLocalPostcondition(self.obj1796, rootNode)
    self.obj1796.postAction( rootNode.CREATE )

    self.obj1797=Attribute(self)
    self.obj1797.isGraphObjectVisual = True

    if(hasattr(self.obj1797, '_setHierarchicalLink')):
      self.obj1797._setHierarchicalLink(False)

    # Type
    self.obj1797.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1797.Type.config = 0

    # name
    self.obj1797.name.setValue('hasOutgoingTransitions')

    self.obj1797.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(340.0,160.0,self.obj1797)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1797.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1797)
    self.globalAndLocalPostcondition(self.obj1797, rootNode)
    self.obj1797.postAction( rootNode.CREATE )

    self.obj1798=Attribute(self)
    self.obj1798.isGraphObjectVisual = True

    if(hasattr(self.obj1798, '_setHierarchicalLink')):
      self.obj1798._setHierarchicalLink(False)

    # Type
    self.obj1798.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1798.Type.config = 0

    # name
    self.obj1798.name.setValue('name')

    self.obj1798.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,240.0,self.obj1798)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1798.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1798)
    self.globalAndLocalPostcondition(self.obj1798, rootNode)
    self.obj1798.postAction( rootNode.CREATE )

    self.obj1799=Attribute(self)
    self.obj1799.isGraphObjectVisual = True

    if(hasattr(self.obj1799, '_setHierarchicalLink')):
      self.obj1799._setHierarchicalLink(False)

    # Type
    self.obj1799.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1799.Type.config = 0

    # name
    self.obj1799.name.setValue('channel')

    self.obj1799.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(405.0,361.0,self.obj1799)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1799.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1799)
    self.globalAndLocalPostcondition(self.obj1799, rootNode)
    self.obj1799.postAction( rootNode.CREATE )

    self.obj1800=Attribute(self)
    self.obj1800.isGraphObjectVisual = True

    if(hasattr(self.obj1800, '_setHierarchicalLink')):
      self.obj1800._setHierarchicalLink(False)

    # Type
    self.obj1800.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1800.Type.config = 0

    # name
    self.obj1800.name.setValue('pivotin')

    self.obj1800.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(80.0,540.0,self.obj1800)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1800.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1800)
    self.globalAndLocalPostcondition(self.obj1800, rootNode)
    self.obj1800.postAction( rootNode.CREATE )

    self.obj1801=Attribute(self)
    self.obj1801.isGraphObjectVisual = True

    if(hasattr(self.obj1801, '_setHierarchicalLink')):
      self.obj1801._setHierarchicalLink(False)

    # Type
    self.obj1801.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1801.Type.config = 0

    # name
    self.obj1801.name.setValue('pivotin')

    self.obj1801.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,540.0,self.obj1801)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1801.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1801)
    self.globalAndLocalPostcondition(self.obj1801, rootNode)
    self.obj1801.postAction( rootNode.CREATE )

    self.obj1802=Equation(self)
    self.obj1802.isGraphObjectVisual = True

    if(hasattr(self.obj1802, '_setHierarchicalLink')):
      self.obj1802._setHierarchicalLink(False)

    # name
    self.obj1802.name.setValue('eq1')

    self.obj1802.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(303.0,242.0,self.obj1802)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1802.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1802)
    self.globalAndLocalPostcondition(self.obj1802, rootNode)
    self.obj1802.postAction( rootNode.CREATE )

    self.obj1803=Equation(self)
    self.obj1803.isGraphObjectVisual = True

    if(hasattr(self.obj1803, '_setHierarchicalLink')):
      self.obj1803._setHierarchicalLink(False)

    # name
    self.obj1803.name.setValue('eq2')

    self.obj1803.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,240.0,self.obj1803)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1803.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1803)
    self.globalAndLocalPostcondition(self.obj1803, rootNode)
    self.obj1803.postAction( rootNode.CREATE )

    self.obj1804=Equation(self)
    self.obj1804.isGraphObjectVisual = True

    if(hasattr(self.obj1804, '_setHierarchicalLink')):
      self.obj1804._setHierarchicalLink(False)

    # name
    self.obj1804.name.setValue('eq3')

    self.obj1804.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(567.0,361.0,self.obj1804)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1804.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1804)
    self.globalAndLocalPostcondition(self.obj1804, rootNode)
    self.obj1804.postAction( rootNode.CREATE )

    self.obj1805=Equation(self)
    self.obj1805.isGraphObjectVisual = True

    if(hasattr(self.obj1805, '_setHierarchicalLink')):
      self.obj1805._setHierarchicalLink(False)

    # name
    self.obj1805.name.setValue('eq4')

    self.obj1805.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(200.0,620.0,self.obj1805)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1805.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1805)
    self.globalAndLocalPostcondition(self.obj1805, rootNode)
    self.obj1805.postAction( rootNode.CREATE )

    self.obj1806=Equation(self)
    self.obj1806.isGraphObjectVisual = True

    if(hasattr(self.obj1806, '_setHierarchicalLink')):
      self.obj1806._setHierarchicalLink(False)

    # name
    self.obj1806.name.setValue('eq5')

    self.obj1806.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,620.0,self.obj1806)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1806.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1806)
    self.globalAndLocalPostcondition(self.obj1806, rootNode)
    self.obj1806.postAction( rootNode.CREATE )

    self.obj1807=Constant(self)
    self.obj1807.isGraphObjectVisual = True

    if(hasattr(self.obj1807, '_setHierarchicalLink')):
      self.obj1807._setHierarchicalLink(False)

    # Type
    self.obj1807.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1807.Type.config = 0

    # name
    self.obj1807.name.setValue('false')

    self.obj1807.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,260.0,self.obj1807)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1807.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1807)
    self.globalAndLocalPostcondition(self.obj1807, rootNode)
    self.obj1807.postAction( rootNode.CREATE )

    self.obj1808=Constant(self)
    self.obj1808.isGraphObjectVisual = True

    if(hasattr(self.obj1808, '_setHierarchicalLink')):
      self.obj1808._setHierarchicalLink(False)

    # Type
    self.obj1808.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1808.Type.config = 0

    # name
    self.obj1808.name.setValue('true')

    self.obj1808.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(500.0,160.0,self.obj1808)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1808.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1808)
    self.globalAndLocalPostcondition(self.obj1808, rootNode)
    self.obj1808.postAction( rootNode.CREATE )

    self.obj1809=Constant(self)
    self.obj1809.isGraphObjectVisual = True

    if(hasattr(self.obj1809, '_setHierarchicalLink')):
      self.obj1809._setHierarchicalLink(False)

    # Type
    self.obj1809.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1809.Type.config = 0

    # name
    self.obj1809.name.setValue('listensimplestate')

    self.obj1809.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,540.0,self.obj1809)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1809.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1809)
    self.globalAndLocalPostcondition(self.obj1809, rootNode)
    self.obj1809.postAction( rootNode.CREATE )

    self.obj1810=Constant(self)
    self.obj1810.isGraphObjectVisual = True

    if(hasattr(self.obj1810, '_setHierarchicalLink')):
      self.obj1810._setHierarchicalLink(False)

    # Type
    self.obj1810.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1810.Type.config = 0

    # name
    self.obj1810.name.setValue('instfortrans')

    self.obj1810.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(920.0,540.0,self.obj1810)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1810.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1810)
    self.globalAndLocalPostcondition(self.obj1810, rootNode)
    self.obj1810.postAction( rootNode.CREATE )

    self.obj1811=paired_with(self)
    self.obj1811.isGraphObjectVisual = True

    if(hasattr(self.obj1811, '_setHierarchicalLink')):
      self.obj1811._setHierarchicalLink(False)

    self.obj1811.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(142.5,213.5,self.obj1811)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1811.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1811)
    self.globalAndLocalPostcondition(self.obj1811, rootNode)
    self.obj1811.postAction( rootNode.CREATE )

    self.obj1812=match_contains(self)
    self.obj1812.isGraphObjectVisual = True

    if(hasattr(self.obj1812, '_setHierarchicalLink')):
      self.obj1812._setHierarchicalLink(False)

    self.obj1812.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,87.5,self.obj1812)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1812.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1812)
    self.globalAndLocalPostcondition(self.obj1812, rootNode)
    self.obj1812.postAction( rootNode.CREATE )

    self.obj1813=match_contains(self)
    self.obj1813.isGraphObjectVisual = True

    if(hasattr(self.obj1813, '_setHierarchicalLink')):
      self.obj1813._setHierarchicalLink(False)

    self.obj1813.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(571.0,87.5,self.obj1813)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1813.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1813)
    self.globalAndLocalPostcondition(self.obj1813, rootNode)
    self.obj1813.postAction( rootNode.CREATE )

    self.obj1814=match_contains(self)
    self.obj1814.isGraphObjectVisual = True

    if(hasattr(self.obj1814, '_setHierarchicalLink')):
      self.obj1814._setHierarchicalLink(False)

    self.obj1814.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(477.5,117.5,self.obj1814)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1814.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1814)
    self.globalAndLocalPostcondition(self.obj1814, rootNode)
    self.obj1814.postAction( rootNode.CREATE )

    self.obj1815=match_contains(self)
    self.obj1815.isGraphObjectVisual = True

    if(hasattr(self.obj1815, '_setHierarchicalLink')):
      self.obj1815._setHierarchicalLink(False)

    self.obj1815.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(582.0,107.5,self.obj1815)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1815.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1815)
    self.globalAndLocalPostcondition(self.obj1815, rootNode)
    self.obj1815.postAction( rootNode.CREATE )

    self.obj1816=apply_contains(self)
    self.obj1816.isGraphObjectVisual = True

    if(hasattr(self.obj1816, '_setHierarchicalLink')):
      self.obj1816._setHierarchicalLink(False)

    self.obj1816.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,417.0,self.obj1816)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1816.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1816)
    self.globalAndLocalPostcondition(self.obj1816, rootNode)
    self.obj1816.postAction( rootNode.CREATE )

    self.obj1817=apply_contains(self)
    self.obj1817.isGraphObjectVisual = True

    if(hasattr(self.obj1817, '_setHierarchicalLink')):
      self.obj1817._setHierarchicalLink(False)

    self.obj1817.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(359.5,432.0,self.obj1817)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1817.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1817)
    self.globalAndLocalPostcondition(self.obj1817, rootNode)
    self.obj1817.postAction( rootNode.CREATE )

    self.obj1818=apply_contains(self)
    self.obj1818.isGraphObjectVisual = True

    if(hasattr(self.obj1818, '_setHierarchicalLink')):
      self.obj1818._setHierarchicalLink(False)

    self.obj1818.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(539.5,431.5,self.obj1818)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1818.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1818)
    self.globalAndLocalPostcondition(self.obj1818, rootNode)
    self.obj1818.postAction( rootNode.CREATE )

    self.obj1819=directLink_T(self)
    self.obj1819.isGraphObjectVisual = True

    if(hasattr(self.obj1819, '_setHierarchicalLink')):
      self.obj1819._setHierarchicalLink(False)

    # associationType
    self.obj1819.associationType.setValue('branches')

    self.obj1819.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(399.0,484.0,self.obj1819)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1819.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1819)
    self.globalAndLocalPostcondition(self.obj1819, rootNode)
    self.obj1819.postAction( rootNode.CREATE )

    self.obj1820=directLink_T(self)
    self.obj1820.isGraphObjectVisual = True

    if(hasattr(self.obj1820, '_setHierarchicalLink')):
      self.obj1820._setHierarchicalLink(False)

    # associationType
    self.obj1820.associationType.setValue('p')

    self.obj1820.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,490.0,self.obj1820)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1820.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1820)
    self.globalAndLocalPostcondition(self.obj1820, rootNode)
    self.obj1820.postAction( rootNode.CREATE )

    self.obj1821=directLink_S(self)
    self.obj1821.isGraphObjectVisual = True

    if(hasattr(self.obj1821, '_setHierarchicalLink')):
      self.obj1821._setHierarchicalLink(False)

    # associationType
    self.obj1821.associationType.setValue('outgoingTransitions')

    self.obj1821.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,123.0,self.obj1821)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1821.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1821)
    self.globalAndLocalPostcondition(self.obj1821, rootNode)
    self.obj1821.postAction( rootNode.CREATE )

    self.obj1822=directLink_S(self)
    self.obj1822.isGraphObjectVisual = True

    if(hasattr(self.obj1822, '_setHierarchicalLink')):
      self.obj1822._setHierarchicalLink(False)

    # associationType
    self.obj1822.associationType.setValue('triggers')

    self.obj1822.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(1024.5,181.0,self.obj1822)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1822.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1822)
    self.globalAndLocalPostcondition(self.obj1822, rootNode)
    self.obj1822.postAction( rootNode.CREATE )

    self.obj1823=directLink_S(self)
    self.obj1823.isGraphObjectVisual = True

    if(hasattr(self.obj1823, '_setHierarchicalLink')):
      self.obj1823._setHierarchicalLink(False)

    # associationType
    self.obj1823.associationType.setValue('signal')

    self.obj1823.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(848.0,187.0,self.obj1823)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1823.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1823)
    self.globalAndLocalPostcondition(self.obj1823, rootNode)
    self.obj1823.postAction( rootNode.CREATE )

    self.obj1824=backward_link(self)
    self.obj1824.isGraphObjectVisual = True

    if(hasattr(self.obj1824, '_setHierarchicalLink')):
      self.obj1824._setHierarchicalLink(False)

    # type
    self.obj1824.type.setValue('ruleDef')

    self.obj1824.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,287.0,self.obj1824)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1824.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1824)
    self.globalAndLocalPostcondition(self.obj1824, rootNode)
    self.obj1824.postAction( rootNode.CREATE )

    self.obj1825=backward_link(self)
    self.obj1825.isGraphObjectVisual = True

    if(hasattr(self.obj1825, '_setHierarchicalLink')):
      self.obj1825._setHierarchicalLink(False)

    # type
    self.obj1825.type.setValue('ruleDef')

    self.obj1825.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(968.0,305.5,self.obj1825)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1825.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1825)
    self.globalAndLocalPostcondition(self.obj1825, rootNode)
    self.obj1825.postAction( rootNode.CREATE )

    self.obj1826=hasAttribute_S(self)
    self.obj1826.isGraphObjectVisual = True

    if(hasattr(self.obj1826, '_setHierarchicalLink')):
      self.obj1826._setHierarchicalLink(False)

    self.obj1826.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,166.0,self.obj1826)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1826.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1826)
    self.globalAndLocalPostcondition(self.obj1826, rootNode)
    self.obj1826.postAction( rootNode.CREATE )

    self.obj1827=hasAttribute_S(self)
    self.obj1827.isGraphObjectVisual = True

    if(hasattr(self.obj1827, '_setHierarchicalLink')):
      self.obj1827._setHierarchicalLink(False)

    self.obj1827.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(402.0,158.5,self.obj1827)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1827.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1827)
    self.globalAndLocalPostcondition(self.obj1827, rootNode)
    self.obj1827.postAction( rootNode.CREATE )

    self.obj1828=hasAttribute_S(self)
    self.obj1828.isGraphObjectVisual = True

    if(hasattr(self.obj1828, '_setHierarchicalLink')):
      self.obj1828._setHierarchicalLink(False)

    self.obj1828.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(815.5,228.5,self.obj1828)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1828.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1828)
    self.globalAndLocalPostcondition(self.obj1828, rootNode)
    self.obj1828.postAction( rootNode.CREATE )

    self.obj1829=hasAttribute_T(self)
    self.obj1829.isGraphObjectVisual = True

    if(hasattr(self.obj1829, '_setHierarchicalLink')):
      self.obj1829._setHierarchicalLink(False)

    self.obj1829.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(555.5,442.0,self.obj1829)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1829.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1829)
    self.globalAndLocalPostcondition(self.obj1829, rootNode)
    self.obj1829.postAction( rootNode.CREATE )

    self.obj1830=hasAttribute_T(self)
    self.obj1830.isGraphObjectVisual = True

    if(hasattr(self.obj1830, '_setHierarchicalLink')):
      self.obj1830._setHierarchicalLink(False)

    self.obj1830.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(283.0,531.5,self.obj1830)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1830.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1830)
    self.globalAndLocalPostcondition(self.obj1830, rootNode)
    self.obj1830.postAction( rootNode.CREATE )

    self.obj1831=hasAttribute_T(self)
    self.obj1831.isGraphObjectVisual = True

    if(hasattr(self.obj1831, '_setHierarchicalLink')):
      self.obj1831._setHierarchicalLink(False)

    self.obj1831.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(893.0,531.0,self.obj1831)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1831.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1831)
    self.globalAndLocalPostcondition(self.obj1831, rootNode)
    self.obj1831.postAction( rootNode.CREATE )

    self.obj1832=leftExpr(self)
    self.obj1832.isGraphObjectVisual = True

    if(hasattr(self.obj1832, '_setHierarchicalLink')):
      self.obj1832._setHierarchicalLink(False)

    self.obj1832.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(367.5,245.0,self.obj1832)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1832.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1832)
    self.globalAndLocalPostcondition(self.obj1832, rootNode)
    self.obj1832.postAction( rootNode.CREATE )

    self.obj1833=leftExpr(self)
    self.obj1833.isGraphObjectVisual = True

    if(hasattr(self.obj1833, '_setHierarchicalLink')):
      self.obj1833._setHierarchicalLink(False)

    self.obj1833.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(556.0,236.5,self.obj1833)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1833.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1833)
    self.globalAndLocalPostcondition(self.obj1833, rootNode)
    self.obj1833.postAction( rootNode.CREATE )

    self.obj1834=leftExpr(self)
    self.obj1834.isGraphObjectVisual = True

    if(hasattr(self.obj1834, '_setHierarchicalLink')):
      self.obj1834._setHierarchicalLink(False)

    self.obj1834.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(622.0,397.5,self.obj1834)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1834.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1834)
    self.globalAndLocalPostcondition(self.obj1834, rootNode)
    self.obj1834.postAction( rootNode.CREATE )

    self.obj1835=leftExpr(self)
    self.obj1835.isGraphObjectVisual = True

    if(hasattr(self.obj1835, '_setHierarchicalLink')):
      self.obj1835._setHierarchicalLink(False)

    self.obj1835.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(276.0,616.5,self.obj1835)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1835.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1835)
    self.globalAndLocalPostcondition(self.obj1835, rootNode)
    self.obj1835.postAction( rootNode.CREATE )

    self.obj1836=leftExpr(self)
    self.obj1836.isGraphObjectVisual = True

    if(hasattr(self.obj1836, '_setHierarchicalLink')):
      self.obj1836._setHierarchicalLink(False)

    self.obj1836.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,616.5,self.obj1836)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1836.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1836)
    self.globalAndLocalPostcondition(self.obj1836, rootNode)
    self.obj1836.postAction( rootNode.CREATE )

    self.obj1837=rightExpr(self)
    self.obj1837.isGraphObjectVisual = True

    if(hasattr(self.obj1837, '_setHierarchicalLink')):
      self.obj1837._setHierarchicalLink(False)

    self.obj1837.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(367.5,287.5,self.obj1837)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1837.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1837)
    self.globalAndLocalPostcondition(self.obj1837, rootNode)
    self.obj1837.postAction( rootNode.CREATE )

    self.obj1838=rightExpr(self)
    self.obj1838.isGraphObjectVisual = True

    if(hasattr(self.obj1838, '_setHierarchicalLink')):
      self.obj1838._setHierarchicalLink(False)

    self.obj1838.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(636.0,236.5,self.obj1838)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1838.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1838)
    self.globalAndLocalPostcondition(self.obj1838, rootNode)
    self.obj1838.postAction( rootNode.CREATE )

    self.obj1839=rightExpr(self)
    self.obj1839.isGraphObjectVisual = True

    if(hasattr(self.obj1839, '_setHierarchicalLink')):
      self.obj1839._setHierarchicalLink(False)

    self.obj1839.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(759.5,337.0,self.obj1839)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1839.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1839)
    self.globalAndLocalPostcondition(self.obj1839, rootNode)
    self.obj1839.postAction( rootNode.CREATE )

    self.obj1840=rightExpr(self)
    self.obj1840.isGraphObjectVisual = True

    if(hasattr(self.obj1840, '_setHierarchicalLink')):
      self.obj1840._setHierarchicalLink(False)

    self.obj1840.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(356.0,616.5,self.obj1840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1840)
    self.globalAndLocalPostcondition(self.obj1840, rootNode)
    self.obj1840.postAction( rootNode.CREATE )

    self.obj1841=rightExpr(self)
    self.obj1841.isGraphObjectVisual = True

    if(hasattr(self.obj1841, '_setHierarchicalLink')):
      self.obj1841._setHierarchicalLink(False)

    self.obj1841.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,616.5,self.obj1841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1841)
    self.globalAndLocalPostcondition(self.obj1841, rootNode)
    self.obj1841.postAction( rootNode.CREATE )

    # Connections for obj1787 (graphObject_: Obj980) of type MatchModel
    self.drawConnections(
(self.obj1787,self.obj1811,[138.0, 52.0, 142.5, 213.5],"true", 2),
(self.obj1787,self.obj1812,[138.0, 52.0, 234.0, 87.5],"true", 2),
(self.obj1787,self.obj1813,[138.0, 52.0, 571.0, 87.5],"true", 2),
(self.obj1787,self.obj1814,[138.0, 52.0, 477.5, 117.5],"true", 2),
(self.obj1787,self.obj1815,[138.0, 52.0, 582.0, 107.5],"true", 2) )
    # Connections for obj1788 (graphObject_: Obj981) of type ApplyModel
    self.drawConnections(
(self.obj1788,self.obj1816,[147.0, 375.0, 219.5, 417.0],"true", 2),
(self.obj1788,self.obj1817,[147.0, 375.0, 359.5, 432.0],"true", 2),
(self.obj1788,self.obj1818,[147.0, 375.0, 539.5, 431.5],"true", 2) )
    # Connections for obj1789 (graphObject_: Obj982) named triggerS1
    self.drawConnections(
(self.obj1789,self.obj1823,[1030.0, 223.0, 848.0, 187.0],"true", 2) )
    # Connections for obj1790 (graphObject_: Obj983) named signal1
    self.drawConnections(
(self.obj1790,self.obj1828,[817.0, 183.0, 815.5, 228.5],"true", 2) )
    # Connections for obj1791 (graphObject_: Obj984) named transition1
    self.drawConnections(
(self.obj1791,self.obj1822,[1004.0, 123.0, 1024.5, 181.0],"true", 2) )
    # Connections for obj1792 (graphObject_: Obj985) named state1
    self.drawConnections(
(self.obj1792,self.obj1821,[330.0, 123.0, 480.0, 123.0],"true", 2),
(self.obj1792,self.obj1826,[330.0, 123.0, 312.0, 166.0],"true", 2),
(self.obj1792,self.obj1827,[330.0, 123.0, 402.0, 158.5],"true", 2) )
    # Connections for obj1793 (graphObject_: Obj986) named listen1
    self.drawConnections(
(self.obj1793,self.obj1824,[352.0, 489.0, 341.0, 287.0],"true", 2),
(self.obj1793,self.obj1819,[352.0, 489.0, 399.0, 484.0],"true", 2),
(self.obj1793,self.obj1830,[352.0, 489.0, 283.0, 531.5],"true", 2) )
    # Connections for obj1794 (graphObject_: Obj987) named listenBranch1
    self.drawConnections(
(self.obj1794,self.obj1829,[572.0, 491.0, 555.5, 442.0],"true", 2),
(self.obj1794,self.obj1820,[572.0, 491.0, 752.0, 490.0],"true", 2) )
    # Connections for obj1795 (graphObject_: Obj988) named inst1
    self.drawConnections(
(self.obj1795,self.obj1825,[932.0, 488.0, 968.0, 305.5],"true", 2),
(self.obj1795,self.obj1831,[932.0, 488.0, 893.0, 531.0],"true", 2) )
    # Connections for obj1796 (graphObject_: Obj989) named isComposite
    self.drawConnections(
 )
    # Connections for obj1797 (graphObject_: Obj990) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj1798 (graphObject_: Obj991) named name
    self.drawConnections(
 )
    # Connections for obj1799 (graphObject_: Obj992) named channel
    self.drawConnections(
 )
    # Connections for obj1800 (graphObject_: Obj993) named pivotin
    self.drawConnections(
 )
    # Connections for obj1801 (graphObject_: Obj994) named pivotin
    self.drawConnections(
 )
    # Connections for obj1802 (graphObject_: Obj995) named eq1
    self.drawConnections(
(self.obj1802,self.obj1832,[441.0, 281.0, 367.5, 245.0],"true", 2),
(self.obj1802,self.obj1837,[441.0, 281.0, 367.5, 287.5],"true", 2) )
    # Connections for obj1803 (graphObject_: Obj996) named eq2
    self.drawConnections(
(self.obj1803,self.obj1838,[638.0, 279.0, 636.0, 236.5],"true", 2),
(self.obj1803,self.obj1833,[638.0, 279.0, 556.0, 236.5],"true", 2) )
    # Connections for obj1804 (graphObject_: Obj997) named eq3
    self.drawConnections(
(self.obj1804,self.obj1839,[705.0, 400.0, 759.5, 337.0],"true", 2),
(self.obj1804,self.obj1834,[705.0, 400.0, 622.0, 397.5],"true", 2) )
    # Connections for obj1805 (graphObject_: Obj998) named eq4
    self.drawConnections(
(self.obj1805,self.obj1835,[338.0, 659.0, 276.0, 616.5],"true", 2),
(self.obj1805,self.obj1840,[338.0, 659.0, 356.0, 616.5],"true", 2) )
    # Connections for obj1806 (graphObject_: Obj999) named eq5
    self.drawConnections(
(self.obj1806,self.obj1836,[938.0, 659.0, 896.0, 616.5],"true", 2),
(self.obj1806,self.obj1841,[938.0, 659.0, 996.0, 616.5],"true", 2) )
    # Connections for obj1807 (graphObject_: Obj1000) named false
    self.drawConnections(
 )
    # Connections for obj1808 (graphObject_: Obj1001) named true
    self.drawConnections(
 )
    # Connections for obj1809 (graphObject_: Obj1002) named listensimplestate
    self.drawConnections(
 )
    # Connections for obj1810 (graphObject_: Obj1003) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1811 (graphObject_: Obj1004) of type paired_with
    self.drawConnections(
(self.obj1811,self.obj1788,[142.5, 213.5, 147.0, 375.0],"true", 2) )
    # Connections for obj1812 (graphObject_: Obj1005) of type match_contains
    self.drawConnections(
(self.obj1812,self.obj1792,[234.0, 87.5, 330.0, 123.0],"true", 2) )
    # Connections for obj1813 (graphObject_: Obj1006) of type match_contains
    self.drawConnections(
(self.obj1813,self.obj1791,[571.0, 87.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj1814 (graphObject_: Obj1007) of type match_contains
    self.drawConnections(
(self.obj1814,self.obj1790,[477.5, 117.5, 817.0, 183.0],"true", 2) )
    # Connections for obj1815 (graphObject_: Obj1008) of type match_contains
    self.drawConnections(
(self.obj1815,self.obj1789,[582.0, 107.5, 1030.0, 223.0],"true", 2) )
    # Connections for obj1816 (graphObject_: Obj1009) of type apply_contains
    self.drawConnections(
(self.obj1816,self.obj1793,[219.5, 417.0, 352.0, 489.0],"true", 2) )
    # Connections for obj1817 (graphObject_: Obj1010) of type apply_contains
    self.drawConnections(
(self.obj1817,self.obj1794,[359.5, 432.0, 572.0, 491.0],"true", 2) )
    # Connections for obj1818 (graphObject_: Obj1011) of type apply_contains
    self.drawConnections(
(self.obj1818,self.obj1795,[539.5, 431.5, 932.0, 488.0],"true", 2) )
    # Connections for obj1819 (graphObject_: Obj1012) of type directLink_T
    self.drawConnections(
(self.obj1819,self.obj1794,[399.0, 484.0, 572.0, 491.0],"true", 2) )
    # Connections for obj1820 (graphObject_: Obj1013) of type directLink_T
    self.drawConnections(
(self.obj1820,self.obj1795,[752.0, 490.0, 932.0, 488.0],"true", 2) )
    # Connections for obj1821 (graphObject_: Obj1014) of type directLink_S
    self.drawConnections(
(self.obj1821,self.obj1791,[480.0, 123.0, 1004.0, 123.0],"true", 2) )
    # Connections for obj1822 (graphObject_: Obj1015) of type directLink_S
    self.drawConnections(
(self.obj1822,self.obj1789,[984.5, 193.0, 1030.0, 223.0],"true", 2) )
    # Connections for obj1823 (graphObject_: Obj1016) of type directLink_S
    self.drawConnections(
(self.obj1823,self.obj1790,[848.0, 187.0, 817.0, 183.0],"true", 2) )
    # Connections for obj1824 (graphObject_: Obj1017) of type backward_link
    self.drawConnections(
(self.obj1824,self.obj1792,[341.0, 287.0, 330.0, 123.0],"true", 2) )
    # Connections for obj1825 (graphObject_: Obj1018) of type backward_link
    self.drawConnections(
(self.obj1825,self.obj1791,[968.0, 305.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj1826 (graphObject_: Obj1019) of type hasAttribute_S
    self.drawConnections(
(self.obj1826,self.obj1796,[312.0, 166.0, 294.0, 209.0],"true", 2) )
    # Connections for obj1827 (graphObject_: Obj1020) of type hasAttribute_S
    self.drawConnections(
(self.obj1827,self.obj1797,[402.0, 158.5, 474.0, 194.0],"true", 2) )
    # Connections for obj1828 (graphObject_: Obj1021) of type hasAttribute_S
    self.drawConnections(
(self.obj1828,self.obj1798,[815.5, 228.5, 814.0, 274.0],"true", 2) )
    # Connections for obj1829 (graphObject_: Obj1022) of type hasAttribute_T
    self.drawConnections(
(self.obj1829,self.obj1799,[555.5, 442.0, 539.0, 395.0],"true", 2) )
    # Connections for obj1830 (graphObject_: Obj1023) of type hasAttribute_T
    self.drawConnections(
(self.obj1830,self.obj1800,[283.0, 531.5, 214.0, 574.0],"true", 2) )
    # Connections for obj1831 (graphObject_: Obj1024) of type hasAttribute_T
    self.drawConnections(
(self.obj1831,self.obj1801,[893.0, 531.0, 854.0, 574.0],"true", 2) )
    # Connections for obj1832 (graphObject_: Obj1025) of type leftExpr
    self.drawConnections(
(self.obj1832,self.obj1796,[367.5, 245.0, 294.0, 209.0],"true", 2) )
    # Connections for obj1833 (graphObject_: Obj1026) of type leftExpr
    self.drawConnections(
(self.obj1833,self.obj1797,[556.0, 236.5, 474.0, 194.0],"true", 2) )
    # Connections for obj1834 (graphObject_: Obj1027) of type leftExpr
    self.drawConnections(
(self.obj1834,self.obj1799,[622.0, 397.5, 539.0, 395.0],"true", 2) )
    # Connections for obj1835 (graphObject_: Obj1028) of type leftExpr
    self.drawConnections(
(self.obj1835,self.obj1800,[276.0, 616.5, 214.0, 574.0],"true", 2) )
    # Connections for obj1836 (graphObject_: Obj1029) of type leftExpr
    self.drawConnections(
(self.obj1836,self.obj1801,[896.0, 616.5, 854.0, 574.0],"true", 2) )
    # Connections for obj1837 (graphObject_: Obj1030) of type rightExpr
    self.drawConnections(
(self.obj1837,self.obj1807,[367.5, 287.5, 294.0, 294.0],"true", 2) )
    # Connections for obj1838 (graphObject_: Obj1031) of type rightExpr
    self.drawConnections(
(self.obj1838,self.obj1808,[636.0, 236.5, 634.0, 194.0],"true", 2) )
    # Connections for obj1839 (graphObject_: Obj1032) of type rightExpr
    self.drawConnections(
(self.obj1839,self.obj1798,[759.5, 337.0, 814.0, 274.0],"true", 2) )
    # Connections for obj1840 (graphObject_: Obj1033) of type rightExpr
    self.drawConnections(
(self.obj1840,self.obj1809,[356.0, 616.5, 374.0, 574.0],"true", 2) )
    # Connections for obj1841 (graphObject_: Obj1034) of type rightExpr
    self.drawConnections(
(self.obj1841,self.obj1810,[996.0, 616.5, 1054.0, 574.0],"true", 2) )

newfunction = Transition2ListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
