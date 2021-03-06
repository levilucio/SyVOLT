"""
__ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:58:31 2015
___________________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from ExitPoint import *
from State import *
from ProcDef import *
from Name import *
from Trigger_T import *
from Par import *
from LocalDef import *
from Attribute import *
from Equation import *
from Concat import *
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
from hasArgs import *
from graph_ExitPoint import *
from graph_Attribute import *
from graph_LocalDef import *
from graph_paired_with import *
from graph_ProcDef import *
from graph_Par import *
from graph_Equation import *
from graph_backward_link import *
from graph_hasArgs import *
from graph_State import *
from graph_rightExpr import *
from graph_Trigger_T import *
from graph_Concat import *
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

def ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans')
    # --- ASG attributes over ---


    self.obj422=MatchModel(self)
    self.obj422.isGraphObjectVisual = True

    if(hasattr(self.obj422, '_setHierarchicalLink')):
      self.obj422._setHierarchicalLink(False)

    self.obj422.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj422)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj422.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj422)
    self.globalAndLocalPostcondition(self.obj422, rootNode)
    self.obj422.postAction( rootNode.CREATE )

    self.obj423=ApplyModel(self)
    self.obj423.isGraphObjectVisual = True

    if(hasattr(self.obj423, '_setHierarchicalLink')):
      self.obj423._setHierarchicalLink(False)

    self.obj423.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,300.0,self.obj423)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj423.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj423)
    self.globalAndLocalPostcondition(self.obj423, rootNode)
    self.obj423.postAction( rootNode.CREATE )

    self.obj424=ExitPoint(self)
    self.obj424.isGraphObjectVisual = True

    if(hasattr(self.obj424, '_setHierarchicalLink')):
      self.obj424._setHierarchicalLink(False)

    # name
    self.obj424.name.setValue('exitpoint1')

    # classtype
    self.obj424.classtype.setValue('ExitPoint')

    # cardinality
    self.obj424.cardinality.setValue('+')

    self.obj424.graphClass_= graph_ExitPoint
    if self.genGraphics:
       new_obj = graph_ExitPoint(480.0,40.0,self.obj424)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj424.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj424)
    self.globalAndLocalPostcondition(self.obj424, rootNode)
    self.obj424.postAction( rootNode.CREATE )

    self.obj425=State(self)
    self.obj425.isGraphObjectVisual = True

    if(hasattr(self.obj425, '_setHierarchicalLink')):
      self.obj425._setHierarchicalLink(False)

    # name
    self.obj425.name.setValue('state1')

    # classtype
    self.obj425.classtype.setValue('State')

    # cardinality
    self.obj425.cardinality.setValue('+')

    self.obj425.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj425)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj425.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj425)
    self.globalAndLocalPostcondition(self.obj425, rootNode)
    self.obj425.postAction( rootNode.CREATE )

    self.obj426=ProcDef(self)
    self.obj426.isGraphObjectVisual = True

    if(hasattr(self.obj426, '_setHierarchicalLink')):
      self.obj426._setHierarchicalLink(False)

    # classtype
    self.obj426.classtype.setValue('ProcDef')

    # cardinality
    self.obj426.cardinality.setValue('1')

    # name
    self.obj426.name.setValue('procdef1')

    self.obj426.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(460.0,380.0,self.obj426)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj426.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj426)
    self.globalAndLocalPostcondition(self.obj426, rootNode)
    self.obj426.postAction( rootNode.CREATE )

    self.obj427=Name(self)
    self.obj427.isGraphObjectVisual = True

    if(hasattr(self.obj427, '_setHierarchicalLink')):
      self.obj427._setHierarchicalLink(False)

    # classtype
    self.obj427.classtype.setValue('Name')

    # cardinality
    self.obj427.cardinality.setValue('1')

    # name
    self.obj427.name.setValue('name1')

    self.obj427.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(660.0,380.0,self.obj427)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj427.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj427)
    self.globalAndLocalPostcondition(self.obj427, rootNode)
    self.obj427.postAction( rootNode.CREATE )

    self.obj428=Trigger_T(self)
    self.obj428.isGraphObjectVisual = True

    if(hasattr(self.obj428, '_setHierarchicalLink')):
      self.obj428._setHierarchicalLink(False)

    # classtype
    self.obj428.classtype.setValue('Trigger_T')

    # cardinality
    self.obj428.cardinality.setValue('1')

    # name
    self.obj428.name.setValue('triggerT1')

    self.obj428.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(700.0,500.0,self.obj428)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj428.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj428)
    self.globalAndLocalPostcondition(self.obj428, rootNode)
    self.obj428.postAction( rootNode.CREATE )

    self.obj429=Par(self)
    self.obj429.isGraphObjectVisual = True

    if(hasattr(self.obj429, '_setHierarchicalLink')):
      self.obj429._setHierarchicalLink(False)

    # classtype
    self.obj429.classtype.setValue('Par')

    # cardinality
    self.obj429.cardinality.setValue('1')

    # name
    self.obj429.name.setValue('par1')

    self.obj429.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(500.0,500.0,self.obj429)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj429.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj429)
    self.globalAndLocalPostcondition(self.obj429, rootNode)
    self.obj429.postAction( rootNode.CREATE )

    self.obj430=LocalDef(self)
    self.obj430.isGraphObjectVisual = True

    if(hasattr(self.obj430, '_setHierarchicalLink')):
      self.obj430._setHierarchicalLink(False)

    # classtype
    self.obj430.classtype.setValue('LocalDef')

    # cardinality
    self.obj430.cardinality.setValue('1')

    # name
    self.obj430.name.setValue('localdef1')

    self.obj430.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(220.0,380.0,self.obj430)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj430.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj430)
    self.globalAndLocalPostcondition(self.obj430, rootNode)
    self.obj430.postAction( rootNode.CREATE )

    self.obj431=Attribute(self)
    self.obj431.isGraphObjectVisual = True

    if(hasattr(self.obj431, '_setHierarchicalLink')):
      self.obj431._setHierarchicalLink(False)

    # Type
    self.obj431.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj431.Type.config = 0

    # name
    self.obj431.name.setValue('isComposite')

    self.obj431.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,140.0,self.obj431)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj431.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj431)
    self.globalAndLocalPostcondition(self.obj431, rootNode)
    self.obj431.postAction( rootNode.CREATE )

    self.obj432=Attribute(self)
    self.obj432.isGraphObjectVisual = True

    if(hasattr(self.obj432, '_setHierarchicalLink')):
      self.obj432._setHierarchicalLink(False)

    # Type
    self.obj432.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj432.Type.config = 0

    # name
    self.obj432.name.setValue('name')

    self.obj432.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(700.0,100.0,self.obj432)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj432.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj432)
    self.globalAndLocalPostcondition(self.obj432, rootNode)
    self.obj432.postAction( rootNode.CREATE )

    self.obj433=Attribute(self)
    self.obj433.isGraphObjectVisual = True

    if(hasattr(self.obj433, '_setHierarchicalLink')):
      self.obj433._setHierarchicalLink(False)

    # Type
    self.obj433.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj433.Type.config = 0

    # name
    self.obj433.name.setValue('name')

    self.obj433.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,300.0,self.obj433)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj433.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj433)
    self.globalAndLocalPostcondition(self.obj433, rootNode)
    self.obj433.postAction( rootNode.CREATE )

    self.obj434=Attribute(self)
    self.obj434.isGraphObjectVisual = True

    if(hasattr(self.obj434, '_setHierarchicalLink')):
      self.obj434._setHierarchicalLink(False)

    # Type
    self.obj434.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj434.Type.config = 0

    # name
    self.obj434.name.setValue('literal')

    self.obj434.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,400.0,self.obj434)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj434.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj434)
    self.globalAndLocalPostcondition(self.obj434, rootNode)
    self.obj434.postAction( rootNode.CREATE )

    self.obj435=Attribute(self)
    self.obj435.isGraphObjectVisual = True

    if(hasattr(self.obj435, '_setHierarchicalLink')):
      self.obj435._setHierarchicalLink(False)

    # Type
    self.obj435.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj435.Type.config = 0

    # name
    self.obj435.name.setValue('channel')

    self.obj435.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(880.0,520.0,self.obj435)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj435.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj435)
    self.globalAndLocalPostcondition(self.obj435, rootNode)
    self.obj435.postAction( rootNode.CREATE )

    self.obj436=Attribute(self)
    self.obj436.isGraphObjectVisual = True

    if(hasattr(self.obj436, '_setHierarchicalLink')):
      self.obj436._setHierarchicalLink(False)

    # Type
    self.obj436.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj436.Type.config = 0

    # name
    self.obj436.name.setValue('pivot')

    self.obj436.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,560.0,self.obj436)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj436.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj436)
    self.globalAndLocalPostcondition(self.obj436, rootNode)
    self.obj436.postAction( rootNode.CREATE )

    self.obj437=Attribute(self)
    self.obj437.isGraphObjectVisual = True

    if(hasattr(self.obj437, '_setHierarchicalLink')):
      self.obj437._setHierarchicalLink(False)

    # Type
    self.obj437.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj437.Type.config = 0

    # name
    self.obj437.name.setValue('pivot')

    self.obj437.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,620.0,self.obj437)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj437.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj437)
    self.globalAndLocalPostcondition(self.obj437, rootNode)
    self.obj437.postAction( rootNode.CREATE )

    self.obj438=Equation(self)
    self.obj438.isGraphObjectVisual = True

    if(hasattr(self.obj438, '_setHierarchicalLink')):
      self.obj438._setHierarchicalLink(False)

    # name
    self.obj438.name.setValue('eq1')

    self.obj438.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,220.0,self.obj438)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj438.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj438)
    self.globalAndLocalPostcondition(self.obj438, rootNode)
    self.obj438.postAction( rootNode.CREATE )

    self.obj439=Equation(self)
    self.obj439.isGraphObjectVisual = True

    if(hasattr(self.obj439, '_setHierarchicalLink')):
      self.obj439._setHierarchicalLink(False)

    # name
    self.obj439.name.setValue('eq2')

    self.obj439.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(700.0,280.0,self.obj439)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj439.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj439)
    self.globalAndLocalPostcondition(self.obj439, rootNode)
    self.obj439.postAction( rootNode.CREATE )

    self.obj440=Equation(self)
    self.obj440.isGraphObjectVisual = True

    if(hasattr(self.obj440, '_setHierarchicalLink')):
      self.obj440._setHierarchicalLink(False)

    # name
    self.obj440.name.setValue('eq3')

    self.obj440.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(960.0,320.0,self.obj440)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj440.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj440)
    self.globalAndLocalPostcondition(self.obj440, rootNode)
    self.obj440.postAction( rootNode.CREATE )

    self.obj441=Equation(self)
    self.obj441.isGraphObjectVisual = True

    if(hasattr(self.obj441, '_setHierarchicalLink')):
      self.obj441._setHierarchicalLink(False)

    # name
    self.obj441.name.setValue('eq4')

    self.obj441.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(960.0,600.0,self.obj441)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj441.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj441)
    self.globalAndLocalPostcondition(self.obj441, rootNode)
    self.obj441.postAction( rootNode.CREATE )

    self.obj442=Equation(self)
    self.obj442.isGraphObjectVisual = True

    if(hasattr(self.obj442, '_setHierarchicalLink')):
      self.obj442._setHierarchicalLink(False)

    # name
    self.obj442.name.setValue('eq5')

    self.obj442.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(260.0,640.0,self.obj442)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj442.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj442)
    self.globalAndLocalPostcondition(self.obj442, rootNode)
    self.obj442.postAction( rootNode.CREATE )

    self.obj443=Equation(self)
    self.obj443.isGraphObjectVisual = True

    if(hasattr(self.obj443, '_setHierarchicalLink')):
      self.obj443._setHierarchicalLink(False)

    # name
    self.obj443.name.setValue('eq6')

    self.obj443.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(560.0,700.0,self.obj443)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj443.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj443)
    self.globalAndLocalPostcondition(self.obj443, rootNode)
    self.obj443.postAction( rootNode.CREATE )

    self.obj444=Concat(self)
    self.obj444.isGraphObjectVisual = True

    if(hasattr(self.obj444, '_setHierarchicalLink')):
      self.obj444._setHierarchicalLink(False)

    # Type
    self.obj444.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj444.Type.config = 0

    # name
    self.obj444.name.setValue('concat1')

    self.obj444.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,200.0,self.obj444)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj444.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj444)
    self.globalAndLocalPostcondition(self.obj444, rootNode)
    self.obj444.postAction( rootNode.CREATE )

    self.obj445=Constant(self)
    self.obj445.isGraphObjectVisual = True

    if(hasattr(self.obj445, '_setHierarchicalLink')):
      self.obj445._setHierarchicalLink(False)

    # Type
    self.obj445.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj445.Type.config = 0

    # name
    self.obj445.name.setValue('true')

    self.obj445.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(340.0,140.0,self.obj445)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj445.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj445)
    self.globalAndLocalPostcondition(self.obj445, rootNode)
    self.obj445.postAction( rootNode.CREATE )

    self.obj446=Constant(self)
    self.obj446.isGraphObjectVisual = True

    if(hasattr(self.obj446, '_setHierarchicalLink')):
      self.obj446._setHierarchicalLink(False)

    # Type
    self.obj446.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj446.Type.config = 0

    # name
    self.obj446.name.setValue('B')

    self.obj446.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,200.0,self.obj446)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj446.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj446)
    self.globalAndLocalPostcondition(self.obj446, rootNode)
    self.obj446.postAction( rootNode.CREATE )

    self.obj447=Constant(self)
    self.obj447.isGraphObjectVisual = True

    if(hasattr(self.obj447, '_setHierarchicalLink')):
      self.obj447._setHierarchicalLink(False)

    # Type
    self.obj447.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj447.Type.config = 0

    # name
    self.obj447.name.setValue('sh_in')

    self.obj447.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1020.0,400.0,self.obj447)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj447.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj447)
    self.globalAndLocalPostcondition(self.obj447, rootNode)
    self.obj447.postAction( rootNode.CREATE )

    self.obj448=Constant(self)
    self.obj448.isGraphObjectVisual = True

    if(hasattr(self.obj448, '_setHierarchicalLink')):
      self.obj448._setHierarchicalLink(False)

    # Type
    self.obj448.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj448.Type.config = 0

    # name
    self.obj448.name.setValue('sh_in')

    self.obj448.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1040.0,520.0,self.obj448)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj448.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj448)
    self.globalAndLocalPostcondition(self.obj448, rootNode)
    self.obj448.postAction( rootNode.CREATE )

    self.obj449=Constant(self)
    self.obj449.isGraphObjectVisual = True

    if(hasattr(self.obj449, '_setHierarchicalLink')):
      self.obj449._setHierarchicalLink(False)

    # Type
    self.obj449.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj449.Type.config = 0

    # name
    self.obj449.name.setValue('localdefcompstate')

    self.obj449.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(340.0,560.0,self.obj449)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj449.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj449)
    self.globalAndLocalPostcondition(self.obj449, rootNode)
    self.obj449.postAction( rootNode.CREATE )

    self.obj450=Constant(self)
    self.obj450.isGraphObjectVisual = True

    if(hasattr(self.obj450, '_setHierarchicalLink')):
      self.obj450._setHierarchicalLink(False)

    # Type
    self.obj450.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj450.Type.config = 0

    # name
    self.obj450.name.setValue('parexitpoint')

    self.obj450.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(660.0,620.0,self.obj450)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj450.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj450)
    self.globalAndLocalPostcondition(self.obj450, rootNode)
    self.obj450.postAction( rootNode.CREATE )

    self.obj451=paired_with(self)
    self.obj451.isGraphObjectVisual = True

    if(hasattr(self.obj451, '_setHierarchicalLink')):
      self.obj451._setHierarchicalLink(False)

    self.obj451.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj451)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj451.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj451)
    self.globalAndLocalPostcondition(self.obj451, rootNode)
    self.obj451.postAction( rootNode.CREATE )

    self.obj452=match_contains(self)
    self.obj452.isGraphObjectVisual = True

    if(hasattr(self.obj452, '_setHierarchicalLink')):
      self.obj452._setHierarchicalLink(False)

    self.obj452.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj452)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj452.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj452)
    self.globalAndLocalPostcondition(self.obj452, rootNode)
    self.obj452.postAction( rootNode.CREATE )

    self.obj453=match_contains(self)
    self.obj453.isGraphObjectVisual = True

    if(hasattr(self.obj453, '_setHierarchicalLink')):
      self.obj453._setHierarchicalLink(False)

    self.obj453.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,67.0,self.obj453)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj453.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj453)
    self.globalAndLocalPostcondition(self.obj453, rootNode)
    self.obj453.postAction( rootNode.CREATE )

    self.obj454=apply_contains(self)
    self.obj454.isGraphObjectVisual = True

    if(hasattr(self.obj454, '_setHierarchicalLink')):
      self.obj454._setHierarchicalLink(False)

    self.obj454.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,375.0,self.obj454)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj454.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj454)
    self.globalAndLocalPostcondition(self.obj454, rootNode)
    self.obj454.postAction( rootNode.CREATE )

    self.obj455=apply_contains(self)
    self.obj455.isGraphObjectVisual = True

    if(hasattr(self.obj455, '_setHierarchicalLink')):
      self.obj455._setHierarchicalLink(False)

    self.obj455.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(377.5,374.0,self.obj455)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj455.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj455)
    self.globalAndLocalPostcondition(self.obj455, rootNode)
    self.obj455.postAction( rootNode.CREATE )

    self.obj456=apply_contains(self)
    self.obj456.isGraphObjectVisual = True

    if(hasattr(self.obj456, '_setHierarchicalLink')):
      self.obj456._setHierarchicalLink(False)

    self.obj456.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,382.0,self.obj456)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj456.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj456)
    self.globalAndLocalPostcondition(self.obj456, rootNode)
    self.obj456.postAction( rootNode.CREATE )

    self.obj457=apply_contains(self)
    self.obj457.isGraphObjectVisual = True

    if(hasattr(self.obj457, '_setHierarchicalLink')):
      self.obj457._setHierarchicalLink(False)

    self.obj457.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,486.0,self.obj457)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj457.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj457)
    self.globalAndLocalPostcondition(self.obj457, rootNode)
    self.obj457.postAction( rootNode.CREATE )

    self.obj458=apply_contains(self)
    self.obj458.isGraphObjectVisual = True

    if(hasattr(self.obj458, '_setHierarchicalLink')):
      self.obj458._setHierarchicalLink(False)

    self.obj458.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(507.5,442.0,self.obj458)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj458.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj458)
    self.globalAndLocalPostcondition(self.obj458, rootNode)
    self.obj458.postAction( rootNode.CREATE )

    self.obj459=directLink_T(self)
    self.obj459.isGraphObjectVisual = True

    if(hasattr(self.obj459, '_setHierarchicalLink')):
      self.obj459._setHierarchicalLink(False)

    # associationType
    self.obj459.associationType.setValue('def')

    self.obj459.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(431.0,427.0,self.obj459)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj459.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj459)
    self.globalAndLocalPostcondition(self.obj459, rootNode)
    self.obj459.postAction( rootNode.CREATE )

    self.obj460=directLink_T(self)
    self.obj460.isGraphObjectVisual = True

    if(hasattr(self.obj460, '_setHierarchicalLink')):
      self.obj460._setHierarchicalLink(False)

    # associationType
    self.obj460.associationType.setValue('channelNames')

    self.obj460.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,431.0,self.obj460)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj460.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj460)
    self.globalAndLocalPostcondition(self.obj460, rootNode)
    self.obj460.postAction( rootNode.CREATE )

    self.obj461=directLink_T(self)
    self.obj461.isGraphObjectVisual = True

    if(hasattr(self.obj461, '_setHierarchicalLink')):
      self.obj461._setHierarchicalLink(False)

    # associationType
    self.obj461.associationType.setValue('p')

    self.obj461.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj461)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj461.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj461)
    self.globalAndLocalPostcondition(self.obj461, rootNode)
    self.obj461.postAction( rootNode.CREATE )

    self.obj462=directLink_T(self)
    self.obj462.isGraphObjectVisual = True

    if(hasattr(self.obj462, '_setHierarchicalLink')):
      self.obj462._setHierarchicalLink(False)

    # associationType
    self.obj462.associationType.setValue('p')

    self.obj462.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(772.0,551.0,self.obj462)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj462.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj462)
    self.globalAndLocalPostcondition(self.obj462, rootNode)
    self.obj462.postAction( rootNode.CREATE )

    self.obj463=directLink_S(self)
    self.obj463.isGraphObjectVisual = True

    if(hasattr(self.obj463, '_setHierarchicalLink')):
      self.obj463._setHierarchicalLink(False)

    # associationType
    self.obj463.associationType.setValue('exitPoints')

    self.obj463.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(500.0,83.0,self.obj463)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj463.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj463)
    self.globalAndLocalPostcondition(self.obj463, rootNode)
    self.obj463.postAction( rootNode.CREATE )

    self.obj464=backward_link(self)
    self.obj464.isGraphObjectVisual = True

    if(hasattr(self.obj464, '_setHierarchicalLink')):
      self.obj464._setHierarchicalLink(False)

    # type
    self.obj464.type.setValue('ruleDef')

    self.obj464.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(371.0,257.0,self.obj464)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj464.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj464)
    self.globalAndLocalPostcondition(self.obj464, rootNode)
    self.obj464.postAction( rootNode.CREATE )

    self.obj465=hasAttribute_S(self)
    self.obj465.isGraphObjectVisual = True

    if(hasattr(self.obj465, '_setHierarchicalLink')):
      self.obj465._setHierarchicalLink(False)

    self.obj465.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(328.0,136.5,self.obj465)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj465.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj465)
    self.globalAndLocalPostcondition(self.obj465, rootNode)
    self.obj465.postAction( rootNode.CREATE )

    self.obj466=hasAttribute_S(self)
    self.obj466.isGraphObjectVisual = True

    if(hasattr(self.obj466, '_setHierarchicalLink')):
      self.obj466._setHierarchicalLink(False)

    self.obj466.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(742.0,108.5,self.obj466)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj466.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj466)
    self.globalAndLocalPostcondition(self.obj466, rootNode)
    self.obj466.postAction( rootNode.CREATE )

    self.obj467=hasAttribute_T(self)
    self.obj467.isGraphObjectVisual = True

    if(hasattr(self.obj467, '_setHierarchicalLink')):
      self.obj467._setHierarchicalLink(False)

    self.obj467.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(634.0,364.5,self.obj467)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj467.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj467)
    self.globalAndLocalPostcondition(self.obj467, rootNode)
    self.obj467.postAction( rootNode.CREATE )

    self.obj468=hasAttribute_T(self)
    self.obj468.isGraphObjectVisual = True

    if(hasattr(self.obj468, '_setHierarchicalLink')):
      self.obj468._setHierarchicalLink(False)

    self.obj468.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(913.0,432.5,self.obj468)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj468.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj468)
    self.globalAndLocalPostcondition(self.obj468, rootNode)
    self.obj468.postAction( rootNode.CREATE )

    self.obj469=hasAttribute_T(self)
    self.obj469.isGraphObjectVisual = True

    if(hasattr(self.obj469, '_setHierarchicalLink')):
      self.obj469._setHierarchicalLink(False)

    self.obj469.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(943.0,552.5,self.obj469)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj469.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj469)
    self.globalAndLocalPostcondition(self.obj469, rootNode)
    self.obj469.postAction( rootNode.CREATE )

    self.obj470=hasAttribute_T(self)
    self.obj470.isGraphObjectVisual = True

    if(hasattr(self.obj470, '_setHierarchicalLink')):
      self.obj470._setHierarchicalLink(False)

    self.obj470.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,512.5,self.obj470)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj470.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj470)
    self.globalAndLocalPostcondition(self.obj470, rootNode)
    self.obj470.postAction( rootNode.CREATE )

    self.obj471=hasAttribute_T(self)
    self.obj471.isGraphObjectVisual = True

    if(hasattr(self.obj471, '_setHierarchicalLink')):
      self.obj471._setHierarchicalLink(False)

    self.obj471.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(653.0,602.5,self.obj471)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj471.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj471)
    self.globalAndLocalPostcondition(self.obj471, rootNode)
    self.obj471.postAction( rootNode.CREATE )

    self.obj472=leftExpr(self)
    self.obj472.isGraphObjectVisual = True

    if(hasattr(self.obj472, '_setHierarchicalLink')):
      self.obj472._setHierarchicalLink(False)

    self.obj472.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,213.5,self.obj472)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj472.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj472)
    self.globalAndLocalPostcondition(self.obj472, rootNode)
    self.obj472.postAction( rootNode.CREATE )

    self.obj473=leftExpr(self)
    self.obj473.isGraphObjectVisual = True

    if(hasattr(self.obj473, '_setHierarchicalLink')):
      self.obj473._setHierarchicalLink(False)

    self.obj473.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(746.0,326.5,self.obj473)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj473.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj473)
    self.globalAndLocalPostcondition(self.obj473, rootNode)
    self.obj473.postAction( rootNode.CREATE )

    self.obj474=leftExpr(self)
    self.obj474.isGraphObjectVisual = True

    if(hasattr(self.obj474, '_setHierarchicalLink')):
      self.obj474._setHierarchicalLink(False)

    self.obj474.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1052.0,380.5,self.obj474)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj474.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj474)
    self.globalAndLocalPostcondition(self.obj474, rootNode)
    self.obj474.postAction( rootNode.CREATE )

    self.obj475=leftExpr(self)
    self.obj475.isGraphObjectVisual = True

    if(hasattr(self.obj475, '_setHierarchicalLink')):
      self.obj475._setHierarchicalLink(False)

    self.obj475.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1056.0,596.5,self.obj475)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj475.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj475)
    self.globalAndLocalPostcondition(self.obj475, rootNode)
    self.obj475.postAction( rootNode.CREATE )

    self.obj476=leftExpr(self)
    self.obj476.isGraphObjectVisual = True

    if(hasattr(self.obj476, '_setHierarchicalLink')):
      self.obj476._setHierarchicalLink(False)

    self.obj476.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(356.0,636.5,self.obj476)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj476.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj476)
    self.globalAndLocalPostcondition(self.obj476, rootNode)
    self.obj476.postAction( rootNode.CREATE )

    self.obj477=leftExpr(self)
    self.obj477.isGraphObjectVisual = True

    if(hasattr(self.obj477, '_setHierarchicalLink')):
      self.obj477._setHierarchicalLink(False)

    self.obj477.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(666.0,696.5,self.obj477)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj477.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj477)
    self.globalAndLocalPostcondition(self.obj477, rootNode)
    self.obj477.postAction( rootNode.CREATE )

    self.obj478=rightExpr(self)
    self.obj478.isGraphObjectVisual = True

    if(hasattr(self.obj478, '_setHierarchicalLink')):
      self.obj478._setHierarchicalLink(False)

    self.obj478.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(457.0,212.5,self.obj478)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj478.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj478)
    self.globalAndLocalPostcondition(self.obj478, rootNode)
    self.obj478.postAction( rootNode.CREATE )

    self.obj479=rightExpr(self)
    self.obj479.isGraphObjectVisual = True

    if(hasattr(self.obj479, '_setHierarchicalLink')):
      self.obj479._setHierarchicalLink(False)

    self.obj479.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(746.0,276.5,self.obj479)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj479.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj479)
    self.globalAndLocalPostcondition(self.obj479, rootNode)
    self.obj479.postAction( rootNode.CREATE )

    self.obj480=rightExpr(self)
    self.obj480.isGraphObjectVisual = True

    if(hasattr(self.obj480, '_setHierarchicalLink')):
      self.obj480._setHierarchicalLink(False)

    self.obj480.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1126.0,396.5,self.obj480)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj480.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj480)
    self.globalAndLocalPostcondition(self.obj480, rootNode)
    self.obj480.postAction( rootNode.CREATE )

    self.obj481=rightExpr(self)
    self.obj481.isGraphObjectVisual = True

    if(hasattr(self.obj481, '_setHierarchicalLink')):
      self.obj481._setHierarchicalLink(False)

    self.obj481.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1136.0,596.5,self.obj481)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj481.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj481)
    self.globalAndLocalPostcondition(self.obj481, rootNode)
    self.obj481.postAction( rootNode.CREATE )

    self.obj482=rightExpr(self)
    self.obj482.isGraphObjectVisual = True

    if(hasattr(self.obj482, '_setHierarchicalLink')):
      self.obj482._setHierarchicalLink(False)

    self.obj482.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(436.0,636.5,self.obj482)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj482.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj482)
    self.globalAndLocalPostcondition(self.obj482, rootNode)
    self.obj482.postAction( rootNode.CREATE )

    self.obj483=rightExpr(self)
    self.obj483.isGraphObjectVisual = True

    if(hasattr(self.obj483, '_setHierarchicalLink')):
      self.obj483._setHierarchicalLink(False)

    self.obj483.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(746.0,696.5,self.obj483)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj483.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj483)
    self.globalAndLocalPostcondition(self.obj483, rootNode)
    self.obj483.postAction( rootNode.CREATE )

    self.obj484=hasArgs(self)
    self.obj484.isGraphObjectVisual = True

    if(hasattr(self.obj484, '_setHierarchicalLink')):
      self.obj484._setHierarchicalLink(False)

    self.obj484.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(744.0,234.0,self.obj484)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj484.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj484)
    self.globalAndLocalPostcondition(self.obj484, rootNode)
    self.obj484.postAction( rootNode.CREATE )

    self.obj485=hasArgs(self)
    self.obj485.isGraphObjectVisual = True

    if(hasattr(self.obj485, '_setHierarchicalLink')):
      self.obj485._setHierarchicalLink(False)

    self.obj485.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(744.0,184.0,self.obj485)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj485.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj485)
    self.globalAndLocalPostcondition(self.obj485, rootNode)
    self.obj485.postAction( rootNode.CREATE )

    # Connections for obj422 (graphObject_: Obj319) of type MatchModel
    self.drawConnections(
(self.obj422,self.obj451,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj422,self.obj452,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj422,self.obj453,[138.0, 51.0, 394.0, 67.0],"true", 2) )
    # Connections for obj423 (graphObject_: Obj320) of type ApplyModel
    self.drawConnections(
(self.obj423,self.obj454,[143.0, 333.0, 247.5, 375.0],"true", 2),
(self.obj423,self.obj455,[143.0, 333.0, 377.5, 374.0],"true", 2),
(self.obj423,self.obj456,[143.0, 333.0, 487.5, 382.0],"true", 2),
(self.obj423,self.obj457,[143.0, 333.0, 219.5, 486.0],"true", 2),
(self.obj423,self.obj458,[143.0, 333.0, 507.5, 442.0],"true", 2) )
    # Connections for obj424 (graphObject_: Obj321) named exitpoint1
    self.drawConnections(
(self.obj424,self.obj466,[650.0, 83.0, 742.0, 108.5],"true", 2) )
    # Connections for obj425 (graphObject_: Obj322) named state1
    self.drawConnections(
(self.obj425,self.obj463,[350.0, 83.0, 500.0, 83.0],"true", 2),
(self.obj425,self.obj465,[350.0, 83.0, 328.0, 136.5],"true", 2) )
    # Connections for obj426 (graphObject_: Obj323) named procdef1
    self.drawConnections(
(self.obj426,self.obj467,[632.0, 431.0, 634.0, 364.5],"true", 2),
(self.obj426,self.obj460,[632.0, 431.0, 752.0, 431.0],"true", 2),
(self.obj426,self.obj461,[632.0, 431.0, 652.0, 491.0],"true", 2) )
    # Connections for obj427 (graphObject_: Obj324) named name1
    self.drawConnections(
(self.obj427,self.obj468,[832.0, 431.0, 913.0, 432.5],"true", 2) )
    # Connections for obj428 (graphObject_: Obj325) named triggerT1
    self.drawConnections(
(self.obj428,self.obj469,[872.0, 551.0, 943.0, 552.5],"true", 2) )
    # Connections for obj429 (graphObject_: Obj326) named par1
    self.drawConnections(
(self.obj429,self.obj462,[672.0, 551.0, 772.0, 551.0],"true", 2),
(self.obj429,self.obj471,[672.0, 551.0, 653.0, 602.5],"true", 2) )
    # Connections for obj430 (graphObject_: Obj327) named localdef1
    self.drawConnections(
(self.obj430,self.obj459,[392.0, 431.0, 431.0, 427.0],"true", 2),
(self.obj430,self.obj464,[392.0, 431.0, 371.0, 257.0],"true", 2),
(self.obj430,self.obj470,[392.0, 431.0, 353.0, 512.5],"true", 2) )
    # Connections for obj431 (graphObject_: Obj328) named isComposite
    self.drawConnections(
 )
    # Connections for obj432 (graphObject_: Obj329) named name
    self.drawConnections(
 )
    # Connections for obj433 (graphObject_: Obj330) named name
    self.drawConnections(
 )
    # Connections for obj434 (graphObject_: Obj331) named literal
    self.drawConnections(
 )
    # Connections for obj435 (graphObject_: Obj332) named channel
    self.drawConnections(
 )
    # Connections for obj436 (graphObject_: Obj333) named pivot
    self.drawConnections(
 )
    # Connections for obj437 (graphObject_: Obj334) named pivot
    self.drawConnections(
 )
    # Connections for obj438 (graphObject_: Obj335) named eq1
    self.drawConnections(
(self.obj438,self.obj472,[438.0, 259.0, 359.0, 213.5],"true", 2),
(self.obj438,self.obj478,[438.0, 259.0, 457.0, 212.5],"true", 2) )
    # Connections for obj439 (graphObject_: Obj336) named eq2
    self.drawConnections(
(self.obj439,self.obj479,[838.0, 319.0, 746.0, 276.5],"true", 2),
(self.obj439,self.obj473,[838.0, 319.0, 746.0, 326.5],"true", 2) )
    # Connections for obj440 (graphObject_: Obj337) named eq3
    self.drawConnections(
(self.obj440,self.obj474,[1098.0, 359.0, 1052.0, 380.5],"true", 2),
(self.obj440,self.obj480,[1098.0, 359.0, 1126.0, 396.5],"true", 2) )
    # Connections for obj441 (graphObject_: Obj338) named eq4
    self.drawConnections(
(self.obj441,self.obj475,[1098.0, 639.0, 1056.0, 596.5],"true", 2),
(self.obj441,self.obj481,[1098.0, 639.0, 1136.0, 596.5],"true", 2) )
    # Connections for obj442 (graphObject_: Obj339) named eq5
    self.drawConnections(
(self.obj442,self.obj476,[398.0, 679.0, 356.0, 636.5],"true", 2),
(self.obj442,self.obj482,[398.0, 679.0, 436.0, 636.5],"true", 2) )
    # Connections for obj443 (graphObject_: Obj340) named eq6
    self.drawConnections(
(self.obj443,self.obj477,[698.0, 739.0, 666.0, 696.5],"true", 2),
(self.obj443,self.obj483,[698.0, 739.0, 746.0, 696.5],"true", 2) )
    # Connections for obj444 (graphObject_: Obj341) named concat1
    self.drawConnections(
(self.obj444,self.obj484,[634.0, 234.0, 744.0, 234.0],"true", 2),
(self.obj444,self.obj485,[634.0, 234.0, 744.0, 184.0],"true", 2) )
    # Connections for obj445 (graphObject_: Obj342) named true
    self.drawConnections(
 )
    # Connections for obj446 (graphObject_: Obj343) named B
    self.drawConnections(
 )
    # Connections for obj447 (graphObject_: Obj344) named sh_in
    self.drawConnections(
 )
    # Connections for obj448 (graphObject_: Obj345) named sh_in
    self.drawConnections(
 )
    # Connections for obj449 (graphObject_: Obj346) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj450 (graphObject_: Obj347) named parexitpoint
    self.drawConnections(
 )
    # Connections for obj451 (graphObject_: Obj348) of type paired_with
    self.drawConnections(
(self.obj451,self.obj423,[140.5, 152.0, 143.0, 333.0],"true", 2) )
    # Connections for obj452 (graphObject_: Obj349) of type match_contains
    self.drawConnections(
(self.obj452,self.obj425,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj453 (graphObject_: Obj350) of type match_contains
    self.drawConnections(
(self.obj453,self.obj424,[394.0, 67.0, 650.0, 83.0],"true", 2) )
    # Connections for obj454 (graphObject_: Obj351) of type apply_contains
    self.drawConnections(
(self.obj454,self.obj430,[247.5, 375.0, 392.0, 431.0],"true", 2) )
    # Connections for obj455 (graphObject_: Obj352) of type apply_contains
    self.drawConnections(
(self.obj455,self.obj426,[377.5, 374.0, 632.0, 431.0],"true", 2) )
    # Connections for obj456 (graphObject_: Obj353) of type apply_contains
    self.drawConnections(
(self.obj456,self.obj427,[487.5, 382.0, 832.0, 431.0],"true", 2) )
    # Connections for obj457 (graphObject_: Obj354) of type apply_contains
    self.drawConnections(
(self.obj457,self.obj429,[222.5, 542.0, 672.0, 551.0],"true", 2) )
    # Connections for obj458 (graphObject_: Obj355) of type apply_contains
    self.drawConnections(
(self.obj458,self.obj428,[507.5, 442.0, 872.0, 551.0],"true", 2) )
    # Connections for obj459 (graphObject_: Obj356) of type directLink_T
    self.drawConnections(
(self.obj459,self.obj426,[431.0, 427.0, 632.0, 431.0],"true", 2) )
    # Connections for obj460 (graphObject_: Obj357) of type directLink_T
    self.drawConnections(
(self.obj460,self.obj427,[752.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj461 (graphObject_: Obj358) of type directLink_T
    self.drawConnections(
(self.obj461,self.obj429,[652.0, 491.0, 672.0, 551.0],"true", 2) )
    # Connections for obj462 (graphObject_: Obj359) of type directLink_T
    self.drawConnections(
(self.obj462,self.obj428,[772.0, 551.0, 872.0, 551.0],"true", 2) )
    # Connections for obj463 (graphObject_: Obj360) of type directLink_S
    self.drawConnections(
(self.obj463,self.obj424,[500.0, 83.0, 650.0, 83.0],"true", 2) )
    # Connections for obj464 (graphObject_: Obj361) of type backward_link
    self.drawConnections(
(self.obj464,self.obj425,[371.0, 257.0, 350.0, 83.0],"true", 2) )
    # Connections for obj465 (graphObject_: Obj362) of type hasAttribute_S
    self.drawConnections(
(self.obj465,self.obj431,[328.0, 136.5, 314.0, 174.0],"true", 2) )
    # Connections for obj466 (graphObject_: Obj363) of type hasAttribute_S
    self.drawConnections(
(self.obj466,self.obj432,[742.0, 108.5, 834.0, 134.0],"true", 2) )
    # Connections for obj467 (graphObject_: Obj364) of type hasAttribute_T
    self.drawConnections(
(self.obj467,self.obj433,[634.0, 364.5, 634.0, 334.0],"true", 2) )
    # Connections for obj468 (graphObject_: Obj365) of type hasAttribute_T
    self.drawConnections(
(self.obj468,self.obj434,[913.0, 432.5, 994.0, 434.0],"true", 2) )
    # Connections for obj469 (graphObject_: Obj366) of type hasAttribute_T
    self.drawConnections(
(self.obj469,self.obj435,[943.0, 552.5, 1014.0, 554.0],"true", 2) )
    # Connections for obj470 (graphObject_: Obj367) of type hasAttribute_T
    self.drawConnections(
(self.obj470,self.obj436,[353.0, 512.5, 314.0, 594.0],"true", 2) )
    # Connections for obj471 (graphObject_: Obj368) of type hasAttribute_T
    self.drawConnections(
(self.obj471,self.obj437,[653.0, 602.5, 634.0, 654.0],"true", 2) )
    # Connections for obj472 (graphObject_: Obj369) of type leftExpr
    self.drawConnections(
(self.obj472,self.obj431,[359.0, 213.5, 314.0, 174.0],"true", 2) )
    # Connections for obj473 (graphObject_: Obj370) of type leftExpr
    self.drawConnections(
(self.obj473,self.obj433,[746.0, 326.5, 634.0, 334.0],"true", 2) )
    # Connections for obj474 (graphObject_: Obj371) of type leftExpr
    self.drawConnections(
(self.obj474,self.obj434,[1046.0, 396.5, 994.0, 434.0],"true", 2) )
    # Connections for obj475 (graphObject_: Obj372) of type leftExpr
    self.drawConnections(
(self.obj475,self.obj435,[1056.0, 596.5, 1014.0, 554.0],"true", 2) )
    # Connections for obj476 (graphObject_: Obj373) of type leftExpr
    self.drawConnections(
(self.obj476,self.obj436,[356.0, 636.5, 314.0, 594.0],"true", 2) )
    # Connections for obj477 (graphObject_: Obj374) of type leftExpr
    self.drawConnections(
(self.obj477,self.obj437,[666.0, 696.5, 634.0, 654.0],"true", 2) )
    # Connections for obj478 (graphObject_: Obj375) of type rightExpr
    self.drawConnections(
(self.obj478,self.obj445,[457.0, 212.5, 474.0, 174.0],"true", 2) )
    # Connections for obj479 (graphObject_: Obj376) of type rightExpr
    self.drawConnections(
(self.obj479,self.obj444,[746.0, 276.5, 634.0, 234.0],"true", 2) )
    # Connections for obj480 (graphObject_: Obj377) of type rightExpr
    self.drawConnections(
(self.obj480,self.obj447,[1126.0, 396.5, 1154.0, 434.0],"true", 2) )
    # Connections for obj481 (graphObject_: Obj378) of type rightExpr
    self.drawConnections(
(self.obj481,self.obj448,[1136.0, 596.5, 1174.0, 554.0],"true", 2) )
    # Connections for obj482 (graphObject_: Obj379) of type rightExpr
    self.drawConnections(
(self.obj482,self.obj449,[436.0, 636.5, 474.0, 594.0],"true", 2) )
    # Connections for obj483 (graphObject_: Obj380) of type rightExpr
    self.drawConnections(
(self.obj483,self.obj450,[746.0, 696.5, 794.0, 654.0],"true", 2) )
    # Connections for obj484 (graphObject_: Obj381) of type hasArgs
    self.drawConnections(
(self.obj484,self.obj446,[744.0, 234.0, 834.0, 234.0],"true", 2) )
    # Connections for obj485 (graphObject_: Obj382) of type hasArgs
    self.drawConnections(
(self.obj485,self.obj432,[744.0, 184.0, 834.0, 134.0],"true", 2) )

newfunction = ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
