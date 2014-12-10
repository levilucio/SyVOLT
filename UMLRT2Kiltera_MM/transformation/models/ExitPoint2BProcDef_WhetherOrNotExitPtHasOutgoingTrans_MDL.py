"""
__ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 14:48:14 2014
___________________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ExitPoint import *
from State import *
from ProcDef import *
from Name import *
from Trigger_T import *
from Par import *
from LocalDef import *
from Attribute import *
from Equation import *
from Concat import *
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
from hasArgs import *
from graph_ExitPoint import *
from graph_Attribute import *
from graph_LocalDef import *
from graph_paired_with import *
from graph_ProcDef import *
from graph_Par import *
from graph_Equation import *
from graph_backward_link import *
from graph_hasArgs import *
from graph_State import *
from graph_rightExpr import *
from graph_Trigger_T import *
from graph_Concat import *
from graph_hasAttribute_T import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_ApplyModel import *
from graph_Name import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_hasAttribute_S import *
from graph_match_contains import *
from graph_leftExpr import *
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

def ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans')
    # --- ASG attributes over ---


    self.obj1131=MatchModel(self)
    self.obj1131.isGraphObjectVisual = True

    if(hasattr(self.obj1131, '_setHierarchicalLink')):
      self.obj1131._setHierarchicalLink(False)

    self.obj1131.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1131)
    self.globalAndLocalPostcondition(self.obj1131, rootNode)
    self.obj1131.postAction( rootNode.CREATE )

    self.obj1132=ApplyModel(self)
    self.obj1132.isGraphObjectVisual = True

    if(hasattr(self.obj1132, '_setHierarchicalLink')):
      self.obj1132._setHierarchicalLink(False)

    self.obj1132.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,300.0,self.obj1132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1132)
    self.globalAndLocalPostcondition(self.obj1132, rootNode)
    self.obj1132.postAction( rootNode.CREATE )

    self.obj1133=ExitPoint(self)
    self.obj1133.isGraphObjectVisual = True

    if(hasattr(self.obj1133, '_setHierarchicalLink')):
      self.obj1133._setHierarchicalLink(False)

    # name
    self.obj1133.name.setValue('exitpoint1')

    # classtype
    self.obj1133.classtype.setValue('ExitPoint')

    # cardinality
    self.obj1133.cardinality.setValue('+')

    self.obj1133.graphClass_= graph_ExitPoint
    if self.genGraphics:
       new_obj = graph_ExitPoint(480.0,40.0,self.obj1133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1133)
    self.globalAndLocalPostcondition(self.obj1133, rootNode)
    self.obj1133.postAction( rootNode.CREATE )

    self.obj1134=State(self)
    self.obj1134.isGraphObjectVisual = True

    if(hasattr(self.obj1134, '_setHierarchicalLink')):
      self.obj1134._setHierarchicalLink(False)

    # name
    self.obj1134.name.setValue('state1')

    # classtype
    self.obj1134.classtype.setValue('State')

    # cardinality
    self.obj1134.cardinality.setValue('+')

    self.obj1134.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj1134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1134)
    self.globalAndLocalPostcondition(self.obj1134, rootNode)
    self.obj1134.postAction( rootNode.CREATE )

    self.obj1135=ProcDef(self)
    self.obj1135.isGraphObjectVisual = True

    if(hasattr(self.obj1135, '_setHierarchicalLink')):
      self.obj1135._setHierarchicalLink(False)

    # classtype
    self.obj1135.classtype.setValue('ProcDef')

    # cardinality
    self.obj1135.cardinality.setValue('1')

    # name
    self.obj1135.name.setValue('procdef1')

    self.obj1135.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(460.0,380.0,self.obj1135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1135)
    self.globalAndLocalPostcondition(self.obj1135, rootNode)
    self.obj1135.postAction( rootNode.CREATE )

    self.obj1136=Name(self)
    self.obj1136.isGraphObjectVisual = True

    if(hasattr(self.obj1136, '_setHierarchicalLink')):
      self.obj1136._setHierarchicalLink(False)

    # classtype
    self.obj1136.classtype.setValue('Name')

    # cardinality
    self.obj1136.cardinality.setValue('1')

    # name
    self.obj1136.name.setValue('name1')

    self.obj1136.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(660.0,380.0,self.obj1136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1136)
    self.globalAndLocalPostcondition(self.obj1136, rootNode)
    self.obj1136.postAction( rootNode.CREATE )

    self.obj1137=Trigger_T(self)
    self.obj1137.isGraphObjectVisual = True

    if(hasattr(self.obj1137, '_setHierarchicalLink')):
      self.obj1137._setHierarchicalLink(False)

    # classtype
    self.obj1137.classtype.setValue('Trigger_T')

    # cardinality
    self.obj1137.cardinality.setValue('1')

    # name
    self.obj1137.name.setValue('triggerT1')

    self.obj1137.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(700.0,500.0,self.obj1137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1137)
    self.globalAndLocalPostcondition(self.obj1137, rootNode)
    self.obj1137.postAction( rootNode.CREATE )

    self.obj1138=Par(self)
    self.obj1138.isGraphObjectVisual = True

    if(hasattr(self.obj1138, '_setHierarchicalLink')):
      self.obj1138._setHierarchicalLink(False)

    # classtype
    self.obj1138.classtype.setValue('Par')

    # cardinality
    self.obj1138.cardinality.setValue('1')

    # name
    self.obj1138.name.setValue('par1')

    self.obj1138.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(500.0,500.0,self.obj1138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1138)
    self.globalAndLocalPostcondition(self.obj1138, rootNode)
    self.obj1138.postAction( rootNode.CREATE )

    self.obj1139=LocalDef(self)
    self.obj1139.isGraphObjectVisual = True

    if(hasattr(self.obj1139, '_setHierarchicalLink')):
      self.obj1139._setHierarchicalLink(False)

    # classtype
    self.obj1139.classtype.setValue('LocalDef')

    # cardinality
    self.obj1139.cardinality.setValue('1')

    # name
    self.obj1139.name.setValue('localdef1')

    self.obj1139.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(220.0,380.0,self.obj1139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1139)
    self.globalAndLocalPostcondition(self.obj1139, rootNode)
    self.obj1139.postAction( rootNode.CREATE )

    self.obj1140=Attribute(self)
    self.obj1140.isGraphObjectVisual = True

    if(hasattr(self.obj1140, '_setHierarchicalLink')):
      self.obj1140._setHierarchicalLink(False)

    # Type
    self.obj1140.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1140.Type.config = 0

    # name
    self.obj1140.name.setValue('isComposite')

    self.obj1140.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,140.0,self.obj1140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1140)
    self.globalAndLocalPostcondition(self.obj1140, rootNode)
    self.obj1140.postAction( rootNode.CREATE )

    self.obj1141=Attribute(self)
    self.obj1141.isGraphObjectVisual = True

    if(hasattr(self.obj1141, '_setHierarchicalLink')):
      self.obj1141._setHierarchicalLink(False)

    # Type
    self.obj1141.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1141.Type.config = 0

    # name
    self.obj1141.name.setValue('name')

    self.obj1141.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(700.0,100.0,self.obj1141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1141)
    self.globalAndLocalPostcondition(self.obj1141, rootNode)
    self.obj1141.postAction( rootNode.CREATE )

    self.obj1142=Attribute(self)
    self.obj1142.isGraphObjectVisual = True

    if(hasattr(self.obj1142, '_setHierarchicalLink')):
      self.obj1142._setHierarchicalLink(False)

    # Type
    self.obj1142.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1142.Type.config = 0

    # name
    self.obj1142.name.setValue('name')

    self.obj1142.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,300.0,self.obj1142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1142)
    self.globalAndLocalPostcondition(self.obj1142, rootNode)
    self.obj1142.postAction( rootNode.CREATE )

    self.obj1143=Attribute(self)
    self.obj1143.isGraphObjectVisual = True

    if(hasattr(self.obj1143, '_setHierarchicalLink')):
      self.obj1143._setHierarchicalLink(False)

    # Type
    self.obj1143.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1143.Type.config = 0

    # name
    self.obj1143.name.setValue('literal')

    self.obj1143.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,400.0,self.obj1143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1143)
    self.globalAndLocalPostcondition(self.obj1143, rootNode)
    self.obj1143.postAction( rootNode.CREATE )

    self.obj1144=Attribute(self)
    self.obj1144.isGraphObjectVisual = True

    if(hasattr(self.obj1144, '_setHierarchicalLink')):
      self.obj1144._setHierarchicalLink(False)

    # Type
    self.obj1144.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1144.Type.config = 0

    # name
    self.obj1144.name.setValue('channel')

    self.obj1144.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(880.0,520.0,self.obj1144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1144)
    self.globalAndLocalPostcondition(self.obj1144, rootNode)
    self.obj1144.postAction( rootNode.CREATE )

    self.obj1145=Attribute(self)
    self.obj1145.isGraphObjectVisual = True

    if(hasattr(self.obj1145, '_setHierarchicalLink')):
      self.obj1145._setHierarchicalLink(False)

    # Type
    self.obj1145.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1145.Type.config = 0

    # name
    self.obj1145.name.setValue('pivotin')

    self.obj1145.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,560.0,self.obj1145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1145)
    self.globalAndLocalPostcondition(self.obj1145, rootNode)
    self.obj1145.postAction( rootNode.CREATE )

    self.obj1146=Attribute(self)
    self.obj1146.isGraphObjectVisual = True

    if(hasattr(self.obj1146, '_setHierarchicalLink')):
      self.obj1146._setHierarchicalLink(False)

    # Type
    self.obj1146.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1146.Type.config = 0

    # name
    self.obj1146.name.setValue('pivotout')

    self.obj1146.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,620.0,self.obj1146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1146)
    self.globalAndLocalPostcondition(self.obj1146, rootNode)
    self.obj1146.postAction( rootNode.CREATE )

    self.obj1147=Equation(self)
    self.obj1147.isGraphObjectVisual = True

    if(hasattr(self.obj1147, '_setHierarchicalLink')):
      self.obj1147._setHierarchicalLink(False)

    # name
    self.obj1147.name.setValue('eq1')

    self.obj1147.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,220.0,self.obj1147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1147)
    self.globalAndLocalPostcondition(self.obj1147, rootNode)
    self.obj1147.postAction( rootNode.CREATE )

    self.obj1148=Equation(self)
    self.obj1148.isGraphObjectVisual = True

    if(hasattr(self.obj1148, '_setHierarchicalLink')):
      self.obj1148._setHierarchicalLink(False)

    # name
    self.obj1148.name.setValue('eq2')

    self.obj1148.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(700.0,280.0,self.obj1148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1148)
    self.globalAndLocalPostcondition(self.obj1148, rootNode)
    self.obj1148.postAction( rootNode.CREATE )

    self.obj1149=Equation(self)
    self.obj1149.isGraphObjectVisual = True

    if(hasattr(self.obj1149, '_setHierarchicalLink')):
      self.obj1149._setHierarchicalLink(False)

    # name
    self.obj1149.name.setValue('eq3')

    self.obj1149.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(960.0,320.0,self.obj1149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1149)
    self.globalAndLocalPostcondition(self.obj1149, rootNode)
    self.obj1149.postAction( rootNode.CREATE )

    self.obj1150=Equation(self)
    self.obj1150.isGraphObjectVisual = True

    if(hasattr(self.obj1150, '_setHierarchicalLink')):
      self.obj1150._setHierarchicalLink(False)

    # name
    self.obj1150.name.setValue('eq4')

    self.obj1150.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(960.0,600.0,self.obj1150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1150)
    self.globalAndLocalPostcondition(self.obj1150, rootNode)
    self.obj1150.postAction( rootNode.CREATE )

    self.obj1151=Equation(self)
    self.obj1151.isGraphObjectVisual = True

    if(hasattr(self.obj1151, '_setHierarchicalLink')):
      self.obj1151._setHierarchicalLink(False)

    # name
    self.obj1151.name.setValue('eq5')

    self.obj1151.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(260.0,640.0,self.obj1151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1151)
    self.globalAndLocalPostcondition(self.obj1151, rootNode)
    self.obj1151.postAction( rootNode.CREATE )

    self.obj1152=Equation(self)
    self.obj1152.isGraphObjectVisual = True

    if(hasattr(self.obj1152, '_setHierarchicalLink')):
      self.obj1152._setHierarchicalLink(False)

    # name
    self.obj1152.name.setValue('eq6')

    self.obj1152.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(560.0,700.0,self.obj1152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1152)
    self.globalAndLocalPostcondition(self.obj1152, rootNode)
    self.obj1152.postAction( rootNode.CREATE )

    self.obj1153=Concat(self)
    self.obj1153.isGraphObjectVisual = True

    if(hasattr(self.obj1153, '_setHierarchicalLink')):
      self.obj1153._setHierarchicalLink(False)

    # Type
    self.obj1153.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1153.Type.config = 0

    # name
    self.obj1153.name.setValue('concat1')

    self.obj1153.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,200.0,self.obj1153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1153)
    self.globalAndLocalPostcondition(self.obj1153, rootNode)
    self.obj1153.postAction( rootNode.CREATE )

    self.obj1154=Constant(self)
    self.obj1154.isGraphObjectVisual = True

    if(hasattr(self.obj1154, '_setHierarchicalLink')):
      self.obj1154._setHierarchicalLink(False)

    # Type
    self.obj1154.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1154.Type.config = 0

    # name
    self.obj1154.name.setValue('true')

    self.obj1154.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(340.0,140.0,self.obj1154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1154)
    self.globalAndLocalPostcondition(self.obj1154, rootNode)
    self.obj1154.postAction( rootNode.CREATE )

    self.obj1155=Constant(self)
    self.obj1155.isGraphObjectVisual = True

    if(hasattr(self.obj1155, '_setHierarchicalLink')):
      self.obj1155._setHierarchicalLink(False)

    # Type
    self.obj1155.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1155.Type.config = 0

    # name
    self.obj1155.name.setValue('B')

    self.obj1155.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,200.0,self.obj1155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1155)
    self.globalAndLocalPostcondition(self.obj1155, rootNode)
    self.obj1155.postAction( rootNode.CREATE )

    self.obj1156=Constant(self)
    self.obj1156.isGraphObjectVisual = True

    if(hasattr(self.obj1156, '_setHierarchicalLink')):
      self.obj1156._setHierarchicalLink(False)

    # Type
    self.obj1156.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1156.Type.config = 0

    # name
    self.obj1156.name.setValue('sh_in')

    self.obj1156.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1020.0,400.0,self.obj1156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1156)
    self.globalAndLocalPostcondition(self.obj1156, rootNode)
    self.obj1156.postAction( rootNode.CREATE )

    self.obj1157=Constant(self)
    self.obj1157.isGraphObjectVisual = True

    if(hasattr(self.obj1157, '_setHierarchicalLink')):
      self.obj1157._setHierarchicalLink(False)

    # Type
    self.obj1157.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1157.Type.config = 0

    # name
    self.obj1157.name.setValue('sh_in')

    self.obj1157.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1040.0,520.0,self.obj1157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1157)
    self.globalAndLocalPostcondition(self.obj1157, rootNode)
    self.obj1157.postAction( rootNode.CREATE )

    self.obj1158=Constant(self)
    self.obj1158.isGraphObjectVisual = True

    if(hasattr(self.obj1158, '_setHierarchicalLink')):
      self.obj1158._setHierarchicalLink(False)

    # Type
    self.obj1158.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1158.Type.config = 0

    # name
    self.obj1158.name.setValue('localdefcompstate')

    self.obj1158.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(340.0,560.0,self.obj1158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1158)
    self.globalAndLocalPostcondition(self.obj1158, rootNode)
    self.obj1158.postAction( rootNode.CREATE )

    self.obj1159=Constant(self)
    self.obj1159.isGraphObjectVisual = True

    if(hasattr(self.obj1159, '_setHierarchicalLink')):
      self.obj1159._setHierarchicalLink(False)

    # Type
    self.obj1159.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1159.Type.config = 0

    # name
    self.obj1159.name.setValue('parexitpoint')

    self.obj1159.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(660.0,620.0,self.obj1159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1159)
    self.globalAndLocalPostcondition(self.obj1159, rootNode)
    self.obj1159.postAction( rootNode.CREATE )

    self.obj1160=paired_with(self)
    self.obj1160.isGraphObjectVisual = True

    if(hasattr(self.obj1160, '_setHierarchicalLink')):
      self.obj1160._setHierarchicalLink(False)

    self.obj1160.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj1160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1160)
    self.globalAndLocalPostcondition(self.obj1160, rootNode)
    self.obj1160.postAction( rootNode.CREATE )

    self.obj1161=match_contains(self)
    self.obj1161.isGraphObjectVisual = True

    if(hasattr(self.obj1161, '_setHierarchicalLink')):
      self.obj1161._setHierarchicalLink(False)

    self.obj1161.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj1161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1161)
    self.globalAndLocalPostcondition(self.obj1161, rootNode)
    self.obj1161.postAction( rootNode.CREATE )

    self.obj1162=match_contains(self)
    self.obj1162.isGraphObjectVisual = True

    if(hasattr(self.obj1162, '_setHierarchicalLink')):
      self.obj1162._setHierarchicalLink(False)

    self.obj1162.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,67.0,self.obj1162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1162)
    self.globalAndLocalPostcondition(self.obj1162, rootNode)
    self.obj1162.postAction( rootNode.CREATE )

    self.obj1163=apply_contains(self)
    self.obj1163.isGraphObjectVisual = True

    if(hasattr(self.obj1163, '_setHierarchicalLink')):
      self.obj1163._setHierarchicalLink(False)

    self.obj1163.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,375.0,self.obj1163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1163)
    self.globalAndLocalPostcondition(self.obj1163, rootNode)
    self.obj1163.postAction( rootNode.CREATE )

    self.obj1164=apply_contains(self)
    self.obj1164.isGraphObjectVisual = True

    if(hasattr(self.obj1164, '_setHierarchicalLink')):
      self.obj1164._setHierarchicalLink(False)

    self.obj1164.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(377.5,374.0,self.obj1164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1164)
    self.globalAndLocalPostcondition(self.obj1164, rootNode)
    self.obj1164.postAction( rootNode.CREATE )

    self.obj1165=apply_contains(self)
    self.obj1165.isGraphObjectVisual = True

    if(hasattr(self.obj1165, '_setHierarchicalLink')):
      self.obj1165._setHierarchicalLink(False)

    self.obj1165.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,382.0,self.obj1165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1165)
    self.globalAndLocalPostcondition(self.obj1165, rootNode)
    self.obj1165.postAction( rootNode.CREATE )

    self.obj1166=apply_contains(self)
    self.obj1166.isGraphObjectVisual = True

    if(hasattr(self.obj1166, '_setHierarchicalLink')):
      self.obj1166._setHierarchicalLink(False)

    self.obj1166.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,486.0,self.obj1166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1166)
    self.globalAndLocalPostcondition(self.obj1166, rootNode)
    self.obj1166.postAction( rootNode.CREATE )

    self.obj1167=apply_contains(self)
    self.obj1167.isGraphObjectVisual = True

    if(hasattr(self.obj1167, '_setHierarchicalLink')):
      self.obj1167._setHierarchicalLink(False)

    self.obj1167.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(507.5,442.0,self.obj1167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1167)
    self.globalAndLocalPostcondition(self.obj1167, rootNode)
    self.obj1167.postAction( rootNode.CREATE )

    self.obj1168=directLink_T(self)
    self.obj1168.isGraphObjectVisual = True

    if(hasattr(self.obj1168, '_setHierarchicalLink')):
      self.obj1168._setHierarchicalLink(False)

    # associationType
    self.obj1168.associationType.setValue('def')

    self.obj1168.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(431.0,427.0,self.obj1168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1168)
    self.globalAndLocalPostcondition(self.obj1168, rootNode)
    self.obj1168.postAction( rootNode.CREATE )

    self.obj1169=directLink_T(self)
    self.obj1169.isGraphObjectVisual = True

    if(hasattr(self.obj1169, '_setHierarchicalLink')):
      self.obj1169._setHierarchicalLink(False)

    # associationType
    self.obj1169.associationType.setValue('channelNames')

    self.obj1169.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,431.0,self.obj1169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1169)
    self.globalAndLocalPostcondition(self.obj1169, rootNode)
    self.obj1169.postAction( rootNode.CREATE )

    self.obj1170=directLink_T(self)
    self.obj1170.isGraphObjectVisual = True

    if(hasattr(self.obj1170, '_setHierarchicalLink')):
      self.obj1170._setHierarchicalLink(False)

    # associationType
    self.obj1170.associationType.setValue('p')

    self.obj1170.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj1170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1170)
    self.globalAndLocalPostcondition(self.obj1170, rootNode)
    self.obj1170.postAction( rootNode.CREATE )

    self.obj1171=directLink_T(self)
    self.obj1171.isGraphObjectVisual = True

    if(hasattr(self.obj1171, '_setHierarchicalLink')):
      self.obj1171._setHierarchicalLink(False)

    # associationType
    self.obj1171.associationType.setValue('p')

    self.obj1171.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(772.0,551.0,self.obj1171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1171)
    self.globalAndLocalPostcondition(self.obj1171, rootNode)
    self.obj1171.postAction( rootNode.CREATE )

    self.obj1172=directLink_S(self)
    self.obj1172.isGraphObjectVisual = True

    if(hasattr(self.obj1172, '_setHierarchicalLink')):
      self.obj1172._setHierarchicalLink(False)

    # associationType
    self.obj1172.associationType.setValue('exitPoints')

    self.obj1172.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(500.0,83.0,self.obj1172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1172)
    self.globalAndLocalPostcondition(self.obj1172, rootNode)
    self.obj1172.postAction( rootNode.CREATE )

    self.obj1173=backward_link(self)
    self.obj1173.isGraphObjectVisual = True

    if(hasattr(self.obj1173, '_setHierarchicalLink')):
      self.obj1173._setHierarchicalLink(False)

    # type
    self.obj1173.type.setValue('ruleDef')

    self.obj1173.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(371.0,257.0,self.obj1173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1173)
    self.globalAndLocalPostcondition(self.obj1173, rootNode)
    self.obj1173.postAction( rootNode.CREATE )

    self.obj1174=hasAttribute_S(self)
    self.obj1174.isGraphObjectVisual = True

    if(hasattr(self.obj1174, '_setHierarchicalLink')):
      self.obj1174._setHierarchicalLink(False)

    self.obj1174.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(328.0,136.5,self.obj1174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1174)
    self.globalAndLocalPostcondition(self.obj1174, rootNode)
    self.obj1174.postAction( rootNode.CREATE )

    self.obj1175=hasAttribute_S(self)
    self.obj1175.isGraphObjectVisual = True

    if(hasattr(self.obj1175, '_setHierarchicalLink')):
      self.obj1175._setHierarchicalLink(False)

    self.obj1175.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(742.0,108.5,self.obj1175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1175)
    self.globalAndLocalPostcondition(self.obj1175, rootNode)
    self.obj1175.postAction( rootNode.CREATE )

    self.obj1176=hasAttribute_T(self)
    self.obj1176.isGraphObjectVisual = True

    if(hasattr(self.obj1176, '_setHierarchicalLink')):
      self.obj1176._setHierarchicalLink(False)

    self.obj1176.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(634.0,364.5,self.obj1176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1176)
    self.globalAndLocalPostcondition(self.obj1176, rootNode)
    self.obj1176.postAction( rootNode.CREATE )

    self.obj1177=hasAttribute_T(self)
    self.obj1177.isGraphObjectVisual = True

    if(hasattr(self.obj1177, '_setHierarchicalLink')):
      self.obj1177._setHierarchicalLink(False)

    self.obj1177.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(913.0,432.5,self.obj1177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1177)
    self.globalAndLocalPostcondition(self.obj1177, rootNode)
    self.obj1177.postAction( rootNode.CREATE )

    self.obj1178=hasAttribute_T(self)
    self.obj1178.isGraphObjectVisual = True

    if(hasattr(self.obj1178, '_setHierarchicalLink')):
      self.obj1178._setHierarchicalLink(False)

    self.obj1178.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(943.0,552.5,self.obj1178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1178)
    self.globalAndLocalPostcondition(self.obj1178, rootNode)
    self.obj1178.postAction( rootNode.CREATE )

    self.obj1179=hasAttribute_T(self)
    self.obj1179.isGraphObjectVisual = True

    if(hasattr(self.obj1179, '_setHierarchicalLink')):
      self.obj1179._setHierarchicalLink(False)

    self.obj1179.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,512.5,self.obj1179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1179)
    self.globalAndLocalPostcondition(self.obj1179, rootNode)
    self.obj1179.postAction( rootNode.CREATE )

    self.obj1180=hasAttribute_T(self)
    self.obj1180.isGraphObjectVisual = True

    if(hasattr(self.obj1180, '_setHierarchicalLink')):
      self.obj1180._setHierarchicalLink(False)

    self.obj1180.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(653.0,602.5,self.obj1180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1180)
    self.globalAndLocalPostcondition(self.obj1180, rootNode)
    self.obj1180.postAction( rootNode.CREATE )

    self.obj1181=leftExpr(self)
    self.obj1181.isGraphObjectVisual = True

    if(hasattr(self.obj1181, '_setHierarchicalLink')):
      self.obj1181._setHierarchicalLink(False)

    self.obj1181.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,213.5,self.obj1181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1181)
    self.globalAndLocalPostcondition(self.obj1181, rootNode)
    self.obj1181.postAction( rootNode.CREATE )

    self.obj1182=leftExpr(self)
    self.obj1182.isGraphObjectVisual = True

    if(hasattr(self.obj1182, '_setHierarchicalLink')):
      self.obj1182._setHierarchicalLink(False)

    self.obj1182.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(746.0,326.5,self.obj1182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1182)
    self.globalAndLocalPostcondition(self.obj1182, rootNode)
    self.obj1182.postAction( rootNode.CREATE )

    self.obj1183=leftExpr(self)
    self.obj1183.isGraphObjectVisual = True

    if(hasattr(self.obj1183, '_setHierarchicalLink')):
      self.obj1183._setHierarchicalLink(False)

    self.obj1183.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1052.0,380.5,self.obj1183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1183)
    self.globalAndLocalPostcondition(self.obj1183, rootNode)
    self.obj1183.postAction( rootNode.CREATE )

    self.obj1184=leftExpr(self)
    self.obj1184.isGraphObjectVisual = True

    if(hasattr(self.obj1184, '_setHierarchicalLink')):
      self.obj1184._setHierarchicalLink(False)

    self.obj1184.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1056.0,596.5,self.obj1184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1184)
    self.globalAndLocalPostcondition(self.obj1184, rootNode)
    self.obj1184.postAction( rootNode.CREATE )

    self.obj1185=leftExpr(self)
    self.obj1185.isGraphObjectVisual = True

    if(hasattr(self.obj1185, '_setHierarchicalLink')):
      self.obj1185._setHierarchicalLink(False)

    self.obj1185.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(356.0,636.5,self.obj1185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1185.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1185)
    self.globalAndLocalPostcondition(self.obj1185, rootNode)
    self.obj1185.postAction( rootNode.CREATE )

    self.obj1186=leftExpr(self)
    self.obj1186.isGraphObjectVisual = True

    if(hasattr(self.obj1186, '_setHierarchicalLink')):
      self.obj1186._setHierarchicalLink(False)

    self.obj1186.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(666.0,696.5,self.obj1186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1186)
    self.globalAndLocalPostcondition(self.obj1186, rootNode)
    self.obj1186.postAction( rootNode.CREATE )

    self.obj1187=rightExpr(self)
    self.obj1187.isGraphObjectVisual = True

    if(hasattr(self.obj1187, '_setHierarchicalLink')):
      self.obj1187._setHierarchicalLink(False)

    self.obj1187.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(457.0,212.5,self.obj1187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1187)
    self.globalAndLocalPostcondition(self.obj1187, rootNode)
    self.obj1187.postAction( rootNode.CREATE )

    self.obj1188=rightExpr(self)
    self.obj1188.isGraphObjectVisual = True

    if(hasattr(self.obj1188, '_setHierarchicalLink')):
      self.obj1188._setHierarchicalLink(False)

    self.obj1188.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(746.0,276.5,self.obj1188)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1188.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1188)
    self.globalAndLocalPostcondition(self.obj1188, rootNode)
    self.obj1188.postAction( rootNode.CREATE )

    self.obj1189=rightExpr(self)
    self.obj1189.isGraphObjectVisual = True

    if(hasattr(self.obj1189, '_setHierarchicalLink')):
      self.obj1189._setHierarchicalLink(False)

    self.obj1189.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1126.0,396.5,self.obj1189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1189)
    self.globalAndLocalPostcondition(self.obj1189, rootNode)
    self.obj1189.postAction( rootNode.CREATE )

    self.obj1190=rightExpr(self)
    self.obj1190.isGraphObjectVisual = True

    if(hasattr(self.obj1190, '_setHierarchicalLink')):
      self.obj1190._setHierarchicalLink(False)

    self.obj1190.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1136.0,596.5,self.obj1190)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1190.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1190)
    self.globalAndLocalPostcondition(self.obj1190, rootNode)
    self.obj1190.postAction( rootNode.CREATE )

    self.obj1191=rightExpr(self)
    self.obj1191.isGraphObjectVisual = True

    if(hasattr(self.obj1191, '_setHierarchicalLink')):
      self.obj1191._setHierarchicalLink(False)

    self.obj1191.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(436.0,636.5,self.obj1191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1191.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1191)
    self.globalAndLocalPostcondition(self.obj1191, rootNode)
    self.obj1191.postAction( rootNode.CREATE )

    self.obj1192=rightExpr(self)
    self.obj1192.isGraphObjectVisual = True

    if(hasattr(self.obj1192, '_setHierarchicalLink')):
      self.obj1192._setHierarchicalLink(False)

    self.obj1192.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(746.0,696.5,self.obj1192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1192.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1192)
    self.globalAndLocalPostcondition(self.obj1192, rootNode)
    self.obj1192.postAction( rootNode.CREATE )

    self.obj1193=hasArgs(self)
    self.obj1193.isGraphObjectVisual = True

    if(hasattr(self.obj1193, '_setHierarchicalLink')):
      self.obj1193._setHierarchicalLink(False)

    self.obj1193.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(744.0,234.0,self.obj1193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1193.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1193)
    self.globalAndLocalPostcondition(self.obj1193, rootNode)
    self.obj1193.postAction( rootNode.CREATE )

    self.obj1194=hasArgs(self)
    self.obj1194.isGraphObjectVisual = True

    if(hasattr(self.obj1194, '_setHierarchicalLink')):
      self.obj1194._setHierarchicalLink(False)

    self.obj1194.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(744.0,184.0,self.obj1194)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1194.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1194)
    self.globalAndLocalPostcondition(self.obj1194, rootNode)
    self.obj1194.postAction( rootNode.CREATE )

    # Connections for obj1131 (graphObject_: Obj452) of type MatchModel
    self.drawConnections(
(self.obj1131,self.obj1160,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj1131,self.obj1161,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj1131,self.obj1162,[138.0, 51.0, 394.0, 67.0],"true", 2) )
    # Connections for obj1132 (graphObject_: Obj453) of type ApplyModel
    self.drawConnections(
(self.obj1132,self.obj1163,[143.0, 333.0, 247.5, 375.0],"true", 2),
(self.obj1132,self.obj1164,[143.0, 333.0, 377.5, 374.0],"true", 2),
(self.obj1132,self.obj1165,[143.0, 333.0, 487.5, 382.0],"true", 2),
(self.obj1132,self.obj1166,[143.0, 333.0, 219.5, 486.0],"true", 2),
(self.obj1132,self.obj1167,[143.0, 333.0, 507.5, 442.0],"true", 2) )
    # Connections for obj1133 (graphObject_: Obj454) named exitpoint1
    self.drawConnections(
(self.obj1133,self.obj1175,[650.0, 83.0, 742.0, 108.5],"true", 2) )
    # Connections for obj1134 (graphObject_: Obj455) named state1
    self.drawConnections(
(self.obj1134,self.obj1172,[350.0, 83.0, 500.0, 83.0],"true", 2),
(self.obj1134,self.obj1174,[350.0, 83.0, 328.0, 136.5],"true", 2) )
    # Connections for obj1135 (graphObject_: Obj456) named procdef1
    self.drawConnections(
(self.obj1135,self.obj1176,[632.0, 431.0, 634.0, 364.5],"true", 2),
(self.obj1135,self.obj1169,[632.0, 431.0, 752.0, 431.0],"true", 2),
(self.obj1135,self.obj1170,[632.0, 431.0, 652.0, 491.0],"true", 2) )
    # Connections for obj1136 (graphObject_: Obj457) named name1
    self.drawConnections(
(self.obj1136,self.obj1177,[832.0, 431.0, 913.0, 432.5],"true", 2) )
    # Connections for obj1137 (graphObject_: Obj458) named triggerT1
    self.drawConnections(
(self.obj1137,self.obj1178,[872.0, 551.0, 943.0, 552.5],"true", 2) )
    # Connections for obj1138 (graphObject_: Obj459) named par1
    self.drawConnections(
(self.obj1138,self.obj1171,[672.0, 551.0, 772.0, 551.0],"true", 2),
(self.obj1138,self.obj1180,[672.0, 551.0, 653.0, 602.5],"true", 2) )
    # Connections for obj1139 (graphObject_: Obj460) named localdef1
    self.drawConnections(
(self.obj1139,self.obj1168,[392.0, 431.0, 431.0, 427.0],"true", 2),
(self.obj1139,self.obj1173,[392.0, 431.0, 371.0, 257.0],"true", 2),
(self.obj1139,self.obj1179,[392.0, 431.0, 353.0, 512.5],"true", 2) )
    # Connections for obj1140 (graphObject_: Obj461) named isComposite
    self.drawConnections(
 )
    # Connections for obj1141 (graphObject_: Obj462) named name
    self.drawConnections(
 )
    # Connections for obj1142 (graphObject_: Obj463) named name
    self.drawConnections(
 )
    # Connections for obj1143 (graphObject_: Obj464) named literal
    self.drawConnections(
 )
    # Connections for obj1144 (graphObject_: Obj465) named channel
    self.drawConnections(
 )
    # Connections for obj1145 (graphObject_: Obj466) named pivotin
    self.drawConnections(
 )
    # Connections for obj1146 (graphObject_: Obj467) named pivotout
    self.drawConnections(
 )
    # Connections for obj1147 (graphObject_: Obj468) named eq1
    self.drawConnections(
(self.obj1147,self.obj1181,[438.0, 259.0, 359.0, 213.5],"true", 2),
(self.obj1147,self.obj1187,[438.0, 259.0, 457.0, 212.5],"true", 2) )
    # Connections for obj1148 (graphObject_: Obj469) named eq2
    self.drawConnections(
(self.obj1148,self.obj1188,[838.0, 319.0, 746.0, 276.5],"true", 2),
(self.obj1148,self.obj1182,[838.0, 319.0, 746.0, 326.5],"true", 2) )
    # Connections for obj1149 (graphObject_: Obj470) named eq3
    self.drawConnections(
(self.obj1149,self.obj1183,[1098.0, 359.0, 1052.0, 380.5],"true", 2),
(self.obj1149,self.obj1189,[1098.0, 359.0, 1126.0, 396.5],"true", 2) )
    # Connections for obj1150 (graphObject_: Obj471) named eq4
    self.drawConnections(
(self.obj1150,self.obj1184,[1098.0, 639.0, 1056.0, 596.5],"true", 2),
(self.obj1150,self.obj1190,[1098.0, 639.0, 1136.0, 596.5],"true", 2) )
    # Connections for obj1151 (graphObject_: Obj472) named eq5
    self.drawConnections(
(self.obj1151,self.obj1185,[398.0, 679.0, 356.0, 636.5],"true", 2),
(self.obj1151,self.obj1191,[398.0, 679.0, 436.0, 636.5],"true", 2) )
    # Connections for obj1152 (graphObject_: Obj473) named eq6
    self.drawConnections(
(self.obj1152,self.obj1186,[698.0, 739.0, 666.0, 696.5],"true", 2),
(self.obj1152,self.obj1192,[698.0, 739.0, 746.0, 696.5],"true", 2) )
    # Connections for obj1153 (graphObject_: Obj474) named concat1
    self.drawConnections(
(self.obj1153,self.obj1193,[634.0, 234.0, 744.0, 234.0],"true", 2),
(self.obj1153,self.obj1194,[634.0, 234.0, 744.0, 184.0],"true", 2) )
    # Connections for obj1154 (graphObject_: Obj475) named true
    self.drawConnections(
 )
    # Connections for obj1155 (graphObject_: Obj476) named B
    self.drawConnections(
 )
    # Connections for obj1156 (graphObject_: Obj477) named sh_in
    self.drawConnections(
 )
    # Connections for obj1157 (graphObject_: Obj478) named sh_in
    self.drawConnections(
 )
    # Connections for obj1158 (graphObject_: Obj479) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj1159 (graphObject_: Obj480) named parexitpoint
    self.drawConnections(
 )
    # Connections for obj1160 (graphObject_: Obj481) of type paired_with
    self.drawConnections(
(self.obj1160,self.obj1132,[140.5, 152.0, 143.0, 333.0],"true", 2) )
    # Connections for obj1161 (graphObject_: Obj482) of type match_contains
    self.drawConnections(
(self.obj1161,self.obj1134,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj1162 (graphObject_: Obj483) of type match_contains
    self.drawConnections(
(self.obj1162,self.obj1133,[394.0, 67.0, 650.0, 83.0],"true", 2) )
    # Connections for obj1163 (graphObject_: Obj484) of type apply_contains
    self.drawConnections(
(self.obj1163,self.obj1139,[247.5, 375.0, 392.0, 431.0],"true", 2) )
    # Connections for obj1164 (graphObject_: Obj485) of type apply_contains
    self.drawConnections(
(self.obj1164,self.obj1135,[377.5, 374.0, 632.0, 431.0],"true", 2) )
    # Connections for obj1165 (graphObject_: Obj486) of type apply_contains
    self.drawConnections(
(self.obj1165,self.obj1136,[487.5, 382.0, 832.0, 431.0],"true", 2) )
    # Connections for obj1166 (graphObject_: Obj487) of type apply_contains
    self.drawConnections(
(self.obj1166,self.obj1138,[222.5, 542.0, 672.0, 551.0],"true", 2) )
    # Connections for obj1167 (graphObject_: Obj488) of type apply_contains
    self.drawConnections(
(self.obj1167,self.obj1137,[507.5, 442.0, 872.0, 551.0],"true", 2) )
    # Connections for obj1168 (graphObject_: Obj489) of type directLink_T
    self.drawConnections(
(self.obj1168,self.obj1135,[431.0, 427.0, 632.0, 431.0],"true", 2) )
    # Connections for obj1169 (graphObject_: Obj490) of type directLink_T
    self.drawConnections(
(self.obj1169,self.obj1136,[752.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj1170 (graphObject_: Obj491) of type directLink_T
    self.drawConnections(
(self.obj1170,self.obj1138,[652.0, 491.0, 672.0, 551.0],"true", 2) )
    # Connections for obj1171 (graphObject_: Obj492) of type directLink_T
    self.drawConnections(
(self.obj1171,self.obj1137,[772.0, 551.0, 872.0, 551.0],"true", 2) )
    # Connections for obj1172 (graphObject_: Obj493) of type directLink_S
    self.drawConnections(
(self.obj1172,self.obj1133,[500.0, 83.0, 650.0, 83.0],"true", 2) )
    # Connections for obj1173 (graphObject_: Obj494) of type backward_link
    self.drawConnections(
(self.obj1173,self.obj1134,[371.0, 257.0, 350.0, 83.0],"true", 2) )
    # Connections for obj1174 (graphObject_: Obj495) of type hasAttribute_S
    self.drawConnections(
(self.obj1174,self.obj1140,[328.0, 136.5, 314.0, 174.0],"true", 2) )
    # Connections for obj1175 (graphObject_: Obj496) of type hasAttribute_S
    self.drawConnections(
(self.obj1175,self.obj1141,[742.0, 108.5, 834.0, 134.0],"true", 2) )
    # Connections for obj1176 (graphObject_: Obj497) of type hasAttribute_T
    self.drawConnections(
(self.obj1176,self.obj1142,[634.0, 364.5, 634.0, 334.0],"true", 2) )
    # Connections for obj1177 (graphObject_: Obj498) of type hasAttribute_T
    self.drawConnections(
(self.obj1177,self.obj1143,[913.0, 432.5, 994.0, 434.0],"true", 2) )
    # Connections for obj1178 (graphObject_: Obj499) of type hasAttribute_T
    self.drawConnections(
(self.obj1178,self.obj1144,[943.0, 552.5, 1014.0, 554.0],"true", 2) )
    # Connections for obj1179 (graphObject_: Obj500) of type hasAttribute_T
    self.drawConnections(
(self.obj1179,self.obj1145,[353.0, 512.5, 314.0, 594.0],"true", 2) )
    # Connections for obj1180 (graphObject_: Obj501) of type hasAttribute_T
    self.drawConnections(
(self.obj1180,self.obj1146,[653.0, 602.5, 634.0, 654.0],"true", 2) )
    # Connections for obj1181 (graphObject_: Obj502) of type leftExpr
    self.drawConnections(
(self.obj1181,self.obj1140,[359.0, 213.5, 314.0, 174.0],"true", 2) )
    # Connections for obj1182 (graphObject_: Obj503) of type leftExpr
    self.drawConnections(
(self.obj1182,self.obj1142,[746.0, 326.5, 634.0, 334.0],"true", 2) )
    # Connections for obj1183 (graphObject_: Obj504) of type leftExpr
    self.drawConnections(
(self.obj1183,self.obj1143,[1046.0, 396.5, 994.0, 434.0],"true", 2) )
    # Connections for obj1184 (graphObject_: Obj505) of type leftExpr
    self.drawConnections(
(self.obj1184,self.obj1144,[1056.0, 596.5, 1014.0, 554.0],"true", 2) )
    # Connections for obj1185 (graphObject_: Obj506) of type leftExpr
    self.drawConnections(
(self.obj1185,self.obj1145,[356.0, 636.5, 314.0, 594.0],"true", 2) )
    # Connections for obj1186 (graphObject_: Obj507) of type leftExpr
    self.drawConnections(
(self.obj1186,self.obj1146,[666.0, 696.5, 634.0, 654.0],"true", 2) )
    # Connections for obj1187 (graphObject_: Obj508) of type rightExpr
    self.drawConnections(
(self.obj1187,self.obj1154,[457.0, 212.5, 474.0, 174.0],"true", 2) )
    # Connections for obj1188 (graphObject_: Obj509) of type rightExpr
    self.drawConnections(
(self.obj1188,self.obj1153,[746.0, 276.5, 634.0, 234.0],"true", 2) )
    # Connections for obj1189 (graphObject_: Obj510) of type rightExpr
    self.drawConnections(
(self.obj1189,self.obj1156,[1126.0, 396.5, 1154.0, 434.0],"true", 2) )
    # Connections for obj1190 (graphObject_: Obj511) of type rightExpr
    self.drawConnections(
(self.obj1190,self.obj1157,[1136.0, 596.5, 1174.0, 554.0],"true", 2) )
    # Connections for obj1191 (graphObject_: Obj512) of type rightExpr
    self.drawConnections(
(self.obj1191,self.obj1158,[436.0, 636.5, 474.0, 594.0],"true", 2) )
    # Connections for obj1192 (graphObject_: Obj513) of type rightExpr
    self.drawConnections(
(self.obj1192,self.obj1159,[746.0, 696.5, 794.0, 654.0],"true", 2) )
    # Connections for obj1193 (graphObject_: Obj514) of type hasArgs
    self.drawConnections(
(self.obj1193,self.obj1155,[744.0, 234.0, 834.0, 234.0],"true", 2) )
    # Connections for obj1194 (graphObject_: Obj515) of type hasArgs
    self.drawConnections(
(self.obj1194,self.obj1141,[744.0, 184.0, 834.0, 134.0],"true", 2) )

newfunction = ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
