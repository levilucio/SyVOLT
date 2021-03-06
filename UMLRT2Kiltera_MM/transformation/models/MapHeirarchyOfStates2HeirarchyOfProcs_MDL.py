"""
__MapHeirarchyOfStates2HeirarchyOfProcs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 15:00:02 2015
___________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from State import *
from ProcDef import *
from LocalDef import *
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
from graph_Equation import *
from graph_match_contains import *
from graph_Attribute import *
from graph_LocalDef import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_hasAttribute_T import *
from graph_hasAttribute_S import *
from graph_leftExpr import *
from graph_ProcDef import *
from graph_Constant import *
from graph_ApplyModel import *
from graph_State import *
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

def MapHeirarchyOfStates2HeirarchyOfProcs_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('MapHeirarchyOfStates2HeirarchyOfProcs')
    # --- ASG attributes over ---


    self.obj486=MatchModel(self)
    self.obj486.isGraphObjectVisual = True

    if(hasattr(self.obj486, '_setHierarchicalLink')):
      self.obj486._setHierarchicalLink(False)

    self.obj486.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj486)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj486.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj486)
    self.globalAndLocalPostcondition(self.obj486, rootNode)
    self.obj486.postAction( rootNode.CREATE )

    self.obj487=ApplyModel(self)
    self.obj487.isGraphObjectVisual = True

    if(hasattr(self.obj487, '_setHierarchicalLink')):
      self.obj487._setHierarchicalLink(False)

    self.obj487.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,240.0,self.obj487)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj487.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj487)
    self.globalAndLocalPostcondition(self.obj487, rootNode)
    self.obj487.postAction( rootNode.CREATE )

    self.obj488=State(self)
    self.obj488.isGraphObjectVisual = True

    if(hasattr(self.obj488, '_setHierarchicalLink')):
      self.obj488._setHierarchicalLink(False)

    # name
    self.obj488.name.setValue('state1')

    # classtype
    self.obj488.classtype.setValue('State')

    # cardinality
    self.obj488.cardinality.setValue('+')

    self.obj488.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,58.0,self.obj488)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj488.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj488)
    self.globalAndLocalPostcondition(self.obj488, rootNode)
    self.obj488.postAction( rootNode.CREATE )

    self.obj489=State(self)
    self.obj489.isGraphObjectVisual = True

    if(hasattr(self.obj489, '_setHierarchicalLink')):
      self.obj489._setHierarchicalLink(False)

    # name
    self.obj489.name.setValue('state2')

    # classtype
    self.obj489.classtype.setValue('State')

    # cardinality
    self.obj489.cardinality.setValue('+')

    self.obj489.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(480.0,60.0,self.obj489)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj489.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj489)
    self.globalAndLocalPostcondition(self.obj489, rootNode)
    self.obj489.postAction( rootNode.CREATE )

    self.obj490=ProcDef(self)
    self.obj490.isGraphObjectVisual = True

    if(hasattr(self.obj490, '_setHierarchicalLink')):
      self.obj490._setHierarchicalLink(False)

    # classtype
    self.obj490.classtype.setValue('ProcDef')

    # cardinality
    self.obj490.cardinality.setValue('1')

    # name
    self.obj490.name.setValue('procDef1')

    self.obj490.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(480.0,300.0,self.obj490)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj490.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj490)
    self.globalAndLocalPostcondition(self.obj490, rootNode)
    self.obj490.postAction( rootNode.CREATE )

    self.obj491=LocalDef(self)
    self.obj491.isGraphObjectVisual = True

    if(hasattr(self.obj491, '_setHierarchicalLink')):
      self.obj491._setHierarchicalLink(False)

    # classtype
    self.obj491.classtype.setValue('LocalDef')

    # cardinality
    self.obj491.cardinality.setValue('1')

    # name
    self.obj491.name.setValue('localDef1')

    self.obj491.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(180.0,300.0,self.obj491)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj491.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj491)
    self.globalAndLocalPostcondition(self.obj491, rootNode)
    self.obj491.postAction( rootNode.CREATE )

    self.obj492=Attribute(self)
    self.obj492.isGraphObjectVisual = True

    if(hasattr(self.obj492, '_setHierarchicalLink')):
      self.obj492._setHierarchicalLink(False)

    # Type
    self.obj492.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj492.Type.config = 0

    # name
    self.obj492.name.setValue('isComposite')

    self.obj492.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(282.0,152.0,self.obj492)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj492.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj492)
    self.globalAndLocalPostcondition(self.obj492, rootNode)
    self.obj492.postAction( rootNode.CREATE )

    self.obj493=Attribute(self)
    self.obj493.isGraphObjectVisual = True

    if(hasattr(self.obj493, '_setHierarchicalLink')):
      self.obj493._setHierarchicalLink(False)

    # Type
    self.obj493.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj493.Type.config = 0

    # name
    self.obj493.name.setValue('pivot')

    self.obj493.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,420.0,self.obj493)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj493.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj493)
    self.globalAndLocalPostcondition(self.obj493, rootNode)
    self.obj493.postAction( rootNode.CREATE )

    self.obj494=Attribute(self)
    self.obj494.isGraphObjectVisual = True

    if(hasattr(self.obj494, '_setHierarchicalLink')):
      self.obj494._setHierarchicalLink(False)

    # Type
    self.obj494.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj494.Type.config = 0

    # name
    self.obj494.name.setValue('pivot')

    self.obj494.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,420.0,self.obj494)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj494.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj494)
    self.globalAndLocalPostcondition(self.obj494, rootNode)
    self.obj494.postAction( rootNode.CREATE )

    self.obj495=Equation(self)
    self.obj495.isGraphObjectVisual = True

    if(hasattr(self.obj495, '_setHierarchicalLink')):
      self.obj495._setHierarchicalLink(False)

    # name
    self.obj495.name.setValue('eq1')

    self.obj495.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,220.0,self.obj495)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj495.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj495)
    self.globalAndLocalPostcondition(self.obj495, rootNode)
    self.obj495.postAction( rootNode.CREATE )

    self.obj496=Equation(self)
    self.obj496.isGraphObjectVisual = True

    if(hasattr(self.obj496, '_setHierarchicalLink')):
      self.obj496._setHierarchicalLink(False)

    # name
    self.obj496.name.setValue('eq2')

    self.obj496.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,420.0,self.obj496)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj496.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj496)
    self.globalAndLocalPostcondition(self.obj496, rootNode)
    self.obj496.postAction( rootNode.CREATE )

    self.obj497=Equation(self)
    self.obj497.isGraphObjectVisual = True

    if(hasattr(self.obj497, '_setHierarchicalLink')):
      self.obj497._setHierarchicalLink(False)

    # name
    self.obj497.name.setValue('eq3')

    self.obj497.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,420.0,self.obj497)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj497.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj497)
    self.globalAndLocalPostcondition(self.obj497, rootNode)
    self.obj497.postAction( rootNode.CREATE )

    self.obj498=Constant(self)
    self.obj498.isGraphObjectVisual = True

    if(hasattr(self.obj498, '_setHierarchicalLink')):
      self.obj498._setHierarchicalLink(False)

    # Type
    self.obj498.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj498.Type.config = 0

    # name
    self.obj498.name.setValue('true')

    self.obj498.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(459.0,152.0,self.obj498)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj498.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj498)
    self.globalAndLocalPostcondition(self.obj498, rootNode)
    self.obj498.postAction( rootNode.CREATE )

    self.obj499=Constant(self)
    self.obj499.isGraphObjectVisual = True

    if(hasattr(self.obj499, '_setHierarchicalLink')):
      self.obj499._setHierarchicalLink(False)

    # Type
    self.obj499.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj499.Type.config = 0

    # name
    self.obj499.name.setValue('localdefcompstate')

    self.obj499.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(200.0,500.0,self.obj499)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj499.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj499)
    self.globalAndLocalPostcondition(self.obj499, rootNode)
    self.obj499.postAction( rootNode.CREATE )

    self.obj500=Constant(self)
    self.obj500.isGraphObjectVisual = True

    if(hasattr(self.obj500, '_setHierarchicalLink')):
      self.obj500._setHierarchicalLink(False)

    # Type
    self.obj500.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj500.Type.config = 0

    # name
    self.obj500.name.setValue('procdef')

    self.obj500.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,500.0,self.obj500)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj500.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj500)
    self.globalAndLocalPostcondition(self.obj500, rootNode)
    self.obj500.postAction( rootNode.CREATE )

    self.obj501=paired_with(self)
    self.obj501.isGraphObjectVisual = True

    if(hasattr(self.obj501, '_setHierarchicalLink')):
      self.obj501._setHierarchicalLink(False)

    self.obj501.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj501)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj501.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj501)
    self.globalAndLocalPostcondition(self.obj501, rootNode)
    self.obj501.postAction( rootNode.CREATE )

    self.obj502=match_contains(self)
    self.obj502.isGraphObjectVisual = True

    if(hasattr(self.obj502, '_setHierarchicalLink')):
      self.obj502._setHierarchicalLink(False)

    self.obj502.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(250.0,76.0,self.obj502)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj502.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj502)
    self.globalAndLocalPostcondition(self.obj502, rootNode)
    self.obj502.postAction( rootNode.CREATE )

    self.obj503=match_contains(self)
    self.obj503.isGraphObjectVisual = True

    if(hasattr(self.obj503, '_setHierarchicalLink')):
      self.obj503._setHierarchicalLink(False)

    self.obj503.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,74.0,self.obj503)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj503.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj503)
    self.globalAndLocalPostcondition(self.obj503, rootNode)
    self.obj503.postAction( rootNode.CREATE )

    self.obj504=apply_contains(self)
    self.obj504.isGraphObjectVisual = True

    if(hasattr(self.obj504, '_setHierarchicalLink')):
      self.obj504._setHierarchicalLink(False)

    self.obj504.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,312.0,self.obj504)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj504.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj504)
    self.globalAndLocalPostcondition(self.obj504, rootNode)
    self.obj504.postAction( rootNode.CREATE )

    self.obj505=apply_contains(self)
    self.obj505.isGraphObjectVisual = True

    if(hasattr(self.obj505, '_setHierarchicalLink')):
      self.obj505._setHierarchicalLink(False)

    self.obj505.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(397.5,312.0,self.obj505)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj505.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj505)
    self.globalAndLocalPostcondition(self.obj505, rootNode)
    self.obj505.postAction( rootNode.CREATE )

    self.obj506=directLink_T(self)
    self.obj506.isGraphObjectVisual = True

    if(hasattr(self.obj506, '_setHierarchicalLink')):
      self.obj506._setHierarchicalLink(False)

    # associationType
    self.obj506.associationType.setValue('def')

    self.obj506.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(502.0,351.0,self.obj506)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj506.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj506)
    self.globalAndLocalPostcondition(self.obj506, rootNode)
    self.obj506.postAction( rootNode.CREATE )

    self.obj507=directLink_S(self)
    self.obj507.isGraphObjectVisual = True

    if(hasattr(self.obj507, '_setHierarchicalLink')):
      self.obj507._setHierarchicalLink(False)

    # associationType
    self.obj507.associationType.setValue('states')

    self.obj507.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,102.0,self.obj507)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj507.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj507)
    self.globalAndLocalPostcondition(self.obj507, rootNode)
    self.obj507.postAction( rootNode.CREATE )

    self.obj508=backward_link(self)
    self.obj508.isGraphObjectVisual = True

    if(hasattr(self.obj508, '_setHierarchicalLink')):
      self.obj508._setHierarchicalLink(False)

    # type
    self.obj508.type.setValue('ruleDef')

    self.obj508.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,226.0,self.obj508)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj508.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj508)
    self.globalAndLocalPostcondition(self.obj508, rootNode)
    self.obj508.postAction( rootNode.CREATE )

    self.obj509=backward_link(self)
    self.obj509.isGraphObjectVisual = True

    if(hasattr(self.obj509, '_setHierarchicalLink')):
      self.obj509._setHierarchicalLink(False)

    # type
    self.obj509.type.setValue('ruleDef')

    self.obj509.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(651.0,227.0,self.obj509)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj509.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj509)
    self.globalAndLocalPostcondition(self.obj509, rootNode)
    self.obj509.postAction( rootNode.CREATE )

    self.obj510=hasAttribute_S(self)
    self.obj510.isGraphObjectVisual = True

    if(hasattr(self.obj510, '_setHierarchicalLink')):
      self.obj510._setHierarchicalLink(False)

    self.obj510.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(377.5,137.5,self.obj510)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj510.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj510)
    self.globalAndLocalPostcondition(self.obj510, rootNode)
    self.obj510.postAction( rootNode.CREATE )

    self.obj511=hasAttribute_T(self)
    self.obj511.isGraphObjectVisual = True

    if(hasattr(self.obj511, '_setHierarchicalLink')):
      self.obj511._setHierarchicalLink(False)

    self.obj511.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(273.0,402.5,self.obj511)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj511.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj511)
    self.globalAndLocalPostcondition(self.obj511, rootNode)
    self.obj511.postAction( rootNode.CREATE )

    self.obj512=hasAttribute_T(self)
    self.obj512.isGraphObjectVisual = True

    if(hasattr(self.obj512, '_setHierarchicalLink')):
      self.obj512._setHierarchicalLink(False)

    self.obj512.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(633.0,402.5,self.obj512)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj512.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj512)
    self.globalAndLocalPostcondition(self.obj512, rootNode)
    self.obj512.postAction( rootNode.CREATE )

    self.obj513=leftExpr(self)
    self.obj513.isGraphObjectVisual = True

    if(hasattr(self.obj513, '_setHierarchicalLink')):
      self.obj513._setHierarchicalLink(False)

    self.obj513.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(439.5,219.0,self.obj513)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj513.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj513)
    self.globalAndLocalPostcondition(self.obj513, rootNode)
    self.obj513.postAction( rootNode.CREATE )

    self.obj514=leftExpr(self)
    self.obj514.isGraphObjectVisual = True

    if(hasattr(self.obj514, '_setHierarchicalLink')):
      self.obj514._setHierarchicalLink(False)

    self.obj514.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,456.5,self.obj514)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj514.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj514)
    self.globalAndLocalPostcondition(self.obj514, rootNode)
    self.obj514.postAction( rootNode.CREATE )

    self.obj515=leftExpr(self)
    self.obj515.isGraphObjectVisual = True

    if(hasattr(self.obj515, '_setHierarchicalLink')):
      self.obj515._setHierarchicalLink(False)

    self.obj515.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(696.0,456.5,self.obj515)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj515.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj515)
    self.globalAndLocalPostcondition(self.obj515, rootNode)
    self.obj515.postAction( rootNode.CREATE )

    self.obj516=rightExpr(self)
    self.obj516.isGraphObjectVisual = True

    if(hasattr(self.obj516, '_setHierarchicalLink')):
      self.obj516._setHierarchicalLink(False)

    self.obj516.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(519.0,236.0,self.obj516)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj516.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj516)
    self.globalAndLocalPostcondition(self.obj516, rootNode)
    self.obj516.postAction( rootNode.CREATE )

    self.obj517=rightExpr(self)
    self.obj517.isGraphObjectVisual = True

    if(hasattr(self.obj517, '_setHierarchicalLink')):
      self.obj517._setHierarchicalLink(False)

    self.obj517.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(386.0,496.5,self.obj517)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj517.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj517)
    self.globalAndLocalPostcondition(self.obj517, rootNode)
    self.obj517.postAction( rootNode.CREATE )

    self.obj518=rightExpr(self)
    self.obj518.isGraphObjectVisual = True

    if(hasattr(self.obj518, '_setHierarchicalLink')):
      self.obj518._setHierarchicalLink(False)

    self.obj518.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(756.0,496.5,self.obj518)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj518.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj518)
    self.globalAndLocalPostcondition(self.obj518, rootNode)
    self.obj518.postAction( rootNode.CREATE )

    # Connections for obj486 (graphObject_: Obj383) of type MatchModel
    self.drawConnections(
(self.obj486,self.obj501,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj486,self.obj502,[138.0, 51.0, 250.0, 76.0],"true", 2),
(self.obj486,self.obj503,[138.0, 51.0, 394.0, 74.0],"true", 2) )
    # Connections for obj487 (graphObject_: Obj384) of type ApplyModel
    self.drawConnections(
(self.obj487,self.obj504,[143.0, 273.0, 247.5, 312.0],"true", 2),
(self.obj487,self.obj505,[143.0, 273.0, 397.5, 312.0],"true", 2) )
    # Connections for obj488 (graphObject_: Obj385) named state1
    self.drawConnections(
(self.obj488,self.obj507,[350.0, 101.0, 470.0, 102.0],"true", 2),
(self.obj488,self.obj510,[350.0, 101.0, 377.5, 137.5],"true", 2) )
    # Connections for obj489 (graphObject_: Obj386) named state2
    self.drawConnections(
 )
    # Connections for obj490 (graphObject_: Obj387) named procDef1
    self.drawConnections(
(self.obj490,self.obj509,[652.0, 351.0, 651.0, 227.0],"true", 2),
(self.obj490,self.obj512,[652.0, 351.0, 633.0, 402.5],"true", 2) )
    # Connections for obj491 (graphObject_: Obj388) named localDef1
    self.drawConnections(
(self.obj491,self.obj506,[352.0, 351.0, 502.0, 351.0],"true", 2),
(self.obj491,self.obj508,[352.0, 351.0, 351.0, 226.0],"true", 2),
(self.obj491,self.obj511,[352.0, 351.0, 273.0, 402.5],"true", 2) )
    # Connections for obj492 (graphObject_: Obj389) named isComposite
    self.drawConnections(
 )
    # Connections for obj493 (graphObject_: Obj390) named pivot
    self.drawConnections(
 )
    # Connections for obj494 (graphObject_: Obj391) named pivot
    self.drawConnections(
 )
    # Connections for obj495 (graphObject_: Obj392) named eq1
    self.drawConnections(
(self.obj495,self.obj513,[478.0, 259.0, 439.5, 219.0],"true", 2),
(self.obj495,self.obj516,[478.0, 259.0, 519.0, 236.0],"true", 2) )
    # Connections for obj496 (graphObject_: Obj393) named eq2
    self.drawConnections(
(self.obj496,self.obj514,[438.0, 459.0, 316.0, 456.5],"true", 2),
(self.obj496,self.obj517,[438.0, 459.0, 386.0, 496.5],"true", 2) )
    # Connections for obj497 (graphObject_: Obj394) named eq3
    self.drawConnections(
(self.obj497,self.obj515,[778.0, 459.0, 696.0, 456.5],"true", 2),
(self.obj497,self.obj518,[778.0, 459.0, 756.0, 496.5],"true", 2) )
    # Connections for obj498 (graphObject_: Obj395) named true
    self.drawConnections(
 )
    # Connections for obj499 (graphObject_: Obj396) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj500 (graphObject_: Obj397) named procdef
    self.drawConnections(
 )
    # Connections for obj501 (graphObject_: Obj398) of type paired_with
    self.drawConnections(
(self.obj501,self.obj487,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj502 (graphObject_: Obj399) of type match_contains
    self.drawConnections(
(self.obj502,self.obj488,[250.0, 76.0, 350.0, 101.0],"true", 2) )
    # Connections for obj503 (graphObject_: Obj400) of type match_contains
    self.drawConnections(
(self.obj503,self.obj489,[394.0, 74.0, 650.0, 103.0],"true", 2) )
    # Connections for obj504 (graphObject_: Obj401) of type apply_contains
    self.drawConnections(
(self.obj504,self.obj491,[247.5, 312.0, 352.0, 351.0],"true", 2) )
    # Connections for obj505 (graphObject_: Obj402) of type apply_contains
    self.drawConnections(
(self.obj505,self.obj490,[397.5, 312.0, 652.0, 351.0],"true", 2) )
    # Connections for obj506 (graphObject_: Obj403) of type directLink_T
    self.drawConnections(
(self.obj506,self.obj490,[502.0, 351.0, 652.0, 351.0],"true", 2) )
    # Connections for obj507 (graphObject_: Obj404) of type directLink_S
    self.drawConnections(
(self.obj507,self.obj489,[470.0, 102.0, 650.0, 103.0],"true", 2) )
    # Connections for obj508 (graphObject_: Obj405) of type backward_link
    self.drawConnections(
(self.obj508,self.obj488,[351.0, 226.0, 350.0, 101.0],"true", 2) )
    # Connections for obj509 (graphObject_: Obj406) of type backward_link
    self.drawConnections(
(self.obj509,self.obj489,[651.0, 227.0, 650.0, 103.0],"true", 2) )
    # Connections for obj510 (graphObject_: Obj407) of type hasAttribute_S
    self.drawConnections(
(self.obj510,self.obj492,[377.5, 137.5, 416.0, 186.0],"true", 2) )
    # Connections for obj511 (graphObject_: Obj408) of type hasAttribute_T
    self.drawConnections(
(self.obj511,self.obj493,[273.0, 402.5, 194.0, 454.0],"true", 2) )
    # Connections for obj512 (graphObject_: Obj409) of type hasAttribute_T
    self.drawConnections(
(self.obj512,self.obj494,[633.0, 402.5, 614.0, 454.0],"true", 2) )
    # Connections for obj513 (graphObject_: Obj410) of type leftExpr
    self.drawConnections(
(self.obj513,self.obj492,[439.5, 219.0, 416.0, 186.0],"true", 2) )
    # Connections for obj514 (graphObject_: Obj411) of type leftExpr
    self.drawConnections(
(self.obj514,self.obj493,[316.0, 456.5, 194.0, 454.0],"true", 2) )
    # Connections for obj515 (graphObject_: Obj412) of type leftExpr
    self.drawConnections(
(self.obj515,self.obj494,[696.0, 456.5, 614.0, 454.0],"true", 2) )
    # Connections for obj516 (graphObject_: Obj413) of type rightExpr
    self.drawConnections(
(self.obj516,self.obj498,[519.0, 236.0, 593.0, 186.0],"true", 2) )
    # Connections for obj517 (graphObject_: Obj414) of type rightExpr
    self.drawConnections(
(self.obj517,self.obj499,[386.0, 496.5, 334.0, 534.0],"true", 2) )
    # Connections for obj518 (graphObject_: Obj415) of type rightExpr
    self.drawConnections(
(self.obj518,self.obj500,[756.0, 496.5, 734.0, 534.0],"true", 2) )

newfunction = MapHeirarchyOfStates2HeirarchyOfProcs_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
