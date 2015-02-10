"""
__MapHeirarchyOfStates2HeirarchyOfProcs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Feb  9 22:28:55 2015
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
       new_obj = graph_ApplyModel(20.0,240.0,self.obj101)
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

    self.obj102=State(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # name
    self.obj102.name.setValue('state1')

    # classtype
    self.obj102.classtype.setValue('State')

    # cardinality
    self.obj102.cardinality.setValue('+')

    self.obj102.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,58.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=State(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('state2')

    # classtype
    self.obj103.classtype.setValue('State')

    # cardinality
    self.obj103.cardinality.setValue('+')

    self.obj103.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(480.0,60.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=ProcDef(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # classtype
    self.obj104.classtype.setValue('ProcDef')

    # cardinality
    self.obj104.cardinality.setValue('1')

    # name
    self.obj104.name.setValue('procDef1')

    self.obj104.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(480.0,300.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=LocalDef(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # classtype
    self.obj105.classtype.setValue('LocalDef')

    # cardinality
    self.obj105.cardinality.setValue('1')

    # name
    self.obj105.name.setValue('localDef1')

    self.obj105.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(180.0,300.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Attribute(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # Type
    self.obj106.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj106.Type.config = 0

    # name
    self.obj106.name.setValue('isComposite')

    self.obj106.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(282.0,152.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=Attribute(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # Type
    self.obj107.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj107.Type.config = 0

    # name
    self.obj107.name.setValue('pivot')

    self.obj107.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,420.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=Attribute(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # Type
    self.obj108.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj108.Type.config = 0

    # name
    self.obj108.name.setValue('pivot')

    self.obj108.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,420.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=Equation(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # name
    self.obj109.name.setValue('eq1')

    self.obj109.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,220.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Equation(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # name
    self.obj110.name.setValue('eq2')

    self.obj110.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,420.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Equation(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # name
    self.obj111.name.setValue('eq3')

    self.obj111.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,420.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=Constant(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # Type
    self.obj112.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj112.Type.config = 0

    # name
    self.obj112.name.setValue('true')

    self.obj112.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(459.0,152.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=Constant(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # Type
    self.obj113.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj113.Type.config = 0

    # name
    self.obj113.name.setValue('localdefcompstate')

    self.obj113.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(200.0,500.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Constant(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # Type
    self.obj114.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj114.Type.config = 0

    # name
    self.obj114.name.setValue('procdef')

    self.obj114.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,500.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=paired_with(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    self.obj115.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=match_contains(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    self.obj116.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(250.0,76.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=match_contains(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    self.obj117.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,74.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=apply_contains(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    self.obj118.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,312.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=apply_contains(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    self.obj119.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(397.5,312.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=directLink_T(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # associationType
    self.obj120.associationType.setValue('def')

    self.obj120.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(502.0,351.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=directLink_S(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # associationType
    self.obj121.associationType.setValue('states')

    self.obj121.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,102.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=backward_link(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # type
    self.obj122.type.setValue('ruleDef')

    self.obj122.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,226.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=backward_link(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # type
    self.obj123.type.setValue('ruleDef')

    self.obj123.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(651.0,227.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=hasAttribute_S(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    self.obj124.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(377.5,137.5,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=hasAttribute_T(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    self.obj125.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(273.0,402.5,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=hasAttribute_T(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    self.obj126.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(633.0,402.5,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=leftExpr(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    self.obj127.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(439.5,219.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=leftExpr(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    self.obj128.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,456.5,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=leftExpr(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    self.obj129.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(696.0,456.5,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=rightExpr(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    self.obj130.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(519.0,236.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=rightExpr(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    self.obj131.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(386.0,496.5,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=rightExpr(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    self.obj132.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(756.0,496.5,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj115,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj100,self.obj116,[138.0, 51.0, 250.0, 76.0],"true", 2),
(self.obj100,self.obj117,[138.0, 51.0, 394.0, 74.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj118,[143.0, 273.0, 247.5, 312.0],"true", 2),
(self.obj101,self.obj119,[143.0, 273.0, 397.5, 312.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj2) named state1
    self.drawConnections(
(self.obj102,self.obj121,[350.0, 101.0, 470.0, 102.0],"true", 2),
(self.obj102,self.obj124,[350.0, 101.0, 377.5, 137.5],"true", 2) )
    # Connections for obj103 (graphObject_: Obj3) named state2
    self.drawConnections(
 )
    # Connections for obj104 (graphObject_: Obj4) named procDef1
    self.drawConnections(
(self.obj104,self.obj123,[652.0, 351.0, 651.0, 227.0],"true", 2),
(self.obj104,self.obj126,[652.0, 351.0, 633.0, 402.5],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) named localDef1
    self.drawConnections(
(self.obj105,self.obj120,[352.0, 351.0, 502.0, 351.0],"true", 2),
(self.obj105,self.obj122,[352.0, 351.0, 351.0, 226.0],"true", 2),
(self.obj105,self.obj125,[352.0, 351.0, 273.0, 402.5],"true", 2) )
    # Connections for obj106 (graphObject_: Obj6) named isComposite
    self.drawConnections(
 )
    # Connections for obj107 (graphObject_: Obj7) named pivot
    self.drawConnections(
 )
    # Connections for obj108 (graphObject_: Obj8) named pivot
    self.drawConnections(
 )
    # Connections for obj109 (graphObject_: Obj9) named eq1
    self.drawConnections(
(self.obj109,self.obj127,[478.0, 259.0, 439.5, 219.0],"true", 2),
(self.obj109,self.obj130,[478.0, 259.0, 519.0, 236.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj10) named eq2
    self.drawConnections(
(self.obj110,self.obj128,[438.0, 459.0, 316.0, 456.5],"true", 2),
(self.obj110,self.obj131,[438.0, 459.0, 386.0, 496.5],"true", 2) )
    # Connections for obj111 (graphObject_: Obj11) named eq3
    self.drawConnections(
(self.obj111,self.obj129,[778.0, 459.0, 696.0, 456.5],"true", 2),
(self.obj111,self.obj132,[778.0, 459.0, 756.0, 496.5],"true", 2) )
    # Connections for obj112 (graphObject_: Obj12) named true
    self.drawConnections(
 )
    # Connections for obj113 (graphObject_: Obj13) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj114 (graphObject_: Obj14) named procdef
    self.drawConnections(
 )
    # Connections for obj115 (graphObject_: Obj15) of type paired_with
    self.drawConnections(
(self.obj115,self.obj101,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj116 (graphObject_: Obj16) of type match_contains
    self.drawConnections(
(self.obj116,self.obj102,[250.0, 76.0, 350.0, 101.0],"true", 2) )
    # Connections for obj117 (graphObject_: Obj17) of type match_contains
    self.drawConnections(
(self.obj117,self.obj103,[394.0, 74.0, 650.0, 103.0],"true", 2) )
    # Connections for obj118 (graphObject_: Obj18) of type apply_contains
    self.drawConnections(
(self.obj118,self.obj105,[247.5, 312.0, 352.0, 351.0],"true", 2) )
    # Connections for obj119 (graphObject_: Obj19) of type apply_contains
    self.drawConnections(
(self.obj119,self.obj104,[397.5, 312.0, 652.0, 351.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj20) of type directLink_T
    self.drawConnections(
(self.obj120,self.obj104,[502.0, 351.0, 652.0, 351.0],"true", 2) )
    # Connections for obj121 (graphObject_: Obj21) of type directLink_S
    self.drawConnections(
(self.obj121,self.obj103,[470.0, 102.0, 650.0, 103.0],"true", 2) )
    # Connections for obj122 (graphObject_: Obj22) of type backward_link
    self.drawConnections(
(self.obj122,self.obj102,[351.0, 226.0, 350.0, 101.0],"true", 2) )
    # Connections for obj123 (graphObject_: Obj23) of type backward_link
    self.drawConnections(
(self.obj123,self.obj103,[651.0, 227.0, 650.0, 103.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj24) of type hasAttribute_S
    self.drawConnections(
(self.obj124,self.obj106,[377.5, 137.5, 416.0, 186.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj25) of type hasAttribute_T
    self.drawConnections(
(self.obj125,self.obj107,[273.0, 402.5, 194.0, 454.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj26) of type hasAttribute_T
    self.drawConnections(
(self.obj126,self.obj108,[633.0, 402.5, 614.0, 454.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj27) of type leftExpr
    self.drawConnections(
(self.obj127,self.obj106,[439.5, 219.0, 416.0, 186.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj28) of type leftExpr
    self.drawConnections(
(self.obj128,self.obj107,[316.0, 456.5, 194.0, 454.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj29) of type leftExpr
    self.drawConnections(
(self.obj129,self.obj108,[696.0, 456.5, 614.0, 454.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj30) of type rightExpr
    self.drawConnections(
(self.obj130,self.obj112,[519.0, 236.0, 593.0, 186.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj31) of type rightExpr
    self.drawConnections(
(self.obj131,self.obj113,[386.0, 496.5, 334.0, 534.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj32) of type rightExpr
    self.drawConnections(
(self.obj132,self.obj114,[756.0, 496.5, 734.0, 534.0],"true", 2) )

newfunction = MapHeirarchyOfStates2HeirarchyOfProcs_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
