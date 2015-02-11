"""
__Transition2ListenBranch_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 15:10:47 2015
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


    self.obj997=MatchModel(self)
    self.obj997.isGraphObjectVisual = True

    if(hasattr(self.obj997, '_setHierarchicalLink')):
      self.obj997._setHierarchicalLink(False)

    self.obj997.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,21.0,self.obj997)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj997.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj997)
    self.globalAndLocalPostcondition(self.obj997, rootNode)
    self.obj997.postAction( rootNode.CREATE )

    self.obj998=ApplyModel(self)
    self.obj998.isGraphObjectVisual = True

    if(hasattr(self.obj998, '_setHierarchicalLink')):
      self.obj998._setHierarchicalLink(False)

    self.obj998.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(24.0,342.0,self.obj998)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj998.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj998)
    self.globalAndLocalPostcondition(self.obj998, rootNode)
    self.obj998.postAction( rootNode.CREATE )

    self.obj999=Trigger_S(self)
    self.obj999.isGraphObjectVisual = True

    if(hasattr(self.obj999, '_setHierarchicalLink')):
      self.obj999._setHierarchicalLink(False)

    # classtype
    self.obj999.classtype.setValue('Trigger_S')

    # cardinality
    self.obj999.cardinality.setValue('1')

    # name
    self.obj999.name.setValue('triggerS1')

    self.obj999.graphClass_= graph_Trigger_S
    if self.genGraphics:
       new_obj = graph_Trigger_S(860.0,180.0,self.obj999)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj999.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj999)
    self.globalAndLocalPostcondition(self.obj999, rootNode)
    self.obj999.postAction( rootNode.CREATE )

    self.obj1000=Signal(self)
    self.obj1000.isGraphObjectVisual = True

    if(hasattr(self.obj1000, '_setHierarchicalLink')):
      self.obj1000._setHierarchicalLink(False)

    # name
    self.obj1000.name.setValue('signal1')

    # classtype
    self.obj1000.classtype.setValue('Signal')

    # cardinality
    self.obj1000.cardinality.setValue('1')

    self.obj1000.graphClass_= graph_Signal
    if self.genGraphics:
       new_obj = graph_Signal(647.0,140.0,self.obj1000)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1000.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1000)
    self.globalAndLocalPostcondition(self.obj1000, rootNode)
    self.obj1000.postAction( rootNode.CREATE )

    self.obj1001=Transition(self)
    self.obj1001.isGraphObjectVisual = True

    if(hasattr(self.obj1001, '_setHierarchicalLink')):
      self.obj1001._setHierarchicalLink(False)

    # name
    self.obj1001.name.setValue('transition1')

    # classtype
    self.obj1001.classtype.setValue('Transition')

    # cardinality
    self.obj1001.cardinality.setValue('+')

    self.obj1001.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(834.0,80.0,self.obj1001)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1001.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1001)
    self.globalAndLocalPostcondition(self.obj1001, rootNode)
    self.obj1001.postAction( rootNode.CREATE )

    self.obj1002=State(self)
    self.obj1002.isGraphObjectVisual = True

    if(hasattr(self.obj1002, '_setHierarchicalLink')):
      self.obj1002._setHierarchicalLink(False)

    # name
    self.obj1002.name.setValue('state1')

    # classtype
    self.obj1002.classtype.setValue('State')

    # cardinality
    self.obj1002.cardinality.setValue('+')

    self.obj1002.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(160.0,80.0,self.obj1002)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1002.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1002)
    self.globalAndLocalPostcondition(self.obj1002, rootNode)
    self.obj1002.postAction( rootNode.CREATE )

    self.obj1003=Listen(self)
    self.obj1003.isGraphObjectVisual = True

    if(hasattr(self.obj1003, '_setHierarchicalLink')):
      self.obj1003._setHierarchicalLink(False)

    # classtype
    self.obj1003.classtype.setValue('Listen')

    # cardinality
    self.obj1003.cardinality.setValue('1')

    # name
    self.obj1003.name.setValue('listen1')

    self.obj1003.graphClass_= graph_Listen
    if self.genGraphics:
       new_obj = graph_Listen(180.0,438.0,self.obj1003)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Listen", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1003.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1003)
    self.globalAndLocalPostcondition(self.obj1003, rootNode)
    self.obj1003.postAction( rootNode.CREATE )

    self.obj1004=ListenBranch(self)
    self.obj1004.isGraphObjectVisual = True

    if(hasattr(self.obj1004, '_setHierarchicalLink')):
      self.obj1004._setHierarchicalLink(False)

    # classtype
    self.obj1004.classtype.setValue('ListenBranch')

    # cardinality
    self.obj1004.cardinality.setValue('1')

    # name
    self.obj1004.name.setValue('listenBranch1')

    self.obj1004.graphClass_= graph_ListenBranch
    if self.genGraphics:
       new_obj = graph_ListenBranch(400.0,440.0,self.obj1004)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1004.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1004)
    self.globalAndLocalPostcondition(self.obj1004, rootNode)
    self.obj1004.postAction( rootNode.CREATE )

    self.obj1005=Inst(self)
    self.obj1005.isGraphObjectVisual = True

    if(hasattr(self.obj1005, '_setHierarchicalLink')):
      self.obj1005._setHierarchicalLink(False)

    # classtype
    self.obj1005.classtype.setValue('Inst')

    # cardinality
    self.obj1005.cardinality.setValue('1')

    # name
    self.obj1005.name.setValue('inst1')

    self.obj1005.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(760.0,437.0,self.obj1005)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1005.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1005)
    self.globalAndLocalPostcondition(self.obj1005, rootNode)
    self.obj1005.postAction( rootNode.CREATE )

    self.obj1006=Attribute(self)
    self.obj1006.isGraphObjectVisual = True

    if(hasattr(self.obj1006, '_setHierarchicalLink')):
      self.obj1006._setHierarchicalLink(False)

    # Type
    self.obj1006.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1006.Type.config = 0

    # name
    self.obj1006.name.setValue('isComposite')

    self.obj1006.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,175.0,self.obj1006)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1006.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1006)
    self.globalAndLocalPostcondition(self.obj1006, rootNode)
    self.obj1006.postAction( rootNode.CREATE )

    self.obj1007=Attribute(self)
    self.obj1007.isGraphObjectVisual = True

    if(hasattr(self.obj1007, '_setHierarchicalLink')):
      self.obj1007._setHierarchicalLink(False)

    # Type
    self.obj1007.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1007.Type.config = 0

    # name
    self.obj1007.name.setValue('hasOutgoingTransitions')

    self.obj1007.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(340.0,160.0,self.obj1007)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1007.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1007)
    self.globalAndLocalPostcondition(self.obj1007, rootNode)
    self.obj1007.postAction( rootNode.CREATE )

    self.obj1008=Attribute(self)
    self.obj1008.isGraphObjectVisual = True

    if(hasattr(self.obj1008, '_setHierarchicalLink')):
      self.obj1008._setHierarchicalLink(False)

    # Type
    self.obj1008.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1008.Type.config = 0

    # name
    self.obj1008.name.setValue('name')

    self.obj1008.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,240.0,self.obj1008)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1008.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1008)
    self.globalAndLocalPostcondition(self.obj1008, rootNode)
    self.obj1008.postAction( rootNode.CREATE )

    self.obj1009=Attribute(self)
    self.obj1009.isGraphObjectVisual = True

    if(hasattr(self.obj1009, '_setHierarchicalLink')):
      self.obj1009._setHierarchicalLink(False)

    # Type
    self.obj1009.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1009.Type.config = 0

    # name
    self.obj1009.name.setValue('channel')

    self.obj1009.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(405.0,361.0,self.obj1009)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1009.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1009)
    self.globalAndLocalPostcondition(self.obj1009, rootNode)
    self.obj1009.postAction( rootNode.CREATE )

    self.obj1010=Attribute(self)
    self.obj1010.isGraphObjectVisual = True

    if(hasattr(self.obj1010, '_setHierarchicalLink')):
      self.obj1010._setHierarchicalLink(False)

    # Type
    self.obj1010.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1010.Type.config = 0

    # name
    self.obj1010.name.setValue('pivot')

    self.obj1010.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(80.0,540.0,self.obj1010)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1010.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1010)
    self.globalAndLocalPostcondition(self.obj1010, rootNode)
    self.obj1010.postAction( rootNode.CREATE )

    self.obj1011=Attribute(self)
    self.obj1011.isGraphObjectVisual = True

    if(hasattr(self.obj1011, '_setHierarchicalLink')):
      self.obj1011._setHierarchicalLink(False)

    # Type
    self.obj1011.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1011.Type.config = 0

    # name
    self.obj1011.name.setValue('pivot')

    self.obj1011.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(720.0,540.0,self.obj1011)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1011.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1011)
    self.globalAndLocalPostcondition(self.obj1011, rootNode)
    self.obj1011.postAction( rootNode.CREATE )

    self.obj1012=Equation(self)
    self.obj1012.isGraphObjectVisual = True

    if(hasattr(self.obj1012, '_setHierarchicalLink')):
      self.obj1012._setHierarchicalLink(False)

    # name
    self.obj1012.name.setValue('eq1')

    self.obj1012.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(303.0,242.0,self.obj1012)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1012.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1012)
    self.globalAndLocalPostcondition(self.obj1012, rootNode)
    self.obj1012.postAction( rootNode.CREATE )

    self.obj1013=Equation(self)
    self.obj1013.isGraphObjectVisual = True

    if(hasattr(self.obj1013, '_setHierarchicalLink')):
      self.obj1013._setHierarchicalLink(False)

    # name
    self.obj1013.name.setValue('eq2')

    self.obj1013.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,240.0,self.obj1013)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1013.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1013)
    self.globalAndLocalPostcondition(self.obj1013, rootNode)
    self.obj1013.postAction( rootNode.CREATE )

    self.obj1014=Equation(self)
    self.obj1014.isGraphObjectVisual = True

    if(hasattr(self.obj1014, '_setHierarchicalLink')):
      self.obj1014._setHierarchicalLink(False)

    # name
    self.obj1014.name.setValue('eq3')

    self.obj1014.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(567.0,361.0,self.obj1014)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1014.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1014)
    self.globalAndLocalPostcondition(self.obj1014, rootNode)
    self.obj1014.postAction( rootNode.CREATE )

    self.obj1015=Equation(self)
    self.obj1015.isGraphObjectVisual = True

    if(hasattr(self.obj1015, '_setHierarchicalLink')):
      self.obj1015._setHierarchicalLink(False)

    # name
    self.obj1015.name.setValue('eq4')

    self.obj1015.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(200.0,620.0,self.obj1015)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1015.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1015)
    self.globalAndLocalPostcondition(self.obj1015, rootNode)
    self.obj1015.postAction( rootNode.CREATE )

    self.obj1016=Equation(self)
    self.obj1016.isGraphObjectVisual = True

    if(hasattr(self.obj1016, '_setHierarchicalLink')):
      self.obj1016._setHierarchicalLink(False)

    # name
    self.obj1016.name.setValue('eq5')

    self.obj1016.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(800.0,620.0,self.obj1016)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1016.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1016)
    self.globalAndLocalPostcondition(self.obj1016, rootNode)
    self.obj1016.postAction( rootNode.CREATE )

    self.obj1017=Constant(self)
    self.obj1017.isGraphObjectVisual = True

    if(hasattr(self.obj1017, '_setHierarchicalLink')):
      self.obj1017._setHierarchicalLink(False)

    # Type
    self.obj1017.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1017.Type.config = 0

    # name
    self.obj1017.name.setValue('false')

    self.obj1017.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(160.0,260.0,self.obj1017)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1017.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1017)
    self.globalAndLocalPostcondition(self.obj1017, rootNode)
    self.obj1017.postAction( rootNode.CREATE )

    self.obj1018=Constant(self)
    self.obj1018.isGraphObjectVisual = True

    if(hasattr(self.obj1018, '_setHierarchicalLink')):
      self.obj1018._setHierarchicalLink(False)

    # Type
    self.obj1018.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1018.Type.config = 0

    # name
    self.obj1018.name.setValue('true')

    self.obj1018.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(500.0,160.0,self.obj1018)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1018.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1018)
    self.globalAndLocalPostcondition(self.obj1018, rootNode)
    self.obj1018.postAction( rootNode.CREATE )

    self.obj1019=Constant(self)
    self.obj1019.isGraphObjectVisual = True

    if(hasattr(self.obj1019, '_setHierarchicalLink')):
      self.obj1019._setHierarchicalLink(False)

    # Type
    self.obj1019.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1019.Type.config = 0

    # name
    self.obj1019.name.setValue('listensimplestate')

    self.obj1019.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,540.0,self.obj1019)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1019.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1019)
    self.globalAndLocalPostcondition(self.obj1019, rootNode)
    self.obj1019.postAction( rootNode.CREATE )

    self.obj1020=Constant(self)
    self.obj1020.isGraphObjectVisual = True

    if(hasattr(self.obj1020, '_setHierarchicalLink')):
      self.obj1020._setHierarchicalLink(False)

    # Type
    self.obj1020.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1020.Type.config = 0

    # name
    self.obj1020.name.setValue('instfortrans')

    self.obj1020.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(920.0,540.0,self.obj1020)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1020.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1020)
    self.globalAndLocalPostcondition(self.obj1020, rootNode)
    self.obj1020.postAction( rootNode.CREATE )

    self.obj1021=paired_with(self)
    self.obj1021.isGraphObjectVisual = True

    if(hasattr(self.obj1021, '_setHierarchicalLink')):
      self.obj1021._setHierarchicalLink(False)

    self.obj1021.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(142.5,213.5,self.obj1021)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1021.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1021)
    self.globalAndLocalPostcondition(self.obj1021, rootNode)
    self.obj1021.postAction( rootNode.CREATE )

    self.obj1022=match_contains(self)
    self.obj1022.isGraphObjectVisual = True

    if(hasattr(self.obj1022, '_setHierarchicalLink')):
      self.obj1022._setHierarchicalLink(False)

    self.obj1022.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,87.5,self.obj1022)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1022.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1022)
    self.globalAndLocalPostcondition(self.obj1022, rootNode)
    self.obj1022.postAction( rootNode.CREATE )

    self.obj1023=match_contains(self)
    self.obj1023.isGraphObjectVisual = True

    if(hasattr(self.obj1023, '_setHierarchicalLink')):
      self.obj1023._setHierarchicalLink(False)

    self.obj1023.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(571.0,87.5,self.obj1023)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1023.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1023)
    self.globalAndLocalPostcondition(self.obj1023, rootNode)
    self.obj1023.postAction( rootNode.CREATE )

    self.obj1024=match_contains(self)
    self.obj1024.isGraphObjectVisual = True

    if(hasattr(self.obj1024, '_setHierarchicalLink')):
      self.obj1024._setHierarchicalLink(False)

    self.obj1024.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(477.5,117.5,self.obj1024)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1024.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1024)
    self.globalAndLocalPostcondition(self.obj1024, rootNode)
    self.obj1024.postAction( rootNode.CREATE )

    self.obj1025=match_contains(self)
    self.obj1025.isGraphObjectVisual = True

    if(hasattr(self.obj1025, '_setHierarchicalLink')):
      self.obj1025._setHierarchicalLink(False)

    self.obj1025.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(582.0,107.5,self.obj1025)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1025.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1025)
    self.globalAndLocalPostcondition(self.obj1025, rootNode)
    self.obj1025.postAction( rootNode.CREATE )

    self.obj1026=apply_contains(self)
    self.obj1026.isGraphObjectVisual = True

    if(hasattr(self.obj1026, '_setHierarchicalLink')):
      self.obj1026._setHierarchicalLink(False)

    self.obj1026.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,417.0,self.obj1026)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1026.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1026)
    self.globalAndLocalPostcondition(self.obj1026, rootNode)
    self.obj1026.postAction( rootNode.CREATE )

    self.obj1027=apply_contains(self)
    self.obj1027.isGraphObjectVisual = True

    if(hasattr(self.obj1027, '_setHierarchicalLink')):
      self.obj1027._setHierarchicalLink(False)

    self.obj1027.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(359.5,432.0,self.obj1027)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1027.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1027)
    self.globalAndLocalPostcondition(self.obj1027, rootNode)
    self.obj1027.postAction( rootNode.CREATE )

    self.obj1028=apply_contains(self)
    self.obj1028.isGraphObjectVisual = True

    if(hasattr(self.obj1028, '_setHierarchicalLink')):
      self.obj1028._setHierarchicalLink(False)

    self.obj1028.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(539.5,431.5,self.obj1028)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1028.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1028)
    self.globalAndLocalPostcondition(self.obj1028, rootNode)
    self.obj1028.postAction( rootNode.CREATE )

    self.obj1029=directLink_T(self)
    self.obj1029.isGraphObjectVisual = True

    if(hasattr(self.obj1029, '_setHierarchicalLink')):
      self.obj1029._setHierarchicalLink(False)

    # associationType
    self.obj1029.associationType.setValue('branches')

    self.obj1029.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(399.0,484.0,self.obj1029)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1029.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1029)
    self.globalAndLocalPostcondition(self.obj1029, rootNode)
    self.obj1029.postAction( rootNode.CREATE )

    self.obj1030=directLink_T(self)
    self.obj1030.isGraphObjectVisual = True

    if(hasattr(self.obj1030, '_setHierarchicalLink')):
      self.obj1030._setHierarchicalLink(False)

    # associationType
    self.obj1030.associationType.setValue('p')

    self.obj1030.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,490.0,self.obj1030)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1030.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1030)
    self.globalAndLocalPostcondition(self.obj1030, rootNode)
    self.obj1030.postAction( rootNode.CREATE )

    self.obj1031=directLink_S(self)
    self.obj1031.isGraphObjectVisual = True

    if(hasattr(self.obj1031, '_setHierarchicalLink')):
      self.obj1031._setHierarchicalLink(False)

    # associationType
    self.obj1031.associationType.setValue('outgoingTransitions')

    self.obj1031.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(480.0,123.0,self.obj1031)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1031.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1031)
    self.globalAndLocalPostcondition(self.obj1031, rootNode)
    self.obj1031.postAction( rootNode.CREATE )

    self.obj1032=directLink_S(self)
    self.obj1032.isGraphObjectVisual = True

    if(hasattr(self.obj1032, '_setHierarchicalLink')):
      self.obj1032._setHierarchicalLink(False)

    # associationType
    self.obj1032.associationType.setValue('triggers')

    self.obj1032.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(1024.5,181.0,self.obj1032)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1032.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1032)
    self.globalAndLocalPostcondition(self.obj1032, rootNode)
    self.obj1032.postAction( rootNode.CREATE )

    self.obj1033=directLink_S(self)
    self.obj1033.isGraphObjectVisual = True

    if(hasattr(self.obj1033, '_setHierarchicalLink')):
      self.obj1033._setHierarchicalLink(False)

    # associationType
    self.obj1033.associationType.setValue('signal')

    self.obj1033.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(848.0,187.0,self.obj1033)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1033.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1033)
    self.globalAndLocalPostcondition(self.obj1033, rootNode)
    self.obj1033.postAction( rootNode.CREATE )

    self.obj1034=backward_link(self)
    self.obj1034.isGraphObjectVisual = True

    if(hasattr(self.obj1034, '_setHierarchicalLink')):
      self.obj1034._setHierarchicalLink(False)

    # type
    self.obj1034.type.setValue('ruleDef')

    self.obj1034.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(341.0,287.0,self.obj1034)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1034.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1034)
    self.globalAndLocalPostcondition(self.obj1034, rootNode)
    self.obj1034.postAction( rootNode.CREATE )

    self.obj1035=backward_link(self)
    self.obj1035.isGraphObjectVisual = True

    if(hasattr(self.obj1035, '_setHierarchicalLink')):
      self.obj1035._setHierarchicalLink(False)

    # type
    self.obj1035.type.setValue('ruleDef')

    self.obj1035.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(968.0,305.5,self.obj1035)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1035.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1035)
    self.globalAndLocalPostcondition(self.obj1035, rootNode)
    self.obj1035.postAction( rootNode.CREATE )

    self.obj1036=hasAttribute_S(self)
    self.obj1036.isGraphObjectVisual = True

    if(hasattr(self.obj1036, '_setHierarchicalLink')):
      self.obj1036._setHierarchicalLink(False)

    self.obj1036.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(312.0,166.0,self.obj1036)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1036.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1036)
    self.globalAndLocalPostcondition(self.obj1036, rootNode)
    self.obj1036.postAction( rootNode.CREATE )

    self.obj1037=hasAttribute_S(self)
    self.obj1037.isGraphObjectVisual = True

    if(hasattr(self.obj1037, '_setHierarchicalLink')):
      self.obj1037._setHierarchicalLink(False)

    self.obj1037.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(402.0,158.5,self.obj1037)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1037.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1037)
    self.globalAndLocalPostcondition(self.obj1037, rootNode)
    self.obj1037.postAction( rootNode.CREATE )

    self.obj1038=hasAttribute_S(self)
    self.obj1038.isGraphObjectVisual = True

    if(hasattr(self.obj1038, '_setHierarchicalLink')):
      self.obj1038._setHierarchicalLink(False)

    self.obj1038.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(815.5,228.5,self.obj1038)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1038.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1038)
    self.globalAndLocalPostcondition(self.obj1038, rootNode)
    self.obj1038.postAction( rootNode.CREATE )

    self.obj1039=hasAttribute_T(self)
    self.obj1039.isGraphObjectVisual = True

    if(hasattr(self.obj1039, '_setHierarchicalLink')):
      self.obj1039._setHierarchicalLink(False)

    self.obj1039.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(555.5,442.0,self.obj1039)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1039.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1039)
    self.globalAndLocalPostcondition(self.obj1039, rootNode)
    self.obj1039.postAction( rootNode.CREATE )

    self.obj1040=hasAttribute_T(self)
    self.obj1040.isGraphObjectVisual = True

    if(hasattr(self.obj1040, '_setHierarchicalLink')):
      self.obj1040._setHierarchicalLink(False)

    self.obj1040.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(283.0,531.5,self.obj1040)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1040.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1040)
    self.globalAndLocalPostcondition(self.obj1040, rootNode)
    self.obj1040.postAction( rootNode.CREATE )

    self.obj1041=hasAttribute_T(self)
    self.obj1041.isGraphObjectVisual = True

    if(hasattr(self.obj1041, '_setHierarchicalLink')):
      self.obj1041._setHierarchicalLink(False)

    self.obj1041.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(893.0,531.0,self.obj1041)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1041.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1041)
    self.globalAndLocalPostcondition(self.obj1041, rootNode)
    self.obj1041.postAction( rootNode.CREATE )

    self.obj1042=leftExpr(self)
    self.obj1042.isGraphObjectVisual = True

    if(hasattr(self.obj1042, '_setHierarchicalLink')):
      self.obj1042._setHierarchicalLink(False)

    self.obj1042.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(367.5,245.0,self.obj1042)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1042.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1042)
    self.globalAndLocalPostcondition(self.obj1042, rootNode)
    self.obj1042.postAction( rootNode.CREATE )

    self.obj1043=leftExpr(self)
    self.obj1043.isGraphObjectVisual = True

    if(hasattr(self.obj1043, '_setHierarchicalLink')):
      self.obj1043._setHierarchicalLink(False)

    self.obj1043.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(556.0,236.5,self.obj1043)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1043.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1043)
    self.globalAndLocalPostcondition(self.obj1043, rootNode)
    self.obj1043.postAction( rootNode.CREATE )

    self.obj1044=leftExpr(self)
    self.obj1044.isGraphObjectVisual = True

    if(hasattr(self.obj1044, '_setHierarchicalLink')):
      self.obj1044._setHierarchicalLink(False)

    self.obj1044.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(622.0,397.5,self.obj1044)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1044.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1044)
    self.globalAndLocalPostcondition(self.obj1044, rootNode)
    self.obj1044.postAction( rootNode.CREATE )

    self.obj1045=leftExpr(self)
    self.obj1045.isGraphObjectVisual = True

    if(hasattr(self.obj1045, '_setHierarchicalLink')):
      self.obj1045._setHierarchicalLink(False)

    self.obj1045.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(276.0,616.5,self.obj1045)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1045.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1045)
    self.globalAndLocalPostcondition(self.obj1045, rootNode)
    self.obj1045.postAction( rootNode.CREATE )

    self.obj1046=leftExpr(self)
    self.obj1046.isGraphObjectVisual = True

    if(hasattr(self.obj1046, '_setHierarchicalLink')):
      self.obj1046._setHierarchicalLink(False)

    self.obj1046.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,616.5,self.obj1046)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1046.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1046)
    self.globalAndLocalPostcondition(self.obj1046, rootNode)
    self.obj1046.postAction( rootNode.CREATE )

    self.obj1047=rightExpr(self)
    self.obj1047.isGraphObjectVisual = True

    if(hasattr(self.obj1047, '_setHierarchicalLink')):
      self.obj1047._setHierarchicalLink(False)

    self.obj1047.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(367.5,287.5,self.obj1047)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1047.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1047)
    self.globalAndLocalPostcondition(self.obj1047, rootNode)
    self.obj1047.postAction( rootNode.CREATE )

    self.obj1048=rightExpr(self)
    self.obj1048.isGraphObjectVisual = True

    if(hasattr(self.obj1048, '_setHierarchicalLink')):
      self.obj1048._setHierarchicalLink(False)

    self.obj1048.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(636.0,236.5,self.obj1048)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1048.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1048)
    self.globalAndLocalPostcondition(self.obj1048, rootNode)
    self.obj1048.postAction( rootNode.CREATE )

    self.obj1049=rightExpr(self)
    self.obj1049.isGraphObjectVisual = True

    if(hasattr(self.obj1049, '_setHierarchicalLink')):
      self.obj1049._setHierarchicalLink(False)

    self.obj1049.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(759.5,337.0,self.obj1049)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1049.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1049)
    self.globalAndLocalPostcondition(self.obj1049, rootNode)
    self.obj1049.postAction( rootNode.CREATE )

    self.obj1050=rightExpr(self)
    self.obj1050.isGraphObjectVisual = True

    if(hasattr(self.obj1050, '_setHierarchicalLink')):
      self.obj1050._setHierarchicalLink(False)

    self.obj1050.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(356.0,616.5,self.obj1050)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1050.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1050)
    self.globalAndLocalPostcondition(self.obj1050, rootNode)
    self.obj1050.postAction( rootNode.CREATE )

    self.obj1051=rightExpr(self)
    self.obj1051.isGraphObjectVisual = True

    if(hasattr(self.obj1051, '_setHierarchicalLink')):
      self.obj1051._setHierarchicalLink(False)

    self.obj1051.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(996.0,616.5,self.obj1051)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1051.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1051)
    self.globalAndLocalPostcondition(self.obj1051, rootNode)
    self.obj1051.postAction( rootNode.CREATE )

    # Connections for obj997 (graphObject_: Obj894) of type MatchModel
    self.drawConnections(
(self.obj997,self.obj1021,[138.0, 52.0, 142.5, 213.5],"true", 2),
(self.obj997,self.obj1022,[138.0, 52.0, 234.0, 87.5],"true", 2),
(self.obj997,self.obj1023,[138.0, 52.0, 571.0, 87.5],"true", 2),
(self.obj997,self.obj1024,[138.0, 52.0, 477.5, 117.5],"true", 2),
(self.obj997,self.obj1025,[138.0, 52.0, 582.0, 107.5],"true", 2) )
    # Connections for obj998 (graphObject_: Obj895) of type ApplyModel
    self.drawConnections(
(self.obj998,self.obj1026,[147.0, 375.0, 219.5, 417.0],"true", 2),
(self.obj998,self.obj1027,[147.0, 375.0, 359.5, 432.0],"true", 2),
(self.obj998,self.obj1028,[147.0, 375.0, 539.5, 431.5],"true", 2) )
    # Connections for obj999 (graphObject_: Obj896) named triggerS1
    self.drawConnections(
(self.obj999,self.obj1033,[1030.0, 223.0, 848.0, 187.0],"true", 2) )
    # Connections for obj1000 (graphObject_: Obj897) named signal1
    self.drawConnections(
(self.obj1000,self.obj1038,[817.0, 183.0, 815.5, 228.5],"true", 2) )
    # Connections for obj1001 (graphObject_: Obj898) named transition1
    self.drawConnections(
(self.obj1001,self.obj1032,[1004.0, 123.0, 1024.5, 181.0],"true", 2) )
    # Connections for obj1002 (graphObject_: Obj899) named state1
    self.drawConnections(
(self.obj1002,self.obj1031,[330.0, 123.0, 480.0, 123.0],"true", 2),
(self.obj1002,self.obj1036,[330.0, 123.0, 312.0, 166.0],"true", 2),
(self.obj1002,self.obj1037,[330.0, 123.0, 402.0, 158.5],"true", 2) )
    # Connections for obj1003 (graphObject_: Obj900) named listen1
    self.drawConnections(
(self.obj1003,self.obj1034,[352.0, 489.0, 341.0, 287.0],"true", 2),
(self.obj1003,self.obj1029,[352.0, 489.0, 399.0, 484.0],"true", 2),
(self.obj1003,self.obj1040,[352.0, 489.0, 283.0, 531.5],"true", 2) )
    # Connections for obj1004 (graphObject_: Obj901) named listenBranch1
    self.drawConnections(
(self.obj1004,self.obj1039,[572.0, 491.0, 555.5, 442.0],"true", 2),
(self.obj1004,self.obj1030,[572.0, 491.0, 752.0, 490.0],"true", 2) )
    # Connections for obj1005 (graphObject_: Obj902) named inst1
    self.drawConnections(
(self.obj1005,self.obj1035,[932.0, 488.0, 968.0, 305.5],"true", 2),
(self.obj1005,self.obj1041,[932.0, 488.0, 893.0, 531.0],"true", 2) )
    # Connections for obj1006 (graphObject_: Obj903) named isComposite
    self.drawConnections(
 )
    # Connections for obj1007 (graphObject_: Obj904) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj1008 (graphObject_: Obj905) named name
    self.drawConnections(
 )
    # Connections for obj1009 (graphObject_: Obj906) named channel
    self.drawConnections(
 )
    # Connections for obj1010 (graphObject_: Obj907) named pivot
    self.drawConnections(
 )
    # Connections for obj1011 (graphObject_: Obj908) named pivot
    self.drawConnections(
 )
    # Connections for obj1012 (graphObject_: Obj909) named eq1
    self.drawConnections(
(self.obj1012,self.obj1042,[441.0, 281.0, 367.5, 245.0],"true", 2),
(self.obj1012,self.obj1047,[441.0, 281.0, 367.5, 287.5],"true", 2) )
    # Connections for obj1013 (graphObject_: Obj910) named eq2
    self.drawConnections(
(self.obj1013,self.obj1048,[638.0, 279.0, 636.0, 236.5],"true", 2),
(self.obj1013,self.obj1043,[638.0, 279.0, 556.0, 236.5],"true", 2) )
    # Connections for obj1014 (graphObject_: Obj911) named eq3
    self.drawConnections(
(self.obj1014,self.obj1049,[705.0, 400.0, 759.5, 337.0],"true", 2),
(self.obj1014,self.obj1044,[705.0, 400.0, 622.0, 397.5],"true", 2) )
    # Connections for obj1015 (graphObject_: Obj912) named eq4
    self.drawConnections(
(self.obj1015,self.obj1045,[338.0, 659.0, 276.0, 616.5],"true", 2),
(self.obj1015,self.obj1050,[338.0, 659.0, 356.0, 616.5],"true", 2) )
    # Connections for obj1016 (graphObject_: Obj913) named eq5
    self.drawConnections(
(self.obj1016,self.obj1046,[938.0, 659.0, 896.0, 616.5],"true", 2),
(self.obj1016,self.obj1051,[938.0, 659.0, 996.0, 616.5],"true", 2) )
    # Connections for obj1017 (graphObject_: Obj914) named false
    self.drawConnections(
 )
    # Connections for obj1018 (graphObject_: Obj915) named true
    self.drawConnections(
 )
    # Connections for obj1019 (graphObject_: Obj916) named listensimplestate
    self.drawConnections(
 )
    # Connections for obj1020 (graphObject_: Obj917) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1021 (graphObject_: Obj918) of type paired_with
    self.drawConnections(
(self.obj1021,self.obj998,[142.5, 213.5, 147.0, 375.0],"true", 2) )
    # Connections for obj1022 (graphObject_: Obj919) of type match_contains
    self.drawConnections(
(self.obj1022,self.obj1002,[234.0, 87.5, 330.0, 123.0],"true", 2) )
    # Connections for obj1023 (graphObject_: Obj920) of type match_contains
    self.drawConnections(
(self.obj1023,self.obj1001,[571.0, 87.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj1024 (graphObject_: Obj921) of type match_contains
    self.drawConnections(
(self.obj1024,self.obj1000,[477.5, 117.5, 817.0, 183.0],"true", 2) )
    # Connections for obj1025 (graphObject_: Obj922) of type match_contains
    self.drawConnections(
(self.obj1025,self.obj999,[582.0, 107.5, 1030.0, 223.0],"true", 2) )
    # Connections for obj1026 (graphObject_: Obj923) of type apply_contains
    self.drawConnections(
(self.obj1026,self.obj1003,[219.5, 417.0, 352.0, 489.0],"true", 2) )
    # Connections for obj1027 (graphObject_: Obj924) of type apply_contains
    self.drawConnections(
(self.obj1027,self.obj1004,[359.5, 432.0, 572.0, 491.0],"true", 2) )
    # Connections for obj1028 (graphObject_: Obj925) of type apply_contains
    self.drawConnections(
(self.obj1028,self.obj1005,[539.5, 431.5, 932.0, 488.0],"true", 2) )
    # Connections for obj1029 (graphObject_: Obj926) of type directLink_T
    self.drawConnections(
(self.obj1029,self.obj1004,[399.0, 484.0, 572.0, 491.0],"true", 2) )
    # Connections for obj1030 (graphObject_: Obj927) of type directLink_T
    self.drawConnections(
(self.obj1030,self.obj1005,[752.0, 490.0, 932.0, 488.0],"true", 2) )
    # Connections for obj1031 (graphObject_: Obj928) of type directLink_S
    self.drawConnections(
(self.obj1031,self.obj1001,[480.0, 123.0, 1004.0, 123.0],"true", 2) )
    # Connections for obj1032 (graphObject_: Obj929) of type directLink_S
    self.drawConnections(
(self.obj1032,self.obj999,[984.5, 193.0, 1030.0, 223.0],"true", 2) )
    # Connections for obj1033 (graphObject_: Obj930) of type directLink_S
    self.drawConnections(
(self.obj1033,self.obj1000,[848.0, 187.0, 817.0, 183.0],"true", 2) )
    # Connections for obj1034 (graphObject_: Obj931) of type backward_link
    self.drawConnections(
(self.obj1034,self.obj1002,[341.0, 287.0, 330.0, 123.0],"true", 2) )
    # Connections for obj1035 (graphObject_: Obj932) of type backward_link
    self.drawConnections(
(self.obj1035,self.obj1001,[968.0, 305.5, 1004.0, 123.0],"true", 2) )
    # Connections for obj1036 (graphObject_: Obj933) of type hasAttribute_S
    self.drawConnections(
(self.obj1036,self.obj1006,[312.0, 166.0, 294.0, 209.0],"true", 2) )
    # Connections for obj1037 (graphObject_: Obj934) of type hasAttribute_S
    self.drawConnections(
(self.obj1037,self.obj1007,[402.0, 158.5, 474.0, 194.0],"true", 2) )
    # Connections for obj1038 (graphObject_: Obj935) of type hasAttribute_S
    self.drawConnections(
(self.obj1038,self.obj1008,[815.5, 228.5, 814.0, 274.0],"true", 2) )
    # Connections for obj1039 (graphObject_: Obj936) of type hasAttribute_T
    self.drawConnections(
(self.obj1039,self.obj1009,[555.5, 442.0, 539.0, 395.0],"true", 2) )
    # Connections for obj1040 (graphObject_: Obj937) of type hasAttribute_T
    self.drawConnections(
(self.obj1040,self.obj1010,[283.0, 531.5, 214.0, 574.0],"true", 2) )
    # Connections for obj1041 (graphObject_: Obj938) of type hasAttribute_T
    self.drawConnections(
(self.obj1041,self.obj1011,[893.0, 531.0, 854.0, 574.0],"true", 2) )
    # Connections for obj1042 (graphObject_: Obj939) of type leftExpr
    self.drawConnections(
(self.obj1042,self.obj1006,[367.5, 245.0, 294.0, 209.0],"true", 2) )
    # Connections for obj1043 (graphObject_: Obj940) of type leftExpr
    self.drawConnections(
(self.obj1043,self.obj1007,[556.0, 236.5, 474.0, 194.0],"true", 2) )
    # Connections for obj1044 (graphObject_: Obj941) of type leftExpr
    self.drawConnections(
(self.obj1044,self.obj1009,[622.0, 397.5, 539.0, 395.0],"true", 2) )
    # Connections for obj1045 (graphObject_: Obj942) of type leftExpr
    self.drawConnections(
(self.obj1045,self.obj1010,[276.0, 616.5, 214.0, 574.0],"true", 2) )
    # Connections for obj1046 (graphObject_: Obj943) of type leftExpr
    self.drawConnections(
(self.obj1046,self.obj1011,[896.0, 616.5, 854.0, 574.0],"true", 2) )
    # Connections for obj1047 (graphObject_: Obj944) of type rightExpr
    self.drawConnections(
(self.obj1047,self.obj1017,[367.5, 287.5, 294.0, 294.0],"true", 2) )
    # Connections for obj1048 (graphObject_: Obj945) of type rightExpr
    self.drawConnections(
(self.obj1048,self.obj1018,[636.0, 236.5, 634.0, 194.0],"true", 2) )
    # Connections for obj1049 (graphObject_: Obj946) of type rightExpr
    self.drawConnections(
(self.obj1049,self.obj1008,[759.5, 337.0, 814.0, 274.0],"true", 2) )
    # Connections for obj1050 (graphObject_: Obj947) of type rightExpr
    self.drawConnections(
(self.obj1050,self.obj1019,[356.0, 616.5, 374.0, 574.0],"true", 2) )
    # Connections for obj1051 (graphObject_: Obj948) of type rightExpr
    self.drawConnections(
(self.obj1051,self.obj1020,[996.0, 616.5, 1054.0, 574.0],"true", 2) )

newfunction = Transition2ListenBranch_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
