"""
__State2ProcDef_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 14:32:49 2014
___________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from State import *
from ProcDef import *
from Name import *
from Attribute import *
from Equation import *
from Concat import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from hasArgs import *
from graph_directLink_T import *
from graph_Name import *
from graph_hasAttribute_T import *
from graph_Attribute import *
from graph_hasAttribute_S import *
from graph_hasArgs import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_Equation import *
from graph_match_contains import *
from graph_Concat import *
from graph_leftExpr import *
from graph_ProcDef import *
from graph_Constant import *
from graph_ApplyModel import *
from graph_State import *
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

def State2ProcDef_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('State2ProcDef')
    # --- ASG attributes over ---


    self.obj863=MatchModel(self)
    self.obj863.isGraphObjectVisual = True

    if(hasattr(self.obj863, '_setHierarchicalLink')):
      self.obj863._setHierarchicalLink(False)

    self.obj863.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(120.0,40.0,self.obj863)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj863.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj863)
    self.globalAndLocalPostcondition(self.obj863, rootNode)
    self.obj863.postAction( rootNode.CREATE )

    self.obj864=ApplyModel(self)
    self.obj864.isGraphObjectVisual = True

    if(hasattr(self.obj864, '_setHierarchicalLink')):
      self.obj864._setHierarchicalLink(False)

    self.obj864.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(120.0,260.0,self.obj864)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj864.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj864)
    self.globalAndLocalPostcondition(self.obj864, rootNode)
    self.obj864.postAction( rootNode.CREATE )

    self.obj865=State(self)
    self.obj865.isGraphObjectVisual = True

    if(hasattr(self.obj865, '_setHierarchicalLink')):
      self.obj865._setHierarchicalLink(False)

    # name
    self.obj865.name.setValue('state1')

    # classtype
    self.obj865.classtype.setValue('State')

    # cardinality
    self.obj865.cardinality.setValue('+')

    self.obj865.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(400.0,80.0,self.obj865)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj865.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj865)
    self.globalAndLocalPostcondition(self.obj865, rootNode)
    self.obj865.postAction( rootNode.CREATE )

    self.obj866=ProcDef(self)
    self.obj866.isGraphObjectVisual = True

    if(hasattr(self.obj866, '_setHierarchicalLink')):
      self.obj866._setHierarchicalLink(False)

    # classtype
    self.obj866.classtype.setValue('ProcDef')

    # cardinality
    self.obj866.cardinality.setValue('1')

    # name
    self.obj866.name.setValue('procdef1')

    self.obj866.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(400.0,260.0,self.obj866)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj866.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj866)
    self.globalAndLocalPostcondition(self.obj866, rootNode)
    self.obj866.postAction( rootNode.CREATE )

    self.obj867=Name(self)
    self.obj867.isGraphObjectVisual = True

    if(hasattr(self.obj867, '_setHierarchicalLink')):
      self.obj867._setHierarchicalLink(False)

    # classtype
    self.obj867.classtype.setValue('Name')

    # cardinality
    self.obj867.cardinality.setValue('1')

    # name
    self.obj867.name.setValue('name1')

    self.obj867.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(260.0,460.0,self.obj867)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj867.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj867)
    self.globalAndLocalPostcondition(self.obj867, rootNode)
    self.obj867.postAction( rootNode.CREATE )

    self.obj868=Name(self)
    self.obj868.isGraphObjectVisual = True

    if(hasattr(self.obj868, '_setHierarchicalLink')):
      self.obj868._setHierarchicalLink(False)

    # classtype
    self.obj868.classtype.setValue('Name')

    # cardinality
    self.obj868.cardinality.setValue('1')

    # name
    self.obj868.name.setValue('name2')

    self.obj868.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(460.0,460.0,self.obj868)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj868.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj868)
    self.globalAndLocalPostcondition(self.obj868, rootNode)
    self.obj868.postAction( rootNode.CREATE )

    self.obj869=Name(self)
    self.obj869.isGraphObjectVisual = True

    if(hasattr(self.obj869, '_setHierarchicalLink')):
      self.obj869._setHierarchicalLink(False)

    # classtype
    self.obj869.classtype.setValue('Name')

    # cardinality
    self.obj869.cardinality.setValue('1')

    # name
    self.obj869.name.setValue('name3')

    self.obj869.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(660.0,460.0,self.obj869)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj869.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj869)
    self.globalAndLocalPostcondition(self.obj869, rootNode)
    self.obj869.postAction( rootNode.CREATE )

    self.obj870=Attribute(self)
    self.obj870.isGraphObjectVisual = True

    if(hasattr(self.obj870, '_setHierarchicalLink')):
      self.obj870._setHierarchicalLink(False)

    # Type
    self.obj870.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj870.Type.config = 0

    # name
    self.obj870.name.setValue('name')

    self.obj870.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,40.0,self.obj870)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj870.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj870)
    self.globalAndLocalPostcondition(self.obj870, rootNode)
    self.obj870.postAction( rootNode.CREATE )

    self.obj871=Attribute(self)
    self.obj871.isGraphObjectVisual = True

    if(hasattr(self.obj871, '_setHierarchicalLink')):
      self.obj871._setHierarchicalLink(False)

    # Type
    self.obj871.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj871.Type.config = 0

    # name
    self.obj871.name.setValue('name')

    self.obj871.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,280.0,self.obj871)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj871.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj871)
    self.globalAndLocalPostcondition(self.obj871, rootNode)
    self.obj871.postAction( rootNode.CREATE )

    self.obj872=Attribute(self)
    self.obj872.isGraphObjectVisual = True

    if(hasattr(self.obj872, '_setHierarchicalLink')):
      self.obj872._setHierarchicalLink(False)

    # Type
    self.obj872.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj872.Type.config = 0

    # name
    self.obj872.name.setValue('literal')

    self.obj872.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,560.0,self.obj872)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj872.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj872)
    self.globalAndLocalPostcondition(self.obj872, rootNode)
    self.obj872.postAction( rootNode.CREATE )

    self.obj873=Attribute(self)
    self.obj873.isGraphObjectVisual = True

    if(hasattr(self.obj873, '_setHierarchicalLink')):
      self.obj873._setHierarchicalLink(False)

    # Type
    self.obj873.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj873.Type.config = 0

    # name
    self.obj873.name.setValue('literal')

    self.obj873.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,560.0,self.obj873)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj873.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj873)
    self.globalAndLocalPostcondition(self.obj873, rootNode)
    self.obj873.postAction( rootNode.CREATE )

    self.obj874=Attribute(self)
    self.obj874.isGraphObjectVisual = True

    if(hasattr(self.obj874, '_setHierarchicalLink')):
      self.obj874._setHierarchicalLink(False)

    # Type
    self.obj874.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj874.Type.config = 0

    # name
    self.obj874.name.setValue('literal')

    self.obj874.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,560.0,self.obj874)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj874.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj874)
    self.globalAndLocalPostcondition(self.obj874, rootNode)
    self.obj874.postAction( rootNode.CREATE )

    self.obj875=Attribute(self)
    self.obj875.isGraphObjectVisual = True

    if(hasattr(self.obj875, '_setHierarchicalLink')):
      self.obj875._setHierarchicalLink(False)

    # Type
    self.obj875.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj875.Type.config = 0

    # name
    self.obj875.name.setValue('pivotout')

    self.obj875.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(740.0,360.0,self.obj875)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj875.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj875)
    self.globalAndLocalPostcondition(self.obj875, rootNode)
    self.obj875.postAction( rootNode.CREATE )

    self.obj876=Equation(self)
    self.obj876.isGraphObjectVisual = True

    if(hasattr(self.obj876, '_setHierarchicalLink')):
      self.obj876._setHierarchicalLink(False)

    # name
    self.obj876.name.setValue('eq1')

    self.obj876.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(880.0,240.0,self.obj876)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj876.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj876)
    self.globalAndLocalPostcondition(self.obj876, rootNode)
    self.obj876.postAction( rootNode.CREATE )

    self.obj877=Equation(self)
    self.obj877.isGraphObjectVisual = True

    if(hasattr(self.obj877, '_setHierarchicalLink')):
      self.obj877._setHierarchicalLink(False)

    # name
    self.obj877.name.setValue('eq2')

    self.obj877.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(20.0,640.0,self.obj877)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj877.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj877)
    self.globalAndLocalPostcondition(self.obj877, rootNode)
    self.obj877.postAction( rootNode.CREATE )

    self.obj878=Equation(self)
    self.obj878.isGraphObjectVisual = True

    if(hasattr(self.obj878, '_setHierarchicalLink')):
      self.obj878._setHierarchicalLink(False)

    # name
    self.obj878.name.setValue('eq3')

    self.obj878.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,600.0,self.obj878)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj878.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj878)
    self.globalAndLocalPostcondition(self.obj878, rootNode)
    self.obj878.postAction( rootNode.CREATE )

    self.obj879=Equation(self)
    self.obj879.isGraphObjectVisual = True

    if(hasattr(self.obj879, '_setHierarchicalLink')):
      self.obj879._setHierarchicalLink(False)

    # name
    self.obj879.name.setValue('eq4')

    self.obj879.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(860.0,600.0,self.obj879)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj879.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj879)
    self.globalAndLocalPostcondition(self.obj879, rootNode)
    self.obj879.postAction( rootNode.CREATE )

    self.obj880=Equation(self)
    self.obj880.isGraphObjectVisual = True

    if(hasattr(self.obj880, '_setHierarchicalLink')):
      self.obj880._setHierarchicalLink(False)

    # name
    self.obj880.name.setValue('eq5')

    self.obj880.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(900.0,360.0,self.obj880)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj880.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj880)
    self.globalAndLocalPostcondition(self.obj880, rootNode)
    self.obj880.postAction( rootNode.CREATE )

    self.obj881=Concat(self)
    self.obj881.isGraphObjectVisual = True

    if(hasattr(self.obj881, '_setHierarchicalLink')):
      self.obj881._setHierarchicalLink(False)

    # Type
    self.obj881.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj881.Type.config = 0

    # name
    self.obj881.name.setValue('concat1')

    self.obj881.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(680.0,140.0,self.obj881)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj881.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj881)
    self.globalAndLocalPostcondition(self.obj881, rootNode)
    self.obj881.postAction( rootNode.CREATE )

    self.obj882=Constant(self)
    self.obj882.isGraphObjectVisual = True

    if(hasattr(self.obj882, '_setHierarchicalLink')):
      self.obj882._setHierarchicalLink(False)

    # Type
    self.obj882.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj882.Type.config = 0

    # name
    self.obj882.name.setValue('S')

    self.obj882.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(860.0,40.0,self.obj882)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj882.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj882)
    self.globalAndLocalPostcondition(self.obj882, rootNode)
    self.obj882.postAction( rootNode.CREATE )

    self.obj883=Constant(self)
    self.obj883.isGraphObjectVisual = True

    if(hasattr(self.obj883, '_setHierarchicalLink')):
      self.obj883._setHierarchicalLink(False)

    # Type
    self.obj883.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj883.Type.config = 0

    # name
    self.obj883.name.setValue('enp')

    self.obj883.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(180.0,640.0,self.obj883)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj883.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj883)
    self.globalAndLocalPostcondition(self.obj883, rootNode)
    self.obj883.postAction( rootNode.CREATE )

    self.obj884=Constant(self)
    self.obj884.isGraphObjectVisual = True

    if(hasattr(self.obj884, '_setHierarchicalLink')):
      self.obj884._setHierarchicalLink(False)

    # Type
    self.obj884.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj884.Type.config = 0

    # name
    self.obj884.name.setValue('exit')

    self.obj884.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(500.0,640.0,self.obj884)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj884.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj884)
    self.globalAndLocalPostcondition(self.obj884, rootNode)
    self.obj884.postAction( rootNode.CREATE )

    self.obj885=Constant(self)
    self.obj885.isGraphObjectVisual = True

    if(hasattr(self.obj885, '_setHierarchicalLink')):
      self.obj885._setHierarchicalLink(False)

    # Type
    self.obj885.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj885.Type.config = 0

    # name
    self.obj885.name.setValue('exack')

    self.obj885.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(680.0,640.0,self.obj885)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj885.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj885)
    self.globalAndLocalPostcondition(self.obj885, rootNode)
    self.obj885.postAction( rootNode.CREATE )

    self.obj886=Constant(self)
    self.obj886.isGraphObjectVisual = True

    if(hasattr(self.obj886, '_setHierarchicalLink')):
      self.obj886._setHierarchicalLink(False)

    # Type
    self.obj886.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj886.Type.config = 0

    # name
    self.obj886.name.setValue('procdef')

    self.obj886.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(900.0,460.0,self.obj886)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj886.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj886)
    self.globalAndLocalPostcondition(self.obj886, rootNode)
    self.obj886.postAction( rootNode.CREATE )

    self.obj887=paired_with(self)
    self.obj887.isGraphObjectVisual = True

    if(hasattr(self.obj887, '_setHierarchicalLink')):
      self.obj887._setHierarchicalLink(False)

    self.obj887.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(240.5,182.0,self.obj887)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj887.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj887)
    self.globalAndLocalPostcondition(self.obj887, rootNode)
    self.obj887.postAction( rootNode.CREATE )

    self.obj888=match_contains(self)
    self.obj888.isGraphObjectVisual = True

    if(hasattr(self.obj888, '_setHierarchicalLink')):
      self.obj888._setHierarchicalLink(False)

    self.obj888.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(404.0,97.0,self.obj888)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj888.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj888)
    self.globalAndLocalPostcondition(self.obj888, rootNode)
    self.obj888.postAction( rootNode.CREATE )

    self.obj889=apply_contains(self)
    self.obj889.isGraphObjectVisual = True

    if(hasattr(self.obj889, '_setHierarchicalLink')):
      self.obj889._setHierarchicalLink(False)

    self.obj889.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(407.5,302.0,self.obj889)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj889.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj889)
    self.globalAndLocalPostcondition(self.obj889, rootNode)
    self.obj889.postAction( rootNode.CREATE )

    self.obj890=apply_contains(self)
    self.obj890.isGraphObjectVisual = True

    if(hasattr(self.obj890, '_setHierarchicalLink')):
      self.obj890._setHierarchicalLink(False)

    self.obj890.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(330.5,393.0,self.obj890)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj890.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj890)
    self.globalAndLocalPostcondition(self.obj890, rootNode)
    self.obj890.postAction( rootNode.CREATE )

    self.obj891=apply_contains(self)
    self.obj891.isGraphObjectVisual = True

    if(hasattr(self.obj891, '_setHierarchicalLink')):
      self.obj891._setHierarchicalLink(False)

    self.obj891.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(423.5,402.0,self.obj891)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj891.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj891)
    self.globalAndLocalPostcondition(self.obj891, rootNode)
    self.obj891.postAction( rootNode.CREATE )

    self.obj892=apply_contains(self)
    self.obj892.isGraphObjectVisual = True

    if(hasattr(self.obj892, '_setHierarchicalLink')):
      self.obj892._setHierarchicalLink(False)

    self.obj892.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(532.5,400.0,self.obj892)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj892.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj892)
    self.globalAndLocalPostcondition(self.obj892, rootNode)
    self.obj892.postAction( rootNode.CREATE )

    self.obj893=directLink_T(self)
    self.obj893.isGraphObjectVisual = True

    if(hasattr(self.obj893, '_setHierarchicalLink')):
      self.obj893._setHierarchicalLink(False)

    # associationType
    self.obj893.associationType.setValue('channelNames')

    self.obj893.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(502.0,391.0,self.obj893)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj893.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj893)
    self.globalAndLocalPostcondition(self.obj893, rootNode)
    self.obj893.postAction( rootNode.CREATE )

    self.obj894=directLink_T(self)
    self.obj894.isGraphObjectVisual = True

    if(hasattr(self.obj894, '_setHierarchicalLink')):
      self.obj894._setHierarchicalLink(False)

    # associationType
    self.obj894.associationType.setValue('channelNames')

    self.obj894.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(602.0,391.0,self.obj894)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj894.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj894)
    self.globalAndLocalPostcondition(self.obj894, rootNode)
    self.obj894.postAction( rootNode.CREATE )

    self.obj895=directLink_T(self)
    self.obj895.isGraphObjectVisual = True

    if(hasattr(self.obj895, '_setHierarchicalLink')):
      self.obj895._setHierarchicalLink(False)

    # associationType
    self.obj895.associationType.setValue('channelNames')

    self.obj895.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(687.0,398.0,self.obj895)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj895.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj895)
    self.globalAndLocalPostcondition(self.obj895, rootNode)
    self.obj895.postAction( rootNode.CREATE )

    self.obj896=hasAttribute_S(self)
    self.obj896.isGraphObjectVisual = True

    if(hasattr(self.obj896, '_setHierarchicalLink')):
      self.obj896._setHierarchicalLink(False)

    self.obj896.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(662.0,100.5,self.obj896)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj896.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj896)
    self.globalAndLocalPostcondition(self.obj896, rootNode)
    self.obj896.postAction( rootNode.CREATE )

    self.obj897=hasAttribute_T(self)
    self.obj897.isGraphObjectVisual = True

    if(hasattr(self.obj897, '_setHierarchicalLink')):
      self.obj897._setHierarchicalLink(False)

    self.obj897.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(693.0,312.5,self.obj897)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj897.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj897)
    self.globalAndLocalPostcondition(self.obj897, rootNode)
    self.obj897.postAction( rootNode.CREATE )

    self.obj898=hasAttribute_T(self)
    self.obj898.isGraphObjectVisual = True

    if(hasattr(self.obj898, '_setHierarchicalLink')):
      self.obj898._setHierarchicalLink(False)

    self.obj898.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(365.0,535.5,self.obj898)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj898.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj898)
    self.globalAndLocalPostcondition(self.obj898, rootNode)
    self.obj898.postAction( rootNode.CREATE )

    self.obj899=hasAttribute_T(self)
    self.obj899.isGraphObjectVisual = True

    if(hasattr(self.obj899, '_setHierarchicalLink')):
      self.obj899._setHierarchicalLink(False)

    self.obj899.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(639.0,530.5,self.obj899)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj899.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj899)
    self.globalAndLocalPostcondition(self.obj899, rootNode)
    self.obj899.postAction( rootNode.CREATE )

    self.obj900=hasAttribute_T(self)
    self.obj900.isGraphObjectVisual = True

    if(hasattr(self.obj900, '_setHierarchicalLink')):
      self.obj900._setHierarchicalLink(False)

    self.obj900.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(823.0,532.5,self.obj900)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj900.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj900)
    self.globalAndLocalPostcondition(self.obj900, rootNode)
    self.obj900.postAction( rootNode.CREATE )

    self.obj901=hasAttribute_T(self)
    self.obj901.isGraphObjectVisual = True

    if(hasattr(self.obj901, '_setHierarchicalLink')):
      self.obj901._setHierarchicalLink(False)

    self.obj901.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(722.0,381.5,self.obj901)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj901.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj901)
    self.globalAndLocalPostcondition(self.obj901, rootNode)
    self.obj901.postAction( rootNode.CREATE )

    self.obj902=leftExpr(self)
    self.obj902.isGraphObjectVisual = True

    if(hasattr(self.obj902, '_setHierarchicalLink')):
      self.obj902._setHierarchicalLink(False)

    self.obj902.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(916.0,296.5,self.obj902)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj902.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj902)
    self.globalAndLocalPostcondition(self.obj902, rootNode)
    self.obj902.postAction( rootNode.CREATE )

    self.obj903=leftExpr(self)
    self.obj903.isGraphObjectVisual = True

    if(hasattr(self.obj903, '_setHierarchicalLink')):
      self.obj903._setHierarchicalLink(False)

    self.obj903.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(246.0,636.5,self.obj903)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj903.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj903)
    self.globalAndLocalPostcondition(self.obj903, rootNode)
    self.obj903.postAction( rootNode.CREATE )

    self.obj904=leftExpr(self)
    self.obj904.isGraphObjectVisual = True

    if(hasattr(self.obj904, '_setHierarchicalLink')):
      self.obj904._setHierarchicalLink(False)

    self.obj904.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(556.0,616.5,self.obj904)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj904.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj904)
    self.globalAndLocalPostcondition(self.obj904, rootNode)
    self.obj904.postAction( rootNode.CREATE )

    self.obj905=leftExpr(self)
    self.obj905.isGraphObjectVisual = True

    if(hasattr(self.obj905, '_setHierarchicalLink')):
      self.obj905._setHierarchicalLink(False)

    self.obj905.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(906.0,616.5,self.obj905)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj905.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj905)
    self.globalAndLocalPostcondition(self.obj905, rootNode)
    self.obj905.postAction( rootNode.CREATE )

    self.obj906=leftExpr(self)
    self.obj906.isGraphObjectVisual = True

    if(hasattr(self.obj906, '_setHierarchicalLink')):
      self.obj906._setHierarchicalLink(False)

    self.obj906.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,396.5,self.obj906)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj906.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj906)
    self.globalAndLocalPostcondition(self.obj906, rootNode)
    self.obj906.postAction( rootNode.CREATE )

    self.obj907=rightExpr(self)
    self.obj907.isGraphObjectVisual = True

    if(hasattr(self.obj907, '_setHierarchicalLink')):
      self.obj907._setHierarchicalLink(False)

    self.obj907.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(916.0,226.5,self.obj907)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj907.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj907)
    self.globalAndLocalPostcondition(self.obj907, rootNode)
    self.obj907.postAction( rootNode.CREATE )

    self.obj908=rightExpr(self)
    self.obj908.isGraphObjectVisual = True

    if(hasattr(self.obj908, '_setHierarchicalLink')):
      self.obj908._setHierarchicalLink(False)

    self.obj908.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(282.0,676.5,self.obj908)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj908.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj908)
    self.globalAndLocalPostcondition(self.obj908, rootNode)
    self.obj908.postAction( rootNode.CREATE )

    self.obj909=rightExpr(self)
    self.obj909.isGraphObjectVisual = True

    if(hasattr(self.obj909, '_setHierarchicalLink')):
      self.obj909._setHierarchicalLink(False)

    self.obj909.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(556.0,656.5,self.obj909)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj909.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj909)
    self.globalAndLocalPostcondition(self.obj909, rootNode)
    self.obj909.postAction( rootNode.CREATE )

    self.obj910=rightExpr(self)
    self.obj910.isGraphObjectVisual = True

    if(hasattr(self.obj910, '_setHierarchicalLink')):
      self.obj910._setHierarchicalLink(False)

    self.obj910.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(906.0,656.5,self.obj910)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj910.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj910)
    self.globalAndLocalPostcondition(self.obj910, rootNode)
    self.obj910.postAction( rootNode.CREATE )

    self.obj911=rightExpr(self)
    self.obj911.isGraphObjectVisual = True

    if(hasattr(self.obj911, '_setHierarchicalLink')):
      self.obj911._setHierarchicalLink(False)

    self.obj911.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1036.0,446.5,self.obj911)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj911.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj911)
    self.globalAndLocalPostcondition(self.obj911, rootNode)
    self.obj911.postAction( rootNode.CREATE )

    self.obj912=hasArgs(self)
    self.obj912.isGraphObjectVisual = True

    if(hasattr(self.obj912, '_setHierarchicalLink')):
      self.obj912._setHierarchicalLink(False)

    self.obj912.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(904.0,124.0,self.obj912)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj912.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj912)
    self.globalAndLocalPostcondition(self.obj912, rootNode)
    self.obj912.postAction( rootNode.CREATE )

    self.obj913=hasArgs(self)
    self.obj913.isGraphObjectVisual = True

    if(hasattr(self.obj913, '_setHierarchicalLink')):
      self.obj913._setHierarchicalLink(False)

    self.obj913.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(814.0,124.0,self.obj913)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj913.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj913)
    self.globalAndLocalPostcondition(self.obj913, rootNode)
    self.obj913.postAction( rootNode.CREATE )

    # Connections for obj863 (graphObject_: Obj220) of type MatchModel
    self.drawConnections(
(self.obj863,self.obj887,[238.0, 71.0, 240.5, 182.0],"true", 2),
(self.obj863,self.obj888,[238.0, 71.0, 404.0, 97.0],"true", 2) )
    # Connections for obj864 (graphObject_: Obj221) of type ApplyModel
    self.drawConnections(
(self.obj864,self.obj889,[243.0, 293.0, 407.5, 302.0],"true", 2),
(self.obj864,self.obj890,[243.0, 293.0, 330.5, 393.0],"true", 2),
(self.obj864,self.obj891,[243.0, 293.0, 423.5, 402.0],"true", 2),
(self.obj864,self.obj892,[243.0, 293.0, 532.5, 400.0],"true", 2) )
    # Connections for obj865 (graphObject_: Obj222) named state1
    self.drawConnections(
(self.obj865,self.obj896,[570.0, 123.0, 662.0, 100.5],"true", 2) )
    # Connections for obj866 (graphObject_: Obj223) named procdef1
    self.drawConnections(
(self.obj866,self.obj897,[572.0, 311.0, 693.0, 312.5],"true", 2),
(self.obj866,self.obj893,[572.0, 311.0, 502.0, 391.0],"true", 2),
(self.obj866,self.obj894,[572.0, 311.0, 602.0, 391.0],"true", 2),
(self.obj866,self.obj895,[572.0, 311.0, 687.0, 398.0],"true", 2),
(self.obj866,self.obj901,[572.0, 311.0, 722.0, 381.5],"true", 2) )
    # Connections for obj867 (graphObject_: Obj224) named name1
    self.drawConnections(
(self.obj867,self.obj898,[432.0, 511.0, 365.0, 535.5],"true", 2) )
    # Connections for obj868 (graphObject_: Obj225) named name2
    self.drawConnections(
(self.obj868,self.obj899,[632.0, 511.0, 639.0, 530.5],"true", 2) )
    # Connections for obj869 (graphObject_: Obj226) named name3
    self.drawConnections(
(self.obj869,self.obj900,[832.0, 511.0, 823.0, 532.5],"true", 2) )
    # Connections for obj870 (graphObject_: Obj227) named name
    self.drawConnections(
 )
    # Connections for obj871 (graphObject_: Obj228) named name
    self.drawConnections(
 )
    # Connections for obj872 (graphObject_: Obj229) named literal
    self.drawConnections(
 )
    # Connections for obj873 (graphObject_: Obj230) named literal
    self.drawConnections(
 )
    # Connections for obj874 (graphObject_: Obj231) named literal
    self.drawConnections(
 )
    # Connections for obj875 (graphObject_: Obj232) named pivotout
    self.drawConnections(
 )
    # Connections for obj876 (graphObject_: Obj233) named eq1
    self.drawConnections(
(self.obj876,self.obj902,[1018.0, 279.0, 916.0, 296.5],"true", 2),
(self.obj876,self.obj907,[1018.0, 279.0, 916.0, 226.5],"true", 2) )
    # Connections for obj877 (graphObject_: Obj234) named eq2
    self.drawConnections(
(self.obj877,self.obj903,[158.0, 679.0, 246.0, 636.5],"true", 2),
(self.obj877,self.obj908,[158.0, 679.0, 282.0, 676.5],"true", 2) )
    # Connections for obj878 (graphObject_: Obj235) named eq3
    self.drawConnections(
(self.obj878,self.obj909,[478.0, 639.0, 556.0, 656.5],"true", 2),
(self.obj878,self.obj904,[478.0, 639.0, 556.0, 616.5],"true", 2) )
    # Connections for obj879 (graphObject_: Obj236) named eq4
    self.drawConnections(
(self.obj879,self.obj905,[998.0, 639.0, 906.0, 616.5],"true", 2),
(self.obj879,self.obj910,[998.0, 639.0, 906.0, 656.5],"true", 2) )
    # Connections for obj880 (graphObject_: Obj237) named eq5
    self.drawConnections(
(self.obj880,self.obj906,[1038.0, 399.0, 956.0, 396.5],"true", 2),
(self.obj880,self.obj911,[1038.0, 399.0, 1036.0, 446.5],"true", 2) )
    # Connections for obj881 (graphObject_: Obj238) named concat1
    self.drawConnections(
(self.obj881,self.obj912,[814.0, 174.0, 904.0, 124.0],"true", 2),
(self.obj881,self.obj913,[814.0, 174.0, 814.0, 124.0],"true", 2) )
    # Connections for obj882 (graphObject_: Obj239) named S
    self.drawConnections(
 )
    # Connections for obj883 (graphObject_: Obj240) named enp
    self.drawConnections(
 )
    # Connections for obj884 (graphObject_: Obj241) named exit
    self.drawConnections(
 )
    # Connections for obj885 (graphObject_: Obj242) named exack
    self.drawConnections(
 )
    # Connections for obj886 (graphObject_: Obj243) named procdef
    self.drawConnections(
 )
    # Connections for obj887 (graphObject_: Obj244) of type paired_with
    self.drawConnections(
(self.obj887,self.obj864,[240.5, 182.0, 243.0, 293.0],"true", 2) )
    # Connections for obj888 (graphObject_: Obj245) of type match_contains
    self.drawConnections(
(self.obj888,self.obj865,[404.0, 97.0, 570.0, 123.0],"true", 2) )
    # Connections for obj889 (graphObject_: Obj246) of type apply_contains
    self.drawConnections(
(self.obj889,self.obj866,[407.5, 302.0, 572.0, 311.0],"true", 2) )
    # Connections for obj890 (graphObject_: Obj247) of type apply_contains
    self.drawConnections(
(self.obj890,self.obj867,[330.5, 393.0, 432.0, 511.0],"true", 2) )
    # Connections for obj891 (graphObject_: Obj248) of type apply_contains
    self.drawConnections(
(self.obj891,self.obj868,[423.5, 402.0, 632.0, 511.0],"true", 2) )
    # Connections for obj892 (graphObject_: Obj249) of type apply_contains
    self.drawConnections(
(self.obj892,self.obj869,[532.5, 400.0, 832.0, 511.0],"true", 2) )
    # Connections for obj893 (graphObject_: Obj250) of type directLink_T
    self.drawConnections(
(self.obj893,self.obj867,[502.0, 391.0, 432.0, 511.0],"true", 2) )
    # Connections for obj894 (graphObject_: Obj251) of type directLink_T
    self.drawConnections(
(self.obj894,self.obj868,[602.0, 391.0, 632.0, 511.0],"true", 2) )
    # Connections for obj895 (graphObject_: Obj252) of type directLink_T
    self.drawConnections(
(self.obj895,self.obj869,[687.0, 398.0, 832.0, 511.0],"true", 2) )
    # Connections for obj896 (graphObject_: Obj253) of type hasAttribute_S
    self.drawConnections(
(self.obj896,self.obj870,[662.0, 100.5, 814.0, 74.0],"true", 2) )
    # Connections for obj897 (graphObject_: Obj254) of type hasAttribute_T
    self.drawConnections(
(self.obj897,self.obj871,[693.0, 312.5, 814.0, 314.0],"true", 2) )
    # Connections for obj898 (graphObject_: Obj255) of type hasAttribute_T
    self.drawConnections(
(self.obj898,self.obj872,[365.0, 535.5, 314.0, 594.0],"true", 2) )
    # Connections for obj899 (graphObject_: Obj256) of type hasAttribute_T
    self.drawConnections(
(self.obj899,self.obj873,[639.0, 530.5, 634.0, 594.0],"true", 2) )
    # Connections for obj900 (graphObject_: Obj257) of type hasAttribute_T
    self.drawConnections(
(self.obj900,self.obj874,[823.0, 532.5, 814.0, 594.0],"true", 2) )
    # Connections for obj901 (graphObject_: Obj258) of type hasAttribute_T
    self.drawConnections(
(self.obj901,self.obj875,[722.0, 381.5, 874.0, 394.0],"true", 2) )
    # Connections for obj902 (graphObject_: Obj259) of type leftExpr
    self.drawConnections(
(self.obj902,self.obj871,[916.0, 296.5, 814.0, 314.0],"true", 2) )
    # Connections for obj903 (graphObject_: Obj260) of type leftExpr
    self.drawConnections(
(self.obj903,self.obj872,[246.0, 636.5, 314.0, 594.0],"true", 2) )
    # Connections for obj904 (graphObject_: Obj261) of type leftExpr
    self.drawConnections(
(self.obj904,self.obj873,[556.0, 616.5, 634.0, 594.0],"true", 2) )
    # Connections for obj905 (graphObject_: Obj262) of type leftExpr
    self.drawConnections(
(self.obj905,self.obj874,[906.0, 616.5, 814.0, 594.0],"true", 2) )
    # Connections for obj906 (graphObject_: Obj263) of type leftExpr
    self.drawConnections(
(self.obj906,self.obj875,[956.0, 396.5, 874.0, 394.0],"true", 2) )
    # Connections for obj907 (graphObject_: Obj264) of type rightExpr
    self.drawConnections(
(self.obj907,self.obj881,[916.0, 226.5, 814.0, 174.0],"true", 2) )
    # Connections for obj908 (graphObject_: Obj265) of type rightExpr
    self.drawConnections(
(self.obj908,self.obj883,[282.0, 676.5, 314.0, 674.0],"true", 2) )
    # Connections for obj909 (graphObject_: Obj266) of type rightExpr
    self.drawConnections(
(self.obj909,self.obj884,[556.0, 656.5, 634.0, 674.0],"true", 2) )
    # Connections for obj910 (graphObject_: Obj267) of type rightExpr
    self.drawConnections(
(self.obj910,self.obj885,[906.0, 656.5, 814.0, 674.0],"true", 2) )
    # Connections for obj911 (graphObject_: Obj268) of type rightExpr
    self.drawConnections(
(self.obj911,self.obj886,[1036.0, 446.5, 1034.0, 494.0],"true", 2) )
    # Connections for obj912 (graphObject_: Obj269) of type hasArgs
    self.drawConnections(
(self.obj912,self.obj882,[904.0, 124.0, 994.0, 74.0],"true", 2) )
    # Connections for obj913 (graphObject_: Obj270) of type hasArgs
    self.drawConnections(
(self.obj913,self.obj870,[814.0, 124.0, 814.0, 74.0],"true", 2) )

newfunction = State2ProcDef_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
