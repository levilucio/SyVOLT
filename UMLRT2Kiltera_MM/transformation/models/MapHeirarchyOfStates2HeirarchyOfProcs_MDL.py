"""
__MapHeirarchyOfStates2HeirarchyOfProcs_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 15:25:28 2014
___________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from State import *
from ProcDef import *
from LocalDef import *
from Attribute import *
from Equation import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from directLink_S import *
from backward_link import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from graph_Equation import *
from graph_match_contains import *
from graph_Attribute import *
from graph_LocalDef import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_directLink_S import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_hasAttribute_T import *
from graph_hasAttribute_S import *
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

def MapHeirarchyOfStates2HeirarchyOfProcs_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('MapHeirarchyOfStates2HeirarchyOfProcs')
    # --- ASG attributes over ---


    self.obj1866=MatchModel(self)
    self.obj1866.isGraphObjectVisual = True

    if(hasattr(self.obj1866, '_setHierarchicalLink')):
      self.obj1866._setHierarchicalLink(False)

    self.obj1866.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj1866)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1866.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1866)
    self.globalAndLocalPostcondition(self.obj1866, rootNode)
    self.obj1866.postAction( rootNode.CREATE )

    self.obj1867=ApplyModel(self)
    self.obj1867.isGraphObjectVisual = True

    if(hasattr(self.obj1867, '_setHierarchicalLink')):
      self.obj1867._setHierarchicalLink(False)

    self.obj1867.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,240.0,self.obj1867)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1867.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1867)
    self.globalAndLocalPostcondition(self.obj1867, rootNode)
    self.obj1867.postAction( rootNode.CREATE )

    self.obj1868=State(self)
    self.obj1868.isGraphObjectVisual = True

    if(hasattr(self.obj1868, '_setHierarchicalLink')):
      self.obj1868._setHierarchicalLink(False)

    # name
    self.obj1868.name.setValue('state1')

    # classtype
    self.obj1868.classtype.setValue('State')

    # cardinality
    self.obj1868.cardinality.setValue('+')

    self.obj1868.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,58.0,self.obj1868)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1868.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1868)
    self.globalAndLocalPostcondition(self.obj1868, rootNode)
    self.obj1868.postAction( rootNode.CREATE )

    self.obj1869=State(self)
    self.obj1869.isGraphObjectVisual = True

    if(hasattr(self.obj1869, '_setHierarchicalLink')):
      self.obj1869._setHierarchicalLink(False)

    # name
    self.obj1869.name.setValue('state2')

    # classtype
    self.obj1869.classtype.setValue('State')

    # cardinality
    self.obj1869.cardinality.setValue('+')

    self.obj1869.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(480.0,60.0,self.obj1869)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1869.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1869)
    self.globalAndLocalPostcondition(self.obj1869, rootNode)
    self.obj1869.postAction( rootNode.CREATE )

    self.obj1870=ProcDef(self)
    self.obj1870.isGraphObjectVisual = True

    if(hasattr(self.obj1870, '_setHierarchicalLink')):
      self.obj1870._setHierarchicalLink(False)

    # classtype
    self.obj1870.classtype.setValue('ProcDef')

    # cardinality
    self.obj1870.cardinality.setValue('1')

    # name
    self.obj1870.name.setValue('procDef1')

    self.obj1870.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(480.0,300.0,self.obj1870)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1870.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1870)
    self.globalAndLocalPostcondition(self.obj1870, rootNode)
    self.obj1870.postAction( rootNode.CREATE )

    self.obj1871=LocalDef(self)
    self.obj1871.isGraphObjectVisual = True

    if(hasattr(self.obj1871, '_setHierarchicalLink')):
      self.obj1871._setHierarchicalLink(False)

    # classtype
    self.obj1871.classtype.setValue('LocalDef')

    # cardinality
    self.obj1871.cardinality.setValue('1')

    # name
    self.obj1871.name.setValue('localDef1')

    self.obj1871.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(180.0,300.0,self.obj1871)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1871.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1871)
    self.globalAndLocalPostcondition(self.obj1871, rootNode)
    self.obj1871.postAction( rootNode.CREATE )

    self.obj1872=Attribute(self)
    self.obj1872.isGraphObjectVisual = True

    if(hasattr(self.obj1872, '_setHierarchicalLink')):
      self.obj1872._setHierarchicalLink(False)

    # Type
    self.obj1872.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1872.Type.config = 0

    # name
    self.obj1872.name.setValue('isComposite')

    self.obj1872.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(282.0,152.0,self.obj1872)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1872.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1872)
    self.globalAndLocalPostcondition(self.obj1872, rootNode)
    self.obj1872.postAction( rootNode.CREATE )

    self.obj1873=Attribute(self)
    self.obj1873.isGraphObjectVisual = True

    if(hasattr(self.obj1873, '_setHierarchicalLink')):
      self.obj1873._setHierarchicalLink(False)

    # Type
    self.obj1873.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1873.Type.config = 0

    # name
    self.obj1873.name.setValue('pivotin')

    self.obj1873.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(60.0,420.0,self.obj1873)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1873.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1873)
    self.globalAndLocalPostcondition(self.obj1873, rootNode)
    self.obj1873.postAction( rootNode.CREATE )

    self.obj1874=Attribute(self)
    self.obj1874.isGraphObjectVisual = True

    if(hasattr(self.obj1874, '_setHierarchicalLink')):
      self.obj1874._setHierarchicalLink(False)

    # Type
    self.obj1874.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1874.Type.config = 0

    # name
    self.obj1874.name.setValue('pivotin')

    self.obj1874.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(480.0,420.0,self.obj1874)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1874.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1874)
    self.globalAndLocalPostcondition(self.obj1874, rootNode)
    self.obj1874.postAction( rootNode.CREATE )

    self.obj1875=Equation(self)
    self.obj1875.isGraphObjectVisual = True

    if(hasattr(self.obj1875, '_setHierarchicalLink')):
      self.obj1875._setHierarchicalLink(False)

    # name
    self.obj1875.name.setValue('eq1')

    self.obj1875.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,220.0,self.obj1875)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1875.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1875)
    self.globalAndLocalPostcondition(self.obj1875, rootNode)
    self.obj1875.postAction( rootNode.CREATE )

    self.obj1876=Equation(self)
    self.obj1876.isGraphObjectVisual = True

    if(hasattr(self.obj1876, '_setHierarchicalLink')):
      self.obj1876._setHierarchicalLink(False)

    # name
    self.obj1876.name.setValue('eq2')

    self.obj1876.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,420.0,self.obj1876)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1876.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1876)
    self.globalAndLocalPostcondition(self.obj1876, rootNode)
    self.obj1876.postAction( rootNode.CREATE )

    self.obj1877=Equation(self)
    self.obj1877.isGraphObjectVisual = True

    if(hasattr(self.obj1877, '_setHierarchicalLink')):
      self.obj1877._setHierarchicalLink(False)

    # name
    self.obj1877.name.setValue('eq3')

    self.obj1877.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,420.0,self.obj1877)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1877.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1877)
    self.globalAndLocalPostcondition(self.obj1877, rootNode)
    self.obj1877.postAction( rootNode.CREATE )

    self.obj1878=Constant(self)
    self.obj1878.isGraphObjectVisual = True

    if(hasattr(self.obj1878, '_setHierarchicalLink')):
      self.obj1878._setHierarchicalLink(False)

    # Type
    self.obj1878.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1878.Type.config = 0

    # name
    self.obj1878.name.setValue('true')

    self.obj1878.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(459.0,152.0,self.obj1878)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1878.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1878)
    self.globalAndLocalPostcondition(self.obj1878, rootNode)
    self.obj1878.postAction( rootNode.CREATE )

    self.obj1879=Constant(self)
    self.obj1879.isGraphObjectVisual = True

    if(hasattr(self.obj1879, '_setHierarchicalLink')):
      self.obj1879._setHierarchicalLink(False)

    # Type
    self.obj1879.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1879.Type.config = 0

    # name
    self.obj1879.name.setValue('localdefcompstate')

    self.obj1879.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(200.0,500.0,self.obj1879)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1879.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1879)
    self.globalAndLocalPostcondition(self.obj1879, rootNode)
    self.obj1879.postAction( rootNode.CREATE )

    self.obj1880=Constant(self)
    self.obj1880.isGraphObjectVisual = True

    if(hasattr(self.obj1880, '_setHierarchicalLink')):
      self.obj1880._setHierarchicalLink(False)

    # Type
    self.obj1880.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1880.Type.config = 0

    # name
    self.obj1880.name.setValue('procdef')

    self.obj1880.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(600.0,500.0,self.obj1880)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1880.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1880)
    self.globalAndLocalPostcondition(self.obj1880, rootNode)
    self.obj1880.postAction( rootNode.CREATE )

    self.obj1881=paired_with(self)
    self.obj1881.isGraphObjectVisual = True

    if(hasattr(self.obj1881, '_setHierarchicalLink')):
      self.obj1881._setHierarchicalLink(False)

    self.obj1881.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,162.0,self.obj1881)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1881.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1881)
    self.globalAndLocalPostcondition(self.obj1881, rootNode)
    self.obj1881.postAction( rootNode.CREATE )

    self.obj1882=match_contains(self)
    self.obj1882.isGraphObjectVisual = True

    if(hasattr(self.obj1882, '_setHierarchicalLink')):
      self.obj1882._setHierarchicalLink(False)

    self.obj1882.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(250.0,76.0,self.obj1882)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1882.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1882)
    self.globalAndLocalPostcondition(self.obj1882, rootNode)
    self.obj1882.postAction( rootNode.CREATE )

    self.obj1883=match_contains(self)
    self.obj1883.isGraphObjectVisual = True

    if(hasattr(self.obj1883, '_setHierarchicalLink')):
      self.obj1883._setHierarchicalLink(False)

    self.obj1883.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,74.0,self.obj1883)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1883.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1883)
    self.globalAndLocalPostcondition(self.obj1883, rootNode)
    self.obj1883.postAction( rootNode.CREATE )

    self.obj1884=apply_contains(self)
    self.obj1884.isGraphObjectVisual = True

    if(hasattr(self.obj1884, '_setHierarchicalLink')):
      self.obj1884._setHierarchicalLink(False)

    self.obj1884.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,312.0,self.obj1884)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1884.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1884)
    self.globalAndLocalPostcondition(self.obj1884, rootNode)
    self.obj1884.postAction( rootNode.CREATE )

    self.obj1885=apply_contains(self)
    self.obj1885.isGraphObjectVisual = True

    if(hasattr(self.obj1885, '_setHierarchicalLink')):
      self.obj1885._setHierarchicalLink(False)

    self.obj1885.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(397.5,312.0,self.obj1885)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1885.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1885)
    self.globalAndLocalPostcondition(self.obj1885, rootNode)
    self.obj1885.postAction( rootNode.CREATE )

    self.obj1886=directLink_T(self)
    self.obj1886.isGraphObjectVisual = True

    if(hasattr(self.obj1886, '_setHierarchicalLink')):
      self.obj1886._setHierarchicalLink(False)

    # associationType
    self.obj1886.associationType.setValue('def')

    self.obj1886.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(502.0,351.0,self.obj1886)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1886.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1886)
    self.globalAndLocalPostcondition(self.obj1886, rootNode)
    self.obj1886.postAction( rootNode.CREATE )

    self.obj1887=directLink_S(self)
    self.obj1887.isGraphObjectVisual = True

    if(hasattr(self.obj1887, '_setHierarchicalLink')):
      self.obj1887._setHierarchicalLink(False)

    # associationType
    self.obj1887.associationType.setValue('states')

    self.obj1887.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(470.0,102.0,self.obj1887)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1887.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1887)
    self.globalAndLocalPostcondition(self.obj1887, rootNode)
    self.obj1887.postAction( rootNode.CREATE )

    self.obj1888=backward_link(self)
    self.obj1888.isGraphObjectVisual = True

    if(hasattr(self.obj1888, '_setHierarchicalLink')):
      self.obj1888._setHierarchicalLink(False)

    # type
    self.obj1888.type.setValue('ruleDef')

    self.obj1888.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(351.0,226.0,self.obj1888)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1888.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1888)
    self.globalAndLocalPostcondition(self.obj1888, rootNode)
    self.obj1888.postAction( rootNode.CREATE )

    self.obj1889=backward_link(self)
    self.obj1889.isGraphObjectVisual = True

    if(hasattr(self.obj1889, '_setHierarchicalLink')):
      self.obj1889._setHierarchicalLink(False)

    # type
    self.obj1889.type.setValue('ruleDef')

    self.obj1889.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(651.0,227.0,self.obj1889)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1889.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1889)
    self.globalAndLocalPostcondition(self.obj1889, rootNode)
    self.obj1889.postAction( rootNode.CREATE )

    self.obj1890=hasAttribute_S(self)
    self.obj1890.isGraphObjectVisual = True

    if(hasattr(self.obj1890, '_setHierarchicalLink')):
      self.obj1890._setHierarchicalLink(False)

    self.obj1890.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(377.5,137.5,self.obj1890)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1890.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1890)
    self.globalAndLocalPostcondition(self.obj1890, rootNode)
    self.obj1890.postAction( rootNode.CREATE )

    self.obj1891=hasAttribute_T(self)
    self.obj1891.isGraphObjectVisual = True

    if(hasattr(self.obj1891, '_setHierarchicalLink')):
      self.obj1891._setHierarchicalLink(False)

    self.obj1891.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(273.0,402.5,self.obj1891)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1891.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1891)
    self.globalAndLocalPostcondition(self.obj1891, rootNode)
    self.obj1891.postAction( rootNode.CREATE )

    self.obj1892=hasAttribute_T(self)
    self.obj1892.isGraphObjectVisual = True

    if(hasattr(self.obj1892, '_setHierarchicalLink')):
      self.obj1892._setHierarchicalLink(False)

    self.obj1892.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(633.0,402.5,self.obj1892)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1892.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1892)
    self.globalAndLocalPostcondition(self.obj1892, rootNode)
    self.obj1892.postAction( rootNode.CREATE )

    self.obj1893=leftExpr(self)
    self.obj1893.isGraphObjectVisual = True

    if(hasattr(self.obj1893, '_setHierarchicalLink')):
      self.obj1893._setHierarchicalLink(False)

    self.obj1893.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(439.5,219.0,self.obj1893)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1893.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1893)
    self.globalAndLocalPostcondition(self.obj1893, rootNode)
    self.obj1893.postAction( rootNode.CREATE )

    self.obj1894=leftExpr(self)
    self.obj1894.isGraphObjectVisual = True

    if(hasattr(self.obj1894, '_setHierarchicalLink')):
      self.obj1894._setHierarchicalLink(False)

    self.obj1894.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(316.0,456.5,self.obj1894)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1894.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1894)
    self.globalAndLocalPostcondition(self.obj1894, rootNode)
    self.obj1894.postAction( rootNode.CREATE )

    self.obj1895=leftExpr(self)
    self.obj1895.isGraphObjectVisual = True

    if(hasattr(self.obj1895, '_setHierarchicalLink')):
      self.obj1895._setHierarchicalLink(False)

    self.obj1895.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(696.0,456.5,self.obj1895)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1895.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1895)
    self.globalAndLocalPostcondition(self.obj1895, rootNode)
    self.obj1895.postAction( rootNode.CREATE )

    self.obj1896=rightExpr(self)
    self.obj1896.isGraphObjectVisual = True

    if(hasattr(self.obj1896, '_setHierarchicalLink')):
      self.obj1896._setHierarchicalLink(False)

    self.obj1896.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(519.0,236.0,self.obj1896)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1896.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1896)
    self.globalAndLocalPostcondition(self.obj1896, rootNode)
    self.obj1896.postAction( rootNode.CREATE )

    self.obj1897=rightExpr(self)
    self.obj1897.isGraphObjectVisual = True

    if(hasattr(self.obj1897, '_setHierarchicalLink')):
      self.obj1897._setHierarchicalLink(False)

    self.obj1897.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(386.0,496.5,self.obj1897)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1897.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1897)
    self.globalAndLocalPostcondition(self.obj1897, rootNode)
    self.obj1897.postAction( rootNode.CREATE )

    self.obj1898=rightExpr(self)
    self.obj1898.isGraphObjectVisual = True

    if(hasattr(self.obj1898, '_setHierarchicalLink')):
      self.obj1898._setHierarchicalLink(False)

    self.obj1898.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(756.0,496.5,self.obj1898)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1898.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1898)
    self.globalAndLocalPostcondition(self.obj1898, rootNode)
    self.obj1898.postAction( rootNode.CREATE )

    # Connections for obj1866 (graphObject_: Obj1035) of type MatchModel
    self.drawConnections(
(self.obj1866,self.obj1881,[138.0, 51.0, 140.5, 162.0],"true", 2),
(self.obj1866,self.obj1882,[138.0, 51.0, 250.0, 76.0],"true", 2),
(self.obj1866,self.obj1883,[138.0, 51.0, 394.0, 74.0],"true", 2) )
    # Connections for obj1867 (graphObject_: Obj1036) of type ApplyModel
    self.drawConnections(
(self.obj1867,self.obj1884,[143.0, 273.0, 247.5, 312.0],"true", 2),
(self.obj1867,self.obj1885,[143.0, 273.0, 397.5, 312.0],"true", 2) )
    # Connections for obj1868 (graphObject_: Obj1037) named state1
    self.drawConnections(
(self.obj1868,self.obj1887,[350.0, 101.0, 470.0, 102.0],"true", 2),
(self.obj1868,self.obj1890,[350.0, 101.0, 377.5, 137.5],"true", 2) )
    # Connections for obj1869 (graphObject_: Obj1038) named state2
    self.drawConnections(
 )
    # Connections for obj1870 (graphObject_: Obj1039) named procDef1
    self.drawConnections(
(self.obj1870,self.obj1889,[652.0, 351.0, 651.0, 227.0],"true", 2),
(self.obj1870,self.obj1892,[652.0, 351.0, 633.0, 402.5],"true", 2) )
    # Connections for obj1871 (graphObject_: Obj1040) named localDef1
    self.drawConnections(
(self.obj1871,self.obj1886,[352.0, 351.0, 502.0, 351.0],"true", 2),
(self.obj1871,self.obj1888,[352.0, 351.0, 351.0, 226.0],"true", 2),
(self.obj1871,self.obj1891,[352.0, 351.0, 273.0, 402.5],"true", 2) )
    # Connections for obj1872 (graphObject_: Obj1041) named isComposite
    self.drawConnections(
 )
    # Connections for obj1873 (graphObject_: Obj1042) named pivotin
    self.drawConnections(
 )
    # Connections for obj1874 (graphObject_: Obj1043) named pivotin
    self.drawConnections(
 )
    # Connections for obj1875 (graphObject_: Obj1044) named eq1
    self.drawConnections(
(self.obj1875,self.obj1893,[478.0, 259.0, 439.5, 219.0],"true", 2),
(self.obj1875,self.obj1896,[478.0, 259.0, 519.0, 236.0],"true", 2) )
    # Connections for obj1876 (graphObject_: Obj1045) named eq2
    self.drawConnections(
(self.obj1876,self.obj1894,[438.0, 459.0, 316.0, 456.5],"true", 2),
(self.obj1876,self.obj1897,[438.0, 459.0, 386.0, 496.5],"true", 2) )
    # Connections for obj1877 (graphObject_: Obj1046) named eq3
    self.drawConnections(
(self.obj1877,self.obj1895,[778.0, 459.0, 696.0, 456.5],"true", 2),
(self.obj1877,self.obj1898,[778.0, 459.0, 756.0, 496.5],"true", 2) )
    # Connections for obj1878 (graphObject_: Obj1047) named true
    self.drawConnections(
 )
    # Connections for obj1879 (graphObject_: Obj1048) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj1880 (graphObject_: Obj1049) named procdef
    self.drawConnections(
 )
    # Connections for obj1881 (graphObject_: Obj1050) of type paired_with
    self.drawConnections(
(self.obj1881,self.obj1867,[140.5, 162.0, 143.0, 273.0],"true", 2) )
    # Connections for obj1882 (graphObject_: Obj1051) of type match_contains
    self.drawConnections(
(self.obj1882,self.obj1868,[250.0, 76.0, 350.0, 101.0],"true", 2) )
    # Connections for obj1883 (graphObject_: Obj1052) of type match_contains
    self.drawConnections(
(self.obj1883,self.obj1869,[394.0, 74.0, 650.0, 103.0],"true", 2) )
    # Connections for obj1884 (graphObject_: Obj1053) of type apply_contains
    self.drawConnections(
(self.obj1884,self.obj1871,[247.5, 312.0, 352.0, 351.0],"true", 2) )
    # Connections for obj1885 (graphObject_: Obj1054) of type apply_contains
    self.drawConnections(
(self.obj1885,self.obj1870,[397.5, 312.0, 652.0, 351.0],"true", 2) )
    # Connections for obj1886 (graphObject_: Obj1055) of type directLink_T
    self.drawConnections(
(self.obj1886,self.obj1870,[502.0, 351.0, 652.0, 351.0],"true", 2) )
    # Connections for obj1887 (graphObject_: Obj1056) of type directLink_S
    self.drawConnections(
(self.obj1887,self.obj1869,[470.0, 102.0, 650.0, 103.0],"true", 2) )
    # Connections for obj1888 (graphObject_: Obj1057) of type backward_link
    self.drawConnections(
(self.obj1888,self.obj1868,[351.0, 226.0, 350.0, 101.0],"true", 2) )
    # Connections for obj1889 (graphObject_: Obj1058) of type backward_link
    self.drawConnections(
(self.obj1889,self.obj1869,[651.0, 227.0, 650.0, 103.0],"true", 2) )
    # Connections for obj1890 (graphObject_: Obj1059) of type hasAttribute_S
    self.drawConnections(
(self.obj1890,self.obj1872,[377.5, 137.5, 416.0, 186.0],"true", 2) )
    # Connections for obj1891 (graphObject_: Obj1060) of type hasAttribute_T
    self.drawConnections(
(self.obj1891,self.obj1873,[273.0, 402.5, 194.0, 454.0],"true", 2) )
    # Connections for obj1892 (graphObject_: Obj1061) of type hasAttribute_T
    self.drawConnections(
(self.obj1892,self.obj1874,[633.0, 402.5, 614.0, 454.0],"true", 2) )
    # Connections for obj1893 (graphObject_: Obj1062) of type leftExpr
    self.drawConnections(
(self.obj1893,self.obj1872,[439.5, 219.0, 416.0, 186.0],"true", 2) )
    # Connections for obj1894 (graphObject_: Obj1063) of type leftExpr
    self.drawConnections(
(self.obj1894,self.obj1873,[316.0, 456.5, 194.0, 454.0],"true", 2) )
    # Connections for obj1895 (graphObject_: Obj1064) of type leftExpr
    self.drawConnections(
(self.obj1895,self.obj1874,[696.0, 456.5, 614.0, 454.0],"true", 2) )
    # Connections for obj1896 (graphObject_: Obj1065) of type rightExpr
    self.drawConnections(
(self.obj1896,self.obj1878,[519.0, 236.0, 593.0, 186.0],"true", 2) )
    # Connections for obj1897 (graphObject_: Obj1066) of type rightExpr
    self.drawConnections(
(self.obj1897,self.obj1879,[386.0, 496.5, 334.0, 534.0],"true", 2) )
    # Connections for obj1898 (graphObject_: Obj1067) of type rightExpr
    self.drawConnections(
(self.obj1898,self.obj1880,[756.0, 496.5, 734.0, 534.0],"true", 2) )

newfunction = MapHeirarchyOfStates2HeirarchyOfProcs_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
