"""
__Transition2Inst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Feb  9 21:55:55 2015
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
       new_obj = graph_ApplyModel(20.0,380.0,self.obj101)
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

    self.obj102=EntryPoint(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # name
    self.obj102.name.setValue('entrypoint1')

    # classtype
    self.obj102.classtype.setValue('EntryPoint')

    # cardinality
    self.obj102.cardinality.setValue('1')

    self.obj102.graphClass_= graph_EntryPoint
    if self.genGraphics:
       new_obj = graph_EntryPoint(780.0,40.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("EntryPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=Transition(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('transition1')

    # classtype
    self.obj103.classtype.setValue('Transition')

    # cardinality
    self.obj103.cardinality.setValue('+')

    self.obj103.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,40.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=StateMachine(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # name
    self.obj104.name.setValue('statemachine1')

    # classtype
    self.obj104.classtype.setValue('StateMachine')

    # cardinality
    self.obj104.cardinality.setValue('1')

    self.obj104.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(620.0,140.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=State(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # name
    self.obj105.name.setValue('state1')

    # classtype
    self.obj105.classtype.setValue('State')

    # cardinality
    self.obj105.cardinality.setValue('+')

    self.obj105.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=IN1(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # classtype
    self.obj106.classtype.setValue('IN1')

    # cardinality
    self.obj106.cardinality.setValue('1')

    # name
    self.obj106.name.setValue('in1_1')

    self.obj106.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(440.0,140.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=Name(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # classtype
    self.obj107.classtype.setValue('Name')

    # cardinality
    self.obj107.cardinality.setValue('1')

    # name
    self.obj107.name.setValue('name1')

    self.obj107.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,280.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=Name(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # classtype
    self.obj108.classtype.setValue('Name')

    # cardinality
    self.obj108.cardinality.setValue('1')

    # name
    self.obj108.name.setValue('name2')

    self.obj108.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,380.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=Name(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # classtype
    self.obj109.classtype.setValue('Name')

    # cardinality
    self.obj109.cardinality.setValue('1')

    # name
    self.obj109.name.setValue('name3')

    self.obj109.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1020.0,520.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Name(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # classtype
    self.obj110.classtype.setValue('Name')

    # cardinality
    self.obj110.cardinality.setValue('1')

    # name
    self.obj110.name.setValue('name4')

    self.obj110.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(580.0,540.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Inst(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # classtype
    self.obj111.classtype.setValue('Inst')

    # cardinality
    self.obj111.cardinality.setValue('1')

    # name
    self.obj111.name.setValue('inst1')

    self.obj111.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(220.0,420.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=Attribute(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # Type
    self.obj112.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj112.Type.config = 0

    # name
    self.obj112.name.setValue('name')

    self.obj112.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,220.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=Attribute(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # Type
    self.obj113.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj113.Type.config = 0

    # name
    self.obj113.name.setValue('name')

    self.obj113.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(540.0,240.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Attribute(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # Type
    self.obj114.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj114.Type.config = 0

    # name
    self.obj114.name.setValue('isComposite')

    self.obj114.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(151.0,140.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Attribute(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # Type
    self.obj115.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj115.Type.config = 0

    # name
    self.obj115.name.setValue('literal')

    self.obj115.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,300.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=Attribute(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # Type
    self.obj116.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj116.Type.config = 0

    # name
    self.obj116.name.setValue('literal')

    self.obj116.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,380.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=Attribute(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # Type
    self.obj117.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj117.Type.config = 0

    # name
    self.obj117.name.setValue('literal')

    self.obj117.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1020.0,440.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=Attribute(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # Type
    self.obj118.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj118.Type.config = 0

    # name
    self.obj118.name.setValue('literal')

    self.obj118.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,560.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=Attribute(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # Type
    self.obj119.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj119.Type.config = 0

    # name
    self.obj119.name.setValue('name')

    self.obj119.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,340.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=Attribute(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # Type
    self.obj120.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj120.Type.config = 0

    # name
    self.obj120.name.setValue('pivot')

    self.obj120.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,580.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=Equation(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # name
    self.obj121.name.setValue('eq1')

    self.obj121.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(295.0,140.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=Equation(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # name
    self.obj122.name.setValue('eq2')

    self.obj122.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,220.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=Equation(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # name
    self.obj123.name.setValue('eq3')

    self.obj123.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,460.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=Equation(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # name
    self.obj124.name.setValue('eq4')

    self.obj124.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(874.0,449.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=Equation(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # name
    self.obj125.name.setValue('eq5')

    self.obj125.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(740.0,640.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=Equation(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # name
    self.obj126.name.setValue('eq6')

    self.obj126.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,340.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=Equation(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # name
    self.obj127.name.setValue('eq7')

    self.obj127.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,660.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=Concat(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # Type
    self.obj128.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj128.Type.config = 0

    # name
    self.obj128.name.setValue('concat1')

    self.obj128.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(940.0,355.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=Concat(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # Type
    self.obj129.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj129.Type.config = 0

    # name
    self.obj129.name.setValue('concat2')

    self.obj129.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,340.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=Constant(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # Type
    self.obj130.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj130.Type.config = 0

    # name
    self.obj130.name.setValue('true')

    self.obj130.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,220.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=Constant(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # Type
    self.obj131.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj131.Type.config = 0

    # name
    self.obj131.name.setValue('exit_in')

    self.obj131.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1200.0,207.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=Constant(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # Type
    self.obj132.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj132.Type.config = 0

    # name
    self.obj132.name.setValue('exack_in')

    self.obj132.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1220.0,480.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=Constant(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # Type
    self.obj133.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj133.Type.config = 0

    # name
    self.obj133.name.setValue('2')

    self.obj133.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1008.0,200.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=Constant(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # Type
    self.obj134.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj134.Type.config = 0

    # name
    self.obj134.name.setValue('1')

    self.obj134.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(720.0,280.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=Constant(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # Type
    self.obj135.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj135.Type.config = 0

    # name
    self.obj135.name.setValue('sh_in')

    self.obj135.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(580.0,640.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=Constant(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # Type
    self.obj136.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj136.Type.config = 0

    # name
    self.obj136.name.setValue('S')

    self.obj136.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(380.0,260.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=Constant(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # Type
    self.obj137.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj137.Type.config = 0

    # name
    self.obj137.name.setValue('instForInTrans')

    self.obj137.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(351.0,580.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=paired_with(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    self.obj138.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,232.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=match_contains(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    self.obj139.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(341.0,33.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=match_contains(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    self.obj140.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(370.0,21.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=match_contains(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    self.obj141.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(368.0,10.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=match_contains(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(531.0,8.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=match_contains(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    self.obj143.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(374.0,117.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=apply_contains(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    self.obj144.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(267.5,442.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=apply_contains(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    self.obj145.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(206.5,532.0,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=apply_contains(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    self.obj146.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(667.5,492.0,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=apply_contains(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    self.obj147.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,422.0,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=apply_contains(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    self.obj148.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,372.0,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj149=directLink_T(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    # associationType
    self.obj149.associationType.setValue('channelNames')

    self.obj149.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1026.0,326.0,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=directLink_T(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    # associationType
    self.obj150.associationType.setValue('channelNames')

    self.obj150.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1013.0,431.0,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=directLink_T(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    # associationType
    self.obj151.associationType.setValue('channelNames')

    self.obj151.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(792.0,521.0,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=directLink_T(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    # associationType
    self.obj152.associationType.setValue('channelNames')

    self.obj152.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(572.0,531.0,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj153=directLink_S(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    # associationType
    self.obj153.associationType.setValue('transitions')

    self.obj153.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,83.0,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=directLink_S(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # associationType
    self.obj154.associationType.setValue('dest')

    self.obj154.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(760.0,83.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=directLink_S(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    # associationType
    self.obj155.associationType.setValue('type')

    self.obj155.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(597.0,124.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=directLink_S(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # associationType
    self.obj156.associationType.setValue('owningStateMachine')

    self.obj156.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(850.5,133.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=hasAttribute_S(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    self.obj157.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(674.5,241.5,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=hasAttribute_S(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    self.obj158.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(912.0,206.5,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=hasAttribute_S(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    self.obj159.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(317.5,128.5,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=hasAttribute_T(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    self.obj160.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,330.5,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=hasAttribute_T(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    self.obj161.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,424.5,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=hasAttribute_T(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    self.obj162.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1201.0,519.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj163=hasAttribute_T(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    self.obj163.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(833.0,592.5,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=hasAttribute_T(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    self.obj164.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,422.5,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=hasAttribute_T(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    self.obj165.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,542.5,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=leftExpr(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    self.obj166.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,176.5,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=leftExpr(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    self.obj167.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1487.0,309.5,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=leftExpr(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    self.obj168.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1492.0,454.0,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=leftExpr(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    self.obj169.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,477.0,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=leftExpr(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    self.obj170.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,636.5,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj171=leftExpr(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    self.obj171.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(396.0,356.5,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=leftExpr(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(False)

    self.obj172.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(346.0,656.5,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=rightExpr(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(False)

    self.obj173.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(403.5,216.5,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=rightExpr(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    self.obj174.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1365.0,243.5,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=rightExpr(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    self.obj175.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1424.0,534.0,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=rightExpr(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    self.obj176.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1063.0,412.5,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    self.obj177=rightExpr(self)
    self.obj177.isGraphObjectVisual = True

    if(hasattr(self.obj177, '_setHierarchicalLink')):
      self.obj177._setHierarchicalLink(False)

    self.obj177.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(796.0,676.5,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)
    self.obj177.postAction( rootNode.CREATE )

    self.obj178=rightExpr(self)
    self.obj178.isGraphObjectVisual = True

    if(hasattr(self.obj178, '_setHierarchicalLink')):
      self.obj178._setHierarchicalLink(False)

    self.obj178.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(556.0,376.5,self.obj178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj178)
    self.globalAndLocalPostcondition(self.obj178, rootNode)
    self.obj178.postAction( rootNode.CREATE )

    self.obj179=rightExpr(self)
    self.obj179.isGraphObjectVisual = True

    if(hasattr(self.obj179, '_setHierarchicalLink')):
      self.obj179._setHierarchicalLink(False)

    self.obj179.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(456.0,666.5,self.obj179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj179)
    self.globalAndLocalPostcondition(self.obj179, rootNode)
    self.obj179.postAction( rootNode.CREATE )

    self.obj180=hasArgs(self)
    self.obj180.isGraphObjectVisual = True

    if(hasattr(self.obj180, '_setHierarchicalLink')):
      self.obj180._setHierarchicalLink(False)

    self.obj180.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(932.0,344.0,self.obj180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj180)
    self.globalAndLocalPostcondition(self.obj180, rootNode)
    self.obj180.postAction( rootNode.CREATE )

    self.obj181=hasArgs(self)
    self.obj181.isGraphObjectVisual = True

    if(hasattr(self.obj181, '_setHierarchicalLink')):
      self.obj181._setHierarchicalLink(False)

    self.obj181.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1029.0,314.0,self.obj181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj181)
    self.globalAndLocalPostcondition(self.obj181, rootNode)
    self.obj181.postAction( rootNode.CREATE )

    self.obj182=hasArgs(self)
    self.obj182.isGraphObjectVisual = True

    if(hasattr(self.obj182, '_setHierarchicalLink')):
      self.obj182._setHierarchicalLink(False)

    self.obj182.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1111.0,312.0,self.obj182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj182)
    self.globalAndLocalPostcondition(self.obj182, rootNode)
    self.obj182.postAction( rootNode.CREATE )

    self.obj183=hasArgs(self)
    self.obj183.isGraphObjectVisual = True

    if(hasattr(self.obj183, '_setHierarchicalLink')):
      self.obj183._setHierarchicalLink(False)

    self.obj183.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(574.0,334.0,self.obj183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj183)
    self.globalAndLocalPostcondition(self.obj183, rootNode)
    self.obj183.postAction( rootNode.CREATE )

    self.obj184=hasArgs(self)
    self.obj184.isGraphObjectVisual = True

    if(hasattr(self.obj184, '_setHierarchicalLink')):
      self.obj184._setHierarchicalLink(False)

    self.obj184.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(644.0,324.0,self.obj184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj184)
    self.globalAndLocalPostcondition(self.obj184, rootNode)
    self.obj184.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj138,[138.0, 51.0, 140.5, 232.0],"true", 2),
(self.obj100,self.obj139,[138.0, 51.0, 341.0, 33.0],"true", 2),
(self.obj100,self.obj140,[138.0, 51.0, 370.0, 21.0],"true", 2),
(self.obj100,self.obj141,[138.0, 51.0, 368.0, 10.0],"true", 2),
(self.obj100,self.obj142,[138.0, 51.0, 531.0, 8.0],"true", 2),
(self.obj100,self.obj143,[138.0, 51.0, 374.0, 117.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj144,[143.0, 413.0, 267.5, 442.0],"true", 2),
(self.obj101,self.obj145,[143.0, 413.0, 206.5, 532.0],"true", 2),
(self.obj101,self.obj146,[143.0, 413.0, 667.5, 492.0],"true", 2),
(self.obj101,self.obj147,[143.0, 413.0, 747.5, 422.0],"true", 2),
(self.obj101,self.obj148,[143.0, 413.0, 747.5, 372.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj2) named entrypoint1
    self.drawConnections(
(self.obj102,self.obj156,[950.0, 83.0, 850.5, 133.0],"true", 2),
(self.obj102,self.obj158,[950.0, 83.0, 912.0, 206.5],"true", 2) )
    # Connections for obj103 (graphObject_: Obj3) named transition1
    self.drawConnections(
(self.obj103,self.obj154,[570.0, 83.0, 760.0, 83.0],"true", 2),
(self.obj103,self.obj155,[570.0, 83.0, 597.0, 124.0],"true", 2) )
    # Connections for obj104 (graphObject_: Obj4) named statemachine1
    self.drawConnections(
(self.obj104,self.obj157,[790.0, 183.0, 674.5, 241.5],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) named state1
    self.drawConnections(
(self.obj105,self.obj153,[350.0, 83.0, 460.0, 83.0],"true", 2),
(self.obj105,self.obj159,[350.0, 83.0, 317.5, 128.5],"true", 2) )
    # Connections for obj106 (graphObject_: Obj6) named in1_1
    self.drawConnections(
 )
    # Connections for obj107 (graphObject_: Obj7) named name1
    self.drawConnections(
(self.obj107,self.obj160,[1352.0, 331.0, 1400.0, 330.5],"true", 2) )
    # Connections for obj108 (graphObject_: Obj8) named name2
    self.drawConnections(
(self.obj108,self.obj161,[1352.0, 431.0, 1400.0, 424.5],"true", 2) )
    # Connections for obj109 (graphObject_: Obj9) named name3
    self.drawConnections(
(self.obj109,self.obj162,[1192.0, 571.0, 1201.0, 519.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj10) named name4
    self.drawConnections(
(self.obj110,self.obj163,[752.0, 591.0, 833.0, 592.5],"true", 2) )
    # Connections for obj111 (graphObject_: Obj11) named inst1
    self.drawConnections(
(self.obj111,self.obj149,[392.0, 471.0, 1026.0, 326.0],"true", 2),
(self.obj111,self.obj150,[392.0, 471.0, 1013.0, 431.0],"true", 2),
(self.obj111,self.obj151,[392.0, 471.0, 792.0, 521.0],"true", 2),
(self.obj111,self.obj152,[392.0, 471.0, 572.0, 531.0],"true", 2),
(self.obj111,self.obj164,[392.0, 471.0, 353.0, 422.5],"true", 2),
(self.obj111,self.obj165,[392.0, 471.0, 353.0, 542.5],"true", 2) )
    # Connections for obj112 (graphObject_: Obj12) named name
    self.drawConnections(
 )
    # Connections for obj113 (graphObject_: Obj13) named name
    self.drawConnections(
 )
    # Connections for obj114 (graphObject_: Obj14) named isComposite
    self.drawConnections(
 )
    # Connections for obj115 (graphObject_: Obj15) named literal
    self.drawConnections(
 )
    # Connections for obj116 (graphObject_: Obj16) named literal
    self.drawConnections(
 )
    # Connections for obj117 (graphObject_: Obj17) named literal
    self.drawConnections(
 )
    # Connections for obj118 (graphObject_: Obj18) named literal
    self.drawConnections(
 )
    # Connections for obj119 (graphObject_: Obj19) named name
    self.drawConnections(
 )
    # Connections for obj120 (graphObject_: Obj20) named pivot
    self.drawConnections(
 )
    # Connections for obj121 (graphObject_: Obj21) named eq1
    self.drawConnections(
(self.obj121,self.obj166,[433.0, 179.0, 359.0, 176.5],"true", 2),
(self.obj121,self.obj173,[433.0, 179.0, 403.5, 216.5],"true", 2) )
    # Connections for obj122 (graphObject_: Obj22) named eq2
    self.drawConnections(
(self.obj122,self.obj167,[1498.0, 259.0, 1487.0, 309.5],"true", 2),
(self.obj122,self.obj174,[1498.0, 259.0, 1365.0, 243.5],"true", 2) )
    # Connections for obj123 (graphObject_: Obj23) named eq3
    self.drawConnections(
(self.obj123,self.obj168,[1498.0, 499.0, 1492.0, 454.0],"true", 2),
(self.obj123,self.obj175,[1498.0, 499.0, 1424.0, 534.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj24) named eq4
    self.drawConnections(
(self.obj124,self.obj169,[1012.0, 488.0, 1100.0, 477.0],"true", 2),
(self.obj124,self.obj176,[1012.0, 488.0, 1063.0, 412.5],"true", 2) )
    # Connections for obj125 (graphObject_: Obj25) named eq5
    self.drawConnections(
(self.obj125,self.obj170,[878.0, 679.0, 896.0, 636.5],"true", 2),
(self.obj125,self.obj177,[878.0, 679.0, 796.0, 676.5],"true", 2) )
    # Connections for obj126 (graphObject_: Obj26) named eq6
    self.drawConnections(
(self.obj126,self.obj171,[478.0, 379.0, 396.0, 356.5],"true", 2),
(self.obj126,self.obj178,[478.0, 379.0, 556.0, 376.5],"true", 2) )
    # Connections for obj127 (graphObject_: Obj27) named eq7
    self.drawConnections(
(self.obj127,self.obj179,[378.0, 699.0, 456.0, 666.5],"true", 2),
(self.obj127,self.obj172,[378.0, 699.0, 346.0, 656.5],"true", 2) )
    # Connections for obj128 (graphObject_: Obj28) named concat1
    self.drawConnections(
(self.obj128,self.obj180,[1074.0, 389.0, 932.0, 344.0],"true", 2),
(self.obj128,self.obj181,[1074.0, 389.0, 1029.0, 314.0],"true", 2),
(self.obj128,self.obj182,[1074.0, 389.0, 1111.0, 312.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj29) named concat2
    self.drawConnections(
(self.obj129,self.obj183,[634.0, 374.0, 574.0, 334.0],"true", 2),
(self.obj129,self.obj184,[634.0, 374.0, 644.0, 324.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj30) named true
    self.drawConnections(
 )
    # Connections for obj131 (graphObject_: Obj31) named exit_in
    self.drawConnections(
 )
    # Connections for obj132 (graphObject_: Obj32) named exack_in
    self.drawConnections(
 )
    # Connections for obj133 (graphObject_: Obj33) named 2
    self.drawConnections(
 )
    # Connections for obj134 (graphObject_: Obj34) named 1
    self.drawConnections(
 )
    # Connections for obj135 (graphObject_: Obj35) named sh_in
    self.drawConnections(
 )
    # Connections for obj136 (graphObject_: Obj36) named S
    self.drawConnections(
 )
    # Connections for obj137 (graphObject_: Obj37) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj138 (graphObject_: Obj38) of type paired_with
    self.drawConnections(
(self.obj138,self.obj101,[140.5, 232.0, 143.0, 413.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj39) of type match_contains
    self.drawConnections(
(self.obj139,self.obj105,[341.0, 33.0, 350.0, 83.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj40) of type match_contains
    self.drawConnections(
(self.obj140,self.obj103,[370.0, 21.0, 570.0, 83.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj41) of type match_contains
    self.drawConnections(
(self.obj141,self.obj102,[368.0, 10.0, 950.0, 83.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj42) of type match_contains
    self.drawConnections(
(self.obj142,self.obj104,[531.0, 8.0, 790.0, 183.0],"true", 2) )
    # Connections for obj143 (graphObject_: Obj43) of type match_contains
    self.drawConnections(
(self.obj143,self.obj106,[374.0, 117.0, 610.0, 183.0],"true", 2) )
    # Connections for obj144 (graphObject_: Obj44) of type apply_contains
    self.drawConnections(
(self.obj144,self.obj111,[267.5, 442.0, 392.0, 471.0],"true", 2) )
    # Connections for obj145 (graphObject_: Obj45) of type apply_contains
    self.drawConnections(
(self.obj145,self.obj110,[206.5, 532.0, 752.0, 591.0],"true", 2) )
    # Connections for obj146 (graphObject_: Obj46) of type apply_contains
    self.drawConnections(
(self.obj146,self.obj109,[667.5, 492.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj147 (graphObject_: Obj47) of type apply_contains
    self.drawConnections(
(self.obj147,self.obj108,[747.5, 422.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj148 (graphObject_: Obj48) of type apply_contains
    self.drawConnections(
(self.obj148,self.obj107,[747.5, 372.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj149 (graphObject_: Obj49) of type directLink_T
    self.drawConnections(
(self.obj149,self.obj107,[1026.0, 326.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj150 (graphObject_: Obj50) of type directLink_T
    self.drawConnections(
(self.obj150,self.obj108,[1013.0, 431.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj151 (graphObject_: Obj51) of type directLink_T
    self.drawConnections(
(self.obj151,self.obj109,[792.0, 521.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj152 (graphObject_: Obj52) of type directLink_T
    self.drawConnections(
(self.obj152,self.obj110,[572.0, 531.0, 752.0, 591.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj53) of type directLink_S
    self.drawConnections(
(self.obj153,self.obj103,[460.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj154 (graphObject_: Obj54) of type directLink_S
    self.drawConnections(
(self.obj154,self.obj102,[760.0, 83.0, 950.0, 83.0],"true", 2) )
    # Connections for obj155 (graphObject_: Obj55) of type directLink_S
    self.drawConnections(
(self.obj155,self.obj106,[597.0, 124.0, 610.0, 183.0],"true", 2) )
    # Connections for obj156 (graphObject_: Obj56) of type directLink_S
    self.drawConnections(
(self.obj156,self.obj104,[850.5, 133.0, 790.0, 183.0],"true", 2) )
    # Connections for obj157 (graphObject_: Obj57) of type hasAttribute_S
    self.drawConnections(
(self.obj157,self.obj113,[674.5, 241.5, 674.0, 274.0],"true", 2) )
    # Connections for obj158 (graphObject_: Obj58) of type hasAttribute_S
    self.drawConnections(
(self.obj158,self.obj112,[912.0, 206.5, 994.0, 254.0],"true", 2) )
    # Connections for obj159 (graphObject_: Obj59) of type hasAttribute_S
    self.drawConnections(
(self.obj159,self.obj114,[317.5, 128.5, 285.0, 174.0],"true", 2) )
    # Connections for obj160 (graphObject_: Obj60) of type hasAttribute_T
    self.drawConnections(
(self.obj160,self.obj115,[1400.0, 330.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj161 (graphObject_: Obj61) of type hasAttribute_T
    self.drawConnections(
(self.obj161,self.obj116,[1400.0, 424.5, 1494.0, 414.0],"true", 2) )
    # Connections for obj162 (graphObject_: Obj62) of type hasAttribute_T
    self.drawConnections(
(self.obj162,self.obj117,[1201.0, 519.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj163 (graphObject_: Obj63) of type hasAttribute_T
    self.drawConnections(
(self.obj163,self.obj118,[833.0, 592.5, 914.0, 594.0],"true", 2) )
    # Connections for obj164 (graphObject_: Obj64) of type hasAttribute_T
    self.drawConnections(
(self.obj164,self.obj119,[353.0, 422.5, 314.0, 374.0],"true", 2) )
    # Connections for obj165 (graphObject_: Obj65) of type hasAttribute_T
    self.drawConnections(
(self.obj165,self.obj120,[353.0, 542.5, 314.0, 614.0],"true", 2) )
    # Connections for obj166 (graphObject_: Obj66) of type leftExpr
    self.drawConnections(
(self.obj166,self.obj114,[359.0, 176.5, 285.0, 174.0],"true", 2) )
    # Connections for obj167 (graphObject_: Obj67) of type leftExpr
    self.drawConnections(
(self.obj167,self.obj115,[1487.0, 309.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj168 (graphObject_: Obj68) of type leftExpr
    self.drawConnections(
(self.obj168,self.obj116,[1492.0, 454.0, 1494.0, 414.0],"true", 2) )
    # Connections for obj169 (graphObject_: Obj69) of type leftExpr
    self.drawConnections(
(self.obj169,self.obj117,[1100.0, 477.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj170 (graphObject_: Obj70) of type leftExpr
    self.drawConnections(
(self.obj170,self.obj118,[896.0, 636.5, 914.0, 594.0],"true", 2) )
    # Connections for obj171 (graphObject_: Obj71) of type leftExpr
    self.drawConnections(
(self.obj171,self.obj119,[396.0, 356.5, 314.0, 374.0],"true", 2) )
    # Connections for obj172 (graphObject_: Obj72) of type leftExpr
    self.drawConnections(
(self.obj172,self.obj120,[346.0, 656.5, 314.0, 614.0],"true", 2) )
    # Connections for obj173 (graphObject_: Obj73) of type rightExpr
    self.drawConnections(
(self.obj173,self.obj130,[403.5, 216.5, 374.0, 254.0],"true", 2) )
    # Connections for obj174 (graphObject_: Obj74) of type rightExpr
    self.drawConnections(
(self.obj174,self.obj131,[1365.0, 243.5, 1334.0, 241.0],"true", 2) )
    # Connections for obj175 (graphObject_: Obj75) of type rightExpr
    self.drawConnections(
(self.obj175,self.obj132,[1424.0, 534.0, 1354.0, 514.0],"true", 2) )
    # Connections for obj176 (graphObject_: Obj76) of type rightExpr
    self.drawConnections(
(self.obj176,self.obj128,[1063.0, 412.5, 1074.0, 389.0],"true", 2) )
    # Connections for obj177 (graphObject_: Obj77) of type rightExpr
    self.drawConnections(
(self.obj177,self.obj135,[796.0, 676.5, 714.0, 674.0],"true", 2) )
    # Connections for obj178 (graphObject_: Obj78) of type rightExpr
    self.drawConnections(
(self.obj178,self.obj129,[556.0, 376.5, 634.0, 374.0],"true", 2) )
    # Connections for obj179 (graphObject_: Obj79) of type rightExpr
    self.drawConnections(
(self.obj179,self.obj137,[456.0, 666.5, 485.0, 614.0],"true", 2) )
    # Connections for obj180 (graphObject_: Obj80) of type hasArgs
    self.drawConnections(
(self.obj180,self.obj134,[932.0, 344.0, 854.0, 314.0],"true", 2) )
    # Connections for obj181 (graphObject_: Obj81) of type hasArgs
    self.drawConnections(
(self.obj181,self.obj112,[1029.0, 314.0, 994.0, 254.0],"true", 2) )
    # Connections for obj182 (graphObject_: Obj82) of type hasArgs
    self.drawConnections(
(self.obj182,self.obj133,[1111.0, 312.0, 1142.0, 234.0],"true", 2) )
    # Connections for obj183 (graphObject_: Obj83) of type hasArgs
    self.drawConnections(
(self.obj183,self.obj136,[574.0, 334.0, 514.0, 294.0],"true", 2) )
    # Connections for obj184 (graphObject_: Obj84) of type hasArgs
    self.drawConnections(
(self.obj184,self.obj113,[644.0, 324.0, 674.0, 274.0],"true", 2) )

newfunction = Transition2Inst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
