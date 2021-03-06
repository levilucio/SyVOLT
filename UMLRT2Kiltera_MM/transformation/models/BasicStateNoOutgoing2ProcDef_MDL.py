"""
__BasicStateNoOutgoing2ProcDef_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:52:16 2015
__________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from State import *
from ProcDef import *
from Null import *
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
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_match_contains import *
from graph_leftExpr import *
from graph_ProcDef import *
from graph_Null import *
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

def BasicStateNoOutgoing2ProcDef_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('BasicStateNoOutgoing2ProcDef')
    # --- ASG attributes over ---


    self.obj156=MatchModel(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    self.obj156.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(40.0,40.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=ApplyModel(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    self.obj157.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(40.0,260.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=State(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # name
    self.obj158.name.setValue('state1')

    # classtype
    self.obj158.classtype.setValue('State')

    # cardinality
    self.obj158.cardinality.setValue('+')

    self.obj158.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(240.0,60.0,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=ProcDef(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # classtype
    self.obj159.classtype.setValue('ProcDef')

    # cardinality
    self.obj159.cardinality.setValue('1')

    # name
    self.obj159.name.setValue('procdef1')

    self.obj159.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(240.0,260.0,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=Null(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # classtype
    self.obj160.classtype.setValue('Null')

    # cardinality
    self.obj160.cardinality.setValue('1')

    # name
    self.obj160.name.setValue('null1')

    self.obj160.graphClass_= graph_Null
    if self.genGraphics:
       new_obj = graph_Null(460.0,260.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Null", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=Attribute(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # Type
    self.obj161.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj161.Type.config = 0

    # name
    self.obj161.name.setValue('isComposite')

    self.obj161.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,20.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=Attribute(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    # Type
    self.obj162.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj162.Type.config = 0

    # name
    self.obj162.name.setValue('hasOutgoingTransitions')

    self.obj162.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(460.0,120.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj163=Attribute(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    # Type
    self.obj163.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj163.Type.config = 0

    # name
    self.obj163.name.setValue('pivot')

    self.obj163.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(300.0,380.0,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=Equation(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    # name
    self.obj164.name.setValue('eq1')

    self.obj164.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,20.0,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=Equation(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    # name
    self.obj165.name.setValue('eq2')

    self.obj165.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,120.0,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=Equation(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    # name
    self.obj166.name.setValue('eq3')

    self.obj166.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,400.0,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=Constant(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    # Type
    self.obj167.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj167.Type.config = 0

    # name
    self.obj167.name.setValue('false')

    self.obj167.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,20.0,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.98
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=Constant(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    # Type
    self.obj168.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj168.Type.config = 0

    # name
    self.obj168.name.setValue('false')

    self.obj168.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,120.0,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=Constant(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    # Type
    self.obj169.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj169.Type.config = 0

    # name
    self.obj169.name.setValue('procdef')

    self.obj169.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(740.0,400.0,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=paired_with(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    self.obj170.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(160.5,182.0,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj171=match_contains(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    self.obj171.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(324.0,87.0,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=apply_contains(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(False)

    self.obj172.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(296.5,310.0,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=apply_contains(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(False)

    self.obj173.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(393.5,267.0,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=directLink_T(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    # associationType
    self.obj174.associationType.setValue('p')

    self.obj174.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.0,328.0,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=backward_link(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    # type
    self.obj175.type.setValue('ruleDef')

    self.obj175.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(411.0,207.0,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=hasAttribute_S(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    self.obj176.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(463.0,80.5,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    self.obj177=hasAttribute_S(self)
    self.obj177.isGraphObjectVisual = True

    if(hasattr(self.obj177, '_setHierarchicalLink')):
      self.obj177._setHierarchicalLink(False)

    self.obj177.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(470.0,124.5,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)
    self.obj177.postAction( rootNode.CREATE )

    self.obj178=hasAttribute_T(self)
    self.obj178.isGraphObjectVisual = True

    if(hasattr(self.obj178, '_setHierarchicalLink')):
      self.obj178._setHierarchicalLink(False)

    self.obj178.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(423.0,362.5,self.obj178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj178)
    self.globalAndLocalPostcondition(self.obj178, rootNode)
    self.obj178.postAction( rootNode.CREATE )

    self.obj179=leftExpr(self)
    self.obj179.isGraphObjectVisual = True

    if(hasattr(self.obj179, '_setHierarchicalLink')):
      self.obj179._setHierarchicalLink(False)

    self.obj179.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(676.0,56.5,self.obj179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj179)
    self.globalAndLocalPostcondition(self.obj179, rootNode)
    self.obj179.postAction( rootNode.CREATE )

    self.obj180=leftExpr(self)
    self.obj180.isGraphObjectVisual = True

    if(hasattr(self.obj180, '_setHierarchicalLink')):
      self.obj180._setHierarchicalLink(False)

    self.obj180.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(686.0,156.5,self.obj180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj180)
    self.globalAndLocalPostcondition(self.obj180, rootNode)
    self.obj180.postAction( rootNode.CREATE )

    self.obj181=leftExpr(self)
    self.obj181.isGraphObjectVisual = True

    if(hasattr(self.obj181, '_setHierarchicalLink')):
      self.obj181._setHierarchicalLink(False)

    self.obj181.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(536.0,426.5,self.obj181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj181)
    self.globalAndLocalPostcondition(self.obj181, rootNode)
    self.obj181.postAction( rootNode.CREATE )

    self.obj182=rightExpr(self)
    self.obj182.isGraphObjectVisual = True

    if(hasattr(self.obj182, '_setHierarchicalLink')):
      self.obj182._setHierarchicalLink(False)

    self.obj182.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(856.0,156.5,self.obj182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj182)
    self.globalAndLocalPostcondition(self.obj182, rootNode)
    self.obj182.postAction( rootNode.CREATE )

    self.obj183=rightExpr(self)
    self.obj183.isGraphObjectVisual = True

    if(hasattr(self.obj183, '_setHierarchicalLink')):
      self.obj183._setHierarchicalLink(False)

    self.obj183.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(856.0,56.5,self.obj183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj183)
    self.globalAndLocalPostcondition(self.obj183, rootNode)
    self.obj183.postAction( rootNode.CREATE )

    self.obj184=rightExpr(self)
    self.obj184.isGraphObjectVisual = True

    if(hasattr(self.obj184, '_setHierarchicalLink')):
      self.obj184._setHierarchicalLink(False)

    self.obj184.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(756.0,436.5,self.obj184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj184)
    self.globalAndLocalPostcondition(self.obj184, rootNode)
    self.obj184.postAction( rootNode.CREATE )

    # Connections for obj156 (graphObject_: Obj53) of type MatchModel
    self.drawConnections(
(self.obj156,self.obj170,[158.0, 71.0, 160.5, 182.0],"true", 2),
(self.obj156,self.obj171,[158.0, 71.0, 324.0, 87.0],"true", 2) )
    # Connections for obj157 (graphObject_: Obj54) of type ApplyModel
    self.drawConnections(
(self.obj157,self.obj172,[163.0, 293.0, 296.5, 310.0],"true", 2),
(self.obj157,self.obj173,[163.0, 293.0, 393.5, 267.0],"true", 2) )
    # Connections for obj158 (graphObject_: Obj55) named state1
    self.drawConnections(
(self.obj158,self.obj176,[410.0, 103.0, 463.0, 80.5],"true", 2),
(self.obj158,self.obj177,[410.0, 103.0, 470.0, 124.5],"true", 2) )
    # Connections for obj159 (graphObject_: Obj56) named procdef1
    self.drawConnections(
(self.obj159,self.obj174,[412.0, 311.0, 452.0, 328.0],"true", 2),
(self.obj159,self.obj175,[412.0, 311.0, 411.0, 207.0],"true", 2),
(self.obj159,self.obj178,[412.0, 311.0, 423.0, 362.5],"true", 2) )
    # Connections for obj160 (graphObject_: Obj57) named null1
    self.drawConnections(
 )
    # Connections for obj161 (graphObject_: Obj58) named isComposite
    self.drawConnections(
 )
    # Connections for obj162 (graphObject_: Obj59) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj163 (graphObject_: Obj60) named pivot
    self.drawConnections(
 )
    # Connections for obj164 (graphObject_: Obj61) named eq1
    self.drawConnections(
(self.obj164,self.obj183,[778.0, 59.0, 856.0, 56.5],"true", 2),
(self.obj164,self.obj179,[778.0, 59.0, 676.0, 56.5],"true", 2) )
    # Connections for obj165 (graphObject_: Obj62) named eq2
    self.drawConnections(
(self.obj165,self.obj182,[778.0, 159.0, 856.0, 156.5],"true", 2),
(self.obj165,self.obj180,[778.0, 159.0, 686.0, 156.5],"true", 2) )
    # Connections for obj166 (graphObject_: Obj63) named eq3
    self.drawConnections(
(self.obj166,self.obj181,[638.0, 439.0, 536.0, 426.5],"true", 2),
(self.obj166,self.obj184,[638.0, 439.0, 756.0, 436.5],"true", 2) )
    # Connections for obj167 (graphObject_: Obj64) named false
    self.drawConnections(
 )
    # Connections for obj168 (graphObject_: Obj65) named false
    self.drawConnections(
 )
    # Connections for obj169 (graphObject_: Obj66) named procdef
    self.drawConnections(
 )
    # Connections for obj170 (graphObject_: Obj67) of type paired_with
    self.drawConnections(
(self.obj170,self.obj157,[160.5, 182.0, 163.0, 293.0],"true", 2) )
    # Connections for obj171 (graphObject_: Obj68) of type match_contains
    self.drawConnections(
(self.obj171,self.obj158,[324.0, 87.0, 410.0, 103.0],"true", 2) )
    # Connections for obj172 (graphObject_: Obj69) of type apply_contains
    self.drawConnections(
(self.obj172,self.obj159,[296.5, 310.0, 412.0, 311.0],"true", 2) )
    # Connections for obj173 (graphObject_: Obj70) of type apply_contains
    self.drawConnections(
(self.obj173,self.obj160,[393.5, 267.0, 632.0, 311.0],"true", 2) )
    # Connections for obj174 (graphObject_: Obj71) of type directLink_T
    self.drawConnections(
(self.obj174,self.obj160,[660.0, 348.0, 632.0, 311.0],"true", 2) )
    # Connections for obj175 (graphObject_: Obj72) of type backward_link
    self.drawConnections(
(self.obj175,self.obj158,[411.0, 207.0, 410.0, 103.0],"true", 2) )
    # Connections for obj176 (graphObject_: Obj73) of type hasAttribute_S
    self.drawConnections(
(self.obj176,self.obj161,[463.0, 80.5, 574.0, 54.0],"true", 2) )
    # Connections for obj177 (graphObject_: Obj74) of type hasAttribute_S
    self.drawConnections(
(self.obj177,self.obj162,[470.0, 124.5, 618.0, 154.0],"true", 2) )
    # Connections for obj178 (graphObject_: Obj75) of type hasAttribute_T
    self.drawConnections(
(self.obj178,self.obj163,[423.0, 362.5, 434.0, 414.0],"true", 2) )
    # Connections for obj179 (graphObject_: Obj76) of type leftExpr
    self.drawConnections(
(self.obj179,self.obj161,[676.0, 56.5, 574.0, 54.0],"true", 2) )
    # Connections for obj180 (graphObject_: Obj77) of type leftExpr
    self.drawConnections(
(self.obj180,self.obj162,[686.0, 156.5, 618.0, 154.0],"true", 2) )
    # Connections for obj181 (graphObject_: Obj78) of type leftExpr
    self.drawConnections(
(self.obj181,self.obj163,[536.0, 426.5, 434.0, 414.0],"true", 2) )
    # Connections for obj182 (graphObject_: Obj79) of type rightExpr
    self.drawConnections(
(self.obj182,self.obj168,[856.0, 156.5, 934.0, 154.0],"true", 2) )
    # Connections for obj183 (graphObject_: Obj80) of type rightExpr
    self.drawConnections(
(self.obj183,self.obj167,[856.0, 56.5, 934.0, 54.0],"true", 2) )
    # Connections for obj184 (graphObject_: Obj81) of type rightExpr
    self.drawConnections(
(self.obj184,self.obj169,[756.0, 436.5, 874.0, 434.0],"true", 2) )

newfunction = BasicStateNoOutgoing2ProcDef_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
