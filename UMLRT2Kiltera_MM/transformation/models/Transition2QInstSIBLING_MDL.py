"""
__Transition2QInstSIBLING_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:32:28 2015
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


    self.obj1185=MatchModel(self)
    self.obj1185.isGraphObjectVisual = True

    if(hasattr(self.obj1185, '_setHierarchicalLink')):
      self.obj1185._setHierarchicalLink(False)

    self.obj1185.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1185.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1185)
    self.globalAndLocalPostcondition(self.obj1185, rootNode)
    self.obj1185.postAction( rootNode.CREATE )

    self.obj1186=ApplyModel(self)
    self.obj1186.isGraphObjectVisual = True

    if(hasattr(self.obj1186, '_setHierarchicalLink')):
      self.obj1186._setHierarchicalLink(False)

    self.obj1186.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,368.0,self.obj1186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, -3.0]
    else: new_obj = None
    self.obj1186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1186)
    self.globalAndLocalPostcondition(self.obj1186, rootNode)
    self.obj1186.postAction( rootNode.CREATE )

    self.obj1187=Vertex(self)
    self.obj1187.isGraphObjectVisual = True

    if(hasattr(self.obj1187, '_setHierarchicalLink')):
      self.obj1187._setHierarchicalLink(False)

    # name
    self.obj1187.name.setValue('vertex1')

    # classtype
    self.obj1187.classtype.setValue('Vertex')

    # cardinality
    self.obj1187.cardinality.setValue('1')

    self.obj1187.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(740.0,40.0,self.obj1187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1187)
    self.globalAndLocalPostcondition(self.obj1187, rootNode)
    self.obj1187.postAction( rootNode.CREATE )

    self.obj1188=Transition(self)
    self.obj1188.isGraphObjectVisual = True

    if(hasattr(self.obj1188, '_setHierarchicalLink')):
      self.obj1188._setHierarchicalLink(False)

    # name
    self.obj1188.name.setValue('transition1')

    # classtype
    self.obj1188.classtype.setValue('Transition')

    # cardinality
    self.obj1188.cardinality.setValue('+')

    self.obj1188.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(180.0,40.0,self.obj1188)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1188.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1188)
    self.globalAndLocalPostcondition(self.obj1188, rootNode)
    self.obj1188.postAction( rootNode.CREATE )

    self.obj1189=StateMachine(self)
    self.obj1189.isGraphObjectVisual = True

    if(hasattr(self.obj1189, '_setHierarchicalLink')):
      self.obj1189._setHierarchicalLink(False)

    # name
    self.obj1189.name.setValue('stateMachine1')

    # classtype
    self.obj1189.classtype.setValue('StateMachine')

    # cardinality
    self.obj1189.cardinality.setValue('1')

    self.obj1189.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(460.0,100.0,self.obj1189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1189)
    self.globalAndLocalPostcondition(self.obj1189, rootNode)
    self.obj1189.postAction( rootNode.CREATE )

    self.obj1190=SIBLING0(self)
    self.obj1190.isGraphObjectVisual = True

    if(hasattr(self.obj1190, '_setHierarchicalLink')):
      self.obj1190._setHierarchicalLink(False)

    # classtype
    self.obj1190.classtype.setValue('SIBLING0')

    # cardinality
    self.obj1190.cardinality.setValue('1')

    # name
    self.obj1190.name.setValue('sibling0_1')

    self.obj1190.graphClass_= graph_SIBLING0
    if self.genGraphics:
       new_obj = graph_SIBLING0(180.0,160.0,self.obj1190)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1190.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1190)
    self.globalAndLocalPostcondition(self.obj1190, rootNode)
    self.obj1190.postAction( rootNode.CREATE )

    self.obj1191=Name(self)
    self.obj1191.isGraphObjectVisual = True

    if(hasattr(self.obj1191, '_setHierarchicalLink')):
      self.obj1191._setHierarchicalLink(False)

    # classtype
    self.obj1191.classtype.setValue('Name')

    # cardinality
    self.obj1191.cardinality.setValue('1')

    # name
    self.obj1191.name.setValue('name1')

    self.obj1191.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(978.0,480.0,self.obj1191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1191.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1191)
    self.globalAndLocalPostcondition(self.obj1191, rootNode)
    self.obj1191.postAction( rootNode.CREATE )

    self.obj1192=Name(self)
    self.obj1192.isGraphObjectVisual = True

    if(hasattr(self.obj1192, '_setHierarchicalLink')):
      self.obj1192._setHierarchicalLink(False)

    # classtype
    self.obj1192.classtype.setValue('Name')

    # cardinality
    self.obj1192.cardinality.setValue('1')

    # name
    self.obj1192.name.setValue('name2')

    self.obj1192.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(796.0,540.0,self.obj1192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 13.0]
    else: new_obj = None
    self.obj1192.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1192)
    self.globalAndLocalPostcondition(self.obj1192, rootNode)
    self.obj1192.postAction( rootNode.CREATE )

    self.obj1193=Name(self)
    self.obj1193.isGraphObjectVisual = True

    if(hasattr(self.obj1193, '_setHierarchicalLink')):
      self.obj1193._setHierarchicalLink(False)

    # classtype
    self.obj1193.classtype.setValue('Name')

    # cardinality
    self.obj1193.cardinality.setValue('1')

    # name
    self.obj1193.name.setValue('name3')

    self.obj1193.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(615.0,590.0,self.obj1193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1193.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1193)
    self.globalAndLocalPostcondition(self.obj1193, rootNode)
    self.obj1193.postAction( rootNode.CREATE )

    self.obj1194=Name(self)
    self.obj1194.isGraphObjectVisual = True

    if(hasattr(self.obj1194, '_setHierarchicalLink')):
      self.obj1194._setHierarchicalLink(False)

    # classtype
    self.obj1194.classtype.setValue('Name')

    # cardinality
    self.obj1194.cardinality.setValue('1')

    # name
    self.obj1194.name.setValue('name4')

    self.obj1194.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(434.0,610.0,self.obj1194)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1194.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1194)
    self.globalAndLocalPostcondition(self.obj1194, rootNode)
    self.obj1194.postAction( rootNode.CREATE )

    self.obj1195=Inst(self)
    self.obj1195.isGraphObjectVisual = True

    if(hasattr(self.obj1195, '_setHierarchicalLink')):
      self.obj1195._setHierarchicalLink(False)

    # classtype
    self.obj1195.classtype.setValue('Inst')

    # cardinality
    self.obj1195.cardinality.setValue('1')

    # name
    self.obj1195.name.setValue('inst1')

    self.obj1195.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(160.0,480.0,self.obj1195)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, 0.0]
    else: new_obj = None
    self.obj1195.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1195)
    self.globalAndLocalPostcondition(self.obj1195, rootNode)
    self.obj1195.postAction( rootNode.CREATE )

    self.obj1196=Attribute(self)
    self.obj1196.isGraphObjectVisual = True

    if(hasattr(self.obj1196, '_setHierarchicalLink')):
      self.obj1196._setHierarchicalLink(False)

    # Type
    self.obj1196.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1196.Type.config = 0

    # name
    self.obj1196.name.setValue('name')

    self.obj1196.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(760.0,160.0,self.obj1196)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1196.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1196)
    self.globalAndLocalPostcondition(self.obj1196, rootNode)
    self.obj1196.postAction( rootNode.CREATE )

    self.obj1197=Attribute(self)
    self.obj1197.isGraphObjectVisual = True

    if(hasattr(self.obj1197, '_setHierarchicalLink')):
      self.obj1197._setHierarchicalLink(False)

    # Type
    self.obj1197.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1197.Type.config = 0

    # name
    self.obj1197.name.setValue('name')

    self.obj1197.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,192.0,self.obj1197)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 3.0]
    else: new_obj = None
    self.obj1197.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1197)
    self.globalAndLocalPostcondition(self.obj1197, rootNode)
    self.obj1197.postAction( rootNode.CREATE )

    self.obj1198=Attribute(self)
    self.obj1198.isGraphObjectVisual = True

    if(hasattr(self.obj1198, '_setHierarchicalLink')):
      self.obj1198._setHierarchicalLink(False)

    # Type
    self.obj1198.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1198.Type.config = 0

    # name
    self.obj1198.name.setValue('name')

    self.obj1198.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(220.0,400.0,self.obj1198)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 2.0]
    else: new_obj = None
    self.obj1198.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1198)
    self.globalAndLocalPostcondition(self.obj1198, rootNode)
    self.obj1198.postAction( rootNode.CREATE )

    self.obj1199=Attribute(self)
    self.obj1199.isGraphObjectVisual = True

    if(hasattr(self.obj1199, '_setHierarchicalLink')):
      self.obj1199._setHierarchicalLink(False)

    # Type
    self.obj1199.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1199.Type.config = 0

    # name
    self.obj1199.name.setValue('literal')

    self.obj1199.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(975.0,593.0,self.obj1199)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [3.0, -1.0]
    else: new_obj = None
    self.obj1199.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1199)
    self.globalAndLocalPostcondition(self.obj1199, rootNode)
    self.obj1199.postAction( rootNode.CREATE )

    self.obj1200=Attribute(self)
    self.obj1200.isGraphObjectVisual = True

    if(hasattr(self.obj1200, '_setHierarchicalLink')):
      self.obj1200._setHierarchicalLink(False)

    # Type
    self.obj1200.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1200.Type.config = 0

    # name
    self.obj1200.name.setValue('literal')

    self.obj1200.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(800.0,646.0,self.obj1200)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj1200.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1200)
    self.globalAndLocalPostcondition(self.obj1200, rootNode)
    self.obj1200.postAction( rootNode.CREATE )

    self.obj1201=Attribute(self)
    self.obj1201.isGraphObjectVisual = True

    if(hasattr(self.obj1201, '_setHierarchicalLink')):
      self.obj1201._setHierarchicalLink(False)

    # Type
    self.obj1201.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1201.Type.config = 0

    # name
    self.obj1201.name.setValue('literal')

    self.obj1201.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,420.0,self.obj1201)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1201.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1201)
    self.globalAndLocalPostcondition(self.obj1201, rootNode)
    self.obj1201.postAction( rootNode.CREATE )

    self.obj1202=Attribute(self)
    self.obj1202.isGraphObjectVisual = True

    if(hasattr(self.obj1202, '_setHierarchicalLink')):
      self.obj1202._setHierarchicalLink(False)

    # Type
    self.obj1202.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1202.Type.config = 0

    # name
    self.obj1202.name.setValue('literal')

    self.obj1202.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(429.0,711.0,self.obj1202)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1202.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1202)
    self.globalAndLocalPostcondition(self.obj1202, rootNode)
    self.obj1202.postAction( rootNode.CREATE )

    self.obj1203=Attribute(self)
    self.obj1203.isGraphObjectVisual = True

    if(hasattr(self.obj1203, '_setHierarchicalLink')):
      self.obj1203._setHierarchicalLink(False)

    # Type
    self.obj1203.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1203.Type.config = 0

    # name
    self.obj1203.name.setValue('pivot')

    self.obj1203.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(20.0,560.0,self.obj1203)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1203.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1203)
    self.globalAndLocalPostcondition(self.obj1203, rootNode)
    self.obj1203.postAction( rootNode.CREATE )

    self.obj1204=Equation(self)
    self.obj1204.isGraphObjectVisual = True

    if(hasattr(self.obj1204, '_setHierarchicalLink')):
      self.obj1204._setHierarchicalLink(False)

    # name
    self.obj1204.name.setValue('eq1')

    self.obj1204.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(226.0,327.0,self.obj1204)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 6.0]
    else: new_obj = None
    self.obj1204.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1204)
    self.globalAndLocalPostcondition(self.obj1204, rootNode)
    self.obj1204.postAction( rootNode.CREATE )

    self.obj1205=Equation(self)
    self.obj1205.isGraphObjectVisual = True

    if(hasattr(self.obj1205, '_setHierarchicalLink')):
      self.obj1205._setHierarchicalLink(False)

    # name
    self.obj1205.name.setValue('eq2')

    self.obj1205.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1147.0,594.0,self.obj1205)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-7.0, 3.0]
    else: new_obj = None
    self.obj1205.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1205)
    self.globalAndLocalPostcondition(self.obj1205, rootNode)
    self.obj1205.postAction( rootNode.CREATE )

    self.obj1206=Equation(self)
    self.obj1206.isGraphObjectVisual = True

    if(hasattr(self.obj1206, '_setHierarchicalLink')):
      self.obj1206._setHierarchicalLink(False)

    # name
    self.obj1206.name.setValue('eq3')

    self.obj1206.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(975.0,683.0,self.obj1206)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1206.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1206)
    self.globalAndLocalPostcondition(self.obj1206, rootNode)
    self.obj1206.postAction( rootNode.CREATE )

    self.obj1207=Equation(self)
    self.obj1207.isGraphObjectVisual = True

    if(hasattr(self.obj1207, '_setHierarchicalLink')):
      self.obj1207._setHierarchicalLink(False)

    # name
    self.obj1207.name.setValue('eq4')

    self.obj1207.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(788.0,428.0,self.obj1207)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj1207.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1207)
    self.globalAndLocalPostcondition(self.obj1207, rootNode)
    self.obj1207.postAction( rootNode.CREATE )

    self.obj1208=Equation(self)
    self.obj1208.isGraphObjectVisual = True

    if(hasattr(self.obj1208, '_setHierarchicalLink')):
      self.obj1208._setHierarchicalLink(False)

    # name
    self.obj1208.name.setValue('eq5')

    self.obj1208.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(264.0,724.0,self.obj1208)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1208.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1208)
    self.globalAndLocalPostcondition(self.obj1208, rootNode)
    self.obj1208.postAction( rootNode.CREATE )

    self.obj1209=Equation(self)
    self.obj1209.isGraphObjectVisual = True

    if(hasattr(self.obj1209, '_setHierarchicalLink')):
      self.obj1209._setHierarchicalLink(False)

    # name
    self.obj1209.name.setValue('eq6')

    self.obj1209.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(180.0,580.0,self.obj1209)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1209.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1209)
    self.globalAndLocalPostcondition(self.obj1209, rootNode)
    self.obj1209.postAction( rootNode.CREATE )

    self.obj1210=Concat(self)
    self.obj1210.isGraphObjectVisual = True

    if(hasattr(self.obj1210, '_setHierarchicalLink')):
      self.obj1210._setHierarchicalLink(False)

    # Type
    self.obj1210.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1210.Type.config = 0

    # name
    self.obj1210.name.setValue('concat1')

    self.obj1210.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(396.0,327.0,self.obj1210)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1210.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1210)
    self.globalAndLocalPostcondition(self.obj1210, rootNode)
    self.obj1210.postAction( rootNode.CREATE )

    self.obj1211=Concat(self)
    self.obj1211.isGraphObjectVisual = True

    if(hasattr(self.obj1211, '_setHierarchicalLink')):
      self.obj1211._setHierarchicalLink(False)

    # Type
    self.obj1211.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1211.Type.config = 0

    # name
    self.obj1211.name.setValue('concat2')

    self.obj1211.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(792.0,324.0,self.obj1211)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [5.0, -2.0]
    else: new_obj = None
    self.obj1211.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1211)
    self.globalAndLocalPostcondition(self.obj1211, rootNode)
    self.obj1211.postAction( rootNode.CREATE )

    self.obj1212=Constant(self)
    self.obj1212.isGraphObjectVisual = True

    if(hasattr(self.obj1212, '_setHierarchicalLink')):
      self.obj1212._setHierarchicalLink(False)

    # Type
    self.obj1212.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1212.Type.config = 0

    # name
    self.obj1212.name.setValue('S')

    self.obj1212.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(333.0,251.0,self.obj1212)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1212.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1212)
    self.globalAndLocalPostcondition(self.obj1212, rootNode)
    self.obj1212.postAction( rootNode.CREATE )

    self.obj1213=Constant(self)
    self.obj1213.isGraphObjectVisual = True

    if(hasattr(self.obj1213, '_setHierarchicalLink')):
      self.obj1213._setHierarchicalLink(False)

    # Type
    self.obj1213.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1213.Type.config = 0

    # name
    self.obj1213.name.setValue('exit')

    self.obj1213.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1140.0,674.0,self.obj1213)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, -4.0]
    else: new_obj = None
    self.obj1213.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1213)
    self.globalAndLocalPostcondition(self.obj1213, rootNode)
    self.obj1213.postAction( rootNode.CREATE )

    self.obj1214=Constant(self)
    self.obj1214.isGraphObjectVisual = True

    if(hasattr(self.obj1214, '_setHierarchicalLink')):
      self.obj1214._setHierarchicalLink(False)

    # Type
    self.obj1214.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1214.Type.config = 0

    # name
    self.obj1214.name.setValue('exack')

    self.obj1214.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,723.0,self.obj1214)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1214.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1214)
    self.globalAndLocalPostcondition(self.obj1214, rootNode)
    self.obj1214.postAction( rootNode.CREATE )

    self.obj1215=Constant(self)
    self.obj1215.isGraphObjectVisual = True

    if(hasattr(self.obj1215, '_setHierarchicalLink')):
      self.obj1215._setHierarchicalLink(False)

    # Type
    self.obj1215.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1215.Type.config = 0

    # name
    self.obj1215.name.setValue('1')

    self.obj1215.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(648.0,250.0,self.obj1215)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1215.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1215)
    self.globalAndLocalPostcondition(self.obj1215, rootNode)
    self.obj1215.postAction( rootNode.CREATE )

    self.obj1216=Constant(self)
    self.obj1216.isGraphObjectVisual = True

    if(hasattr(self.obj1216, '_setHierarchicalLink')):
      self.obj1216._setHierarchicalLink(False)

    # Type
    self.obj1216.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1216.Type.config = 0

    # name
    self.obj1216.name.setValue('2')

    self.obj1216.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(936.0,246.0,self.obj1216)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1216.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1216)
    self.globalAndLocalPostcondition(self.obj1216, rootNode)
    self.obj1216.postAction( rootNode.CREATE )

    self.obj1217=Constant(self)
    self.obj1217.isGraphObjectVisual = True

    if(hasattr(self.obj1217, '_setHierarchicalLink')):
      self.obj1217._setHierarchicalLink(False)

    # Type
    self.obj1217.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1217.Type.config = 0

    # name
    self.obj1217.name.setValue('sh')

    self.obj1217.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,786.0,self.obj1217)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1217.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1217)
    self.globalAndLocalPostcondition(self.obj1217, rootNode)
    self.obj1217.postAction( rootNode.CREATE )

    self.obj1218=Constant(self)
    self.obj1218.isGraphObjectVisual = True

    if(hasattr(self.obj1218, '_setHierarchicalLink')):
      self.obj1218._setHierarchicalLink(False)

    # Type
    self.obj1218.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1218.Type.config = 0

    # name
    self.obj1218.name.setValue('instfortrans')

    self.obj1218.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(21.0,640.0,self.obj1218)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1218.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1218)
    self.globalAndLocalPostcondition(self.obj1218, rootNode)
    self.obj1218.postAction( rootNode.CREATE )

    self.obj1219=paired_with(self)
    self.obj1219.isGraphObjectVisual = True

    if(hasattr(self.obj1219, '_setHierarchicalLink')):
      self.obj1219._setHierarchicalLink(False)

    self.obj1219.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,182.0,self.obj1219)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1219.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1219)
    self.globalAndLocalPostcondition(self.obj1219, rootNode)
    self.obj1219.postAction( rootNode.CREATE )

    self.obj1220=match_contains(self)
    self.obj1220.isGraphObjectVisual = True

    if(hasattr(self.obj1220, '_setHierarchicalLink')):
      self.obj1220._setHierarchicalLink(False)

    self.obj1220.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj1220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1220)
    self.globalAndLocalPostcondition(self.obj1220, rootNode)
    self.obj1220.postAction( rootNode.CREATE )

    self.obj1221=match_contains(self)
    self.obj1221.isGraphObjectVisual = True

    if(hasattr(self.obj1221, '_setHierarchicalLink')):
      self.obj1221._setHierarchicalLink(False)

    self.obj1221.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,127.0,self.obj1221)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1221.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1221)
    self.globalAndLocalPostcondition(self.obj1221, rootNode)
    self.obj1221.postAction( rootNode.CREATE )

    self.obj1222=match_contains(self)
    self.obj1222.isGraphObjectVisual = True

    if(hasattr(self.obj1222, '_setHierarchicalLink')):
      self.obj1222._setHierarchicalLink(False)

    self.obj1222.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,97.0,self.obj1222)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1222.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1222)
    self.globalAndLocalPostcondition(self.obj1222, rootNode)
    self.obj1222.postAction( rootNode.CREATE )

    self.obj1223=match_contains(self)
    self.obj1223.isGraphObjectVisual = True

    if(hasattr(self.obj1223, '_setHierarchicalLink')):
      self.obj1223._setHierarchicalLink(False)

    self.obj1223.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(524.0,67.0,self.obj1223)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1223.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1223)
    self.globalAndLocalPostcondition(self.obj1223, rootNode)
    self.obj1223.postAction( rootNode.CREATE )

    self.obj1224=apply_contains(self)
    self.obj1224.isGraphObjectVisual = True

    if(hasattr(self.obj1224, '_setHierarchicalLink')):
      self.obj1224._setHierarchicalLink(False)

    self.obj1224.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(237.5,466.0,self.obj1224)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1224.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1224)
    self.globalAndLocalPostcondition(self.obj1224, rootNode)
    self.obj1224.postAction( rootNode.CREATE )

    self.obj1225=apply_contains(self)
    self.obj1225.isGraphObjectVisual = True

    if(hasattr(self.obj1225, '_setHierarchicalLink')):
      self.obj1225._setHierarchicalLink(False)

    self.obj1225.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(374.5,531.0,self.obj1225)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1225.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1225)
    self.globalAndLocalPostcondition(self.obj1225, rootNode)
    self.obj1225.postAction( rootNode.CREATE )

    self.obj1226=apply_contains(self)
    self.obj1226.isGraphObjectVisual = True

    if(hasattr(self.obj1226, '_setHierarchicalLink')):
      self.obj1226._setHierarchicalLink(False)

    self.obj1226.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(465.0,521.0,self.obj1226)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1226.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1226)
    self.globalAndLocalPostcondition(self.obj1226, rootNode)
    self.obj1226.postAction( rootNode.CREATE )

    self.obj1227=apply_contains(self)
    self.obj1227.isGraphObjectVisual = True

    if(hasattr(self.obj1227, '_setHierarchicalLink')):
      self.obj1227._setHierarchicalLink(False)

    self.obj1227.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(555.5,496.0,self.obj1227)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1227.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1227)
    self.globalAndLocalPostcondition(self.obj1227, rootNode)
    self.obj1227.postAction( rootNode.CREATE )

    self.obj1228=apply_contains(self)
    self.obj1228.isGraphObjectVisual = True

    if(hasattr(self.obj1228, '_setHierarchicalLink')):
      self.obj1228._setHierarchicalLink(False)

    self.obj1228.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(646.5,466.0,self.obj1228)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1228.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1228)
    self.globalAndLocalPostcondition(self.obj1228, rootNode)
    self.obj1228.postAction( rootNode.CREATE )

    self.obj1229=directLink_T(self)
    self.obj1229.isGraphObjectVisual = True

    if(hasattr(self.obj1229, '_setHierarchicalLink')):
      self.obj1229._setHierarchicalLink(False)

    # associationType
    self.obj1229.associationType.setValue('channelNames')

    self.obj1229.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(522.0,531.0,self.obj1229)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1229.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1229)
    self.globalAndLocalPostcondition(self.obj1229, rootNode)
    self.obj1229.postAction( rootNode.CREATE )

    self.obj1230=directLink_T(self)
    self.obj1230.isGraphObjectVisual = True

    if(hasattr(self.obj1230, '_setHierarchicalLink')):
      self.obj1230._setHierarchicalLink(False)

    # associationType
    self.obj1230.associationType.setValue('channelNames')

    self.obj1230.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(645.5,566.0,self.obj1230)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1230.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1230)
    self.globalAndLocalPostcondition(self.obj1230, rootNode)
    self.obj1230.postAction( rootNode.CREATE )

    self.obj1231=directLink_T(self)
    self.obj1231.isGraphObjectVisual = True

    if(hasattr(self.obj1231, '_setHierarchicalLink')):
      self.obj1231._setHierarchicalLink(False)

    # associationType
    self.obj1231.associationType.setValue('channelNames')

    self.obj1231.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(553.0,586.0,self.obj1231)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1231.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1231)
    self.globalAndLocalPostcondition(self.obj1231, rootNode)
    self.obj1231.postAction( rootNode.CREATE )

    self.obj1232=directLink_T(self)
    self.obj1232.isGraphObjectVisual = True

    if(hasattr(self.obj1232, '_setHierarchicalLink')):
      self.obj1232._setHierarchicalLink(False)

    # associationType
    self.obj1232.associationType.setValue('channelNames')

    self.obj1232.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(469.0,596.0,self.obj1232)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1232.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1232)
    self.globalAndLocalPostcondition(self.obj1232, rootNode)
    self.obj1232.postAction( rootNode.CREATE )

    self.obj1233=directLink_S(self)
    self.obj1233.isGraphObjectVisual = True

    if(hasattr(self.obj1233, '_setHierarchicalLink')):
      self.obj1233._setHierarchicalLink(False)

    # associationType
    self.obj1233.associationType.setValue('type')

    self.obj1233.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(350.0,153.0,self.obj1233)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1233.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1233)
    self.globalAndLocalPostcondition(self.obj1233, rootNode)
    self.obj1233.postAction( rootNode.CREATE )

    self.obj1234=directLink_S(self)
    self.obj1234.isGraphObjectVisual = True

    if(hasattr(self.obj1234, '_setHierarchicalLink')):
      self.obj1234._setHierarchicalLink(False)

    # associationType
    self.obj1234.associationType.setValue('dest')

    self.obj1234.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(640.0,84.0,self.obj1234)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1234.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1234)
    self.globalAndLocalPostcondition(self.obj1234, rootNode)
    self.obj1234.postAction( rootNode.CREATE )

    self.obj1235=directLink_S(self)
    self.obj1235.isGraphObjectVisual = True

    if(hasattr(self.obj1235, '_setHierarchicalLink')):
      self.obj1235._setHierarchicalLink(False)

    # associationType
    self.obj1235.associationType.setValue('owningStateMachine')

    self.obj1235.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(770.0,113.0,self.obj1235)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1235.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1235)
    self.globalAndLocalPostcondition(self.obj1235, rootNode)
    self.obj1235.postAction( rootNode.CREATE )

    self.obj1236=hasAttribute_S(self)
    self.obj1236.isGraphObjectVisual = True

    if(hasattr(self.obj1236, '_setHierarchicalLink')):
      self.obj1236._setHierarchicalLink(False)

    self.obj1236.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(902.0,148.5,self.obj1236)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1236.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1236)
    self.globalAndLocalPostcondition(self.obj1236, rootNode)
    self.obj1236.postAction( rootNode.CREATE )

    self.obj1237=hasAttribute_S(self)
    self.obj1237.isGraphObjectVisual = True

    if(hasattr(self.obj1237, '_setHierarchicalLink')):
      self.obj1237._setHierarchicalLink(False)

    self.obj1237.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(622.0,184.5,self.obj1237)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1237.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1237)
    self.globalAndLocalPostcondition(self.obj1237, rootNode)
    self.obj1237.postAction( rootNode.CREATE )

    self.obj1238=hasAttribute_T(self)
    self.obj1238.isGraphObjectVisual = True

    if(hasattr(self.obj1238, '_setHierarchicalLink')):
      self.obj1238._setHierarchicalLink(False)

    self.obj1238.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(343.0,482.5,self.obj1238)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1238.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1238)
    self.globalAndLocalPostcondition(self.obj1238, rootNode)
    self.obj1238.postAction( rootNode.CREATE )

    self.obj1239=hasAttribute_T(self)
    self.obj1239.isGraphObjectVisual = True

    if(hasattr(self.obj1239, '_setHierarchicalLink')):
      self.obj1239._setHierarchicalLink(False)

    self.obj1239.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1127.0,592.0,self.obj1239)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1239.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1239)
    self.globalAndLocalPostcondition(self.obj1239, rootNode)
    self.obj1239.postAction( rootNode.CREATE )

    self.obj1240=hasAttribute_T(self)
    self.obj1240.isGraphObjectVisual = True

    if(hasattr(self.obj1240, '_setHierarchicalLink')):
      self.obj1240._setHierarchicalLink(False)

    self.obj1240.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(946.5,649.0,self.obj1240)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1240.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1240)
    self.globalAndLocalPostcondition(self.obj1240, rootNode)
    self.obj1240.postAction( rootNode.CREATE )

    self.obj1241=hasAttribute_T(self)
    self.obj1241.isGraphObjectVisual = True

    if(hasattr(self.obj1241, '_setHierarchicalLink')):
      self.obj1241._setHierarchicalLink(False)

    self.obj1241.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(777.5,567.5,self.obj1241)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1241.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1241)
    self.globalAndLocalPostcondition(self.obj1241, rootNode)
    self.obj1241.postAction( rootNode.CREATE )

    self.obj1242=hasAttribute_T(self)
    self.obj1242.isGraphObjectVisual = True

    if(hasattr(self.obj1242, '_setHierarchicalLink')):
      self.obj1242._setHierarchicalLink(False)

    self.obj1242.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(584.5,703.0,self.obj1242)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1242.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1242)
    self.globalAndLocalPostcondition(self.obj1242, rootNode)
    self.obj1242.postAction( rootNode.CREATE )

    self.obj1243=hasAttribute_T(self)
    self.obj1243.isGraphObjectVisual = True

    if(hasattr(self.obj1243, '_setHierarchicalLink')):
      self.obj1243._setHierarchicalLink(False)

    self.obj1243.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(243.0,562.5,self.obj1243)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1243.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1243)
    self.globalAndLocalPostcondition(self.obj1243, rootNode)
    self.obj1243.postAction( rootNode.CREATE )

    self.obj1244=leftExpr(self)
    self.obj1244.isGraphObjectVisual = True

    if(hasattr(self.obj1244, '_setHierarchicalLink')):
      self.obj1244._setHierarchicalLink(False)

    self.obj1244.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(358.0,403.5,self.obj1244)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1244.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1244)
    self.globalAndLocalPostcondition(self.obj1244, rootNode)
    self.obj1244.postAction( rootNode.CREATE )

    self.obj1245=leftExpr(self)
    self.obj1245.isGraphObjectVisual = True

    if(hasattr(self.obj1245, '_setHierarchicalLink')):
      self.obj1245._setHierarchicalLink(False)

    self.obj1245.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,630.0,self.obj1245)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1245.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1245)
    self.globalAndLocalPostcondition(self.obj1245, rootNode)
    self.obj1245.postAction( rootNode.CREATE )

    self.obj1246=leftExpr(self)
    self.obj1246.isGraphObjectVisual = True

    if(hasattr(self.obj1246, '_setHierarchicalLink')):
      self.obj1246._setHierarchicalLink(False)

    self.obj1246.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1023.5,709.5,self.obj1246)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1246.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1246)
    self.globalAndLocalPostcondition(self.obj1246, rootNode)
    self.obj1246.postAction( rootNode.CREATE )

    self.obj1247=leftExpr(self)
    self.obj1247.isGraphObjectVisual = True

    if(hasattr(self.obj1247, '_setHierarchicalLink')):
      self.obj1247._setHierarchicalLink(False)

    self.obj1247.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(793.0,464.0,self.obj1247)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1247.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1247)
    self.globalAndLocalPostcondition(self.obj1247, rootNode)
    self.obj1247.postAction( rootNode.CREATE )

    self.obj1248=leftExpr(self)
    self.obj1248.isGraphObjectVisual = True

    if(hasattr(self.obj1248, '_setHierarchicalLink')):
      self.obj1248._setHierarchicalLink(False)

    self.obj1248.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(482.5,754.0,self.obj1248)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1248.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1248)
    self.globalAndLocalPostcondition(self.obj1248, rootNode)
    self.obj1248.postAction( rootNode.CREATE )

    self.obj1249=leftExpr(self)
    self.obj1249.isGraphObjectVisual = True

    if(hasattr(self.obj1249, '_setHierarchicalLink')):
      self.obj1249._setHierarchicalLink(False)

    self.obj1249.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(236.0,606.5,self.obj1249)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1249.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1249)
    self.globalAndLocalPostcondition(self.obj1249, rootNode)
    self.obj1249.postAction( rootNode.CREATE )

    self.obj1250=rightExpr(self)
    self.obj1250.isGraphObjectVisual = True

    if(hasattr(self.obj1250, '_setHierarchicalLink')):
      self.obj1250._setHierarchicalLink(False)

    self.obj1250.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(447.0,363.5,self.obj1250)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1250.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1250)
    self.globalAndLocalPostcondition(self.obj1250, rootNode)
    self.obj1250.postAction( rootNode.CREATE )

    self.obj1251=rightExpr(self)
    self.obj1251.isGraphObjectVisual = True

    if(hasattr(self.obj1251, '_setHierarchicalLink')):
      self.obj1251._setHierarchicalLink(False)

    self.obj1251.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1279.5,683.5,self.obj1251)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1251.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1251)
    self.globalAndLocalPostcondition(self.obj1251, rootNode)
    self.obj1251.postAction( rootNode.CREATE )

    self.obj1252=rightExpr(self)
    self.obj1252.isGraphObjectVisual = True

    if(hasattr(self.obj1252, '_setHierarchicalLink')):
      self.obj1252._setHierarchicalLink(False)

    self.obj1252.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1023.5,753.5,self.obj1252)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1252.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1252)
    self.globalAndLocalPostcondition(self.obj1252, rootNode)
    self.obj1252.postAction( rootNode.CREATE )

    self.obj1253=rightExpr(self)
    self.obj1253.isGraphObjectVisual = True

    if(hasattr(self.obj1253, '_setHierarchicalLink')):
      self.obj1253._setHierarchicalLink(False)

    self.obj1253.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(926.0,449.0,self.obj1253)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1253.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1253)
    self.globalAndLocalPostcondition(self.obj1253, rootNode)
    self.obj1253.postAction( rootNode.CREATE )

    self.obj1254=rightExpr(self)
    self.obj1254.isGraphObjectVisual = True

    if(hasattr(self.obj1254, '_setHierarchicalLink')):
      self.obj1254._setHierarchicalLink(False)

    self.obj1254.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(478.0,791.5,self.obj1254)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1254.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1254)
    self.globalAndLocalPostcondition(self.obj1254, rootNode)
    self.obj1254.postAction( rootNode.CREATE )

    self.obj1255=rightExpr(self)
    self.obj1255.isGraphObjectVisual = True

    if(hasattr(self.obj1255, '_setHierarchicalLink')):
      self.obj1255._setHierarchicalLink(False)

    self.obj1255.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(236.5,646.5,self.obj1255)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1255.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1255)
    self.globalAndLocalPostcondition(self.obj1255, rootNode)
    self.obj1255.postAction( rootNode.CREATE )

    self.obj1256=hasArgs(self)
    self.obj1256.isGraphObjectVisual = True

    if(hasattr(self.obj1256, '_setHierarchicalLink')):
      self.obj1256._setHierarchicalLink(False)

    self.obj1256.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(498.5,323.0,self.obj1256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1256.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1256)
    self.globalAndLocalPostcondition(self.obj1256, rootNode)
    self.obj1256.postAction( rootNode.CREATE )

    self.obj1257=hasArgs(self)
    self.obj1257.isGraphObjectVisual = True

    if(hasattr(self.obj1257, '_setHierarchicalLink')):
      self.obj1257._setHierarchicalLink(False)

    self.obj1257.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(572.0,293.5,self.obj1257)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1257.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1257)
    self.globalAndLocalPostcondition(self.obj1257, rootNode)
    self.obj1257.postAction( rootNode.CREATE )

    self.obj1258=hasArgs(self)
    self.obj1258.isGraphObjectVisual = True

    if(hasattr(self.obj1258, '_setHierarchicalLink')):
      self.obj1258._setHierarchicalLink(False)

    self.obj1258.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(862.0,336.0,self.obj1258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1258.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1258)
    self.globalAndLocalPostcondition(self.obj1258, rootNode)
    self.obj1258.postAction( rootNode.CREATE )

    self.obj1259=hasArgs(self)
    self.obj1259.isGraphObjectVisual = True

    if(hasattr(self.obj1259, '_setHierarchicalLink')):
      self.obj1259._setHierarchicalLink(False)

    self.obj1259.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(910.0,298.0,self.obj1259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1259)
    self.globalAndLocalPostcondition(self.obj1259, rootNode)
    self.obj1259.postAction( rootNode.CREATE )

    self.obj1260=hasArgs(self)
    self.obj1260.isGraphObjectVisual = True

    if(hasattr(self.obj1260, '_setHierarchicalLink')):
      self.obj1260._setHierarchicalLink(False)

    self.obj1260.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(958.0,353.0,self.obj1260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1260)
    self.globalAndLocalPostcondition(self.obj1260, rootNode)
    self.obj1260.postAction( rootNode.CREATE )

    # Connections for obj1185 (graphObject_: Obj992) of type MatchModel
    self.drawConnections(
(self.obj1185,self.obj1219,[138.0, 51.0, 140.5, 182.0],"true", 2),
(self.obj1185,self.obj1220,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj1185,self.obj1221,[138.0, 51.0, 244.0, 127.0],"true", 2),
(self.obj1185,self.obj1222,[138.0, 51.0, 384.0, 97.0],"true", 2),
(self.obj1185,self.obj1223,[138.0, 51.0, 524.0, 67.0],"true", 2) )
    # Connections for obj1186 (graphObject_: Obj993) of type ApplyModel
    self.drawConnections(
(self.obj1186,self.obj1224,[143.0, 401.0, 237.5, 466.0],"true", 2),
(self.obj1186,self.obj1225,[143.0, 401.0, 374.5, 531.0],"true", 2),
(self.obj1186,self.obj1226,[143.0, 401.0, 465.0, 521.0],"true", 2),
(self.obj1186,self.obj1227,[143.0, 401.0, 555.5, 496.0],"true", 2),
(self.obj1186,self.obj1228,[143.0, 401.0, 646.5, 466.0],"true", 2) )
    # Connections for obj1187 (graphObject_: Obj994) named vertex1
    self.drawConnections(
(self.obj1187,self.obj1236,[910.0, 83.0, 902.0, 148.5],"true", 2),
(self.obj1187,self.obj1235,[910.0, 83.0, 770.0, 113.0],"true", 2) )
    # Connections for obj1188 (graphObject_: Obj995) named transition1
    self.drawConnections(
(self.obj1188,self.obj1233,[350.0, 83.0, 350.0, 153.0],"true", 2),
(self.obj1188,self.obj1234,[350.0, 83.0, 640.0, 84.0],"true", 2) )
    # Connections for obj1189 (graphObject_: Obj996) named stateMachine1
    self.drawConnections(
(self.obj1189,self.obj1237,[630.0, 143.0, 622.0, 184.5],"true", 2) )
    # Connections for obj1190 (graphObject_: Obj997) named sibling0_1
    self.drawConnections(
 )
    # Connections for obj1191 (graphObject_: Obj998) named name1
    self.drawConnections(
(self.obj1191,self.obj1239,[1150.0, 531.0, 1127.0, 592.0],"true", 2) )
    # Connections for obj1192 (graphObject_: Obj999) named name2
    self.drawConnections(
(self.obj1192,self.obj1240,[968.0, 591.0, 946.5, 649.0],"true", 2) )
    # Connections for obj1193 (graphObject_: Obj1000) named name3
    self.drawConnections(
(self.obj1193,self.obj1241,[787.0, 641.0, 777.5, 567.5],"true", 2) )
    # Connections for obj1194 (graphObject_: Obj1001) named name4
    self.drawConnections(
(self.obj1194,self.obj1242,[606.0, 661.0, 584.5, 703.0],"true", 2) )
    # Connections for obj1195 (graphObject_: Obj1002) named inst1
    self.drawConnections(
(self.obj1195,self.obj1238,[332.0, 531.0, 343.0, 482.5],"true", 2),
(self.obj1195,self.obj1229,[332.0, 531.0, 522.0, 531.0],"true", 2),
(self.obj1195,self.obj1230,[332.0, 531.0, 645.5, 566.0],"true", 2),
(self.obj1195,self.obj1231,[332.0, 531.0, 553.0, 586.0],"true", 2),
(self.obj1195,self.obj1232,[332.0, 531.0, 469.0, 596.0],"true", 2),
(self.obj1195,self.obj1243,[332.0, 531.0, 243.0, 562.5],"true", 2) )
    # Connections for obj1196 (graphObject_: Obj1003) named name
    self.drawConnections(
 )
    # Connections for obj1197 (graphObject_: Obj1004) named name
    self.drawConnections(
 )
    # Connections for obj1198 (graphObject_: Obj1005) named name
    self.drawConnections(
 )
    # Connections for obj1199 (graphObject_: Obj1006) named literal
    self.drawConnections(
 )
    # Connections for obj1200 (graphObject_: Obj1007) named literal
    self.drawConnections(
 )
    # Connections for obj1201 (graphObject_: Obj1008) named literal
    self.drawConnections(
 )
    # Connections for obj1202 (graphObject_: Obj1009) named literal
    self.drawConnections(
 )
    # Connections for obj1203 (graphObject_: Obj1010) named pivot
    self.drawConnections(
 )
    # Connections for obj1204 (graphObject_: Obj1011) named eq1
    self.drawConnections(
(self.obj1204,self.obj1244,[364.0, 366.0, 358.0, 403.5],"true", 2),
(self.obj1204,self.obj1250,[364.0, 366.0, 447.0, 363.5],"true", 2) )
    # Connections for obj1205 (graphObject_: Obj1012) named eq2
    self.drawConnections(
(self.obj1205,self.obj1245,[1285.0, 633.0, 1100.0, 630.0],"true", 2),
(self.obj1205,self.obj1251,[1285.0, 633.0, 1279.5, 683.5],"true", 2) )
    # Connections for obj1206 (graphObject_: Obj1013) named eq3
    self.drawConnections(
(self.obj1206,self.obj1246,[1113.0, 722.0, 1023.5, 709.5],"true", 2),
(self.obj1206,self.obj1252,[1113.0, 722.0, 1023.5, 753.5],"true", 2) )
    # Connections for obj1207 (graphObject_: Obj1014) named eq4
    self.drawConnections(
(self.obj1207,self.obj1247,[926.0, 467.0, 793.0, 464.0],"true", 2),
(self.obj1207,self.obj1253,[926.0, 467.0, 926.0, 449.0],"true", 2) )
    # Connections for obj1208 (graphObject_: Obj1015) named eq5
    self.drawConnections(
(self.obj1208,self.obj1248,[402.0, 763.0, 482.5, 754.0],"true", 2),
(self.obj1208,self.obj1254,[402.0, 763.0, 478.0, 791.5],"true", 2) )
    # Connections for obj1209 (graphObject_: Obj1016) named eq6
    self.drawConnections(
(self.obj1209,self.obj1255,[318.0, 619.0, 236.5, 646.5],"true", 2),
(self.obj1209,self.obj1249,[318.0, 619.0, 236.0, 606.5],"true", 2) )
    # Connections for obj1210 (graphObject_: Obj1017) named concat1
    self.drawConnections(
(self.obj1210,self.obj1256,[530.0, 361.0, 498.5, 323.0],"true", 2),
(self.obj1210,self.obj1257,[530.0, 361.0, 572.0, 293.5],"true", 2) )
    # Connections for obj1211 (graphObject_: Obj1018) named concat2
    self.drawConnections(
(self.obj1211,self.obj1258,[926.0, 358.0, 862.0, 336.0],"true", 2),
(self.obj1211,self.obj1259,[926.0, 358.0, 910.0, 298.0],"true", 2),
(self.obj1211,self.obj1260,[926.0, 358.0, 958.0, 353.0],"true", 2) )
    # Connections for obj1212 (graphObject_: Obj1019) named S
    self.drawConnections(
 )
    # Connections for obj1213 (graphObject_: Obj1020) named exit
    self.drawConnections(
 )
    # Connections for obj1214 (graphObject_: Obj1021) named exack
    self.drawConnections(
 )
    # Connections for obj1215 (graphObject_: Obj1022) named 1
    self.drawConnections(
 )
    # Connections for obj1216 (graphObject_: Obj1023) named 2
    self.drawConnections(
 )
    # Connections for obj1217 (graphObject_: Obj1024) named sh
    self.drawConnections(
 )
    # Connections for obj1218 (graphObject_: Obj1025) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1219 (graphObject_: Obj1026) of type paired_with
    self.drawConnections(
(self.obj1219,self.obj1186,[140.5, 182.0, 143.0, 401.0],"true", 2) )
    # Connections for obj1220 (graphObject_: Obj1027) of type match_contains
    self.drawConnections(
(self.obj1220,self.obj1188,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj1221 (graphObject_: Obj1028) of type match_contains
    self.drawConnections(
(self.obj1221,self.obj1190,[244.0, 127.0, 350.0, 203.0],"true", 2) )
    # Connections for obj1222 (graphObject_: Obj1029) of type match_contains
    self.drawConnections(
(self.obj1222,self.obj1189,[384.0, 97.0, 630.0, 143.0],"true", 2) )
    # Connections for obj1223 (graphObject_: Obj1030) of type match_contains
    self.drawConnections(
(self.obj1223,self.obj1187,[524.0, 67.0, 910.0, 83.0],"true", 2) )
    # Connections for obj1224 (graphObject_: Obj1031) of type apply_contains
    self.drawConnections(
(self.obj1224,self.obj1195,[237.5, 466.0, 332.0, 531.0],"true", 2) )
    # Connections for obj1225 (graphObject_: Obj1032) of type apply_contains
    self.drawConnections(
(self.obj1225,self.obj1194,[374.5, 531.0, 606.0, 661.0],"true", 2) )
    # Connections for obj1226 (graphObject_: Obj1033) of type apply_contains
    self.drawConnections(
(self.obj1226,self.obj1193,[465.0, 521.0, 787.0, 641.0],"true", 2) )
    # Connections for obj1227 (graphObject_: Obj1034) of type apply_contains
    self.drawConnections(
(self.obj1227,self.obj1192,[555.5, 496.0, 968.0, 591.0],"true", 2) )
    # Connections for obj1228 (graphObject_: Obj1035) of type apply_contains
    self.drawConnections(
(self.obj1228,self.obj1191,[646.5, 466.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj1229 (graphObject_: Obj1036) of type directLink_T
    self.drawConnections(
(self.obj1229,self.obj1191,[522.0, 531.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj1230 (graphObject_: Obj1037) of type directLink_T
    self.drawConnections(
(self.obj1230,self.obj1192,[645.5, 566.0, 968.0, 591.0],"true", 2) )
    # Connections for obj1231 (graphObject_: Obj1038) of type directLink_T
    self.drawConnections(
(self.obj1231,self.obj1193,[553.0, 586.0, 787.0, 641.0],"true", 2) )
    # Connections for obj1232 (graphObject_: Obj1039) of type directLink_T
    self.drawConnections(
(self.obj1232,self.obj1194,[469.0, 596.0, 606.0, 661.0],"true", 2) )
    # Connections for obj1233 (graphObject_: Obj1040) of type directLink_S
    self.drawConnections(
(self.obj1233,self.obj1190,[350.0, 153.0, 350.0, 203.0],"true", 2) )
    # Connections for obj1234 (graphObject_: Obj1041) of type directLink_S
    self.drawConnections(
(self.obj1234,self.obj1187,[640.0, 84.0, 910.0, 83.0],"true", 2) )
    # Connections for obj1235 (graphObject_: Obj1042) of type directLink_S
    self.drawConnections(
(self.obj1235,self.obj1189,[770.0, 113.0, 630.0, 143.0],"true", 2) )
    # Connections for obj1236 (graphObject_: Obj1043) of type hasAttribute_S
    self.drawConnections(
(self.obj1236,self.obj1196,[902.0, 148.5, 894.0, 194.0],"true", 2) )
    # Connections for obj1237 (graphObject_: Obj1044) of type hasAttribute_S
    self.drawConnections(
(self.obj1237,self.obj1197,[622.0, 184.5, 614.0, 226.0],"true", 2) )
    # Connections for obj1238 (graphObject_: Obj1045) of type hasAttribute_T
    self.drawConnections(
(self.obj1238,self.obj1198,[343.0, 482.5, 354.0, 434.0],"true", 2) )
    # Connections for obj1239 (graphObject_: Obj1046) of type hasAttribute_T
    self.drawConnections(
(self.obj1239,self.obj1199,[1127.0, 592.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj1240 (graphObject_: Obj1047) of type hasAttribute_T
    self.drawConnections(
(self.obj1240,self.obj1200,[946.5, 649.0, 934.0, 680.0],"true", 2) )
    # Connections for obj1241 (graphObject_: Obj1048) of type hasAttribute_T
    self.drawConnections(
(self.obj1241,self.obj1201,[777.5, 567.5, 774.0, 454.0],"true", 2) )
    # Connections for obj1242 (graphObject_: Obj1049) of type hasAttribute_T
    self.drawConnections(
(self.obj1242,self.obj1202,[584.5, 703.0, 563.0, 745.0],"true", 2) )
    # Connections for obj1243 (graphObject_: Obj1050) of type hasAttribute_T
    self.drawConnections(
(self.obj1243,self.obj1203,[243.0, 562.5, 154.0, 594.0],"true", 2) )
    # Connections for obj1244 (graphObject_: Obj1051) of type leftExpr
    self.drawConnections(
(self.obj1244,self.obj1198,[358.0, 403.5, 354.0, 434.0],"true", 2) )
    # Connections for obj1245 (graphObject_: Obj1052) of type leftExpr
    self.drawConnections(
(self.obj1245,self.obj1199,[1100.0, 630.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj1246 (graphObject_: Obj1053) of type leftExpr
    self.drawConnections(
(self.obj1246,self.obj1200,[1023.5, 709.5, 934.0, 680.0],"true", 2) )
    # Connections for obj1247 (graphObject_: Obj1054) of type leftExpr
    self.drawConnections(
(self.obj1247,self.obj1201,[793.0, 464.0, 774.0, 454.0],"true", 2) )
    # Connections for obj1248 (graphObject_: Obj1055) of type leftExpr
    self.drawConnections(
(self.obj1248,self.obj1202,[482.5, 754.0, 563.0, 745.0],"true", 2) )
    # Connections for obj1249 (graphObject_: Obj1056) of type leftExpr
    self.drawConnections(
(self.obj1249,self.obj1203,[236.0, 606.5, 154.0, 594.0],"true", 2) )
    # Connections for obj1250 (graphObject_: Obj1057) of type rightExpr
    self.drawConnections(
(self.obj1250,self.obj1210,[447.0, 363.5, 530.0, 361.0],"true", 2) )
    # Connections for obj1251 (graphObject_: Obj1058) of type rightExpr
    self.drawConnections(
(self.obj1251,self.obj1213,[1279.5, 683.5, 1274.0, 708.0],"true", 2) )
    # Connections for obj1252 (graphObject_: Obj1059) of type rightExpr
    self.drawConnections(
(self.obj1252,self.obj1214,[1023.5, 753.5, 934.0, 757.0],"true", 2) )
    # Connections for obj1253 (graphObject_: Obj1060) of type rightExpr
    self.drawConnections(
(self.obj1253,self.obj1211,[926.0, 449.0, 926.0, 358.0],"true", 2) )
    # Connections for obj1254 (graphObject_: Obj1061) of type rightExpr
    self.drawConnections(
(self.obj1254,self.obj1217,[478.0, 791.5, 554.0, 820.0],"true", 2) )
    # Connections for obj1255 (graphObject_: Obj1062) of type rightExpr
    self.drawConnections(
(self.obj1255,self.obj1218,[236.5, 646.5, 155.0, 674.0],"true", 2) )
    # Connections for obj1256 (graphObject_: Obj1063) of type hasArgs
    self.drawConnections(
(self.obj1256,self.obj1212,[498.5, 323.0, 467.0, 285.0],"true", 2) )
    # Connections for obj1257 (graphObject_: Obj1064) of type hasArgs
    self.drawConnections(
(self.obj1257,self.obj1197,[572.0, 293.5, 614.0, 226.0],"true", 2) )
    # Connections for obj1258 (graphObject_: Obj1065) of type hasArgs
    self.drawConnections(
(self.obj1258,self.obj1215,[862.0, 336.0, 782.0, 284.0],"true", 2) )
    # Connections for obj1259 (graphObject_: Obj1066) of type hasArgs
    self.drawConnections(
(self.obj1259,self.obj1196,[910.0, 298.0, 894.0, 194.0],"true", 2) )
    # Connections for obj1260 (graphObject_: Obj1067) of type hasArgs
    self.drawConnections(
(self.obj1260,self.obj1216,[958.0, 353.0, 1070.0, 280.0],"true", 2) )

newfunction = Transition2QInstSIBLING_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
