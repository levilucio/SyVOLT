"""
__Transition2QInstOUT_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Feb  9 21:46:36 2015
_________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from Vertex import *
from Transition import *
from StateMachine import *
from OUT2 import *
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
from graph_Equation import *
from graph_hasArgs import *
from graph_rightExpr import *
from graph_Concat import *
from graph_Inst import *
from graph_hasAttribute_T import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_OUT2 import *
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

def Transition2QInstOUT_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('Transition2QInstOUT')
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
       new_obj = graph_ApplyModel(20.0,240.0,self.obj101)
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

    self.obj102=Vertex(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # name
    self.obj102.name.setValue('vertex1')

    # classtype
    self.obj102.classtype.setValue('Vertex')

    # cardinality
    self.obj102.cardinality.setValue('1')

    self.obj102.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,120.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
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
       new_obj = graph_Transition(160.0,34.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.9699999999999989, 0.8599999999999994]
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
       new_obj = graph_StateMachine(660.0,25.0,self.obj104)
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

    self.obj105=OUT2(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # classtype
    self.obj105.classtype.setValue('OUT2')

    # cardinality
    self.obj105.cardinality.setValue('1')

    # name
    self.obj105.name.setValue('out2_1')

    self.obj105.graphClass_= graph_OUT2
    if self.genGraphics:
       new_obj = graph_OUT2(160.0,121.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Name(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # classtype
    self.obj106.classtype.setValue('Name')

    # cardinality
    self.obj106.cardinality.setValue('1')

    # name
    self.obj106.name.setValue('name1')

    self.obj106.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(600.0,380.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=Inst(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # classtype
    self.obj107.classtype.setValue('Inst')

    # cardinality
    self.obj107.cardinality.setValue('1')

    # name
    self.obj107.name.setValue('inst1')

    self.obj107.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(200.0,380.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=Attribute(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # Type
    self.obj108.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj108.Type.config = 0

    # name
    self.obj108.name.setValue('name')

    self.obj108.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(420.0,127.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=Attribute(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # Type
    self.obj109.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj109.Type.config = 0

    # name
    self.obj109.name.setValue('literal')

    self.obj109.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,372.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Attribute(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # Type
    self.obj110.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj110.Type.config = 0

    # name
    self.obj110.name.setValue('name')

    self.obj110.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(240.0,280.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Attribute(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # Type
    self.obj111.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj111.Type.config = 0

    # name
    self.obj111.name.setValue('pivot')

    self.obj111.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,500.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=Equation(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # name
    self.obj112.name.setValue('eq2')

    self.obj112.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,300.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=Equation(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # name
    self.obj113.name.setValue('eq1')

    self.obj113.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(540.0,280.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Equation(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # name
    self.obj114.name.setValue('eq3')

    self.obj114.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,520.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Concat(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # Type
    self.obj115.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj115.Type.config = 0

    # name
    self.obj115.name.setValue('concat1')

    self.obj115.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(520.0,200.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=Constant(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # Type
    self.obj116.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj116.Type.config = 0

    # name
    self.obj116.name.setValue('sh')

    self.obj116.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(860.0,440.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=Constant(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # Type
    self.obj117.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj117.Type.config = 0

    # name
    self.obj117.name.setValue('B')

    self.obj117.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(363.0,200.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=Constant(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # Type
    self.obj118.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj118.Type.config = 0

    # name
    self.obj118.name.setValue('instfortrans')

    self.obj118.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(400.0,480.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=paired_with(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    self.obj119.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=match_contains(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    self.obj120.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(238.0,60.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=match_contains(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    self.obj121.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,117.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=match_contains(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    self.obj122.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(465.0,50.5,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=match_contains(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    self.obj123.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,107.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=apply_contains(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    self.obj124.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(149.5,358.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=apply_contains(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    self.obj125.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(179.5,347.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=directLink_T(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # associationType
    self.obj126.associationType.setValue('channelNames')

    self.obj126.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(517.0,430.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=directLink_S(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # associationType
    self.obj127.associationType.setValue('type')

    self.obj127.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(330.0,133.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=directLink_S(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # associationType
    self.obj128.associationType.setValue('owningStateMachine')

    self.obj128.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(577.242375062,73.1510372393,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=directLink_S(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # associationType
    self.obj129.associationType.setValue('exitPoints')

    self.obj129.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(859.0,103.5,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=directLink_S(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # associationType
    self.obj130.associationType.setValue('dest')

    self.obj130.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(621.242375062,102.151037239,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=hasAttribute_S(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    self.obj131.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(692.0,158.5,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=hasAttribute_T(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    self.obj132.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(843.0,418.5,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=hasAttribute_T(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    self.obj133.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(363.0,392.5,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=hasAttribute_T(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    self.obj134.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(303.0,482.5,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=leftExpr(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    self.obj135.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(936.0,372.5,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=leftExpr(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    self.obj136.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(526.0,316.5,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=leftExpr(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    self.obj137.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,549.5,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=rightExpr(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    self.obj138.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(976.0,406.5,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=rightExpr(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    self.obj139.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(666.0,276.5,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=rightExpr(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    self.obj140.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(445.0,539.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=hasArgs(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    self.obj141.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(584.0,234.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=hasArgs(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(604.0,194.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    # Connections for obj100 (graphObject_: Obj0) of type MatchModel
    self.drawConnections(
(self.obj100,self.obj119,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj100,self.obj120,[138.0, 51.0, 238.0, 60.0],"true", 2),
(self.obj100,self.obj121,[138.0, 51.0, 234.0, 117.0],"true", 2),
(self.obj100,self.obj122,[138.0, 51.0, 465.0, 50.5],"true", 2),
(self.obj100,self.obj123,[138.0, 51.0, 484.0, 107.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj1) of type ApplyModel
    self.drawConnections(
(self.obj101,self.obj124,[143.0, 273.0, 149.5, 358.0],"true", 2),
(self.obj101,self.obj125,[143.0, 273.0, 179.5, 347.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj2) named vertex1
    self.drawConnections(
(self.obj102,self.obj131,[830.0, 163.0, 692.0, 158.5],"true", 2) )
    # Connections for obj103 (graphObject_: Obj3) named transition1
    self.drawConnections(
(self.obj103,self.obj127,[324.4847501237708, 71.30207447863364, 330.0, 133.0],"true", 2),
(self.obj103,self.obj128,[324.4847501237708, 71.30207447863364, 577.2423750618855, 73.15103723931682],"true", 2),
(self.obj103,self.obj130,[324.4847501237708, 71.30207447863364, 621.2423750618855, 102.15103723931682],"true", 2) )
    # Connections for obj104 (graphObject_: Obj4) named statemachine1
    self.drawConnections(
(self.obj104,self.obj129,[830.0, 68.0, 859.0, 103.5],"true", 2) )
    # Connections for obj105 (graphObject_: Obj5) named out2_1
    self.drawConnections(
 )
    # Connections for obj106 (graphObject_: Obj6) named name1
    self.drawConnections(
(self.obj106,self.obj132,[772.0, 431.0, 843.0, 418.5],"true", 2) )
    # Connections for obj107 (graphObject_: Obj7) named inst1
    self.drawConnections(
(self.obj107,self.obj126,[372.0, 431.0, 517.0, 430.0],"true", 2),
(self.obj107,self.obj133,[372.0, 431.0, 363.0, 392.5],"true", 2),
(self.obj107,self.obj134,[372.0, 431.0, 303.0, 482.5],"true", 2) )
    # Connections for obj108 (graphObject_: Obj8) named name
    self.drawConnections(
 )
    # Connections for obj109 (graphObject_: Obj9) named literal
    self.drawConnections(
 )
    # Connections for obj110 (graphObject_: Obj10) named name
    self.drawConnections(
 )
    # Connections for obj111 (graphObject_: Obj11) named pivot
    self.drawConnections(
 )
    # Connections for obj112 (graphObject_: Obj12) named eq2
    self.drawConnections(
(self.obj112,self.obj135,[958.0, 339.0, 936.0, 372.5],"true", 2),
(self.obj112,self.obj138,[958.0, 339.0, 976.0, 406.5],"true", 2) )
    # Connections for obj113 (graphObject_: Obj13) named eq1
    self.drawConnections(
(self.obj113,self.obj136,[678.0, 319.0, 526.0, 316.5],"true", 2),
(self.obj113,self.obj139,[678.0, 319.0, 666.0, 276.5],"true", 2) )
    # Connections for obj114 (graphObject_: Obj14) named eq3
    self.drawConnections(
(self.obj114,self.obj137,[378.0, 559.0, 316.0, 549.5],"true", 2),
(self.obj114,self.obj140,[378.0, 559.0, 445.0, 539.0],"true", 2) )
    # Connections for obj115 (graphObject_: Obj15) named concat1
    self.drawConnections(
(self.obj115,self.obj141,[654.0, 234.0, 584.0, 234.0],"true", 2),
(self.obj115,self.obj142,[654.0, 234.0, 604.0, 194.0],"true", 2) )
    # Connections for obj116 (graphObject_: Obj16) named sh
    self.drawConnections(
 )
    # Connections for obj117 (graphObject_: Obj17) named B
    self.drawConnections(
 )
    # Connections for obj118 (graphObject_: Obj18) named instfortrans
    self.drawConnections(
 )
    # Connections for obj119 (graphObject_: Obj19) of type paired_with
    self.drawConnections(
(self.obj119,self.obj101,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj20) of type match_contains
    self.drawConnections(
(self.obj120,self.obj103,[234.0, 67.0, 324.4847501237708, 71.30207447863364],"true", 2) )
    # Connections for obj121 (graphObject_: Obj21) of type match_contains
    self.drawConnections(
(self.obj121,self.obj105,[234.0, 117.0, 330.0, 164.0],"true", 2) )
    # Connections for obj122 (graphObject_: Obj22) of type match_contains
    self.drawConnections(
(self.obj122,self.obj104,[465.0, 50.5, 830.0, 68.0],"true", 2) )
    # Connections for obj123 (graphObject_: Obj23) of type match_contains
    self.drawConnections(
(self.obj123,self.obj102,[484.0, 107.0, 830.0, 163.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj24) of type apply_contains
    self.drawConnections(
(self.obj124,self.obj107,[149.5, 358.0, 372.0, 431.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj25) of type apply_contains
    self.drawConnections(
(self.obj125,self.obj106,[179.5, 347.0, 772.0, 431.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj26) of type directLink_T
    self.drawConnections(
(self.obj126,self.obj106,[517.0, 430.0, 772.0, 431.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj27) of type directLink_S
    self.drawConnections(
(self.obj127,self.obj105,[330.0, 133.0, 330.0, 164.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj28) of type directLink_S
    self.drawConnections(
(self.obj128,self.obj104,[577.2423750618855, 73.15103723931682, 830.0, 68.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj29) of type directLink_S
    self.drawConnections(
(self.obj129,self.obj102,[859.0, 103.5, 830.0, 163.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj30) of type directLink_S
    self.drawConnections(
(self.obj130,self.obj102,[621.2423750618855, 102.15103723931682, 830.0, 163.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj31) of type hasAttribute_S
    self.drawConnections(
(self.obj131,self.obj108,[692.0, 158.5, 554.0, 161.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj32) of type hasAttribute_T
    self.drawConnections(
(self.obj132,self.obj109,[843.0, 418.5, 914.0, 406.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj33) of type hasAttribute_T
    self.drawConnections(
(self.obj133,self.obj110,[363.0, 392.5, 374.0, 314.0],"true", 2) )
    # Connections for obj134 (graphObject_: Obj34) of type hasAttribute_T
    self.drawConnections(
(self.obj134,self.obj111,[303.0, 482.5, 194.0, 534.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj35) of type leftExpr
    self.drawConnections(
(self.obj135,self.obj109,[936.0, 372.5, 914.0, 406.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj36) of type leftExpr
    self.drawConnections(
(self.obj136,self.obj110,[526.0, 316.5, 374.0, 314.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj37) of type leftExpr
    self.drawConnections(
(self.obj137,self.obj111,[316.0, 549.5, 194.0, 534.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj38) of type rightExpr
    self.drawConnections(
(self.obj138,self.obj116,[976.0, 406.5, 994.0, 474.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj39) of type rightExpr
    self.drawConnections(
(self.obj139,self.obj115,[666.0, 276.5, 654.0, 234.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj40) of type rightExpr
    self.drawConnections(
(self.obj140,self.obj118,[445.0, 539.0, 534.0, 514.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj41) of type hasArgs
    self.drawConnections(
(self.obj141,self.obj117,[584.0, 234.0, 497.0, 234.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj42) of type hasArgs
    self.drawConnections(
(self.obj142,self.obj108,[604.0, 194.0, 554.0, 161.0],"true", 2) )

newfunction = Transition2QInstOUT_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
