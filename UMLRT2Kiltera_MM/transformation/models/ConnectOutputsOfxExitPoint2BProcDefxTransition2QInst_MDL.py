"""
__ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 13:58:59 2015
__________________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ExitPoint import *
from Transition import *
from Par import *
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
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from graph_Par import *
from graph_ExitPoint import *
from graph_Equation import *
from graph_hasAttribute_T import *
from graph_Attribute import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_match_contains import *
from graph_leftExpr import *
from graph_Transition import *
from graph_ApplyModel import *
from graph_Inst import *
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

def ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst')
    # --- ASG attributes over ---


    self.obj421=MatchModel(self)
    self.obj421.isGraphObjectVisual = True

    if(hasattr(self.obj421, '_setHierarchicalLink')):
      self.obj421._setHierarchicalLink(False)

    self.obj421.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj421)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj421.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj421)
    self.globalAndLocalPostcondition(self.obj421, rootNode)
    self.obj421.postAction( rootNode.CREATE )

    self.obj422=ApplyModel(self)
    self.obj422.isGraphObjectVisual = True

    if(hasattr(self.obj422, '_setHierarchicalLink')):
      self.obj422._setHierarchicalLink(False)

    self.obj422.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,200.0,self.obj422)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj422.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj422)
    self.globalAndLocalPostcondition(self.obj422, rootNode)
    self.obj422.postAction( rootNode.CREATE )

    self.obj423=ExitPoint(self)
    self.obj423.isGraphObjectVisual = True

    if(hasattr(self.obj423, '_setHierarchicalLink')):
      self.obj423._setHierarchicalLink(False)

    # name
    self.obj423.name.setValue('exitpoint1')

    # classtype
    self.obj423.classtype.setValue('ExitPoint')

    # cardinality
    self.obj423.cardinality.setValue('+')

    self.obj423.graphClass_= graph_ExitPoint
    if self.genGraphics:
       new_obj = graph_ExitPoint(180.0,80.0,self.obj423)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj423.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj423)
    self.globalAndLocalPostcondition(self.obj423, rootNode)
    self.obj423.postAction( rootNode.CREATE )

    self.obj424=Transition(self)
    self.obj424.isGraphObjectVisual = True

    if(hasattr(self.obj424, '_setHierarchicalLink')):
      self.obj424._setHierarchicalLink(False)

    # name
    self.obj424.name.setValue('transition1')

    # classtype
    self.obj424.classtype.setValue('Transition')

    # cardinality
    self.obj424.cardinality.setValue('1')

    self.obj424.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,80.0,self.obj424)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj424.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj424)
    self.globalAndLocalPostcondition(self.obj424, rootNode)
    self.obj424.postAction( rootNode.CREATE )

    self.obj425=Par(self)
    self.obj425.isGraphObjectVisual = True

    if(hasattr(self.obj425, '_setHierarchicalLink')):
      self.obj425._setHierarchicalLink(False)

    # classtype
    self.obj425.classtype.setValue('Par')

    # cardinality
    self.obj425.cardinality.setValue('1')

    # name
    self.obj425.name.setValue('par1')

    self.obj425.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(180.0,240.0,self.obj425)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj425.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj425)
    self.globalAndLocalPostcondition(self.obj425, rootNode)
    self.obj425.postAction( rootNode.CREATE )

    self.obj426=Inst(self)
    self.obj426.isGraphObjectVisual = True

    if(hasattr(self.obj426, '_setHierarchicalLink')):
      self.obj426._setHierarchicalLink(False)

    # classtype
    self.obj426.classtype.setValue('Inst')

    # cardinality
    self.obj426.cardinality.setValue('1')

    # name
    self.obj426.name.setValue('inst1')

    self.obj426.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(420.0,240.0,self.obj426)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj426.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj426)
    self.globalAndLocalPostcondition(self.obj426, rootNode)
    self.obj426.postAction( rootNode.CREATE )

    self.obj427=Attribute(self)
    self.obj427.isGraphObjectVisual = True

    if(hasattr(self.obj427, '_setHierarchicalLink')):
      self.obj427._setHierarchicalLink(False)

    # Type
    self.obj427.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj427.Type.config = 0

    # name
    self.obj427.name.setValue('pivot')

    self.obj427.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(100.0,340.0,self.obj427)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj427.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj427)
    self.globalAndLocalPostcondition(self.obj427, rootNode)
    self.obj427.postAction( rootNode.CREATE )

    self.obj428=Attribute(self)
    self.obj428.isGraphObjectVisual = True

    if(hasattr(self.obj428, '_setHierarchicalLink')):
      self.obj428._setHierarchicalLink(False)

    # Type
    self.obj428.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj428.Type.config = 0

    # name
    self.obj428.name.setValue('pivot')

    self.obj428.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,340.0,self.obj428)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj428.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj428)
    self.globalAndLocalPostcondition(self.obj428, rootNode)
    self.obj428.postAction( rootNode.CREATE )

    self.obj429=Equation(self)
    self.obj429.isGraphObjectVisual = True

    if(hasattr(self.obj429, '_setHierarchicalLink')):
      self.obj429._setHierarchicalLink(False)

    # name
    self.obj429.name.setValue('eq1')

    self.obj429.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,420.0,self.obj429)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj429.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj429)
    self.globalAndLocalPostcondition(self.obj429, rootNode)
    self.obj429.postAction( rootNode.CREATE )

    self.obj430=Equation(self)
    self.obj430.isGraphObjectVisual = True

    if(hasattr(self.obj430, '_setHierarchicalLink')):
      self.obj430._setHierarchicalLink(False)

    # name
    self.obj430.name.setValue('eq2')

    self.obj430.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(480.0,420.0,self.obj430)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj430.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj430)
    self.globalAndLocalPostcondition(self.obj430, rootNode)
    self.obj430.postAction( rootNode.CREATE )

    self.obj431=Constant(self)
    self.obj431.isGraphObjectVisual = True

    if(hasattr(self.obj431, '_setHierarchicalLink')):
      self.obj431._setHierarchicalLink(False)

    # Type
    self.obj431.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj431.Type.config = 0

    # name
    self.obj431.name.setValue('parexitpoint')

    self.obj431.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(280.0,340.0,self.obj431)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj431.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj431)
    self.globalAndLocalPostcondition(self.obj431, rootNode)
    self.obj431.postAction( rootNode.CREATE )

    self.obj432=Constant(self)
    self.obj432.isGraphObjectVisual = True

    if(hasattr(self.obj432, '_setHierarchicalLink')):
      self.obj432._setHierarchicalLink(False)

    # Type
    self.obj432.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj432.Type.config = 0

    # name
    self.obj432.name.setValue('instfortrans')

    self.obj432.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,340.0,self.obj432)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj432.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj432)
    self.globalAndLocalPostcondition(self.obj432, rootNode)
    self.obj432.postAction( rootNode.CREATE )

    self.obj433=paired_with(self)
    self.obj433.isGraphObjectVisual = True

    if(hasattr(self.obj433, '_setHierarchicalLink')):
      self.obj433._setHierarchicalLink(False)

    self.obj433.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,202.0,self.obj433)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj433.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj433)
    self.globalAndLocalPostcondition(self.obj433, rootNode)
    self.obj433.postAction( rootNode.CREATE )

    self.obj434=match_contains(self)
    self.obj434.isGraphObjectVisual = True

    if(hasattr(self.obj434, '_setHierarchicalLink')):
      self.obj434._setHierarchicalLink(False)

    self.obj434.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,87.0,self.obj434)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj434.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj434)
    self.globalAndLocalPostcondition(self.obj434, rootNode)
    self.obj434.postAction( rootNode.CREATE )

    self.obj435=match_contains(self)
    self.obj435.isGraphObjectVisual = True

    if(hasattr(self.obj435, '_setHierarchicalLink')):
      self.obj435._setHierarchicalLink(False)

    self.obj435.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,87.0,self.obj435)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj435.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj435)
    self.globalAndLocalPostcondition(self.obj435, rootNode)
    self.obj435.postAction( rootNode.CREATE )

    self.obj436=apply_contains(self)
    self.obj436.isGraphObjectVisual = True

    if(hasattr(self.obj436, '_setHierarchicalLink')):
      self.obj436._setHierarchicalLink(False)

    self.obj436.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,262.0,self.obj436)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj436.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj436)
    self.globalAndLocalPostcondition(self.obj436, rootNode)
    self.obj436.postAction( rootNode.CREATE )

    self.obj437=apply_contains(self)
    self.obj437.isGraphObjectVisual = True

    if(hasattr(self.obj437, '_setHierarchicalLink')):
      self.obj437._setHierarchicalLink(False)

    self.obj437.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(367.5,262.0,self.obj437)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj437.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj437)
    self.globalAndLocalPostcondition(self.obj437, rootNode)
    self.obj437.postAction( rootNode.CREATE )

    self.obj438=directLink_T(self)
    self.obj438.isGraphObjectVisual = True

    if(hasattr(self.obj438, '_setHierarchicalLink')):
      self.obj438._setHierarchicalLink(False)

    # associationType
    self.obj438.associationType.setValue('p')

    self.obj438.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(472.0,291.0,self.obj438)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj438.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj438)
    self.globalAndLocalPostcondition(self.obj438, rootNode)
    self.obj438.postAction( rootNode.CREATE )

    self.obj439=directLink_S(self)
    self.obj439.isGraphObjectVisual = True

    if(hasattr(self.obj439, '_setHierarchicalLink')):
      self.obj439._setHierarchicalLink(False)

    # associationType
    self.obj439.associationType.setValue('outgoingTransitions')

    self.obj439.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,123.0,self.obj439)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj439.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj439)
    self.globalAndLocalPostcondition(self.obj439, rootNode)
    self.obj439.postAction( rootNode.CREATE )

    self.obj440=backward_link(self)
    self.obj440.isGraphObjectVisual = True

    if(hasattr(self.obj440, '_setHierarchicalLink')):
      self.obj440._setHierarchicalLink(False)

    # type
    self.obj440.type.setValue('ruleDef')

    self.obj440.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,207.0,self.obj440)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj440.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj440)
    self.globalAndLocalPostcondition(self.obj440, rootNode)
    self.obj440.postAction( rootNode.CREATE )

    self.obj441=backward_link(self)
    self.obj441.isGraphObjectVisual = True

    if(hasattr(self.obj441, '_setHierarchicalLink')):
      self.obj441._setHierarchicalLink(False)

    # type
    self.obj441.type.setValue('ruleDef')

    self.obj441.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(581.0,207.0,self.obj441)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj441.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj441)
    self.globalAndLocalPostcondition(self.obj441, rootNode)
    self.obj441.postAction( rootNode.CREATE )

    self.obj442=hasAttribute_T(self)
    self.obj442.isGraphObjectVisual = True

    if(hasattr(self.obj442, '_setHierarchicalLink')):
      self.obj442._setHierarchicalLink(False)

    self.obj442.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(264.0,330.5,self.obj442)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj442.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj442)
    self.globalAndLocalPostcondition(self.obj442, rootNode)
    self.obj442.postAction( rootNode.CREATE )

    self.obj443=hasAttribute_T(self)
    self.obj443.isGraphObjectVisual = True

    if(hasattr(self.obj443, '_setHierarchicalLink')):
      self.obj443._setHierarchicalLink(False)

    self.obj443.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(583.0,332.5,self.obj443)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj443.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj443)
    self.globalAndLocalPostcondition(self.obj443, rootNode)
    self.obj443.postAction( rootNode.CREATE )

    self.obj444=leftExpr(self)
    self.obj444.isGraphObjectVisual = True

    if(hasattr(self.obj444, '_setHierarchicalLink')):
      self.obj444._setHierarchicalLink(False)

    self.obj444.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(277.0,418.5,self.obj444)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj444.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj444)
    self.globalAndLocalPostcondition(self.obj444, rootNode)
    self.obj444.postAction( rootNode.CREATE )

    self.obj445=leftExpr(self)
    self.obj445.isGraphObjectVisual = True

    if(hasattr(self.obj445, '_setHierarchicalLink')):
      self.obj445._setHierarchicalLink(False)

    self.obj445.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(596.0,416.5,self.obj445)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj445.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj445)
    self.globalAndLocalPostcondition(self.obj445, rootNode)
    self.obj445.postAction( rootNode.CREATE )

    self.obj446=rightExpr(self)
    self.obj446.isGraphObjectVisual = True

    if(hasattr(self.obj446, '_setHierarchicalLink')):
      self.obj446._setHierarchicalLink(False)

    self.obj446.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(396.0,416.5,self.obj446)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj446.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj446)
    self.globalAndLocalPostcondition(self.obj446, rootNode)
    self.obj446.postAction( rootNode.CREATE )

    self.obj447=rightExpr(self)
    self.obj447.isGraphObjectVisual = True

    if(hasattr(self.obj447, '_setHierarchicalLink')):
      self.obj447._setHierarchicalLink(False)

    self.obj447.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(676.0,416.5,self.obj447)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj447.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj447)
    self.globalAndLocalPostcondition(self.obj447, rootNode)
    self.obj447.postAction( rootNode.CREATE )

    # Connections for obj421 (graphObject_: Obj292) of type MatchModel
    self.drawConnections(
(self.obj421,self.obj433,[138.0, 51.0, 140.5, 202.0],"true", 2),
(self.obj421,self.obj434,[138.0, 51.0, 244.0, 87.0],"true", 2),
(self.obj421,self.obj435,[138.0, 51.0, 354.0, 87.0],"true", 2) )
    # Connections for obj422 (graphObject_: Obj293) of type ApplyModel
    self.drawConnections(
(self.obj422,self.obj436,[143.0, 233.0, 247.5, 262.0],"true", 2),
(self.obj422,self.obj437,[143.0, 233.0, 367.5, 262.0],"true", 2) )
    # Connections for obj423 (graphObject_: Obj294) named exitpoint1
    self.drawConnections(
(self.obj423,self.obj439,[350.0, 123.0, 460.0, 123.0],"true", 2) )
    # Connections for obj424 (graphObject_: Obj295) named transition1
    self.drawConnections(
 )
    # Connections for obj425 (graphObject_: Obj296) named par1
    self.drawConnections(
(self.obj425,self.obj438,[352.0, 291.0, 472.0, 291.0],"true", 2),
(self.obj425,self.obj442,[352.0, 291.0, 264.0, 330.5],"true", 2),
(self.obj425,self.obj440,[352.0, 291.0, 351.0, 207.0],"true", 2) )
    # Connections for obj426 (graphObject_: Obj297) named inst1
    self.drawConnections(
(self.obj426,self.obj443,[592.0, 291.0, 583.0, 332.5],"true", 2),
(self.obj426,self.obj441,[592.0, 291.0, 581.0, 207.0],"true", 2) )
    # Connections for obj427 (graphObject_: Obj298) named pivot
    self.drawConnections(
 )
    # Connections for obj428 (graphObject_: Obj299) named pivot
    self.drawConnections(
 )
    # Connections for obj429 (graphObject_: Obj300) named eq1
    self.drawConnections(
(self.obj429,self.obj444,[358.0, 459.0, 277.0, 418.5],"true", 2),
(self.obj429,self.obj446,[358.0, 459.0, 396.0, 416.5],"true", 2) )
    # Connections for obj430 (graphObject_: Obj301) named eq2
    self.drawConnections(
(self.obj430,self.obj445,[618.0, 459.0, 596.0, 416.5],"true", 2),
(self.obj430,self.obj447,[618.0, 459.0, 676.0, 416.5],"true", 2) )
    # Connections for obj431 (graphObject_: Obj302) named parexitpoint
    self.drawConnections(
 )
    # Connections for obj432 (graphObject_: Obj303) named instfortrans
    self.drawConnections(
 )
    # Connections for obj433 (graphObject_: Obj304) of type paired_with
    self.drawConnections(
(self.obj433,self.obj422,[140.5, 202.0, 143.0, 233.0],"true", 2) )
    # Connections for obj434 (graphObject_: Obj305) of type match_contains
    self.drawConnections(
(self.obj434,self.obj423,[244.0, 87.0, 350.0, 123.0],"true", 2) )
    # Connections for obj435 (graphObject_: Obj306) of type match_contains
    self.drawConnections(
(self.obj435,self.obj424,[354.0, 87.0, 570.0, 123.0],"true", 2) )
    # Connections for obj436 (graphObject_: Obj307) of type apply_contains
    self.drawConnections(
(self.obj436,self.obj425,[247.5, 262.0, 352.0, 291.0],"true", 2) )
    # Connections for obj437 (graphObject_: Obj308) of type apply_contains
    self.drawConnections(
(self.obj437,self.obj426,[367.5, 262.0, 592.0, 291.0],"true", 2) )
    # Connections for obj438 (graphObject_: Obj309) of type directLink_T
    self.drawConnections(
(self.obj438,self.obj426,[472.0, 291.0, 592.0, 291.0],"true", 2) )
    # Connections for obj439 (graphObject_: Obj310) of type directLink_S
    self.drawConnections(
(self.obj439,self.obj424,[460.0, 123.0, 570.0, 123.0],"true", 2) )
    # Connections for obj440 (graphObject_: Obj311) of type backward_link
    self.drawConnections(
(self.obj440,self.obj423,[351.0, 207.0, 350.0, 123.0],"true", 2) )
    # Connections for obj441 (graphObject_: Obj312) of type backward_link
    self.drawConnections(
(self.obj441,self.obj424,[581.0, 207.0, 570.0, 123.0],"true", 2) )
    # Connections for obj442 (graphObject_: Obj313) of type hasAttribute_T
    self.drawConnections(
(self.obj442,self.obj427,[264.0, 330.5, 234.0, 374.0],"true", 2) )
    # Connections for obj443 (graphObject_: Obj314) of type hasAttribute_T
    self.drawConnections(
(self.obj443,self.obj428,[583.0, 332.5, 574.0, 374.0],"true", 2) )
    # Connections for obj444 (graphObject_: Obj315) of type leftExpr
    self.drawConnections(
(self.obj444,self.obj427,[277.0, 418.5, 234.0, 374.0],"true", 2) )
    # Connections for obj445 (graphObject_: Obj316) of type leftExpr
    self.drawConnections(
(self.obj445,self.obj428,[596.0, 416.5, 574.0, 374.0],"true", 2) )
    # Connections for obj446 (graphObject_: Obj317) of type rightExpr
    self.drawConnections(
(self.obj446,self.obj431,[396.0, 416.5, 414.0, 374.0],"true", 2) )
    # Connections for obj447 (graphObject_: Obj318) of type rightExpr
    self.drawConnections(
(self.obj447,self.obj432,[676.0, 416.5, 734.0, 374.0],"true", 2) )

newfunction = ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
