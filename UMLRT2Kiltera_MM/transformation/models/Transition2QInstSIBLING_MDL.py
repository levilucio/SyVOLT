"""
__Transition2QInstSIBLING_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 15:13:49 2015
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from Vertex import *
from Transition import *
from StateMachine import *
from SIBLING0 import *
from Name import *
from Inst import *
from Attribute import *
from Equation import *
from Concat import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from directLink_S import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from hasArgs import *
from graph_StateMachine import *
from graph_Attribute import *
from graph_Vertex import *
from graph_Transition import *
from graph_paired_with import *
from graph_SIBLING0 import *
from graph_Equation import *
from graph_hasArgs import *
from graph_rightExpr import *
from graph_Concat import *
from graph_Inst import *
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

def Transition2QInstSIBLING_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2QInstSIBLING')
    # --- ASG attributes over ---


    self.obj1095=MatchModel(self)
    self.obj1095.isGraphObjectVisual = True

    if(hasattr(self.obj1095, '_setHierarchicalLink')):
      self.obj1095._setHierarchicalLink(False)

    self.obj1095.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1095)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1095.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1095)
    self.globalAndLocalPostcondition(self.obj1095, rootNode)
    self.obj1095.postAction( rootNode.CREATE )

    self.obj1096=ApplyModel(self)
    self.obj1096.isGraphObjectVisual = True

    if(hasattr(self.obj1096, '_setHierarchicalLink')):
      self.obj1096._setHierarchicalLink(False)

    self.obj1096.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,368.0,self.obj1096)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, -3.0]
    else: new_obj = None
    self.obj1096.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1096)
    self.globalAndLocalPostcondition(self.obj1096, rootNode)
    self.obj1096.postAction( rootNode.CREATE )

    self.obj1097=Vertex(self)
    self.obj1097.isGraphObjectVisual = True

    if(hasattr(self.obj1097, '_setHierarchicalLink')):
      self.obj1097._setHierarchicalLink(False)

    # name
    self.obj1097.name.setValue('vertex1')

    # classtype
    self.obj1097.classtype.setValue('Vertex')

    # cardinality
    self.obj1097.cardinality.setValue('1')

    self.obj1097.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(740.0,40.0,self.obj1097)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1097.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1097)
    self.globalAndLocalPostcondition(self.obj1097, rootNode)
    self.obj1097.postAction( rootNode.CREATE )

    self.obj1098=Transition(self)
    self.obj1098.isGraphObjectVisual = True

    if(hasattr(self.obj1098, '_setHierarchicalLink')):
      self.obj1098._setHierarchicalLink(False)

    # name
    self.obj1098.name.setValue('transition1')

    # classtype
    self.obj1098.classtype.setValue('Transition')

    # cardinality
    self.obj1098.cardinality.setValue('+')

    self.obj1098.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(180.0,40.0,self.obj1098)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1098.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1098)
    self.globalAndLocalPostcondition(self.obj1098, rootNode)
    self.obj1098.postAction( rootNode.CREATE )

    self.obj1099=StateMachine(self)
    self.obj1099.isGraphObjectVisual = True

    if(hasattr(self.obj1099, '_setHierarchicalLink')):
      self.obj1099._setHierarchicalLink(False)

    # name
    self.obj1099.name.setValue('stateMachine1')

    # classtype
    self.obj1099.classtype.setValue('StateMachine')

    # cardinality
    self.obj1099.cardinality.setValue('1')

    self.obj1099.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(460.0,100.0,self.obj1099)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1099.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1099)
    self.globalAndLocalPostcondition(self.obj1099, rootNode)
    self.obj1099.postAction( rootNode.CREATE )

    self.obj1100=SIBLING0(self)
    self.obj1100.isGraphObjectVisual = True

    if(hasattr(self.obj1100, '_setHierarchicalLink')):
      self.obj1100._setHierarchicalLink(False)

    # classtype
    self.obj1100.classtype.setValue('SIBLING0')

    # cardinality
    self.obj1100.cardinality.setValue('1')

    # name
    self.obj1100.name.setValue('sibling0_1')

    self.obj1100.graphClass_= graph_SIBLING0
    if self.genGraphics:
       new_obj = graph_SIBLING0(180.0,160.0,self.obj1100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1100)
    self.globalAndLocalPostcondition(self.obj1100, rootNode)
    self.obj1100.postAction( rootNode.CREATE )

    self.obj1101=Name(self)
    self.obj1101.isGraphObjectVisual = True

    if(hasattr(self.obj1101, '_setHierarchicalLink')):
      self.obj1101._setHierarchicalLink(False)

    # classtype
    self.obj1101.classtype.setValue('Name')

    # cardinality
    self.obj1101.cardinality.setValue('1')

    # name
    self.obj1101.name.setValue('name1')

    self.obj1101.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(978.0,480.0,self.obj1101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1101)
    self.globalAndLocalPostcondition(self.obj1101, rootNode)
    self.obj1101.postAction( rootNode.CREATE )

    self.obj1102=Name(self)
    self.obj1102.isGraphObjectVisual = True

    if(hasattr(self.obj1102, '_setHierarchicalLink')):
      self.obj1102._setHierarchicalLink(False)

    # classtype
    self.obj1102.classtype.setValue('Name')

    # cardinality
    self.obj1102.cardinality.setValue('1')

    # name
    self.obj1102.name.setValue('name2')

    self.obj1102.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(796.0,540.0,self.obj1102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 13.0]
    else: new_obj = None
    self.obj1102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1102)
    self.globalAndLocalPostcondition(self.obj1102, rootNode)
    self.obj1102.postAction( rootNode.CREATE )

    self.obj1103=Name(self)
    self.obj1103.isGraphObjectVisual = True

    if(hasattr(self.obj1103, '_setHierarchicalLink')):
      self.obj1103._setHierarchicalLink(False)

    # classtype
    self.obj1103.classtype.setValue('Name')

    # cardinality
    self.obj1103.cardinality.setValue('1')

    # name
    self.obj1103.name.setValue('name3')

    self.obj1103.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(615.0,590.0,self.obj1103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1103)
    self.globalAndLocalPostcondition(self.obj1103, rootNode)
    self.obj1103.postAction( rootNode.CREATE )

    self.obj1104=Name(self)
    self.obj1104.isGraphObjectVisual = True

    if(hasattr(self.obj1104, '_setHierarchicalLink')):
      self.obj1104._setHierarchicalLink(False)

    # classtype
    self.obj1104.classtype.setValue('Name')

    # cardinality
    self.obj1104.cardinality.setValue('1')

    # name
    self.obj1104.name.setValue('name4')

    self.obj1104.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(434.0,610.0,self.obj1104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1104)
    self.globalAndLocalPostcondition(self.obj1104, rootNode)
    self.obj1104.postAction( rootNode.CREATE )

    self.obj1105=Inst(self)
    self.obj1105.isGraphObjectVisual = True

    if(hasattr(self.obj1105, '_setHierarchicalLink')):
      self.obj1105._setHierarchicalLink(False)

    # classtype
    self.obj1105.classtype.setValue('Inst')

    # cardinality
    self.obj1105.cardinality.setValue('1')

    # name
    self.obj1105.name.setValue('inst1')

    self.obj1105.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(160.0,480.0,self.obj1105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, 0.0]
    else: new_obj = None
    self.obj1105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1105)
    self.globalAndLocalPostcondition(self.obj1105, rootNode)
    self.obj1105.postAction( rootNode.CREATE )

    self.obj1106=Attribute(self)
    self.obj1106.isGraphObjectVisual = True

    if(hasattr(self.obj1106, '_setHierarchicalLink')):
      self.obj1106._setHierarchicalLink(False)

    # Type
    self.obj1106.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1106.Type.config = 0

    # name
    self.obj1106.name.setValue('name')

    self.obj1106.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(760.0,160.0,self.obj1106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1106)
    self.globalAndLocalPostcondition(self.obj1106, rootNode)
    self.obj1106.postAction( rootNode.CREATE )

    self.obj1107=Attribute(self)
    self.obj1107.isGraphObjectVisual = True

    if(hasattr(self.obj1107, '_setHierarchicalLink')):
      self.obj1107._setHierarchicalLink(False)

    # Type
    self.obj1107.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1107.Type.config = 0

    # name
    self.obj1107.name.setValue('name')

    self.obj1107.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,192.0,self.obj1107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 3.0]
    else: new_obj = None
    self.obj1107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1107)
    self.globalAndLocalPostcondition(self.obj1107, rootNode)
    self.obj1107.postAction( rootNode.CREATE )

    self.obj1108=Attribute(self)
    self.obj1108.isGraphObjectVisual = True

    if(hasattr(self.obj1108, '_setHierarchicalLink')):
      self.obj1108._setHierarchicalLink(False)

    # Type
    self.obj1108.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1108.Type.config = 0

    # name
    self.obj1108.name.setValue('name')

    self.obj1108.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(220.0,400.0,self.obj1108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 2.0]
    else: new_obj = None
    self.obj1108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1108)
    self.globalAndLocalPostcondition(self.obj1108, rootNode)
    self.obj1108.postAction( rootNode.CREATE )

    self.obj1109=Attribute(self)
    self.obj1109.isGraphObjectVisual = True

    if(hasattr(self.obj1109, '_setHierarchicalLink')):
      self.obj1109._setHierarchicalLink(False)

    # Type
    self.obj1109.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1109.Type.config = 0

    # name
    self.obj1109.name.setValue('literal')

    self.obj1109.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(975.0,593.0,self.obj1109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [3.0, -1.0]
    else: new_obj = None
    self.obj1109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1109)
    self.globalAndLocalPostcondition(self.obj1109, rootNode)
    self.obj1109.postAction( rootNode.CREATE )

    self.obj1110=Attribute(self)
    self.obj1110.isGraphObjectVisual = True

    if(hasattr(self.obj1110, '_setHierarchicalLink')):
      self.obj1110._setHierarchicalLink(False)

    # Type
    self.obj1110.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1110.Type.config = 0

    # name
    self.obj1110.name.setValue('literal')

    self.obj1110.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(800.0,646.0,self.obj1110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj1110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1110)
    self.globalAndLocalPostcondition(self.obj1110, rootNode)
    self.obj1110.postAction( rootNode.CREATE )

    self.obj1111=Attribute(self)
    self.obj1111.isGraphObjectVisual = True

    if(hasattr(self.obj1111, '_setHierarchicalLink')):
      self.obj1111._setHierarchicalLink(False)

    # Type
    self.obj1111.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1111.Type.config = 0

    # name
    self.obj1111.name.setValue('literal')

    self.obj1111.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,420.0,self.obj1111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1111)
    self.globalAndLocalPostcondition(self.obj1111, rootNode)
    self.obj1111.postAction( rootNode.CREATE )

    self.obj1112=Attribute(self)
    self.obj1112.isGraphObjectVisual = True

    if(hasattr(self.obj1112, '_setHierarchicalLink')):
      self.obj1112._setHierarchicalLink(False)

    # Type
    self.obj1112.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1112.Type.config = 0

    # name
    self.obj1112.name.setValue('literal')

    self.obj1112.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(429.0,711.0,self.obj1112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1112)
    self.globalAndLocalPostcondition(self.obj1112, rootNode)
    self.obj1112.postAction( rootNode.CREATE )

    self.obj1113=Attribute(self)
    self.obj1113.isGraphObjectVisual = True

    if(hasattr(self.obj1113, '_setHierarchicalLink')):
      self.obj1113._setHierarchicalLink(False)

    # Type
    self.obj1113.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1113.Type.config = 0

    # name
    self.obj1113.name.setValue('pivot')

    self.obj1113.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(20.0,560.0,self.obj1113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1113)
    self.globalAndLocalPostcondition(self.obj1113, rootNode)
    self.obj1113.postAction( rootNode.CREATE )

    self.obj1114=Equation(self)
    self.obj1114.isGraphObjectVisual = True

    if(hasattr(self.obj1114, '_setHierarchicalLink')):
      self.obj1114._setHierarchicalLink(False)

    # name
    self.obj1114.name.setValue('eq1')

    self.obj1114.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(226.0,327.0,self.obj1114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 6.0]
    else: new_obj = None
    self.obj1114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1114)
    self.globalAndLocalPostcondition(self.obj1114, rootNode)
    self.obj1114.postAction( rootNode.CREATE )

    self.obj1115=Equation(self)
    self.obj1115.isGraphObjectVisual = True

    if(hasattr(self.obj1115, '_setHierarchicalLink')):
      self.obj1115._setHierarchicalLink(False)

    # name
    self.obj1115.name.setValue('eq2')

    self.obj1115.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1147.0,594.0,self.obj1115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-7.0, 3.0]
    else: new_obj = None
    self.obj1115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1115)
    self.globalAndLocalPostcondition(self.obj1115, rootNode)
    self.obj1115.postAction( rootNode.CREATE )

    self.obj1116=Equation(self)
    self.obj1116.isGraphObjectVisual = True

    if(hasattr(self.obj1116, '_setHierarchicalLink')):
      self.obj1116._setHierarchicalLink(False)

    # name
    self.obj1116.name.setValue('eq3')

    self.obj1116.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(975.0,683.0,self.obj1116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1116)
    self.globalAndLocalPostcondition(self.obj1116, rootNode)
    self.obj1116.postAction( rootNode.CREATE )

    self.obj1117=Equation(self)
    self.obj1117.isGraphObjectVisual = True

    if(hasattr(self.obj1117, '_setHierarchicalLink')):
      self.obj1117._setHierarchicalLink(False)

    # name
    self.obj1117.name.setValue('eq4')

    self.obj1117.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(788.0,428.0,self.obj1117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj1117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1117)
    self.globalAndLocalPostcondition(self.obj1117, rootNode)
    self.obj1117.postAction( rootNode.CREATE )

    self.obj1118=Equation(self)
    self.obj1118.isGraphObjectVisual = True

    if(hasattr(self.obj1118, '_setHierarchicalLink')):
      self.obj1118._setHierarchicalLink(False)

    # name
    self.obj1118.name.setValue('eq5')

    self.obj1118.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(264.0,724.0,self.obj1118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1118)
    self.globalAndLocalPostcondition(self.obj1118, rootNode)
    self.obj1118.postAction( rootNode.CREATE )

    self.obj1119=Equation(self)
    self.obj1119.isGraphObjectVisual = True

    if(hasattr(self.obj1119, '_setHierarchicalLink')):
      self.obj1119._setHierarchicalLink(False)

    # name
    self.obj1119.name.setValue('eq6')

    self.obj1119.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(180.0,580.0,self.obj1119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1119)
    self.globalAndLocalPostcondition(self.obj1119, rootNode)
    self.obj1119.postAction( rootNode.CREATE )

    self.obj1120=Concat(self)
    self.obj1120.isGraphObjectVisual = True

    if(hasattr(self.obj1120, '_setHierarchicalLink')):
      self.obj1120._setHierarchicalLink(False)

    # Type
    self.obj1120.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1120.Type.config = 0

    # name
    self.obj1120.name.setValue('concat1')

    self.obj1120.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(396.0,327.0,self.obj1120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1120)
    self.globalAndLocalPostcondition(self.obj1120, rootNode)
    self.obj1120.postAction( rootNode.CREATE )

    self.obj1121=Concat(self)
    self.obj1121.isGraphObjectVisual = True

    if(hasattr(self.obj1121, '_setHierarchicalLink')):
      self.obj1121._setHierarchicalLink(False)

    # Type
    self.obj1121.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1121.Type.config = 0

    # name
    self.obj1121.name.setValue('concat2')

    self.obj1121.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(792.0,324.0,self.obj1121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [5.0, -2.0]
    else: new_obj = None
    self.obj1121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1121)
    self.globalAndLocalPostcondition(self.obj1121, rootNode)
    self.obj1121.postAction( rootNode.CREATE )

    self.obj1122=Constant(self)
    self.obj1122.isGraphObjectVisual = True

    if(hasattr(self.obj1122, '_setHierarchicalLink')):
      self.obj1122._setHierarchicalLink(False)

    # Type
    self.obj1122.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1122.Type.config = 0

    # name
    self.obj1122.name.setValue('S')

    self.obj1122.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(333.0,251.0,self.obj1122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1122)
    self.globalAndLocalPostcondition(self.obj1122, rootNode)
    self.obj1122.postAction( rootNode.CREATE )

    self.obj1123=Constant(self)
    self.obj1123.isGraphObjectVisual = True

    if(hasattr(self.obj1123, '_setHierarchicalLink')):
      self.obj1123._setHierarchicalLink(False)

    # Type
    self.obj1123.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1123.Type.config = 0

    # name
    self.obj1123.name.setValue('exit')

    self.obj1123.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1140.0,674.0,self.obj1123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, -4.0]
    else: new_obj = None
    self.obj1123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1123)
    self.globalAndLocalPostcondition(self.obj1123, rootNode)
    self.obj1123.postAction( rootNode.CREATE )

    self.obj1124=Constant(self)
    self.obj1124.isGraphObjectVisual = True

    if(hasattr(self.obj1124, '_setHierarchicalLink')):
      self.obj1124._setHierarchicalLink(False)

    # Type
    self.obj1124.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1124.Type.config = 0

    # name
    self.obj1124.name.setValue('exack')

    self.obj1124.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,723.0,self.obj1124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1124)
    self.globalAndLocalPostcondition(self.obj1124, rootNode)
    self.obj1124.postAction( rootNode.CREATE )

    self.obj1125=Constant(self)
    self.obj1125.isGraphObjectVisual = True

    if(hasattr(self.obj1125, '_setHierarchicalLink')):
      self.obj1125._setHierarchicalLink(False)

    # Type
    self.obj1125.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1125.Type.config = 0

    # name
    self.obj1125.name.setValue('1')

    self.obj1125.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(648.0,250.0,self.obj1125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1125)
    self.globalAndLocalPostcondition(self.obj1125, rootNode)
    self.obj1125.postAction( rootNode.CREATE )

    self.obj1126=Constant(self)
    self.obj1126.isGraphObjectVisual = True

    if(hasattr(self.obj1126, '_setHierarchicalLink')):
      self.obj1126._setHierarchicalLink(False)

    # Type
    self.obj1126.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1126.Type.config = 0

    # name
    self.obj1126.name.setValue('2')

    self.obj1126.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(936.0,246.0,self.obj1126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1126)
    self.globalAndLocalPostcondition(self.obj1126, rootNode)
    self.obj1126.postAction( rootNode.CREATE )

    self.obj1127=Constant(self)
    self.obj1127.isGraphObjectVisual = True

    if(hasattr(self.obj1127, '_setHierarchicalLink')):
      self.obj1127._setHierarchicalLink(False)

    # Type
    self.obj1127.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1127.Type.config = 0

    # name
    self.obj1127.name.setValue('sh')

    self.obj1127.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,786.0,self.obj1127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1127)
    self.globalAndLocalPostcondition(self.obj1127, rootNode)
    self.obj1127.postAction( rootNode.CREATE )

    self.obj1128=Constant(self)
    self.obj1128.isGraphObjectVisual = True

    if(hasattr(self.obj1128, '_setHierarchicalLink')):
      self.obj1128._setHierarchicalLink(False)

    # Type
    self.obj1128.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1128.Type.config = 0

    # name
    self.obj1128.name.setValue('instfortrans')

    self.obj1128.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(21.0,640.0,self.obj1128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1128)
    self.globalAndLocalPostcondition(self.obj1128, rootNode)
    self.obj1128.postAction( rootNode.CREATE )

    self.obj1129=paired_with(self)
    self.obj1129.isGraphObjectVisual = True

    if(hasattr(self.obj1129, '_setHierarchicalLink')):
      self.obj1129._setHierarchicalLink(False)

    self.obj1129.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,182.0,self.obj1129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1129)
    self.globalAndLocalPostcondition(self.obj1129, rootNode)
    self.obj1129.postAction( rootNode.CREATE )

    self.obj1130=match_contains(self)
    self.obj1130.isGraphObjectVisual = True

    if(hasattr(self.obj1130, '_setHierarchicalLink')):
      self.obj1130._setHierarchicalLink(False)

    self.obj1130.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj1130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1130)
    self.globalAndLocalPostcondition(self.obj1130, rootNode)
    self.obj1130.postAction( rootNode.CREATE )

    self.obj1131=match_contains(self)
    self.obj1131.isGraphObjectVisual = True

    if(hasattr(self.obj1131, '_setHierarchicalLink')):
      self.obj1131._setHierarchicalLink(False)

    self.obj1131.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,127.0,self.obj1131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1131)
    self.globalAndLocalPostcondition(self.obj1131, rootNode)
    self.obj1131.postAction( rootNode.CREATE )

    self.obj1132=match_contains(self)
    self.obj1132.isGraphObjectVisual = True

    if(hasattr(self.obj1132, '_setHierarchicalLink')):
      self.obj1132._setHierarchicalLink(False)

    self.obj1132.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,97.0,self.obj1132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1132)
    self.globalAndLocalPostcondition(self.obj1132, rootNode)
    self.obj1132.postAction( rootNode.CREATE )

    self.obj1133=match_contains(self)
    self.obj1133.isGraphObjectVisual = True

    if(hasattr(self.obj1133, '_setHierarchicalLink')):
      self.obj1133._setHierarchicalLink(False)

    self.obj1133.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(524.0,67.0,self.obj1133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1133)
    self.globalAndLocalPostcondition(self.obj1133, rootNode)
    self.obj1133.postAction( rootNode.CREATE )

    self.obj1134=apply_contains(self)
    self.obj1134.isGraphObjectVisual = True

    if(hasattr(self.obj1134, '_setHierarchicalLink')):
      self.obj1134._setHierarchicalLink(False)

    self.obj1134.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(237.5,466.0,self.obj1134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1134)
    self.globalAndLocalPostcondition(self.obj1134, rootNode)
    self.obj1134.postAction( rootNode.CREATE )

    self.obj1135=apply_contains(self)
    self.obj1135.isGraphObjectVisual = True

    if(hasattr(self.obj1135, '_setHierarchicalLink')):
      self.obj1135._setHierarchicalLink(False)

    self.obj1135.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(374.5,531.0,self.obj1135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1135)
    self.globalAndLocalPostcondition(self.obj1135, rootNode)
    self.obj1135.postAction( rootNode.CREATE )

    self.obj1136=apply_contains(self)
    self.obj1136.isGraphObjectVisual = True

    if(hasattr(self.obj1136, '_setHierarchicalLink')):
      self.obj1136._setHierarchicalLink(False)

    self.obj1136.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(465.0,521.0,self.obj1136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1136)
    self.globalAndLocalPostcondition(self.obj1136, rootNode)
    self.obj1136.postAction( rootNode.CREATE )

    self.obj1137=apply_contains(self)
    self.obj1137.isGraphObjectVisual = True

    if(hasattr(self.obj1137, '_setHierarchicalLink')):
      self.obj1137._setHierarchicalLink(False)

    self.obj1137.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(555.5,496.0,self.obj1137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1137)
    self.globalAndLocalPostcondition(self.obj1137, rootNode)
    self.obj1137.postAction( rootNode.CREATE )

    self.obj1138=apply_contains(self)
    self.obj1138.isGraphObjectVisual = True

    if(hasattr(self.obj1138, '_setHierarchicalLink')):
      self.obj1138._setHierarchicalLink(False)

    self.obj1138.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(646.5,466.0,self.obj1138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1138)
    self.globalAndLocalPostcondition(self.obj1138, rootNode)
    self.obj1138.postAction( rootNode.CREATE )

    self.obj1139=directLink_T(self)
    self.obj1139.isGraphObjectVisual = True

    if(hasattr(self.obj1139, '_setHierarchicalLink')):
      self.obj1139._setHierarchicalLink(False)

    # associationType
    self.obj1139.associationType.setValue('channelNames')

    self.obj1139.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(522.0,531.0,self.obj1139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1139)
    self.globalAndLocalPostcondition(self.obj1139, rootNode)
    self.obj1139.postAction( rootNode.CREATE )

    self.obj1140=directLink_T(self)
    self.obj1140.isGraphObjectVisual = True

    if(hasattr(self.obj1140, '_setHierarchicalLink')):
      self.obj1140._setHierarchicalLink(False)

    # associationType
    self.obj1140.associationType.setValue('channelNames')

    self.obj1140.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(645.5,566.0,self.obj1140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1140)
    self.globalAndLocalPostcondition(self.obj1140, rootNode)
    self.obj1140.postAction( rootNode.CREATE )

    self.obj1141=directLink_T(self)
    self.obj1141.isGraphObjectVisual = True

    if(hasattr(self.obj1141, '_setHierarchicalLink')):
      self.obj1141._setHierarchicalLink(False)

    # associationType
    self.obj1141.associationType.setValue('channelNames')

    self.obj1141.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(553.0,586.0,self.obj1141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1141)
    self.globalAndLocalPostcondition(self.obj1141, rootNode)
    self.obj1141.postAction( rootNode.CREATE )

    self.obj1142=directLink_T(self)
    self.obj1142.isGraphObjectVisual = True

    if(hasattr(self.obj1142, '_setHierarchicalLink')):
      self.obj1142._setHierarchicalLink(False)

    # associationType
    self.obj1142.associationType.setValue('channelNames')

    self.obj1142.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(469.0,596.0,self.obj1142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1142)
    self.globalAndLocalPostcondition(self.obj1142, rootNode)
    self.obj1142.postAction( rootNode.CREATE )

    self.obj1143=directLink_S(self)
    self.obj1143.isGraphObjectVisual = True

    if(hasattr(self.obj1143, '_setHierarchicalLink')):
      self.obj1143._setHierarchicalLink(False)

    # associationType
    self.obj1143.associationType.setValue('type')

    self.obj1143.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(350.0,153.0,self.obj1143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1143)
    self.globalAndLocalPostcondition(self.obj1143, rootNode)
    self.obj1143.postAction( rootNode.CREATE )

    self.obj1144=directLink_S(self)
    self.obj1144.isGraphObjectVisual = True

    if(hasattr(self.obj1144, '_setHierarchicalLink')):
      self.obj1144._setHierarchicalLink(False)

    # associationType
    self.obj1144.associationType.setValue('dest')

    self.obj1144.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(640.0,84.0,self.obj1144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1144)
    self.globalAndLocalPostcondition(self.obj1144, rootNode)
    self.obj1144.postAction( rootNode.CREATE )

    self.obj1145=directLink_S(self)
    self.obj1145.isGraphObjectVisual = True

    if(hasattr(self.obj1145, '_setHierarchicalLink')):
      self.obj1145._setHierarchicalLink(False)

    # associationType
    self.obj1145.associationType.setValue('owningStateMachine')

    self.obj1145.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(770.0,113.0,self.obj1145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1145)
    self.globalAndLocalPostcondition(self.obj1145, rootNode)
    self.obj1145.postAction( rootNode.CREATE )

    self.obj1146=hasAttribute_S(self)
    self.obj1146.isGraphObjectVisual = True

    if(hasattr(self.obj1146, '_setHierarchicalLink')):
      self.obj1146._setHierarchicalLink(False)

    self.obj1146.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(902.0,148.5,self.obj1146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1146)
    self.globalAndLocalPostcondition(self.obj1146, rootNode)
    self.obj1146.postAction( rootNode.CREATE )

    self.obj1147=hasAttribute_S(self)
    self.obj1147.isGraphObjectVisual = True

    if(hasattr(self.obj1147, '_setHierarchicalLink')):
      self.obj1147._setHierarchicalLink(False)

    self.obj1147.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(622.0,184.5,self.obj1147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1147)
    self.globalAndLocalPostcondition(self.obj1147, rootNode)
    self.obj1147.postAction( rootNode.CREATE )

    self.obj1148=hasAttribute_T(self)
    self.obj1148.isGraphObjectVisual = True

    if(hasattr(self.obj1148, '_setHierarchicalLink')):
      self.obj1148._setHierarchicalLink(False)

    self.obj1148.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(343.0,482.5,self.obj1148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1148)
    self.globalAndLocalPostcondition(self.obj1148, rootNode)
    self.obj1148.postAction( rootNode.CREATE )

    self.obj1149=hasAttribute_T(self)
    self.obj1149.isGraphObjectVisual = True

    if(hasattr(self.obj1149, '_setHierarchicalLink')):
      self.obj1149._setHierarchicalLink(False)

    self.obj1149.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1127.0,592.0,self.obj1149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1149)
    self.globalAndLocalPostcondition(self.obj1149, rootNode)
    self.obj1149.postAction( rootNode.CREATE )

    self.obj1150=hasAttribute_T(self)
    self.obj1150.isGraphObjectVisual = True

    if(hasattr(self.obj1150, '_setHierarchicalLink')):
      self.obj1150._setHierarchicalLink(False)

    self.obj1150.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(946.5,649.0,self.obj1150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1150)
    self.globalAndLocalPostcondition(self.obj1150, rootNode)
    self.obj1150.postAction( rootNode.CREATE )

    self.obj1151=hasAttribute_T(self)
    self.obj1151.isGraphObjectVisual = True

    if(hasattr(self.obj1151, '_setHierarchicalLink')):
      self.obj1151._setHierarchicalLink(False)

    self.obj1151.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(777.5,567.5,self.obj1151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1151)
    self.globalAndLocalPostcondition(self.obj1151, rootNode)
    self.obj1151.postAction( rootNode.CREATE )

    self.obj1152=hasAttribute_T(self)
    self.obj1152.isGraphObjectVisual = True

    if(hasattr(self.obj1152, '_setHierarchicalLink')):
      self.obj1152._setHierarchicalLink(False)

    self.obj1152.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(584.5,703.0,self.obj1152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1152)
    self.globalAndLocalPostcondition(self.obj1152, rootNode)
    self.obj1152.postAction( rootNode.CREATE )

    self.obj1153=hasAttribute_T(self)
    self.obj1153.isGraphObjectVisual = True

    if(hasattr(self.obj1153, '_setHierarchicalLink')):
      self.obj1153._setHierarchicalLink(False)

    self.obj1153.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(243.0,562.5,self.obj1153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1153)
    self.globalAndLocalPostcondition(self.obj1153, rootNode)
    self.obj1153.postAction( rootNode.CREATE )

    self.obj1154=leftExpr(self)
    self.obj1154.isGraphObjectVisual = True

    if(hasattr(self.obj1154, '_setHierarchicalLink')):
      self.obj1154._setHierarchicalLink(False)

    self.obj1154.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(358.0,403.5,self.obj1154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1154)
    self.globalAndLocalPostcondition(self.obj1154, rootNode)
    self.obj1154.postAction( rootNode.CREATE )

    self.obj1155=leftExpr(self)
    self.obj1155.isGraphObjectVisual = True

    if(hasattr(self.obj1155, '_setHierarchicalLink')):
      self.obj1155._setHierarchicalLink(False)

    self.obj1155.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,630.0,self.obj1155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1155)
    self.globalAndLocalPostcondition(self.obj1155, rootNode)
    self.obj1155.postAction( rootNode.CREATE )

    self.obj1156=leftExpr(self)
    self.obj1156.isGraphObjectVisual = True

    if(hasattr(self.obj1156, '_setHierarchicalLink')):
      self.obj1156._setHierarchicalLink(False)

    self.obj1156.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1023.5,709.5,self.obj1156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1156)
    self.globalAndLocalPostcondition(self.obj1156, rootNode)
    self.obj1156.postAction( rootNode.CREATE )

    self.obj1157=leftExpr(self)
    self.obj1157.isGraphObjectVisual = True

    if(hasattr(self.obj1157, '_setHierarchicalLink')):
      self.obj1157._setHierarchicalLink(False)

    self.obj1157.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(793.0,464.0,self.obj1157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1157)
    self.globalAndLocalPostcondition(self.obj1157, rootNode)
    self.obj1157.postAction( rootNode.CREATE )

    self.obj1158=leftExpr(self)
    self.obj1158.isGraphObjectVisual = True

    if(hasattr(self.obj1158, '_setHierarchicalLink')):
      self.obj1158._setHierarchicalLink(False)

    self.obj1158.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(482.5,754.0,self.obj1158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1158)
    self.globalAndLocalPostcondition(self.obj1158, rootNode)
    self.obj1158.postAction( rootNode.CREATE )

    self.obj1159=leftExpr(self)
    self.obj1159.isGraphObjectVisual = True

    if(hasattr(self.obj1159, '_setHierarchicalLink')):
      self.obj1159._setHierarchicalLink(False)

    self.obj1159.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(236.0,606.5,self.obj1159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1159)
    self.globalAndLocalPostcondition(self.obj1159, rootNode)
    self.obj1159.postAction( rootNode.CREATE )

    self.obj1160=rightExpr(self)
    self.obj1160.isGraphObjectVisual = True

    if(hasattr(self.obj1160, '_setHierarchicalLink')):
      self.obj1160._setHierarchicalLink(False)

    self.obj1160.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(447.0,363.5,self.obj1160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1160)
    self.globalAndLocalPostcondition(self.obj1160, rootNode)
    self.obj1160.postAction( rootNode.CREATE )

    self.obj1161=rightExpr(self)
    self.obj1161.isGraphObjectVisual = True

    if(hasattr(self.obj1161, '_setHierarchicalLink')):
      self.obj1161._setHierarchicalLink(False)

    self.obj1161.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1279.5,683.5,self.obj1161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1161)
    self.globalAndLocalPostcondition(self.obj1161, rootNode)
    self.obj1161.postAction( rootNode.CREATE )

    self.obj1162=rightExpr(self)
    self.obj1162.isGraphObjectVisual = True

    if(hasattr(self.obj1162, '_setHierarchicalLink')):
      self.obj1162._setHierarchicalLink(False)

    self.obj1162.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1023.5,753.5,self.obj1162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1162)
    self.globalAndLocalPostcondition(self.obj1162, rootNode)
    self.obj1162.postAction( rootNode.CREATE )

    self.obj1163=rightExpr(self)
    self.obj1163.isGraphObjectVisual = True

    if(hasattr(self.obj1163, '_setHierarchicalLink')):
      self.obj1163._setHierarchicalLink(False)

    self.obj1163.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(926.0,449.0,self.obj1163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1163)
    self.globalAndLocalPostcondition(self.obj1163, rootNode)
    self.obj1163.postAction( rootNode.CREATE )

    self.obj1164=rightExpr(self)
    self.obj1164.isGraphObjectVisual = True

    if(hasattr(self.obj1164, '_setHierarchicalLink')):
      self.obj1164._setHierarchicalLink(False)

    self.obj1164.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(478.0,791.5,self.obj1164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1164)
    self.globalAndLocalPostcondition(self.obj1164, rootNode)
    self.obj1164.postAction( rootNode.CREATE )

    self.obj1165=rightExpr(self)
    self.obj1165.isGraphObjectVisual = True

    if(hasattr(self.obj1165, '_setHierarchicalLink')):
      self.obj1165._setHierarchicalLink(False)

    self.obj1165.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(236.5,646.5,self.obj1165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1165)
    self.globalAndLocalPostcondition(self.obj1165, rootNode)
    self.obj1165.postAction( rootNode.CREATE )

    self.obj1166=hasArgs(self)
    self.obj1166.isGraphObjectVisual = True

    if(hasattr(self.obj1166, '_setHierarchicalLink')):
      self.obj1166._setHierarchicalLink(False)

    self.obj1166.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(498.5,323.0,self.obj1166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1166)
    self.globalAndLocalPostcondition(self.obj1166, rootNode)
    self.obj1166.postAction( rootNode.CREATE )

    self.obj1167=hasArgs(self)
    self.obj1167.isGraphObjectVisual = True

    if(hasattr(self.obj1167, '_setHierarchicalLink')):
      self.obj1167._setHierarchicalLink(False)

    self.obj1167.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(572.0,293.5,self.obj1167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1167)
    self.globalAndLocalPostcondition(self.obj1167, rootNode)
    self.obj1167.postAction( rootNode.CREATE )

    self.obj1168=hasArgs(self)
    self.obj1168.isGraphObjectVisual = True

    if(hasattr(self.obj1168, '_setHierarchicalLink')):
      self.obj1168._setHierarchicalLink(False)

    self.obj1168.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(862.0,336.0,self.obj1168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1168)
    self.globalAndLocalPostcondition(self.obj1168, rootNode)
    self.obj1168.postAction( rootNode.CREATE )

    self.obj1169=hasArgs(self)
    self.obj1169.isGraphObjectVisual = True

    if(hasattr(self.obj1169, '_setHierarchicalLink')):
      self.obj1169._setHierarchicalLink(False)

    self.obj1169.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(910.0,298.0,self.obj1169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1169)
    self.globalAndLocalPostcondition(self.obj1169, rootNode)
    self.obj1169.postAction( rootNode.CREATE )

    self.obj1170=hasArgs(self)
    self.obj1170.isGraphObjectVisual = True

    if(hasattr(self.obj1170, '_setHierarchicalLink')):
      self.obj1170._setHierarchicalLink(False)

    self.obj1170.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(958.0,353.0,self.obj1170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1170)
    self.globalAndLocalPostcondition(self.obj1170, rootNode)
    self.obj1170.postAction( rootNode.CREATE )

    # Connections for obj1095 (graphObject_: Obj992) of type MatchModel
    self.drawConnections(
(self.obj1095,self.obj1129,[138.0, 51.0, 140.5, 182.0],"true", 2),
(self.obj1095,self.obj1130,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj1095,self.obj1131,[138.0, 51.0, 244.0, 127.0],"true", 2),
(self.obj1095,self.obj1132,[138.0, 51.0, 384.0, 97.0],"true", 2),
(self.obj1095,self.obj1133,[138.0, 51.0, 524.0, 67.0],"true", 2) )
    # Connections for obj1096 (graphObject_: Obj993) of type ApplyModel
    self.drawConnections(
(self.obj1096,self.obj1134,[143.0, 401.0, 237.5, 466.0],"true", 2),
(self.obj1096,self.obj1135,[143.0, 401.0, 374.5, 531.0],"true", 2),
(self.obj1096,self.obj1136,[143.0, 401.0, 465.0, 521.0],"true", 2),
(self.obj1096,self.obj1137,[143.0, 401.0, 555.5, 496.0],"true", 2),
(self.obj1096,self.obj1138,[143.0, 401.0, 646.5, 466.0],"true", 2) )
    # Connections for obj1097 (graphObject_: Obj994) named vertex1
    self.drawConnections(
(self.obj1097,self.obj1146,[910.0, 83.0, 902.0, 148.5],"true", 2),
(self.obj1097,self.obj1145,[910.0, 83.0, 770.0, 113.0],"true", 2) )
    # Connections for obj1098 (graphObject_: Obj995) named transition1
    self.drawConnections(
(self.obj1098,self.obj1143,[350.0, 83.0, 350.0, 153.0],"true", 2),
(self.obj1098,self.obj1144,[350.0, 83.0, 640.0, 84.0],"true", 2) )
    # Connections for obj1099 (graphObject_: Obj996) named stateMachine1
    self.drawConnections(
(self.obj1099,self.obj1147,[630.0, 143.0, 622.0, 184.5],"true", 2) )
    # Connections for obj1100 (graphObject_: Obj997) named sibling0_1
    self.drawConnections(
 )
    # Connections for obj1101 (graphObject_: Obj998) named name1
    self.drawConnections(
(self.obj1101,self.obj1149,[1150.0, 531.0, 1127.0, 592.0],"true", 2) )
    # Connections for obj1102 (graphObject_: Obj999) named name2
    self.drawConnections(
(self.obj1102,self.obj1150,[968.0, 591.0, 946.5, 649.0],"true", 2) )
    # Connections for obj1103 (graphObject_: Obj1000) named name3
    self.drawConnections(
(self.obj1103,self.obj1151,[787.0, 641.0, 777.5, 567.5],"true", 2) )
    # Connections for obj1104 (graphObject_: Obj1001) named name4
    self.drawConnections(
(self.obj1104,self.obj1152,[606.0, 661.0, 584.5, 703.0],"true", 2) )
    # Connections for obj1105 (graphObject_: Obj1002) named inst1
    self.drawConnections(
(self.obj1105,self.obj1148,[332.0, 531.0, 343.0, 482.5],"true", 2),
(self.obj1105,self.obj1139,[332.0, 531.0, 522.0, 531.0],"true", 2),
(self.obj1105,self.obj1140,[332.0, 531.0, 645.5, 566.0],"true", 2),
(self.obj1105,self.obj1141,[332.0, 531.0, 553.0, 586.0],"true", 2),
(self.obj1105,self.obj1142,[332.0, 531.0, 469.0, 596.0],"true", 2),
(self.obj1105,self.obj1153,[332.0, 531.0, 243.0, 562.5],"true", 2) )
    # Connections for obj1106 (graphObject_: Obj1003) named name
    self.drawConnections(
 )
    # Connections for obj1107 (graphObject_: Obj1004) named name
    self.drawConnections(
 )
    # Connections for obj1108 (graphObject_: Obj1005) named name
    self.drawConnections(
 )
    # Connections for obj1109 (graphObject_: Obj1006) named literal
    self.drawConnections(
 )
    # Connections for obj1110 (graphObject_: Obj1007) named literal
    self.drawConnections(
 )
    # Connections for obj1111 (graphObject_: Obj1008) named literal
    self.drawConnections(
 )
    # Connections for obj1112 (graphObject_: Obj1009) named literal
    self.drawConnections(
 )
    # Connections for obj1113 (graphObject_: Obj1010) named pivot
    self.drawConnections(
 )
    # Connections for obj1114 (graphObject_: Obj1011) named eq1
    self.drawConnections(
(self.obj1114,self.obj1154,[364.0, 366.0, 358.0, 403.5],"true", 2),
(self.obj1114,self.obj1160,[364.0, 366.0, 447.0, 363.5],"true", 2) )
    # Connections for obj1115 (graphObject_: Obj1012) named eq2
    self.drawConnections(
(self.obj1115,self.obj1155,[1285.0, 633.0, 1100.0, 630.0],"true", 2),
(self.obj1115,self.obj1161,[1285.0, 633.0, 1279.5, 683.5],"true", 2) )
    # Connections for obj1116 (graphObject_: Obj1013) named eq3
    self.drawConnections(
(self.obj1116,self.obj1156,[1113.0, 722.0, 1023.5, 709.5],"true", 2),
(self.obj1116,self.obj1162,[1113.0, 722.0, 1023.5, 753.5],"true", 2) )
    # Connections for obj1117 (graphObject_: Obj1014) named eq4
    self.drawConnections(
(self.obj1117,self.obj1157,[926.0, 467.0, 793.0, 464.0],"true", 2),
(self.obj1117,self.obj1163,[926.0, 467.0, 926.0, 449.0],"true", 2) )
    # Connections for obj1118 (graphObject_: Obj1015) named eq5
    self.drawConnections(
(self.obj1118,self.obj1158,[402.0, 763.0, 482.5, 754.0],"true", 2),
(self.obj1118,self.obj1164,[402.0, 763.0, 478.0, 791.5],"true", 2) )
    # Connections for obj1119 (graphObject_: Obj1016) named eq6
    self.drawConnections(
(self.obj1119,self.obj1165,[318.0, 619.0, 236.5, 646.5],"true", 2),
(self.obj1119,self.obj1159,[318.0, 619.0, 236.0, 606.5],"true", 2) )
    # Connections for obj1120 (graphObject_: Obj1017) named concat1
    self.drawConnections(
(self.obj1120,self.obj1166,[530.0, 361.0, 498.5, 323.0],"true", 2),
(self.obj1120,self.obj1167,[530.0, 361.0, 572.0, 293.5],"true", 2) )
    # Connections for obj1121 (graphObject_: Obj1018) named concat2
    self.drawConnections(
(self.obj1121,self.obj1168,[926.0, 358.0, 862.0, 336.0],"true", 2),
(self.obj1121,self.obj1169,[926.0, 358.0, 910.0, 298.0],"true", 2),
(self.obj1121,self.obj1170,[926.0, 358.0, 958.0, 353.0],"true", 2) )
    # Connections for obj1122 (graphObject_: Obj1019) named S
    self.drawConnections(
 )
    # Connections for obj1123 (graphObject_: Obj1020) named exit
    self.drawConnections(
 )
    # Connections for obj1124 (graphObject_: Obj1021) named exack
    self.drawConnections(
 )
    # Connections for obj1125 (graphObject_: Obj1022) named 1
    self.drawConnections(
 )
    # Connections for obj1126 (graphObject_: Obj1023) named 2
    self.drawConnections(
 )
    # Connections for obj1127 (graphObject_: Obj1024) named sh
    self.drawConnections(
 )
    # Connections for obj1128 (graphObject_: Obj1025) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1129 (graphObject_: Obj1026) of type paired_with
    self.drawConnections(
(self.obj1129,self.obj1096,[140.5, 182.0, 143.0, 401.0],"true", 2) )
    # Connections for obj1130 (graphObject_: Obj1027) of type match_contains
    self.drawConnections(
(self.obj1130,self.obj1098,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj1131 (graphObject_: Obj1028) of type match_contains
    self.drawConnections(
(self.obj1131,self.obj1100,[244.0, 127.0, 350.0, 203.0],"true", 2) )
    # Connections for obj1132 (graphObject_: Obj1029) of type match_contains
    self.drawConnections(
(self.obj1132,self.obj1099,[384.0, 97.0, 630.0, 143.0],"true", 2) )
    # Connections for obj1133 (graphObject_: Obj1030) of type match_contains
    self.drawConnections(
(self.obj1133,self.obj1097,[524.0, 67.0, 910.0, 83.0],"true", 2) )
    # Connections for obj1134 (graphObject_: Obj1031) of type apply_contains
    self.drawConnections(
(self.obj1134,self.obj1105,[237.5, 466.0, 332.0, 531.0],"true", 2) )
    # Connections for obj1135 (graphObject_: Obj1032) of type apply_contains
    self.drawConnections(
(self.obj1135,self.obj1104,[374.5, 531.0, 606.0, 661.0],"true", 2) )
    # Connections for obj1136 (graphObject_: Obj1033) of type apply_contains
    self.drawConnections(
(self.obj1136,self.obj1103,[465.0, 521.0, 787.0, 641.0],"true", 2) )
    # Connections for obj1137 (graphObject_: Obj1034) of type apply_contains
    self.drawConnections(
(self.obj1137,self.obj1102,[555.5, 496.0, 968.0, 591.0],"true", 2) )
    # Connections for obj1138 (graphObject_: Obj1035) of type apply_contains
    self.drawConnections(
(self.obj1138,self.obj1101,[646.5, 466.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj1139 (graphObject_: Obj1036) of type directLink_T
    self.drawConnections(
(self.obj1139,self.obj1101,[522.0, 531.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj1140 (graphObject_: Obj1037) of type directLink_T
    self.drawConnections(
(self.obj1140,self.obj1102,[645.5, 566.0, 968.0, 591.0],"true", 2) )
    # Connections for obj1141 (graphObject_: Obj1038) of type directLink_T
    self.drawConnections(
(self.obj1141,self.obj1103,[553.0, 586.0, 787.0, 641.0],"true", 2) )
    # Connections for obj1142 (graphObject_: Obj1039) of type directLink_T
    self.drawConnections(
(self.obj1142,self.obj1104,[469.0, 596.0, 606.0, 661.0],"true", 2) )
    # Connections for obj1143 (graphObject_: Obj1040) of type directLink_S
    self.drawConnections(
(self.obj1143,self.obj1100,[350.0, 153.0, 350.0, 203.0],"true", 2) )
    # Connections for obj1144 (graphObject_: Obj1041) of type directLink_S
    self.drawConnections(
(self.obj1144,self.obj1097,[640.0, 84.0, 910.0, 83.0],"true", 2) )
    # Connections for obj1145 (graphObject_: Obj1042) of type directLink_S
    self.drawConnections(
(self.obj1145,self.obj1099,[770.0, 113.0, 630.0, 143.0],"true", 2) )
    # Connections for obj1146 (graphObject_: Obj1043) of type hasAttribute_S
    self.drawConnections(
(self.obj1146,self.obj1106,[902.0, 148.5, 894.0, 194.0],"true", 2) )
    # Connections for obj1147 (graphObject_: Obj1044) of type hasAttribute_S
    self.drawConnections(
(self.obj1147,self.obj1107,[622.0, 184.5, 614.0, 226.0],"true", 2) )
    # Connections for obj1148 (graphObject_: Obj1045) of type hasAttribute_T
    self.drawConnections(
(self.obj1148,self.obj1108,[343.0, 482.5, 354.0, 434.0],"true", 2) )
    # Connections for obj1149 (graphObject_: Obj1046) of type hasAttribute_T
    self.drawConnections(
(self.obj1149,self.obj1109,[1127.0, 592.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj1150 (graphObject_: Obj1047) of type hasAttribute_T
    self.drawConnections(
(self.obj1150,self.obj1110,[946.5, 649.0, 934.0, 680.0],"true", 2) )
    # Connections for obj1151 (graphObject_: Obj1048) of type hasAttribute_T
    self.drawConnections(
(self.obj1151,self.obj1111,[777.5, 567.5, 774.0, 454.0],"true", 2) )
    # Connections for obj1152 (graphObject_: Obj1049) of type hasAttribute_T
    self.drawConnections(
(self.obj1152,self.obj1112,[584.5, 703.0, 563.0, 745.0],"true", 2) )
    # Connections for obj1153 (graphObject_: Obj1050) of type hasAttribute_T
    self.drawConnections(
(self.obj1153,self.obj1113,[243.0, 562.5, 154.0, 594.0],"true", 2) )
    # Connections for obj1154 (graphObject_: Obj1051) of type leftExpr
    self.drawConnections(
(self.obj1154,self.obj1108,[358.0, 403.5, 354.0, 434.0],"true", 2) )
    # Connections for obj1155 (graphObject_: Obj1052) of type leftExpr
    self.drawConnections(
(self.obj1155,self.obj1109,[1100.0, 630.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj1156 (graphObject_: Obj1053) of type leftExpr
    self.drawConnections(
(self.obj1156,self.obj1110,[1023.5, 709.5, 934.0, 680.0],"true", 2) )
    # Connections for obj1157 (graphObject_: Obj1054) of type leftExpr
    self.drawConnections(
(self.obj1157,self.obj1111,[793.0, 464.0, 774.0, 454.0],"true", 2) )
    # Connections for obj1158 (graphObject_: Obj1055) of type leftExpr
    self.drawConnections(
(self.obj1158,self.obj1112,[482.5, 754.0, 563.0, 745.0],"true", 2) )
    # Connections for obj1159 (graphObject_: Obj1056) of type leftExpr
    self.drawConnections(
(self.obj1159,self.obj1113,[236.0, 606.5, 154.0, 594.0],"true", 2) )
    # Connections for obj1160 (graphObject_: Obj1057) of type rightExpr
    self.drawConnections(
(self.obj1160,self.obj1120,[447.0, 363.5, 530.0, 361.0],"true", 2) )
    # Connections for obj1161 (graphObject_: Obj1058) of type rightExpr
    self.drawConnections(
(self.obj1161,self.obj1123,[1279.5, 683.5, 1274.0, 708.0],"true", 2) )
    # Connections for obj1162 (graphObject_: Obj1059) of type rightExpr
    self.drawConnections(
(self.obj1162,self.obj1124,[1023.5, 753.5, 934.0, 757.0],"true", 2) )
    # Connections for obj1163 (graphObject_: Obj1060) of type rightExpr
    self.drawConnections(
(self.obj1163,self.obj1121,[926.0, 449.0, 926.0, 358.0],"true", 2) )
    # Connections for obj1164 (graphObject_: Obj1061) of type rightExpr
    self.drawConnections(
(self.obj1164,self.obj1127,[478.0, 791.5, 554.0, 820.0],"true", 2) )
    # Connections for obj1165 (graphObject_: Obj1062) of type rightExpr
    self.drawConnections(
(self.obj1165,self.obj1128,[236.5, 646.5, 155.0, 674.0],"true", 2) )
    # Connections for obj1166 (graphObject_: Obj1063) of type hasArgs
    self.drawConnections(
(self.obj1166,self.obj1122,[498.5, 323.0, 467.0, 285.0],"true", 2) )
    # Connections for obj1167 (graphObject_: Obj1064) of type hasArgs
    self.drawConnections(
(self.obj1167,self.obj1107,[572.0, 293.5, 614.0, 226.0],"true", 2) )
    # Connections for obj1168 (graphObject_: Obj1065) of type hasArgs
    self.drawConnections(
(self.obj1168,self.obj1125,[862.0, 336.0, 782.0, 284.0],"true", 2) )
    # Connections for obj1169 (graphObject_: Obj1066) of type hasArgs
    self.drawConnections(
(self.obj1169,self.obj1106,[910.0, 298.0, 894.0, 194.0],"true", 2) )
    # Connections for obj1170 (graphObject_: Obj1067) of type hasArgs
    self.drawConnections(
(self.obj1170,self.obj1126,[958.0, 353.0, 1070.0, 280.0],"true", 2) )

newfunction = Transition2QInstSIBLING_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
