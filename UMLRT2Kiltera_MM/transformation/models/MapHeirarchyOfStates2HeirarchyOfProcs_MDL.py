"""
__MapHeirarchyOfStates2HeirarchyOfProcs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:06:26 2015
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


    self.obj524=MatchModel(self)
    self.obj524.isGraphObjectVisual = True

    if(hasattr(self.obj524, '_setHierarchicalLink')):
      self.obj524._setHierarchicalLink(False)

    self.obj524.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj524)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj524.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj524)
    self.globalAndLocalPostcondition(self.obj524, rootNode)
    self.obj524.postAction( rootNode.CREATE )

    self.obj525=ApplyModel(self)
    self.obj525.isGraphObjectVisual = True

    if(hasattr(self.obj525, '_setHierarchicalLink')):
      self.obj525._setHierarchicalLink(False)

    self.obj525.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,240.0,self.obj525)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj525.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj525)
    self.globalAndLocalPostcondition(self.obj525, rootNode)
    self.obj525.postAction( rootNode.CREATE )

    self.obj526=State(self)
    self.obj526.isGraphObjectVisual = True

    if(hasattr(self.obj526, '_setHierarchicalLink')):
      self.obj526._setHierarchicalLink(False)

    # name
    self.obj526.name.setValue('state1')

    # classtype
    self.obj526.classtype.setValue('State')

    # cardinality
    self.obj526.cardinality.setValue('+')

    self.obj526.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,58.0,self.obj526)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj526.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj526)
    self.globalAndLocalPostcondition(self.obj526, rootNode)
    self.obj526.postAction( rootNode.CREATE )

    self.obj527=State(self)
    self.obj527.isGraphObjectVisual = True

    if(hasattr(self.obj527, '_setHierarchicalLink')):
      self.obj527._setHierarchicalLink(False)

    # name
    self.obj527.name.setValue('state2')

    # classtype
    self.obj527.classtype.setValue('State')

    # cardinality
    self.obj527.cardinality.setValue('+')

    self.obj527.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(480.0,60.0,self.obj527)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj527.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj527)
    self.globalAndLocalPostcondition(self.obj527, rootNode)
    self.obj527.postAction( rootNode.CREATE )

    self.obj528=ProcDef(self)
    self.obj528.isGraphObjectVisual = True

    if(hasattr(self.obj528, '_setHierarchicalLink')):
      self.obj528._setHierarchicalLink(False)

    # classtype
    self.obj528.classtype.setValue('ProcDef')

    # cardinality
    self.obj528.cardinality.setValue('1')

    # name
    self.obj528.name.setValue('procDef1')

    self.obj528.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(480.0,300.0,self.obj528)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj528.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj528)
    self.globalAndLocalPostcondition(self.obj528, rootNode)
    self.obj528.postAction( rootNode.CREATE )

    self.obj529=LocalDef(self)
    self.obj529.isGraphObjectVisual = True

    if(hasattr(self.obj529, '_setHierarchicalLink')):
      self.obj529._setHierarchicalLink(False)

    # classtype
    self.obj529.classtype.setValue('LocalDef')

    # cardinality
    self.obj529.cardinality.setValue('1')

    # name
    self.obj529.name.setValue('localDef1')

    self.obj529.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(180.0,300.0,self.obj529)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj529.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj529)
    self.globalAndLocalPostcondition(self.obj529, rootNode)
    self.obj529.postAction( rootNode.CREATE )

    self.obj530=Attribute(self)
    self.obj530.isGraphObjectVisual = True

    if(hasattr(self.obj530, '_setHierarchicalLink')):
      self.obj530._setHierarchicalLink(False)

    # Type
    self.obj530.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj530.Type.config = 0

    # name
    self.obj530.name.setValue('isComposite')

    self.obj530.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(282.0,152.0,self.obj530)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj530.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj530)
    self.globalAndLocalPostcondition(self.obj530, rootNode)
    self.obj530.postAction( rootNode.CREATE )

    self.obj531=Attribute(self)
    self.obj531.isGraphObjectVisual = True

    if(hasattr(self.obj531, '_setHierarchicalLink')):
      self.obj531._setHierarchicalLink(False)

    # Type
    self.obj531.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj531.Type.config = 0

    # name
    self.obj531.name.setValue('pivot')

    self.obj531.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,420.0,self.obj531)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj531.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj531)
    self.globalAndLocalPostcondition(self.obj531, rootNode)
    self.obj531.postAction( rootNode.CREATE )

    self.obj532=Attribute(self)
    self.obj532.isGraphObjectVisual = True

    if(hasattr(self.obj532, '_setHierarchicalLink')):
      self.obj532._setHierarchicalLink(False)

    # Type
    self.obj532.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj532.Type.config = 0

    # name
    self.obj532.name.setValue('pivot')

    self.obj532.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,420.0,self.obj532)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj532.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj532)
    self.globalAndLocalPostcondition(self.obj532, rootNode)
    self.obj532.postAction( rootNode.CREATE )

    self.obj533=Equation(self)
    self.obj533.isGraphObjectVisual = True

    if(hasattr(self.obj533, '_setHierarchicalLink')):
      self.obj533._setHierarchicalLink(False)

    # name
    self.obj533.name.setValue('eq1')

    self.obj533.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,220.0,self.obj533)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj533.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj533)
    self.globalAndLocalPostcondition(self.obj533, rootNode)
    self.obj533.postAction( rootNode.CREATE )

    self.obj534=Equation(self)
    self.obj534.isGraphObjectVisual = True

    if(hasattr(self.obj534, '_setHierarchicalLink')):
      self.obj534._setHierarchicalLink(False)

    # name
    self.obj534.name.setValue('eq2')

    self.obj534.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,420.0,self.obj534)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj534.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj534)
    self.globalAndLocalPostcondition(self.obj534, rootNode)
    self.obj534.postAction( rootNode.CREATE )

    self.obj535=Equation(self)
    self.obj535.isGraphObjectVisual = True

    if(hasattr(self.obj535, '_setHierarchicalLink')):
      self.obj535._setHierarchicalLink(False)

    # name
    self.obj535.name.setValue('eq3')

    self.obj535.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,420.0,self.obj535)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj535.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj535)
    self.globalAndLocalPostcondition(self.obj535, rootNode)
    self.obj535.postAction( rootNode.CREATE )

    self.obj536=Constant(self)
    self.obj536.isGraphObjectVisual = True

    if(hasattr(self.obj536, '_setHierarchicalLink')):
      self.obj536._setHierarchicalLink(False)

    # Type
    self.obj536.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj536.Type.config = 0

    # name
    self.obj536.name.setValue('true')

    self.obj536.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(459.0,152.0,self.obj536)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj536.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj536)
    self.globalAndLocalPostcondition(self.obj536, rootNode)
    self.obj536.postAction( rootNode.CREATE )

    self.obj537=Constant(self)
    self.obj537.isGraphObjectVisual = True

    if(hasattr(self.obj537, '_setHierarchicalLink')):
      self.obj537._setHierarchicalLink(False)

    # Type
    self.obj537.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj537.Type.config = 0

    # name
    self.obj537.name.setValue('localdefcompstate')

    self.obj537.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(200.0,500.0,self.obj537)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj537.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj537)
    self.globalAndLocalPostcondition(self.obj537, rootNode)
    self.obj537.postAction( rootNode.CREATE )

    self.obj538=Constant(self)
    self.obj538.isGraphObjectVisual = True

    if(hasattr(self.obj538, '_setHierarchicalLink')):
      self.obj538._setHierarchicalLink(False)

    # Type
    self.obj538.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj538.Type.config = 0

    # name
    self.obj538.name.setValue('procdef')

    self.obj538.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,500.0,self.obj538)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj538.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj538)
    self.globalAndLocalPostcondition(self.obj538, rootNode)
    self.obj538.postAction( rootNode.CREATE )

    self.obj539=paired_with(self)
    self.obj539.isGraphObjectVisual = True

    if(hasattr(self.obj539, '_setHierarchicalLink')):
      self.obj539._setHierarchicalLink(False)

    self.obj539.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj539)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj539.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj539)
    self.globalAndLocalPostcondition(self.obj539, rootNode)
    self.obj539.postAction( rootNode.CREATE )

    self.obj540=match_contains(self)
    self.obj540.isGraphObjectVisual = True

    if(hasattr(self.obj540, '_setHierarchicalLink')):
      self.obj540._setHierarchicalLink(False)

    self.obj540.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(250.0,76.0,self.obj540)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj540.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj540)
    self.globalAndLocalPostcondition(self.obj540, rootNode)
    self.obj540.postAction( rootNode.CREATE )

    self.obj541=match_contains(self)
    self.obj541.isGraphObjectVisual = True

    if(hasattr(self.obj541, '_setHierarchicalLink')):
      self.obj541._setHierarchicalLink(False)

    self.obj541.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,74.0,self.obj541)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj541.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj541)
    self.globalAndLocalPostcondition(self.obj541, rootNode)
    self.obj541.postAction( rootNode.CREATE )

    self.obj542=apply_contains(self)
    self.obj542.isGraphObjectVisual = True

    if(hasattr(self.obj542, '_setHierarchicalLink')):
      self.obj542._setHierarchicalLink(False)

    self.obj542.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,312.0,self.obj542)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj542.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj542)
    self.globalAndLocalPostcondition(self.obj542, rootNode)
    self.obj542.postAction( rootNode.CREATE )

    self.obj543=apply_contains(self)
    self.obj543.isGraphObjectVisual = True

    if(hasattr(self.obj543, '_setHierarchicalLink')):
      self.obj543._setHierarchicalLink(False)

    self.obj543.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(397.5,312.0,self.obj543)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj543.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj543)
    self.globalAndLocalPostcondition(self.obj543, rootNode)
    self.obj543.postAction( rootNode.CREATE )

    self.obj544=directLink_T(self)
    self.obj544.isGraphObjectVisual = True

    if(hasattr(self.obj544, '_setHierarchicalLink')):
      self.obj544._setHierarchicalLink(False)

    # associationType
    self.obj544.associationType.setValue('def')

    self.obj544.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(502.0,351.0,self.obj544)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj544.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj544)
    self.globalAndLocalPostcondition(self.obj544, rootNode)
    self.obj544.postAction( rootNode.CREATE )

    self.obj545=directLink_S(self)
    self.obj545.isGraphObjectVisual = True

    if(hasattr(self.obj545, '_setHierarchicalLink')):
      self.obj545._setHierarchicalLink(False)

    # associationType
    self.obj545.associationType.setValue('states')

    self.obj545.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,102.0,self.obj545)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj545.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj545)
    self.globalAndLocalPostcondition(self.obj545, rootNode)
    self.obj545.postAction( rootNode.CREATE )

    self.obj546=backward_link(self)
    self.obj546.isGraphObjectVisual = True

    if(hasattr(self.obj546, '_setHierarchicalLink')):
      self.obj546._setHierarchicalLink(False)

    # type
    self.obj546.type.setValue('ruleDef')

    self.obj546.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,226.0,self.obj546)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj546.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj546)
    self.globalAndLocalPostcondition(self.obj546, rootNode)
    self.obj546.postAction( rootNode.CREATE )

    self.obj547=backward_link(self)
    self.obj547.isGraphObjectVisual = True

    if(hasattr(self.obj547, '_setHierarchicalLink')):
      self.obj547._setHierarchicalLink(False)

    # type
    self.obj547.type.setValue('ruleDef')

    self.obj547.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(651.0,227.0,self.obj547)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj547.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj547)
    self.globalAndLocalPostcondition(self.obj547, rootNode)
    self.obj547.postAction( rootNode.CREATE )

    self.obj548=hasAttribute_S(self)
    self.obj548.isGraphObjectVisual = True

    if(hasattr(self.obj548, '_setHierarchicalLink')):
      self.obj548._setHierarchicalLink(False)

    self.obj548.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(377.5,137.5,self.obj548)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj548.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj548)
    self.globalAndLocalPostcondition(self.obj548, rootNode)
    self.obj548.postAction( rootNode.CREATE )

    self.obj549=hasAttribute_T(self)
    self.obj549.isGraphObjectVisual = True

    if(hasattr(self.obj549, '_setHierarchicalLink')):
      self.obj549._setHierarchicalLink(False)

    self.obj549.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(273.0,402.5,self.obj549)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj549.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj549)
    self.globalAndLocalPostcondition(self.obj549, rootNode)
    self.obj549.postAction( rootNode.CREATE )

    self.obj550=hasAttribute_T(self)
    self.obj550.isGraphObjectVisual = True

    if(hasattr(self.obj550, '_setHierarchicalLink')):
      self.obj550._setHierarchicalLink(False)

    self.obj550.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(633.0,402.5,self.obj550)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj550.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj550)
    self.globalAndLocalPostcondition(self.obj550, rootNode)
    self.obj550.postAction( rootNode.CREATE )

    self.obj551=leftExpr(self)
    self.obj551.isGraphObjectVisual = True

    if(hasattr(self.obj551, '_setHierarchicalLink')):
      self.obj551._setHierarchicalLink(False)

    self.obj551.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(439.5,219.0,self.obj551)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj551.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj551)
    self.globalAndLocalPostcondition(self.obj551, rootNode)
    self.obj551.postAction( rootNode.CREATE )

    self.obj552=leftExpr(self)
    self.obj552.isGraphObjectVisual = True

    if(hasattr(self.obj552, '_setHierarchicalLink')):
      self.obj552._setHierarchicalLink(False)

    self.obj552.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,456.5,self.obj552)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj552.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj552)
    self.globalAndLocalPostcondition(self.obj552, rootNode)
    self.obj552.postAction( rootNode.CREATE )

    self.obj553=leftExpr(self)
    self.obj553.isGraphObjectVisual = True

    if(hasattr(self.obj553, '_setHierarchicalLink')):
      self.obj553._setHierarchicalLink(False)

    self.obj553.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(696.0,456.5,self.obj553)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj553.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj553)
    self.globalAndLocalPostcondition(self.obj553, rootNode)
    self.obj553.postAction( rootNode.CREATE )

    self.obj554=rightExpr(self)
    self.obj554.isGraphObjectVisual = True

    if(hasattr(self.obj554, '_setHierarchicalLink')):
      self.obj554._setHierarchicalLink(False)

    self.obj554.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(519.0,236.0,self.obj554)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj554.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj554)
    self.globalAndLocalPostcondition(self.obj554, rootNode)
    self.obj554.postAction( rootNode.CREATE )

    self.obj555=rightExpr(self)
    self.obj555.isGraphObjectVisual = True

    if(hasattr(self.obj555, '_setHierarchicalLink')):
      self.obj555._setHierarchicalLink(False)

    self.obj555.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(386.0,496.5,self.obj555)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj555.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj555)
    self.globalAndLocalPostcondition(self.obj555, rootNode)
    self.obj555.postAction( rootNode.CREATE )

    self.obj556=rightExpr(self)
    self.obj556.isGraphObjectVisual = True

    if(hasattr(self.obj556, '_setHierarchicalLink')):
      self.obj556._setHierarchicalLink(False)

    self.obj556.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(756.0,496.5,self.obj556)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj556.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj556)
    self.globalAndLocalPostcondition(self.obj556, rootNode)
    self.obj556.postAction( rootNode.CREATE )

    # Connections for obj524 (graphObject_: Obj383) of type MatchModel
    self.drawConnections(
(self.obj524,self.obj539,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj524,self.obj540,[138.0, 51.0, 250.0, 76.0],"true", 2),
(self.obj524,self.obj541,[138.0, 51.0, 394.0, 74.0],"true", 2) )
    # Connections for obj525 (graphObject_: Obj384) of type ApplyModel
    self.drawConnections(
(self.obj525,self.obj542,[143.0, 273.0, 247.5, 312.0],"true", 2),
(self.obj525,self.obj543,[143.0, 273.0, 397.5, 312.0],"true", 2) )
    # Connections for obj526 (graphObject_: Obj385) named state1
    self.drawConnections(
(self.obj526,self.obj545,[350.0, 101.0, 470.0, 102.0],"true", 2),
(self.obj526,self.obj548,[350.0, 101.0, 377.5, 137.5],"true", 2) )
    # Connections for obj527 (graphObject_: Obj386) named state2
    self.drawConnections(
 )
    # Connections for obj528 (graphObject_: Obj387) named procDef1
    self.drawConnections(
(self.obj528,self.obj547,[652.0, 351.0, 651.0, 227.0],"true", 2),
(self.obj528,self.obj550,[652.0, 351.0, 633.0, 402.5],"true", 2) )
    # Connections for obj529 (graphObject_: Obj388) named localDef1
    self.drawConnections(
(self.obj529,self.obj544,[352.0, 351.0, 502.0, 351.0],"true", 2),
(self.obj529,self.obj546,[352.0, 351.0, 351.0, 226.0],"true", 2),
(self.obj529,self.obj549,[352.0, 351.0, 273.0, 402.5],"true", 2) )
    # Connections for obj530 (graphObject_: Obj389) named isComposite
    self.drawConnections(
 )
    # Connections for obj531 (graphObject_: Obj390) named pivot
    self.drawConnections(
 )
    # Connections for obj532 (graphObject_: Obj391) named pivot
    self.drawConnections(
 )
    # Connections for obj533 (graphObject_: Obj392) named eq1
    self.drawConnections(
(self.obj533,self.obj551,[478.0, 259.0, 439.5, 219.0],"true", 2),
(self.obj533,self.obj554,[478.0, 259.0, 519.0, 236.0],"true", 2) )
    # Connections for obj534 (graphObject_: Obj393) named eq2
    self.drawConnections(
(self.obj534,self.obj552,[438.0, 459.0, 316.0, 456.5],"true", 2),
(self.obj534,self.obj555,[438.0, 459.0, 386.0, 496.5],"true", 2) )
    # Connections for obj535 (graphObject_: Obj394) named eq3
    self.drawConnections(
(self.obj535,self.obj553,[778.0, 459.0, 696.0, 456.5],"true", 2),
(self.obj535,self.obj556,[778.0, 459.0, 756.0, 496.5],"true", 2) )
    # Connections for obj536 (graphObject_: Obj395) named true
    self.drawConnections(
 )
    # Connections for obj537 (graphObject_: Obj396) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj538 (graphObject_: Obj397) named procdef
    self.drawConnections(
 )
    # Connections for obj539 (graphObject_: Obj398) of type paired_with
    self.drawConnections(
(self.obj539,self.obj525,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj540 (graphObject_: Obj399) of type match_contains
    self.drawConnections(
(self.obj540,self.obj526,[250.0, 76.0, 350.0, 101.0],"true", 2) )
    # Connections for obj541 (graphObject_: Obj400) of type match_contains
    self.drawConnections(
(self.obj541,self.obj527,[394.0, 74.0, 650.0, 103.0],"true", 2) )
    # Connections for obj542 (graphObject_: Obj401) of type apply_contains
    self.drawConnections(
(self.obj542,self.obj529,[247.5, 312.0, 352.0, 351.0],"true", 2) )
    # Connections for obj543 (graphObject_: Obj402) of type apply_contains
    self.drawConnections(
(self.obj543,self.obj528,[397.5, 312.0, 652.0, 351.0],"true", 2) )
    # Connections for obj544 (graphObject_: Obj403) of type directLink_T
    self.drawConnections(
(self.obj544,self.obj528,[502.0, 351.0, 652.0, 351.0],"true", 2) )
    # Connections for obj545 (graphObject_: Obj404) of type directLink_S
    self.drawConnections(
(self.obj545,self.obj527,[470.0, 102.0, 650.0, 103.0],"true", 2) )
    # Connections for obj546 (graphObject_: Obj405) of type backward_link
    self.drawConnections(
(self.obj546,self.obj526,[351.0, 226.0, 350.0, 101.0],"true", 2) )
    # Connections for obj547 (graphObject_: Obj406) of type backward_link
    self.drawConnections(
(self.obj547,self.obj527,[651.0, 227.0, 650.0, 103.0],"true", 2) )
    # Connections for obj548 (graphObject_: Obj407) of type hasAttribute_S
    self.drawConnections(
(self.obj548,self.obj530,[377.5, 137.5, 416.0, 186.0],"true", 2) )
    # Connections for obj549 (graphObject_: Obj408) of type hasAttribute_T
    self.drawConnections(
(self.obj549,self.obj531,[273.0, 402.5, 194.0, 454.0],"true", 2) )
    # Connections for obj550 (graphObject_: Obj409) of type hasAttribute_T
    self.drawConnections(
(self.obj550,self.obj532,[633.0, 402.5, 614.0, 454.0],"true", 2) )
    # Connections for obj551 (graphObject_: Obj410) of type leftExpr
    self.drawConnections(
(self.obj551,self.obj530,[439.5, 219.0, 416.0, 186.0],"true", 2) )
    # Connections for obj552 (graphObject_: Obj411) of type leftExpr
    self.drawConnections(
(self.obj552,self.obj531,[316.0, 456.5, 194.0, 454.0],"true", 2) )
    # Connections for obj553 (graphObject_: Obj412) of type leftExpr
    self.drawConnections(
(self.obj553,self.obj532,[696.0, 456.5, 614.0, 454.0],"true", 2) )
    # Connections for obj554 (graphObject_: Obj413) of type rightExpr
    self.drawConnections(
(self.obj554,self.obj536,[519.0, 236.0, 593.0, 186.0],"true", 2) )
    # Connections for obj555 (graphObject_: Obj414) of type rightExpr
    self.drawConnections(
(self.obj555,self.obj537,[386.0, 496.5, 334.0, 534.0],"true", 2) )
    # Connections for obj556 (graphObject_: Obj415) of type rightExpr
    self.drawConnections(
(self.obj556,self.obj538,[756.0, 496.5, 734.0, 534.0],"true", 2) )

newfunction = MapHeirarchyOfStates2HeirarchyOfProcs_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
