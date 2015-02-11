"""
__Transition2Inst_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:24:55 2015
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


    self.obj984=MatchModel(self)
    self.obj984.isGraphObjectVisual = True

    if(hasattr(self.obj984, '_setHierarchicalLink')):
      self.obj984._setHierarchicalLink(False)

    self.obj984.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj984)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj984.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj984)
    self.globalAndLocalPostcondition(self.obj984, rootNode)
    self.obj984.postAction( rootNode.CREATE )

    self.obj985=ApplyModel(self)
    self.obj985.isGraphObjectVisual = True

    if(hasattr(self.obj985, '_setHierarchicalLink')):
      self.obj985._setHierarchicalLink(False)

    self.obj985.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,380.0,self.obj985)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj985.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj985)
    self.globalAndLocalPostcondition(self.obj985, rootNode)
    self.obj985.postAction( rootNode.CREATE )

    self.obj986=EntryPoint(self)
    self.obj986.isGraphObjectVisual = True

    if(hasattr(self.obj986, '_setHierarchicalLink')):
      self.obj986._setHierarchicalLink(False)

    # name
    self.obj986.name.setValue('entrypoint1')

    # classtype
    self.obj986.classtype.setValue('EntryPoint')

    # cardinality
    self.obj986.cardinality.setValue('1')

    self.obj986.graphClass_= graph_EntryPoint
    if self.genGraphics:
       new_obj = graph_EntryPoint(780.0,40.0,self.obj986)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("EntryPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj986.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj986)
    self.globalAndLocalPostcondition(self.obj986, rootNode)
    self.obj986.postAction( rootNode.CREATE )

    self.obj987=Transition(self)
    self.obj987.isGraphObjectVisual = True

    if(hasattr(self.obj987, '_setHierarchicalLink')):
      self.obj987._setHierarchicalLink(False)

    # name
    self.obj987.name.setValue('transition1')

    # classtype
    self.obj987.classtype.setValue('Transition')

    # cardinality
    self.obj987.cardinality.setValue('+')

    self.obj987.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(400.0,40.0,self.obj987)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj987.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj987)
    self.globalAndLocalPostcondition(self.obj987, rootNode)
    self.obj987.postAction( rootNode.CREATE )

    self.obj988=StateMachine(self)
    self.obj988.isGraphObjectVisual = True

    if(hasattr(self.obj988, '_setHierarchicalLink')):
      self.obj988._setHierarchicalLink(False)

    # name
    self.obj988.name.setValue('statemachine1')

    # classtype
    self.obj988.classtype.setValue('StateMachine')

    # cardinality
    self.obj988.cardinality.setValue('1')

    self.obj988.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(620.0,140.0,self.obj988)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj988.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj988)
    self.globalAndLocalPostcondition(self.obj988, rootNode)
    self.obj988.postAction( rootNode.CREATE )

    self.obj989=State(self)
    self.obj989.isGraphObjectVisual = True

    if(hasattr(self.obj989, '_setHierarchicalLink')):
      self.obj989._setHierarchicalLink(False)

    # name
    self.obj989.name.setValue('state1')

    # classtype
    self.obj989.classtype.setValue('State')

    # cardinality
    self.obj989.cardinality.setValue('+')

    self.obj989.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj989)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj989.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj989)
    self.globalAndLocalPostcondition(self.obj989, rootNode)
    self.obj989.postAction( rootNode.CREATE )

    self.obj990=IN1(self)
    self.obj990.isGraphObjectVisual = True

    if(hasattr(self.obj990, '_setHierarchicalLink')):
      self.obj990._setHierarchicalLink(False)

    # classtype
    self.obj990.classtype.setValue('IN1')

    # cardinality
    self.obj990.cardinality.setValue('1')

    # name
    self.obj990.name.setValue('in1_1')

    self.obj990.graphClass_= graph_IN1
    if self.genGraphics:
       new_obj = graph_IN1(440.0,140.0,self.obj990)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IN1", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj990.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj990)
    self.globalAndLocalPostcondition(self.obj990, rootNode)
    self.obj990.postAction( rootNode.CREATE )

    self.obj991=Name(self)
    self.obj991.isGraphObjectVisual = True

    if(hasattr(self.obj991, '_setHierarchicalLink')):
      self.obj991._setHierarchicalLink(False)

    # classtype
    self.obj991.classtype.setValue('Name')

    # cardinality
    self.obj991.cardinality.setValue('1')

    # name
    self.obj991.name.setValue('name1')

    self.obj991.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,280.0,self.obj991)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj991.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj991)
    self.globalAndLocalPostcondition(self.obj991, rootNode)
    self.obj991.postAction( rootNode.CREATE )

    self.obj992=Name(self)
    self.obj992.isGraphObjectVisual = True

    if(hasattr(self.obj992, '_setHierarchicalLink')):
      self.obj992._setHierarchicalLink(False)

    # classtype
    self.obj992.classtype.setValue('Name')

    # cardinality
    self.obj992.cardinality.setValue('1')

    # name
    self.obj992.name.setValue('name2')

    self.obj992.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1180.0,380.0,self.obj992)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj992.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj992)
    self.globalAndLocalPostcondition(self.obj992, rootNode)
    self.obj992.postAction( rootNode.CREATE )

    self.obj993=Name(self)
    self.obj993.isGraphObjectVisual = True

    if(hasattr(self.obj993, '_setHierarchicalLink')):
      self.obj993._setHierarchicalLink(False)

    # classtype
    self.obj993.classtype.setValue('Name')

    # cardinality
    self.obj993.cardinality.setValue('1')

    # name
    self.obj993.name.setValue('name3')

    self.obj993.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1020.0,520.0,self.obj993)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj993.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj993)
    self.globalAndLocalPostcondition(self.obj993, rootNode)
    self.obj993.postAction( rootNode.CREATE )

    self.obj994=Name(self)
    self.obj994.isGraphObjectVisual = True

    if(hasattr(self.obj994, '_setHierarchicalLink')):
      self.obj994._setHierarchicalLink(False)

    # classtype
    self.obj994.classtype.setValue('Name')

    # cardinality
    self.obj994.cardinality.setValue('1')

    # name
    self.obj994.name.setValue('name4')

    self.obj994.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(580.0,540.0,self.obj994)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj994.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj994)
    self.globalAndLocalPostcondition(self.obj994, rootNode)
    self.obj994.postAction( rootNode.CREATE )

    self.obj995=Inst(self)
    self.obj995.isGraphObjectVisual = True

    if(hasattr(self.obj995, '_setHierarchicalLink')):
      self.obj995._setHierarchicalLink(False)

    # classtype
    self.obj995.classtype.setValue('Inst')

    # cardinality
    self.obj995.cardinality.setValue('1')

    # name
    self.obj995.name.setValue('inst1')

    self.obj995.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(220.0,420.0,self.obj995)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj995.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj995)
    self.globalAndLocalPostcondition(self.obj995, rootNode)
    self.obj995.postAction( rootNode.CREATE )

    self.obj996=Attribute(self)
    self.obj996.isGraphObjectVisual = True

    if(hasattr(self.obj996, '_setHierarchicalLink')):
      self.obj996._setHierarchicalLink(False)

    # Type
    self.obj996.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj996.Type.config = 0

    # name
    self.obj996.name.setValue('name')

    self.obj996.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,220.0,self.obj996)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj996.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj996)
    self.globalAndLocalPostcondition(self.obj996, rootNode)
    self.obj996.postAction( rootNode.CREATE )

    self.obj997=Attribute(self)
    self.obj997.isGraphObjectVisual = True

    if(hasattr(self.obj997, '_setHierarchicalLink')):
      self.obj997._setHierarchicalLink(False)

    # Type
    self.obj997.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj997.Type.config = 0

    # name
    self.obj997.name.setValue('name')

    self.obj997.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(540.0,240.0,self.obj997)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj997.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj997)
    self.globalAndLocalPostcondition(self.obj997, rootNode)
    self.obj997.postAction( rootNode.CREATE )

    self.obj998=Attribute(self)
    self.obj998.isGraphObjectVisual = True

    if(hasattr(self.obj998, '_setHierarchicalLink')):
      self.obj998._setHierarchicalLink(False)

    # Type
    self.obj998.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj998.Type.config = 0

    # name
    self.obj998.name.setValue('isComposite')

    self.obj998.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(151.0,140.0,self.obj998)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj998.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj998)
    self.globalAndLocalPostcondition(self.obj998, rootNode)
    self.obj998.postAction( rootNode.CREATE )

    self.obj999=Attribute(self)
    self.obj999.isGraphObjectVisual = True

    if(hasattr(self.obj999, '_setHierarchicalLink')):
      self.obj999._setHierarchicalLink(False)

    # Type
    self.obj999.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj999.Type.config = 0

    # name
    self.obj999.name.setValue('literal')

    self.obj999.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,300.0,self.obj999)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj999.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj999)
    self.globalAndLocalPostcondition(self.obj999, rootNode)
    self.obj999.postAction( rootNode.CREATE )

    self.obj1000=Attribute(self)
    self.obj1000.isGraphObjectVisual = True

    if(hasattr(self.obj1000, '_setHierarchicalLink')):
      self.obj1000._setHierarchicalLink(False)

    # Type
    self.obj1000.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1000.Type.config = 0

    # name
    self.obj1000.name.setValue('literal')

    self.obj1000.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1360.0,380.0,self.obj1000)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1000.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1000)
    self.globalAndLocalPostcondition(self.obj1000, rootNode)
    self.obj1000.postAction( rootNode.CREATE )

    self.obj1001=Attribute(self)
    self.obj1001.isGraphObjectVisual = True

    if(hasattr(self.obj1001, '_setHierarchicalLink')):
      self.obj1001._setHierarchicalLink(False)

    # Type
    self.obj1001.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1001.Type.config = 0

    # name
    self.obj1001.name.setValue('literal')

    self.obj1001.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1020.0,440.0,self.obj1001)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1001.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1001)
    self.globalAndLocalPostcondition(self.obj1001, rootNode)
    self.obj1001.postAction( rootNode.CREATE )

    self.obj1002=Attribute(self)
    self.obj1002.isGraphObjectVisual = True

    if(hasattr(self.obj1002, '_setHierarchicalLink')):
      self.obj1002._setHierarchicalLink(False)

    # Type
    self.obj1002.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1002.Type.config = 0

    # name
    self.obj1002.name.setValue('literal')

    self.obj1002.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,560.0,self.obj1002)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1002.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1002)
    self.globalAndLocalPostcondition(self.obj1002, rootNode)
    self.obj1002.postAction( rootNode.CREATE )

    self.obj1003=Attribute(self)
    self.obj1003.isGraphObjectVisual = True

    if(hasattr(self.obj1003, '_setHierarchicalLink')):
      self.obj1003._setHierarchicalLink(False)

    # Type
    self.obj1003.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1003.Type.config = 0

    # name
    self.obj1003.name.setValue('name')

    self.obj1003.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,340.0,self.obj1003)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1003.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1003)
    self.globalAndLocalPostcondition(self.obj1003, rootNode)
    self.obj1003.postAction( rootNode.CREATE )

    self.obj1004=Attribute(self)
    self.obj1004.isGraphObjectVisual = True

    if(hasattr(self.obj1004, '_setHierarchicalLink')):
      self.obj1004._setHierarchicalLink(False)

    # Type
    self.obj1004.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1004.Type.config = 0

    # name
    self.obj1004.name.setValue('pivot')

    self.obj1004.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,580.0,self.obj1004)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1004.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1004)
    self.globalAndLocalPostcondition(self.obj1004, rootNode)
    self.obj1004.postAction( rootNode.CREATE )

    self.obj1005=Equation(self)
    self.obj1005.isGraphObjectVisual = True

    if(hasattr(self.obj1005, '_setHierarchicalLink')):
      self.obj1005._setHierarchicalLink(False)

    # name
    self.obj1005.name.setValue('eq1')

    self.obj1005.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(295.0,140.0,self.obj1005)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1005.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1005)
    self.globalAndLocalPostcondition(self.obj1005, rootNode)
    self.obj1005.postAction( rootNode.CREATE )

    self.obj1006=Equation(self)
    self.obj1006.isGraphObjectVisual = True

    if(hasattr(self.obj1006, '_setHierarchicalLink')):
      self.obj1006._setHierarchicalLink(False)

    # name
    self.obj1006.name.setValue('eq2')

    self.obj1006.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,220.0,self.obj1006)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1006.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1006)
    self.globalAndLocalPostcondition(self.obj1006, rootNode)
    self.obj1006.postAction( rootNode.CREATE )

    self.obj1007=Equation(self)
    self.obj1007.isGraphObjectVisual = True

    if(hasattr(self.obj1007, '_setHierarchicalLink')):
      self.obj1007._setHierarchicalLink(False)

    # name
    self.obj1007.name.setValue('eq3')

    self.obj1007.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1360.0,460.0,self.obj1007)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1007.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1007)
    self.globalAndLocalPostcondition(self.obj1007, rootNode)
    self.obj1007.postAction( rootNode.CREATE )

    self.obj1008=Equation(self)
    self.obj1008.isGraphObjectVisual = True

    if(hasattr(self.obj1008, '_setHierarchicalLink')):
      self.obj1008._setHierarchicalLink(False)

    # name
    self.obj1008.name.setValue('eq4')

    self.obj1008.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(874.0,449.0,self.obj1008)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1008.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1008)
    self.globalAndLocalPostcondition(self.obj1008, rootNode)
    self.obj1008.postAction( rootNode.CREATE )

    self.obj1009=Equation(self)
    self.obj1009.isGraphObjectVisual = True

    if(hasattr(self.obj1009, '_setHierarchicalLink')):
      self.obj1009._setHierarchicalLink(False)

    # name
    self.obj1009.name.setValue('eq5')

    self.obj1009.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(740.0,640.0,self.obj1009)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1009.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1009)
    self.globalAndLocalPostcondition(self.obj1009, rootNode)
    self.obj1009.postAction( rootNode.CREATE )

    self.obj1010=Equation(self)
    self.obj1010.isGraphObjectVisual = True

    if(hasattr(self.obj1010, '_setHierarchicalLink')):
      self.obj1010._setHierarchicalLink(False)

    # name
    self.obj1010.name.setValue('eq6')

    self.obj1010.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,340.0,self.obj1010)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1010.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1010)
    self.globalAndLocalPostcondition(self.obj1010, rootNode)
    self.obj1010.postAction( rootNode.CREATE )

    self.obj1011=Equation(self)
    self.obj1011.isGraphObjectVisual = True

    if(hasattr(self.obj1011, '_setHierarchicalLink')):
      self.obj1011._setHierarchicalLink(False)

    # name
    self.obj1011.name.setValue('eq7')

    self.obj1011.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,660.0,self.obj1011)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1011.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1011)
    self.globalAndLocalPostcondition(self.obj1011, rootNode)
    self.obj1011.postAction( rootNode.CREATE )

    self.obj1012=Concat(self)
    self.obj1012.isGraphObjectVisual = True

    if(hasattr(self.obj1012, '_setHierarchicalLink')):
      self.obj1012._setHierarchicalLink(False)

    # Type
    self.obj1012.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1012.Type.config = 0

    # name
    self.obj1012.name.setValue('concat1')

    self.obj1012.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(940.0,355.0,self.obj1012)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1012.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1012)
    self.globalAndLocalPostcondition(self.obj1012, rootNode)
    self.obj1012.postAction( rootNode.CREATE )

    self.obj1013=Concat(self)
    self.obj1013.isGraphObjectVisual = True

    if(hasattr(self.obj1013, '_setHierarchicalLink')):
      self.obj1013._setHierarchicalLink(False)

    # Type
    self.obj1013.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1013.Type.config = 0

    # name
    self.obj1013.name.setValue('concat2')

    self.obj1013.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,340.0,self.obj1013)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1013.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1013)
    self.globalAndLocalPostcondition(self.obj1013, rootNode)
    self.obj1013.postAction( rootNode.CREATE )

    self.obj1014=Constant(self)
    self.obj1014.isGraphObjectVisual = True

    if(hasattr(self.obj1014, '_setHierarchicalLink')):
      self.obj1014._setHierarchicalLink(False)

    # Type
    self.obj1014.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1014.Type.config = 0

    # name
    self.obj1014.name.setValue('true')

    self.obj1014.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(240.0,220.0,self.obj1014)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1014.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1014)
    self.globalAndLocalPostcondition(self.obj1014, rootNode)
    self.obj1014.postAction( rootNode.CREATE )

    self.obj1015=Constant(self)
    self.obj1015.isGraphObjectVisual = True

    if(hasattr(self.obj1015, '_setHierarchicalLink')):
      self.obj1015._setHierarchicalLink(False)

    # Type
    self.obj1015.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1015.Type.config = 0

    # name
    self.obj1015.name.setValue('exit_in')

    self.obj1015.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1200.0,207.0,self.obj1015)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1015.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1015)
    self.globalAndLocalPostcondition(self.obj1015, rootNode)
    self.obj1015.postAction( rootNode.CREATE )

    self.obj1016=Constant(self)
    self.obj1016.isGraphObjectVisual = True

    if(hasattr(self.obj1016, '_setHierarchicalLink')):
      self.obj1016._setHierarchicalLink(False)

    # Type
    self.obj1016.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1016.Type.config = 0

    # name
    self.obj1016.name.setValue('exack_in')

    self.obj1016.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1220.0,480.0,self.obj1016)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1016.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1016)
    self.globalAndLocalPostcondition(self.obj1016, rootNode)
    self.obj1016.postAction( rootNode.CREATE )

    self.obj1017=Constant(self)
    self.obj1017.isGraphObjectVisual = True

    if(hasattr(self.obj1017, '_setHierarchicalLink')):
      self.obj1017._setHierarchicalLink(False)

    # Type
    self.obj1017.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1017.Type.config = 0

    # name
    self.obj1017.name.setValue('2')

    self.obj1017.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1008.0,200.0,self.obj1017)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1017.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1017)
    self.globalAndLocalPostcondition(self.obj1017, rootNode)
    self.obj1017.postAction( rootNode.CREATE )

    self.obj1018=Constant(self)
    self.obj1018.isGraphObjectVisual = True

    if(hasattr(self.obj1018, '_setHierarchicalLink')):
      self.obj1018._setHierarchicalLink(False)

    # Type
    self.obj1018.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1018.Type.config = 0

    # name
    self.obj1018.name.setValue('1')

    self.obj1018.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(720.0,280.0,self.obj1018)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1018.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1018)
    self.globalAndLocalPostcondition(self.obj1018, rootNode)
    self.obj1018.postAction( rootNode.CREATE )

    self.obj1019=Constant(self)
    self.obj1019.isGraphObjectVisual = True

    if(hasattr(self.obj1019, '_setHierarchicalLink')):
      self.obj1019._setHierarchicalLink(False)

    # Type
    self.obj1019.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1019.Type.config = 0

    # name
    self.obj1019.name.setValue('sh_in')

    self.obj1019.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(580.0,640.0,self.obj1019)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1019.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1019)
    self.globalAndLocalPostcondition(self.obj1019, rootNode)
    self.obj1019.postAction( rootNode.CREATE )

    self.obj1020=Constant(self)
    self.obj1020.isGraphObjectVisual = True

    if(hasattr(self.obj1020, '_setHierarchicalLink')):
      self.obj1020._setHierarchicalLink(False)

    # Type
    self.obj1020.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1020.Type.config = 0

    # name
    self.obj1020.name.setValue('S')

    self.obj1020.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(380.0,260.0,self.obj1020)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1020.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1020)
    self.globalAndLocalPostcondition(self.obj1020, rootNode)
    self.obj1020.postAction( rootNode.CREATE )

    self.obj1021=Constant(self)
    self.obj1021.isGraphObjectVisual = True

    if(hasattr(self.obj1021, '_setHierarchicalLink')):
      self.obj1021._setHierarchicalLink(False)

    # Type
    self.obj1021.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1021.Type.config = 0

    # name
    self.obj1021.name.setValue('instForInTrans')

    self.obj1021.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(351.0,580.0,self.obj1021)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1021.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1021)
    self.globalAndLocalPostcondition(self.obj1021, rootNode)
    self.obj1021.postAction( rootNode.CREATE )

    self.obj1022=paired_with(self)
    self.obj1022.isGraphObjectVisual = True

    if(hasattr(self.obj1022, '_setHierarchicalLink')):
      self.obj1022._setHierarchicalLink(False)

    self.obj1022.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,232.0,self.obj1022)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1022.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1022)
    self.globalAndLocalPostcondition(self.obj1022, rootNode)
    self.obj1022.postAction( rootNode.CREATE )

    self.obj1023=match_contains(self)
    self.obj1023.isGraphObjectVisual = True

    if(hasattr(self.obj1023, '_setHierarchicalLink')):
      self.obj1023._setHierarchicalLink(False)

    self.obj1023.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(341.0,33.0,self.obj1023)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1023.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1023)
    self.globalAndLocalPostcondition(self.obj1023, rootNode)
    self.obj1023.postAction( rootNode.CREATE )

    self.obj1024=match_contains(self)
    self.obj1024.isGraphObjectVisual = True

    if(hasattr(self.obj1024, '_setHierarchicalLink')):
      self.obj1024._setHierarchicalLink(False)

    self.obj1024.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(370.0,21.0,self.obj1024)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1024.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1024)
    self.globalAndLocalPostcondition(self.obj1024, rootNode)
    self.obj1024.postAction( rootNode.CREATE )

    self.obj1025=match_contains(self)
    self.obj1025.isGraphObjectVisual = True

    if(hasattr(self.obj1025, '_setHierarchicalLink')):
      self.obj1025._setHierarchicalLink(False)

    self.obj1025.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(368.0,10.0,self.obj1025)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1025.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1025)
    self.globalAndLocalPostcondition(self.obj1025, rootNode)
    self.obj1025.postAction( rootNode.CREATE )

    self.obj1026=match_contains(self)
    self.obj1026.isGraphObjectVisual = True

    if(hasattr(self.obj1026, '_setHierarchicalLink')):
      self.obj1026._setHierarchicalLink(False)

    self.obj1026.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(531.0,8.0,self.obj1026)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1026.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1026)
    self.globalAndLocalPostcondition(self.obj1026, rootNode)
    self.obj1026.postAction( rootNode.CREATE )

    self.obj1027=match_contains(self)
    self.obj1027.isGraphObjectVisual = True

    if(hasattr(self.obj1027, '_setHierarchicalLink')):
      self.obj1027._setHierarchicalLink(False)

    self.obj1027.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(374.0,117.0,self.obj1027)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1027.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1027)
    self.globalAndLocalPostcondition(self.obj1027, rootNode)
    self.obj1027.postAction( rootNode.CREATE )

    self.obj1028=apply_contains(self)
    self.obj1028.isGraphObjectVisual = True

    if(hasattr(self.obj1028, '_setHierarchicalLink')):
      self.obj1028._setHierarchicalLink(False)

    self.obj1028.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(267.5,442.0,self.obj1028)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1028.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1028)
    self.globalAndLocalPostcondition(self.obj1028, rootNode)
    self.obj1028.postAction( rootNode.CREATE )

    self.obj1029=apply_contains(self)
    self.obj1029.isGraphObjectVisual = True

    if(hasattr(self.obj1029, '_setHierarchicalLink')):
      self.obj1029._setHierarchicalLink(False)

    self.obj1029.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(206.5,532.0,self.obj1029)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1029.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1029)
    self.globalAndLocalPostcondition(self.obj1029, rootNode)
    self.obj1029.postAction( rootNode.CREATE )

    self.obj1030=apply_contains(self)
    self.obj1030.isGraphObjectVisual = True

    if(hasattr(self.obj1030, '_setHierarchicalLink')):
      self.obj1030._setHierarchicalLink(False)

    self.obj1030.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(667.5,492.0,self.obj1030)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1030.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1030)
    self.globalAndLocalPostcondition(self.obj1030, rootNode)
    self.obj1030.postAction( rootNode.CREATE )

    self.obj1031=apply_contains(self)
    self.obj1031.isGraphObjectVisual = True

    if(hasattr(self.obj1031, '_setHierarchicalLink')):
      self.obj1031._setHierarchicalLink(False)

    self.obj1031.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,422.0,self.obj1031)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1031.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1031)
    self.globalAndLocalPostcondition(self.obj1031, rootNode)
    self.obj1031.postAction( rootNode.CREATE )

    self.obj1032=apply_contains(self)
    self.obj1032.isGraphObjectVisual = True

    if(hasattr(self.obj1032, '_setHierarchicalLink')):
      self.obj1032._setHierarchicalLink(False)

    self.obj1032.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(747.5,372.0,self.obj1032)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1032.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1032)
    self.globalAndLocalPostcondition(self.obj1032, rootNode)
    self.obj1032.postAction( rootNode.CREATE )

    self.obj1033=directLink_T(self)
    self.obj1033.isGraphObjectVisual = True

    if(hasattr(self.obj1033, '_setHierarchicalLink')):
      self.obj1033._setHierarchicalLink(False)

    # associationType
    self.obj1033.associationType.setValue('channelNames')

    self.obj1033.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1026.0,326.0,self.obj1033)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1033.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1033)
    self.globalAndLocalPostcondition(self.obj1033, rootNode)
    self.obj1033.postAction( rootNode.CREATE )

    self.obj1034=directLink_T(self)
    self.obj1034.isGraphObjectVisual = True

    if(hasattr(self.obj1034, '_setHierarchicalLink')):
      self.obj1034._setHierarchicalLink(False)

    # associationType
    self.obj1034.associationType.setValue('channelNames')

    self.obj1034.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1013.0,431.0,self.obj1034)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1034.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1034)
    self.globalAndLocalPostcondition(self.obj1034, rootNode)
    self.obj1034.postAction( rootNode.CREATE )

    self.obj1035=directLink_T(self)
    self.obj1035.isGraphObjectVisual = True

    if(hasattr(self.obj1035, '_setHierarchicalLink')):
      self.obj1035._setHierarchicalLink(False)

    # associationType
    self.obj1035.associationType.setValue('channelNames')

    self.obj1035.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(792.0,521.0,self.obj1035)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1035.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1035)
    self.globalAndLocalPostcondition(self.obj1035, rootNode)
    self.obj1035.postAction( rootNode.CREATE )

    self.obj1036=directLink_T(self)
    self.obj1036.isGraphObjectVisual = True

    if(hasattr(self.obj1036, '_setHierarchicalLink')):
      self.obj1036._setHierarchicalLink(False)

    # associationType
    self.obj1036.associationType.setValue('channelNames')

    self.obj1036.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(572.0,531.0,self.obj1036)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1036.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1036)
    self.globalAndLocalPostcondition(self.obj1036, rootNode)
    self.obj1036.postAction( rootNode.CREATE )

    self.obj1037=directLink_S(self)
    self.obj1037.isGraphObjectVisual = True

    if(hasattr(self.obj1037, '_setHierarchicalLink')):
      self.obj1037._setHierarchicalLink(False)

    # associationType
    self.obj1037.associationType.setValue('transitions')

    self.obj1037.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(460.0,83.0,self.obj1037)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1037.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1037)
    self.globalAndLocalPostcondition(self.obj1037, rootNode)
    self.obj1037.postAction( rootNode.CREATE )

    self.obj1038=directLink_S(self)
    self.obj1038.isGraphObjectVisual = True

    if(hasattr(self.obj1038, '_setHierarchicalLink')):
      self.obj1038._setHierarchicalLink(False)

    # associationType
    self.obj1038.associationType.setValue('dest')

    self.obj1038.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(760.0,83.0,self.obj1038)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1038.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1038)
    self.globalAndLocalPostcondition(self.obj1038, rootNode)
    self.obj1038.postAction( rootNode.CREATE )

    self.obj1039=directLink_S(self)
    self.obj1039.isGraphObjectVisual = True

    if(hasattr(self.obj1039, '_setHierarchicalLink')):
      self.obj1039._setHierarchicalLink(False)

    # associationType
    self.obj1039.associationType.setValue('type')

    self.obj1039.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(597.0,124.0,self.obj1039)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1039.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1039)
    self.globalAndLocalPostcondition(self.obj1039, rootNode)
    self.obj1039.postAction( rootNode.CREATE )

    self.obj1040=directLink_S(self)
    self.obj1040.isGraphObjectVisual = True

    if(hasattr(self.obj1040, '_setHierarchicalLink')):
      self.obj1040._setHierarchicalLink(False)

    # associationType
    self.obj1040.associationType.setValue('owningStateMachine')

    self.obj1040.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(850.5,133.0,self.obj1040)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1040.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1040)
    self.globalAndLocalPostcondition(self.obj1040, rootNode)
    self.obj1040.postAction( rootNode.CREATE )

    self.obj1041=hasAttribute_S(self)
    self.obj1041.isGraphObjectVisual = True

    if(hasattr(self.obj1041, '_setHierarchicalLink')):
      self.obj1041._setHierarchicalLink(False)

    self.obj1041.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(674.5,241.5,self.obj1041)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1041.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1041)
    self.globalAndLocalPostcondition(self.obj1041, rootNode)
    self.obj1041.postAction( rootNode.CREATE )

    self.obj1042=hasAttribute_S(self)
    self.obj1042.isGraphObjectVisual = True

    if(hasattr(self.obj1042, '_setHierarchicalLink')):
      self.obj1042._setHierarchicalLink(False)

    self.obj1042.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(912.0,206.5,self.obj1042)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1042.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1042)
    self.globalAndLocalPostcondition(self.obj1042, rootNode)
    self.obj1042.postAction( rootNode.CREATE )

    self.obj1043=hasAttribute_S(self)
    self.obj1043.isGraphObjectVisual = True

    if(hasattr(self.obj1043, '_setHierarchicalLink')):
      self.obj1043._setHierarchicalLink(False)

    self.obj1043.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(317.5,128.5,self.obj1043)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1043.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1043)
    self.globalAndLocalPostcondition(self.obj1043, rootNode)
    self.obj1043.postAction( rootNode.CREATE )

    self.obj1044=hasAttribute_T(self)
    self.obj1044.isGraphObjectVisual = True

    if(hasattr(self.obj1044, '_setHierarchicalLink')):
      self.obj1044._setHierarchicalLink(False)

    self.obj1044.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,330.5,self.obj1044)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1044.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1044)
    self.globalAndLocalPostcondition(self.obj1044, rootNode)
    self.obj1044.postAction( rootNode.CREATE )

    self.obj1045=hasAttribute_T(self)
    self.obj1045.isGraphObjectVisual = True

    if(hasattr(self.obj1045, '_setHierarchicalLink')):
      self.obj1045._setHierarchicalLink(False)

    self.obj1045.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1400.0,424.5,self.obj1045)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1045.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1045)
    self.globalAndLocalPostcondition(self.obj1045, rootNode)
    self.obj1045.postAction( rootNode.CREATE )

    self.obj1046=hasAttribute_T(self)
    self.obj1046.isGraphObjectVisual = True

    if(hasattr(self.obj1046, '_setHierarchicalLink')):
      self.obj1046._setHierarchicalLink(False)

    self.obj1046.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1201.0,519.0,self.obj1046)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1046.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1046)
    self.globalAndLocalPostcondition(self.obj1046, rootNode)
    self.obj1046.postAction( rootNode.CREATE )

    self.obj1047=hasAttribute_T(self)
    self.obj1047.isGraphObjectVisual = True

    if(hasattr(self.obj1047, '_setHierarchicalLink')):
      self.obj1047._setHierarchicalLink(False)

    self.obj1047.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(833.0,592.5,self.obj1047)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1047.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1047)
    self.globalAndLocalPostcondition(self.obj1047, rootNode)
    self.obj1047.postAction( rootNode.CREATE )

    self.obj1048=hasAttribute_T(self)
    self.obj1048.isGraphObjectVisual = True

    if(hasattr(self.obj1048, '_setHierarchicalLink')):
      self.obj1048._setHierarchicalLink(False)

    self.obj1048.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,422.5,self.obj1048)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1048.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1048)
    self.globalAndLocalPostcondition(self.obj1048, rootNode)
    self.obj1048.postAction( rootNode.CREATE )

    self.obj1049=hasAttribute_T(self)
    self.obj1049.isGraphObjectVisual = True

    if(hasattr(self.obj1049, '_setHierarchicalLink')):
      self.obj1049._setHierarchicalLink(False)

    self.obj1049.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,542.5,self.obj1049)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1049.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1049)
    self.globalAndLocalPostcondition(self.obj1049, rootNode)
    self.obj1049.postAction( rootNode.CREATE )

    self.obj1050=leftExpr(self)
    self.obj1050.isGraphObjectVisual = True

    if(hasattr(self.obj1050, '_setHierarchicalLink')):
      self.obj1050._setHierarchicalLink(False)

    self.obj1050.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,176.5,self.obj1050)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1050.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1050)
    self.globalAndLocalPostcondition(self.obj1050, rootNode)
    self.obj1050.postAction( rootNode.CREATE )

    self.obj1051=leftExpr(self)
    self.obj1051.isGraphObjectVisual = True

    if(hasattr(self.obj1051, '_setHierarchicalLink')):
      self.obj1051._setHierarchicalLink(False)

    self.obj1051.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1487.0,309.5,self.obj1051)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1051.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1051)
    self.globalAndLocalPostcondition(self.obj1051, rootNode)
    self.obj1051.postAction( rootNode.CREATE )

    self.obj1052=leftExpr(self)
    self.obj1052.isGraphObjectVisual = True

    if(hasattr(self.obj1052, '_setHierarchicalLink')):
      self.obj1052._setHierarchicalLink(False)

    self.obj1052.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1492.0,454.0,self.obj1052)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1052.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1052)
    self.globalAndLocalPostcondition(self.obj1052, rootNode)
    self.obj1052.postAction( rootNode.CREATE )

    self.obj1053=leftExpr(self)
    self.obj1053.isGraphObjectVisual = True

    if(hasattr(self.obj1053, '_setHierarchicalLink')):
      self.obj1053._setHierarchicalLink(False)

    self.obj1053.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,477.0,self.obj1053)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1053.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1053)
    self.globalAndLocalPostcondition(self.obj1053, rootNode)
    self.obj1053.postAction( rootNode.CREATE )

    self.obj1054=leftExpr(self)
    self.obj1054.isGraphObjectVisual = True

    if(hasattr(self.obj1054, '_setHierarchicalLink')):
      self.obj1054._setHierarchicalLink(False)

    self.obj1054.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(896.0,636.5,self.obj1054)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1054.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1054)
    self.globalAndLocalPostcondition(self.obj1054, rootNode)
    self.obj1054.postAction( rootNode.CREATE )

    self.obj1055=leftExpr(self)
    self.obj1055.isGraphObjectVisual = True

    if(hasattr(self.obj1055, '_setHierarchicalLink')):
      self.obj1055._setHierarchicalLink(False)

    self.obj1055.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(396.0,356.5,self.obj1055)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1055.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1055)
    self.globalAndLocalPostcondition(self.obj1055, rootNode)
    self.obj1055.postAction( rootNode.CREATE )

    self.obj1056=leftExpr(self)
    self.obj1056.isGraphObjectVisual = True

    if(hasattr(self.obj1056, '_setHierarchicalLink')):
      self.obj1056._setHierarchicalLink(False)

    self.obj1056.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(346.0,656.5,self.obj1056)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1056.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1056)
    self.globalAndLocalPostcondition(self.obj1056, rootNode)
    self.obj1056.postAction( rootNode.CREATE )

    self.obj1057=rightExpr(self)
    self.obj1057.isGraphObjectVisual = True

    if(hasattr(self.obj1057, '_setHierarchicalLink')):
      self.obj1057._setHierarchicalLink(False)

    self.obj1057.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(403.5,216.5,self.obj1057)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1057.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1057)
    self.globalAndLocalPostcondition(self.obj1057, rootNode)
    self.obj1057.postAction( rootNode.CREATE )

    self.obj1058=rightExpr(self)
    self.obj1058.isGraphObjectVisual = True

    if(hasattr(self.obj1058, '_setHierarchicalLink')):
      self.obj1058._setHierarchicalLink(False)

    self.obj1058.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1365.0,243.5,self.obj1058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1058)
    self.globalAndLocalPostcondition(self.obj1058, rootNode)
    self.obj1058.postAction( rootNode.CREATE )

    self.obj1059=rightExpr(self)
    self.obj1059.isGraphObjectVisual = True

    if(hasattr(self.obj1059, '_setHierarchicalLink')):
      self.obj1059._setHierarchicalLink(False)

    self.obj1059.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1424.0,534.0,self.obj1059)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1059.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1059)
    self.globalAndLocalPostcondition(self.obj1059, rootNode)
    self.obj1059.postAction( rootNode.CREATE )

    self.obj1060=rightExpr(self)
    self.obj1060.isGraphObjectVisual = True

    if(hasattr(self.obj1060, '_setHierarchicalLink')):
      self.obj1060._setHierarchicalLink(False)

    self.obj1060.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1063.0,412.5,self.obj1060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1060)
    self.globalAndLocalPostcondition(self.obj1060, rootNode)
    self.obj1060.postAction( rootNode.CREATE )

    self.obj1061=rightExpr(self)
    self.obj1061.isGraphObjectVisual = True

    if(hasattr(self.obj1061, '_setHierarchicalLink')):
      self.obj1061._setHierarchicalLink(False)

    self.obj1061.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(796.0,676.5,self.obj1061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1061)
    self.globalAndLocalPostcondition(self.obj1061, rootNode)
    self.obj1061.postAction( rootNode.CREATE )

    self.obj1062=rightExpr(self)
    self.obj1062.isGraphObjectVisual = True

    if(hasattr(self.obj1062, '_setHierarchicalLink')):
      self.obj1062._setHierarchicalLink(False)

    self.obj1062.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(556.0,376.5,self.obj1062)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1062.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1062)
    self.globalAndLocalPostcondition(self.obj1062, rootNode)
    self.obj1062.postAction( rootNode.CREATE )

    self.obj1063=rightExpr(self)
    self.obj1063.isGraphObjectVisual = True

    if(hasattr(self.obj1063, '_setHierarchicalLink')):
      self.obj1063._setHierarchicalLink(False)

    self.obj1063.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(456.0,666.5,self.obj1063)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1063.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1063)
    self.globalAndLocalPostcondition(self.obj1063, rootNode)
    self.obj1063.postAction( rootNode.CREATE )

    self.obj1064=hasArgs(self)
    self.obj1064.isGraphObjectVisual = True

    if(hasattr(self.obj1064, '_setHierarchicalLink')):
      self.obj1064._setHierarchicalLink(False)

    self.obj1064.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(932.0,344.0,self.obj1064)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1064.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1064)
    self.globalAndLocalPostcondition(self.obj1064, rootNode)
    self.obj1064.postAction( rootNode.CREATE )

    self.obj1065=hasArgs(self)
    self.obj1065.isGraphObjectVisual = True

    if(hasattr(self.obj1065, '_setHierarchicalLink')):
      self.obj1065._setHierarchicalLink(False)

    self.obj1065.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1029.0,314.0,self.obj1065)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1065.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1065)
    self.globalAndLocalPostcondition(self.obj1065, rootNode)
    self.obj1065.postAction( rootNode.CREATE )

    self.obj1066=hasArgs(self)
    self.obj1066.isGraphObjectVisual = True

    if(hasattr(self.obj1066, '_setHierarchicalLink')):
      self.obj1066._setHierarchicalLink(False)

    self.obj1066.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(1111.0,312.0,self.obj1066)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1066.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1066)
    self.globalAndLocalPostcondition(self.obj1066, rootNode)
    self.obj1066.postAction( rootNode.CREATE )

    self.obj1067=hasArgs(self)
    self.obj1067.isGraphObjectVisual = True

    if(hasattr(self.obj1067, '_setHierarchicalLink')):
      self.obj1067._setHierarchicalLink(False)

    self.obj1067.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(574.0,334.0,self.obj1067)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1067.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1067)
    self.globalAndLocalPostcondition(self.obj1067, rootNode)
    self.obj1067.postAction( rootNode.CREATE )

    self.obj1068=hasArgs(self)
    self.obj1068.isGraphObjectVisual = True

    if(hasattr(self.obj1068, '_setHierarchicalLink')):
      self.obj1068._setHierarchicalLink(False)

    self.obj1068.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(644.0,324.0,self.obj1068)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1068.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1068)
    self.globalAndLocalPostcondition(self.obj1068, rootNode)
    self.obj1068.postAction( rootNode.CREATE )

    # Connections for obj984 (graphObject_: Obj809) of type MatchModel
    self.drawConnections(
(self.obj984,self.obj1022,[138.0, 51.0, 140.5, 232.0],"true", 2),
(self.obj984,self.obj1023,[138.0, 51.0, 341.0, 33.0],"true", 2),
(self.obj984,self.obj1024,[138.0, 51.0, 370.0, 21.0],"true", 2),
(self.obj984,self.obj1025,[138.0, 51.0, 368.0, 10.0],"true", 2),
(self.obj984,self.obj1026,[138.0, 51.0, 531.0, 8.0],"true", 2),
(self.obj984,self.obj1027,[138.0, 51.0, 374.0, 117.0],"true", 2) )
    # Connections for obj985 (graphObject_: Obj810) of type ApplyModel
    self.drawConnections(
(self.obj985,self.obj1028,[143.0, 413.0, 267.5, 442.0],"true", 2),
(self.obj985,self.obj1029,[143.0, 413.0, 206.5, 532.0],"true", 2),
(self.obj985,self.obj1030,[143.0, 413.0, 667.5, 492.0],"true", 2),
(self.obj985,self.obj1031,[143.0, 413.0, 747.5, 422.0],"true", 2),
(self.obj985,self.obj1032,[143.0, 413.0, 747.5, 372.0],"true", 2) )
    # Connections for obj986 (graphObject_: Obj811) named entrypoint1
    self.drawConnections(
(self.obj986,self.obj1040,[950.0, 83.0, 850.5, 133.0],"true", 2),
(self.obj986,self.obj1042,[950.0, 83.0, 912.0, 206.5],"true", 2) )
    # Connections for obj987 (graphObject_: Obj812) named transition1
    self.drawConnections(
(self.obj987,self.obj1038,[570.0, 83.0, 760.0, 83.0],"true", 2),
(self.obj987,self.obj1039,[570.0, 83.0, 597.0, 124.0],"true", 2) )
    # Connections for obj988 (graphObject_: Obj813) named statemachine1
    self.drawConnections(
(self.obj988,self.obj1041,[790.0, 183.0, 674.5, 241.5],"true", 2) )
    # Connections for obj989 (graphObject_: Obj814) named state1
    self.drawConnections(
(self.obj989,self.obj1037,[350.0, 83.0, 460.0, 83.0],"true", 2),
(self.obj989,self.obj1043,[350.0, 83.0, 317.5, 128.5],"true", 2) )
    # Connections for obj990 (graphObject_: Obj815) named in1_1
    self.drawConnections(
 )
    # Connections for obj991 (graphObject_: Obj816) named name1
    self.drawConnections(
(self.obj991,self.obj1044,[1352.0, 331.0, 1400.0, 330.5],"true", 2) )
    # Connections for obj992 (graphObject_: Obj817) named name2
    self.drawConnections(
(self.obj992,self.obj1045,[1352.0, 431.0, 1400.0, 424.5],"true", 2) )
    # Connections for obj993 (graphObject_: Obj818) named name3
    self.drawConnections(
(self.obj993,self.obj1046,[1192.0, 571.0, 1201.0, 519.0],"true", 2) )
    # Connections for obj994 (graphObject_: Obj819) named name4
    self.drawConnections(
(self.obj994,self.obj1047,[752.0, 591.0, 833.0, 592.5],"true", 2) )
    # Connections for obj995 (graphObject_: Obj820) named inst1
    self.drawConnections(
(self.obj995,self.obj1033,[392.0, 471.0, 1026.0, 326.0],"true", 2),
(self.obj995,self.obj1034,[392.0, 471.0, 1013.0, 431.0],"true", 2),
(self.obj995,self.obj1035,[392.0, 471.0, 792.0, 521.0],"true", 2),
(self.obj995,self.obj1036,[392.0, 471.0, 572.0, 531.0],"true", 2),
(self.obj995,self.obj1048,[392.0, 471.0, 353.0, 422.5],"true", 2),
(self.obj995,self.obj1049,[392.0, 471.0, 353.0, 542.5],"true", 2) )
    # Connections for obj996 (graphObject_: Obj821) named name
    self.drawConnections(
 )
    # Connections for obj997 (graphObject_: Obj822) named name
    self.drawConnections(
 )
    # Connections for obj998 (graphObject_: Obj823) named isComposite
    self.drawConnections(
 )
    # Connections for obj999 (graphObject_: Obj824) named literal
    self.drawConnections(
 )
    # Connections for obj1000 (graphObject_: Obj825) named literal
    self.drawConnections(
 )
    # Connections for obj1001 (graphObject_: Obj826) named literal
    self.drawConnections(
 )
    # Connections for obj1002 (graphObject_: Obj827) named literal
    self.drawConnections(
 )
    # Connections for obj1003 (graphObject_: Obj828) named name
    self.drawConnections(
 )
    # Connections for obj1004 (graphObject_: Obj829) named pivot
    self.drawConnections(
 )
    # Connections for obj1005 (graphObject_: Obj830) named eq1
    self.drawConnections(
(self.obj1005,self.obj1050,[433.0, 179.0, 359.0, 176.5],"true", 2),
(self.obj1005,self.obj1057,[433.0, 179.0, 403.5, 216.5],"true", 2) )
    # Connections for obj1006 (graphObject_: Obj831) named eq2
    self.drawConnections(
(self.obj1006,self.obj1051,[1498.0, 259.0, 1487.0, 309.5],"true", 2),
(self.obj1006,self.obj1058,[1498.0, 259.0, 1365.0, 243.5],"true", 2) )
    # Connections for obj1007 (graphObject_: Obj832) named eq3
    self.drawConnections(
(self.obj1007,self.obj1052,[1498.0, 499.0, 1492.0, 454.0],"true", 2),
(self.obj1007,self.obj1059,[1498.0, 499.0, 1424.0, 534.0],"true", 2) )
    # Connections for obj1008 (graphObject_: Obj833) named eq4
    self.drawConnections(
(self.obj1008,self.obj1053,[1012.0, 488.0, 1100.0, 477.0],"true", 2),
(self.obj1008,self.obj1060,[1012.0, 488.0, 1063.0, 412.5],"true", 2) )
    # Connections for obj1009 (graphObject_: Obj834) named eq5
    self.drawConnections(
(self.obj1009,self.obj1054,[878.0, 679.0, 896.0, 636.5],"true", 2),
(self.obj1009,self.obj1061,[878.0, 679.0, 796.0, 676.5],"true", 2) )
    # Connections for obj1010 (graphObject_: Obj835) named eq6
    self.drawConnections(
(self.obj1010,self.obj1055,[478.0, 379.0, 396.0, 356.5],"true", 2),
(self.obj1010,self.obj1062,[478.0, 379.0, 556.0, 376.5],"true", 2) )
    # Connections for obj1011 (graphObject_: Obj836) named eq7
    self.drawConnections(
(self.obj1011,self.obj1063,[378.0, 699.0, 456.0, 666.5],"true", 2),
(self.obj1011,self.obj1056,[378.0, 699.0, 346.0, 656.5],"true", 2) )
    # Connections for obj1012 (graphObject_: Obj837) named concat1
    self.drawConnections(
(self.obj1012,self.obj1064,[1074.0, 389.0, 932.0, 344.0],"true", 2),
(self.obj1012,self.obj1065,[1074.0, 389.0, 1029.0, 314.0],"true", 2),
(self.obj1012,self.obj1066,[1074.0, 389.0, 1111.0, 312.0],"true", 2) )
    # Connections for obj1013 (graphObject_: Obj838) named concat2
    self.drawConnections(
(self.obj1013,self.obj1067,[634.0, 374.0, 574.0, 334.0],"true", 2),
(self.obj1013,self.obj1068,[634.0, 374.0, 644.0, 324.0],"true", 2) )
    # Connections for obj1014 (graphObject_: Obj839) named true
    self.drawConnections(
 )
    # Connections for obj1015 (graphObject_: Obj840) named exit_in
    self.drawConnections(
 )
    # Connections for obj1016 (graphObject_: Obj841) named exack_in
    self.drawConnections(
 )
    # Connections for obj1017 (graphObject_: Obj842) named 2
    self.drawConnections(
 )
    # Connections for obj1018 (graphObject_: Obj843) named 1
    self.drawConnections(
 )
    # Connections for obj1019 (graphObject_: Obj844) named sh_in
    self.drawConnections(
 )
    # Connections for obj1020 (graphObject_: Obj845) named S
    self.drawConnections(
 )
    # Connections for obj1021 (graphObject_: Obj846) named instForInTrans
    self.drawConnections(
 )
    # Connections for obj1022 (graphObject_: Obj847) of type paired_with
    self.drawConnections(
(self.obj1022,self.obj985,[140.5, 232.0, 143.0, 413.0],"true", 2) )
    # Connections for obj1023 (graphObject_: Obj848) of type match_contains
    self.drawConnections(
(self.obj1023,self.obj989,[341.0, 33.0, 350.0, 83.0],"true", 2) )
    # Connections for obj1024 (graphObject_: Obj849) of type match_contains
    self.drawConnections(
(self.obj1024,self.obj987,[370.0, 21.0, 570.0, 83.0],"true", 2) )
    # Connections for obj1025 (graphObject_: Obj850) of type match_contains
    self.drawConnections(
(self.obj1025,self.obj986,[368.0, 10.0, 950.0, 83.0],"true", 2) )
    # Connections for obj1026 (graphObject_: Obj851) of type match_contains
    self.drawConnections(
(self.obj1026,self.obj988,[531.0, 8.0, 790.0, 183.0],"true", 2) )
    # Connections for obj1027 (graphObject_: Obj852) of type match_contains
    self.drawConnections(
(self.obj1027,self.obj990,[374.0, 117.0, 610.0, 183.0],"true", 2) )
    # Connections for obj1028 (graphObject_: Obj853) of type apply_contains
    self.drawConnections(
(self.obj1028,self.obj995,[267.5, 442.0, 392.0, 471.0],"true", 2) )
    # Connections for obj1029 (graphObject_: Obj854) of type apply_contains
    self.drawConnections(
(self.obj1029,self.obj994,[206.5, 532.0, 752.0, 591.0],"true", 2) )
    # Connections for obj1030 (graphObject_: Obj855) of type apply_contains
    self.drawConnections(
(self.obj1030,self.obj993,[667.5, 492.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj1031 (graphObject_: Obj856) of type apply_contains
    self.drawConnections(
(self.obj1031,self.obj992,[747.5, 422.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj1032 (graphObject_: Obj857) of type apply_contains
    self.drawConnections(
(self.obj1032,self.obj991,[747.5, 372.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj1033 (graphObject_: Obj858) of type directLink_T
    self.drawConnections(
(self.obj1033,self.obj991,[1026.0, 326.0, 1352.0, 331.0],"true", 2) )
    # Connections for obj1034 (graphObject_: Obj859) of type directLink_T
    self.drawConnections(
(self.obj1034,self.obj992,[1013.0, 431.0, 1352.0, 431.0],"true", 2) )
    # Connections for obj1035 (graphObject_: Obj860) of type directLink_T
    self.drawConnections(
(self.obj1035,self.obj993,[792.0, 521.0, 1192.0, 571.0],"true", 2) )
    # Connections for obj1036 (graphObject_: Obj861) of type directLink_T
    self.drawConnections(
(self.obj1036,self.obj994,[572.0, 531.0, 752.0, 591.0],"true", 2) )
    # Connections for obj1037 (graphObject_: Obj862) of type directLink_S
    self.drawConnections(
(self.obj1037,self.obj987,[460.0, 83.0, 570.0, 83.0],"true", 2) )
    # Connections for obj1038 (graphObject_: Obj863) of type directLink_S
    self.drawConnections(
(self.obj1038,self.obj986,[760.0, 83.0, 950.0, 83.0],"true", 2) )
    # Connections for obj1039 (graphObject_: Obj864) of type directLink_S
    self.drawConnections(
(self.obj1039,self.obj990,[597.0, 124.0, 610.0, 183.0],"true", 2) )
    # Connections for obj1040 (graphObject_: Obj865) of type directLink_S
    self.drawConnections(
(self.obj1040,self.obj988,[850.5, 133.0, 790.0, 183.0],"true", 2) )
    # Connections for obj1041 (graphObject_: Obj866) of type hasAttribute_S
    self.drawConnections(
(self.obj1041,self.obj997,[674.5, 241.5, 674.0, 274.0],"true", 2) )
    # Connections for obj1042 (graphObject_: Obj867) of type hasAttribute_S
    self.drawConnections(
(self.obj1042,self.obj996,[912.0, 206.5, 994.0, 254.0],"true", 2) )
    # Connections for obj1043 (graphObject_: Obj868) of type hasAttribute_S
    self.drawConnections(
(self.obj1043,self.obj998,[317.5, 128.5, 285.0, 174.0],"true", 2) )
    # Connections for obj1044 (graphObject_: Obj869) of type hasAttribute_T
    self.drawConnections(
(self.obj1044,self.obj999,[1400.0, 330.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj1045 (graphObject_: Obj870) of type hasAttribute_T
    self.drawConnections(
(self.obj1045,self.obj1000,[1400.0, 424.5, 1494.0, 414.0],"true", 2) )
    # Connections for obj1046 (graphObject_: Obj871) of type hasAttribute_T
    self.drawConnections(
(self.obj1046,self.obj1001,[1201.0, 519.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj1047 (graphObject_: Obj872) of type hasAttribute_T
    self.drawConnections(
(self.obj1047,self.obj1002,[833.0, 592.5, 914.0, 594.0],"true", 2) )
    # Connections for obj1048 (graphObject_: Obj873) of type hasAttribute_T
    self.drawConnections(
(self.obj1048,self.obj1003,[353.0, 422.5, 314.0, 374.0],"true", 2) )
    # Connections for obj1049 (graphObject_: Obj874) of type hasAttribute_T
    self.drawConnections(
(self.obj1049,self.obj1004,[353.0, 542.5, 314.0, 614.0],"true", 2) )
    # Connections for obj1050 (graphObject_: Obj875) of type leftExpr
    self.drawConnections(
(self.obj1050,self.obj998,[359.0, 176.5, 285.0, 174.0],"true", 2) )
    # Connections for obj1051 (graphObject_: Obj876) of type leftExpr
    self.drawConnections(
(self.obj1051,self.obj999,[1487.0, 309.5, 1494.0, 334.0],"true", 2) )
    # Connections for obj1052 (graphObject_: Obj877) of type leftExpr
    self.drawConnections(
(self.obj1052,self.obj1000,[1492.0, 454.0, 1494.0, 414.0],"true", 2) )
    # Connections for obj1053 (graphObject_: Obj878) of type leftExpr
    self.drawConnections(
(self.obj1053,self.obj1001,[1100.0, 477.0, 1154.0, 474.0],"true", 2) )
    # Connections for obj1054 (graphObject_: Obj879) of type leftExpr
    self.drawConnections(
(self.obj1054,self.obj1002,[896.0, 636.5, 914.0, 594.0],"true", 2) )
    # Connections for obj1055 (graphObject_: Obj880) of type leftExpr
    self.drawConnections(
(self.obj1055,self.obj1003,[396.0, 356.5, 314.0, 374.0],"true", 2) )
    # Connections for obj1056 (graphObject_: Obj881) of type leftExpr
    self.drawConnections(
(self.obj1056,self.obj1004,[346.0, 656.5, 314.0, 614.0],"true", 2) )
    # Connections for obj1057 (graphObject_: Obj882) of type rightExpr
    self.drawConnections(
(self.obj1057,self.obj1014,[403.5, 216.5, 374.0, 254.0],"true", 2) )
    # Connections for obj1058 (graphObject_: Obj883) of type rightExpr
    self.drawConnections(
(self.obj1058,self.obj1015,[1365.0, 243.5, 1334.0, 241.0],"true", 2) )
    # Connections for obj1059 (graphObject_: Obj884) of type rightExpr
    self.drawConnections(
(self.obj1059,self.obj1016,[1424.0, 534.0, 1354.0, 514.0],"true", 2) )
    # Connections for obj1060 (graphObject_: Obj885) of type rightExpr
    self.drawConnections(
(self.obj1060,self.obj1012,[1063.0, 412.5, 1074.0, 389.0],"true", 2) )
    # Connections for obj1061 (graphObject_: Obj886) of type rightExpr
    self.drawConnections(
(self.obj1061,self.obj1019,[796.0, 676.5, 714.0, 674.0],"true", 2) )
    # Connections for obj1062 (graphObject_: Obj887) of type rightExpr
    self.drawConnections(
(self.obj1062,self.obj1013,[556.0, 376.5, 634.0, 374.0],"true", 2) )
    # Connections for obj1063 (graphObject_: Obj888) of type rightExpr
    self.drawConnections(
(self.obj1063,self.obj1021,[456.0, 666.5, 485.0, 614.0],"true", 2) )
    # Connections for obj1064 (graphObject_: Obj889) of type hasArgs
    self.drawConnections(
(self.obj1064,self.obj1018,[932.0, 344.0, 854.0, 314.0],"true", 2) )
    # Connections for obj1065 (graphObject_: Obj890) of type hasArgs
    self.drawConnections(
(self.obj1065,self.obj996,[1029.0, 314.0, 994.0, 254.0],"true", 2) )
    # Connections for obj1066 (graphObject_: Obj891) of type hasArgs
    self.drawConnections(
(self.obj1066,self.obj1017,[1111.0, 312.0, 1142.0, 234.0],"true", 2) )
    # Connections for obj1067 (graphObject_: Obj892) of type hasArgs
    self.drawConnections(
(self.obj1067,self.obj1020,[574.0, 334.0, 514.0, 294.0],"true", 2) )
    # Connections for obj1068 (graphObject_: Obj893) of type hasArgs
    self.drawConnections(
(self.obj1068,self.obj997,[644.0, 324.0, 674.0, 274.0],"true", 2) )

newfunction = Transition2Inst_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
