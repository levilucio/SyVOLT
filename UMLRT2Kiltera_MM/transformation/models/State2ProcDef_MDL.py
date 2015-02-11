"""
__State2ProcDef_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:18:50 2015
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


    self.obj837=MatchModel(self)
    self.obj837.isGraphObjectVisual = True

    if(hasattr(self.obj837, '_setHierarchicalLink')):
      self.obj837._setHierarchicalLink(False)

    self.obj837.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(120.0,40.0,self.obj837)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj837.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj837)
    self.globalAndLocalPostcondition(self.obj837, rootNode)
    self.obj837.postAction( rootNode.CREATE )

    self.obj838=ApplyModel(self)
    self.obj838.isGraphObjectVisual = True

    if(hasattr(self.obj838, '_setHierarchicalLink')):
      self.obj838._setHierarchicalLink(False)

    self.obj838.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(120.0,260.0,self.obj838)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj838.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj838)
    self.globalAndLocalPostcondition(self.obj838, rootNode)
    self.obj838.postAction( rootNode.CREATE )

    self.obj839=State(self)
    self.obj839.isGraphObjectVisual = True

    if(hasattr(self.obj839, '_setHierarchicalLink')):
      self.obj839._setHierarchicalLink(False)

    # name
    self.obj839.name.setValue('state1')

    # classtype
    self.obj839.classtype.setValue('State')

    # cardinality
    self.obj839.cardinality.setValue('+')

    self.obj839.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(400.0,80.0,self.obj839)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj839.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj839)
    self.globalAndLocalPostcondition(self.obj839, rootNode)
    self.obj839.postAction( rootNode.CREATE )

    self.obj840=ProcDef(self)
    self.obj840.isGraphObjectVisual = True

    if(hasattr(self.obj840, '_setHierarchicalLink')):
      self.obj840._setHierarchicalLink(False)

    # classtype
    self.obj840.classtype.setValue('ProcDef')

    # cardinality
    self.obj840.cardinality.setValue('1')

    # name
    self.obj840.name.setValue('procdef1')

    self.obj840.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(400.0,260.0,self.obj840)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj840.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj840)
    self.globalAndLocalPostcondition(self.obj840, rootNode)
    self.obj840.postAction( rootNode.CREATE )

    self.obj841=Name(self)
    self.obj841.isGraphObjectVisual = True

    if(hasattr(self.obj841, '_setHierarchicalLink')):
      self.obj841._setHierarchicalLink(False)

    # classtype
    self.obj841.classtype.setValue('Name')

    # cardinality
    self.obj841.cardinality.setValue('1')

    # name
    self.obj841.name.setValue('name1')

    self.obj841.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(260.0,460.0,self.obj841)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj841.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj841)
    self.globalAndLocalPostcondition(self.obj841, rootNode)
    self.obj841.postAction( rootNode.CREATE )

    self.obj842=Name(self)
    self.obj842.isGraphObjectVisual = True

    if(hasattr(self.obj842, '_setHierarchicalLink')):
      self.obj842._setHierarchicalLink(False)

    # classtype
    self.obj842.classtype.setValue('Name')

    # cardinality
    self.obj842.cardinality.setValue('1')

    # name
    self.obj842.name.setValue('name2')

    self.obj842.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(460.0,460.0,self.obj842)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj842.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj842)
    self.globalAndLocalPostcondition(self.obj842, rootNode)
    self.obj842.postAction( rootNode.CREATE )

    self.obj843=Name(self)
    self.obj843.isGraphObjectVisual = True

    if(hasattr(self.obj843, '_setHierarchicalLink')):
      self.obj843._setHierarchicalLink(False)

    # classtype
    self.obj843.classtype.setValue('Name')

    # cardinality
    self.obj843.cardinality.setValue('1')

    # name
    self.obj843.name.setValue('name3')

    self.obj843.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(660.0,460.0,self.obj843)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj843.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj843)
    self.globalAndLocalPostcondition(self.obj843, rootNode)
    self.obj843.postAction( rootNode.CREATE )

    self.obj844=Attribute(self)
    self.obj844.isGraphObjectVisual = True

    if(hasattr(self.obj844, '_setHierarchicalLink')):
      self.obj844._setHierarchicalLink(False)

    # Type
    self.obj844.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj844.Type.config = 0

    # name
    self.obj844.name.setValue('name')

    self.obj844.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,40.0,self.obj844)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj844.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj844)
    self.globalAndLocalPostcondition(self.obj844, rootNode)
    self.obj844.postAction( rootNode.CREATE )

    self.obj845=Attribute(self)
    self.obj845.isGraphObjectVisual = True

    if(hasattr(self.obj845, '_setHierarchicalLink')):
      self.obj845._setHierarchicalLink(False)

    # Type
    self.obj845.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj845.Type.config = 0

    # name
    self.obj845.name.setValue('name')

    self.obj845.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,280.0,self.obj845)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj845.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj845)
    self.globalAndLocalPostcondition(self.obj845, rootNode)
    self.obj845.postAction( rootNode.CREATE )

    self.obj846=Attribute(self)
    self.obj846.isGraphObjectVisual = True

    if(hasattr(self.obj846, '_setHierarchicalLink')):
      self.obj846._setHierarchicalLink(False)

    # Type
    self.obj846.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj846.Type.config = 0

    # name
    self.obj846.name.setValue('literal')

    self.obj846.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,560.0,self.obj846)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj846.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj846)
    self.globalAndLocalPostcondition(self.obj846, rootNode)
    self.obj846.postAction( rootNode.CREATE )

    self.obj847=Attribute(self)
    self.obj847.isGraphObjectVisual = True

    if(hasattr(self.obj847, '_setHierarchicalLink')):
      self.obj847._setHierarchicalLink(False)

    # Type
    self.obj847.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj847.Type.config = 0

    # name
    self.obj847.name.setValue('literal')

    self.obj847.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,560.0,self.obj847)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj847.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj847)
    self.globalAndLocalPostcondition(self.obj847, rootNode)
    self.obj847.postAction( rootNode.CREATE )

    self.obj848=Attribute(self)
    self.obj848.isGraphObjectVisual = True

    if(hasattr(self.obj848, '_setHierarchicalLink')):
      self.obj848._setHierarchicalLink(False)

    # Type
    self.obj848.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj848.Type.config = 0

    # name
    self.obj848.name.setValue('literal')

    self.obj848.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(680.0,560.0,self.obj848)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj848.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj848)
    self.globalAndLocalPostcondition(self.obj848, rootNode)
    self.obj848.postAction( rootNode.CREATE )

    self.obj849=Attribute(self)
    self.obj849.isGraphObjectVisual = True

    if(hasattr(self.obj849, '_setHierarchicalLink')):
      self.obj849._setHierarchicalLink(False)

    # Type
    self.obj849.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj849.Type.config = 0

    # name
    self.obj849.name.setValue('pivot')

    self.obj849.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(740.0,360.0,self.obj849)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj849.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj849)
    self.globalAndLocalPostcondition(self.obj849, rootNode)
    self.obj849.postAction( rootNode.CREATE )

    self.obj850=Equation(self)
    self.obj850.isGraphObjectVisual = True

    if(hasattr(self.obj850, '_setHierarchicalLink')):
      self.obj850._setHierarchicalLink(False)

    # name
    self.obj850.name.setValue('eq1')

    self.obj850.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(880.0,240.0,self.obj850)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj850.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj850)
    self.globalAndLocalPostcondition(self.obj850, rootNode)
    self.obj850.postAction( rootNode.CREATE )

    self.obj851=Equation(self)
    self.obj851.isGraphObjectVisual = True

    if(hasattr(self.obj851, '_setHierarchicalLink')):
      self.obj851._setHierarchicalLink(False)

    # name
    self.obj851.name.setValue('eq2')

    self.obj851.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(20.0,640.0,self.obj851)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj851.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj851)
    self.globalAndLocalPostcondition(self.obj851, rootNode)
    self.obj851.postAction( rootNode.CREATE )

    self.obj852=Equation(self)
    self.obj852.isGraphObjectVisual = True

    if(hasattr(self.obj852, '_setHierarchicalLink')):
      self.obj852._setHierarchicalLink(False)

    # name
    self.obj852.name.setValue('eq3')

    self.obj852.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(340.0,600.0,self.obj852)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj852.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj852)
    self.globalAndLocalPostcondition(self.obj852, rootNode)
    self.obj852.postAction( rootNode.CREATE )

    self.obj853=Equation(self)
    self.obj853.isGraphObjectVisual = True

    if(hasattr(self.obj853, '_setHierarchicalLink')):
      self.obj853._setHierarchicalLink(False)

    # name
    self.obj853.name.setValue('eq4')

    self.obj853.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(860.0,600.0,self.obj853)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj853.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj853)
    self.globalAndLocalPostcondition(self.obj853, rootNode)
    self.obj853.postAction( rootNode.CREATE )

    self.obj854=Equation(self)
    self.obj854.isGraphObjectVisual = True

    if(hasattr(self.obj854, '_setHierarchicalLink')):
      self.obj854._setHierarchicalLink(False)

    # name
    self.obj854.name.setValue('eq5')

    self.obj854.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(900.0,360.0,self.obj854)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj854.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj854)
    self.globalAndLocalPostcondition(self.obj854, rootNode)
    self.obj854.postAction( rootNode.CREATE )

    self.obj855=Concat(self)
    self.obj855.isGraphObjectVisual = True

    if(hasattr(self.obj855, '_setHierarchicalLink')):
      self.obj855._setHierarchicalLink(False)

    # Type
    self.obj855.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj855.Type.config = 0

    # name
    self.obj855.name.setValue('concat1')

    self.obj855.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(680.0,140.0,self.obj855)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj855.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj855)
    self.globalAndLocalPostcondition(self.obj855, rootNode)
    self.obj855.postAction( rootNode.CREATE )

    self.obj856=Constant(self)
    self.obj856.isGraphObjectVisual = True

    if(hasattr(self.obj856, '_setHierarchicalLink')):
      self.obj856._setHierarchicalLink(False)

    # Type
    self.obj856.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj856.Type.config = 0

    # name
    self.obj856.name.setValue('S')

    self.obj856.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(860.0,40.0,self.obj856)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj856.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj856)
    self.globalAndLocalPostcondition(self.obj856, rootNode)
    self.obj856.postAction( rootNode.CREATE )

    self.obj857=Constant(self)
    self.obj857.isGraphObjectVisual = True

    if(hasattr(self.obj857, '_setHierarchicalLink')):
      self.obj857._setHierarchicalLink(False)

    # Type
    self.obj857.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj857.Type.config = 0

    # name
    self.obj857.name.setValue('enp')

    self.obj857.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(180.0,640.0,self.obj857)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj857.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj857)
    self.globalAndLocalPostcondition(self.obj857, rootNode)
    self.obj857.postAction( rootNode.CREATE )

    self.obj858=Constant(self)
    self.obj858.isGraphObjectVisual = True

    if(hasattr(self.obj858, '_setHierarchicalLink')):
      self.obj858._setHierarchicalLink(False)

    # Type
    self.obj858.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj858.Type.config = 0

    # name
    self.obj858.name.setValue('exit')

    self.obj858.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(500.0,640.0,self.obj858)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj858.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj858)
    self.globalAndLocalPostcondition(self.obj858, rootNode)
    self.obj858.postAction( rootNode.CREATE )

    self.obj859=Constant(self)
    self.obj859.isGraphObjectVisual = True

    if(hasattr(self.obj859, '_setHierarchicalLink')):
      self.obj859._setHierarchicalLink(False)

    # Type
    self.obj859.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj859.Type.config = 0

    # name
    self.obj859.name.setValue('exack')

    self.obj859.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(680.0,640.0,self.obj859)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj859.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj859)
    self.globalAndLocalPostcondition(self.obj859, rootNode)
    self.obj859.postAction( rootNode.CREATE )

    self.obj860=Constant(self)
    self.obj860.isGraphObjectVisual = True

    if(hasattr(self.obj860, '_setHierarchicalLink')):
      self.obj860._setHierarchicalLink(False)

    # Type
    self.obj860.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj860.Type.config = 0

    # name
    self.obj860.name.setValue('procdef')

    self.obj860.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(900.0,460.0,self.obj860)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj860.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj860)
    self.globalAndLocalPostcondition(self.obj860, rootNode)
    self.obj860.postAction( rootNode.CREATE )

    self.obj861=paired_with(self)
    self.obj861.isGraphObjectVisual = True

    if(hasattr(self.obj861, '_setHierarchicalLink')):
      self.obj861._setHierarchicalLink(False)

    self.obj861.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(240.5,182.0,self.obj861)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj861.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj861)
    self.globalAndLocalPostcondition(self.obj861, rootNode)
    self.obj861.postAction( rootNode.CREATE )

    self.obj862=match_contains(self)
    self.obj862.isGraphObjectVisual = True

    if(hasattr(self.obj862, '_setHierarchicalLink')):
      self.obj862._setHierarchicalLink(False)

    self.obj862.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(404.0,97.0,self.obj862)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj862.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj862)
    self.globalAndLocalPostcondition(self.obj862, rootNode)
    self.obj862.postAction( rootNode.CREATE )

    self.obj863=apply_contains(self)
    self.obj863.isGraphObjectVisual = True

    if(hasattr(self.obj863, '_setHierarchicalLink')):
      self.obj863._setHierarchicalLink(False)

    self.obj863.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(407.5,302.0,self.obj863)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj863.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj863)
    self.globalAndLocalPostcondition(self.obj863, rootNode)
    self.obj863.postAction( rootNode.CREATE )

    self.obj864=apply_contains(self)
    self.obj864.isGraphObjectVisual = True

    if(hasattr(self.obj864, '_setHierarchicalLink')):
      self.obj864._setHierarchicalLink(False)

    self.obj864.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(330.5,393.0,self.obj864)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj864.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj864)
    self.globalAndLocalPostcondition(self.obj864, rootNode)
    self.obj864.postAction( rootNode.CREATE )

    self.obj865=apply_contains(self)
    self.obj865.isGraphObjectVisual = True

    if(hasattr(self.obj865, '_setHierarchicalLink')):
      self.obj865._setHierarchicalLink(False)

    self.obj865.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(423.5,402.0,self.obj865)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj865.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj865)
    self.globalAndLocalPostcondition(self.obj865, rootNode)
    self.obj865.postAction( rootNode.CREATE )

    self.obj866=apply_contains(self)
    self.obj866.isGraphObjectVisual = True

    if(hasattr(self.obj866, '_setHierarchicalLink')):
      self.obj866._setHierarchicalLink(False)

    self.obj866.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(532.5,400.0,self.obj866)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj866.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj866)
    self.globalAndLocalPostcondition(self.obj866, rootNode)
    self.obj866.postAction( rootNode.CREATE )

    self.obj867=directLink_T(self)
    self.obj867.isGraphObjectVisual = True

    if(hasattr(self.obj867, '_setHierarchicalLink')):
      self.obj867._setHierarchicalLink(False)

    # associationType
    self.obj867.associationType.setValue('channelNames')

    self.obj867.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(502.0,391.0,self.obj867)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj867.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj867)
    self.globalAndLocalPostcondition(self.obj867, rootNode)
    self.obj867.postAction( rootNode.CREATE )

    self.obj868=directLink_T(self)
    self.obj868.isGraphObjectVisual = True

    if(hasattr(self.obj868, '_setHierarchicalLink')):
      self.obj868._setHierarchicalLink(False)

    # associationType
    self.obj868.associationType.setValue('channelNames')

    self.obj868.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(602.0,391.0,self.obj868)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj868.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj868)
    self.globalAndLocalPostcondition(self.obj868, rootNode)
    self.obj868.postAction( rootNode.CREATE )

    self.obj869=directLink_T(self)
    self.obj869.isGraphObjectVisual = True

    if(hasattr(self.obj869, '_setHierarchicalLink')):
      self.obj869._setHierarchicalLink(False)

    # associationType
    self.obj869.associationType.setValue('channelNames')

    self.obj869.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(687.0,398.0,self.obj869)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj869.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj869)
    self.globalAndLocalPostcondition(self.obj869, rootNode)
    self.obj869.postAction( rootNode.CREATE )

    self.obj870=hasAttribute_S(self)
    self.obj870.isGraphObjectVisual = True

    if(hasattr(self.obj870, '_setHierarchicalLink')):
      self.obj870._setHierarchicalLink(False)

    self.obj870.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(662.0,100.5,self.obj870)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj870.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj870)
    self.globalAndLocalPostcondition(self.obj870, rootNode)
    self.obj870.postAction( rootNode.CREATE )

    self.obj871=hasAttribute_T(self)
    self.obj871.isGraphObjectVisual = True

    if(hasattr(self.obj871, '_setHierarchicalLink')):
      self.obj871._setHierarchicalLink(False)

    self.obj871.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(693.0,312.5,self.obj871)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj871.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj871)
    self.globalAndLocalPostcondition(self.obj871, rootNode)
    self.obj871.postAction( rootNode.CREATE )

    self.obj872=hasAttribute_T(self)
    self.obj872.isGraphObjectVisual = True

    if(hasattr(self.obj872, '_setHierarchicalLink')):
      self.obj872._setHierarchicalLink(False)

    self.obj872.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(365.0,535.5,self.obj872)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj872.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj872)
    self.globalAndLocalPostcondition(self.obj872, rootNode)
    self.obj872.postAction( rootNode.CREATE )

    self.obj873=hasAttribute_T(self)
    self.obj873.isGraphObjectVisual = True

    if(hasattr(self.obj873, '_setHierarchicalLink')):
      self.obj873._setHierarchicalLink(False)

    self.obj873.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(639.0,530.5,self.obj873)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj873.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj873)
    self.globalAndLocalPostcondition(self.obj873, rootNode)
    self.obj873.postAction( rootNode.CREATE )

    self.obj874=hasAttribute_T(self)
    self.obj874.isGraphObjectVisual = True

    if(hasattr(self.obj874, '_setHierarchicalLink')):
      self.obj874._setHierarchicalLink(False)

    self.obj874.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(823.0,532.5,self.obj874)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj874.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj874)
    self.globalAndLocalPostcondition(self.obj874, rootNode)
    self.obj874.postAction( rootNode.CREATE )

    self.obj875=hasAttribute_T(self)
    self.obj875.isGraphObjectVisual = True

    if(hasattr(self.obj875, '_setHierarchicalLink')):
      self.obj875._setHierarchicalLink(False)

    self.obj875.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(722.0,381.5,self.obj875)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj875.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj875)
    self.globalAndLocalPostcondition(self.obj875, rootNode)
    self.obj875.postAction( rootNode.CREATE )

    self.obj876=leftExpr(self)
    self.obj876.isGraphObjectVisual = True

    if(hasattr(self.obj876, '_setHierarchicalLink')):
      self.obj876._setHierarchicalLink(False)

    self.obj876.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(916.0,296.5,self.obj876)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj876.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj876)
    self.globalAndLocalPostcondition(self.obj876, rootNode)
    self.obj876.postAction( rootNode.CREATE )

    self.obj877=leftExpr(self)
    self.obj877.isGraphObjectVisual = True

    if(hasattr(self.obj877, '_setHierarchicalLink')):
      self.obj877._setHierarchicalLink(False)

    self.obj877.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(246.0,636.5,self.obj877)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj877.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj877)
    self.globalAndLocalPostcondition(self.obj877, rootNode)
    self.obj877.postAction( rootNode.CREATE )

    self.obj878=leftExpr(self)
    self.obj878.isGraphObjectVisual = True

    if(hasattr(self.obj878, '_setHierarchicalLink')):
      self.obj878._setHierarchicalLink(False)

    self.obj878.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(556.0,616.5,self.obj878)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj878.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj878)
    self.globalAndLocalPostcondition(self.obj878, rootNode)
    self.obj878.postAction( rootNode.CREATE )

    self.obj879=leftExpr(self)
    self.obj879.isGraphObjectVisual = True

    if(hasattr(self.obj879, '_setHierarchicalLink')):
      self.obj879._setHierarchicalLink(False)

    self.obj879.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(906.0,616.5,self.obj879)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj879.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj879)
    self.globalAndLocalPostcondition(self.obj879, rootNode)
    self.obj879.postAction( rootNode.CREATE )

    self.obj880=leftExpr(self)
    self.obj880.isGraphObjectVisual = True

    if(hasattr(self.obj880, '_setHierarchicalLink')):
      self.obj880._setHierarchicalLink(False)

    self.obj880.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(956.0,396.5,self.obj880)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj880.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj880)
    self.globalAndLocalPostcondition(self.obj880, rootNode)
    self.obj880.postAction( rootNode.CREATE )

    self.obj881=rightExpr(self)
    self.obj881.isGraphObjectVisual = True

    if(hasattr(self.obj881, '_setHierarchicalLink')):
      self.obj881._setHierarchicalLink(False)

    self.obj881.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(916.0,226.5,self.obj881)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj881.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj881)
    self.globalAndLocalPostcondition(self.obj881, rootNode)
    self.obj881.postAction( rootNode.CREATE )

    self.obj882=rightExpr(self)
    self.obj882.isGraphObjectVisual = True

    if(hasattr(self.obj882, '_setHierarchicalLink')):
      self.obj882._setHierarchicalLink(False)

    self.obj882.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(282.0,676.5,self.obj882)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj882.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj882)
    self.globalAndLocalPostcondition(self.obj882, rootNode)
    self.obj882.postAction( rootNode.CREATE )

    self.obj883=rightExpr(self)
    self.obj883.isGraphObjectVisual = True

    if(hasattr(self.obj883, '_setHierarchicalLink')):
      self.obj883._setHierarchicalLink(False)

    self.obj883.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(556.0,656.5,self.obj883)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj883.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj883)
    self.globalAndLocalPostcondition(self.obj883, rootNode)
    self.obj883.postAction( rootNode.CREATE )

    self.obj884=rightExpr(self)
    self.obj884.isGraphObjectVisual = True

    if(hasattr(self.obj884, '_setHierarchicalLink')):
      self.obj884._setHierarchicalLink(False)

    self.obj884.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(906.0,656.5,self.obj884)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj884.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj884)
    self.globalAndLocalPostcondition(self.obj884, rootNode)
    self.obj884.postAction( rootNode.CREATE )

    self.obj885=rightExpr(self)
    self.obj885.isGraphObjectVisual = True

    if(hasattr(self.obj885, '_setHierarchicalLink')):
      self.obj885._setHierarchicalLink(False)

    self.obj885.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1036.0,446.5,self.obj885)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj885.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj885)
    self.globalAndLocalPostcondition(self.obj885, rootNode)
    self.obj885.postAction( rootNode.CREATE )

    self.obj886=hasArgs(self)
    self.obj886.isGraphObjectVisual = True

    if(hasattr(self.obj886, '_setHierarchicalLink')):
      self.obj886._setHierarchicalLink(False)

    self.obj886.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(904.0,124.0,self.obj886)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj886.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj886)
    self.globalAndLocalPostcondition(self.obj886, rootNode)
    self.obj886.postAction( rootNode.CREATE )

    self.obj887=hasArgs(self)
    self.obj887.isGraphObjectVisual = True

    if(hasattr(self.obj887, '_setHierarchicalLink')):
      self.obj887._setHierarchicalLink(False)

    self.obj887.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(814.0,124.0,self.obj887)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj887.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj887)
    self.globalAndLocalPostcondition(self.obj887, rootNode)
    self.obj887.postAction( rootNode.CREATE )

    # Connections for obj837 (graphObject_: Obj676) of type MatchModel
    self.drawConnections(
(self.obj837,self.obj861,[238.0, 71.0, 240.5, 182.0],"true", 2),
(self.obj837,self.obj862,[238.0, 71.0, 404.0, 97.0],"true", 2) )
    # Connections for obj838 (graphObject_: Obj677) of type ApplyModel
    self.drawConnections(
(self.obj838,self.obj863,[243.0, 293.0, 407.5, 302.0],"true", 2),
(self.obj838,self.obj864,[243.0, 293.0, 330.5, 393.0],"true", 2),
(self.obj838,self.obj865,[243.0, 293.0, 423.5, 402.0],"true", 2),
(self.obj838,self.obj866,[243.0, 293.0, 532.5, 400.0],"true", 2) )
    # Connections for obj839 (graphObject_: Obj678) named state1
    self.drawConnections(
(self.obj839,self.obj870,[570.0, 123.0, 662.0, 100.5],"true", 2) )
    # Connections for obj840 (graphObject_: Obj679) named procdef1
    self.drawConnections(
(self.obj840,self.obj871,[572.0, 311.0, 693.0, 312.5],"true", 2),
(self.obj840,self.obj867,[572.0, 311.0, 502.0, 391.0],"true", 2),
(self.obj840,self.obj868,[572.0, 311.0, 602.0, 391.0],"true", 2),
(self.obj840,self.obj869,[572.0, 311.0, 687.0, 398.0],"true", 2),
(self.obj840,self.obj875,[572.0, 311.0, 722.0, 381.5],"true", 2) )
    # Connections for obj841 (graphObject_: Obj680) named name1
    self.drawConnections(
(self.obj841,self.obj872,[432.0, 511.0, 365.0, 535.5],"true", 2) )
    # Connections for obj842 (graphObject_: Obj681) named name2
    self.drawConnections(
(self.obj842,self.obj873,[632.0, 511.0, 639.0, 530.5],"true", 2) )
    # Connections for obj843 (graphObject_: Obj682) named name3
    self.drawConnections(
(self.obj843,self.obj874,[832.0, 511.0, 823.0, 532.5],"true", 2) )
    # Connections for obj844 (graphObject_: Obj683) named name
    self.drawConnections(
 )
    # Connections for obj845 (graphObject_: Obj684) named name
    self.drawConnections(
 )
    # Connections for obj846 (graphObject_: Obj685) named literal
    self.drawConnections(
 )
    # Connections for obj847 (graphObject_: Obj686) named literal
    self.drawConnections(
 )
    # Connections for obj848 (graphObject_: Obj687) named literal
    self.drawConnections(
 )
    # Connections for obj849 (graphObject_: Obj688) named pivot
    self.drawConnections(
 )
    # Connections for obj850 (graphObject_: Obj689) named eq1
    self.drawConnections(
(self.obj850,self.obj876,[1018.0, 279.0, 916.0, 296.5],"true", 2),
(self.obj850,self.obj881,[1018.0, 279.0, 916.0, 226.5],"true", 2) )
    # Connections for obj851 (graphObject_: Obj690) named eq2
    self.drawConnections(
(self.obj851,self.obj877,[158.0, 679.0, 246.0, 636.5],"true", 2),
(self.obj851,self.obj882,[158.0, 679.0, 282.0, 676.5],"true", 2) )
    # Connections for obj852 (graphObject_: Obj691) named eq3
    self.drawConnections(
(self.obj852,self.obj883,[478.0, 639.0, 556.0, 656.5],"true", 2),
(self.obj852,self.obj878,[478.0, 639.0, 556.0, 616.5],"true", 2) )
    # Connections for obj853 (graphObject_: Obj692) named eq4
    self.drawConnections(
(self.obj853,self.obj879,[998.0, 639.0, 906.0, 616.5],"true", 2),
(self.obj853,self.obj884,[998.0, 639.0, 906.0, 656.5],"true", 2) )
    # Connections for obj854 (graphObject_: Obj693) named eq5
    self.drawConnections(
(self.obj854,self.obj880,[1038.0, 399.0, 956.0, 396.5],"true", 2),
(self.obj854,self.obj885,[1038.0, 399.0, 1036.0, 446.5],"true", 2) )
    # Connections for obj855 (graphObject_: Obj694) named concat1
    self.drawConnections(
(self.obj855,self.obj886,[814.0, 174.0, 904.0, 124.0],"true", 2),
(self.obj855,self.obj887,[814.0, 174.0, 814.0, 124.0],"true", 2) )
    # Connections for obj856 (graphObject_: Obj695) named S
    self.drawConnections(
 )
    # Connections for obj857 (graphObject_: Obj696) named enp
    self.drawConnections(
 )
    # Connections for obj858 (graphObject_: Obj697) named exit
    self.drawConnections(
 )
    # Connections for obj859 (graphObject_: Obj698) named exack
    self.drawConnections(
 )
    # Connections for obj860 (graphObject_: Obj699) named procdef
    self.drawConnections(
 )
    # Connections for obj861 (graphObject_: Obj700) of type paired_with
    self.drawConnections(
(self.obj861,self.obj838,[240.5, 182.0, 243.0, 293.0],"true", 2) )
    # Connections for obj862 (graphObject_: Obj701) of type match_contains
    self.drawConnections(
(self.obj862,self.obj839,[404.0, 97.0, 570.0, 123.0],"true", 2) )
    # Connections for obj863 (graphObject_: Obj702) of type apply_contains
    self.drawConnections(
(self.obj863,self.obj840,[407.5, 302.0, 572.0, 311.0],"true", 2) )
    # Connections for obj864 (graphObject_: Obj703) of type apply_contains
    self.drawConnections(
(self.obj864,self.obj841,[330.5, 393.0, 432.0, 511.0],"true", 2) )
    # Connections for obj865 (graphObject_: Obj704) of type apply_contains
    self.drawConnections(
(self.obj865,self.obj842,[423.5, 402.0, 632.0, 511.0],"true", 2) )
    # Connections for obj866 (graphObject_: Obj705) of type apply_contains
    self.drawConnections(
(self.obj866,self.obj843,[532.5, 400.0, 832.0, 511.0],"true", 2) )
    # Connections for obj867 (graphObject_: Obj706) of type directLink_T
    self.drawConnections(
(self.obj867,self.obj841,[502.0, 391.0, 432.0, 511.0],"true", 2) )
    # Connections for obj868 (graphObject_: Obj707) of type directLink_T
    self.drawConnections(
(self.obj868,self.obj842,[602.0, 391.0, 632.0, 511.0],"true", 2) )
    # Connections for obj869 (graphObject_: Obj708) of type directLink_T
    self.drawConnections(
(self.obj869,self.obj843,[687.0, 398.0, 832.0, 511.0],"true", 2) )
    # Connections for obj870 (graphObject_: Obj709) of type hasAttribute_S
    self.drawConnections(
(self.obj870,self.obj844,[662.0, 100.5, 814.0, 74.0],"true", 2) )
    # Connections for obj871 (graphObject_: Obj710) of type hasAttribute_T
    self.drawConnections(
(self.obj871,self.obj845,[693.0, 312.5, 814.0, 314.0],"true", 2) )
    # Connections for obj872 (graphObject_: Obj711) of type hasAttribute_T
    self.drawConnections(
(self.obj872,self.obj846,[365.0, 535.5, 314.0, 594.0],"true", 2) )
    # Connections for obj873 (graphObject_: Obj712) of type hasAttribute_T
    self.drawConnections(
(self.obj873,self.obj847,[639.0, 530.5, 634.0, 594.0],"true", 2) )
    # Connections for obj874 (graphObject_: Obj713) of type hasAttribute_T
    self.drawConnections(
(self.obj874,self.obj848,[823.0, 532.5, 814.0, 594.0],"true", 2) )
    # Connections for obj875 (graphObject_: Obj714) of type hasAttribute_T
    self.drawConnections(
(self.obj875,self.obj849,[722.0, 381.5, 874.0, 394.0],"true", 2) )
    # Connections for obj876 (graphObject_: Obj715) of type leftExpr
    self.drawConnections(
(self.obj876,self.obj845,[916.0, 296.5, 814.0, 314.0],"true", 2) )
    # Connections for obj877 (graphObject_: Obj716) of type leftExpr
    self.drawConnections(
(self.obj877,self.obj846,[246.0, 636.5, 314.0, 594.0],"true", 2) )
    # Connections for obj878 (graphObject_: Obj717) of type leftExpr
    self.drawConnections(
(self.obj878,self.obj847,[556.0, 616.5, 634.0, 594.0],"true", 2) )
    # Connections for obj879 (graphObject_: Obj718) of type leftExpr
    self.drawConnections(
(self.obj879,self.obj848,[906.0, 616.5, 814.0, 594.0],"true", 2) )
    # Connections for obj880 (graphObject_: Obj719) of type leftExpr
    self.drawConnections(
(self.obj880,self.obj849,[956.0, 396.5, 874.0, 394.0],"true", 2) )
    # Connections for obj881 (graphObject_: Obj720) of type rightExpr
    self.drawConnections(
(self.obj881,self.obj855,[916.0, 226.5, 814.0, 174.0],"true", 2) )
    # Connections for obj882 (graphObject_: Obj721) of type rightExpr
    self.drawConnections(
(self.obj882,self.obj857,[282.0, 676.5, 314.0, 674.0],"true", 2) )
    # Connections for obj883 (graphObject_: Obj722) of type rightExpr
    self.drawConnections(
(self.obj883,self.obj858,[556.0, 656.5, 634.0, 674.0],"true", 2) )
    # Connections for obj884 (graphObject_: Obj723) of type rightExpr
    self.drawConnections(
(self.obj884,self.obj859,[906.0, 656.5, 814.0, 674.0],"true", 2) )
    # Connections for obj885 (graphObject_: Obj724) of type rightExpr
    self.drawConnections(
(self.obj885,self.obj860,[1036.0, 446.5, 1034.0, 494.0],"true", 2) )
    # Connections for obj886 (graphObject_: Obj725) of type hasArgs
    self.drawConnections(
(self.obj886,self.obj856,[904.0, 124.0, 994.0, 74.0],"true", 2) )
    # Connections for obj887 (graphObject_: Obj726) of type hasArgs
    self.drawConnections(
(self.obj887,self.obj844,[814.0, 124.0, 814.0, 74.0],"true", 2) )

newfunction = State2ProcDef_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
