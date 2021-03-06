"""
__Transition2QInstSIBLING_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 16:38:05 2015
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


    self.obj251=MatchModel(self)
    self.obj251.isGraphObjectVisual = True

    if(hasattr(self.obj251, '_setHierarchicalLink')):
      self.obj251._setHierarchicalLink(False)

    self.obj251.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj251)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj251.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj251)
    self.globalAndLocalPostcondition(self.obj251, rootNode)
    self.obj251.postAction( rootNode.CREATE )

    self.obj252=ApplyModel(self)
    self.obj252.isGraphObjectVisual = True

    if(hasattr(self.obj252, '_setHierarchicalLink')):
      self.obj252._setHierarchicalLink(False)

    self.obj252.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,368.0,self.obj252)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, -3.0]
    else: new_obj = None
    self.obj252.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj252)
    self.globalAndLocalPostcondition(self.obj252, rootNode)
    self.obj252.postAction( rootNode.CREATE )

    self.obj253=Vertex(self)
    self.obj253.isGraphObjectVisual = True

    if(hasattr(self.obj253, '_setHierarchicalLink')):
      self.obj253._setHierarchicalLink(False)

    # name
    self.obj253.name.setValue('vertex1')

    # classtype
    self.obj253.classtype.setValue('Vertex')

    # cardinality
    self.obj253.cardinality.setValue('1')

    self.obj253.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(740.0,40.0,self.obj253)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj253.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj253)
    self.globalAndLocalPostcondition(self.obj253, rootNode)
    self.obj253.postAction( rootNode.CREATE )

    self.obj254=Transition(self)
    self.obj254.isGraphObjectVisual = True

    if(hasattr(self.obj254, '_setHierarchicalLink')):
      self.obj254._setHierarchicalLink(False)

    # name
    self.obj254.name.setValue('transition1')

    # classtype
    self.obj254.classtype.setValue('Transition')

    # cardinality
    self.obj254.cardinality.setValue('+')

    self.obj254.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(180.0,40.0,self.obj254)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj254.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj254)
    self.globalAndLocalPostcondition(self.obj254, rootNode)
    self.obj254.postAction( rootNode.CREATE )

    self.obj255=StateMachine(self)
    self.obj255.isGraphObjectVisual = True

    if(hasattr(self.obj255, '_setHierarchicalLink')):
      self.obj255._setHierarchicalLink(False)

    # name
    self.obj255.name.setValue('stateMachine1')

    # classtype
    self.obj255.classtype.setValue('StateMachine')

    # cardinality
    self.obj255.cardinality.setValue('1')

    self.obj255.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(460.0,100.0,self.obj255)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj255.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj255)
    self.globalAndLocalPostcondition(self.obj255, rootNode)
    self.obj255.postAction( rootNode.CREATE )

    self.obj256=SIBLING0(self)
    self.obj256.isGraphObjectVisual = True

    if(hasattr(self.obj256, '_setHierarchicalLink')):
      self.obj256._setHierarchicalLink(False)

    # classtype
    self.obj256.classtype.setValue('SIBLING0')

    # cardinality
    self.obj256.cardinality.setValue('1')

    # name
    self.obj256.name.setValue('sibling0_1')

    self.obj256.graphClass_= graph_SIBLING0
    if self.genGraphics:
       new_obj = graph_SIBLING0(180.0,160.0,self.obj256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj256.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj256)
    self.globalAndLocalPostcondition(self.obj256, rootNode)
    self.obj256.postAction( rootNode.CREATE )

    self.obj257=Name(self)
    self.obj257.isGraphObjectVisual = True

    if(hasattr(self.obj257, '_setHierarchicalLink')):
      self.obj257._setHierarchicalLink(False)

    # classtype
    self.obj257.classtype.setValue('Name')

    # cardinality
    self.obj257.cardinality.setValue('1')

    # name
    self.obj257.name.setValue('name1')

    self.obj257.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(978.0,480.0,self.obj257)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj257.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj257)
    self.globalAndLocalPostcondition(self.obj257, rootNode)
    self.obj257.postAction( rootNode.CREATE )

    self.obj258=Name(self)
    self.obj258.isGraphObjectVisual = True

    if(hasattr(self.obj258, '_setHierarchicalLink')):
      self.obj258._setHierarchicalLink(False)

    # classtype
    self.obj258.classtype.setValue('Name')

    # cardinality
    self.obj258.cardinality.setValue('1')

    # name
    self.obj258.name.setValue('name2')

    self.obj258.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(796.0,540.0,self.obj258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 13.0]
    else: new_obj = None
    self.obj258.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj258)
    self.globalAndLocalPostcondition(self.obj258, rootNode)
    self.obj258.postAction( rootNode.CREATE )

    self.obj259=Name(self)
    self.obj259.isGraphObjectVisual = True

    if(hasattr(self.obj259, '_setHierarchicalLink')):
      self.obj259._setHierarchicalLink(False)

    # classtype
    self.obj259.classtype.setValue('Name')

    # cardinality
    self.obj259.cardinality.setValue('1')

    # name
    self.obj259.name.setValue('name3')

    self.obj259.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(615.0,590.0,self.obj259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj259)
    self.globalAndLocalPostcondition(self.obj259, rootNode)
    self.obj259.postAction( rootNode.CREATE )

    self.obj260=Name(self)
    self.obj260.isGraphObjectVisual = True

    if(hasattr(self.obj260, '_setHierarchicalLink')):
      self.obj260._setHierarchicalLink(False)

    # classtype
    self.obj260.classtype.setValue('Name')

    # cardinality
    self.obj260.cardinality.setValue('1')

    # name
    self.obj260.name.setValue('name4')

    self.obj260.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(434.0,610.0,self.obj260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj260)
    self.globalAndLocalPostcondition(self.obj260, rootNode)
    self.obj260.postAction( rootNode.CREATE )

    self.obj261=Inst(self)
    self.obj261.isGraphObjectVisual = True

    if(hasattr(self.obj261, '_setHierarchicalLink')):
      self.obj261._setHierarchicalLink(False)

    # classtype
    self.obj261.classtype.setValue('Inst')

    # cardinality
    self.obj261.cardinality.setValue('1')

    # name
    self.obj261.name.setValue('inst1')

    self.obj261.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(160.0,480.0,self.obj261)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, 0.0]
    else: new_obj = None
    self.obj261.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj261)
    self.globalAndLocalPostcondition(self.obj261, rootNode)
    self.obj261.postAction( rootNode.CREATE )

    self.obj262=Attribute(self)
    self.obj262.isGraphObjectVisual = True

    if(hasattr(self.obj262, '_setHierarchicalLink')):
      self.obj262._setHierarchicalLink(False)

    # Type
    self.obj262.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj262.Type.config = 0

    # name
    self.obj262.name.setValue('name')

    self.obj262.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(760.0,160.0,self.obj262)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj262.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj262)
    self.globalAndLocalPostcondition(self.obj262, rootNode)
    self.obj262.postAction( rootNode.CREATE )

    self.obj263=Attribute(self)
    self.obj263.isGraphObjectVisual = True

    if(hasattr(self.obj263, '_setHierarchicalLink')):
      self.obj263._setHierarchicalLink(False)

    # Type
    self.obj263.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj263.Type.config = 0

    # name
    self.obj263.name.setValue('name')

    self.obj263.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,192.0,self.obj263)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 3.0]
    else: new_obj = None
    self.obj263.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj263)
    self.globalAndLocalPostcondition(self.obj263, rootNode)
    self.obj263.postAction( rootNode.CREATE )

    self.obj264=Attribute(self)
    self.obj264.isGraphObjectVisual = True

    if(hasattr(self.obj264, '_setHierarchicalLink')):
      self.obj264._setHierarchicalLink(False)

    # Type
    self.obj264.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj264.Type.config = 0

    # name
    self.obj264.name.setValue('name')

    self.obj264.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(220.0,400.0,self.obj264)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 2.0]
    else: new_obj = None
    self.obj264.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj264)
    self.globalAndLocalPostcondition(self.obj264, rootNode)
    self.obj264.postAction( rootNode.CREATE )

    self.obj265=Attribute(self)
    self.obj265.isGraphObjectVisual = True

    if(hasattr(self.obj265, '_setHierarchicalLink')):
      self.obj265._setHierarchicalLink(False)

    # Type
    self.obj265.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj265.Type.config = 0

    # name
    self.obj265.name.setValue('literal')

    self.obj265.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(975.0,593.0,self.obj265)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [3.0, -1.0]
    else: new_obj = None
    self.obj265.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj265)
    self.globalAndLocalPostcondition(self.obj265, rootNode)
    self.obj265.postAction( rootNode.CREATE )

    self.obj266=Attribute(self)
    self.obj266.isGraphObjectVisual = True

    if(hasattr(self.obj266, '_setHierarchicalLink')):
      self.obj266._setHierarchicalLink(False)

    # Type
    self.obj266.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj266.Type.config = 0

    # name
    self.obj266.name.setValue('literal')

    self.obj266.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(800.0,646.0,self.obj266)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj266.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj266)
    self.globalAndLocalPostcondition(self.obj266, rootNode)
    self.obj266.postAction( rootNode.CREATE )

    self.obj267=Attribute(self)
    self.obj267.isGraphObjectVisual = True

    if(hasattr(self.obj267, '_setHierarchicalLink')):
      self.obj267._setHierarchicalLink(False)

    # Type
    self.obj267.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj267.Type.config = 0

    # name
    self.obj267.name.setValue('literal')

    self.obj267.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,420.0,self.obj267)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj267.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj267)
    self.globalAndLocalPostcondition(self.obj267, rootNode)
    self.obj267.postAction( rootNode.CREATE )

    self.obj268=Attribute(self)
    self.obj268.isGraphObjectVisual = True

    if(hasattr(self.obj268, '_setHierarchicalLink')):
      self.obj268._setHierarchicalLink(False)

    # Type
    self.obj268.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj268.Type.config = 0

    # name
    self.obj268.name.setValue('literal')

    self.obj268.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(429.0,711.0,self.obj268)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj268.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj268)
    self.globalAndLocalPostcondition(self.obj268, rootNode)
    self.obj268.postAction( rootNode.CREATE )

    self.obj269=Attribute(self)
    self.obj269.isGraphObjectVisual = True

    if(hasattr(self.obj269, '_setHierarchicalLink')):
      self.obj269._setHierarchicalLink(False)

    # Type
    self.obj269.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj269.Type.config = 0

    # name
    self.obj269.name.setValue('pivot')

    self.obj269.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(20.0,560.0,self.obj269)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj269.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj269)
    self.globalAndLocalPostcondition(self.obj269, rootNode)
    self.obj269.postAction( rootNode.CREATE )

    self.obj270=Equation(self)
    self.obj270.isGraphObjectVisual = True

    if(hasattr(self.obj270, '_setHierarchicalLink')):
      self.obj270._setHierarchicalLink(False)

    # name
    self.obj270.name.setValue('eq1')

    self.obj270.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(226.0,327.0,self.obj270)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 6.0]
    else: new_obj = None
    self.obj270.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj270)
    self.globalAndLocalPostcondition(self.obj270, rootNode)
    self.obj270.postAction( rootNode.CREATE )

    self.obj271=Equation(self)
    self.obj271.isGraphObjectVisual = True

    if(hasattr(self.obj271, '_setHierarchicalLink')):
      self.obj271._setHierarchicalLink(False)

    # name
    self.obj271.name.setValue('eq2')

    self.obj271.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1147.0,594.0,self.obj271)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-7.0, 3.0]
    else: new_obj = None
    self.obj271.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj271)
    self.globalAndLocalPostcondition(self.obj271, rootNode)
    self.obj271.postAction( rootNode.CREATE )

    self.obj272=Equation(self)
    self.obj272.isGraphObjectVisual = True

    if(hasattr(self.obj272, '_setHierarchicalLink')):
      self.obj272._setHierarchicalLink(False)

    # name
    self.obj272.name.setValue('eq3')

    self.obj272.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(975.0,683.0,self.obj272)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj272.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj272)
    self.globalAndLocalPostcondition(self.obj272, rootNode)
    self.obj272.postAction( rootNode.CREATE )

    self.obj273=Equation(self)
    self.obj273.isGraphObjectVisual = True

    if(hasattr(self.obj273, '_setHierarchicalLink')):
      self.obj273._setHierarchicalLink(False)

    # name
    self.obj273.name.setValue('eq4')

    self.obj273.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(788.0,428.0,self.obj273)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj273.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj273)
    self.globalAndLocalPostcondition(self.obj273, rootNode)
    self.obj273.postAction( rootNode.CREATE )

    self.obj274=Equation(self)
    self.obj274.isGraphObjectVisual = True

    if(hasattr(self.obj274, '_setHierarchicalLink')):
      self.obj274._setHierarchicalLink(False)

    # name
    self.obj274.name.setValue('eq5')

    self.obj274.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(264.0,724.0,self.obj274)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj274.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj274)
    self.globalAndLocalPostcondition(self.obj274, rootNode)
    self.obj274.postAction( rootNode.CREATE )

    self.obj275=Equation(self)
    self.obj275.isGraphObjectVisual = True

    if(hasattr(self.obj275, '_setHierarchicalLink')):
      self.obj275._setHierarchicalLink(False)

    # name
    self.obj275.name.setValue('eq6')

    self.obj275.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(180.0,580.0,self.obj275)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj275.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj275)
    self.globalAndLocalPostcondition(self.obj275, rootNode)
    self.obj275.postAction( rootNode.CREATE )

    self.obj276=Concat(self)
    self.obj276.isGraphObjectVisual = True

    if(hasattr(self.obj276, '_setHierarchicalLink')):
      self.obj276._setHierarchicalLink(False)

    # Type
    self.obj276.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj276.Type.config = 0

    # name
    self.obj276.name.setValue('concat1')

    self.obj276.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(396.0,327.0,self.obj276)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj276.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj276)
    self.globalAndLocalPostcondition(self.obj276, rootNode)
    self.obj276.postAction( rootNode.CREATE )

    self.obj277=Concat(self)
    self.obj277.isGraphObjectVisual = True

    if(hasattr(self.obj277, '_setHierarchicalLink')):
      self.obj277._setHierarchicalLink(False)

    # Type
    self.obj277.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj277.Type.config = 0

    # name
    self.obj277.name.setValue('concat2')

    self.obj277.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(792.0,324.0,self.obj277)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [5.0, -2.0]
    else: new_obj = None
    self.obj277.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj277)
    self.globalAndLocalPostcondition(self.obj277, rootNode)
    self.obj277.postAction( rootNode.CREATE )

    self.obj278=Constant(self)
    self.obj278.isGraphObjectVisual = True

    if(hasattr(self.obj278, '_setHierarchicalLink')):
      self.obj278._setHierarchicalLink(False)

    # Type
    self.obj278.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj278.Type.config = 0

    # name
    self.obj278.name.setValue('S')

    self.obj278.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(333.0,251.0,self.obj278)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj278.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj278)
    self.globalAndLocalPostcondition(self.obj278, rootNode)
    self.obj278.postAction( rootNode.CREATE )

    self.obj279=Constant(self)
    self.obj279.isGraphObjectVisual = True

    if(hasattr(self.obj279, '_setHierarchicalLink')):
      self.obj279._setHierarchicalLink(False)

    # Type
    self.obj279.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj279.Type.config = 0

    # name
    self.obj279.name.setValue('exit')

    self.obj279.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1140.0,674.0,self.obj279)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, -4.0]
    else: new_obj = None
    self.obj279.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj279)
    self.globalAndLocalPostcondition(self.obj279, rootNode)
    self.obj279.postAction( rootNode.CREATE )

    self.obj280=Constant(self)
    self.obj280.isGraphObjectVisual = True

    if(hasattr(self.obj280, '_setHierarchicalLink')):
      self.obj280._setHierarchicalLink(False)

    # Type
    self.obj280.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj280.Type.config = 0

    # name
    self.obj280.name.setValue('exack')

    self.obj280.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,723.0,self.obj280)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj280.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj280)
    self.globalAndLocalPostcondition(self.obj280, rootNode)
    self.obj280.postAction( rootNode.CREATE )

    self.obj281=Constant(self)
    self.obj281.isGraphObjectVisual = True

    if(hasattr(self.obj281, '_setHierarchicalLink')):
      self.obj281._setHierarchicalLink(False)

    # Type
    self.obj281.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj281.Type.config = 0

    # name
    self.obj281.name.setValue('xox')

    self.obj281.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(648.0,250.0,self.obj281)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj281.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj281)
    self.globalAndLocalPostcondition(self.obj281, rootNode)
    self.obj281.postAction( rootNode.CREATE )

    self.obj282=Constant(self)
    self.obj282.isGraphObjectVisual = True

    if(hasattr(self.obj282, '_setHierarchicalLink')):
      self.obj282._setHierarchicalLink(False)

    # Type
    self.obj282.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj282.Type.config = 0

    # name
    self.obj282.name.setValue('xox')

    self.obj282.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(936.0,246.0,self.obj282)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj282.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj282)
    self.globalAndLocalPostcondition(self.obj282, rootNode)
    self.obj282.postAction( rootNode.CREATE )

    self.obj283=Constant(self)
    self.obj283.isGraphObjectVisual = True

    if(hasattr(self.obj283, '_setHierarchicalLink')):
      self.obj283._setHierarchicalLink(False)

    # Type
    self.obj283.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj283.Type.config = 0

    # name
    self.obj283.name.setValue('sh')

    self.obj283.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,786.0,self.obj283)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj283.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj283)
    self.globalAndLocalPostcondition(self.obj283, rootNode)
    self.obj283.postAction( rootNode.CREATE )

    self.obj284=Constant(self)
    self.obj284.isGraphObjectVisual = True

    if(hasattr(self.obj284, '_setHierarchicalLink')):
      self.obj284._setHierarchicalLink(False)

    # Type
    self.obj284.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj284.Type.config = 0

    # name
    self.obj284.name.setValue('instfortrans')

    self.obj284.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(21.0,640.0,self.obj284)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj284.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj284)
    self.globalAndLocalPostcondition(self.obj284, rootNode)
    self.obj284.postAction( rootNode.CREATE )

    self.obj285=paired_with(self)
    self.obj285.isGraphObjectVisual = True

    if(hasattr(self.obj285, '_setHierarchicalLink')):
      self.obj285._setHierarchicalLink(False)

    self.obj285.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,182.0,self.obj285)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj285.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj285)
    self.globalAndLocalPostcondition(self.obj285, rootNode)
    self.obj285.postAction( rootNode.CREATE )

    self.obj286=match_contains(self)
    self.obj286.isGraphObjectVisual = True

    if(hasattr(self.obj286, '_setHierarchicalLink')):
      self.obj286._setHierarchicalLink(False)

    self.obj286.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj286)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj286.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj286)
    self.globalAndLocalPostcondition(self.obj286, rootNode)
    self.obj286.postAction( rootNode.CREATE )

    self.obj287=match_contains(self)
    self.obj287.isGraphObjectVisual = True

    if(hasattr(self.obj287, '_setHierarchicalLink')):
      self.obj287._setHierarchicalLink(False)

    self.obj287.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,127.0,self.obj287)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj287.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj287)
    self.globalAndLocalPostcondition(self.obj287, rootNode)
    self.obj287.postAction( rootNode.CREATE )

    self.obj288=match_contains(self)
    self.obj288.isGraphObjectVisual = True

    if(hasattr(self.obj288, '_setHierarchicalLink')):
      self.obj288._setHierarchicalLink(False)

    self.obj288.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,97.0,self.obj288)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj288.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj288)
    self.globalAndLocalPostcondition(self.obj288, rootNode)
    self.obj288.postAction( rootNode.CREATE )

    self.obj289=match_contains(self)
    self.obj289.isGraphObjectVisual = True

    if(hasattr(self.obj289, '_setHierarchicalLink')):
      self.obj289._setHierarchicalLink(False)

    self.obj289.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(524.0,67.0,self.obj289)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj289.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj289)
    self.globalAndLocalPostcondition(self.obj289, rootNode)
    self.obj289.postAction( rootNode.CREATE )

    self.obj290=apply_contains(self)
    self.obj290.isGraphObjectVisual = True

    if(hasattr(self.obj290, '_setHierarchicalLink')):
      self.obj290._setHierarchicalLink(False)

    self.obj290.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(237.5,466.0,self.obj290)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj290.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj290)
    self.globalAndLocalPostcondition(self.obj290, rootNode)
    self.obj290.postAction( rootNode.CREATE )

    self.obj291=apply_contains(self)
    self.obj291.isGraphObjectVisual = True

    if(hasattr(self.obj291, '_setHierarchicalLink')):
      self.obj291._setHierarchicalLink(False)

    self.obj291.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(374.5,531.0,self.obj291)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj291.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj291)
    self.globalAndLocalPostcondition(self.obj291, rootNode)
    self.obj291.postAction( rootNode.CREATE )

    self.obj292=apply_contains(self)
    self.obj292.isGraphObjectVisual = True

    if(hasattr(self.obj292, '_setHierarchicalLink')):
      self.obj292._setHierarchicalLink(False)

    self.obj292.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(465.0,521.0,self.obj292)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj292.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj292)
    self.globalAndLocalPostcondition(self.obj292, rootNode)
    self.obj292.postAction( rootNode.CREATE )

    self.obj293=apply_contains(self)
    self.obj293.isGraphObjectVisual = True

    if(hasattr(self.obj293, '_setHierarchicalLink')):
      self.obj293._setHierarchicalLink(False)

    self.obj293.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(555.5,496.0,self.obj293)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj293.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj293)
    self.globalAndLocalPostcondition(self.obj293, rootNode)
    self.obj293.postAction( rootNode.CREATE )

    self.obj294=apply_contains(self)
    self.obj294.isGraphObjectVisual = True

    if(hasattr(self.obj294, '_setHierarchicalLink')):
      self.obj294._setHierarchicalLink(False)

    self.obj294.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(646.5,466.0,self.obj294)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj294.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj294)
    self.globalAndLocalPostcondition(self.obj294, rootNode)
    self.obj294.postAction( rootNode.CREATE )

    self.obj295=directLink_T(self)
    self.obj295.isGraphObjectVisual = True

    if(hasattr(self.obj295, '_setHierarchicalLink')):
      self.obj295._setHierarchicalLink(False)

    # associationType
    self.obj295.associationType.setValue('channelNames')

    self.obj295.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(522.0,531.0,self.obj295)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj295.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj295)
    self.globalAndLocalPostcondition(self.obj295, rootNode)
    self.obj295.postAction( rootNode.CREATE )

    self.obj296=directLink_T(self)
    self.obj296.isGraphObjectVisual = True

    if(hasattr(self.obj296, '_setHierarchicalLink')):
      self.obj296._setHierarchicalLink(False)

    # associationType
    self.obj296.associationType.setValue('channelNames')

    self.obj296.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(645.5,566.0,self.obj296)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj296.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj296)
    self.globalAndLocalPostcondition(self.obj296, rootNode)
    self.obj296.postAction( rootNode.CREATE )

    self.obj297=directLink_T(self)
    self.obj297.isGraphObjectVisual = True

    if(hasattr(self.obj297, '_setHierarchicalLink')):
      self.obj297._setHierarchicalLink(False)

    # associationType
    self.obj297.associationType.setValue('channelNames')

    self.obj297.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(553.0,586.0,self.obj297)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj297.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj297)
    self.globalAndLocalPostcondition(self.obj297, rootNode)
    self.obj297.postAction( rootNode.CREATE )

    self.obj298=directLink_T(self)
    self.obj298.isGraphObjectVisual = True

    if(hasattr(self.obj298, '_setHierarchicalLink')):
      self.obj298._setHierarchicalLink(False)

    # associationType
    self.obj298.associationType.setValue('channelNames')

    self.obj298.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(469.0,596.0,self.obj298)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj298.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj298)
    self.globalAndLocalPostcondition(self.obj298, rootNode)
    self.obj298.postAction( rootNode.CREATE )

    self.obj299=directLink_S(self)
    self.obj299.isGraphObjectVisual = True

    if(hasattr(self.obj299, '_setHierarchicalLink')):
      self.obj299._setHierarchicalLink(False)

    # associationType
    self.obj299.associationType.setValue('type')

    self.obj299.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(350.0,153.0,self.obj299)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj299.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj299)
    self.globalAndLocalPostcondition(self.obj299, rootNode)
    self.obj299.postAction( rootNode.CREATE )

    self.obj300=directLink_S(self)
    self.obj300.isGraphObjectVisual = True

    if(hasattr(self.obj300, '_setHierarchicalLink')):
      self.obj300._setHierarchicalLink(False)

    # associationType
    self.obj300.associationType.setValue('dest')

    self.obj300.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(640.0,84.0,self.obj300)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj300.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj300)
    self.globalAndLocalPostcondition(self.obj300, rootNode)
    self.obj300.postAction( rootNode.CREATE )

    self.obj301=directLink_S(self)
    self.obj301.isGraphObjectVisual = True

    if(hasattr(self.obj301, '_setHierarchicalLink')):
      self.obj301._setHierarchicalLink(False)

    # associationType
    self.obj301.associationType.setValue('owningStateMachine')

    self.obj301.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(770.0,113.0,self.obj301)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj301.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj301)
    self.globalAndLocalPostcondition(self.obj301, rootNode)
    self.obj301.postAction( rootNode.CREATE )

    self.obj302=hasAttribute_S(self)
    self.obj302.isGraphObjectVisual = True

    if(hasattr(self.obj302, '_setHierarchicalLink')):
      self.obj302._setHierarchicalLink(False)

    self.obj302.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(902.0,148.5,self.obj302)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj302.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj302)
    self.globalAndLocalPostcondition(self.obj302, rootNode)
    self.obj302.postAction( rootNode.CREATE )

    self.obj303=hasAttribute_S(self)
    self.obj303.isGraphObjectVisual = True

    if(hasattr(self.obj303, '_setHierarchicalLink')):
      self.obj303._setHierarchicalLink(False)

    self.obj303.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(622.0,184.5,self.obj303)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj303.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj303)
    self.globalAndLocalPostcondition(self.obj303, rootNode)
    self.obj303.postAction( rootNode.CREATE )

    self.obj304=hasAttribute_T(self)
    self.obj304.isGraphObjectVisual = True

    if(hasattr(self.obj304, '_setHierarchicalLink')):
      self.obj304._setHierarchicalLink(False)

    self.obj304.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(343.0,482.5,self.obj304)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj304.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj304)
    self.globalAndLocalPostcondition(self.obj304, rootNode)
    self.obj304.postAction( rootNode.CREATE )

    self.obj305=hasAttribute_T(self)
    self.obj305.isGraphObjectVisual = True

    if(hasattr(self.obj305, '_setHierarchicalLink')):
      self.obj305._setHierarchicalLink(False)

    self.obj305.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1127.0,592.0,self.obj305)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj305.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj305)
    self.globalAndLocalPostcondition(self.obj305, rootNode)
    self.obj305.postAction( rootNode.CREATE )

    self.obj306=hasAttribute_T(self)
    self.obj306.isGraphObjectVisual = True

    if(hasattr(self.obj306, '_setHierarchicalLink')):
      self.obj306._setHierarchicalLink(False)

    self.obj306.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(946.5,649.0,self.obj306)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj306.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj306)
    self.globalAndLocalPostcondition(self.obj306, rootNode)
    self.obj306.postAction( rootNode.CREATE )

    self.obj307=hasAttribute_T(self)
    self.obj307.isGraphObjectVisual = True

    if(hasattr(self.obj307, '_setHierarchicalLink')):
      self.obj307._setHierarchicalLink(False)

    self.obj307.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(777.5,567.5,self.obj307)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj307.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj307)
    self.globalAndLocalPostcondition(self.obj307, rootNode)
    self.obj307.postAction( rootNode.CREATE )

    self.obj308=hasAttribute_T(self)
    self.obj308.isGraphObjectVisual = True

    if(hasattr(self.obj308, '_setHierarchicalLink')):
      self.obj308._setHierarchicalLink(False)

    self.obj308.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(584.5,703.0,self.obj308)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj308.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj308)
    self.globalAndLocalPostcondition(self.obj308, rootNode)
    self.obj308.postAction( rootNode.CREATE )

    self.obj309=hasAttribute_T(self)
    self.obj309.isGraphObjectVisual = True

    if(hasattr(self.obj309, '_setHierarchicalLink')):
      self.obj309._setHierarchicalLink(False)

    self.obj309.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(243.0,562.5,self.obj309)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj309.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj309)
    self.globalAndLocalPostcondition(self.obj309, rootNode)
    self.obj309.postAction( rootNode.CREATE )

    self.obj310=leftExpr(self)
    self.obj310.isGraphObjectVisual = True

    if(hasattr(self.obj310, '_setHierarchicalLink')):
      self.obj310._setHierarchicalLink(False)

    self.obj310.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(358.0,403.5,self.obj310)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj310.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj310)
    self.globalAndLocalPostcondition(self.obj310, rootNode)
    self.obj310.postAction( rootNode.CREATE )

    self.obj311=leftExpr(self)
    self.obj311.isGraphObjectVisual = True

    if(hasattr(self.obj311, '_setHierarchicalLink')):
      self.obj311._setHierarchicalLink(False)

    self.obj311.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,630.0,self.obj311)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj311.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj311)
    self.globalAndLocalPostcondition(self.obj311, rootNode)
    self.obj311.postAction( rootNode.CREATE )

    self.obj312=leftExpr(self)
    self.obj312.isGraphObjectVisual = True

    if(hasattr(self.obj312, '_setHierarchicalLink')):
      self.obj312._setHierarchicalLink(False)

    self.obj312.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1023.5,709.5,self.obj312)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj312.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj312)
    self.globalAndLocalPostcondition(self.obj312, rootNode)
    self.obj312.postAction( rootNode.CREATE )

    self.obj313=leftExpr(self)
    self.obj313.isGraphObjectVisual = True

    if(hasattr(self.obj313, '_setHierarchicalLink')):
      self.obj313._setHierarchicalLink(False)

    self.obj313.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(793.0,464.0,self.obj313)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj313.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj313)
    self.globalAndLocalPostcondition(self.obj313, rootNode)
    self.obj313.postAction( rootNode.CREATE )

    self.obj314=leftExpr(self)
    self.obj314.isGraphObjectVisual = True

    if(hasattr(self.obj314, '_setHierarchicalLink')):
      self.obj314._setHierarchicalLink(False)

    self.obj314.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(482.5,754.0,self.obj314)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj314.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj314)
    self.globalAndLocalPostcondition(self.obj314, rootNode)
    self.obj314.postAction( rootNode.CREATE )

    self.obj315=leftExpr(self)
    self.obj315.isGraphObjectVisual = True

    if(hasattr(self.obj315, '_setHierarchicalLink')):
      self.obj315._setHierarchicalLink(False)

    self.obj315.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(236.0,606.5,self.obj315)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj315.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj315)
    self.globalAndLocalPostcondition(self.obj315, rootNode)
    self.obj315.postAction( rootNode.CREATE )

    self.obj316=rightExpr(self)
    self.obj316.isGraphObjectVisual = True

    if(hasattr(self.obj316, '_setHierarchicalLink')):
      self.obj316._setHierarchicalLink(False)

    self.obj316.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(447.0,363.5,self.obj316)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj316.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj316)
    self.globalAndLocalPostcondition(self.obj316, rootNode)
    self.obj316.postAction( rootNode.CREATE )

    self.obj317=rightExpr(self)
    self.obj317.isGraphObjectVisual = True

    if(hasattr(self.obj317, '_setHierarchicalLink')):
      self.obj317._setHierarchicalLink(False)

    self.obj317.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1279.5,683.5,self.obj317)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj317.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj317)
    self.globalAndLocalPostcondition(self.obj317, rootNode)
    self.obj317.postAction( rootNode.CREATE )

    self.obj318=rightExpr(self)
    self.obj318.isGraphObjectVisual = True

    if(hasattr(self.obj318, '_setHierarchicalLink')):
      self.obj318._setHierarchicalLink(False)

    self.obj318.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1023.5,753.5,self.obj318)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj318.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj318)
    self.globalAndLocalPostcondition(self.obj318, rootNode)
    self.obj318.postAction( rootNode.CREATE )

    self.obj319=rightExpr(self)
    self.obj319.isGraphObjectVisual = True

    if(hasattr(self.obj319, '_setHierarchicalLink')):
      self.obj319._setHierarchicalLink(False)

    self.obj319.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(926.0,449.0,self.obj319)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj319.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj319)
    self.globalAndLocalPostcondition(self.obj319, rootNode)
    self.obj319.postAction( rootNode.CREATE )

    self.obj320=rightExpr(self)
    self.obj320.isGraphObjectVisual = True

    if(hasattr(self.obj320, '_setHierarchicalLink')):
      self.obj320._setHierarchicalLink(False)

    self.obj320.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(478.0,791.5,self.obj320)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj320.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj320)
    self.globalAndLocalPostcondition(self.obj320, rootNode)
    self.obj320.postAction( rootNode.CREATE )

    self.obj321=rightExpr(self)
    self.obj321.isGraphObjectVisual = True

    if(hasattr(self.obj321, '_setHierarchicalLink')):
      self.obj321._setHierarchicalLink(False)

    self.obj321.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(236.5,646.5,self.obj321)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj321.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj321)
    self.globalAndLocalPostcondition(self.obj321, rootNode)
    self.obj321.postAction( rootNode.CREATE )

    self.obj322=hasArgs(self)
    self.obj322.isGraphObjectVisual = True

    if(hasattr(self.obj322, '_setHierarchicalLink')):
      self.obj322._setHierarchicalLink(False)

    self.obj322.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(498.5,323.0,self.obj322)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj322.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj322)
    self.globalAndLocalPostcondition(self.obj322, rootNode)
    self.obj322.postAction( rootNode.CREATE )

    self.obj323=hasArgs(self)
    self.obj323.isGraphObjectVisual = True

    if(hasattr(self.obj323, '_setHierarchicalLink')):
      self.obj323._setHierarchicalLink(False)

    self.obj323.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(572.0,293.5,self.obj323)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj323.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj323)
    self.globalAndLocalPostcondition(self.obj323, rootNode)
    self.obj323.postAction( rootNode.CREATE )

    self.obj324=hasArgs(self)
    self.obj324.isGraphObjectVisual = True

    if(hasattr(self.obj324, '_setHierarchicalLink')):
      self.obj324._setHierarchicalLink(False)

    self.obj324.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(862.0,336.0,self.obj324)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj324.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj324)
    self.globalAndLocalPostcondition(self.obj324, rootNode)
    self.obj324.postAction( rootNode.CREATE )

    self.obj325=hasArgs(self)
    self.obj325.isGraphObjectVisual = True

    if(hasattr(self.obj325, '_setHierarchicalLink')):
      self.obj325._setHierarchicalLink(False)

    self.obj325.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(910.0,298.0,self.obj325)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj325.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj325)
    self.globalAndLocalPostcondition(self.obj325, rootNode)
    self.obj325.postAction( rootNode.CREATE )

    self.obj326=hasArgs(self)
    self.obj326.isGraphObjectVisual = True

    if(hasattr(self.obj326, '_setHierarchicalLink')):
      self.obj326._setHierarchicalLink(False)

    self.obj326.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(958.0,353.0,self.obj326)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj326.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj326)
    self.globalAndLocalPostcondition(self.obj326, rootNode)
    self.obj326.postAction( rootNode.CREATE )

    # Connections for obj251 (graphObject_: Obj140) of type MatchModel
    self.drawConnections(
(self.obj251,self.obj285,[138.0, 51.0, 140.5, 182.0],"true", 2),
(self.obj251,self.obj286,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj251,self.obj287,[138.0, 51.0, 244.0, 127.0],"true", 2),
(self.obj251,self.obj288,[138.0, 51.0, 384.0, 97.0],"true", 2),
(self.obj251,self.obj289,[138.0, 51.0, 524.0, 67.0],"true", 2) )
    # Connections for obj252 (graphObject_: Obj141) of type ApplyModel
    self.drawConnections(
(self.obj252,self.obj290,[143.0, 401.0, 237.5, 466.0],"true", 2),
(self.obj252,self.obj291,[143.0, 401.0, 374.5, 531.0],"true", 2),
(self.obj252,self.obj292,[143.0, 401.0, 465.0, 521.0],"true", 2),
(self.obj252,self.obj293,[143.0, 401.0, 555.5, 496.0],"true", 2),
(self.obj252,self.obj294,[143.0, 401.0, 646.5, 466.0],"true", 2) )
    # Connections for obj253 (graphObject_: Obj142) named vertex1
    self.drawConnections(
(self.obj253,self.obj302,[910.0, 83.0, 902.0, 148.5],"true", 2),
(self.obj253,self.obj301,[910.0, 83.0, 770.0, 113.0],"true", 2) )
    # Connections for obj254 (graphObject_: Obj143) named transition1
    self.drawConnections(
(self.obj254,self.obj299,[350.0, 83.0, 350.0, 153.0],"true", 2),
(self.obj254,self.obj300,[350.0, 83.0, 640.0, 84.0],"true", 2) )
    # Connections for obj255 (graphObject_: Obj144) named stateMachine1
    self.drawConnections(
(self.obj255,self.obj303,[630.0, 143.0, 622.0, 184.5],"true", 2) )
    # Connections for obj256 (graphObject_: Obj145) named sibling0_1
    self.drawConnections(
 )
    # Connections for obj257 (graphObject_: Obj146) named name1
    self.drawConnections(
(self.obj257,self.obj305,[1150.0, 531.0, 1127.0, 592.0],"true", 2) )
    # Connections for obj258 (graphObject_: Obj147) named name2
    self.drawConnections(
(self.obj258,self.obj306,[968.0, 591.0, 946.5, 649.0],"true", 2) )
    # Connections for obj259 (graphObject_: Obj148) named name3
    self.drawConnections(
(self.obj259,self.obj307,[787.0, 641.0, 777.5, 567.5],"true", 2) )
    # Connections for obj260 (graphObject_: Obj149) named name4
    self.drawConnections(
(self.obj260,self.obj308,[606.0, 661.0, 584.5, 703.0],"true", 2) )
    # Connections for obj261 (graphObject_: Obj150) named inst1
    self.drawConnections(
(self.obj261,self.obj304,[332.0, 531.0, 343.0, 482.5],"true", 2),
(self.obj261,self.obj295,[332.0, 531.0, 522.0, 531.0],"true", 2),
(self.obj261,self.obj296,[332.0, 531.0, 645.5, 566.0],"true", 2),
(self.obj261,self.obj297,[332.0, 531.0, 553.0, 586.0],"true", 2),
(self.obj261,self.obj298,[332.0, 531.0, 469.0, 596.0],"true", 2),
(self.obj261,self.obj309,[332.0, 531.0, 243.0, 562.5],"true", 2) )
    # Connections for obj262 (graphObject_: Obj151) named name
    self.drawConnections(
 )
    # Connections for obj263 (graphObject_: Obj152) named name
    self.drawConnections(
 )
    # Connections for obj264 (graphObject_: Obj153) named name
    self.drawConnections(
 )
    # Connections for obj265 (graphObject_: Obj154) named literal
    self.drawConnections(
 )
    # Connections for obj266 (graphObject_: Obj155) named literal
    self.drawConnections(
 )
    # Connections for obj267 (graphObject_: Obj156) named literal
    self.drawConnections(
 )
    # Connections for obj268 (graphObject_: Obj157) named literal
    self.drawConnections(
 )
    # Connections for obj269 (graphObject_: Obj158) named pivot
    self.drawConnections(
 )
    # Connections for obj270 (graphObject_: Obj159) named eq1
    self.drawConnections(
(self.obj270,self.obj310,[364.0, 366.0, 358.0, 403.5],"true", 2),
(self.obj270,self.obj316,[364.0, 366.0, 447.0, 363.5],"true", 2) )
    # Connections for obj271 (graphObject_: Obj160) named eq2
    self.drawConnections(
(self.obj271,self.obj311,[1285.0, 633.0, 1100.0, 630.0],"true", 2),
(self.obj271,self.obj317,[1285.0, 633.0, 1279.5, 683.5],"true", 2) )
    # Connections for obj272 (graphObject_: Obj161) named eq3
    self.drawConnections(
(self.obj272,self.obj312,[1113.0, 722.0, 1023.5, 709.5],"true", 2),
(self.obj272,self.obj318,[1113.0, 722.0, 1023.5, 753.5],"true", 2) )
    # Connections for obj273 (graphObject_: Obj162) named eq4
    self.drawConnections(
(self.obj273,self.obj313,[926.0, 467.0, 793.0, 464.0],"true", 2),
(self.obj273,self.obj319,[926.0, 467.0, 926.0, 449.0],"true", 2) )
    # Connections for obj274 (graphObject_: Obj163) named eq5
    self.drawConnections(
(self.obj274,self.obj314,[402.0, 763.0, 482.5, 754.0],"true", 2),
(self.obj274,self.obj320,[402.0, 763.0, 478.0, 791.5],"true", 2) )
    # Connections for obj275 (graphObject_: Obj164) named eq6
    self.drawConnections(
(self.obj275,self.obj321,[318.0, 619.0, 236.5, 646.5],"true", 2),
(self.obj275,self.obj315,[318.0, 619.0, 236.0, 606.5],"true", 2) )
    # Connections for obj276 (graphObject_: Obj165) named concat1
    self.drawConnections(
(self.obj276,self.obj322,[530.0, 361.0, 498.5, 323.0],"true", 2),
(self.obj276,self.obj323,[530.0, 361.0, 572.0, 293.5],"true", 2) )
    # Connections for obj277 (graphObject_: Obj166) named concat2
    self.drawConnections(
(self.obj277,self.obj324,[926.0, 358.0, 862.0, 336.0],"true", 2),
(self.obj277,self.obj325,[926.0, 358.0, 910.0, 298.0],"true", 2),
(self.obj277,self.obj326,[926.0, 358.0, 958.0, 353.0],"true", 2) )
    # Connections for obj278 (graphObject_: Obj167) named S
    self.drawConnections(
 )
    # Connections for obj279 (graphObject_: Obj168) named exit
    self.drawConnections(
 )
    # Connections for obj280 (graphObject_: Obj169) named exack
    self.drawConnections(
 )
    # Connections for obj281 (graphObject_: Obj170) named xox
    self.drawConnections(
 )
    # Connections for obj282 (graphObject_: Obj171) named xox
    self.drawConnections(
 )
    # Connections for obj283 (graphObject_: Obj172) named sh
    self.drawConnections(
 )
    # Connections for obj284 (graphObject_: Obj173) named instfortrans
    self.drawConnections(
 )
    # Connections for obj285 (graphObject_: Obj174) of type paired_with
    self.drawConnections(
(self.obj285,self.obj252,[140.5, 182.0, 143.0, 401.0],"true", 2) )
    # Connections for obj286 (graphObject_: Obj175) of type match_contains
    self.drawConnections(
(self.obj286,self.obj254,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj287 (graphObject_: Obj176) of type match_contains
    self.drawConnections(
(self.obj287,self.obj256,[244.0, 127.0, 350.0, 203.0],"true", 2) )
    # Connections for obj288 (graphObject_: Obj177) of type match_contains
    self.drawConnections(
(self.obj288,self.obj255,[384.0, 97.0, 630.0, 143.0],"true", 2) )
    # Connections for obj289 (graphObject_: Obj178) of type match_contains
    self.drawConnections(
(self.obj289,self.obj253,[524.0, 67.0, 910.0, 83.0],"true", 2) )
    # Connections for obj290 (graphObject_: Obj179) of type apply_contains
    self.drawConnections(
(self.obj290,self.obj261,[237.5, 466.0, 332.0, 531.0],"true", 2) )
    # Connections for obj291 (graphObject_: Obj180) of type apply_contains
    self.drawConnections(
(self.obj291,self.obj260,[374.5, 531.0, 606.0, 661.0],"true", 2) )
    # Connections for obj292 (graphObject_: Obj181) of type apply_contains
    self.drawConnections(
(self.obj292,self.obj259,[465.0, 521.0, 787.0, 641.0],"true", 2) )
    # Connections for obj293 (graphObject_: Obj182) of type apply_contains
    self.drawConnections(
(self.obj293,self.obj258,[555.5, 496.0, 968.0, 591.0],"true", 2) )
    # Connections for obj294 (graphObject_: Obj183) of type apply_contains
    self.drawConnections(
(self.obj294,self.obj257,[646.5, 466.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj295 (graphObject_: Obj184) of type directLink_T
    self.drawConnections(
(self.obj295,self.obj257,[522.0, 531.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj296 (graphObject_: Obj185) of type directLink_T
    self.drawConnections(
(self.obj296,self.obj258,[645.5, 566.0, 968.0, 591.0],"true", 2) )
    # Connections for obj297 (graphObject_: Obj186) of type directLink_T
    self.drawConnections(
(self.obj297,self.obj259,[553.0, 586.0, 787.0, 641.0],"true", 2) )
    # Connections for obj298 (graphObject_: Obj187) of type directLink_T
    self.drawConnections(
(self.obj298,self.obj260,[469.0, 596.0, 606.0, 661.0],"true", 2) )
    # Connections for obj299 (graphObject_: Obj188) of type directLink_S
    self.drawConnections(
(self.obj299,self.obj256,[350.0, 153.0, 350.0, 203.0],"true", 2) )
    # Connections for obj300 (graphObject_: Obj189) of type directLink_S
    self.drawConnections(
(self.obj300,self.obj253,[640.0, 84.0, 910.0, 83.0],"true", 2) )
    # Connections for obj301 (graphObject_: Obj190) of type directLink_S
    self.drawConnections(
(self.obj301,self.obj255,[770.0, 113.0, 630.0, 143.0],"true", 2) )
    # Connections for obj302 (graphObject_: Obj191) of type hasAttribute_S
    self.drawConnections(
(self.obj302,self.obj262,[902.0, 148.5, 894.0, 194.0],"true", 2) )
    # Connections for obj303 (graphObject_: Obj192) of type hasAttribute_S
    self.drawConnections(
(self.obj303,self.obj263,[622.0, 184.5, 614.0, 226.0],"true", 2) )
    # Connections for obj304 (graphObject_: Obj193) of type hasAttribute_T
    self.drawConnections(
(self.obj304,self.obj264,[343.0, 482.5, 354.0, 434.0],"true", 2) )
    # Connections for obj305 (graphObject_: Obj194) of type hasAttribute_T
    self.drawConnections(
(self.obj305,self.obj265,[1127.0, 592.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj306 (graphObject_: Obj195) of type hasAttribute_T
    self.drawConnections(
(self.obj306,self.obj266,[946.5, 649.0, 934.0, 680.0],"true", 2) )
    # Connections for obj307 (graphObject_: Obj196) of type hasAttribute_T
    self.drawConnections(
(self.obj307,self.obj267,[777.5, 567.5, 774.0, 454.0],"true", 2) )
    # Connections for obj308 (graphObject_: Obj197) of type hasAttribute_T
    self.drawConnections(
(self.obj308,self.obj268,[584.5, 703.0, 563.0, 745.0],"true", 2) )
    # Connections for obj309 (graphObject_: Obj198) of type hasAttribute_T
    self.drawConnections(
(self.obj309,self.obj269,[243.0, 562.5, 154.0, 594.0],"true", 2) )
    # Connections for obj310 (graphObject_: Obj199) of type leftExpr
    self.drawConnections(
(self.obj310,self.obj264,[358.0, 403.5, 354.0, 434.0],"true", 2) )
    # Connections for obj311 (graphObject_: Obj200) of type leftExpr
    self.drawConnections(
(self.obj311,self.obj265,[1100.0, 630.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj312 (graphObject_: Obj201) of type leftExpr
    self.drawConnections(
(self.obj312,self.obj266,[1023.5, 709.5, 934.0, 680.0],"true", 2) )
    # Connections for obj313 (graphObject_: Obj202) of type leftExpr
    self.drawConnections(
(self.obj313,self.obj267,[793.0, 464.0, 774.0, 454.0],"true", 2) )
    # Connections for obj314 (graphObject_: Obj203) of type leftExpr
    self.drawConnections(
(self.obj314,self.obj268,[482.5, 754.0, 563.0, 745.0],"true", 2) )
    # Connections for obj315 (graphObject_: Obj204) of type leftExpr
    self.drawConnections(
(self.obj315,self.obj269,[236.0, 606.5, 154.0, 594.0],"true", 2) )
    # Connections for obj316 (graphObject_: Obj205) of type rightExpr
    self.drawConnections(
(self.obj316,self.obj276,[447.0, 363.5, 530.0, 361.0],"true", 2) )
    # Connections for obj317 (graphObject_: Obj206) of type rightExpr
    self.drawConnections(
(self.obj317,self.obj279,[1279.5, 683.5, 1274.0, 708.0],"true", 2) )
    # Connections for obj318 (graphObject_: Obj207) of type rightExpr
    self.drawConnections(
(self.obj318,self.obj280,[1023.5, 753.5, 934.0, 757.0],"true", 2) )
    # Connections for obj319 (graphObject_: Obj208) of type rightExpr
    self.drawConnections(
(self.obj319,self.obj277,[926.0, 449.0, 926.0, 358.0],"true", 2) )
    # Connections for obj320 (graphObject_: Obj209) of type rightExpr
    self.drawConnections(
(self.obj320,self.obj283,[478.0, 791.5, 554.0, 820.0],"true", 2) )
    # Connections for obj321 (graphObject_: Obj210) of type rightExpr
    self.drawConnections(
(self.obj321,self.obj284,[236.5, 646.5, 155.0, 674.0],"true", 2) )
    # Connections for obj322 (graphObject_: Obj211) of type hasArgs
    self.drawConnections(
(self.obj322,self.obj278,[498.5, 323.0, 467.0, 285.0],"true", 2) )
    # Connections for obj323 (graphObject_: Obj212) of type hasArgs
    self.drawConnections(
(self.obj323,self.obj263,[572.0, 293.5, 614.0, 226.0],"true", 2) )
    # Connections for obj324 (graphObject_: Obj213) of type hasArgs
    self.drawConnections(
(self.obj324,self.obj281,[862.0, 336.0, 782.0, 284.0],"true", 2) )
    # Connections for obj325 (graphObject_: Obj214) of type hasArgs
    self.drawConnections(
(self.obj325,self.obj262,[910.0, 298.0, 894.0, 194.0],"true", 2) )
    # Connections for obj326 (graphObject_: Obj215) of type hasArgs
    self.drawConnections(
(self.obj326,self.obj282,[958.0, 353.0, 1070.0, 280.0],"true", 2) )

newfunction = Transition2QInstSIBLING_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
