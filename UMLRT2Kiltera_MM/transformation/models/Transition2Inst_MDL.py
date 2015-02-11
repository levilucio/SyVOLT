"""
__Transition2Inst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 16:41:25 2015
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from EntryPoint import *
from Transition import *
from StateMachine import *
from State import *
from IN1 import *
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
from graph_Transition import *
from graph_paired_with import *
from graph_State import *
from graph_Equation import *
from graph_IN1 import *
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
from graph_EntryPoint import *
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

def Transition2Inst_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2Inst')
    # --- ASG attributes over ---


    self.obj335=MatchModel(self)
    self.obj335.isGraphObjectVisual = True

    if(hasattr(self.obj335, '_setHierarchicalLink')):
      self.obj335._setHierarchicalLink(False)

    self.obj335.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj335)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj335.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj335)
    self.globalAndLocalPostcondition(self.obj335, rootNode)
    self.obj335.postAction( rootNode.CREATE )

    self.obj336=ApplyModel(self)
    self.obj336.isGraphObjectVisual = True

    if(hasattr(self.obj336, '_setHierarchicalLink')):
      self.obj336._setHierarchicalLink(False)

    self.obj336.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,380.0,self.obj336)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj336.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj336)
    self.globalAndLocalPostcondition(self.obj336, rootNode)
    self.obj336.postAction( rootNode.CREATE )

    self.obj337=EntryPoint(self)
    self.obj337.isGraphObjectVisual = True

    if(hasattr(self.obj337, '_setHierarchicalLink')):
      self.obj337._setHierarchicalLink(False)

    # name
    self.obj337.name.setValue('entrypoint1')

    # classtype
    self.obj337.classtype.setValue('EntryPoint')

    # cardinality
    self.obj337.cardinality.setValue('1')

    self.obj337.graphClass_= graph_EntryPoint
    if self.genGraphics:
       new_obj = graph_EntryPoint(780.0,40.0,self.obj337)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("EntryPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj337.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj337)
    self.globalAndLocalPostcondition(self.obj337, rootNode)
    self.obj337.postAction( rootNode.CREATE )

    self.obj338=Transition(self)
    self.obj338.isGraphObjectVisual = True

    if(hasattr(self.obj338, '_setHierarchicalLink')):
      self.obj338._setHierarchicalLink(False)

    # name
    self.obj338.name.setValue('transition1')

    # classtype
    self.obj338.classtype.setValue('Transition')

    # cardinality
    self.obj338.cardinality.setValue('+')

    self.obj338.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,40.0,self.obj338)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj338.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj338)
    self.globalAndLocalPostcondition(self.obj338, rootNode)
    self.obj338.postAction( rootNode.CREATE )

    self.obj339=StateMachine(self)
    self.obj339.isGraphObjectVisual = True

    if(hasattr(self.obj339, '_setHierarchicalLink')):
      self.obj339._setHierarchicalLink(False)

    # name
    self.obj339.name.setValue('statemachine1')

    # classtype
    self.obj339.classtype.setValue('StateMachine')

    # cardinality
    self.obj339.cardinality.setValue('1')

    self.obj339.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(620.0,140.0,self.obj339)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj339.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj339)
    self.globalAndLocalPostcondition(self.obj339, rootNode)
    self.obj339.postAction( rootNode.CREATE )

    self.obj340=State(self)
    self.obj340.isGraphObjectVisual = True

    if(hasattr(self.obj340, '_setHierarchicalLink')):
      self.obj340._setHierarchicalLink(False)

    # name
    self.obj340.name.setValue('state1')

    # classtype
    self.obj340.classtype.setValue('State')

    # cardinality
    self.obj340.cardinality.setValue('+')

    self.obj340.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj340)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj340.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj340)
    self.globalAndLocalPostcondition(self.obj340, rootNode)
    self.obj340.postAction( rootNode.CREATE )

    self.obj341=IN1(self)
    self.obj341.isGraphObjectVisual = True

    if(hasattr(self.obj341, '_setHierarchicalLink')):
      self.obj341._setHierarchicalLink(False)

    # classtype
    self.obj341.classtype.setValue('IN1')

    # cardinality
    self.obj341.cardinality.setValue('1')

    # name
    self.obj341.name.setValue('in1_1')

    self.obj341.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(440.0,140.0,self.obj341)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj341.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj341)
    self.globalAndLocalPostcondition(self.obj341, rootNode)
    self.obj341.postAction( rootNode.CREATE )

    self.obj342=Name(self)
    self.obj342.isGraphObjectVisual = True

    if(hasattr(self.obj342, '_setHierarchicalLink')):
      self.obj342._setHierarchicalLink(False)

    # classtype
    self.obj342.classtype.setValue('Name')

    # cardinality
    self.obj342.cardinality.setValue('1')

    # name
    self.obj342.name.setValue('name1')

    self.obj342.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,280.0,self.obj342)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj342.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj342)
    self.globalAndLocalPostcondition(self.obj342, rootNode)
    self.obj342.postAction( rootNode.CREATE )

    self.obj343=Name(self)
    self.obj343.isGraphObjectVisual = True

    if(hasattr(self.obj343, '_setHierarchicalLink')):
      self.obj343._setHierarchicalLink(False)

    # classtype
    self.obj343.classtype.setValue('Name')

    # cardinality
    self.obj343.cardinality.setValue('1')

    # name
    self.obj343.name.setValue('name2')

    self.obj343.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,380.0,self.obj343)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj343.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj343)
    self.globalAndLocalPostcondition(self.obj343, rootNode)
    self.obj343.postAction( rootNode.CREATE )

    self.obj344=Name(self)
    self.obj344.isGraphObjectVisual = True

    if(hasattr(self.obj344, '_setHierarchicalLink')):
      self.obj344._setHierarchicalLink(False)

    # classtype
    self.obj344.classtype.setValue('Name')

    # cardinality
    self.obj344.cardinality.setValue('1')

    # name
    self.obj344.name.setValue('name3')

    self.obj344.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1020.0,520.0,self.obj344)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj344.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj344)
    self.globalAndLocalPostcondition(self.obj344, rootNode)
    self.obj344.postAction( rootNode.CREATE )

    self.obj345=Name(self)
    self.obj345.isGraphObjectVisual = True

    if(hasattr(self.obj345, '_setHierarchicalLink')):
      self.obj345._setHierarchicalLink(False)

    # classtype
    self.obj345.classtype.setValue('Name')

    # cardinality
    self.obj345.cardinality.setValue('1')

    # name
    self.obj345.name.setValue('name4')

    self.obj345.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(580.0,540.0,self.obj345)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj345.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj345)
    self.globalAndLocalPostcondition(self.obj345, rootNode)
    self.obj345.postAction( rootNode.CREATE )

    self.obj346=Inst(self)
    self.obj346.isGraphObjectVisual = True

    if(hasattr(self.obj346, '_setHierarchicalLink')):
      self.obj346._setHierarchicalLink(False)

    # classtype
    self.obj346.classtype.setValue('Inst')

    # cardinality
    self.obj346.cardinality.setValue('1')

    # name
    self.obj346.name.setValue('inst1')

    self.obj346.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(220.0,420.0,self.obj346)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj346.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj346)
    self.globalAndLocalPostcondition(self.obj346, rootNode)
    self.obj346.postAction( rootNode.CREATE )

    self.obj347=Attribute(self)
    self.obj347.isGraphObjectVisual = True

    if(hasattr(self.obj347, '_setHierarchicalLink')):
      self.obj347._setHierarchicalLink(False)

    # Type
    self.obj347.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj347.Type.config = 0

    # name
    self.obj347.name.setValue('name')

    self.obj347.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,220.0,self.obj347)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj347.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj347)
    self.globalAndLocalPostcondition(self.obj347, rootNode)
    self.obj347.postAction( rootNode.CREATE )

    self.obj348=Attribute(self)
    self.obj348.isGraphObjectVisual = True

    if(hasattr(self.obj348, '_setHierarchicalLink')):
      self.obj348._setHierarchicalLink(False)

    # Type
    self.obj348.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj348.Type.config = 0

    # name
    self.obj348.name.setValue('name')

    self.obj348.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(540.0,240.0,self.obj348)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj348.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj348)
    self.globalAndLocalPostcondition(self.obj348, rootNode)
    self.obj348.postAction( rootNode.CREATE )

    self.obj349=Attribute(self)
    self.obj349.isGraphObjectVisual = True

    if(hasattr(self.obj349, '_setHierarchicalLink')):
      self.obj349._setHierarchicalLink(False)

    # Type
    self.obj349.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj349.Type.config = 0

    # name
    self.obj349.name.setValue('isComposite')

    self.obj349.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(151.0,140.0,self.obj349)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj349.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj349)
    self.globalAndLocalPostcondition(self.obj349, rootNode)
    self.obj349.postAction( rootNode.CREATE )

    self.obj350=Attribute(self)
    self.obj350.isGraphObjectVisual = True

    if(hasattr(self.obj350, '_setHierarchicalLink')):
      self.obj350._setHierarchicalLink(False)

    # Type
    self.obj350.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj350.Type.config = 0

    # name
    self.obj350.name.setValue('literal')

    self.obj350.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,300.0,self.obj350)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj350.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj350)
    self.globalAndLocalPostcondition(self.obj350, rootNode)
    self.obj350.postAction( rootNode.CREATE )

    self.obj351=Attribute(self)
    self.obj351.isGraphObjectVisual = True

    if(hasattr(self.obj351, '_setHierarchicalLink')):
      self.obj351._setHierarchicalLink(False)

    # Type
    self.obj351.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj351.Type.config = 0

    # name
    self.obj351.name.setValue('literal')

    self.obj351.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,380.0,self.obj351)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj351.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj351)
    self.globalAndLocalPostcondition(self.obj351, rootNode)
    self.obj351.postAction( rootNode.CREATE )

    self.obj352=Attribute(self)
    self.obj352.isGraphObjectVisual = True

    if(hasattr(self.obj352, '_setHierarchicalLink')):
      self.obj352._setHierarchicalLink(False)

    # Type
    self.obj352.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj352.Type.config = 0

    # name
    self.obj352.name.setValue('literal')

    self.obj352.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1020.0,440.0,self.obj352)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj352.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj352)
    self.globalAndLocalPostcondition(self.obj352, rootNode)
    self.obj352.postAction( rootNode.CREATE )

    self.obj353=Attribute(self)
    self.obj353.isGraphObjectVisual = True

    if(hasattr(self.obj353, '_setHierarchicalLink')):
      self.obj353._setHierarchicalLink(False)

    # Type
    self.obj353.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj353.Type.config = 0

    # name
    self.obj353.name.setValue('literal')

    self.obj353.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,560.0,self.obj353)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj353.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj353)
    self.globalAndLocalPostcondition(self.obj353, rootNode)
    self.obj353.postAction( rootNode.CREATE )

    self.obj354=Attribute(self)
    self.obj354.isGraphObjectVisual = True

    if(hasattr(self.obj354, '_setHierarchicalLink')):
      self.obj354._setHierarchicalLink(False)

    # Type
    self.obj354.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj354.Type.config = 0

    # name
    self.obj354.name.setValue('name')

    self.obj354.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,340.0,self.obj354)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj354.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj354)
    self.globalAndLocalPostcondition(self.obj354, rootNode)
    self.obj354.postAction( rootNode.CREATE )

    self.obj355=Attribute(self)
    self.obj355.isGraphObjectVisual = True

    if(hasattr(self.obj355, '_setHierarchicalLink')):
      self.obj355._setHierarchicalLink(False)

    # Type
    self.obj355.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj355.Type.config = 0

    # name
    self.obj355.name.setValue('pivot')

    self.obj355.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,580.0,self.obj355)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj355.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj355)
    self.globalAndLocalPostcondition(self.obj355, rootNode)
    self.obj355.postAction( rootNode.CREATE )

    self.obj356=Equation(self)
    self.obj356.isGraphObjectVisual = True

    if(hasattr(self.obj356, '_setHierarchicalLink')):
      self.obj356._setHierarchicalLink(False)

    # name
    self.obj356.name.setValue('eq1')

    self.obj356.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(295.0,140.0,self.obj356)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj356.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj356)
    self.globalAndLocalPostcondition(self.obj356, rootNode)
    self.obj356.postAction( rootNode.CREATE )

    self.obj357=Equation(self)
    self.obj357.isGraphObjectVisual = True

    if(hasattr(self.obj357, '_setHierarchicalLink')):
      self.obj357._setHierarchicalLink(False)

    # name
    self.obj357.name.setValue('eq2')

    self.obj357.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,220.0,self.obj357)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj357.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj357)
    self.globalAndLocalPostcondition(self.obj357, rootNode)
    self.obj357.postAction( rootNode.CREATE )

    self.obj358=Equation(self)
    self.obj358.isGraphObjectVisual = True

    if(hasattr(self.obj358, '_setHierarchicalLink')):
      self.obj358._setHierarchicalLink(False)

    # name
    self.obj358.name.setValue('eq3')

    self.obj358.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,460.0,self.obj358)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj358.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj358)
    self.globalAndLocalPostcondition(self.obj358, rootNode)
    self.obj358.postAction( rootNode.CREATE )

    self.obj359=Equation(self)
    self.obj359.isGraphObjectVisual = True

    if(hasattr(self.obj359, '_setHierarchicalLink')):
      self.obj359._setHierarchicalLink(False)

    # name
    self.obj359.name.setValue('eq4')

    self.obj359.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(874.0,449.0,self.obj359)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj359.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj359)
    self.globalAndLocalPostcondition(self.obj359, rootNode)
    self.obj359.postAction( rootNode.CREATE )

    self.obj360=Equation(self)
    self.obj360.isGraphObjectVisual = True

    if(hasattr(self.obj360, '_setHierarchicalLink')):
      self.obj360._setHierarchicalLink(False)

    # name
    self.obj360.name.setValue('eq5')

    self.obj360.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(740.0,640.0,self.obj360)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj360.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj360)
    self.globalAndLocalPostcondition(self.obj360, rootNode)
    self.obj360.postAction( rootNode.CREATE )

    self.obj361=Equation(self)
    self.obj361.isGraphObjectVisual = True

    if(hasattr(self.obj361, '_setHierarchicalLink')):
      self.obj361._setHierarchicalLink(False)

    # name
    self.obj361.name.setValue('eq6')

    self.obj361.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,340.0,self.obj361)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj361.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj361)
    self.globalAndLocalPostcondition(self.obj361, rootNode)
    self.obj361.postAction( rootNode.CREATE )

    self.obj362=Equation(self)
    self.obj362.isGraphObjectVisual = True

    if(hasattr(self.obj362, '_setHierarchicalLink')):
      self.obj362._setHierarchicalLink(False)

    # name
    self.obj362.name.setValue('eq7')

    self.obj362.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,660.0,self.obj362)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj362.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj362)
    self.globalAndLocalPostcondition(self.obj362, rootNode)
    self.obj362.postAction( rootNode.CREATE )

    self.obj363=Concat(self)
    self.obj363.isGraphObjectVisual = True

    if(hasattr(self.obj363, '_setHierarchicalLink')):
      self.obj363._setHierarchicalLink(False)

    # Type
    self.obj363.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj363.Type.config = 0

    # name
    self.obj363.name.setValue('concat1')

    self.obj363.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(940.0,355.0,self.obj363)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj363.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj363)
    self.globalAndLocalPostcondition(self.obj363, rootNode)
    self.obj363.postAction( rootNode.CREATE )

    self.obj364=Concat(self)
    self.obj364.isGraphObjectVisual = True

    if(hasattr(self.obj364, '_setHierarchicalLink')):
      self.obj364._setHierarchicalLink(False)

    # Type
    self.obj364.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj364.Type.config = 0

    # name
    self.obj364.name.setValue('concat2')

    self.obj364.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,340.0,self.obj364)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj364.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj364)
    self.globalAndLocalPostcondition(self.obj364, rootNode)
    self.obj364.postAction( rootNode.CREATE )

    self.obj365=Constant(self)
    self.obj365.isGraphObjectVisual = True

    if(hasattr(self.obj365, '_setHierarchicalLink')):
      self.obj365._setHierarchicalLink(False)

    # Type
    self.obj365.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj365.Type.config = 0

    # name
    self.obj365.name.setValue('true')

    self.obj365.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,220.0,self.obj365)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj365.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj365)
    self.globalAndLocalPostcondition(self.obj365, rootNode)
    self.obj365.postAction( rootNode.CREATE )

    self.obj366=Constant(self)
    self.obj366.isGraphObjectVisual = True

    if(hasattr(self.obj366, '_setHierarchicalLink')):
      self.obj366._setHierarchicalLink(False)

    # Type
    self.obj366.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj366.Type.config = 0

    # name
    self.obj366.name.setValue('exit_in')

    self.obj366.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1200.0,207.0,self.obj366)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj366.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj366)
    self.globalAndLocalPostcondition(self.obj366, rootNode)
    self.obj366.postAction( rootNode.CREATE )

    self.obj367=Constant(self)
    self.obj367.isGraphObjectVisual = True

    if(hasattr(self.obj367, '_setHierarchicalLink')):
      self.obj367._setHierarchicalLink(False)

    # Type
    self.obj367.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj367.Type.config = 0

    # name
    self.obj367.name.setValue('exack_in')

    self.obj367.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1220.0,480.0,self.obj367)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj367.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj367)
    self.globalAndLocalPostcondition(self.obj367, rootNode)
    self.obj367.postAction( rootNode.CREATE )

    self.obj368=Constant(self)
    self.obj368.isGraphObjectVisual = True

    if(hasattr(self.obj368, '_setHierarchicalLink')):
      self.obj368._setHierarchicalLink(False)

    # Type
    self.obj368.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj368.Type.config = 0

    # name
    self.obj368.name.setValue('xox')

    self.obj368.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1000.0,200.0,self.obj368)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj368.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj368)
    self.globalAndLocalPostcondition(self.obj368, rootNode)
    self.obj368.postAction( rootNode.CREATE )

    self.obj369=Constant(self)
    self.obj369.isGraphObjectVisual = True

    if(hasattr(self.obj369, '_setHierarchicalLink')):
      self.obj369._setHierarchicalLink(False)

    # Type
    self.obj369.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj369.Type.config = 0

    # name
    self.obj369.name.setValue('xox')

    self.obj369.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(720.0,280.0,self.obj369)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj369.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj369)
    self.globalAndLocalPostcondition(self.obj369, rootNode)
    self.obj369.postAction( rootNode.CREATE )

    self.obj370=Constant(self)
    self.obj370.isGraphObjectVisual = True

    if(hasattr(self.obj370, '_setHierarchicalLink')):
      self.obj370._setHierarchicalLink(False)

    # Type
    self.obj370.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj370.Type.config = 0

    # name
    self.obj370.name.setValue('sh_in')

    self.obj370.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(580.0,640.0,self.obj370)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj370.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj370)
    self.globalAndLocalPostcondition(self.obj370, rootNode)
    self.obj370.postAction( rootNode.CREATE )

    self.obj371=Constant(self)
    self.obj371.isGraphObjectVisual = True

    if(hasattr(self.obj371, '_setHierarchicalLink')):
      self.obj371._setHierarchicalLink(False)

    # Type
    self.obj371.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj371.Type.config = 0

    # name
    self.obj371.name.setValue('S')

    self.obj371.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(380.0,260.0,self.obj371)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj371.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj371)
    self.globalAndLocalPostcondition(self.obj371, rootNode)
    self.obj371.postAction( rootNode.CREATE )

    self.obj372=Constant(self)
    self.obj372.isGraphObjectVisual = True

    if(hasattr(self.obj372, '_setHierarchicalLink')):
      self.obj372._setHierarchicalLink(False)

    # Type
    self.obj372.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj372.Type.config = 0

    # name
    self.obj372.name.setValue('instForInTrans')

    self.obj372.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(351.0,580.0,self.obj372)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj372.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj372)
    self.globalAndLocalPostcondition(self.obj372, rootNode)
    self.obj372.postAction( rootNode.CREATE )

    self.obj373=paired_with(self)
    self.obj373.isGraphObjectVisual = True

    if(hasattr(self.obj373, '_setHierarchicalLink')):
      self.obj373._setHierarchicalLink(False)

    self.obj373.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,232.0,self.obj373)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj373.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj373)
    self.globalAndLocalPostcondition(self.obj373, rootNode)
    self.obj373.postAction( rootNode.CREATE )

    self.obj374=match_contains(self)
    self.obj374.isGraphObjectVisual = True

    if(hasattr(self.obj374, '_setHierarchicalLink')):
      self.obj374._setHierarchicalLink(False)

    self.obj374.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(341.0,33.0,self.obj374)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj374.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj374)
    self.globalAndLocalPostcondition(self.obj374, rootNode)
    self.obj374.postAction( rootNode.CREATE )

    self.obj375=match_contains(self)
    self.obj375.isGraphObjectVisual = True

    if(hasattr(self.obj375, '_setHierarchicalLink')):
      self.obj375._setHierarchicalLink(False)

    self.obj375.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(370.0,21.0,self.obj375)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj375.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj375)
    self.globalAndLocalPostcondition(self.obj375, rootNode)
    self.obj375.postAction( rootNode.CREATE )

    self.obj376=match_contains(self)
    self.obj376.isGraphObjectVisual = True

    if(hasattr(self.obj376, '_setHierarchicalLink')):
      self.obj376._setHierarchicalLink(False)

    self.obj376.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(368.0,10.0,self.obj376)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj376.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj376)
    self.globalAndLocalPostcondition(self.obj376, rootNode)
    self.obj376.postAction( rootNode.CREATE )

    self.obj377=match_contains(self)
    self.obj377.isGraphObjectVisual = True

    if(hasattr(self.obj377, '_setHierarchicalLink')):
      self.obj377._setHierarchicalLink(False)

    self.obj377.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(531.0,8.0,self.obj377)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj377.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj377)
    self.globalAndLocalPostcondition(self.obj377, rootNode)
    self.obj377.postAction( rootNode.CREATE )

    self.obj378=match_contains(self)
    self.obj378.isGraphObjectVisual = True

    if(hasattr(self.obj378, '_setHierarchicalLink')):
      self.obj378._setHierarchicalLink(False)

    self.obj378.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(374.0,117.0,self.obj378)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj378.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj378)
    self.globalAndLocalPostcondition(self.obj378, rootNode)
    self.obj378.postAction( rootNode.CREATE )

    self.obj379=apply_contains(self)
    self.obj379.isGraphObjectVisual = True

    if(hasattr(self.obj379, '_setHierarchicalLink')):
      self.obj379._setHierarchicalLink(False)

    self.obj379.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(267.5,442.0,self.obj379)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj379.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj379)
    self.globalAndLocalPostcondition(self.obj379, rootNode)
    self.obj379.postAction( rootNode.CREATE )

    self.obj380=apply_contains(self)
    self.obj380.isGraphObjectVisual = True

    if(hasattr(self.obj380, '_setHierarchicalLink')):
      self.obj380._setHierarchicalLink(False)

    self.obj380.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(206.5,532.0,self.obj380)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj380.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj380)
    self.globalAndLocalPostcondition(self.obj380, rootNode)
    self.obj380.postAction( rootNode.CREATE )

    self.obj381=apply_contains(self)
    self.obj381.isGraphObjectVisual = True

    if(hasattr(self.obj381, '_setHierarchicalLink')):
      self.obj381._setHierarchicalLink(False)

    self.obj381.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(667.5,492.0,self.obj381)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj381.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj381)
    self.globalAndLocalPostcondition(self.obj381, rootNode)
    self.obj381.postAction( rootNode.CREATE )

    self.obj382=apply_contains(self)
    self.obj382.isGraphObjectVisual = True

    if(hasattr(self.obj382, '_setHierarchicalLink')):
      self.obj382._setHierarchicalLink(False)

    self.obj382.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,422.0,self.obj382)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj382.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj382)
    self.globalAndLocalPostcondition(self.obj382, rootNode)
    self.obj382.postAction( rootNode.CREATE )

    self.obj383=apply_contains(self)
    self.obj383.isGraphObjectVisual = True

    if(hasattr(self.obj383, '_setHierarchicalLink')):
      self.obj383._setHierarchicalLink(False)

    self.obj383.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,372.0,self.obj383)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj383.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj383)
    self.globalAndLocalPostcondition(self.obj383, rootNode)
    self.obj383.postAction( rootNode.CREATE )

    self.obj384=directLink_T(self)
    self.obj384.isGraphObjectVisual = True

    if(hasattr(self.obj384, '_setHierarchicalLink')):
      self.obj384._setHierarchicalLink(False)

    # associationType
    self.obj384.associationType.setValue('channelNames')

    self.obj384.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1026.0,326.0,self.obj384)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj384.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj384)
    self.globalAndLocalPostcondition(self.obj384, rootNode)
    self.obj384.postAction( rootNode.CREATE )

    self.obj385=directLink_T(self)
    self.obj385.isGraphObjectVisual = True

    if(hasattr(self.obj385, '_setHierarchicalLink')):
      self.obj385._setHierarchicalLink(False)

    # associationType
    self.obj385.associationType.setValue('channelNames')

    self.obj385.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1013.0,431.0,self.obj385)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj385.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj385)
    self.globalAndLocalPostcondition(self.obj385, rootNode)
    self.obj385.postAction( rootNode.CREATE )

    self.obj386=directLink_T(self)
    self.obj386.isGraphObjectVisual = True

    if(hasattr(self.obj386, '_setHierarchicalLink')):
      self.obj386._setHierarchicalLink(False)

    # associationType
    self.obj386.associationType.setValue('channelNames')

    self.obj386.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(792.0,521.0,self.obj386)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj386.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj386)
    self.globalAndLocalPostcondition(self.obj386, rootNode)
    self.obj386.postAction( rootNode.CREATE )

    self.obj387=directLink_T(self)
    self.obj387.isGraphObjectVisual = True

    if(hasattr(self.obj387, '_setHierarchicalLink')):
      self.obj387._setHierarchicalLink(False)

    # associationType
    self.obj387.associationType.setValue('channelNames')

    self.obj387.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(572.0,531.0,self.obj387)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj387.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj387)
    self.globalAndLocalPostcondition(self.obj387, rootNode)
    self.obj387.postAction( rootNode.CREATE )

    self.obj388=directLink_S(self)
    self.obj388.isGraphObjectVisual = True

    if(hasattr(self.obj388, '_setHierarchicalLink')):
      self.obj388._setHierarchicalLink(False)

    # associationType
    self.obj388.associationType.setValue('transitions')

    self.obj388.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,83.0,self.obj388)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj388.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj388)
    self.globalAndLocalPostcondition(self.obj388, rootNode)
    self.obj388.postAction( rootNode.CREATE )

    self.obj389=directLink_S(self)
    self.obj389.isGraphObjectVisual = True

    if(hasattr(self.obj389, '_setHierarchicalLink')):
      self.obj389._setHierarchicalLink(False)

    # associationType
    self.obj389.associationType.setValue('dest')

    self.obj389.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(760.0,83.0,self.obj389)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj389.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj389)
    self.globalAndLocalPostcondition(self.obj389, rootNode)
    self.obj389.postAction( rootNode.CREATE )

    self.obj390=directLink_S(self)
    self.obj390.isGraphObjectVisual = True

    if(hasattr(self.obj390, '_setHierarchicalLink')):
      self.obj390._setHierarchicalLink(False)

    # associationType
    self.obj390.associationType.setValue('type')

    self.obj390.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(597.0,124.0,self.obj390)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj390.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj390)
    self.globalAndLocalPostcondition(self.obj390, rootNode)
    self.obj390.postAction( rootNode.CREATE )

    self.obj391=directLink_S(self)
    self.obj391.isGraphObjectVisual = True

    if(hasattr(self.obj391, '_setHierarchicalLink')):
      self.obj391._setHierarchicalLink(False)

    # associationType
    self.obj391.associationType.setValue('owningStateMachine')

    self.obj391.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(850.5,133.0,self.obj391)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj391.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj391)
    self.globalAndLocalPostcondition(self.obj391, rootNode)
    self.obj391.postAction( rootNode.CREATE )

    self.obj392=hasAttribute_S(self)
    self.obj392.isGraphObjectVisual = True

    if(hasattr(self.obj392, '_setHierarchicalLink')):
      self.obj392._setHierarchicalLink(False)

    self.obj392.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(674.5,241.5,self.obj392)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj392.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj392)
    self.globalAndLocalPostcondition(self.obj392, rootNode)
    self.obj392.postAction( rootNode.CREATE )

    self.obj393=hasAttribute_S(self)
    self.obj393.isGraphObjectVisual = True

    if(hasattr(self.obj393, '_setHierarchicalLink')):
      self.obj393._setHierarchicalLink(False)

    self.obj393.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(912.0,206.5,self.obj393)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj393.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj393)
    self.globalAndLocalPostcondition(self.obj393, rootNode)
    self.obj393.postAction( rootNode.CREATE )

    self.obj394=hasAttribute_S(self)
    self.obj394.isGraphObjectVisual = True

    if(hasattr(self.obj394, '_setHierarchicalLink')):
      self.obj394._setHierarchicalLink(False)

    self.obj394.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(317.5,128.5,self.obj394)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj394.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj394)
    self.globalAndLocalPostcondition(self.obj394, rootNode)
    self.obj394.postAction( rootNode.CREATE )

    self.obj395=hasAttribute_T(self)
    self.obj395.isGraphObjectVisual = True

    if(hasattr(self.obj395, '_setHierarchicalLink')):
      self.obj395._setHierarchicalLink(False)

    self.obj395.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,330.5,self.obj395)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj395.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj395)
    self.globalAndLocalPostcondition(self.obj395, rootNode)
    self.obj395.postAction( rootNode.CREATE )

    self.obj396=hasAttribute_T(self)
    self.obj396.isGraphObjectVisual = True

    if(hasattr(self.obj396, '_setHierarchicalLink')):
      self.obj396._setHierarchicalLink(False)

    self.obj396.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,424.5,self.obj396)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj396.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj396)
    self.globalAndLocalPostcondition(self.obj396, rootNode)
    self.obj396.postAction( rootNode.CREATE )

    self.obj397=hasAttribute_T(self)
    self.obj397.isGraphObjectVisual = True

    if(hasattr(self.obj397, '_setHierarchicalLink')):
      self.obj397._setHierarchicalLink(False)

    self.obj397.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1201.0,519.0,self.obj397)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj397.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj397)
    self.globalAndLocalPostcondition(self.obj397, rootNode)
    self.obj397.postAction( rootNode.CREATE )

    self.obj398=hasAttribute_T(self)
    self.obj398.isGraphObjectVisual = True

    if(hasattr(self.obj398, '_setHierarchicalLink')):
      self.obj398._setHierarchicalLink(False)

    self.obj398.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(833.0,592.5,self.obj398)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj398.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj398)
    self.globalAndLocalPostcondition(self.obj398, rootNode)
    self.obj398.postAction( rootNode.CREATE )

    self.obj399=hasAttribute_T(self)
    self.obj399.isGraphObjectVisual = True

    if(hasattr(self.obj399, '_setHierarchicalLink')):
      self.obj399._setHierarchicalLink(False)

    self.obj399.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,422.5,self.obj399)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj399.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj399)
    self.globalAndLocalPostcondition(self.obj399, rootNode)
    self.obj399.postAction( rootNode.CREATE )

    self.obj400=hasAttribute_T(self)
    self.obj400.isGraphObjectVisual = True

    if(hasattr(self.obj400, '_setHierarchicalLink')):
      self.obj400._setHierarchicalLink(False)

    self.obj400.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,542.5,self.obj400)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj400.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj400)
    self.globalAndLocalPostcondition(self.obj400, rootNode)
    self.obj400.postAction( rootNode.CREATE )

    self.obj401=leftExpr(self)
    self.obj401.isGraphObjectVisual = True

    if(hasattr(self.obj401, '_setHierarchicalLink')):
      self.obj401._setHierarchicalLink(False)

    self.obj401.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,176.5,self.obj401)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj401.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj401)
    self.globalAndLocalPostcondition(self.obj401, rootNode)
    self.obj401.postAction( rootNode.CREATE )

    self.obj402=leftExpr(self)
    self.obj402.isGraphObjectVisual = True

    if(hasattr(self.obj402, '_setHierarchicalLink')):
      self.obj402._setHierarchicalLink(False)

    self.obj402.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1487.0,309.5,self.obj402)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj402.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj402)
    self.globalAndLocalPostcondition(self.obj402, rootNode)
    self.obj402.postAction( rootNode.CREATE )

    self.obj403=leftExpr(self)
    self.obj403.isGraphObjectVisual = True

    if(hasattr(self.obj403, '_setHierarchicalLink')):
      self.obj403._setHierarchicalLink(False)

    self.obj403.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1492.0,454.0,self.obj403)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj403.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj403)
    self.globalAndLocalPostcondition(self.obj403, rootNode)
    self.obj403.postAction( rootNode.CREATE )

    self.obj404=leftExpr(self)
    self.obj404.isGraphObjectVisual = True

    if(hasattr(self.obj404, '_setHierarchicalLink')):
      self.obj404._setHierarchicalLink(False)

    self.obj404.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,477.0,self.obj404)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj404.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj404)
    self.globalAndLocalPostcondition(self.obj404, rootNode)
    self.obj404.postAction( rootNode.CREATE )

    self.obj405=leftExpr(self)
    self.obj405.isGraphObjectVisual = True

    if(hasattr(self.obj405, '_setHierarchicalLink')):
      self.obj405._setHierarchicalLink(False)

    self.obj405.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,636.5,self.obj405)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj405.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj405)
    self.globalAndLocalPostcondition(self.obj405, rootNode)
    self.obj405.postAction( rootNode.CREATE )

    self.obj406=leftExpr(self)
    self.obj406.isGraphObjectVisual = True

    if(hasattr(self.obj406, '_setHierarchicalLink')):
      self.obj406._setHierarchicalLink(False)

    self.obj406.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(396.0,356.5,self.obj406)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj406.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj406)
    self.globalAndLocalPostcondition(self.obj406, rootNode)
    self.obj406.postAction( rootNode.CREATE )

    self.obj407=leftExpr(self)
    self.obj407.isGraphObjectVisual = True

    if(hasattr(self.obj407, '_setHierarchicalLink')):
      self.obj407._setHierarchicalLink(False)

    self.obj407.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(346.0,656.5,self.obj407)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj407.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj407)
    self.globalAndLocalPostcondition(self.obj407, rootNode)
    self.obj407.postAction( rootNode.CREATE )

    self.obj408=rightExpr(self)
    self.obj408.isGraphObjectVisual = True

    if(hasattr(self.obj408, '_setHierarchicalLink')):
      self.obj408._setHierarchicalLink(False)

    self.obj408.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(403.5,216.5,self.obj408)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj408.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj408)
    self.globalAndLocalPostcondition(self.obj408, rootNode)
    self.obj408.postAction( rootNode.CREATE )

    self.obj409=rightExpr(self)
    self.obj409.isGraphObjectVisual = True

    if(hasattr(self.obj409, '_setHierarchicalLink')):
      self.obj409._setHierarchicalLink(False)

    self.obj409.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1365.0,243.5,self.obj409)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj409.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj409)
    self.globalAndLocalPostcondition(self.obj409, rootNode)
    self.obj409.postAction( rootNode.CREATE )

    self.obj410=rightExpr(self)
    self.obj410.isGraphObjectVisual = True

    if(hasattr(self.obj410, '_setHierarchicalLink')):
      self.obj410._setHierarchicalLink(False)

    self.obj410.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1424.0,534.0,self.obj410)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj410.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj410)
    self.globalAndLocalPostcondition(self.obj410, rootNode)
    self.obj410.postAction( rootNode.CREATE )

    self.obj411=rightExpr(self)
    self.obj411.isGraphObjectVisual = True

    if(hasattr(self.obj411, '_setHierarchicalLink')):
      self.obj411._setHierarchicalLink(False)

    self.obj411.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1063.0,412.5,self.obj411)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj411.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj411)
    self.globalAndLocalPostcondition(self.obj411, rootNode)
    self.obj411.postAction( rootNode.CREATE )

    self.obj412=rightExpr(self)
    self.obj412.isGraphObjectVisual = True

    if(hasattr(self.obj412, '_setHierarchicalLink')):
      self.obj412._setHierarchicalLink(False)

    self.obj412.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(796.0,676.5,self.obj412)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj412.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj412)
    self.globalAndLocalPostcondition(self.obj412, rootNode)
    self.obj412.postAction( rootNode.CREATE )

    self.obj413=rightExpr(self)
    self.obj413.isGraphObjectVisual = True

    if(hasattr(self.obj413, '_setHierarchicalLink')):
      self.obj413._setHierarchicalLink(False)

    self.obj413.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(556.0,376.5,self.obj413)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj413.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj413)
    self.globalAndLocalPostcondition(self.obj413, rootNode)
    self.obj413.postAction( rootNode.CREATE )

    self.obj414=rightExpr(self)
    self.obj414.isGraphObjectVisual = True

    if(hasattr(self.obj414, '_setHierarchicalLink')):
      self.obj414._setHierarchicalLink(False)

    self.obj414.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(456.0,666.5,self.obj414)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj414.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj414)
    self.globalAndLocalPostcondition(self.obj414, rootNode)
    self.obj414.postAction( rootNode.CREATE )

    self.obj415=hasArgs(self)
    self.obj415.isGraphObjectVisual = True

    if(hasattr(self.obj415, '_setHierarchicalLink')):
      self.obj415._setHierarchicalLink(False)

    self.obj415.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(932.0,344.0,self.obj415)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj415.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj415)
    self.globalAndLocalPostcondition(self.obj415, rootNode)
    self.obj415.postAction( rootNode.CREATE )

    self.obj416=hasArgs(self)
    self.obj416.isGraphObjectVisual = True

    if(hasattr(self.obj416, '_setHierarchicalLink')):
      self.obj416._setHierarchicalLink(False)

    self.obj416.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1029.0,314.0,self.obj416)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj416.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj416)
    self.globalAndLocalPostcondition(self.obj416, rootNode)
    self.obj416.postAction( rootNode.CREATE )

    self.obj417=hasArgs(self)
    self.obj417.isGraphObjectVisual = True

    if(hasattr(self.obj417, '_setHierarchicalLink')):
      self.obj417._setHierarchicalLink(False)

    self.obj417.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1111.0,312.0,self.obj417)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj417.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj417)
    self.globalAndLocalPostcondition(self.obj417, rootNode)
    self.obj417.postAction( rootNode.CREATE )

    self.obj418=hasArgs(self)
    self.obj418.isGraphObjectVisual = True

    if(hasattr(self.obj418, '_setHierarchicalLink')):
      self.obj418._setHierarchicalLink(False)

    self.obj418.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(574.0,334.0,self.obj418)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj418.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj418)
    self.globalAndLocalPostcondition(self.obj418, rootNode)
    self.obj418.postAction( rootNode.CREATE )

    self.obj419=hasArgs(self)
    self.obj419.isGraphObjectVisual = True

    if(hasattr(self.obj419, '_setHierarchicalLink')):
      self.obj419._setHierarchicalLink(False)

    self.obj419.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(644.0,324.0,self.obj419)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj419.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj419)
    self.globalAndLocalPostcondition(self.obj419, rootNode)
    self.obj419.postAction( rootNode.CREATE )

    # Connections for obj335 (graphObject_: Obj216) of type MatchModel
    self.drawConnections(
(self.obj335,self.obj373,[138.0, 51.0, 140.5, 232.0],"true", 2),
(self.obj335,self.obj374,[138.0, 51.0, 341.0, 33.0],"true", 2),
(self.obj335,self.obj375,[138.0, 51.0, 370.0, 21.0],"true", 2),
(self.obj335,self.obj376,[138.0, 51.0, 368.0, 10.0],"true", 2),
(self.obj335,self.obj377,[138.0, 51.0, 531.0, 8.0],"true", 2),
(self.obj335,self.obj378,[138.0, 51.0, 374.0, 117.0],"true", 2) )
    # Connections for obj336 (graphObject_: Obj217) of type ApplyModel
    self.drawConnections(
(self.obj336,self.obj379,[143.0, 413.0, 267.5, 442.0],"true", 2),
(self.obj336,self.obj380,[143.0, 413.0, 206.5, 532.0],"true", 2),
(self.obj336,self.obj381,[143.0, 413.0, 667.5, 492.0],"true", 2),
(self.obj336,self.obj382,[143.0, 413.0, 747.5, 422.0],"true", 2),
(self.obj336,self.obj383,[143.0, 413.0, 747.5, 372.0],"true", 2) )
    # Connections for obj337 (graphObject_: Obj218) named entrypoint1
    self.drawConnections(
(self.obj337,self.obj391,[950.0, 83.0, 850.5, 133.0],"true", 2),
(self.obj337,self.obj393,[950.0, 83.0, 912.0, 206.5],"true", 2) )
    # Connections for obj338 (graphObject_: Obj219) named transition1
    self.drawConnections(
(self.obj338,self.obj389,[570.0, 83.0, 760.0, 83.0],"true", 2),
(self.obj338,self.obj390,[570.0, 83.0, 597.0, 124.0],"true", 2) )
    # Connections for obj339 (graphObject_: Obj220) named statemachine1
    self.drawConnections(
(self.obj339,self.obj392,[790.0, 183.0, 674.5, 241.5],"true", 2) )
    # Connections for obj340 (graphObject_: Obj221) named state1
    self.drawConnections(
(self.obj340,self.obj388,[350.0, 83.0, 460.0, 83.0],"true", 2),
(self.obj340,self.obj394,[350.0, 83.0, 317.5, 128.5],"true", 2) )
    # Connections for obj341 (graphObject_: Obj222) named in1_1
    self.drawConnections(
 )
    # Connections for obj342 (graphObject_: Obj223) named name1
    self.drawConnections(
(self.obj342,self.obj395,[1352.0, 331.0, 1400.0, 330.5],"true", 2) )
    # Connections for obj343 (graphObject_: Obj224) named name2
    self.drawConnections(
(self.obj343,self.obj396,[1352.0, 431.0, 1400.0, 424.5],"true", 2) )
    # Connections for obj344 (graphObject_: Obj225) named name3
    self.drawConnections(
(self.obj344,self.obj397,[1192.0, 571.0, 1201.0, 519.0],"true", 2) )
    # Connections for obj345 (graphObject_: Obj226) named name4
    self.drawConnections(
(self.obj345,self.obj398,[752.0, 591.0, 833.0, 592.5],"true", 2) )
    # Connections for obj346 (graphObject_: Obj227) named inst1
    self.drawConnections(
(self.obj346,self.obj384,[392.0, 471.0, 1026.0, 326.0],"true", 2),
(self.obj346,self.obj385,[392.0, 471.0, 1013.0, 431.0],"true", 2),
(self.obj346,self.obj386,[392.0, 471.0, 792.0, 521.0],"true", 2),
(self.obj346,self.obj387,[392.0, 471.0, 572.0, 531.0],"true", 2),
(self.obj346,self.obj399,[392.0, 471.0, 353.0, 422.5],"true", 2),
(self.obj346,self.obj400,[392.0, 471.0, 353.0, 542.5],"true", 2) )
    # Connections for obj347 (graphObject_: Obj228) named name
    self.drawConnections(
 )
    # Connections for obj348 (graphObject_: Obj229) named name
    self.drawConnections(
 )
    # Connections for obj349 (graphObject_: Obj230) named isComposite
    self.drawConnections(
 )
    # Connections for obj350 (graphObject_: Obj231) named literal
    self.drawConnections(
 )
    # Connections for obj351 (graphObject_: Obj232) named literal
    self.drawConnections(
 )
    # Connections for obj352 (graphObject_: Obj233) named literal
    self.drawConnections(
 )
    # Connections for obj353 (graphObject_: Obj234) named literal
    self.drawConnections(
 )
    # Connections for obj354 (graphObject_: Obj235) named name
    self.drawConnections(
 )
    # Connections for obj355 (graphObject_: Obj236) named pivot
    self.drawConnections(
 )
    # Connections for obj356 (graphObject_: Obj237) named eq1
    self.drawConnections(
(self.obj356,self.obj401,[433.0, 179.0, 359.0, 176.5],"true", 2),
(self.obj356,self.obj408,[433.0, 179.0, 403.5, 216.5],"true", 2) )
    # Connections for obj357 (graphObject_: Obj238) named eq2
    self.drawConnections(
(self.obj357,self.obj402,[1498.0, 259.0, 1487.0, 309.5],"true", 2),
(self.obj357,self.obj409,[1498.0, 259.0, 1365.0, 243.5],"true", 2) )
    # Connections for obj358 (graphObject_: Obj239) named eq3
    self.drawConnections(
(self.obj358,self.obj403,[1498.0, 499.0, 1492.0, 454.0],"true", 2),
(self.obj358,self.obj410,[1498.0, 499.0, 1424.0, 534.0],"true", 2) )
    # Connections for obj359 (graphObject_: Obj240) named eq4
    self.drawConnections(
(self.obj359,self.obj404,[1012.0, 488.0, 1100.0, 477.0],"true", 2),
(self.obj359,self.obj411,[1012.0, 488.0, 1063.0, 412.5],"true", 2) )
    # Connections for obj360 (graphObject_: Obj241) named eq5
    self.drawConnections(
(self.obj360,self.obj405,[878.0, 679.0, 896.0, 636.5],"true", 2),
(self.obj360,self.obj412,[878.0, 679.0, 796.0, 676.5],"true", 2) )
    # Connections for obj361 (graphObject_: Obj242) named eq6
    self.drawConnections(
(self.obj361,self.obj406,[478.0, 379.0, 396.0, 356.5],"true", 2),
(self.obj361,self.obj413,[478.0, 379.0, 556.0, 376.5],"true", 2) )
    # Connections for obj362 (graphObject_: Obj243) named eq7
    self.drawConnections(
(self.obj362,self.obj414,[378.0, 699.0, 456.0, 666.5],"true", 2),
(self.obj362,self.obj407,[378.0, 699.0, 346.0, 656.5],"true", 2) )
    # Connections for obj363 (graphObject_: Obj244) named concat1
    self.drawConnections(
(self.obj363,self.obj415,[1074.0, 389.0, 932.0, 344.0],"true", 2),
(self.obj363,self.obj416,[1074.0, 389.0, 1029.0, 314.0],"true", 2),
(self.obj363,self.obj417,[1074.0, 389.0, 1111.0, 312.0],"true", 2) )
    # Connections for obj364 (graphObject_: Obj245) named concat2
    self.drawConnections(
(self.obj364,self.obj418,[634.0, 374.0, 574.0, 334.0],"true", 2),
(self.obj364,self.obj419,[634.0, 374.0, 644.0, 324.0],"true", 2) )
    # Connections for obj365 (graphObject_: Obj246) named true
    self.drawConnections(
 )
    # Connections for obj366 (graphObject_: Obj247) named exit_in
    self.drawConnections(
 )
    # Connections for obj367 (graphObject_: Obj248) named exack_in
    self.drawConnections(
 )
    # Connections for obj368 (graphObject_: Obj249) named xox
    self.drawConnections(
 )
    # Connections for obj369 (graphObject_: Obj250) named xox
    self.drawConnections(
 )
    # Connections for obj370 (graphObject_: Obj251) named sh_in
    self.drawConnections(
 )
    # Connections for obj371 (graphObject_: Obj252) named S
    self.drawConnections(
 )
    # Connections for obj372 (graphObject_: Obj253) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj373 (graphObject_: Obj254) of type paired_with
    self.drawConnections(
(self.obj373,self.obj336,[140.5, 232.0, 143.0, 413.0],"true", 2) )
    # Connections for obj374 (graphObject_: Obj255) of type match_contains
    self.drawConnections(
(self.obj374,self.obj340,[341.0, 33.0, 350.0, 83.0],"true", 2) )
    # Connections for obj375 (graphObject_: Obj256) of type match_contains
    self.drawConnections(
(self.obj375,self.obj338,[370.0, 21.0, 570.0, 83.0],"true", 2) )
    # Connections for obj376 (graphObject_: Obj257) of type match_contains
    self.drawConnections(
(self.obj376,self.obj337,[368.0, 10.0, 950.0, 83.0],"true", 2) )
    # Connections for obj377 (graphObject_: Obj258) of type match_contains
    self.drawConnections(
(self.obj377,self.obj339,[531.0, 8.0, 790.0, 183.0],"true", 2) )
    # Connections for obj378 (graphObject_: Obj259) of type match_contains
    self.drawConnections(
(self.obj378,self.obj341,[374.0, 117.0, 610.0, 183.0],"true", 2) )
    # Connections for obj379 (graphObject_: Obj260) of type apply_contains
    self.drawConnections(
(self.obj379,self.obj346,[267.5, 442.0, 392.0, 471.0],"true", 2) )
    # Connections for obj380 (graphObject_: Obj261) of type apply_contains
    self.drawConnections(
(self.obj380,self.obj345,[206.5, 532.0, 752.0, 591.0],"true", 2) )
    # Connections for obj381 (graphObject_: Obj262) of type apply_contains
    self.drawConnections(
(self.obj381,self.obj344,[667.5, 492.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj382 (graphObject_: Obj263) of type apply_contains
    self.drawConnections(
(self.obj382,self.obj343,[747.5, 422.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj383 (graphObject_: Obj264) of type apply_contains
    self.drawConnections(
(self.obj383,self.obj342,[747.5, 372.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj384 (graphObject_: Obj265) of type directLink_T
    self.drawConnections(
(self.obj384,self.obj342,[1026.0, 326.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj385 (graphObject_: Obj266) of type directLink_T
    self.drawConnections(
(self.obj385,self.obj343,[1013.0, 431.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj386 (graphObject_: Obj267) of type directLink_T
    self.drawConnections(
(self.obj386,self.obj344,[792.0, 521.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj387 (graphObject_: Obj268) of type directLink_T
    self.drawConnections(
(self.obj387,self.obj345,[572.0, 531.0, 752.0, 591.0],"true", 2) )
    # Connections for obj388 (graphObject_: Obj269) of type directLink_S
    self.drawConnections(
(self.obj388,self.obj338,[460.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj389 (graphObject_: Obj270) of type directLink_S
    self.drawConnections(
(self.obj389,self.obj337,[760.0, 83.0, 950.0, 83.0],"true", 2) )
    # Connections for obj390 (graphObject_: Obj271) of type directLink_S
    self.drawConnections(
(self.obj390,self.obj341,[597.0, 124.0, 610.0, 183.0],"true", 2) )
    # Connections for obj391 (graphObject_: Obj272) of type directLink_S
    self.drawConnections(
(self.obj391,self.obj339,[850.5, 133.0, 790.0, 183.0],"true", 2) )
    # Connections for obj392 (graphObject_: Obj273) of type hasAttribute_S
    self.drawConnections(
(self.obj392,self.obj348,[674.5, 241.5, 674.0, 274.0],"true", 2) )
    # Connections for obj393 (graphObject_: Obj274) of type hasAttribute_S
    self.drawConnections(
(self.obj393,self.obj347,[912.0, 206.5, 994.0, 254.0],"true", 2) )
    # Connections for obj394 (graphObject_: Obj275) of type hasAttribute_S
    self.drawConnections(
(self.obj394,self.obj349,[317.5, 128.5, 285.0, 174.0],"true", 2) )
    # Connections for obj395 (graphObject_: Obj276) of type hasAttribute_T
    self.drawConnections(
(self.obj395,self.obj350,[1400.0, 330.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj396 (graphObject_: Obj277) of type hasAttribute_T
    self.drawConnections(
(self.obj396,self.obj351,[1400.0, 424.5, 1494.0, 414.0],"true", 2) )
    # Connections for obj397 (graphObject_: Obj278) of type hasAttribute_T
    self.drawConnections(
(self.obj397,self.obj352,[1201.0, 519.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj398 (graphObject_: Obj279) of type hasAttribute_T
    self.drawConnections(
(self.obj398,self.obj353,[833.0, 592.5, 914.0, 594.0],"true", 2) )
    # Connections for obj399 (graphObject_: Obj280) of type hasAttribute_T
    self.drawConnections(
(self.obj399,self.obj354,[353.0, 422.5, 314.0, 374.0],"true", 2) )
    # Connections for obj400 (graphObject_: Obj281) of type hasAttribute_T
    self.drawConnections(
(self.obj400,self.obj355,[353.0, 542.5, 314.0, 614.0],"true", 2) )
    # Connections for obj401 (graphObject_: Obj282) of type leftExpr
    self.drawConnections(
(self.obj401,self.obj349,[359.0, 176.5, 285.0, 174.0],"true", 2) )
    # Connections for obj402 (graphObject_: Obj283) of type leftExpr
    self.drawConnections(
(self.obj402,self.obj350,[1487.0, 309.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj403 (graphObject_: Obj284) of type leftExpr
    self.drawConnections(
(self.obj403,self.obj351,[1492.0, 454.0, 1494.0, 414.0],"true", 2) )
    # Connections for obj404 (graphObject_: Obj285) of type leftExpr
    self.drawConnections(
(self.obj404,self.obj352,[1100.0, 477.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj405 (graphObject_: Obj286) of type leftExpr
    self.drawConnections(
(self.obj405,self.obj353,[896.0, 636.5, 914.0, 594.0],"true", 2) )
    # Connections for obj406 (graphObject_: Obj287) of type leftExpr
    self.drawConnections(
(self.obj406,self.obj354,[396.0, 356.5, 314.0, 374.0],"true", 2) )
    # Connections for obj407 (graphObject_: Obj288) of type leftExpr
    self.drawConnections(
(self.obj407,self.obj355,[346.0, 656.5, 314.0, 614.0],"true", 2) )
    # Connections for obj408 (graphObject_: Obj289) of type rightExpr
    self.drawConnections(
(self.obj408,self.obj365,[403.5, 216.5, 374.0, 254.0],"true", 2) )
    # Connections for obj409 (graphObject_: Obj290) of type rightExpr
    self.drawConnections(
(self.obj409,self.obj366,[1365.0, 243.5, 1334.0, 241.0],"true", 2) )
    # Connections for obj410 (graphObject_: Obj291) of type rightExpr
    self.drawConnections(
(self.obj410,self.obj367,[1424.0, 534.0, 1354.0, 514.0],"true", 2) )
    # Connections for obj411 (graphObject_: Obj292) of type rightExpr
    self.drawConnections(
(self.obj411,self.obj363,[1063.0, 412.5, 1074.0, 389.0],"true", 2) )
    # Connections for obj412 (graphObject_: Obj293) of type rightExpr
    self.drawConnections(
(self.obj412,self.obj370,[796.0, 676.5, 714.0, 674.0],"true", 2) )
    # Connections for obj413 (graphObject_: Obj294) of type rightExpr
    self.drawConnections(
(self.obj413,self.obj364,[556.0, 376.5, 634.0, 374.0],"true", 2) )
    # Connections for obj414 (graphObject_: Obj295) of type rightExpr
    self.drawConnections(
(self.obj414,self.obj372,[456.0, 666.5, 485.0, 614.0],"true", 2) )
    # Connections for obj415 (graphObject_: Obj296) of type hasArgs
    self.drawConnections(
(self.obj415,self.obj369,[932.0, 344.0, 854.0, 314.0],"true", 2) )
    # Connections for obj416 (graphObject_: Obj297) of type hasArgs
    self.drawConnections(
(self.obj416,self.obj347,[1029.0, 314.0, 994.0, 254.0],"true", 2) )
    # Connections for obj417 (graphObject_: Obj298) of type hasArgs
    self.drawConnections(
(self.obj417,self.obj368,[1111.0, 312.0, 1134.0, 234.0],"true", 2) )
    # Connections for obj418 (graphObject_: Obj299) of type hasArgs
    self.drawConnections(
(self.obj418,self.obj371,[574.0, 334.0, 514.0, 294.0],"true", 2) )
    # Connections for obj419 (graphObject_: Obj300) of type hasArgs
    self.drawConnections(
(self.obj419,self.obj348,[644.0, 324.0, 674.0, 274.0],"true", 2) )

newfunction = Transition2Inst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
