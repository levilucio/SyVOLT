"""
__ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:57:09 2015
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


    self.obj395=MatchModel(self)
    self.obj395.isGraphObjectVisual = True

    if(hasattr(self.obj395, '_setHierarchicalLink')):
      self.obj395._setHierarchicalLink(False)

    self.obj395.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj395)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj395.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj395)
    self.globalAndLocalPostcondition(self.obj395, rootNode)
    self.obj395.postAction( rootNode.CREATE )

    self.obj396=ApplyModel(self)
    self.obj396.isGraphObjectVisual = True

    if(hasattr(self.obj396, '_setHierarchicalLink')):
      self.obj396._setHierarchicalLink(False)

    self.obj396.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,200.0,self.obj396)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj396.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj396)
    self.globalAndLocalPostcondition(self.obj396, rootNode)
    self.obj396.postAction( rootNode.CREATE )

    self.obj397=ExitPoint(self)
    self.obj397.isGraphObjectVisual = True

    if(hasattr(self.obj397, '_setHierarchicalLink')):
      self.obj397._setHierarchicalLink(False)

    # name
    self.obj397.name.setValue('exitpoint1')

    # classtype
    self.obj397.classtype.setValue('ExitPoint')

    # cardinality
    self.obj397.cardinality.setValue('+')

    self.obj397.graphClass_= graph_ExitPoint
    if self.genGraphics:
       new_obj = graph_ExitPoint(180.0,80.0,self.obj397)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj397.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj397)
    self.globalAndLocalPostcondition(self.obj397, rootNode)
    self.obj397.postAction( rootNode.CREATE )

    self.obj398=Transition(self)
    self.obj398.isGraphObjectVisual = True

    if(hasattr(self.obj398, '_setHierarchicalLink')):
      self.obj398._setHierarchicalLink(False)

    # name
    self.obj398.name.setValue('transition1')

    # classtype
    self.obj398.classtype.setValue('Transition')

    # cardinality
    self.obj398.cardinality.setValue('1')

    self.obj398.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,80.0,self.obj398)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj398.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj398)
    self.globalAndLocalPostcondition(self.obj398, rootNode)
    self.obj398.postAction( rootNode.CREATE )

    self.obj399=Par(self)
    self.obj399.isGraphObjectVisual = True

    if(hasattr(self.obj399, '_setHierarchicalLink')):
      self.obj399._setHierarchicalLink(False)

    # classtype
    self.obj399.classtype.setValue('Par')

    # cardinality
    self.obj399.cardinality.setValue('1')

    # name
    self.obj399.name.setValue('par1')

    self.obj399.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(180.0,240.0,self.obj399)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj399.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj399)
    self.globalAndLocalPostcondition(self.obj399, rootNode)
    self.obj399.postAction( rootNode.CREATE )

    self.obj400=Inst(self)
    self.obj400.isGraphObjectVisual = True

    if(hasattr(self.obj400, '_setHierarchicalLink')):
      self.obj400._setHierarchicalLink(False)

    # classtype
    self.obj400.classtype.setValue('Inst')

    # cardinality
    self.obj400.cardinality.setValue('1')

    # name
    self.obj400.name.setValue('inst1')

    self.obj400.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(420.0,240.0,self.obj400)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj400.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj400)
    self.globalAndLocalPostcondition(self.obj400, rootNode)
    self.obj400.postAction( rootNode.CREATE )

    self.obj401=Attribute(self)
    self.obj401.isGraphObjectVisual = True

    if(hasattr(self.obj401, '_setHierarchicalLink')):
      self.obj401._setHierarchicalLink(False)

    # Type
    self.obj401.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj401.Type.config = 0

    # name
    self.obj401.name.setValue('pivot')

    self.obj401.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(100.0,340.0,self.obj401)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj401.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj401)
    self.globalAndLocalPostcondition(self.obj401, rootNode)
    self.obj401.postAction( rootNode.CREATE )

    self.obj402=Attribute(self)
    self.obj402.isGraphObjectVisual = True

    if(hasattr(self.obj402, '_setHierarchicalLink')):
      self.obj402._setHierarchicalLink(False)

    # Type
    self.obj402.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj402.Type.config = 0

    # name
    self.obj402.name.setValue('pivot')

    self.obj402.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,340.0,self.obj402)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj402.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj402)
    self.globalAndLocalPostcondition(self.obj402, rootNode)
    self.obj402.postAction( rootNode.CREATE )

    self.obj403=Equation(self)
    self.obj403.isGraphObjectVisual = True

    if(hasattr(self.obj403, '_setHierarchicalLink')):
      self.obj403._setHierarchicalLink(False)

    # name
    self.obj403.name.setValue('eq1')

    self.obj403.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(220.0,420.0,self.obj403)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj403.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj403)
    self.globalAndLocalPostcondition(self.obj403, rootNode)
    self.obj403.postAction( rootNode.CREATE )

    self.obj404=Equation(self)
    self.obj404.isGraphObjectVisual = True

    if(hasattr(self.obj404, '_setHierarchicalLink')):
      self.obj404._setHierarchicalLink(False)

    # name
    self.obj404.name.setValue('eq2')

    self.obj404.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(480.0,420.0,self.obj404)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj404.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj404)
    self.globalAndLocalPostcondition(self.obj404, rootNode)
    self.obj404.postAction( rootNode.CREATE )

    self.obj405=Constant(self)
    self.obj405.isGraphObjectVisual = True

    if(hasattr(self.obj405, '_setHierarchicalLink')):
      self.obj405._setHierarchicalLink(False)

    # Type
    self.obj405.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj405.Type.config = 0

    # name
    self.obj405.name.setValue('parexitpoint')

    self.obj405.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(280.0,340.0,self.obj405)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj405.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj405)
    self.globalAndLocalPostcondition(self.obj405, rootNode)
    self.obj405.postAction( rootNode.CREATE )

    self.obj406=Constant(self)
    self.obj406.isGraphObjectVisual = True

    if(hasattr(self.obj406, '_setHierarchicalLink')):
      self.obj406._setHierarchicalLink(False)

    # Type
    self.obj406.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj406.Type.config = 0

    # name
    self.obj406.name.setValue('instfortrans')

    self.obj406.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,340.0,self.obj406)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj406.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj406)
    self.globalAndLocalPostcondition(self.obj406, rootNode)
    self.obj406.postAction( rootNode.CREATE )

    self.obj407=paired_with(self)
    self.obj407.isGraphObjectVisual = True

    if(hasattr(self.obj407, '_setHierarchicalLink')):
      self.obj407._setHierarchicalLink(False)

    self.obj407.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,202.0,self.obj407)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj407.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj407)
    self.globalAndLocalPostcondition(self.obj407, rootNode)
    self.obj407.postAction( rootNode.CREATE )

    self.obj408=match_contains(self)
    self.obj408.isGraphObjectVisual = True

    if(hasattr(self.obj408, '_setHierarchicalLink')):
      self.obj408._setHierarchicalLink(False)

    self.obj408.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,87.0,self.obj408)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj408.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj408)
    self.globalAndLocalPostcondition(self.obj408, rootNode)
    self.obj408.postAction( rootNode.CREATE )

    self.obj409=match_contains(self)
    self.obj409.isGraphObjectVisual = True

    if(hasattr(self.obj409, '_setHierarchicalLink')):
      self.obj409._setHierarchicalLink(False)

    self.obj409.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(354.0,87.0,self.obj409)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj409.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj409)
    self.globalAndLocalPostcondition(self.obj409, rootNode)
    self.obj409.postAction( rootNode.CREATE )

    self.obj410=apply_contains(self)
    self.obj410.isGraphObjectVisual = True

    if(hasattr(self.obj410, '_setHierarchicalLink')):
      self.obj410._setHierarchicalLink(False)

    self.obj410.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,262.0,self.obj410)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj410.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj410)
    self.globalAndLocalPostcondition(self.obj410, rootNode)
    self.obj410.postAction( rootNode.CREATE )

    self.obj411=apply_contains(self)
    self.obj411.isGraphObjectVisual = True

    if(hasattr(self.obj411, '_setHierarchicalLink')):
      self.obj411._setHierarchicalLink(False)

    self.obj411.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(367.5,262.0,self.obj411)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj411.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj411)
    self.globalAndLocalPostcondition(self.obj411, rootNode)
    self.obj411.postAction( rootNode.CREATE )

    self.obj412=directLink_T(self)
    self.obj412.isGraphObjectVisual = True

    if(hasattr(self.obj412, '_setHierarchicalLink')):
      self.obj412._setHierarchicalLink(False)

    # associationType
    self.obj412.associationType.setValue('p')

    self.obj412.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(472.0,291.0,self.obj412)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj412.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj412)
    self.globalAndLocalPostcondition(self.obj412, rootNode)
    self.obj412.postAction( rootNode.CREATE )

    self.obj413=directLink_S(self)
    self.obj413.isGraphObjectVisual = True

    if(hasattr(self.obj413, '_setHierarchicalLink')):
      self.obj413._setHierarchicalLink(False)

    # associationType
    self.obj413.associationType.setValue('outgoingTransitions')

    self.obj413.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,123.0,self.obj413)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj413.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj413)
    self.globalAndLocalPostcondition(self.obj413, rootNode)
    self.obj413.postAction( rootNode.CREATE )

    self.obj414=backward_link(self)
    self.obj414.isGraphObjectVisual = True

    if(hasattr(self.obj414, '_setHierarchicalLink')):
      self.obj414._setHierarchicalLink(False)

    # type
    self.obj414.type.setValue('ruleDef')

    self.obj414.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,207.0,self.obj414)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj414.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj414)
    self.globalAndLocalPostcondition(self.obj414, rootNode)
    self.obj414.postAction( rootNode.CREATE )

    self.obj415=backward_link(self)
    self.obj415.isGraphObjectVisual = True

    if(hasattr(self.obj415, '_setHierarchicalLink')):
      self.obj415._setHierarchicalLink(False)

    # type
    self.obj415.type.setValue('ruleDef')

    self.obj415.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(581.0,207.0,self.obj415)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj415.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj415)
    self.globalAndLocalPostcondition(self.obj415, rootNode)
    self.obj415.postAction( rootNode.CREATE )

    self.obj416=hasAttribute_T(self)
    self.obj416.isGraphObjectVisual = True

    if(hasattr(self.obj416, '_setHierarchicalLink')):
      self.obj416._setHierarchicalLink(False)

    self.obj416.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(264.0,330.5,self.obj416)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj416.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj416)
    self.globalAndLocalPostcondition(self.obj416, rootNode)
    self.obj416.postAction( rootNode.CREATE )

    self.obj417=hasAttribute_T(self)
    self.obj417.isGraphObjectVisual = True

    if(hasattr(self.obj417, '_setHierarchicalLink')):
      self.obj417._setHierarchicalLink(False)

    self.obj417.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(583.0,332.5,self.obj417)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj417.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj417)
    self.globalAndLocalPostcondition(self.obj417, rootNode)
    self.obj417.postAction( rootNode.CREATE )

    self.obj418=leftExpr(self)
    self.obj418.isGraphObjectVisual = True

    if(hasattr(self.obj418, '_setHierarchicalLink')):
      self.obj418._setHierarchicalLink(False)

    self.obj418.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(277.0,418.5,self.obj418)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj418.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj418)
    self.globalAndLocalPostcondition(self.obj418, rootNode)
    self.obj418.postAction( rootNode.CREATE )

    self.obj419=leftExpr(self)
    self.obj419.isGraphObjectVisual = True

    if(hasattr(self.obj419, '_setHierarchicalLink')):
      self.obj419._setHierarchicalLink(False)

    self.obj419.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(596.0,416.5,self.obj419)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj419.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj419)
    self.globalAndLocalPostcondition(self.obj419, rootNode)
    self.obj419.postAction( rootNode.CREATE )

    self.obj420=rightExpr(self)
    self.obj420.isGraphObjectVisual = True

    if(hasattr(self.obj420, '_setHierarchicalLink')):
      self.obj420._setHierarchicalLink(False)

    self.obj420.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(396.0,416.5,self.obj420)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj420.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj420)
    self.globalAndLocalPostcondition(self.obj420, rootNode)
    self.obj420.postAction( rootNode.CREATE )

    self.obj421=rightExpr(self)
    self.obj421.isGraphObjectVisual = True

    if(hasattr(self.obj421, '_setHierarchicalLink')):
      self.obj421._setHierarchicalLink(False)

    self.obj421.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(676.0,416.5,self.obj421)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj421.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj421)
    self.globalAndLocalPostcondition(self.obj421, rootNode)
    self.obj421.postAction( rootNode.CREATE )

    # Connections for obj395 (graphObject_: Obj292) of type MatchModel
    self.drawConnections(
(self.obj395,self.obj407,[138.0, 51.0, 140.5, 202.0],"true", 2),
(self.obj395,self.obj408,[138.0, 51.0, 244.0, 87.0],"true", 2),
(self.obj395,self.obj409,[138.0, 51.0, 354.0, 87.0],"true", 2) )
    # Connections for obj396 (graphObject_: Obj293) of type ApplyModel
    self.drawConnections(
(self.obj396,self.obj410,[143.0, 233.0, 247.5, 262.0],"true", 2),
(self.obj396,self.obj411,[143.0, 233.0, 367.5, 262.0],"true", 2) )
    # Connections for obj397 (graphObject_: Obj294) named exitpoint1
    self.drawConnections(
(self.obj397,self.obj413,[350.0, 123.0, 460.0, 123.0],"true", 2) )
    # Connections for obj398 (graphObject_: Obj295) named transition1
    self.drawConnections(
 )
    # Connections for obj399 (graphObject_: Obj296) named par1
    self.drawConnections(
(self.obj399,self.obj412,[352.0, 291.0, 472.0, 291.0],"true", 2),
(self.obj399,self.obj416,[352.0, 291.0, 264.0, 330.5],"true", 2),
(self.obj399,self.obj414,[352.0, 291.0, 351.0, 207.0],"true", 2) )
    # Connections for obj400 (graphObject_: Obj297) named inst1
    self.drawConnections(
(self.obj400,self.obj417,[592.0, 291.0, 583.0, 332.5],"true", 2),
(self.obj400,self.obj415,[592.0, 291.0, 581.0, 207.0],"true", 2) )
    # Connections for obj401 (graphObject_: Obj298) named pivot
    self.drawConnections(
 )
    # Connections for obj402 (graphObject_: Obj299) named pivot
    self.drawConnections(
 )
    # Connections for obj403 (graphObject_: Obj300) named eq1
    self.drawConnections(
(self.obj403,self.obj418,[358.0, 459.0, 277.0, 418.5],"true", 2),
(self.obj403,self.obj420,[358.0, 459.0, 396.0, 416.5],"true", 2) )
    # Connections for obj404 (graphObject_: Obj301) named eq2
    self.drawConnections(
(self.obj404,self.obj419,[618.0, 459.0, 596.0, 416.5],"true", 2),
(self.obj404,self.obj421,[618.0, 459.0, 676.0, 416.5],"true", 2) )
    # Connections for obj405 (graphObject_: Obj302) named parexitpoint
    self.drawConnections(
 )
    # Connections for obj406 (graphObject_: Obj303) named instfortrans
    self.drawConnections(
 )
    # Connections for obj407 (graphObject_: Obj304) of type paired_with
    self.drawConnections(
(self.obj407,self.obj396,[140.5, 202.0, 143.0, 233.0],"true", 2) )
    # Connections for obj408 (graphObject_: Obj305) of type match_contains
    self.drawConnections(
(self.obj408,self.obj397,[244.0, 87.0, 350.0, 123.0],"true", 2) )
    # Connections for obj409 (graphObject_: Obj306) of type match_contains
    self.drawConnections(
(self.obj409,self.obj398,[354.0, 87.0, 570.0, 123.0],"true", 2) )
    # Connections for obj410 (graphObject_: Obj307) of type apply_contains
    self.drawConnections(
(self.obj410,self.obj399,[247.5, 262.0, 352.0, 291.0],"true", 2) )
    # Connections for obj411 (graphObject_: Obj308) of type apply_contains
    self.drawConnections(
(self.obj411,self.obj400,[367.5, 262.0, 592.0, 291.0],"true", 2) )
    # Connections for obj412 (graphObject_: Obj309) of type directLink_T
    self.drawConnections(
(self.obj412,self.obj400,[472.0, 291.0, 592.0, 291.0],"true", 2) )
    # Connections for obj413 (graphObject_: Obj310) of type directLink_S
    self.drawConnections(
(self.obj413,self.obj398,[460.0, 123.0, 570.0, 123.0],"true", 2) )
    # Connections for obj414 (graphObject_: Obj311) of type backward_link
    self.drawConnections(
(self.obj414,self.obj397,[351.0, 207.0, 350.0, 123.0],"true", 2) )
    # Connections for obj415 (graphObject_: Obj312) of type backward_link
    self.drawConnections(
(self.obj415,self.obj398,[581.0, 207.0, 570.0, 123.0],"true", 2) )
    # Connections for obj416 (graphObject_: Obj313) of type hasAttribute_T
    self.drawConnections(
(self.obj416,self.obj401,[264.0, 330.5, 234.0, 374.0],"true", 2) )
    # Connections for obj417 (graphObject_: Obj314) of type hasAttribute_T
    self.drawConnections(
(self.obj417,self.obj402,[583.0, 332.5, 574.0, 374.0],"true", 2) )
    # Connections for obj418 (graphObject_: Obj315) of type leftExpr
    self.drawConnections(
(self.obj418,self.obj401,[277.0, 418.5, 234.0, 374.0],"true", 2) )
    # Connections for obj419 (graphObject_: Obj316) of type leftExpr
    self.drawConnections(
(self.obj419,self.obj402,[596.0, 416.5, 574.0, 374.0],"true", 2) )
    # Connections for obj420 (graphObject_: Obj317) of type rightExpr
    self.drawConnections(
(self.obj420,self.obj405,[396.0, 416.5, 414.0, 374.0],"true", 2) )
    # Connections for obj421 (graphObject_: Obj318) of type rightExpr
    self.drawConnections(
(self.obj421,self.obj406,[676.0, 416.5, 734.0, 374.0],"true", 2) )

newfunction = ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
