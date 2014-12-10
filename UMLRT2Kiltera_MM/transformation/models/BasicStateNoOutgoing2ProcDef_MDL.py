"""
__BasicStateNoOutgoing2ProcDef_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 14:36:37 2014
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


    self.obj920=MatchModel(self)
    self.obj920.isGraphObjectVisual = True

    if(hasattr(self.obj920, '_setHierarchicalLink')):
      self.obj920._setHierarchicalLink(False)

    self.obj920.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(40.0,40.0,self.obj920)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj920.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj920)
    self.globalAndLocalPostcondition(self.obj920, rootNode)
    self.obj920.postAction( rootNode.CREATE )

    self.obj921=ApplyModel(self)
    self.obj921.isGraphObjectVisual = True

    if(hasattr(self.obj921, '_setHierarchicalLink')):
      self.obj921._setHierarchicalLink(False)

    self.obj921.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(40.0,260.0,self.obj921)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj921.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj921)
    self.globalAndLocalPostcondition(self.obj921, rootNode)
    self.obj921.postAction( rootNode.CREATE )

    self.obj922=State(self)
    self.obj922.isGraphObjectVisual = True

    if(hasattr(self.obj922, '_setHierarchicalLink')):
      self.obj922._setHierarchicalLink(False)

    # name
    self.obj922.name.setValue('state1')

    # classtype
    self.obj922.classtype.setValue('State')

    # cardinality
    self.obj922.cardinality.setValue('+')

    self.obj922.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(240.0,60.0,self.obj922)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj922.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj922)
    self.globalAndLocalPostcondition(self.obj922, rootNode)
    self.obj922.postAction( rootNode.CREATE )

    self.obj923=ProcDef(self)
    self.obj923.isGraphObjectVisual = True

    if(hasattr(self.obj923, '_setHierarchicalLink')):
      self.obj923._setHierarchicalLink(False)

    # classtype
    self.obj923.classtype.setValue('ProcDef')

    # cardinality
    self.obj923.cardinality.setValue('1')

    # name
    self.obj923.name.setValue('procdef1')

    self.obj923.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(240.0,260.0,self.obj923)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj923.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj923)
    self.globalAndLocalPostcondition(self.obj923, rootNode)
    self.obj923.postAction( rootNode.CREATE )

    self.obj924=Null(self)
    self.obj924.isGraphObjectVisual = True

    if(hasattr(self.obj924, '_setHierarchicalLink')):
      self.obj924._setHierarchicalLink(False)

    # classtype
    self.obj924.classtype.setValue('Null')

    # cardinality
    self.obj924.cardinality.setValue('1')

    # name
    self.obj924.name.setValue('null1')

    self.obj924.graphClass_= graph_Null
    if self.genGraphics:
       new_obj = graph_Null(460.0,260.0,self.obj924)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Null", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj924.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj924)
    self.globalAndLocalPostcondition(self.obj924, rootNode)
    self.obj924.postAction( rootNode.CREATE )

    self.obj925=Attribute(self)
    self.obj925.isGraphObjectVisual = True

    if(hasattr(self.obj925, '_setHierarchicalLink')):
      self.obj925._setHierarchicalLink(False)

    # Type
    self.obj925.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj925.Type.config = 0

    # name
    self.obj925.name.setValue('isComposite')

    self.obj925.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,20.0,self.obj925)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj925.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj925)
    self.globalAndLocalPostcondition(self.obj925, rootNode)
    self.obj925.postAction( rootNode.CREATE )

    self.obj926=Attribute(self)
    self.obj926.isGraphObjectVisual = True

    if(hasattr(self.obj926, '_setHierarchicalLink')):
      self.obj926._setHierarchicalLink(False)

    # Type
    self.obj926.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj926.Type.config = 0

    # name
    self.obj926.name.setValue('hasOutgoingTransitions')

    self.obj926.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(460.0,120.0,self.obj926)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj926.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj926)
    self.globalAndLocalPostcondition(self.obj926, rootNode)
    self.obj926.postAction( rootNode.CREATE )

    self.obj927=Attribute(self)
    self.obj927.isGraphObjectVisual = True

    if(hasattr(self.obj927, '_setHierarchicalLink')):
      self.obj927._setHierarchicalLink(False)

    # Type
    self.obj927.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj927.Type.config = 0

    # name
    self.obj927.name.setValue('pivotin')

    self.obj927.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(300.0,380.0,self.obj927)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj927.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj927)
    self.globalAndLocalPostcondition(self.obj927, rootNode)
    self.obj927.postAction( rootNode.CREATE )

    self.obj928=Equation(self)
    self.obj928.isGraphObjectVisual = True

    if(hasattr(self.obj928, '_setHierarchicalLink')):
      self.obj928._setHierarchicalLink(False)

    # name
    self.obj928.name.setValue('eq1')

    self.obj928.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,20.0,self.obj928)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj928.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj928)
    self.globalAndLocalPostcondition(self.obj928, rootNode)
    self.obj928.postAction( rootNode.CREATE )

    self.obj929=Equation(self)
    self.obj929.isGraphObjectVisual = True

    if(hasattr(self.obj929, '_setHierarchicalLink')):
      self.obj929._setHierarchicalLink(False)

    # name
    self.obj929.name.setValue('eq2')

    self.obj929.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,120.0,self.obj929)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj929.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj929)
    self.globalAndLocalPostcondition(self.obj929, rootNode)
    self.obj929.postAction( rootNode.CREATE )

    self.obj930=Equation(self)
    self.obj930.isGraphObjectVisual = True

    if(hasattr(self.obj930, '_setHierarchicalLink')):
      self.obj930._setHierarchicalLink(False)

    # name
    self.obj930.name.setValue('eq3')

    self.obj930.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(500.0,400.0,self.obj930)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj930.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj930)
    self.globalAndLocalPostcondition(self.obj930, rootNode)
    self.obj930.postAction( rootNode.CREATE )

    self.obj931=Constant(self)
    self.obj931.isGraphObjectVisual = True

    if(hasattr(self.obj931, '_setHierarchicalLink')):
      self.obj931._setHierarchicalLink(False)

    # Type
    self.obj931.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj931.Type.config = 0

    # name
    self.obj931.name.setValue('false')

    self.obj931.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,20.0,self.obj931)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.98
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj931.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj931)
    self.globalAndLocalPostcondition(self.obj931, rootNode)
    self.obj931.postAction( rootNode.CREATE )

    self.obj932=Constant(self)
    self.obj932.isGraphObjectVisual = True

    if(hasattr(self.obj932, '_setHierarchicalLink')):
      self.obj932._setHierarchicalLink(False)

    # Type
    self.obj932.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj932.Type.config = 0

    # name
    self.obj932.name.setValue('false')

    self.obj932.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,120.0,self.obj932)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj932.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj932)
    self.globalAndLocalPostcondition(self.obj932, rootNode)
    self.obj932.postAction( rootNode.CREATE )

    self.obj933=Constant(self)
    self.obj933.isGraphObjectVisual = True

    if(hasattr(self.obj933, '_setHierarchicalLink')):
      self.obj933._setHierarchicalLink(False)

    # Type
    self.obj933.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj933.Type.config = 0

    # name
    self.obj933.name.setValue('procdef')

    self.obj933.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(740.0,400.0,self.obj933)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj933.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj933)
    self.globalAndLocalPostcondition(self.obj933, rootNode)
    self.obj933.postAction( rootNode.CREATE )

    self.obj934=paired_with(self)
    self.obj934.isGraphObjectVisual = True

    if(hasattr(self.obj934, '_setHierarchicalLink')):
      self.obj934._setHierarchicalLink(False)

    self.obj934.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(160.5,182.0,self.obj934)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj934.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj934)
    self.globalAndLocalPostcondition(self.obj934, rootNode)
    self.obj934.postAction( rootNode.CREATE )

    self.obj935=match_contains(self)
    self.obj935.isGraphObjectVisual = True

    if(hasattr(self.obj935, '_setHierarchicalLink')):
      self.obj935._setHierarchicalLink(False)

    self.obj935.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(324.0,87.0,self.obj935)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj935.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj935)
    self.globalAndLocalPostcondition(self.obj935, rootNode)
    self.obj935.postAction( rootNode.CREATE )

    self.obj936=apply_contains(self)
    self.obj936.isGraphObjectVisual = True

    if(hasattr(self.obj936, '_setHierarchicalLink')):
      self.obj936._setHierarchicalLink(False)

    self.obj936.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(296.5,310.0,self.obj936)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj936.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj936)
    self.globalAndLocalPostcondition(self.obj936, rootNode)
    self.obj936.postAction( rootNode.CREATE )

    self.obj937=apply_contains(self)
    self.obj937.isGraphObjectVisual = True

    if(hasattr(self.obj937, '_setHierarchicalLink')):
      self.obj937._setHierarchicalLink(False)

    self.obj937.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(393.5,267.0,self.obj937)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj937.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj937)
    self.globalAndLocalPostcondition(self.obj937, rootNode)
    self.obj937.postAction( rootNode.CREATE )

    self.obj938=directLink_T(self)
    self.obj938.isGraphObjectVisual = True

    if(hasattr(self.obj938, '_setHierarchicalLink')):
      self.obj938._setHierarchicalLink(False)

    # associationType
    self.obj938.associationType.setValue('p')

    self.obj938.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(452.0,328.0,self.obj938)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj938.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj938)
    self.globalAndLocalPostcondition(self.obj938, rootNode)
    self.obj938.postAction( rootNode.CREATE )

    self.obj939=backward_link(self)
    self.obj939.isGraphObjectVisual = True

    if(hasattr(self.obj939, '_setHierarchicalLink')):
      self.obj939._setHierarchicalLink(False)

    # type
    self.obj939.type.setValue('ruleDef')

    self.obj939.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(411.0,207.0,self.obj939)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj939.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj939)
    self.globalAndLocalPostcondition(self.obj939, rootNode)
    self.obj939.postAction( rootNode.CREATE )

    self.obj940=hasAttribute_S(self)
    self.obj940.isGraphObjectVisual = True

    if(hasattr(self.obj940, '_setHierarchicalLink')):
      self.obj940._setHierarchicalLink(False)

    self.obj940.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(463.0,80.5,self.obj940)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj940.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj940)
    self.globalAndLocalPostcondition(self.obj940, rootNode)
    self.obj940.postAction( rootNode.CREATE )

    self.obj941=hasAttribute_S(self)
    self.obj941.isGraphObjectVisual = True

    if(hasattr(self.obj941, '_setHierarchicalLink')):
      self.obj941._setHierarchicalLink(False)

    self.obj941.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(470.0,124.5,self.obj941)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj941.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj941)
    self.globalAndLocalPostcondition(self.obj941, rootNode)
    self.obj941.postAction( rootNode.CREATE )

    self.obj942=hasAttribute_T(self)
    self.obj942.isGraphObjectVisual = True

    if(hasattr(self.obj942, '_setHierarchicalLink')):
      self.obj942._setHierarchicalLink(False)

    self.obj942.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(423.0,362.5,self.obj942)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj942.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj942)
    self.globalAndLocalPostcondition(self.obj942, rootNode)
    self.obj942.postAction( rootNode.CREATE )

    self.obj943=leftExpr(self)
    self.obj943.isGraphObjectVisual = True

    if(hasattr(self.obj943, '_setHierarchicalLink')):
      self.obj943._setHierarchicalLink(False)

    self.obj943.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(676.0,56.5,self.obj943)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj943.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj943)
    self.globalAndLocalPostcondition(self.obj943, rootNode)
    self.obj943.postAction( rootNode.CREATE )

    self.obj944=leftExpr(self)
    self.obj944.isGraphObjectVisual = True

    if(hasattr(self.obj944, '_setHierarchicalLink')):
      self.obj944._setHierarchicalLink(False)

    self.obj944.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(686.0,156.5,self.obj944)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj944.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj944)
    self.globalAndLocalPostcondition(self.obj944, rootNode)
    self.obj944.postAction( rootNode.CREATE )

    self.obj945=leftExpr(self)
    self.obj945.isGraphObjectVisual = True

    if(hasattr(self.obj945, '_setHierarchicalLink')):
      self.obj945._setHierarchicalLink(False)

    self.obj945.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(536.0,426.5,self.obj945)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj945.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj945)
    self.globalAndLocalPostcondition(self.obj945, rootNode)
    self.obj945.postAction( rootNode.CREATE )

    self.obj946=rightExpr(self)
    self.obj946.isGraphObjectVisual = True

    if(hasattr(self.obj946, '_setHierarchicalLink')):
      self.obj946._setHierarchicalLink(False)

    self.obj946.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(856.0,156.5,self.obj946)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj946.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj946)
    self.globalAndLocalPostcondition(self.obj946, rootNode)
    self.obj946.postAction( rootNode.CREATE )

    self.obj947=rightExpr(self)
    self.obj947.isGraphObjectVisual = True

    if(hasattr(self.obj947, '_setHierarchicalLink')):
      self.obj947._setHierarchicalLink(False)

    self.obj947.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(856.0,56.5,self.obj947)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj947.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj947)
    self.globalAndLocalPostcondition(self.obj947, rootNode)
    self.obj947.postAction( rootNode.CREATE )

    self.obj948=rightExpr(self)
    self.obj948.isGraphObjectVisual = True

    if(hasattr(self.obj948, '_setHierarchicalLink')):
      self.obj948._setHierarchicalLink(False)

    self.obj948.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(756.0,436.5,self.obj948)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj948.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj948)
    self.globalAndLocalPostcondition(self.obj948, rootNode)
    self.obj948.postAction( rootNode.CREATE )

    # Connections for obj920 (graphObject_: Obj271) of type MatchModel
    self.drawConnections(
(self.obj920,self.obj934,[158.0, 71.0, 160.5, 182.0],"true", 2),
(self.obj920,self.obj935,[158.0, 71.0, 324.0, 87.0],"true", 2) )
    # Connections for obj921 (graphObject_: Obj272) of type ApplyModel
    self.drawConnections(
(self.obj921,self.obj936,[163.0, 293.0, 296.5, 310.0],"true", 2),
(self.obj921,self.obj937,[163.0, 293.0, 393.5, 267.0],"true", 2) )
    # Connections for obj922 (graphObject_: Obj273) named state1
    self.drawConnections(
(self.obj922,self.obj940,[410.0, 103.0, 463.0, 80.5],"true", 2),
(self.obj922,self.obj941,[410.0, 103.0, 470.0, 124.5],"true", 2) )
    # Connections for obj923 (graphObject_: Obj274) named procdef1
    self.drawConnections(
(self.obj923,self.obj938,[412.0, 311.0, 452.0, 328.0],"true", 2),
(self.obj923,self.obj939,[412.0, 311.0, 411.0, 207.0],"true", 2),
(self.obj923,self.obj942,[412.0, 311.0, 423.0, 362.5],"true", 2) )
    # Connections for obj924 (graphObject_: Obj275) named null1
    self.drawConnections(
 )
    # Connections for obj925 (graphObject_: Obj276) named isComposite
    self.drawConnections(
 )
    # Connections for obj926 (graphObject_: Obj277) named hasOutgoingTransitions
    self.drawConnections(
 )
    # Connections for obj927 (graphObject_: Obj278) named pivotin
    self.drawConnections(
 )
    # Connections for obj928 (graphObject_: Obj279) named eq1
    self.drawConnections(
(self.obj928,self.obj947,[778.0, 59.0, 856.0, 56.5],"true", 2),
(self.obj928,self.obj943,[778.0, 59.0, 676.0, 56.5],"true", 2) )
    # Connections for obj929 (graphObject_: Obj280) named eq2
    self.drawConnections(
(self.obj929,self.obj946,[778.0, 159.0, 856.0, 156.5],"true", 2),
(self.obj929,self.obj944,[778.0, 159.0, 686.0, 156.5],"true", 2) )
    # Connections for obj930 (graphObject_: Obj281) named eq3
    self.drawConnections(
(self.obj930,self.obj945,[638.0, 439.0, 536.0, 426.5],"true", 2),
(self.obj930,self.obj948,[638.0, 439.0, 756.0, 436.5],"true", 2) )
    # Connections for obj931 (graphObject_: Obj282) named false
    self.drawConnections(
 )
    # Connections for obj932 (graphObject_: Obj283) named false
    self.drawConnections(
 )
    # Connections for obj933 (graphObject_: Obj284) named procdef
    self.drawConnections(
 )
    # Connections for obj934 (graphObject_: Obj285) of type paired_with
    self.drawConnections(
(self.obj934,self.obj921,[160.5, 182.0, 163.0, 293.0],"true", 2) )
    # Connections for obj935 (graphObject_: Obj286) of type match_contains
    self.drawConnections(
(self.obj935,self.obj922,[324.0, 87.0, 410.0, 103.0],"true", 2) )
    # Connections for obj936 (graphObject_: Obj287) of type apply_contains
    self.drawConnections(
(self.obj936,self.obj923,[296.5, 310.0, 412.0, 311.0],"true", 2) )
    # Connections for obj937 (graphObject_: Obj288) of type apply_contains
    self.drawConnections(
(self.obj937,self.obj924,[393.5, 267.0, 632.0, 311.0],"true", 2) )
    # Connections for obj938 (graphObject_: Obj289) of type directLink_T
    self.drawConnections(
(self.obj938,self.obj924,[660.0, 348.0, 632.0, 311.0],"true", 2) )
    # Connections for obj939 (graphObject_: Obj290) of type backward_link
    self.drawConnections(
(self.obj939,self.obj922,[411.0, 207.0, 410.0, 103.0],"true", 2) )
    # Connections for obj940 (graphObject_: Obj291) of type hasAttribute_S
    self.drawConnections(
(self.obj940,self.obj925,[463.0, 80.5, 574.0, 54.0],"true", 2) )
    # Connections for obj941 (graphObject_: Obj292) of type hasAttribute_S
    self.drawConnections(
(self.obj941,self.obj926,[470.0, 124.5, 618.0, 154.0],"true", 2) )
    # Connections for obj942 (graphObject_: Obj293) of type hasAttribute_T
    self.drawConnections(
(self.obj942,self.obj927,[423.0, 362.5, 434.0, 414.0],"true", 2) )
    # Connections for obj943 (graphObject_: Obj294) of type leftExpr
    self.drawConnections(
(self.obj943,self.obj925,[676.0, 56.5, 574.0, 54.0],"true", 2) )
    # Connections for obj944 (graphObject_: Obj295) of type leftExpr
    self.drawConnections(
(self.obj944,self.obj926,[686.0, 156.5, 618.0, 154.0],"true", 2) )
    # Connections for obj945 (graphObject_: Obj296) of type leftExpr
    self.drawConnections(
(self.obj945,self.obj927,[536.0, 426.5, 434.0, 414.0],"true", 2) )
    # Connections for obj946 (graphObject_: Obj297) of type rightExpr
    self.drawConnections(
(self.obj946,self.obj932,[856.0, 156.5, 934.0, 154.0],"true", 2) )
    # Connections for obj947 (graphObject_: Obj298) of type rightExpr
    self.drawConnections(
(self.obj947,self.obj931,[856.0, 56.5, 934.0, 54.0],"true", 2) )
    # Connections for obj948 (graphObject_: Obj299) of type rightExpr
    self.drawConnections(
(self.obj948,self.obj933,[756.0, 436.5, 874.0, 434.0],"true", 2) )

newfunction = BasicStateNoOutgoing2ProcDef_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
