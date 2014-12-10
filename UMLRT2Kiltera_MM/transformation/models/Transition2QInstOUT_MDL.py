"""
__Transition2QInstOUT_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 15:09:38 2014
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


    self.obj1603=MatchModel(self)
    self.obj1603.isGraphObjectVisual = True

    if(hasattr(self.obj1603, '_setHierarchicalLink')):
      self.obj1603._setHierarchicalLink(False)

    self.obj1603.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1603)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1603.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1603)
    self.globalAndLocalPostcondition(self.obj1603, rootNode)
    self.obj1603.postAction( rootNode.CREATE )

    self.obj1604=ApplyModel(self)
    self.obj1604.isGraphObjectVisual = True

    if(hasattr(self.obj1604, '_setHierarchicalLink')):
      self.obj1604._setHierarchicalLink(False)

    self.obj1604.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,240.0,self.obj1604)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1604.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1604)
    self.globalAndLocalPostcondition(self.obj1604, rootNode)
    self.obj1604.postAction( rootNode.CREATE )

    self.obj1605=Vertex(self)
    self.obj1605.isGraphObjectVisual = True

    if(hasattr(self.obj1605, '_setHierarchicalLink')):
      self.obj1605._setHierarchicalLink(False)

    # name
    self.obj1605.name.setValue('vertex1')

    # classtype
    self.obj1605.classtype.setValue('Vertex')

    # cardinality
    self.obj1605.cardinality.setValue('1')

    self.obj1605.graphClass_= graph_Vertex
    if self.genGraphics:
       new_obj = graph_Vertex(660.0,120.0,self.obj1605)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Vertex", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1605.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1605)
    self.globalAndLocalPostcondition(self.obj1605, rootNode)
    self.obj1605.postAction( rootNode.CREATE )

    self.obj1606=Transition(self)
    self.obj1606.isGraphObjectVisual = True

    if(hasattr(self.obj1606, '_setHierarchicalLink')):
      self.obj1606._setHierarchicalLink(False)

    # name
    self.obj1606.name.setValue('transition1')

    # classtype
    self.obj1606.classtype.setValue('Transition')

    # cardinality
    self.obj1606.cardinality.setValue('+')

    self.obj1606.graphClass_= graph_Transition
    if self.genGraphics:
       new_obj = graph_Transition(160.0,34.0,self.obj1606)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.96999999999999886, 0.85999999999999943]
    else: new_obj = None
    self.obj1606.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1606)
    self.globalAndLocalPostcondition(self.obj1606, rootNode)
    self.obj1606.postAction( rootNode.CREATE )

    self.obj1607=StateMachine(self)
    self.obj1607.isGraphObjectVisual = True

    if(hasattr(self.obj1607, '_setHierarchicalLink')):
      self.obj1607._setHierarchicalLink(False)

    # name
    self.obj1607.name.setValue('statemachine1')

    # classtype
    self.obj1607.classtype.setValue('StateMachine')

    # cardinality
    self.obj1607.cardinality.setValue('1')

    self.obj1607.graphClass_= graph_StateMachine
    if self.genGraphics:
       new_obj = graph_StateMachine(660.0,25.0,self.obj1607)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateMachine", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1607.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1607)
    self.globalAndLocalPostcondition(self.obj1607, rootNode)
    self.obj1607.postAction( rootNode.CREATE )

    self.obj1608=OUT2(self)
    self.obj1608.isGraphObjectVisual = True

    if(hasattr(self.obj1608, '_setHierarchicalLink')):
      self.obj1608._setHierarchicalLink(False)

    # classtype
    self.obj1608.classtype.setValue('OUT2')

    # cardinality
    self.obj1608.cardinality.setValue('1')

    # name
    self.obj1608.name.setValue('out2_1')

    self.obj1608.graphClass_= graph_OUT2
    if self.genGraphics:
       new_obj = graph_OUT2(160.0,121.0,self.obj1608)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1608.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1608)
    self.globalAndLocalPostcondition(self.obj1608, rootNode)
    self.obj1608.postAction( rootNode.CREATE )

    self.obj1609=Name(self)
    self.obj1609.isGraphObjectVisual = True

    if(hasattr(self.obj1609, '_setHierarchicalLink')):
      self.obj1609._setHierarchicalLink(False)

    # classtype
    self.obj1609.classtype.setValue('Name')

    # cardinality
    self.obj1609.cardinality.setValue('1')

    # name
    self.obj1609.name.setValue('name1')

    self.obj1609.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(600.0,380.0,self.obj1609)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1609.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1609)
    self.globalAndLocalPostcondition(self.obj1609, rootNode)
    self.obj1609.postAction( rootNode.CREATE )

    self.obj1610=Inst(self)
    self.obj1610.isGraphObjectVisual = True

    if(hasattr(self.obj1610, '_setHierarchicalLink')):
      self.obj1610._setHierarchicalLink(False)

    # classtype
    self.obj1610.classtype.setValue('Inst')

    # cardinality
    self.obj1610.cardinality.setValue('1')

    # name
    self.obj1610.name.setValue('inst1')

    self.obj1610.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(200.0,380.0,self.obj1610)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1610.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1610)
    self.globalAndLocalPostcondition(self.obj1610, rootNode)
    self.obj1610.postAction( rootNode.CREATE )

    self.obj1611=Attribute(self)
    self.obj1611.isGraphObjectVisual = True

    if(hasattr(self.obj1611, '_setHierarchicalLink')):
      self.obj1611._setHierarchicalLink(False)

    # Type
    self.obj1611.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1611.Type.config = 0

    # name
    self.obj1611.name.setValue('name')

    self.obj1611.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(420.0,127.0,self.obj1611)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1611.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1611)
    self.globalAndLocalPostcondition(self.obj1611, rootNode)
    self.obj1611.postAction( rootNode.CREATE )

    self.obj1612=Attribute(self)
    self.obj1612.isGraphObjectVisual = True

    if(hasattr(self.obj1612, '_setHierarchicalLink')):
      self.obj1612._setHierarchicalLink(False)

    # Type
    self.obj1612.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1612.Type.config = 0

    # name
    self.obj1612.name.setValue('literal')

    self.obj1612.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(780.0,372.0,self.obj1612)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1612.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1612)
    self.globalAndLocalPostcondition(self.obj1612, rootNode)
    self.obj1612.postAction( rootNode.CREATE )

    self.obj1613=Attribute(self)
    self.obj1613.isGraphObjectVisual = True

    if(hasattr(self.obj1613, '_setHierarchicalLink')):
      self.obj1613._setHierarchicalLink(False)

    # Type
    self.obj1613.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1613.Type.config = 0

    # name
    self.obj1613.name.setValue('name')

    self.obj1613.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(240.0,280.0,self.obj1613)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1613.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1613)
    self.globalAndLocalPostcondition(self.obj1613, rootNode)
    self.obj1613.postAction( rootNode.CREATE )

    self.obj1614=Attribute(self)
    self.obj1614.isGraphObjectVisual = True

    if(hasattr(self.obj1614, '_setHierarchicalLink')):
      self.obj1614._setHierarchicalLink(False)

    # Type
    self.obj1614.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1614.Type.config = 0

    # name
    self.obj1614.name.setValue('pivotout')

    self.obj1614.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,500.0,self.obj1614)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1614.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1614)
    self.globalAndLocalPostcondition(self.obj1614, rootNode)
    self.obj1614.postAction( rootNode.CREATE )

    self.obj1615=Equation(self)
    self.obj1615.isGraphObjectVisual = True

    if(hasattr(self.obj1615, '_setHierarchicalLink')):
      self.obj1615._setHierarchicalLink(False)

    # name
    self.obj1615.name.setValue('eq2')

    self.obj1615.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(820.0,300.0,self.obj1615)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1615.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1615)
    self.globalAndLocalPostcondition(self.obj1615, rootNode)
    self.obj1615.postAction( rootNode.CREATE )

    self.obj1616=Equation(self)
    self.obj1616.isGraphObjectVisual = True

    if(hasattr(self.obj1616, '_setHierarchicalLink')):
      self.obj1616._setHierarchicalLink(False)

    # name
    self.obj1616.name.setValue('eq1')

    self.obj1616.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(540.0,280.0,self.obj1616)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1616.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1616)
    self.globalAndLocalPostcondition(self.obj1616, rootNode)
    self.obj1616.postAction( rootNode.CREATE )

    self.obj1617=Equation(self)
    self.obj1617.isGraphObjectVisual = True

    if(hasattr(self.obj1617, '_setHierarchicalLink')):
      self.obj1617._setHierarchicalLink(False)

    # name
    self.obj1617.name.setValue('eq3')

    self.obj1617.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(240.0,520.0,self.obj1617)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1617.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1617)
    self.globalAndLocalPostcondition(self.obj1617, rootNode)
    self.obj1617.postAction( rootNode.CREATE )

    self.obj1618=Concat(self)
    self.obj1618.isGraphObjectVisual = True

    if(hasattr(self.obj1618, '_setHierarchicalLink')):
      self.obj1618._setHierarchicalLink(False)

    # Type
    self.obj1618.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1618.Type.config = 0

    # name
    self.obj1618.name.setValue('concat1')

    self.obj1618.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(520.0,200.0,self.obj1618)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1618.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1618)
    self.globalAndLocalPostcondition(self.obj1618, rootNode)
    self.obj1618.postAction( rootNode.CREATE )

    self.obj1619=Constant(self)
    self.obj1619.isGraphObjectVisual = True

    if(hasattr(self.obj1619, '_setHierarchicalLink')):
      self.obj1619._setHierarchicalLink(False)

    # Type
    self.obj1619.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1619.Type.config = 0

    # name
    self.obj1619.name.setValue('sh')

    self.obj1619.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(860.0,440.0,self.obj1619)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1619.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1619)
    self.globalAndLocalPostcondition(self.obj1619, rootNode)
    self.obj1619.postAction( rootNode.CREATE )

    self.obj1620=Constant(self)
    self.obj1620.isGraphObjectVisual = True

    if(hasattr(self.obj1620, '_setHierarchicalLink')):
      self.obj1620._setHierarchicalLink(False)

    # Type
    self.obj1620.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1620.Type.config = 0

    # name
    self.obj1620.name.setValue('B')

    self.obj1620.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(363.0,200.0,self.obj1620)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1620.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1620)
    self.globalAndLocalPostcondition(self.obj1620, rootNode)
    self.obj1620.postAction( rootNode.CREATE )

    self.obj1621=Constant(self)
    self.obj1621.isGraphObjectVisual = True

    if(hasattr(self.obj1621, '_setHierarchicalLink')):
      self.obj1621._setHierarchicalLink(False)

    # Type
    self.obj1621.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1621.Type.config = 0

    # name
    self.obj1621.name.setValue('instfortrans')

    self.obj1621.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(400.0,480.0,self.obj1621)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1621.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1621)
    self.globalAndLocalPostcondition(self.obj1621, rootNode)
    self.obj1621.postAction( rootNode.CREATE )

    self.obj1622=paired_with(self)
    self.obj1622.isGraphObjectVisual = True

    if(hasattr(self.obj1622, '_setHierarchicalLink')):
      self.obj1622._setHierarchicalLink(False)

    self.obj1622.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj1622)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1622.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1622)
    self.globalAndLocalPostcondition(self.obj1622, rootNode)
    self.obj1622.postAction( rootNode.CREATE )

    self.obj1623=match_contains(self)
    self.obj1623.isGraphObjectVisual = True

    if(hasattr(self.obj1623, '_setHierarchicalLink')):
      self.obj1623._setHierarchicalLink(False)

    self.obj1623.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(238.0,60.0,self.obj1623)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1623.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1623)
    self.globalAndLocalPostcondition(self.obj1623, rootNode)
    self.obj1623.postAction( rootNode.CREATE )

    self.obj1624=match_contains(self)
    self.obj1624.isGraphObjectVisual = True

    if(hasattr(self.obj1624, '_setHierarchicalLink')):
      self.obj1624._setHierarchicalLink(False)

    self.obj1624.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(234.0,117.0,self.obj1624)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1624.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1624)
    self.globalAndLocalPostcondition(self.obj1624, rootNode)
    self.obj1624.postAction( rootNode.CREATE )

    self.obj1625=match_contains(self)
    self.obj1625.isGraphObjectVisual = True

    if(hasattr(self.obj1625, '_setHierarchicalLink')):
      self.obj1625._setHierarchicalLink(False)

    self.obj1625.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(465.0,50.5,self.obj1625)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1625.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1625)
    self.globalAndLocalPostcondition(self.obj1625, rootNode)
    self.obj1625.postAction( rootNode.CREATE )

    self.obj1626=match_contains(self)
    self.obj1626.isGraphObjectVisual = True

    if(hasattr(self.obj1626, '_setHierarchicalLink')):
      self.obj1626._setHierarchicalLink(False)

    self.obj1626.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(484.0,107.0,self.obj1626)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1626.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1626)
    self.globalAndLocalPostcondition(self.obj1626, rootNode)
    self.obj1626.postAction( rootNode.CREATE )

    self.obj1627=apply_contains(self)
    self.obj1627.isGraphObjectVisual = True

    if(hasattr(self.obj1627, '_setHierarchicalLink')):
      self.obj1627._setHierarchicalLink(False)

    self.obj1627.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(149.5,358.0,self.obj1627)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1627.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1627)
    self.globalAndLocalPostcondition(self.obj1627, rootNode)
    self.obj1627.postAction( rootNode.CREATE )

    self.obj1628=apply_contains(self)
    self.obj1628.isGraphObjectVisual = True

    if(hasattr(self.obj1628, '_setHierarchicalLink')):
      self.obj1628._setHierarchicalLink(False)

    self.obj1628.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(179.5,347.0,self.obj1628)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1628.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1628)
    self.globalAndLocalPostcondition(self.obj1628, rootNode)
    self.obj1628.postAction( rootNode.CREATE )

    self.obj1629=directLink_T(self)
    self.obj1629.isGraphObjectVisual = True

    if(hasattr(self.obj1629, '_setHierarchicalLink')):
      self.obj1629._setHierarchicalLink(False)

    # associationType
    self.obj1629.associationType.setValue('channelNames')

    self.obj1629.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(517.0,430.0,self.obj1629)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1629.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1629)
    self.globalAndLocalPostcondition(self.obj1629, rootNode)
    self.obj1629.postAction( rootNode.CREATE )

    self.obj1630=directLink_S(self)
    self.obj1630.isGraphObjectVisual = True

    if(hasattr(self.obj1630, '_setHierarchicalLink')):
      self.obj1630._setHierarchicalLink(False)

    # associationType
    self.obj1630.associationType.setValue('type')

    self.obj1630.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(330.0,133.0,self.obj1630)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1630.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1630)
    self.globalAndLocalPostcondition(self.obj1630, rootNode)
    self.obj1630.postAction( rootNode.CREATE )

    self.obj1631=directLink_S(self)
    self.obj1631.isGraphObjectVisual = True

    if(hasattr(self.obj1631, '_setHierarchicalLink')):
      self.obj1631._setHierarchicalLink(False)

    # associationType
    self.obj1631.associationType.setValue('owningStateMachine')

    self.obj1631.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(577.242375062,73.1510372393,self.obj1631)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1631.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1631)
    self.globalAndLocalPostcondition(self.obj1631, rootNode)
    self.obj1631.postAction( rootNode.CREATE )

    self.obj1632=directLink_S(self)
    self.obj1632.isGraphObjectVisual = True

    if(hasattr(self.obj1632, '_setHierarchicalLink')):
      self.obj1632._setHierarchicalLink(False)

    # associationType
    self.obj1632.associationType.setValue('exitPoints')

    self.obj1632.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(859.0,103.5,self.obj1632)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1632.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1632)
    self.globalAndLocalPostcondition(self.obj1632, rootNode)
    self.obj1632.postAction( rootNode.CREATE )

    self.obj1633=directLink_S(self)
    self.obj1633.isGraphObjectVisual = True

    if(hasattr(self.obj1633, '_setHierarchicalLink')):
      self.obj1633._setHierarchicalLink(False)

    # associationType
    self.obj1633.associationType.setValue('dest')

    self.obj1633.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(621.242375062,102.151037239,self.obj1633)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1633.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1633)
    self.globalAndLocalPostcondition(self.obj1633, rootNode)
    self.obj1633.postAction( rootNode.CREATE )

    self.obj1634=hasAttribute_S(self)
    self.obj1634.isGraphObjectVisual = True

    if(hasattr(self.obj1634, '_setHierarchicalLink')):
      self.obj1634._setHierarchicalLink(False)

    self.obj1634.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(692.0,158.5,self.obj1634)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1634.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1634)
    self.globalAndLocalPostcondition(self.obj1634, rootNode)
    self.obj1634.postAction( rootNode.CREATE )

    self.obj1635=hasAttribute_T(self)
    self.obj1635.isGraphObjectVisual = True

    if(hasattr(self.obj1635, '_setHierarchicalLink')):
      self.obj1635._setHierarchicalLink(False)

    self.obj1635.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(843.0,418.5,self.obj1635)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1635.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1635)
    self.globalAndLocalPostcondition(self.obj1635, rootNode)
    self.obj1635.postAction( rootNode.CREATE )

    self.obj1636=hasAttribute_T(self)
    self.obj1636.isGraphObjectVisual = True

    if(hasattr(self.obj1636, '_setHierarchicalLink')):
      self.obj1636._setHierarchicalLink(False)

    self.obj1636.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(363.0,392.5,self.obj1636)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1636.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1636)
    self.globalAndLocalPostcondition(self.obj1636, rootNode)
    self.obj1636.postAction( rootNode.CREATE )

    self.obj1637=hasAttribute_T(self)
    self.obj1637.isGraphObjectVisual = True

    if(hasattr(self.obj1637, '_setHierarchicalLink')):
      self.obj1637._setHierarchicalLink(False)

    self.obj1637.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(303.0,482.5,self.obj1637)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1637.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1637)
    self.globalAndLocalPostcondition(self.obj1637, rootNode)
    self.obj1637.postAction( rootNode.CREATE )

    self.obj1638=leftExpr(self)
    self.obj1638.isGraphObjectVisual = True

    if(hasattr(self.obj1638, '_setHierarchicalLink')):
      self.obj1638._setHierarchicalLink(False)

    self.obj1638.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(936.0,372.5,self.obj1638)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1638.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1638)
    self.globalAndLocalPostcondition(self.obj1638, rootNode)
    self.obj1638.postAction( rootNode.CREATE )

    self.obj1639=leftExpr(self)
    self.obj1639.isGraphObjectVisual = True

    if(hasattr(self.obj1639, '_setHierarchicalLink')):
      self.obj1639._setHierarchicalLink(False)

    self.obj1639.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(526.0,316.5,self.obj1639)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1639.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1639)
    self.globalAndLocalPostcondition(self.obj1639, rootNode)
    self.obj1639.postAction( rootNode.CREATE )

    self.obj1640=leftExpr(self)
    self.obj1640.isGraphObjectVisual = True

    if(hasattr(self.obj1640, '_setHierarchicalLink')):
      self.obj1640._setHierarchicalLink(False)

    self.obj1640.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,549.5,self.obj1640)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1640.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1640)
    self.globalAndLocalPostcondition(self.obj1640, rootNode)
    self.obj1640.postAction( rootNode.CREATE )

    self.obj1641=rightExpr(self)
    self.obj1641.isGraphObjectVisual = True

    if(hasattr(self.obj1641, '_setHierarchicalLink')):
      self.obj1641._setHierarchicalLink(False)

    self.obj1641.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(976.0,406.5,self.obj1641)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1641.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1641)
    self.globalAndLocalPostcondition(self.obj1641, rootNode)
    self.obj1641.postAction( rootNode.CREATE )

    self.obj1642=rightExpr(self)
    self.obj1642.isGraphObjectVisual = True

    if(hasattr(self.obj1642, '_setHierarchicalLink')):
      self.obj1642._setHierarchicalLink(False)

    self.obj1642.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(666.0,276.5,self.obj1642)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1642.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1642)
    self.globalAndLocalPostcondition(self.obj1642, rootNode)
    self.obj1642.postAction( rootNode.CREATE )

    self.obj1643=rightExpr(self)
    self.obj1643.isGraphObjectVisual = True

    if(hasattr(self.obj1643, '_setHierarchicalLink')):
      self.obj1643._setHierarchicalLink(False)

    self.obj1643.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(445.0,539.0,self.obj1643)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1643.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1643)
    self.globalAndLocalPostcondition(self.obj1643, rootNode)
    self.obj1643.postAction( rootNode.CREATE )

    self.obj1644=hasArgs(self)
    self.obj1644.isGraphObjectVisual = True

    if(hasattr(self.obj1644, '_setHierarchicalLink')):
      self.obj1644._setHierarchicalLink(False)

    self.obj1644.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(584.0,234.0,self.obj1644)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1644.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1644)
    self.globalAndLocalPostcondition(self.obj1644, rootNode)
    self.obj1644.postAction( rootNode.CREATE )

    self.obj1645=hasArgs(self)
    self.obj1645.isGraphObjectVisual = True

    if(hasattr(self.obj1645, '_setHierarchicalLink')):
      self.obj1645._setHierarchicalLink(False)

    self.obj1645.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(604.0,194.0,self.obj1645)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1645.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1645)
    self.globalAndLocalPostcondition(self.obj1645, rootNode)
    self.obj1645.postAction( rootNode.CREATE )

    # Connections for obj1603 (graphObject_: Obj852) of type MatchModel
    self.drawConnections(
(self.obj1603,self.obj1622,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj1603,self.obj1623,[138.0, 51.0, 238.0, 60.0],"true", 2),
(self.obj1603,self.obj1624,[138.0, 51.0, 234.0, 117.0],"true", 2),
(self.obj1603,self.obj1625,[138.0, 51.0, 465.0, 50.5],"true", 2),
(self.obj1603,self.obj1626,[138.0, 51.0, 484.0, 107.0],"true", 2) )
    # Connections for obj1604 (graphObject_: Obj853) of type ApplyModel
    self.drawConnections(
(self.obj1604,self.obj1627,[143.0, 273.0, 149.5, 358.0],"true", 2),
(self.obj1604,self.obj1628,[143.0, 273.0, 179.5, 347.0],"true", 2) )
    # Connections for obj1605 (graphObject_: Obj854) named vertex1
    self.drawConnections(
(self.obj1605,self.obj1634,[830.0, 163.0, 692.0, 158.5],"true", 2) )
    # Connections for obj1606 (graphObject_: Obj855) named transition1
    self.drawConnections(
(self.obj1606,self.obj1630,[324.48475012377082, 71.302074478633642, 330.0, 133.0],"true", 2),
(self.obj1606,self.obj1631,[324.48475012377082, 71.302074478633642, 577.24237506188547, 73.151037239316821],"true", 2),
(self.obj1606,self.obj1633,[324.48475012377082, 71.302074478633642, 621.24237506188547, 102.15103723931682],"true", 2) )
    # Connections for obj1607 (graphObject_: Obj856) named statemachine1
    self.drawConnections(
(self.obj1607,self.obj1632,[830.0, 68.0, 859.0, 103.5],"true", 2) )
    # Connections for obj1608 (graphObject_: Obj857) named out2_1
    self.drawConnections(
 )
    # Connections for obj1609 (graphObject_: Obj858) named name1
    self.drawConnections(
(self.obj1609,self.obj1635,[772.0, 431.0, 843.0, 418.5],"true", 2) )
    # Connections for obj1610 (graphObject_: Obj859) named inst1
    self.drawConnections(
(self.obj1610,self.obj1629,[372.0, 431.0, 517.0, 430.0],"true", 2),
(self.obj1610,self.obj1636,[372.0, 431.0, 363.0, 392.5],"true", 2),
(self.obj1610,self.obj1637,[372.0, 431.0, 303.0, 482.5],"true", 2) )
    # Connections for obj1611 (graphObject_: Obj860) named name
    self.drawConnections(
 )
    # Connections for obj1612 (graphObject_: Obj861) named literal
    self.drawConnections(
 )
    # Connections for obj1613 (graphObject_: Obj862) named name
    self.drawConnections(
 )
    # Connections for obj1614 (graphObject_: Obj863) named pivotout
    self.drawConnections(
 )
    # Connections for obj1615 (graphObject_: Obj864) named eq2
    self.drawConnections(
(self.obj1615,self.obj1638,[958.0, 339.0, 936.0, 372.5],"true", 2),
(self.obj1615,self.obj1641,[958.0, 339.0, 976.0, 406.5],"true", 2) )
    # Connections for obj1616 (graphObject_: Obj865) named eq1
    self.drawConnections(
(self.obj1616,self.obj1639,[678.0, 319.0, 526.0, 316.5],"true", 2),
(self.obj1616,self.obj1642,[678.0, 319.0, 666.0, 276.5],"true", 2) )
    # Connections for obj1617 (graphObject_: Obj866) named eq3
    self.drawConnections(
(self.obj1617,self.obj1640,[378.0, 559.0, 316.0, 549.5],"true", 2),
(self.obj1617,self.obj1643,[378.0, 559.0, 445.0, 539.0],"true", 2) )
    # Connections for obj1618 (graphObject_: Obj867) named concat1
    self.drawConnections(
(self.obj1618,self.obj1644,[654.0, 234.0, 584.0, 234.0],"true", 2),
(self.obj1618,self.obj1645,[654.0, 234.0, 604.0, 194.0],"true", 2) )
    # Connections for obj1619 (graphObject_: Obj868) named sh
    self.drawConnections(
 )
    # Connections for obj1620 (graphObject_: Obj869) named B
    self.drawConnections(
 )
    # Connections for obj1621 (graphObject_: Obj870) named instfortrans
    self.drawConnections(
 )
    # Connections for obj1622 (graphObject_: Obj871) of type paired_with
    self.drawConnections(
(self.obj1622,self.obj1604,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj1623 (graphObject_: Obj872) of type match_contains
    self.drawConnections(
(self.obj1623,self.obj1606,[234.0, 67.0, 324.48475012377082, 71.302074478633642],"true", 2) )
    # Connections for obj1624 (graphObject_: Obj873) of type match_contains
    self.drawConnections(
(self.obj1624,self.obj1608,[234.0, 117.0, 330.0, 164.0],"true", 2) )
    # Connections for obj1625 (graphObject_: Obj874) of type match_contains
    self.drawConnections(
(self.obj1625,self.obj1607,[465.0, 50.5, 830.0, 68.0],"true", 2) )
    # Connections for obj1626 (graphObject_: Obj875) of type match_contains
    self.drawConnections(
(self.obj1626,self.obj1605,[484.0, 107.0, 830.0, 163.0],"true", 2) )
    # Connections for obj1627 (graphObject_: Obj876) of type apply_contains
    self.drawConnections(
(self.obj1627,self.obj1610,[149.5, 358.0, 372.0, 431.0],"true", 2) )
    # Connections for obj1628 (graphObject_: Obj877) of type apply_contains
    self.drawConnections(
(self.obj1628,self.obj1609,[179.5, 347.0, 772.0, 431.0],"true", 2) )
    # Connections for obj1629 (graphObject_: Obj878) of type directLink_T
    self.drawConnections(
(self.obj1629,self.obj1609,[517.0, 430.0, 772.0, 431.0],"true", 2) )
    # Connections for obj1630 (graphObject_: Obj879) of type directLink_S
    self.drawConnections(
(self.obj1630,self.obj1608,[330.0, 133.0, 330.0, 164.0],"true", 2) )
    # Connections for obj1631 (graphObject_: Obj880) of type directLink_S
    self.drawConnections(
(self.obj1631,self.obj1607,[577.24237506188547, 73.151037239316821, 830.0, 68.0],"true", 2) )
    # Connections for obj1632 (graphObject_: Obj881) of type directLink_S
    self.drawConnections(
(self.obj1632,self.obj1605,[859.0, 103.5, 830.0, 163.0],"true", 2) )
    # Connections for obj1633 (graphObject_: Obj882) of type directLink_S
    self.drawConnections(
(self.obj1633,self.obj1605,[621.24237506188547, 102.15103723931682, 830.0, 163.0],"true", 2) )
    # Connections for obj1634 (graphObject_: Obj883) of type hasAttribute_S
    self.drawConnections(
(self.obj1634,self.obj1611,[692.0, 158.5, 554.0, 161.0],"true", 2) )
    # Connections for obj1635 (graphObject_: Obj884) of type hasAttribute_T
    self.drawConnections(
(self.obj1635,self.obj1612,[843.0, 418.5, 914.0, 406.0],"true", 2) )
    # Connections for obj1636 (graphObject_: Obj885) of type hasAttribute_T
    self.drawConnections(
(self.obj1636,self.obj1613,[363.0, 392.5, 374.0, 314.0],"true", 2) )
    # Connections for obj1637 (graphObject_: Obj886) of type hasAttribute_T
    self.drawConnections(
(self.obj1637,self.obj1614,[303.0, 482.5, 194.0, 534.0],"true", 2) )
    # Connections for obj1638 (graphObject_: Obj887) of type leftExpr
    self.drawConnections(
(self.obj1638,self.obj1612,[936.0, 372.5, 914.0, 406.0],"true", 2) )
    # Connections for obj1639 (graphObject_: Obj888) of type leftExpr
    self.drawConnections(
(self.obj1639,self.obj1613,[526.0, 316.5, 374.0, 314.0],"true", 2) )
    # Connections for obj1640 (graphObject_: Obj889) of type leftExpr
    self.drawConnections(
(self.obj1640,self.obj1614,[316.0, 549.5, 194.0, 534.0],"true", 2) )
    # Connections for obj1641 (graphObject_: Obj890) of type rightExpr
    self.drawConnections(
(self.obj1641,self.obj1619,[976.0, 406.5, 994.0, 474.0],"true", 2) )
    # Connections for obj1642 (graphObject_: Obj891) of type rightExpr
    self.drawConnections(
(self.obj1642,self.obj1618,[666.0, 276.5, 654.0, 234.0],"true", 2) )
    # Connections for obj1643 (graphObject_: Obj892) of type rightExpr
    self.drawConnections(
(self.obj1643,self.obj1621,[445.0, 539.0, 534.0, 514.0],"true", 2) )
    # Connections for obj1644 (graphObject_: Obj893) of type hasArgs
    self.drawConnections(
(self.obj1644,self.obj1620,[584.0, 234.0, 497.0, 234.0],"true", 2) )
    # Connections for obj1645 (graphObject_: Obj894) of type hasArgs
    self.drawConnections(
(self.obj1645,self.obj1611,[604.0, 194.0, 554.0, 161.0],"true", 2) )

newfunction = Transition2QInstOUT_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
