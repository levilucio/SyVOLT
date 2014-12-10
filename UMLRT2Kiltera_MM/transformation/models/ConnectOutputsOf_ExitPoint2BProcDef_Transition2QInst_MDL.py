"""
__ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 10:48:11 2014
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

def ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst')
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
       new_obj = graph_ApplyModel(20.0,200.0,self.obj101)
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

    self.obj103=ExitPoint(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('exitpoint1')

    # classtype
    self.obj103.classtype.setValue('ExitPoint')

    # cardinality
    self.obj103.cardinality.setValue('+')

    self.obj103.graphClass_= graph_ExitPoint
    if self.genGraphics:
       new_obj = graph_ExitPoint(180.0,80.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExitPoint", new_obj.tag)
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
    self.obj104.cardinality.setValue('1')

    self.obj104.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,80.0,self.obj104)
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

    self.obj114=Par(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # classtype
    self.obj114.classtype.setValue('Par')

    # cardinality
    self.obj114.cardinality.setValue('1')

    # name
    self.obj114.name.setValue('par1')

    self.obj114.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(180.0,240.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Inst(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # classtype
    self.obj115.classtype.setValue('Inst')

    # cardinality
    self.obj115.cardinality.setValue('1')

    # name
    self.obj115.name.setValue('inst1')

    self.obj115.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(420.0,240.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj135=Attribute(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # Type
    self.obj135.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj135.Type.config = 0

    # name
    self.obj135.name.setValue('pivotin')

    self.obj135.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(100.0,340.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj141=Attribute(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    # Type
    self.obj141.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj141.Type.config = 0

    # name
    self.obj141.name.setValue('pivotin')

    self.obj141.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,340.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj132=Equation(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # name
    self.obj132.name.setValue('eq1')

    self.obj132.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,420.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj144=Equation(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    # name
    self.obj144.name.setValue('eq2')

    self.obj144.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(480.0,420.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj129=Constant(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # Type
    self.obj129.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj129.Type.config = 0

    # name
    self.obj129.name.setValue('parexitpoint')

    self.obj129.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(280.0,340.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj147=Constant(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    # Type
    self.obj147.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj147.Type.config = 0

    # name
    self.obj147.name.setValue('instfortrans')

    self.obj147.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,340.0,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj102=paired_with(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    self.obj102.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,202.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj105=match_contains(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    self.obj105.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,87.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=match_contains(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    self.obj106.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,87.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj125=apply_contains(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    self.obj125.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,262.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=apply_contains(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    self.obj126.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(367.5,262.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj120=directLink_T(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # associationType
    self.obj120.associationType.setValue('p')

    self.obj120.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(472.0,291.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj111=directLink_S(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # associationType
    self.obj111.associationType.setValue('outgoingTransitions')

    self.obj111.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,123.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj153=backward_link(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    # type
    self.obj153.type.setValue('ruleDef')

    self.obj153.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,207.0,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=backward_link(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # type
    self.obj154.type.setValue('ruleDef')

    self.obj154.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(581.0,207.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj138=hasAttribute_T(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    self.obj138.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(264.0,330.5,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj150=hasAttribute_T(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    self.obj150.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(583.0,332.5,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj139=leftExpr(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    self.obj139.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(277.0,418.5,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj151=leftExpr(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    self.obj151.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(596.0,416.5,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj140=rightExpr(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    self.obj140.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(396.0,416.5,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj152=rightExpr(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    self.obj152.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(676.0,416.5,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj102,[138.0, 51.0, 140.5, 202.0],"true", 2),
(self.obj100,self.obj105,[138.0, 51.0, 244.0, 87.0],"true", 0),
(self.obj100,self.obj106,[138.0, 51.0, 354.0, 87.0],"true", 0) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj125,[143.0, 233.0, 247.5, 262.0],"true", 0),
(self.obj101,self.obj126,[143.0, 233.0, 367.5, 262.0],"true", 0) )
    # Connections for obj103 (graphObject_: Obj3) named exitpoint1
    self.drawConnections(
(self.obj103,self.obj111,[350.0, 123.0, 460.0, 123.0],"true", 2) )
    # Connections for obj104 (graphObject_: Obj4) named transition1
    self.drawConnections(
 )
    # Connections for obj114 (graphObject_: Obj8) named par1
    self.drawConnections(
(self.obj114,self.obj120,[352.0, 291.0, 472.0, 291.0],"true", 2),
(self.obj114,self.obj138,[352.0, 291.0, 264.0, 330.5],"true", 2),
(self.obj114,self.obj153,[352.0, 291.0, 351.0, 207.0],"true", 2) )
    # Connections for obj115 (graphObject_: Obj9) named inst1
    self.drawConnections(
(self.obj115,self.obj150,[592.0, 291.0, 583.0, 332.5],"true", 2),
(self.obj115,self.obj154,[592.0, 291.0, 581.0, 207.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj15) named pivotin
    self.drawConnections(
 )
    # Connections for obj141 (graphObject_: Obj19) named pivotin
    self.drawConnections(
 )
    # Connections for obj132 (graphObject_: Obj14) named eq1
    self.drawConnections(
(self.obj132,self.obj139,[358.0, 459.0, 277.0, 418.5],"true", 2),
(self.obj132,self.obj140,[358.0, 459.0, 396.0, 416.5],"true", 2) )
    # Connections for obj144 (graphObject_: Obj20) named eq2
    self.drawConnections(
(self.obj144,self.obj151,[618.0, 459.0, 596.0, 416.5],"true", 2),
(self.obj144,self.obj152,[618.0, 459.0, 676.0, 416.5],"true", 2) )
    # Connections for obj129 (graphObject_: Obj13) named parexitpoint
    self.drawConnections(
 )
    # Connections for obj147 (graphObject_: Obj21) named instfortrans
    self.drawConnections(
 )
    # Connections for obj102 (graphObject_: Obj2) of type paired_with
    self.drawConnections(
(self.obj102,self.obj101,[140.5, 202.0, 143.0, 233.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) of type match_contains
    self.drawConnections(
(self.obj105,self.obj103,[244.0, 87.0, 350.0, 123.0],"true", 2) )
    # Connections for obj106 (graphObject_: Obj6) of type match_contains
    self.drawConnections(
(self.obj106,self.obj104,[354.0, 87.0, 570.0, 123.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj11) of type apply_contains
    self.drawConnections(
(self.obj125,self.obj114,[247.5, 262.0, 352.0, 291.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj12) of type apply_contains
    self.drawConnections(
(self.obj126,self.obj115,[367.5, 262.0, 592.0, 291.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj10) of type directLink_T
    self.drawConnections(
(self.obj120,self.obj115,[472.0, 291.0, 592.0, 291.0],"true", 2) )
    # Connections for obj111 (graphObject_: Obj7) of type directLink_S
    self.drawConnections(
(self.obj111,self.obj104,[460.0, 123.0, 570.0, 123.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj25) of type backward_link
    self.drawConnections(
(self.obj153,self.obj103,[351.0, 207.0, 350.0, 123.0],"true", 2) )
    # Connections for obj154 (graphObject_: Obj26) of type backward_link
    self.drawConnections(
(self.obj154,self.obj104,[581.0, 207.0, 570.0, 123.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj16) of type hasAttribute_T
    self.drawConnections(
(self.obj138,self.obj135,[264.0, 330.5, 234.0, 374.0],"true", 2) )
    # Connections for obj150 (graphObject_: Obj22) of type hasAttribute_T
    self.drawConnections(
(self.obj150,self.obj141,[583.0, 332.5, 574.0, 374.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj17) of type leftExpr
    self.drawConnections(
(self.obj139,self.obj135,[277.0, 418.5, 234.0, 374.0],"true", 2) )
    # Connections for obj151 (graphObject_: Obj23) of type leftExpr
    self.drawConnections(
(self.obj151,self.obj141,[596.0, 416.5, 574.0, 374.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj18) of type rightExpr
    self.drawConnections(
(self.obj140,self.obj129,[396.0, 416.5, 414.0, 374.0],"true", 2) )
    # Connections for obj152 (graphObject_: Obj24) of type rightExpr
    self.drawConnections(
(self.obj152,self.obj147,[676.0, 416.5, 734.0, 374.0],"true", 2) )

newfunction = ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
