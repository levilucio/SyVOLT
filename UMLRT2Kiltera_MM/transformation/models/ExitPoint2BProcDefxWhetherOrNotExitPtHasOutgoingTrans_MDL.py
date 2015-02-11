"""
__ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Feb 11 14:03:40 2015
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


    self.obj452=MatchModel(self)
    self.obj452.isGraphObjectVisual = True

    if(hasattr(self.obj452, '_setHierarchicalLink')):
      self.obj452._setHierarchicalLink(False)

    self.obj452.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj452)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj452.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj452)
    self.globalAndLocalPostcondition(self.obj452, rootNode)
    self.obj452.postAction( rootNode.CREATE )

    self.obj453=ApplyModel(self)
    self.obj453.isGraphObjectVisual = True

    if(hasattr(self.obj453, '_setHierarchicalLink')):
      self.obj453._setHierarchicalLink(False)

    self.obj453.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,300.0,self.obj453)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj453.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj453)
    self.globalAndLocalPostcondition(self.obj453, rootNode)
    self.obj453.postAction( rootNode.CREATE )

    self.obj454=ExitPoint(self)
    self.obj454.isGraphObjectVisual = True

    if(hasattr(self.obj454, '_setHierarchicalLink')):
      self.obj454._setHierarchicalLink(False)

    # name
    self.obj454.name.setValue('exitpoint1')

    # classtype
    self.obj454.classtype.setValue('ExitPoint')

    # cardinality
    self.obj454.cardinality.setValue('+')

    self.obj454.graphClass_= graph_ExitPoint
    if self.genGraphics:
       new_obj = graph_ExitPoint(480.0,40.0,self.obj454)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ExitPoint", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj454.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj454)
    self.globalAndLocalPostcondition(self.obj454, rootNode)
    self.obj454.postAction( rootNode.CREATE )

    self.obj455=State(self)
    self.obj455.isGraphObjectVisual = True

    if(hasattr(self.obj455, '_setHierarchicalLink')):
      self.obj455._setHierarchicalLink(False)

    # name
    self.obj455.name.setValue('state1')

    # classtype
    self.obj455.classtype.setValue('State')

    # cardinality
    self.obj455.cardinality.setValue('+')

    self.obj455.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(180.0,40.0,self.obj455)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj455.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj455)
    self.globalAndLocalPostcondition(self.obj455, rootNode)
    self.obj455.postAction( rootNode.CREATE )

    self.obj456=ProcDef(self)
    self.obj456.isGraphObjectVisual = True

    if(hasattr(self.obj456, '_setHierarchicalLink')):
      self.obj456._setHierarchicalLink(False)

    # classtype
    self.obj456.classtype.setValue('ProcDef')

    # cardinality
    self.obj456.cardinality.setValue('1')

    # name
    self.obj456.name.setValue('procdef1')

    self.obj456.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(460.0,380.0,self.obj456)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj456.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj456)
    self.globalAndLocalPostcondition(self.obj456, rootNode)
    self.obj456.postAction( rootNode.CREATE )

    self.obj457=Name(self)
    self.obj457.isGraphObjectVisual = True

    if(hasattr(self.obj457, '_setHierarchicalLink')):
      self.obj457._setHierarchicalLink(False)

    # classtype
    self.obj457.classtype.setValue('Name')

    # cardinality
    self.obj457.cardinality.setValue('1')

    # name
    self.obj457.name.setValue('name1')

    self.obj457.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(660.0,380.0,self.obj457)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj457.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj457)
    self.globalAndLocalPostcondition(self.obj457, rootNode)
    self.obj457.postAction( rootNode.CREATE )

    self.obj458=Trigger_T(self)
    self.obj458.isGraphObjectVisual = True

    if(hasattr(self.obj458, '_setHierarchicalLink')):
      self.obj458._setHierarchicalLink(False)

    # classtype
    self.obj458.classtype.setValue('Trigger_T')

    # cardinality
    self.obj458.cardinality.setValue('1')

    # name
    self.obj458.name.setValue('triggerT1')

    self.obj458.graphClass_= graph_Trigger_T
    if self.genGraphics:
       new_obj = graph_Trigger_T(700.0,500.0,self.obj458)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Trigger_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj458.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj458)
    self.globalAndLocalPostcondition(self.obj458, rootNode)
    self.obj458.postAction( rootNode.CREATE )

    self.obj459=Par(self)
    self.obj459.isGraphObjectVisual = True

    if(hasattr(self.obj459, '_setHierarchicalLink')):
      self.obj459._setHierarchicalLink(False)

    # classtype
    self.obj459.classtype.setValue('Par')

    # cardinality
    self.obj459.cardinality.setValue('1')

    # name
    self.obj459.name.setValue('par1')

    self.obj459.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(500.0,500.0,self.obj459)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj459.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj459)
    self.globalAndLocalPostcondition(self.obj459, rootNode)
    self.obj459.postAction( rootNode.CREATE )

    self.obj460=LocalDef(self)
    self.obj460.isGraphObjectVisual = True

    if(hasattr(self.obj460, '_setHierarchicalLink')):
      self.obj460._setHierarchicalLink(False)

    # classtype
    self.obj460.classtype.setValue('LocalDef')

    # cardinality
    self.obj460.cardinality.setValue('1')

    # name
    self.obj460.name.setValue('localdef1')

    self.obj460.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(220.0,380.0,self.obj460)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj460.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj460)
    self.globalAndLocalPostcondition(self.obj460, rootNode)
    self.obj460.postAction( rootNode.CREATE )

    self.obj461=Attribute(self)
    self.obj461.isGraphObjectVisual = True

    if(hasattr(self.obj461, '_setHierarchicalLink')):
      self.obj461._setHierarchicalLink(False)

    # Type
    self.obj461.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj461.Type.config = 0

    # name
    self.obj461.name.setValue('isComposite')

    self.obj461.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,140.0,self.obj461)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj461.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj461)
    self.globalAndLocalPostcondition(self.obj461, rootNode)
    self.obj461.postAction( rootNode.CREATE )

    self.obj462=Attribute(self)
    self.obj462.isGraphObjectVisual = True

    if(hasattr(self.obj462, '_setHierarchicalLink')):
      self.obj462._setHierarchicalLink(False)

    # Type
    self.obj462.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj462.Type.config = 0

    # name
    self.obj462.name.setValue('name')

    self.obj462.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(700.0,100.0,self.obj462)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj462.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj462)
    self.globalAndLocalPostcondition(self.obj462, rootNode)
    self.obj462.postAction( rootNode.CREATE )

    self.obj463=Attribute(self)
    self.obj463.isGraphObjectVisual = True

    if(hasattr(self.obj463, '_setHierarchicalLink')):
      self.obj463._setHierarchicalLink(False)

    # Type
    self.obj463.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj463.Type.config = 0

    # name
    self.obj463.name.setValue('name')

    self.obj463.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,300.0,self.obj463)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj463.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj463)
    self.globalAndLocalPostcondition(self.obj463, rootNode)
    self.obj463.postAction( rootNode.CREATE )

    self.obj464=Attribute(self)
    self.obj464.isGraphObjectVisual = True

    if(hasattr(self.obj464, '_setHierarchicalLink')):
      self.obj464._setHierarchicalLink(False)

    # Type
    self.obj464.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj464.Type.config = 0

    # name
    self.obj464.name.setValue('literal')

    self.obj464.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(860.0,400.0,self.obj464)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj464.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj464)
    self.globalAndLocalPostcondition(self.obj464, rootNode)
    self.obj464.postAction( rootNode.CREATE )

    self.obj465=Attribute(self)
    self.obj465.isGraphObjectVisual = True

    if(hasattr(self.obj465, '_setHierarchicalLink')):
      self.obj465._setHierarchicalLink(False)

    # Type
    self.obj465.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj465.Type.config = 0

    # name
    self.obj465.name.setValue('channel')

    self.obj465.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(880.0,520.0,self.obj465)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj465.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj465)
    self.globalAndLocalPostcondition(self.obj465, rootNode)
    self.obj465.postAction( rootNode.CREATE )

    self.obj466=Attribute(self)
    self.obj466.isGraphObjectVisual = True

    if(hasattr(self.obj466, '_setHierarchicalLink')):
      self.obj466._setHierarchicalLink(False)

    # Type
    self.obj466.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj466.Type.config = 0

    # name
    self.obj466.name.setValue('pivot')

    self.obj466.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(180.0,560.0,self.obj466)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj466.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj466)
    self.globalAndLocalPostcondition(self.obj466, rootNode)
    self.obj466.postAction( rootNode.CREATE )

    self.obj467=Attribute(self)
    self.obj467.isGraphObjectVisual = True

    if(hasattr(self.obj467, '_setHierarchicalLink')):
      self.obj467._setHierarchicalLink(False)

    # Type
    self.obj467.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj467.Type.config = 0

    # name
    self.obj467.name.setValue('pivot')

    self.obj467.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(500.0,620.0,self.obj467)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj467.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj467)
    self.globalAndLocalPostcondition(self.obj467, rootNode)
    self.obj467.postAction( rootNode.CREATE )

    self.obj468=Equation(self)
    self.obj468.isGraphObjectVisual = True

    if(hasattr(self.obj468, '_setHierarchicalLink')):
      self.obj468._setHierarchicalLink(False)

    # name
    self.obj468.name.setValue('eq1')

    self.obj468.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(300.0,220.0,self.obj468)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj468.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj468)
    self.globalAndLocalPostcondition(self.obj468, rootNode)
    self.obj468.postAction( rootNode.CREATE )

    self.obj469=Equation(self)
    self.obj469.isGraphObjectVisual = True

    if(hasattr(self.obj469, '_setHierarchicalLink')):
      self.obj469._setHierarchicalLink(False)

    # name
    self.obj469.name.setValue('eq2')

    self.obj469.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(700.0,280.0,self.obj469)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj469.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj469)
    self.globalAndLocalPostcondition(self.obj469, rootNode)
    self.obj469.postAction( rootNode.CREATE )

    self.obj470=Equation(self)
    self.obj470.isGraphObjectVisual = True

    if(hasattr(self.obj470, '_setHierarchicalLink')):
      self.obj470._setHierarchicalLink(False)

    # name
    self.obj470.name.setValue('eq3')

    self.obj470.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(960.0,320.0,self.obj470)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj470.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj470)
    self.globalAndLocalPostcondition(self.obj470, rootNode)
    self.obj470.postAction( rootNode.CREATE )

    self.obj471=Equation(self)
    self.obj471.isGraphObjectVisual = True

    if(hasattr(self.obj471, '_setHierarchicalLink')):
      self.obj471._setHierarchicalLink(False)

    # name
    self.obj471.name.setValue('eq4')

    self.obj471.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(960.0,600.0,self.obj471)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj471.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj471)
    self.globalAndLocalPostcondition(self.obj471, rootNode)
    self.obj471.postAction( rootNode.CREATE )

    self.obj472=Equation(self)
    self.obj472.isGraphObjectVisual = True

    if(hasattr(self.obj472, '_setHierarchicalLink')):
      self.obj472._setHierarchicalLink(False)

    # name
    self.obj472.name.setValue('eq5')

    self.obj472.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(260.0,640.0,self.obj472)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj472.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj472)
    self.globalAndLocalPostcondition(self.obj472, rootNode)
    self.obj472.postAction( rootNode.CREATE )

    self.obj473=Equation(self)
    self.obj473.isGraphObjectVisual = True

    if(hasattr(self.obj473, '_setHierarchicalLink')):
      self.obj473._setHierarchicalLink(False)

    # name
    self.obj473.name.setValue('eq6')

    self.obj473.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(560.0,700.0,self.obj473)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj473.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj473)
    self.globalAndLocalPostcondition(self.obj473, rootNode)
    self.obj473.postAction( rootNode.CREATE )

    self.obj474=Concat(self)
    self.obj474.isGraphObjectVisual = True

    if(hasattr(self.obj474, '_setHierarchicalLink')):
      self.obj474._setHierarchicalLink(False)

    # Type
    self.obj474.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj474.Type.config = 0

    # name
    self.obj474.name.setValue('concat1')

    self.obj474.graphClass_= graph_Concat
    if self.genGraphics:
       new_obj = graph_Concat(500.0,200.0,self.obj474)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj474.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj474)
    self.globalAndLocalPostcondition(self.obj474, rootNode)
    self.obj474.postAction( rootNode.CREATE )

    self.obj475=Constant(self)
    self.obj475.isGraphObjectVisual = True

    if(hasattr(self.obj475, '_setHierarchicalLink')):
      self.obj475._setHierarchicalLink(False)

    # Type
    self.obj475.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj475.Type.config = 0

    # name
    self.obj475.name.setValue('true')

    self.obj475.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(340.0,140.0,self.obj475)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj475.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj475)
    self.globalAndLocalPostcondition(self.obj475, rootNode)
    self.obj475.postAction( rootNode.CREATE )

    self.obj476=Constant(self)
    self.obj476.isGraphObjectVisual = True

    if(hasattr(self.obj476, '_setHierarchicalLink')):
      self.obj476._setHierarchicalLink(False)

    # Type
    self.obj476.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj476.Type.config = 0

    # name
    self.obj476.name.setValue('B')

    self.obj476.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(700.0,200.0,self.obj476)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj476.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj476)
    self.globalAndLocalPostcondition(self.obj476, rootNode)
    self.obj476.postAction( rootNode.CREATE )

    self.obj477=Constant(self)
    self.obj477.isGraphObjectVisual = True

    if(hasattr(self.obj477, '_setHierarchicalLink')):
      self.obj477._setHierarchicalLink(False)

    # Type
    self.obj477.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj477.Type.config = 0

    # name
    self.obj477.name.setValue('sh_in')

    self.obj477.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1020.0,400.0,self.obj477)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj477.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj477)
    self.globalAndLocalPostcondition(self.obj477, rootNode)
    self.obj477.postAction( rootNode.CREATE )

    self.obj478=Constant(self)
    self.obj478.isGraphObjectVisual = True

    if(hasattr(self.obj478, '_setHierarchicalLink')):
      self.obj478._setHierarchicalLink(False)

    # Type
    self.obj478.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj478.Type.config = 0

    # name
    self.obj478.name.setValue('sh_in')

    self.obj478.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1040.0,520.0,self.obj478)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj478.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj478)
    self.globalAndLocalPostcondition(self.obj478, rootNode)
    self.obj478.postAction( rootNode.CREATE )

    self.obj479=Constant(self)
    self.obj479.isGraphObjectVisual = True

    if(hasattr(self.obj479, '_setHierarchicalLink')):
      self.obj479._setHierarchicalLink(False)

    # Type
    self.obj479.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj479.Type.config = 0

    # name
    self.obj479.name.setValue('localdefcompstate')

    self.obj479.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(340.0,560.0,self.obj479)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj479.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj479)
    self.globalAndLocalPostcondition(self.obj479, rootNode)
    self.obj479.postAction( rootNode.CREATE )

    self.obj480=Constant(self)
    self.obj480.isGraphObjectVisual = True

    if(hasattr(self.obj480, '_setHierarchicalLink')):
      self.obj480._setHierarchicalLink(False)

    # Type
    self.obj480.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj480.Type.config = 0

    # name
    self.obj480.name.setValue('parexitpoint')

    self.obj480.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(660.0,620.0,self.obj480)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj480.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj480)
    self.globalAndLocalPostcondition(self.obj480, rootNode)
    self.obj480.postAction( rootNode.CREATE )

    self.obj481=paired_with(self)
    self.obj481.isGraphObjectVisual = True

    if(hasattr(self.obj481, '_setHierarchicalLink')):
      self.obj481._setHierarchicalLink(False)

    self.obj481.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,152.0,self.obj481)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj481.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj481)
    self.globalAndLocalPostcondition(self.obj481, rootNode)
    self.obj481.postAction( rootNode.CREATE )

    self.obj482=match_contains(self)
    self.obj482.isGraphObjectVisual = True

    if(hasattr(self.obj482, '_setHierarchicalLink')):
      self.obj482._setHierarchicalLink(False)

    self.obj482.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(244.0,67.0,self.obj482)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj482.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj482)
    self.globalAndLocalPostcondition(self.obj482, rootNode)
    self.obj482.postAction( rootNode.CREATE )

    self.obj483=match_contains(self)
    self.obj483.isGraphObjectVisual = True

    if(hasattr(self.obj483, '_setHierarchicalLink')):
      self.obj483._setHierarchicalLink(False)

    self.obj483.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(394.0,67.0,self.obj483)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj483.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj483)
    self.globalAndLocalPostcondition(self.obj483, rootNode)
    self.obj483.postAction( rootNode.CREATE )

    self.obj484=apply_contains(self)
    self.obj484.isGraphObjectVisual = True

    if(hasattr(self.obj484, '_setHierarchicalLink')):
      self.obj484._setHierarchicalLink(False)

    self.obj484.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(247.5,375.0,self.obj484)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj484.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj484)
    self.globalAndLocalPostcondition(self.obj484, rootNode)
    self.obj484.postAction( rootNode.CREATE )

    self.obj485=apply_contains(self)
    self.obj485.isGraphObjectVisual = True

    if(hasattr(self.obj485, '_setHierarchicalLink')):
      self.obj485._setHierarchicalLink(False)

    self.obj485.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(377.5,374.0,self.obj485)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj485.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj485)
    self.globalAndLocalPostcondition(self.obj485, rootNode)
    self.obj485.postAction( rootNode.CREATE )

    self.obj486=apply_contains(self)
    self.obj486.isGraphObjectVisual = True

    if(hasattr(self.obj486, '_setHierarchicalLink')):
      self.obj486._setHierarchicalLink(False)

    self.obj486.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(487.5,382.0,self.obj486)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj486.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj486)
    self.globalAndLocalPostcondition(self.obj486, rootNode)
    self.obj486.postAction( rootNode.CREATE )

    self.obj487=apply_contains(self)
    self.obj487.isGraphObjectVisual = True

    if(hasattr(self.obj487, '_setHierarchicalLink')):
      self.obj487._setHierarchicalLink(False)

    self.obj487.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(219.5,486.0,self.obj487)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj487.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj487)
    self.globalAndLocalPostcondition(self.obj487, rootNode)
    self.obj487.postAction( rootNode.CREATE )

    self.obj488=apply_contains(self)
    self.obj488.isGraphObjectVisual = True

    if(hasattr(self.obj488, '_setHierarchicalLink')):
      self.obj488._setHierarchicalLink(False)

    self.obj488.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(507.5,442.0,self.obj488)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj488.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj488)
    self.globalAndLocalPostcondition(self.obj488, rootNode)
    self.obj488.postAction( rootNode.CREATE )

    self.obj489=directLink_T(self)
    self.obj489.isGraphObjectVisual = True

    if(hasattr(self.obj489, '_setHierarchicalLink')):
      self.obj489._setHierarchicalLink(False)

    # associationType
    self.obj489.associationType.setValue('def')

    self.obj489.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(431.0,427.0,self.obj489)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj489.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj489)
    self.globalAndLocalPostcondition(self.obj489, rootNode)
    self.obj489.postAction( rootNode.CREATE )

    self.obj490=directLink_T(self)
    self.obj490.isGraphObjectVisual = True

    if(hasattr(self.obj490, '_setHierarchicalLink')):
      self.obj490._setHierarchicalLink(False)

    # associationType
    self.obj490.associationType.setValue('channelNames')

    self.obj490.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(752.0,431.0,self.obj490)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj490.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj490)
    self.globalAndLocalPostcondition(self.obj490, rootNode)
    self.obj490.postAction( rootNode.CREATE )

    self.obj491=directLink_T(self)
    self.obj491.isGraphObjectVisual = True

    if(hasattr(self.obj491, '_setHierarchicalLink')):
      self.obj491._setHierarchicalLink(False)

    # associationType
    self.obj491.associationType.setValue('p')

    self.obj491.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(652.0,491.0,self.obj491)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj491.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj491)
    self.globalAndLocalPostcondition(self.obj491, rootNode)
    self.obj491.postAction( rootNode.CREATE )

    self.obj492=directLink_T(self)
    self.obj492.isGraphObjectVisual = True

    if(hasattr(self.obj492, '_setHierarchicalLink')):
      self.obj492._setHierarchicalLink(False)

    # associationType
    self.obj492.associationType.setValue('p')

    self.obj492.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(772.0,551.0,self.obj492)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj492.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj492)
    self.globalAndLocalPostcondition(self.obj492, rootNode)
    self.obj492.postAction( rootNode.CREATE )

    self.obj493=directLink_S(self)
    self.obj493.isGraphObjectVisual = True

    if(hasattr(self.obj493, '_setHierarchicalLink')):
      self.obj493._setHierarchicalLink(False)

    # associationType
    self.obj493.associationType.setValue('exitPoints')

    self.obj493.graphClass_= graph_directLink_S
    if self.genGraphics:
       new_obj = graph_directLink_S(500.0,83.0,self.obj493)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj493.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj493)
    self.globalAndLocalPostcondition(self.obj493, rootNode)
    self.obj493.postAction( rootNode.CREATE )

    self.obj494=backward_link(self)
    self.obj494.isGraphObjectVisual = True

    if(hasattr(self.obj494, '_setHierarchicalLink')):
      self.obj494._setHierarchicalLink(False)

    # type
    self.obj494.type.setValue('ruleDef')

    self.obj494.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(371.0,257.0,self.obj494)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj494.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj494)
    self.globalAndLocalPostcondition(self.obj494, rootNode)
    self.obj494.postAction( rootNode.CREATE )

    self.obj495=hasAttribute_S(self)
    self.obj495.isGraphObjectVisual = True

    if(hasattr(self.obj495, '_setHierarchicalLink')):
      self.obj495._setHierarchicalLink(False)

    self.obj495.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(328.0,136.5,self.obj495)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj495.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj495)
    self.globalAndLocalPostcondition(self.obj495, rootNode)
    self.obj495.postAction( rootNode.CREATE )

    self.obj496=hasAttribute_S(self)
    self.obj496.isGraphObjectVisual = True

    if(hasattr(self.obj496, '_setHierarchicalLink')):
      self.obj496._setHierarchicalLink(False)

    self.obj496.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(742.0,108.5,self.obj496)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj496.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj496)
    self.globalAndLocalPostcondition(self.obj496, rootNode)
    self.obj496.postAction( rootNode.CREATE )

    self.obj497=hasAttribute_T(self)
    self.obj497.isGraphObjectVisual = True

    if(hasattr(self.obj497, '_setHierarchicalLink')):
      self.obj497._setHierarchicalLink(False)

    self.obj497.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(634.0,364.5,self.obj497)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj497.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj497)
    self.globalAndLocalPostcondition(self.obj497, rootNode)
    self.obj497.postAction( rootNode.CREATE )

    self.obj498=hasAttribute_T(self)
    self.obj498.isGraphObjectVisual = True

    if(hasattr(self.obj498, '_setHierarchicalLink')):
      self.obj498._setHierarchicalLink(False)

    self.obj498.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(913.0,432.5,self.obj498)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj498.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj498)
    self.globalAndLocalPostcondition(self.obj498, rootNode)
    self.obj498.postAction( rootNode.CREATE )

    self.obj499=hasAttribute_T(self)
    self.obj499.isGraphObjectVisual = True

    if(hasattr(self.obj499, '_setHierarchicalLink')):
      self.obj499._setHierarchicalLink(False)

    self.obj499.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(943.0,552.5,self.obj499)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj499.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj499)
    self.globalAndLocalPostcondition(self.obj499, rootNode)
    self.obj499.postAction( rootNode.CREATE )

    self.obj500=hasAttribute_T(self)
    self.obj500.isGraphObjectVisual = True

    if(hasattr(self.obj500, '_setHierarchicalLink')):
      self.obj500._setHierarchicalLink(False)

    self.obj500.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(353.0,512.5,self.obj500)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj500.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj500)
    self.globalAndLocalPostcondition(self.obj500, rootNode)
    self.obj500.postAction( rootNode.CREATE )

    self.obj501=hasAttribute_T(self)
    self.obj501.isGraphObjectVisual = True

    if(hasattr(self.obj501, '_setHierarchicalLink')):
      self.obj501._setHierarchicalLink(False)

    self.obj501.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(653.0,602.5,self.obj501)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj501.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj501)
    self.globalAndLocalPostcondition(self.obj501, rootNode)
    self.obj501.postAction( rootNode.CREATE )

    self.obj502=leftExpr(self)
    self.obj502.isGraphObjectVisual = True

    if(hasattr(self.obj502, '_setHierarchicalLink')):
      self.obj502._setHierarchicalLink(False)

    self.obj502.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(359.0,213.5,self.obj502)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj502.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj502)
    self.globalAndLocalPostcondition(self.obj502, rootNode)
    self.obj502.postAction( rootNode.CREATE )

    self.obj503=leftExpr(self)
    self.obj503.isGraphObjectVisual = True

    if(hasattr(self.obj503, '_setHierarchicalLink')):
      self.obj503._setHierarchicalLink(False)

    self.obj503.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(746.0,326.5,self.obj503)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj503.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj503)
    self.globalAndLocalPostcondition(self.obj503, rootNode)
    self.obj503.postAction( rootNode.CREATE )

    self.obj504=leftExpr(self)
    self.obj504.isGraphObjectVisual = True

    if(hasattr(self.obj504, '_setHierarchicalLink')):
      self.obj504._setHierarchicalLink(False)

    self.obj504.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1052.0,380.5,self.obj504)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj504.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj504)
    self.globalAndLocalPostcondition(self.obj504, rootNode)
    self.obj504.postAction( rootNode.CREATE )

    self.obj505=leftExpr(self)
    self.obj505.isGraphObjectVisual = True

    if(hasattr(self.obj505, '_setHierarchicalLink')):
      self.obj505._setHierarchicalLink(False)

    self.obj505.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1056.0,596.5,self.obj505)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj505.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj505)
    self.globalAndLocalPostcondition(self.obj505, rootNode)
    self.obj505.postAction( rootNode.CREATE )

    self.obj506=leftExpr(self)
    self.obj506.isGraphObjectVisual = True

    if(hasattr(self.obj506, '_setHierarchicalLink')):
      self.obj506._setHierarchicalLink(False)

    self.obj506.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(356.0,636.5,self.obj506)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj506.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj506)
    self.globalAndLocalPostcondition(self.obj506, rootNode)
    self.obj506.postAction( rootNode.CREATE )

    self.obj507=leftExpr(self)
    self.obj507.isGraphObjectVisual = True

    if(hasattr(self.obj507, '_setHierarchicalLink')):
      self.obj507._setHierarchicalLink(False)

    self.obj507.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(666.0,696.5,self.obj507)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj507.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj507)
    self.globalAndLocalPostcondition(self.obj507, rootNode)
    self.obj507.postAction( rootNode.CREATE )

    self.obj508=rightExpr(self)
    self.obj508.isGraphObjectVisual = True

    if(hasattr(self.obj508, '_setHierarchicalLink')):
      self.obj508._setHierarchicalLink(False)

    self.obj508.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(457.0,212.5,self.obj508)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj508.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj508)
    self.globalAndLocalPostcondition(self.obj508, rootNode)
    self.obj508.postAction( rootNode.CREATE )

    self.obj509=rightExpr(self)
    self.obj509.isGraphObjectVisual = True

    if(hasattr(self.obj509, '_setHierarchicalLink')):
      self.obj509._setHierarchicalLink(False)

    self.obj509.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(746.0,276.5,self.obj509)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj509.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj509)
    self.globalAndLocalPostcondition(self.obj509, rootNode)
    self.obj509.postAction( rootNode.CREATE )

    self.obj510=rightExpr(self)
    self.obj510.isGraphObjectVisual = True

    if(hasattr(self.obj510, '_setHierarchicalLink')):
      self.obj510._setHierarchicalLink(False)

    self.obj510.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1126.0,396.5,self.obj510)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj510.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj510)
    self.globalAndLocalPostcondition(self.obj510, rootNode)
    self.obj510.postAction( rootNode.CREATE )

    self.obj511=rightExpr(self)
    self.obj511.isGraphObjectVisual = True

    if(hasattr(self.obj511, '_setHierarchicalLink')):
      self.obj511._setHierarchicalLink(False)

    self.obj511.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1136.0,596.5,self.obj511)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj511.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj511)
    self.globalAndLocalPostcondition(self.obj511, rootNode)
    self.obj511.postAction( rootNode.CREATE )

    self.obj512=rightExpr(self)
    self.obj512.isGraphObjectVisual = True

    if(hasattr(self.obj512, '_setHierarchicalLink')):
      self.obj512._setHierarchicalLink(False)

    self.obj512.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(436.0,636.5,self.obj512)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj512.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj512)
    self.globalAndLocalPostcondition(self.obj512, rootNode)
    self.obj512.postAction( rootNode.CREATE )

    self.obj513=rightExpr(self)
    self.obj513.isGraphObjectVisual = True

    if(hasattr(self.obj513, '_setHierarchicalLink')):
      self.obj513._setHierarchicalLink(False)

    self.obj513.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(746.0,696.5,self.obj513)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj513.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj513)
    self.globalAndLocalPostcondition(self.obj513, rootNode)
    self.obj513.postAction( rootNode.CREATE )

    self.obj514=hasArgs(self)
    self.obj514.isGraphObjectVisual = True

    if(hasattr(self.obj514, '_setHierarchicalLink')):
      self.obj514._setHierarchicalLink(False)

    self.obj514.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(744.0,234.0,self.obj514)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj514.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj514)
    self.globalAndLocalPostcondition(self.obj514, rootNode)
    self.obj514.postAction( rootNode.CREATE )

    self.obj515=hasArgs(self)
    self.obj515.isGraphObjectVisual = True

    if(hasattr(self.obj515, '_setHierarchicalLink')):
      self.obj515._setHierarchicalLink(False)

    self.obj515.graphClass_= graph_hasArgs
    if self.genGraphics:
       new_obj = graph_hasArgs(744.0,184.0,self.obj515)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasArgs", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj515.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj515)
    self.globalAndLocalPostcondition(self.obj515, rootNode)
    self.obj515.postAction( rootNode.CREATE )

    # Connections for obj452 (graphObject_: Obj319) of type MatchModel
    self.drawConnections(
(self.obj452,self.obj481,[138.0, 51.0, 140.5, 152.0],"true", 2),
(self.obj452,self.obj482,[138.0, 51.0, 244.0, 67.0],"true", 2),
(self.obj452,self.obj483,[138.0, 51.0, 394.0, 67.0],"true", 2) )
    # Connections for obj453 (graphObject_: Obj320) of type ApplyModel
    self.drawConnections(
(self.obj453,self.obj484,[143.0, 333.0, 247.5, 375.0],"true", 2),
(self.obj453,self.obj485,[143.0, 333.0, 377.5, 374.0],"true", 2),
(self.obj453,self.obj486,[143.0, 333.0, 487.5, 382.0],"true", 2),
(self.obj453,self.obj487,[143.0, 333.0, 219.5, 486.0],"true", 2),
(self.obj453,self.obj488,[143.0, 333.0, 507.5, 442.0],"true", 2) )
    # Connections for obj454 (graphObject_: Obj321) named exitpoint1
    self.drawConnections(
(self.obj454,self.obj496,[650.0, 83.0, 742.0, 108.5],"true", 2) )
    # Connections for obj455 (graphObject_: Obj322) named state1
    self.drawConnections(
(self.obj455,self.obj493,[350.0, 83.0, 500.0, 83.0],"true", 2),
(self.obj455,self.obj495,[350.0, 83.0, 328.0, 136.5],"true", 2) )
    # Connections for obj456 (graphObject_: Obj323) named procdef1
    self.drawConnections(
(self.obj456,self.obj497,[632.0, 431.0, 634.0, 364.5],"true", 2),
(self.obj456,self.obj490,[632.0, 431.0, 752.0, 431.0],"true", 2),
(self.obj456,self.obj491,[632.0, 431.0, 652.0, 491.0],"true", 2) )
    # Connections for obj457 (graphObject_: Obj324) named name1
    self.drawConnections(
(self.obj457,self.obj498,[832.0, 431.0, 913.0, 432.5],"true", 2) )
    # Connections for obj458 (graphObject_: Obj325) named triggerT1
    self.drawConnections(
(self.obj458,self.obj499,[872.0, 551.0, 943.0, 552.5],"true", 2) )
    # Connections for obj459 (graphObject_: Obj326) named par1
    self.drawConnections(
(self.obj459,self.obj492,[672.0, 551.0, 772.0, 551.0],"true", 2),
(self.obj459,self.obj501,[672.0, 551.0, 653.0, 602.5],"true", 2) )
    # Connections for obj460 (graphObject_: Obj327) named localdef1
    self.drawConnections(
(self.obj460,self.obj489,[392.0, 431.0, 431.0, 427.0],"true", 2),
(self.obj460,self.obj494,[392.0, 431.0, 371.0, 257.0],"true", 2),
(self.obj460,self.obj500,[392.0, 431.0, 353.0, 512.5],"true", 2) )
    # Connections for obj461 (graphObject_: Obj328) named isComposite
    self.drawConnections(
 )
    # Connections for obj462 (graphObject_: Obj329) named name
    self.drawConnections(
 )
    # Connections for obj463 (graphObject_: Obj330) named name
    self.drawConnections(
 )
    # Connections for obj464 (graphObject_: Obj331) named literal
    self.drawConnections(
 )
    # Connections for obj465 (graphObject_: Obj332) named channel
    self.drawConnections(
 )
    # Connections for obj466 (graphObject_: Obj333) named pivot
    self.drawConnections(
 )
    # Connections for obj467 (graphObject_: Obj334) named pivot
    self.drawConnections(
 )
    # Connections for obj468 (graphObject_: Obj335) named eq1
    self.drawConnections(
(self.obj468,self.obj502,[438.0, 259.0, 359.0, 213.5],"true", 2),
(self.obj468,self.obj508,[438.0, 259.0, 457.0, 212.5],"true", 2) )
    # Connections for obj469 (graphObject_: Obj336) named eq2
    self.drawConnections(
(self.obj469,self.obj509,[838.0, 319.0, 746.0, 276.5],"true", 2),
(self.obj469,self.obj503,[838.0, 319.0, 746.0, 326.5],"true", 2) )
    # Connections for obj470 (graphObject_: Obj337) named eq3
    self.drawConnections(
(self.obj470,self.obj504,[1098.0, 359.0, 1052.0, 380.5],"true", 2),
(self.obj470,self.obj510,[1098.0, 359.0, 1126.0, 396.5],"true", 2) )
    # Connections for obj471 (graphObject_: Obj338) named eq4
    self.drawConnections(
(self.obj471,self.obj505,[1098.0, 639.0, 1056.0, 596.5],"true", 2),
(self.obj471,self.obj511,[1098.0, 639.0, 1136.0, 596.5],"true", 2) )
    # Connections for obj472 (graphObject_: Obj339) named eq5
    self.drawConnections(
(self.obj472,self.obj506,[398.0, 679.0, 356.0, 636.5],"true", 2),
(self.obj472,self.obj512,[398.0, 679.0, 436.0, 636.5],"true", 2) )
    # Connections for obj473 (graphObject_: Obj340) named eq6
    self.drawConnections(
(self.obj473,self.obj507,[698.0, 739.0, 666.0, 696.5],"true", 2),
(self.obj473,self.obj513,[698.0, 739.0, 746.0, 696.5],"true", 2) )
    # Connections for obj474 (graphObject_: Obj341) named concat1
    self.drawConnections(
(self.obj474,self.obj514,[634.0, 234.0, 744.0, 234.0],"true", 2),
(self.obj474,self.obj515,[634.0, 234.0, 744.0, 184.0],"true", 2) )
    # Connections for obj475 (graphObject_: Obj342) named true
    self.drawConnections(
 )
    # Connections for obj476 (graphObject_: Obj343) named B
    self.drawConnections(
 )
    # Connections for obj477 (graphObject_: Obj344) named sh_in
    self.drawConnections(
 )
    # Connections for obj478 (graphObject_: Obj345) named sh_in
    self.drawConnections(
 )
    # Connections for obj479 (graphObject_: Obj346) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj480 (graphObject_: Obj347) named parexitpoint
    self.drawConnections(
 )
    # Connections for obj481 (graphObject_: Obj348) of type paired_with
    self.drawConnections(
(self.obj481,self.obj453,[140.5, 152.0, 143.0, 333.0],"true", 2) )
    # Connections for obj482 (graphObject_: Obj349) of type match_contains
    self.drawConnections(
(self.obj482,self.obj455,[244.0, 67.0, 350.0, 83.0],"true", 2) )
    # Connections for obj483 (graphObject_: Obj350) of type match_contains
    self.drawConnections(
(self.obj483,self.obj454,[394.0, 67.0, 650.0, 83.0],"true", 2) )
    # Connections for obj484 (graphObject_: Obj351) of type apply_contains
    self.drawConnections(
(self.obj484,self.obj460,[247.5, 375.0, 392.0, 431.0],"true", 2) )
    # Connections for obj485 (graphObject_: Obj352) of type apply_contains
    self.drawConnections(
(self.obj485,self.obj456,[377.5, 374.0, 632.0, 431.0],"true", 2) )
    # Connections for obj486 (graphObject_: Obj353) of type apply_contains
    self.drawConnections(
(self.obj486,self.obj457,[487.5, 382.0, 832.0, 431.0],"true", 2) )
    # Connections for obj487 (graphObject_: Obj354) of type apply_contains
    self.drawConnections(
(self.obj487,self.obj459,[222.5, 542.0, 672.0, 551.0],"true", 2) )
    # Connections for obj488 (graphObject_: Obj355) of type apply_contains
    self.drawConnections(
(self.obj488,self.obj458,[507.5, 442.0, 872.0, 551.0],"true", 2) )
    # Connections for obj489 (graphObject_: Obj356) of type directLink_T
    self.drawConnections(
(self.obj489,self.obj456,[431.0, 427.0, 632.0, 431.0],"true", 2) )
    # Connections for obj490 (graphObject_: Obj357) of type directLink_T
    self.drawConnections(
(self.obj490,self.obj457,[752.0, 431.0, 832.0, 431.0],"true", 2) )
    # Connections for obj491 (graphObject_: Obj358) of type directLink_T
    self.drawConnections(
(self.obj491,self.obj459,[652.0, 491.0, 672.0, 551.0],"true", 2) )
    # Connections for obj492 (graphObject_: Obj359) of type directLink_T
    self.drawConnections(
(self.obj492,self.obj458,[772.0, 551.0, 872.0, 551.0],"true", 2) )
    # Connections for obj493 (graphObject_: Obj360) of type directLink_S
    self.drawConnections(
(self.obj493,self.obj454,[500.0, 83.0, 650.0, 83.0],"true", 2) )
    # Connections for obj494 (graphObject_: Obj361) of type backward_link
    self.drawConnections(
(self.obj494,self.obj455,[371.0, 257.0, 350.0, 83.0],"true", 2) )
    # Connections for obj495 (graphObject_: Obj362) of type hasAttribute_S
    self.drawConnections(
(self.obj495,self.obj461,[328.0, 136.5, 314.0, 174.0],"true", 2) )
    # Connections for obj496 (graphObject_: Obj363) of type hasAttribute_S
    self.drawConnections(
(self.obj496,self.obj462,[742.0, 108.5, 834.0, 134.0],"true", 2) )
    # Connections for obj497 (graphObject_: Obj364) of type hasAttribute_T
    self.drawConnections(
(self.obj497,self.obj463,[634.0, 364.5, 634.0, 334.0],"true", 2) )
    # Connections for obj498 (graphObject_: Obj365) of type hasAttribute_T
    self.drawConnections(
(self.obj498,self.obj464,[913.0, 432.5, 994.0, 434.0],"true", 2) )
    # Connections for obj499 (graphObject_: Obj366) of type hasAttribute_T
    self.drawConnections(
(self.obj499,self.obj465,[943.0, 552.5, 1014.0, 554.0],"true", 2) )
    # Connections for obj500 (graphObject_: Obj367) of type hasAttribute_T
    self.drawConnections(
(self.obj500,self.obj466,[353.0, 512.5, 314.0, 594.0],"true", 2) )
    # Connections for obj501 (graphObject_: Obj368) of type hasAttribute_T
    self.drawConnections(
(self.obj501,self.obj467,[653.0, 602.5, 634.0, 654.0],"true", 2) )
    # Connections for obj502 (graphObject_: Obj369) of type leftExpr
    self.drawConnections(
(self.obj502,self.obj461,[359.0, 213.5, 314.0, 174.0],"true", 2) )
    # Connections for obj503 (graphObject_: Obj370) of type leftExpr
    self.drawConnections(
(self.obj503,self.obj463,[746.0, 326.5, 634.0, 334.0],"true", 2) )
    # Connections for obj504 (graphObject_: Obj371) of type leftExpr
    self.drawConnections(
(self.obj504,self.obj464,[1046.0, 396.5, 994.0, 434.0],"true", 2) )
    # Connections for obj505 (graphObject_: Obj372) of type leftExpr
    self.drawConnections(
(self.obj505,self.obj465,[1056.0, 596.5, 1014.0, 554.0],"true", 2) )
    # Connections for obj506 (graphObject_: Obj373) of type leftExpr
    self.drawConnections(
(self.obj506,self.obj466,[356.0, 636.5, 314.0, 594.0],"true", 2) )
    # Connections for obj507 (graphObject_: Obj374) of type leftExpr
    self.drawConnections(
(self.obj507,self.obj467,[666.0, 696.5, 634.0, 654.0],"true", 2) )
    # Connections for obj508 (graphObject_: Obj375) of type rightExpr
    self.drawConnections(
(self.obj508,self.obj475,[457.0, 212.5, 474.0, 174.0],"true", 2) )
    # Connections for obj509 (graphObject_: Obj376) of type rightExpr
    self.drawConnections(
(self.obj509,self.obj474,[746.0, 276.5, 634.0, 234.0],"true", 2) )
    # Connections for obj510 (graphObject_: Obj377) of type rightExpr
    self.drawConnections(
(self.obj510,self.obj477,[1126.0, 396.5, 1154.0, 434.0],"true", 2) )
    # Connections for obj511 (graphObject_: Obj378) of type rightExpr
    self.drawConnections(
(self.obj511,self.obj478,[1136.0, 596.5, 1174.0, 554.0],"true", 2) )
    # Connections for obj512 (graphObject_: Obj379) of type rightExpr
    self.drawConnections(
(self.obj512,self.obj479,[436.0, 636.5, 474.0, 594.0],"true", 2) )
    # Connections for obj513 (graphObject_: Obj380) of type rightExpr
    self.drawConnections(
(self.obj513,self.obj480,[746.0, 696.5, 794.0, 654.0],"true", 2) )
    # Connections for obj514 (graphObject_: Obj381) of type hasArgs
    self.drawConnections(
(self.obj514,self.obj476,[744.0, 234.0, 834.0, 234.0],"true", 2) )
    # Connections for obj515 (graphObject_: Obj382) of type hasArgs
    self.drawConnections(
(self.obj515,self.obj462,[744.0, 184.0, 834.0, 134.0],"true", 2) )

newfunction = ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
