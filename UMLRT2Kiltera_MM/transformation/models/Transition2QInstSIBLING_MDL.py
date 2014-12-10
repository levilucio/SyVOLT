"""
__Transition2QInstSIBLING_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 15:04:28 2014
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


    self.obj1507=MatchModel(self)
    self.obj1507.isGraphObjectVisual = True

    if(hasattr(self.obj1507, '_setHierarchicalLink')):
      self.obj1507._setHierarchicalLink(False)

    self.obj1507.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1507)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1507.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1507)
    self.globalAndLocalPostcondition(self.obj1507, rootNode)
    self.obj1507.postAction( rootNode.CREATE )

    self.obj1508=ApplyModel(self)
    self.obj1508.isGraphObjectVisual = True

    if(hasattr(self.obj1508, '_setHierarchicalLink')):
      self.obj1508._setHierarchicalLink(False)

    self.obj1508.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,368.0,self.obj1508)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, -3.0]
    else: new_obj = None
    self.obj1508.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1508)
    self.globalAndLocalPostcondition(self.obj1508, rootNode)
    self.obj1508.postAction( rootNode.CREATE )

    self.obj1509=Vertex(self)
    self.obj1509.isGraphObjectVisual = True

    if(hasattr(self.obj1509, '_setHierarchicalLink')):
      self.obj1509._setHierarchicalLink(False)

    # name
    self.obj1509.name.setValue('vertex1')

    # classtype
    self.obj1509.classtype.setValue('Vertex')

    # cardinality
    self.obj1509.cardinality.setValue('1')

    self.obj1509.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(740.0,40.0,self.obj1509)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1509.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1509)
    self.globalAndLocalPostcondition(self.obj1509, rootNode)
    self.obj1509.postAction( rootNode.CREATE )

    self.obj1510=Transition(self)
    self.obj1510.isGraphObjectVisual = True

    if(hasattr(self.obj1510, '_setHierarchicalLink')):
      self.obj1510._setHierarchicalLink(False)

    # name
    self.obj1510.name.setValue('transition1')

    # classtype
    self.obj1510.classtype.setValue('Transition')

    # cardinality
    self.obj1510.cardinality.setValue('+')

    self.obj1510.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(180.0,40.0,self.obj1510)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1510.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1510)
    self.globalAndLocalPostcondition(self.obj1510, rootNode)
    self.obj1510.postAction( rootNode.CREATE )

    self.obj1511=StateMachine(self)
    self.obj1511.isGraphObjectVisual = True

    if(hasattr(self.obj1511, '_setHierarchicalLink')):
      self.obj1511._setHierarchicalLink(False)

    # name
    self.obj1511.name.setValue('stateMachine1')

    # classtype
    self.obj1511.classtype.setValue('StateMachine')

    # cardinality
    self.obj1511.cardinality.setValue('1')

    self.obj1511.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(460.0,100.0,self.obj1511)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1511.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1511)
    self.globalAndLocalPostcondition(self.obj1511, rootNode)
    self.obj1511.postAction( rootNode.CREATE )

    self.obj1512=SIBLING0(self)
    self.obj1512.isGraphObjectVisual = True

    if(hasattr(self.obj1512, '_setHierarchicalLink')):
      self.obj1512._setHierarchicalLink(False)

    # classtype
    self.obj1512.classtype.setValue('SIBLING0')

    # cardinality
    self.obj1512.cardinality.setValue('1')

    # name
    self.obj1512.name.setValue('sibling0_1')

    self.obj1512.graphClass_= graph_SIBLING0
    if self.genGraphics:
       new_obj = graph_SIBLING0(180.0,160.0,self.obj1512)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SIBLING0", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1512.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1512)
    self.globalAndLocalPostcondition(self.obj1512, rootNode)
    self.obj1512.postAction( rootNode.CREATE )

    self.obj1513=Name(self)
    self.obj1513.isGraphObjectVisual = True

    if(hasattr(self.obj1513, '_setHierarchicalLink')):
      self.obj1513._setHierarchicalLink(False)

    # classtype
    self.obj1513.classtype.setValue('Name')

    # cardinality
    self.obj1513.cardinality.setValue('1')

    # name
    self.obj1513.name.setValue('name1')

    self.obj1513.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(978.0,480.0,self.obj1513)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1513.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1513)
    self.globalAndLocalPostcondition(self.obj1513, rootNode)
    self.obj1513.postAction( rootNode.CREATE )

    self.obj1514=Name(self)
    self.obj1514.isGraphObjectVisual = True

    if(hasattr(self.obj1514, '_setHierarchicalLink')):
      self.obj1514._setHierarchicalLink(False)

    # classtype
    self.obj1514.classtype.setValue('Name')

    # cardinality
    self.obj1514.cardinality.setValue('1')

    # name
    self.obj1514.name.setValue('name2')

    self.obj1514.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(796.0,540.0,self.obj1514)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 13.0]
    else: new_obj = None
    self.obj1514.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1514)
    self.globalAndLocalPostcondition(self.obj1514, rootNode)
    self.obj1514.postAction( rootNode.CREATE )

    self.obj1515=Name(self)
    self.obj1515.isGraphObjectVisual = True

    if(hasattr(self.obj1515, '_setHierarchicalLink')):
      self.obj1515._setHierarchicalLink(False)

    # classtype
    self.obj1515.classtype.setValue('Name')

    # cardinality
    self.obj1515.cardinality.setValue('1')

    # name
    self.obj1515.name.setValue('name3')

    self.obj1515.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(615.0,590.0,self.obj1515)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1515.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1515)
    self.globalAndLocalPostcondition(self.obj1515, rootNode)
    self.obj1515.postAction( rootNode.CREATE )

    self.obj1516=Name(self)
    self.obj1516.isGraphObjectVisual = True

    if(hasattr(self.obj1516, '_setHierarchicalLink')):
      self.obj1516._setHierarchicalLink(False)

    # classtype
    self.obj1516.classtype.setValue('Name')

    # cardinality
    self.obj1516.cardinality.setValue('1')

    # name
    self.obj1516.name.setValue('name4')

    self.obj1516.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(434.0,610.0,self.obj1516)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1516.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1516)
    self.globalAndLocalPostcondition(self.obj1516, rootNode)
    self.obj1516.postAction( rootNode.CREATE )

    self.obj1517=Inst(self)
    self.obj1517.isGraphObjectVisual = True

    if(hasattr(self.obj1517, '_setHierarchicalLink')):
      self.obj1517._setHierarchicalLink(False)

    # classtype
    self.obj1517.classtype.setValue('Inst')

    # cardinality
    self.obj1517.cardinality.setValue('1')

    # name
    self.obj1517.name.setValue('inst1')

    self.obj1517.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(160.0,480.0,self.obj1517)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, 0.0]
    else: new_obj = None
    self.obj1517.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1517)
    self.globalAndLocalPostcondition(self.obj1517, rootNode)
    self.obj1517.postAction( rootNode.CREATE )

    self.obj1518=Attribute(self)
    self.obj1518.isGraphObjectVisual = True

    if(hasattr(self.obj1518, '_setHierarchicalLink')):
      self.obj1518._setHierarchicalLink(False)

    # Type
    self.obj1518.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1518.Type.config = 0

    # name
    self.obj1518.name.setValue('name')

    self.obj1518.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(760.0,160.0,self.obj1518)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1518.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1518)
    self.globalAndLocalPostcondition(self.obj1518, rootNode)
    self.obj1518.postAction( rootNode.CREATE )

    self.obj1519=Attribute(self)
    self.obj1519.isGraphObjectVisual = True

    if(hasattr(self.obj1519, '_setHierarchicalLink')):
      self.obj1519._setHierarchicalLink(False)

    # Type
    self.obj1519.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1519.Type.config = 0

    # name
    self.obj1519.name.setValue('name')

    self.obj1519.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,192.0,self.obj1519)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 3.0]
    else: new_obj = None
    self.obj1519.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1519)
    self.globalAndLocalPostcondition(self.obj1519, rootNode)
    self.obj1519.postAction( rootNode.CREATE )

    self.obj1520=Attribute(self)
    self.obj1520.isGraphObjectVisual = True

    if(hasattr(self.obj1520, '_setHierarchicalLink')):
      self.obj1520._setHierarchicalLink(False)

    # Type
    self.obj1520.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1520.Type.config = 0

    # name
    self.obj1520.name.setValue('name')

    self.obj1520.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(220.0,400.0,self.obj1520)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 2.0]
    else: new_obj = None
    self.obj1520.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1520)
    self.globalAndLocalPostcondition(self.obj1520, rootNode)
    self.obj1520.postAction( rootNode.CREATE )

    self.obj1521=Attribute(self)
    self.obj1521.isGraphObjectVisual = True

    if(hasattr(self.obj1521, '_setHierarchicalLink')):
      self.obj1521._setHierarchicalLink(False)

    # Type
    self.obj1521.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1521.Type.config = 0

    # name
    self.obj1521.name.setValue('literal')

    self.obj1521.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(975.0,593.0,self.obj1521)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [3.0, -1.0]
    else: new_obj = None
    self.obj1521.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1521)
    self.globalAndLocalPostcondition(self.obj1521, rootNode)
    self.obj1521.postAction( rootNode.CREATE )

    self.obj1522=Attribute(self)
    self.obj1522.isGraphObjectVisual = True

    if(hasattr(self.obj1522, '_setHierarchicalLink')):
      self.obj1522._setHierarchicalLink(False)

    # Type
    self.obj1522.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1522.Type.config = 0

    # name
    self.obj1522.name.setValue('literal')

    self.obj1522.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(800.0,646.0,self.obj1522)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj1522.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1522)
    self.globalAndLocalPostcondition(self.obj1522, rootNode)
    self.obj1522.postAction( rootNode.CREATE )

    self.obj1523=Attribute(self)
    self.obj1523.isGraphObjectVisual = True

    if(hasattr(self.obj1523, '_setHierarchicalLink')):
      self.obj1523._setHierarchicalLink(False)

    # Type
    self.obj1523.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1523.Type.config = 0

    # name
    self.obj1523.name.setValue('literal')

    self.obj1523.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,420.0,self.obj1523)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1523.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1523)
    self.globalAndLocalPostcondition(self.obj1523, rootNode)
    self.obj1523.postAction( rootNode.CREATE )

    self.obj1524=Attribute(self)
    self.obj1524.isGraphObjectVisual = True

    if(hasattr(self.obj1524, '_setHierarchicalLink')):
      self.obj1524._setHierarchicalLink(False)

    # Type
    self.obj1524.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1524.Type.config = 0

    # name
    self.obj1524.name.setValue('literal')

    self.obj1524.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(429.0,711.0,self.obj1524)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1524.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1524)
    self.globalAndLocalPostcondition(self.obj1524, rootNode)
    self.obj1524.postAction( rootNode.CREATE )

    self.obj1525=Attribute(self)
    self.obj1525.isGraphObjectVisual = True

    if(hasattr(self.obj1525, '_setHierarchicalLink')):
      self.obj1525._setHierarchicalLink(False)

    # Type
    self.obj1525.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1525.Type.config = 0

    # name
    self.obj1525.name.setValue('pivotout')

    self.obj1525.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(20.0,560.0,self.obj1525)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1525.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1525)
    self.globalAndLocalPostcondition(self.obj1525, rootNode)
    self.obj1525.postAction( rootNode.CREATE )

    self.obj1526=Equation(self)
    self.obj1526.isGraphObjectVisual = True

    if(hasattr(self.obj1526, '_setHierarchicalLink')):
      self.obj1526._setHierarchicalLink(False)

    # name
    self.obj1526.name.setValue('eq1')

    self.obj1526.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(226.0,327.0,self.obj1526)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, 6.0]
    else: new_obj = None
    self.obj1526.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1526)
    self.globalAndLocalPostcondition(self.obj1526, rootNode)
    self.obj1526.postAction( rootNode.CREATE )

    self.obj1527=Equation(self)
    self.obj1527.isGraphObjectVisual = True

    if(hasattr(self.obj1527, '_setHierarchicalLink')):
      self.obj1527._setHierarchicalLink(False)

    # name
    self.obj1527.name.setValue('eq2')

    self.obj1527.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1147.0,594.0,self.obj1527)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-7.0, 3.0]
    else: new_obj = None
    self.obj1527.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1527)
    self.globalAndLocalPostcondition(self.obj1527, rootNode)
    self.obj1527.postAction( rootNode.CREATE )

    self.obj1528=Equation(self)
    self.obj1528.isGraphObjectVisual = True

    if(hasattr(self.obj1528, '_setHierarchicalLink')):
      self.obj1528._setHierarchicalLink(False)

    # name
    self.obj1528.name.setValue('eq3')

    self.obj1528.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(975.0,683.0,self.obj1528)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1528.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1528)
    self.globalAndLocalPostcondition(self.obj1528, rootNode)
    self.obj1528.postAction( rootNode.CREATE )

    self.obj1529=Equation(self)
    self.obj1529.isGraphObjectVisual = True

    if(hasattr(self.obj1529, '_setHierarchicalLink')):
      self.obj1529._setHierarchicalLink(False)

    # name
    self.obj1529.name.setValue('eq4')

    self.obj1529.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(788.0,428.0,self.obj1529)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [0.0, -1.0]
    else: new_obj = None
    self.obj1529.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1529)
    self.globalAndLocalPostcondition(self.obj1529, rootNode)
    self.obj1529.postAction( rootNode.CREATE )

    self.obj1530=Equation(self)
    self.obj1530.isGraphObjectVisual = True

    if(hasattr(self.obj1530, '_setHierarchicalLink')):
      self.obj1530._setHierarchicalLink(False)

    # name
    self.obj1530.name.setValue('eq5')

    self.obj1530.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(264.0,724.0,self.obj1530)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1530.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1530)
    self.globalAndLocalPostcondition(self.obj1530, rootNode)
    self.obj1530.postAction( rootNode.CREATE )

    self.obj1531=Equation(self)
    self.obj1531.isGraphObjectVisual = True

    if(hasattr(self.obj1531, '_setHierarchicalLink')):
      self.obj1531._setHierarchicalLink(False)

    # name
    self.obj1531.name.setValue('eq6')

    self.obj1531.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(180.0,580.0,self.obj1531)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1531.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1531)
    self.globalAndLocalPostcondition(self.obj1531, rootNode)
    self.obj1531.postAction( rootNode.CREATE )

    self.obj1532=Concat(self)
    self.obj1532.isGraphObjectVisual = True

    if(hasattr(self.obj1532, '_setHierarchicalLink')):
      self.obj1532._setHierarchicalLink(False)

    # Type
    self.obj1532.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1532.Type.config = 0

    # name
    self.obj1532.name.setValue('concat1')

    self.obj1532.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(396.0,327.0,self.obj1532)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1532.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1532)
    self.globalAndLocalPostcondition(self.obj1532, rootNode)
    self.obj1532.postAction( rootNode.CREATE )

    self.obj1533=Concat(self)
    self.obj1533.isGraphObjectVisual = True

    if(hasattr(self.obj1533, '_setHierarchicalLink')):
      self.obj1533._setHierarchicalLink(False)

    # Type
    self.obj1533.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1533.Type.config = 0

    # name
    self.obj1533.name.setValue('concat2')

    self.obj1533.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(792.0,324.0,self.obj1533)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [5.0, -2.0]
    else: new_obj = None
    self.obj1533.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1533)
    self.globalAndLocalPostcondition(self.obj1533, rootNode)
    self.obj1533.postAction( rootNode.CREATE )

    self.obj1534=Constant(self)
    self.obj1534.isGraphObjectVisual = True

    if(hasattr(self.obj1534, '_setHierarchicalLink')):
      self.obj1534._setHierarchicalLink(False)

    # Type
    self.obj1534.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1534.Type.config = 0

    # name
    self.obj1534.name.setValue('S')

    self.obj1534.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(333.0,251.0,self.obj1534)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1534.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1534)
    self.globalAndLocalPostcondition(self.obj1534, rootNode)
    self.obj1534.postAction( rootNode.CREATE )

    self.obj1535=Constant(self)
    self.obj1535.isGraphObjectVisual = True

    if(hasattr(self.obj1535, '_setHierarchicalLink')):
      self.obj1535._setHierarchicalLink(False)

    # Type
    self.obj1535.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1535.Type.config = 0

    # name
    self.obj1535.name.setValue('exit')

    self.obj1535.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1140.0,674.0,self.obj1535)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, -4.0]
    else: new_obj = None
    self.obj1535.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1535)
    self.globalAndLocalPostcondition(self.obj1535, rootNode)
    self.obj1535.postAction( rootNode.CREATE )

    self.obj1536=Constant(self)
    self.obj1536.isGraphObjectVisual = True

    if(hasattr(self.obj1536, '_setHierarchicalLink')):
      self.obj1536._setHierarchicalLink(False)

    # Type
    self.obj1536.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1536.Type.config = 0

    # name
    self.obj1536.name.setValue('exack')

    self.obj1536.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,723.0,self.obj1536)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1536.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1536)
    self.globalAndLocalPostcondition(self.obj1536, rootNode)
    self.obj1536.postAction( rootNode.CREATE )

    self.obj1537=Constant(self)
    self.obj1537.isGraphObjectVisual = True

    if(hasattr(self.obj1537, '_setHierarchicalLink')):
      self.obj1537._setHierarchicalLink(False)

    # Type
    self.obj1537.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1537.Type.config = 0

    # name
    self.obj1537.name.setValue('"')

    self.obj1537.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(648.0,250.0,self.obj1537)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1537.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1537)
    self.globalAndLocalPostcondition(self.obj1537, rootNode)
    self.obj1537.postAction( rootNode.CREATE )

    self.obj1538=Constant(self)
    self.obj1538.isGraphObjectVisual = True

    if(hasattr(self.obj1538, '_setHierarchicalLink')):
      self.obj1538._setHierarchicalLink(False)

    # Type
    self.obj1538.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1538.Type.config = 0

    # name
    self.obj1538.name.setValue('"')

    self.obj1538.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(936.0,246.0,self.obj1538)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1538.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1538)
    self.globalAndLocalPostcondition(self.obj1538, rootNode)
    self.obj1538.postAction( rootNode.CREATE )

    self.obj1539=Constant(self)
    self.obj1539.isGraphObjectVisual = True

    if(hasattr(self.obj1539, '_setHierarchicalLink')):
      self.obj1539._setHierarchicalLink(False)

    # Type
    self.obj1539.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1539.Type.config = 0

    # name
    self.obj1539.name.setValue('sh')

    self.obj1539.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(420.0,786.0,self.obj1539)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1539.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1539)
    self.globalAndLocalPostcondition(self.obj1539, rootNode)
    self.obj1539.postAction( rootNode.CREATE )

    self.obj1540=Constant(self)
    self.obj1540.isGraphObjectVisual = True

    if(hasattr(self.obj1540, '_setHierarchicalLink')):
      self.obj1540._setHierarchicalLink(False)

    # Type
    self.obj1540.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1540.Type.config = 0

    # name
    self.obj1540.name.setValue('instfortrans')

    self.obj1540.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(21.0,640.0,self.obj1540)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1540.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1540)
    self.globalAndLocalPostcondition(self.obj1540, rootNode)
    self.obj1540.postAction( rootNode.CREATE )

    self.obj1541=paired_with(self)
    self.obj1541.isGraphObjectVisual = True

    if(hasattr(self.obj1541, '_setHierarchicalLink')):
      self.obj1541._setHierarchicalLink(False)

    self.obj1541.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,182.0,self.obj1541)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1541.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1541)
    self.globalAndLocalPostcondition(self.obj1541, rootNode)
    self.obj1541.postAction( rootNode.CREATE )

    self.obj1542=match_contains(self)
    self.obj1542.isGraphObjectVisual = True

    if(hasattr(self.obj1542, '_setHierarchicalLink')):
      self.obj1542._setHierarchicalLink(False)

    self.obj1542.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj1542)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1542.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1542)
    self.globalAndLocalPostcondition(self.obj1542, rootNode)
    self.obj1542.postAction( rootNode.CREATE )

    self.obj1543=match_contains(self)
    self.obj1543.isGraphObjectVisual = True

    if(hasattr(self.obj1543, '_setHierarchicalLink')):
      self.obj1543._setHierarchicalLink(False)

    self.obj1543.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,127.0,self.obj1543)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1543.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1543)
    self.globalAndLocalPostcondition(self.obj1543, rootNode)
    self.obj1543.postAction( rootNode.CREATE )

    self.obj1544=match_contains(self)
    self.obj1544.isGraphObjectVisual = True

    if(hasattr(self.obj1544, '_setHierarchicalLink')):
      self.obj1544._setHierarchicalLink(False)

    self.obj1544.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(384.0,97.0,self.obj1544)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1544.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1544)
    self.globalAndLocalPostcondition(self.obj1544, rootNode)
    self.obj1544.postAction( rootNode.CREATE )

    self.obj1545=match_contains(self)
    self.obj1545.isGraphObjectVisual = True

    if(hasattr(self.obj1545, '_setHierarchicalLink')):
      self.obj1545._setHierarchicalLink(False)

    self.obj1545.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(524.0,67.0,self.obj1545)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1545.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1545)
    self.globalAndLocalPostcondition(self.obj1545, rootNode)
    self.obj1545.postAction( rootNode.CREATE )

    self.obj1546=apply_contains(self)
    self.obj1546.isGraphObjectVisual = True

    if(hasattr(self.obj1546, '_setHierarchicalLink')):
      self.obj1546._setHierarchicalLink(False)

    self.obj1546.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(237.5,466.0,self.obj1546)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1546.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1546)
    self.globalAndLocalPostcondition(self.obj1546, rootNode)
    self.obj1546.postAction( rootNode.CREATE )

    self.obj1547=apply_contains(self)
    self.obj1547.isGraphObjectVisual = True

    if(hasattr(self.obj1547, '_setHierarchicalLink')):
      self.obj1547._setHierarchicalLink(False)

    self.obj1547.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(374.5,531.0,self.obj1547)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1547.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1547)
    self.globalAndLocalPostcondition(self.obj1547, rootNode)
    self.obj1547.postAction( rootNode.CREATE )

    self.obj1548=apply_contains(self)
    self.obj1548.isGraphObjectVisual = True

    if(hasattr(self.obj1548, '_setHierarchicalLink')):
      self.obj1548._setHierarchicalLink(False)

    self.obj1548.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(465.0,521.0,self.obj1548)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1548.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1548)
    self.globalAndLocalPostcondition(self.obj1548, rootNode)
    self.obj1548.postAction( rootNode.CREATE )

    self.obj1549=apply_contains(self)
    self.obj1549.isGraphObjectVisual = True

    if(hasattr(self.obj1549, '_setHierarchicalLink')):
      self.obj1549._setHierarchicalLink(False)

    self.obj1549.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(555.5,496.0,self.obj1549)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1549.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1549)
    self.globalAndLocalPostcondition(self.obj1549, rootNode)
    self.obj1549.postAction( rootNode.CREATE )

    self.obj1550=apply_contains(self)
    self.obj1550.isGraphObjectVisual = True

    if(hasattr(self.obj1550, '_setHierarchicalLink')):
      self.obj1550._setHierarchicalLink(False)

    self.obj1550.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(646.5,466.0,self.obj1550)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1550.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1550)
    self.globalAndLocalPostcondition(self.obj1550, rootNode)
    self.obj1550.postAction( rootNode.CREATE )

    self.obj1551=directLink_T(self)
    self.obj1551.isGraphObjectVisual = True

    if(hasattr(self.obj1551, '_setHierarchicalLink')):
      self.obj1551._setHierarchicalLink(False)

    # associationType
    self.obj1551.associationType.setValue('channelNames')

    self.obj1551.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(522.0,531.0,self.obj1551)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1551.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1551)
    self.globalAndLocalPostcondition(self.obj1551, rootNode)
    self.obj1551.postAction( rootNode.CREATE )

    self.obj1552=directLink_T(self)
    self.obj1552.isGraphObjectVisual = True

    if(hasattr(self.obj1552, '_setHierarchicalLink')):
      self.obj1552._setHierarchicalLink(False)

    # associationType
    self.obj1552.associationType.setValue('channelNames')

    self.obj1552.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(645.5,566.0,self.obj1552)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1552.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1552)
    self.globalAndLocalPostcondition(self.obj1552, rootNode)
    self.obj1552.postAction( rootNode.CREATE )

    self.obj1553=directLink_T(self)
    self.obj1553.isGraphObjectVisual = True

    if(hasattr(self.obj1553, '_setHierarchicalLink')):
      self.obj1553._setHierarchicalLink(False)

    # associationType
    self.obj1553.associationType.setValue('channelNames')

    self.obj1553.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(553.0,586.0,self.obj1553)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1553.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1553)
    self.globalAndLocalPostcondition(self.obj1553, rootNode)
    self.obj1553.postAction( rootNode.CREATE )

    self.obj1554=directLink_T(self)
    self.obj1554.isGraphObjectVisual = True

    if(hasattr(self.obj1554, '_setHierarchicalLink')):
      self.obj1554._setHierarchicalLink(False)

    # associationType
    self.obj1554.associationType.setValue('channelNames')

    self.obj1554.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(469.0,596.0,self.obj1554)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1554.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1554)
    self.globalAndLocalPostcondition(self.obj1554, rootNode)
    self.obj1554.postAction( rootNode.CREATE )

    self.obj1555=directLink_S(self)
    self.obj1555.isGraphObjectVisual = True

    if(hasattr(self.obj1555, '_setHierarchicalLink')):
      self.obj1555._setHierarchicalLink(False)

    # associationType
    self.obj1555.associationType.setValue('type')

    self.obj1555.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(350.0,153.0,self.obj1555)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1555.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1555)
    self.globalAndLocalPostcondition(self.obj1555, rootNode)
    self.obj1555.postAction( rootNode.CREATE )

    self.obj1556=directLink_S(self)
    self.obj1556.isGraphObjectVisual = True

    if(hasattr(self.obj1556, '_setHierarchicalLink')):
      self.obj1556._setHierarchicalLink(False)

    # associationType
    self.obj1556.associationType.setValue('dest')

    self.obj1556.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(640.0,84.0,self.obj1556)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1556.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1556)
    self.globalAndLocalPostcondition(self.obj1556, rootNode)
    self.obj1556.postAction( rootNode.CREATE )

    self.obj1557=directLink_S(self)
    self.obj1557.isGraphObjectVisual = True

    if(hasattr(self.obj1557, '_setHierarchicalLink')):
      self.obj1557._setHierarchicalLink(False)

    # associationType
    self.obj1557.associationType.setValue('owningStateMachine')

    self.obj1557.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(770.0,113.0,self.obj1557)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1557.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1557)
    self.globalAndLocalPostcondition(self.obj1557, rootNode)
    self.obj1557.postAction( rootNode.CREATE )

    self.obj1558=hasAttribute_S(self)
    self.obj1558.isGraphObjectVisual = True

    if(hasattr(self.obj1558, '_setHierarchicalLink')):
      self.obj1558._setHierarchicalLink(False)

    self.obj1558.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(902.0,148.5,self.obj1558)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1558.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1558)
    self.globalAndLocalPostcondition(self.obj1558, rootNode)
    self.obj1558.postAction( rootNode.CREATE )

    self.obj1559=hasAttribute_S(self)
    self.obj1559.isGraphObjectVisual = True

    if(hasattr(self.obj1559, '_setHierarchicalLink')):
      self.obj1559._setHierarchicalLink(False)

    self.obj1559.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(622.0,184.5,self.obj1559)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1559.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1559)
    self.globalAndLocalPostcondition(self.obj1559, rootNode)
    self.obj1559.postAction( rootNode.CREATE )

    self.obj1560=hasAttribute_T(self)
    self.obj1560.isGraphObjectVisual = True

    if(hasattr(self.obj1560, '_setHierarchicalLink')):
      self.obj1560._setHierarchicalLink(False)

    self.obj1560.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(343.0,482.5,self.obj1560)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1560.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1560)
    self.globalAndLocalPostcondition(self.obj1560, rootNode)
    self.obj1560.postAction( rootNode.CREATE )

    self.obj1561=hasAttribute_T(self)
    self.obj1561.isGraphObjectVisual = True

    if(hasattr(self.obj1561, '_setHierarchicalLink')):
      self.obj1561._setHierarchicalLink(False)

    self.obj1561.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1127.0,592.0,self.obj1561)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1561.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1561)
    self.globalAndLocalPostcondition(self.obj1561, rootNode)
    self.obj1561.postAction( rootNode.CREATE )

    self.obj1562=hasAttribute_T(self)
    self.obj1562.isGraphObjectVisual = True

    if(hasattr(self.obj1562, '_setHierarchicalLink')):
      self.obj1562._setHierarchicalLink(False)

    self.obj1562.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(946.5,649.0,self.obj1562)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1562.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1562)
    self.globalAndLocalPostcondition(self.obj1562, rootNode)
    self.obj1562.postAction( rootNode.CREATE )

    self.obj1563=hasAttribute_T(self)
    self.obj1563.isGraphObjectVisual = True

    if(hasattr(self.obj1563, '_setHierarchicalLink')):
      self.obj1563._setHierarchicalLink(False)

    self.obj1563.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(777.5,567.5,self.obj1563)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1563.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1563)
    self.globalAndLocalPostcondition(self.obj1563, rootNode)
    self.obj1563.postAction( rootNode.CREATE )

    self.obj1564=hasAttribute_T(self)
    self.obj1564.isGraphObjectVisual = True

    if(hasattr(self.obj1564, '_setHierarchicalLink')):
      self.obj1564._setHierarchicalLink(False)

    self.obj1564.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(584.5,703.0,self.obj1564)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1564.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1564)
    self.globalAndLocalPostcondition(self.obj1564, rootNode)
    self.obj1564.postAction( rootNode.CREATE )

    self.obj1565=hasAttribute_T(self)
    self.obj1565.isGraphObjectVisual = True

    if(hasattr(self.obj1565, '_setHierarchicalLink')):
      self.obj1565._setHierarchicalLink(False)

    self.obj1565.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(243.0,562.5,self.obj1565)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1565.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1565)
    self.globalAndLocalPostcondition(self.obj1565, rootNode)
    self.obj1565.postAction( rootNode.CREATE )

    self.obj1566=leftExpr(self)
    self.obj1566.isGraphObjectVisual = True

    if(hasattr(self.obj1566, '_setHierarchicalLink')):
      self.obj1566._setHierarchicalLink(False)

    self.obj1566.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(358.0,403.5,self.obj1566)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1566.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1566)
    self.globalAndLocalPostcondition(self.obj1566, rootNode)
    self.obj1566.postAction( rootNode.CREATE )

    self.obj1567=leftExpr(self)
    self.obj1567.isGraphObjectVisual = True

    if(hasattr(self.obj1567, '_setHierarchicalLink')):
      self.obj1567._setHierarchicalLink(False)

    self.obj1567.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1100.0,630.0,self.obj1567)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1567.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1567)
    self.globalAndLocalPostcondition(self.obj1567, rootNode)
    self.obj1567.postAction( rootNode.CREATE )

    self.obj1568=leftExpr(self)
    self.obj1568.isGraphObjectVisual = True

    if(hasattr(self.obj1568, '_setHierarchicalLink')):
      self.obj1568._setHierarchicalLink(False)

    self.obj1568.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1023.5,709.5,self.obj1568)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1568.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1568)
    self.globalAndLocalPostcondition(self.obj1568, rootNode)
    self.obj1568.postAction( rootNode.CREATE )

    self.obj1569=leftExpr(self)
    self.obj1569.isGraphObjectVisual = True

    if(hasattr(self.obj1569, '_setHierarchicalLink')):
      self.obj1569._setHierarchicalLink(False)

    self.obj1569.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(793.0,464.0,self.obj1569)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1569.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1569)
    self.globalAndLocalPostcondition(self.obj1569, rootNode)
    self.obj1569.postAction( rootNode.CREATE )

    self.obj1570=leftExpr(self)
    self.obj1570.isGraphObjectVisual = True

    if(hasattr(self.obj1570, '_setHierarchicalLink')):
      self.obj1570._setHierarchicalLink(False)

    self.obj1570.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(482.5,754.0,self.obj1570)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1570.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1570)
    self.globalAndLocalPostcondition(self.obj1570, rootNode)
    self.obj1570.postAction( rootNode.CREATE )

    self.obj1571=leftExpr(self)
    self.obj1571.isGraphObjectVisual = True

    if(hasattr(self.obj1571, '_setHierarchicalLink')):
      self.obj1571._setHierarchicalLink(False)

    self.obj1571.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(236.0,606.5,self.obj1571)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1571.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1571)
    self.globalAndLocalPostcondition(self.obj1571, rootNode)
    self.obj1571.postAction( rootNode.CREATE )

    self.obj1572=rightExpr(self)
    self.obj1572.isGraphObjectVisual = True

    if(hasattr(self.obj1572, '_setHierarchicalLink')):
      self.obj1572._setHierarchicalLink(False)

    self.obj1572.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(447.0,363.5,self.obj1572)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1572.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1572)
    self.globalAndLocalPostcondition(self.obj1572, rootNode)
    self.obj1572.postAction( rootNode.CREATE )

    self.obj1573=rightExpr(self)
    self.obj1573.isGraphObjectVisual = True

    if(hasattr(self.obj1573, '_setHierarchicalLink')):
      self.obj1573._setHierarchicalLink(False)

    self.obj1573.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1279.5,683.5,self.obj1573)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1573.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1573)
    self.globalAndLocalPostcondition(self.obj1573, rootNode)
    self.obj1573.postAction( rootNode.CREATE )

    self.obj1574=rightExpr(self)
    self.obj1574.isGraphObjectVisual = True

    if(hasattr(self.obj1574, '_setHierarchicalLink')):
      self.obj1574._setHierarchicalLink(False)

    self.obj1574.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1023.5,753.5,self.obj1574)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1574.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1574)
    self.globalAndLocalPostcondition(self.obj1574, rootNode)
    self.obj1574.postAction( rootNode.CREATE )

    self.obj1575=rightExpr(self)
    self.obj1575.isGraphObjectVisual = True

    if(hasattr(self.obj1575, '_setHierarchicalLink')):
      self.obj1575._setHierarchicalLink(False)

    self.obj1575.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(926.0,449.0,self.obj1575)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1575.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1575)
    self.globalAndLocalPostcondition(self.obj1575, rootNode)
    self.obj1575.postAction( rootNode.CREATE )

    self.obj1576=rightExpr(self)
    self.obj1576.isGraphObjectVisual = True

    if(hasattr(self.obj1576, '_setHierarchicalLink')):
      self.obj1576._setHierarchicalLink(False)

    self.obj1576.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(478.0,791.5,self.obj1576)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1576.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1576)
    self.globalAndLocalPostcondition(self.obj1576, rootNode)
    self.obj1576.postAction( rootNode.CREATE )

    self.obj1577=rightExpr(self)
    self.obj1577.isGraphObjectVisual = True

    if(hasattr(self.obj1577, '_setHierarchicalLink')):
      self.obj1577._setHierarchicalLink(False)

    self.obj1577.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(236.5,646.5,self.obj1577)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1577.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1577)
    self.globalAndLocalPostcondition(self.obj1577, rootNode)
    self.obj1577.postAction( rootNode.CREATE )

    self.obj1578=hasArgs(self)
    self.obj1578.isGraphObjectVisual = True

    if(hasattr(self.obj1578, '_setHierarchicalLink')):
      self.obj1578._setHierarchicalLink(False)

    self.obj1578.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(498.5,323.0,self.obj1578)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1578.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1578)
    self.globalAndLocalPostcondition(self.obj1578, rootNode)
    self.obj1578.postAction( rootNode.CREATE )

    self.obj1579=hasArgs(self)
    self.obj1579.isGraphObjectVisual = True

    if(hasattr(self.obj1579, '_setHierarchicalLink')):
      self.obj1579._setHierarchicalLink(False)

    self.obj1579.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(572.0,293.5,self.obj1579)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1579.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1579)
    self.globalAndLocalPostcondition(self.obj1579, rootNode)
    self.obj1579.postAction( rootNode.CREATE )

    self.obj1580=hasArgs(self)
    self.obj1580.isGraphObjectVisual = True

    if(hasattr(self.obj1580, '_setHierarchicalLink')):
      self.obj1580._setHierarchicalLink(False)

    self.obj1580.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(862.0,336.0,self.obj1580)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1580.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1580)
    self.globalAndLocalPostcondition(self.obj1580, rootNode)
    self.obj1580.postAction( rootNode.CREATE )

    self.obj1581=hasArgs(self)
    self.obj1581.isGraphObjectVisual = True

    if(hasattr(self.obj1581, '_setHierarchicalLink')):
      self.obj1581._setHierarchicalLink(False)

    self.obj1581.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(910.0,298.0,self.obj1581)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1581.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1581)
    self.globalAndLocalPostcondition(self.obj1581, rootNode)
    self.obj1581.postAction( rootNode.CREATE )

    self.obj1582=hasArgs(self)
    self.obj1582.isGraphObjectVisual = True

    if(hasattr(self.obj1582, '_setHierarchicalLink')):
      self.obj1582._setHierarchicalLink(False)

    self.obj1582.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(958.0,353.0,self.obj1582)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1582.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1582)
    self.globalAndLocalPostcondition(self.obj1582, rootNode)
    self.obj1582.postAction( rootNode.CREATE )

    # Connections for obj1507 (graphObject_: Obj776) of type MatchModel
    self.drawConnections(
(self.obj1507,self.obj1541,[138.0, 51.0, 140.5, 182.0],"true", 2),
(self.obj1507,self.obj1542,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj1507,self.obj1543,[138.0, 51.0, 244.0, 127.0],"true", 2),
(self.obj1507,self.obj1544,[138.0, 51.0, 384.0, 97.0],"true", 2),
(self.obj1507,self.obj1545,[138.0, 51.0, 524.0, 67.0],"true", 2) )
    # Connections for obj1508 (graphObject_: Obj777) of type ApplyModel
    self.drawConnections(
(self.obj1508,self.obj1546,[143.0, 401.0, 237.5, 466.0],"true", 2),
(self.obj1508,self.obj1547,[143.0, 401.0, 374.5, 531.0],"true", 2),
(self.obj1508,self.obj1548,[143.0, 401.0, 465.0, 521.0],"true", 2),
(self.obj1508,self.obj1549,[143.0, 401.0, 555.5, 496.0],"true", 2),
(self.obj1508,self.obj1550,[143.0, 401.0, 646.5, 466.0],"true", 2) )
    # Connections for obj1509 (graphObject_: Obj778) named vertex1
    self.drawConnections(
(self.obj1509,self.obj1558,[910.0, 83.0, 902.0, 148.5],"true", 2),
(self.obj1509,self.obj1557,[910.0, 83.0, 770.0, 113.0],"true", 2) )
    # Connections for obj1510 (graphObject_: Obj779) named transition1
    self.drawConnections(
(self.obj1510,self.obj1555,[350.0, 83.0, 350.0, 153.0],"true", 2),
(self.obj1510,self.obj1556,[350.0, 83.0, 640.0, 84.0],"true", 2) )
    # Connections for obj1511 (graphObject_: Obj780) named stateMachine1
    self.drawConnections(
(self.obj1511,self.obj1559,[630.0, 143.0, 622.0, 184.5],"true", 2) )
    # Connections for obj1512 (graphObject_: Obj781) named sibling0_1
    self.drawConnections(
 )
    # Connections for obj1513 (graphObject_: Obj782) named name1
    self.drawConnections(
(self.obj1513,self.obj1561,[1150.0, 531.0, 1127.0, 592.0],"true", 2) )
    # Connections for obj1514 (graphObject_: Obj783) named name2
    self.drawConnections(
(self.obj1514,self.obj1562,[968.0, 591.0, 946.5, 649.0],"true", 2) )
    # Connections for obj1515 (graphObject_: Obj784) named name3
    self.drawConnections(
(self.obj1515,self.obj1563,[787.0, 641.0, 777.5, 567.5],"true", 2) )
    # Connections for obj1516 (graphObject_: Obj785) named name4
    self.drawConnections(
(self.obj1516,self.obj1564,[606.0, 661.0, 584.5, 703.0],"true", 2) )
    # Connections for obj1517 (graphObject_: Obj786) named inst1
    self.drawConnections(
(self.obj1517,self.obj1560,[332.0, 531.0, 343.0, 482.5],"true", 2),
(self.obj1517,self.obj1551,[332.0, 531.0, 522.0, 531.0],"true", 2),
(self.obj1517,self.obj1552,[332.0, 531.0, 645.5, 566.0],"true", 2),
(self.obj1517,self.obj1553,[332.0, 531.0, 553.0, 586.0],"true", 2),
(self.obj1517,self.obj1554,[332.0, 531.0, 469.0, 596.0],"true", 2),
(self.obj1517,self.obj1565,[332.0, 531.0, 243.0, 562.5],"true", 2) )
    # Connections for obj1518 (graphObject_: Obj787) named name
    self.drawConnections(
 )
    # Connections for obj1519 (graphObject_: Obj788) named name
    self.drawConnections(
 )
    # Connections for obj1520 (graphObject_: Obj789) named name
    self.drawConnections(
 )
    # Connections for obj1521 (graphObject_: Obj790) named literal
    self.drawConnections(
 )
    # Connections for obj1522 (graphObject_: Obj791) named literal
    self.drawConnections(
 )
    # Connections for obj1523 (graphObject_: Obj792) named literal
    self.drawConnections(
 )
    # Connections for obj1524 (graphObject_: Obj793) named literal
    self.drawConnections(
 )
    # Connections for obj1525 (graphObject_: Obj794) named pivotout
    self.drawConnections(
 )
    # Connections for obj1526 (graphObject_: Obj795) named eq1
    self.drawConnections(
(self.obj1526,self.obj1566,[364.0, 366.0, 358.0, 403.5],"true", 2),
(self.obj1526,self.obj1572,[364.0, 366.0, 447.0, 363.5],"true", 2) )
    # Connections for obj1527 (graphObject_: Obj796) named eq2
    self.drawConnections(
(self.obj1527,self.obj1567,[1285.0, 633.0, 1100.0, 630.0],"true", 2),
(self.obj1527,self.obj1573,[1285.0, 633.0, 1279.5, 683.5],"true", 2) )
    # Connections for obj1528 (graphObject_: Obj797) named eq3
    self.drawConnections(
(self.obj1528,self.obj1568,[1113.0, 722.0, 1023.5, 709.5],"true", 2),
(self.obj1528,self.obj1574,[1113.0, 722.0, 1023.5, 753.5],"true", 2) )
    # Connections for obj1529 (graphObject_: Obj798) named eq4
    self.drawConnections(
(self.obj1529,self.obj1569,[926.0, 467.0, 793.0, 464.0],"true", 2),
(self.obj1529,self.obj1575,[926.0, 467.0, 926.0, 449.0],"true", 2) )
    # Connections for obj1530 (graphObject_: Obj799) named eq5
    self.drawConnections(
(self.obj1530,self.obj1570,[402.0, 763.0, 482.5, 754.0],"true", 2),
(self.obj1530,self.obj1576,[402.0, 763.0, 478.0, 791.5],"true", 2) )
    # Connections for obj1531 (graphObject_: Obj800) named eq6
    self.drawConnections(
(self.obj1531,self.obj1577,[318.0, 619.0, 236.5, 646.5],"true", 2),
(self.obj1531,self.obj1571,[318.0, 619.0, 236.0, 606.5],"true", 2) )
    # Connections for obj1532 (graphObject_: Obj801) named concat1
    self.drawConnections(
(self.obj1532,self.obj1578,[530.0, 361.0, 498.5, 323.0],"true", 2),
(self.obj1532,self.obj1579,[530.0, 361.0, 572.0, 293.5],"true", 2) )
    # Connections for obj1533 (graphObject_: Obj802) named concat2
    self.drawConnections(
(self.obj1533,self.obj1580,[926.0, 358.0, 862.0, 336.0],"true", 2),
(self.obj1533,self.obj1581,[926.0, 358.0, 910.0, 298.0],"true", 2),
(self.obj1533,self.obj1582,[926.0, 358.0, 958.0, 353.0],"true", 2) )
    # Connections for obj1534 (graphObject_: Obj803) named S
    self.drawConnections(
 )
    # Connections for obj1535 (graphObject_: Obj804) named exit
    self.drawConnections(
 )
    # Connections for obj1536 (graphObject_: Obj805) named exack
    self.drawConnections(
 )
    # Connections for obj1537 (graphObject_: Obj806) named "
    self.drawConnections(
 )
    # Connections for obj1538 (graphObject_: Obj807) named "
    self.drawConnections(
 )
    # Connections for obj1539 (graphObject_: Obj808) named sh
    self.drawConnections(
 )
    # Connections for obj1540 (graphObject_: Obj809) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1541 (graphObject_: Obj810) of type paired_with
    self.drawConnections(
(self.obj1541,self.obj1508,[140.5, 182.0, 143.0, 401.0],"true", 2) )
    # Connections for obj1542 (graphObject_: Obj811) of type match_contains
    self.drawConnections(
(self.obj1542,self.obj1510,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj1543 (graphObject_: Obj812) of type match_contains
    self.drawConnections(
(self.obj1543,self.obj1512,[244.0, 127.0, 350.0, 203.0],"true", 2) )
    # Connections for obj1544 (graphObject_: Obj813) of type match_contains
    self.drawConnections(
(self.obj1544,self.obj1511,[384.0, 97.0, 630.0, 143.0],"true", 2) )
    # Connections for obj1545 (graphObject_: Obj814) of type match_contains
    self.drawConnections(
(self.obj1545,self.obj1509,[524.0, 67.0, 910.0, 83.0],"true", 2) )
    # Connections for obj1546 (graphObject_: Obj815) of type apply_contains
    self.drawConnections(
(self.obj1546,self.obj1517,[237.5, 466.0, 332.0, 531.0],"true", 2) )
    # Connections for obj1547 (graphObject_: Obj816) of type apply_contains
    self.drawConnections(
(self.obj1547,self.obj1516,[374.5, 531.0, 606.0, 661.0],"true", 2) )
    # Connections for obj1548 (graphObject_: Obj817) of type apply_contains
    self.drawConnections(
(self.obj1548,self.obj1515,[465.0, 521.0, 787.0, 641.0],"true", 2) )
    # Connections for obj1549 (graphObject_: Obj818) of type apply_contains
    self.drawConnections(
(self.obj1549,self.obj1514,[555.5, 496.0, 968.0, 591.0],"true", 2) )
    # Connections for obj1550 (graphObject_: Obj819) of type apply_contains
    self.drawConnections(
(self.obj1550,self.obj1513,[646.5, 466.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj1551 (graphObject_: Obj820) of type directLink_T
    self.drawConnections(
(self.obj1551,self.obj1513,[522.0, 531.0, 1150.0, 531.0],"true", 2) )
    # Connections for obj1552 (graphObject_: Obj821) of type directLink_T
    self.drawConnections(
(self.obj1552,self.obj1514,[645.5, 566.0, 968.0, 591.0],"true", 2) )
    # Connections for obj1553 (graphObject_: Obj822) of type directLink_T
    self.drawConnections(
(self.obj1553,self.obj1515,[553.0, 586.0, 787.0, 641.0],"true", 2) )
    # Connections for obj1554 (graphObject_: Obj823) of type directLink_T
    self.drawConnections(
(self.obj1554,self.obj1516,[469.0, 596.0, 606.0, 661.0],"true", 2) )
    # Connections for obj1555 (graphObject_: Obj824) of type directLink_S
    self.drawConnections(
(self.obj1555,self.obj1512,[350.0, 153.0, 350.0, 203.0],"true", 2) )
    # Connections for obj1556 (graphObject_: Obj825) of type directLink_S
    self.drawConnections(
(self.obj1556,self.obj1509,[640.0, 84.0, 910.0, 83.0],"true", 2) )
    # Connections for obj1557 (graphObject_: Obj826) of type directLink_S
    self.drawConnections(
(self.obj1557,self.obj1511,[770.0, 113.0, 630.0, 143.0],"true", 2) )
    # Connections for obj1558 (graphObject_: Obj827) of type hasAttribute_S
    self.drawConnections(
(self.obj1558,self.obj1518,[902.0, 148.5, 894.0, 194.0],"true", 2) )
    # Connections for obj1559 (graphObject_: Obj828) of type hasAttribute_S
    self.drawConnections(
(self.obj1559,self.obj1519,[622.0, 184.5, 614.0, 226.0],"true", 2) )
    # Connections for obj1560 (graphObject_: Obj829) of type hasAttribute_T
    self.drawConnections(
(self.obj1560,self.obj1520,[343.0, 482.5, 354.0, 434.0],"true", 2) )
    # Connections for obj1561 (graphObject_: Obj830) of type hasAttribute_T
    self.drawConnections(
(self.obj1561,self.obj1521,[1127.0, 592.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj1562 (graphObject_: Obj831) of type hasAttribute_T
    self.drawConnections(
(self.obj1562,self.obj1522,[946.5, 649.0, 934.0, 680.0],"true", 2) )
    # Connections for obj1563 (graphObject_: Obj832) of type hasAttribute_T
    self.drawConnections(
(self.obj1563,self.obj1523,[777.5, 567.5, 774.0, 454.0],"true", 2) )
    # Connections for obj1564 (graphObject_: Obj833) of type hasAttribute_T
    self.drawConnections(
(self.obj1564,self.obj1524,[584.5, 703.0, 563.0, 745.0],"true", 2) )
    # Connections for obj1565 (graphObject_: Obj834) of type hasAttribute_T
    self.drawConnections(
(self.obj1565,self.obj1525,[243.0, 562.5, 154.0, 594.0],"true", 2) )
    # Connections for obj1566 (graphObject_: Obj835) of type leftExpr
    self.drawConnections(
(self.obj1566,self.obj1520,[358.0, 403.5, 354.0, 434.0],"true", 2) )
    # Connections for obj1567 (graphObject_: Obj836) of type leftExpr
    self.drawConnections(
(self.obj1567,self.obj1521,[1100.0, 630.0, 1109.0, 627.0],"true", 2) )
    # Connections for obj1568 (graphObject_: Obj837) of type leftExpr
    self.drawConnections(
(self.obj1568,self.obj1522,[1023.5, 709.5, 934.0, 680.0],"true", 2) )
    # Connections for obj1569 (graphObject_: Obj838) of type leftExpr
    self.drawConnections(
(self.obj1569,self.obj1523,[793.0, 464.0, 774.0, 454.0],"true", 2) )
    # Connections for obj1570 (graphObject_: Obj839) of type leftExpr
    self.drawConnections(
(self.obj1570,self.obj1524,[482.5, 754.0, 563.0, 745.0],"true", 2) )
    # Connections for obj1571 (graphObject_: Obj840) of type leftExpr
    self.drawConnections(
(self.obj1571,self.obj1525,[236.0, 606.5, 154.0, 594.0],"true", 2) )
    # Connections for obj1572 (graphObject_: Obj841) of type rightExpr
    self.drawConnections(
(self.obj1572,self.obj1532,[447.0, 363.5, 530.0, 361.0],"true", 2) )
    # Connections for obj1573 (graphObject_: Obj842) of type rightExpr
    self.drawConnections(
(self.obj1573,self.obj1535,[1279.5, 683.5, 1274.0, 708.0],"true", 2) )
    # Connections for obj1574 (graphObject_: Obj843) of type rightExpr
    self.drawConnections(
(self.obj1574,self.obj1536,[1023.5, 753.5, 934.0, 757.0],"true", 2) )
    # Connections for obj1575 (graphObject_: Obj844) of type rightExpr
    self.drawConnections(
(self.obj1575,self.obj1533,[926.0, 449.0, 926.0, 358.0],"true", 2) )
    # Connections for obj1576 (graphObject_: Obj845) of type rightExpr
    self.drawConnections(
(self.obj1576,self.obj1539,[478.0, 791.5, 554.0, 820.0],"true", 2) )
    # Connections for obj1577 (graphObject_: Obj846) of type rightExpr
    self.drawConnections(
(self.obj1577,self.obj1540,[236.5, 646.5, 155.0, 674.0],"true", 2) )
    # Connections for obj1578 (graphObject_: Obj847) of type hasArgs
    self.drawConnections(
(self.obj1578,self.obj1534,[498.5, 323.0, 467.0, 285.0],"true", 2) )
    # Connections for obj1579 (graphObject_: Obj848) of type hasArgs
    self.drawConnections(
(self.obj1579,self.obj1519,[572.0, 293.5, 614.0, 226.0],"true", 2) )
    # Connections for obj1580 (graphObject_: Obj849) of type hasArgs
    self.drawConnections(
(self.obj1580,self.obj1537,[862.0, 336.0, 782.0, 284.0],"true", 2) )
    # Connections for obj1581 (graphObject_: Obj850) of type hasArgs
    self.drawConnections(
(self.obj1581,self.obj1518,[910.0, 298.0, 894.0, 194.0],"true", 2) )
    # Connections for obj1582 (graphObject_: Obj851) of type hasArgs
    self.drawConnections(
(self.obj1582,self.obj1538,[958.0, 353.0, 1070.0, 280.0],"true", 2) )

newfunction = Transition2QInstSIBLING_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
