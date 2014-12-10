"""
__CompositeState2ProcDef_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Wed Oct 15 14:43:01 2014
____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MatchModel import *
from ApplyModel import *
from State import *
from ProcDef import *
from Name import *
from New import *
from Par import *
from Inst import *
from LocalDef import *
from Attribute import *
from Equation import *
from Constant import *
from paired_with import *
from match_contains import *
from apply_contains import *
from directLink_T import *
from backward_link import *
from hasAttribute_S import *
from hasAttribute_T import *
from leftExpr import *
from rightExpr import *
from graph_Par import *
from graph_New import *
from graph_Equation import *
from graph_leftExpr import *
from graph_hasAttribute_T import *
from graph_Attribute import *
from graph_LocalDef import *
from graph_backward_link import *
from graph_directLink_T import *
from graph_MatchModel import *
from graph_apply_contains import *
from graph_rightExpr import *
from graph_paired_with import *
from graph_Name import *
from graph_match_contains import *
from graph_hasAttribute_S import *
from graph_Inst import *
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

def CompositeState2ProcDef_MDL(self, rootNode, UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG UMLRT2Kiltera_MM ---
    if( UMLRT2Kiltera_MMRootNode ): 
        # author
        UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        UMLRT2Kiltera_MMRootNode.name.setValue('CompositeState2ProcDef')
    # --- ASG attributes over ---


    self.obj959=MatchModel(self)
    self.obj959.isGraphObjectVisual = True

    if(hasattr(self.obj959, '_setHierarchicalLink')):
      self.obj959._setHierarchicalLink(False)

    self.obj959.graphClass_= graph_MatchModel
    if self.genGraphics:
       new_obj = graph_MatchModel(20.0,20.0,self.obj959)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj959.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj959)
    self.globalAndLocalPostcondition(self.obj959, rootNode)
    self.obj959.postAction( rootNode.CREATE )

    self.obj960=ApplyModel(self)
    self.obj960.isGraphObjectVisual = True

    if(hasattr(self.obj960, '_setHierarchicalLink')):
      self.obj960._setHierarchicalLink(False)

    self.obj960.graphClass_= graph_ApplyModel
    if self.genGraphics:
       new_obj = graph_ApplyModel(20.0,140.0,self.obj960)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj960.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj960)
    self.globalAndLocalPostcondition(self.obj960, rootNode)
    self.obj960.postAction( rootNode.CREATE )

    self.obj961=State(self)
    self.obj961.isGraphObjectVisual = True

    if(hasattr(self.obj961, '_setHierarchicalLink')):
      self.obj961._setHierarchicalLink(False)

    # name
    self.obj961.name.setValue('state1')

    # classtype
    self.obj961.classtype.setValue('State')

    # cardinality
    self.obj961.cardinality.setValue('+')

    self.obj961.graphClass_= graph_State
    if self.genGraphics:
       new_obj = graph_State(220.0,8.0,self.obj961)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("State", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj961.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj961)
    self.globalAndLocalPostcondition(self.obj961, rootNode)
    self.obj961.postAction( rootNode.CREATE )

    self.obj962=ProcDef(self)
    self.obj962.isGraphObjectVisual = True

    if(hasattr(self.obj962, '_setHierarchicalLink')):
      self.obj962._setHierarchicalLink(False)

    # classtype
    self.obj962.classtype.setValue('ProcDef')

    # cardinality
    self.obj962.cardinality.setValue('1')

    # name
    self.obj962.name.setValue('procdef1')

    self.obj962.graphClass_= graph_ProcDef
    if self.genGraphics:
       new_obj = graph_ProcDef(220.0,180.0,self.obj962)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ProcDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj962.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj962)
    self.globalAndLocalPostcondition(self.obj962, rootNode)
    self.obj962.postAction( rootNode.CREATE )

    self.obj963=Name(self)
    self.obj963.isGraphObjectVisual = True

    if(hasattr(self.obj963, '_setHierarchicalLink')):
      self.obj963._setHierarchicalLink(False)

    # classtype
    self.obj963.classtype.setValue('Name')

    # cardinality
    self.obj963.cardinality.setValue('1')

    # name
    self.obj963.name.setValue('name1')

    self.obj963.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(20.0,280.0,self.obj963)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj963.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj963)
    self.globalAndLocalPostcondition(self.obj963, rootNode)
    self.obj963.postAction( rootNode.CREATE )

    self.obj964=Name(self)
    self.obj964.isGraphObjectVisual = True

    if(hasattr(self.obj964, '_setHierarchicalLink')):
      self.obj964._setHierarchicalLink(False)

    # classtype
    self.obj964.classtype.setValue('Name')

    # cardinality
    self.obj964.cardinality.setValue('1')

    # name
    self.obj964.name.setValue('name2')

    self.obj964.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(220.0,460.0,self.obj964)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj964.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj964)
    self.globalAndLocalPostcondition(self.obj964, rootNode)
    self.obj964.postAction( rootNode.CREATE )

    self.obj965=Name(self)
    self.obj965.isGraphObjectVisual = True

    if(hasattr(self.obj965, '_setHierarchicalLink')):
      self.obj965._setHierarchicalLink(False)

    # classtype
    self.obj965.classtype.setValue('Name')

    # cardinality
    self.obj965.cardinality.setValue('1')

    # name
    self.obj965.name.setValue('name3')

    self.obj965.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(440.0,460.0,self.obj965)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj965.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj965)
    self.globalAndLocalPostcondition(self.obj965, rootNode)
    self.obj965.postAction( rootNode.CREATE )

    self.obj966=Name(self)
    self.obj966.isGraphObjectVisual = True

    if(hasattr(self.obj966, '_setHierarchicalLink')):
      self.obj966._setHierarchicalLink(False)

    # classtype
    self.obj966.classtype.setValue('Name')

    # cardinality
    self.obj966.cardinality.setValue('1')

    # name
    self.obj966.name.setValue('name4')

    self.obj966.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(640.0,460.0,self.obj966)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj966.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj966)
    self.globalAndLocalPostcondition(self.obj966, rootNode)
    self.obj966.postAction( rootNode.CREATE )

    self.obj967=Name(self)
    self.obj967.isGraphObjectVisual = True

    if(hasattr(self.obj967, '_setHierarchicalLink')):
      self.obj967._setHierarchicalLink(False)

    # classtype
    self.obj967.classtype.setValue('Name')

    # cardinality
    self.obj967.cardinality.setValue('1')

    # name
    self.obj967.name.setValue('name5')

    self.obj967.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,20.0,self.obj967)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj967.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj967)
    self.globalAndLocalPostcondition(self.obj967, rootNode)
    self.obj967.postAction( rootNode.CREATE )

    self.obj968=Name(self)
    self.obj968.isGraphObjectVisual = True

    if(hasattr(self.obj968, '_setHierarchicalLink')):
      self.obj968._setHierarchicalLink(False)

    # classtype
    self.obj968.classtype.setValue('Name')

    # cardinality
    self.obj968.cardinality.setValue('1')

    # name
    self.obj968.name.setValue('name6')

    self.obj968.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,120.0,self.obj968)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj968.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj968)
    self.globalAndLocalPostcondition(self.obj968, rootNode)
    self.obj968.postAction( rootNode.CREATE )

    self.obj969=Name(self)
    self.obj969.isGraphObjectVisual = True

    if(hasattr(self.obj969, '_setHierarchicalLink')):
      self.obj969._setHierarchicalLink(False)

    # classtype
    self.obj969.classtype.setValue('Name')

    # cardinality
    self.obj969.cardinality.setValue('1')

    # name
    self.obj969.name.setValue('name7')

    self.obj969.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,220.0,self.obj969)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj969.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj969)
    self.globalAndLocalPostcondition(self.obj969, rootNode)
    self.obj969.postAction( rootNode.CREATE )

    self.obj970=Name(self)
    self.obj970.isGraphObjectVisual = True

    if(hasattr(self.obj970, '_setHierarchicalLink')):
      self.obj970._setHierarchicalLink(False)

    # classtype
    self.obj970.classtype.setValue('Name')

    # cardinality
    self.obj970.cardinality.setValue('1')

    # name
    self.obj970.name.setValue('name8')

    self.obj970.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,320.0,self.obj970)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj970.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj970)
    self.globalAndLocalPostcondition(self.obj970, rootNode)
    self.obj970.postAction( rootNode.CREATE )

    self.obj971=Name(self)
    self.obj971.isGraphObjectVisual = True

    if(hasattr(self.obj971, '_setHierarchicalLink')):
      self.obj971._setHierarchicalLink(False)

    # classtype
    self.obj971.classtype.setValue('Name')

    # cardinality
    self.obj971.cardinality.setValue('1')

    # name
    self.obj971.name.setValue('name9')

    self.obj971.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,440.0,self.obj971)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj971.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj971)
    self.globalAndLocalPostcondition(self.obj971, rootNode)
    self.obj971.postAction( rootNode.CREATE )

    self.obj972=Name(self)
    self.obj972.isGraphObjectVisual = True

    if(hasattr(self.obj972, '_setHierarchicalLink')):
      self.obj972._setHierarchicalLink(False)

    # classtype
    self.obj972.classtype.setValue('Name')

    # cardinality
    self.obj972.cardinality.setValue('1')

    # name
    self.obj972.name.setValue('name10')

    self.obj972.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,540.0,self.obj972)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj972.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj972)
    self.globalAndLocalPostcondition(self.obj972, rootNode)
    self.obj972.postAction( rootNode.CREATE )

    self.obj973=Name(self)
    self.obj973.isGraphObjectVisual = True

    if(hasattr(self.obj973, '_setHierarchicalLink')):
      self.obj973._setHierarchicalLink(False)

    # classtype
    self.obj973.classtype.setValue('Name')

    # cardinality
    self.obj973.cardinality.setValue('1')

    # name
    self.obj973.name.setValue('name11')

    self.obj973.graphClass_= graph_Name
    if self.genGraphics:
       new_obj = graph_Name(1360.0,660.0,self.obj973)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj973.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj973)
    self.globalAndLocalPostcondition(self.obj973, rootNode)
    self.obj973.postAction( rootNode.CREATE )

    self.obj974=New(self)
    self.obj974.isGraphObjectVisual = True

    if(hasattr(self.obj974, '_setHierarchicalLink')):
      self.obj974._setHierarchicalLink(False)

    # classtype
    self.obj974.classtype.setValue('New')

    # cardinality
    self.obj974.cardinality.setValue('1')

    # name
    self.obj974.name.setValue('new1')

    self.obj974.graphClass_= graph_New
    if self.genGraphics:
       new_obj = graph_New(660.0,300.0,self.obj974)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("New", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj974.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj974)
    self.globalAndLocalPostcondition(self.obj974, rootNode)
    self.obj974.postAction( rootNode.CREATE )

    self.obj975=Par(self)
    self.obj975.isGraphObjectVisual = True

    if(hasattr(self.obj975, '_setHierarchicalLink')):
      self.obj975._setHierarchicalLink(False)

    # classtype
    self.obj975.classtype.setValue('Par')

    # cardinality
    self.obj975.cardinality.setValue('1')

    # name
    self.obj975.name.setValue('par1')

    self.obj975.graphClass_= graph_Par
    if self.genGraphics:
       new_obj = graph_Par(840.0,180.0,self.obj975)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Par", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj975.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj975)
    self.globalAndLocalPostcondition(self.obj975, rootNode)
    self.obj975.postAction( rootNode.CREATE )

    self.obj976=Inst(self)
    self.obj976.isGraphObjectVisual = True

    if(hasattr(self.obj976, '_setHierarchicalLink')):
      self.obj976._setHierarchicalLink(False)

    # classtype
    self.obj976.classtype.setValue('Inst')

    # cardinality
    self.obj976.cardinality.setValue('1')

    # name
    self.obj976.name.setValue('inst1')

    self.obj976.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(1040.0,180.0,self.obj976)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj976.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj976)
    self.globalAndLocalPostcondition(self.obj976, rootNode)
    self.obj976.postAction( rootNode.CREATE )

    self.obj977=Inst(self)
    self.obj977.isGraphObjectVisual = True

    if(hasattr(self.obj977, '_setHierarchicalLink')):
      self.obj977._setHierarchicalLink(False)

    # classtype
    self.obj977.classtype.setValue('Inst')

    # cardinality
    self.obj977.cardinality.setValue('1')

    # name
    self.obj977.name.setValue('inst2')

    self.obj977.graphClass_= graph_Inst
    if self.genGraphics:
       new_obj = graph_Inst(1040.0,440.0,self.obj977)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj977.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj977)
    self.globalAndLocalPostcondition(self.obj977, rootNode)
    self.obj977.postAction( rootNode.CREATE )

    self.obj978=LocalDef(self)
    self.obj978.isGraphObjectVisual = True

    if(hasattr(self.obj978, '_setHierarchicalLink')):
      self.obj978._setHierarchicalLink(False)

    # classtype
    self.obj978.classtype.setValue('LocalDef')

    # cardinality
    self.obj978.cardinality.setValue('1')

    # name
    self.obj978.name.setValue('localdef1')

    self.obj978.graphClass_= graph_LocalDef
    if self.genGraphics:
       new_obj = graph_LocalDef(420.0,300.0,self.obj978)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LocalDef", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj978.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj978)
    self.globalAndLocalPostcondition(self.obj978, rootNode)
    self.obj978.postAction( rootNode.CREATE )

    self.obj979=Attribute(self)
    self.obj979.isGraphObjectVisual = True

    if(hasattr(self.obj979, '_setHierarchicalLink')):
      self.obj979._setHierarchicalLink(False)

    # Type
    self.obj979.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj979.Type.config = 0

    # name
    self.obj979.name.setValue('isComposite')

    self.obj979.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,6.0,self.obj979)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj979.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj979)
    self.globalAndLocalPostcondition(self.obj979, rootNode)
    self.obj979.postAction( rootNode.CREATE )

    self.obj980=Attribute(self)
    self.obj980.isGraphObjectVisual = True

    if(hasattr(self.obj980, '_setHierarchicalLink')):
      self.obj980._setHierarchicalLink(False)

    # Type
    self.obj980.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj980.Type.config = 0

    # name
    self.obj980.name.setValue('literal')

    self.obj980.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(20.0,380.0,self.obj980)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj980.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj980)
    self.globalAndLocalPostcondition(self.obj980, rootNode)
    self.obj980.postAction( rootNode.CREATE )

    self.obj981=Attribute(self)
    self.obj981.isGraphObjectVisual = True

    if(hasattr(self.obj981, '_setHierarchicalLink')):
      self.obj981._setHierarchicalLink(False)

    # Type
    self.obj981.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj981.Type.config = 0

    # name
    self.obj981.name.setValue('literal')

    self.obj981.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(260.0,580.0,self.obj981)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj981.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj981)
    self.globalAndLocalPostcondition(self.obj981, rootNode)
    self.obj981.postAction( rootNode.CREATE )

    self.obj982=Attribute(self)
    self.obj982.isGraphObjectVisual = True

    if(hasattr(self.obj982, '_setHierarchicalLink')):
      self.obj982._setHierarchicalLink(False)

    # Type
    self.obj982.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj982.Type.config = 0

    # name
    self.obj982.name.setValue('literal')

    self.obj982.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(440.0,580.0,self.obj982)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj982.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj982)
    self.globalAndLocalPostcondition(self.obj982, rootNode)
    self.obj982.postAction( rootNode.CREATE )

    self.obj983=Attribute(self)
    self.obj983.isGraphObjectVisual = True

    if(hasattr(self.obj983, '_setHierarchicalLink')):
      self.obj983._setHierarchicalLink(False)

    # Type
    self.obj983.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj983.Type.config = 0

    # name
    self.obj983.name.setValue('literal')

    self.obj983.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(640.0,600.0,self.obj983)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj983.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj983)
    self.globalAndLocalPostcondition(self.obj983, rootNode)
    self.obj983.postAction( rootNode.CREATE )

    self.obj984=Attribute(self)
    self.obj984.isGraphObjectVisual = True

    if(hasattr(self.obj984, '_setHierarchicalLink')):
      self.obj984._setHierarchicalLink(False)

    # Type
    self.obj984.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj984.Type.config = 0

    # name
    self.obj984.name.setValue('name')

    self.obj984.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1040.0,280.0,self.obj984)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj984.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj984)
    self.globalAndLocalPostcondition(self.obj984, rootNode)
    self.obj984.postAction( rootNode.CREATE )

    self.obj985=Attribute(self)
    self.obj985.isGraphObjectVisual = True

    if(hasattr(self.obj985, '_setHierarchicalLink')):
      self.obj985._setHierarchicalLink(False)

    # Type
    self.obj985.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj985.Type.config = 0

    # name
    self.obj985.name.setValue('literal')

    self.obj985.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,20.0,self.obj985)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj985.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj985)
    self.globalAndLocalPostcondition(self.obj985, rootNode)
    self.obj985.postAction( rootNode.CREATE )

    self.obj986=Attribute(self)
    self.obj986.isGraphObjectVisual = True

    if(hasattr(self.obj986, '_setHierarchicalLink')):
      self.obj986._setHierarchicalLink(False)

    # Type
    self.obj986.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj986.Type.config = 0

    # name
    self.obj986.name.setValue('literal')

    self.obj986.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,120.0,self.obj986)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj986.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj986)
    self.globalAndLocalPostcondition(self.obj986, rootNode)
    self.obj986.postAction( rootNode.CREATE )

    self.obj987=Attribute(self)
    self.obj987.isGraphObjectVisual = True

    if(hasattr(self.obj987, '_setHierarchicalLink')):
      self.obj987._setHierarchicalLink(False)

    # Type
    self.obj987.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj987.Type.config = 0

    # name
    self.obj987.name.setValue('literal')

    self.obj987.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,220.0,self.obj987)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj987.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj987)
    self.globalAndLocalPostcondition(self.obj987, rootNode)
    self.obj987.postAction( rootNode.CREATE )

    self.obj988=Attribute(self)
    self.obj988.isGraphObjectVisual = True

    if(hasattr(self.obj988, '_setHierarchicalLink')):
      self.obj988._setHierarchicalLink(False)

    # Type
    self.obj988.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj988.Type.config = 0

    # name
    self.obj988.name.setValue('literal')

    self.obj988.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,320.0,self.obj988)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj988.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj988)
    self.globalAndLocalPostcondition(self.obj988, rootNode)
    self.obj988.postAction( rootNode.CREATE )

    self.obj989=Attribute(self)
    self.obj989.isGraphObjectVisual = True

    if(hasattr(self.obj989, '_setHierarchicalLink')):
      self.obj989._setHierarchicalLink(False)

    # Type
    self.obj989.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj989.Type.config = 0

    # name
    self.obj989.name.setValue('name')

    self.obj989.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1040.0,540.0,self.obj989)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj989.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj989)
    self.globalAndLocalPostcondition(self.obj989, rootNode)
    self.obj989.postAction( rootNode.CREATE )

    self.obj990=Attribute(self)
    self.obj990.isGraphObjectVisual = True

    if(hasattr(self.obj990, '_setHierarchicalLink')):
      self.obj990._setHierarchicalLink(False)

    # Type
    self.obj990.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj990.Type.config = 0

    # name
    self.obj990.name.setValue('literal')

    self.obj990.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,440.0,self.obj990)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj990.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj990)
    self.globalAndLocalPostcondition(self.obj990, rootNode)
    self.obj990.postAction( rootNode.CREATE )

    self.obj991=Attribute(self)
    self.obj991.isGraphObjectVisual = True

    if(hasattr(self.obj991, '_setHierarchicalLink')):
      self.obj991._setHierarchicalLink(False)

    # Type
    self.obj991.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj991.Type.config = 0

    # name
    self.obj991.name.setValue('literal')

    self.obj991.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,540.0,self.obj991)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj991.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj991)
    self.globalAndLocalPostcondition(self.obj991, rootNode)
    self.obj991.postAction( rootNode.CREATE )

    self.obj992=Attribute(self)
    self.obj992.isGraphObjectVisual = True

    if(hasattr(self.obj992, '_setHierarchicalLink')):
      self.obj992._setHierarchicalLink(False)

    # Type
    self.obj992.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj992.Type.config = 0

    # name
    self.obj992.name.setValue('literal')

    self.obj992.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(1540.0,660.0,self.obj992)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj992.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj992)
    self.globalAndLocalPostcondition(self.obj992, rootNode)
    self.obj992.postAction( rootNode.CREATE )

    self.obj993=Attribute(self)
    self.obj993.isGraphObjectVisual = True

    if(hasattr(self.obj993, '_setHierarchicalLink')):
      self.obj993._setHierarchicalLink(False)

    # Type
    self.obj993.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj993.Type.config = 0

    # name
    self.obj993.name.setValue('pivotin')

    self.obj993.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(160.0,100.0,self.obj993)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj993.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj993)
    self.globalAndLocalPostcondition(self.obj993, rootNode)
    self.obj993.postAction( rootNode.CREATE )

    self.obj994=Attribute(self)
    self.obj994.isGraphObjectVisual = True

    if(hasattr(self.obj994, '_setHierarchicalLink')):
      self.obj994._setHierarchicalLink(False)

    # Type
    self.obj994.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj994.Type.config = 0

    # name
    self.obj994.name.setValue('pivotout')

    self.obj994.graphClass_= graph_Attribute
    if self.genGraphics:
       new_obj = graph_Attribute(600.0,80.0,self.obj994)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj994.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj994)
    self.globalAndLocalPostcondition(self.obj994, rootNode)
    self.obj994.postAction( rootNode.CREATE )

    self.obj995=Equation(self)
    self.obj995.isGraphObjectVisual = True

    if(hasattr(self.obj995, '_setHierarchicalLink')):
      self.obj995._setHierarchicalLink(False)

    # name
    self.obj995.name.setValue('eq1')

    self.obj995.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(620.0,6.0,self.obj995)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj995.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj995)
    self.globalAndLocalPostcondition(self.obj995, rootNode)
    self.obj995.postAction( rootNode.CREATE )

    self.obj996=Equation(self)
    self.obj996.isGraphObjectVisual = True

    if(hasattr(self.obj996, '_setHierarchicalLink')):
      self.obj996._setHierarchicalLink(False)

    # name
    self.obj996.name.setValue('eq2')

    self.obj996.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(20.0,460.0,self.obj996)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj996.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj996)
    self.globalAndLocalPostcondition(self.obj996, rootNode)
    self.obj996.postAction( rootNode.CREATE )

    self.obj997=Equation(self)
    self.obj997.isGraphObjectVisual = True

    if(hasattr(self.obj997, '_setHierarchicalLink')):
      self.obj997._setHierarchicalLink(False)

    # name
    self.obj997.name.setValue('eq3')

    self.obj997.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(260.0,660.0,self.obj997)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj997.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj997)
    self.globalAndLocalPostcondition(self.obj997, rootNode)
    self.obj997.postAction( rootNode.CREATE )

    self.obj998=Equation(self)
    self.obj998.isGraphObjectVisual = True

    if(hasattr(self.obj998, '_setHierarchicalLink')):
      self.obj998._setHierarchicalLink(False)

    # name
    self.obj998.name.setValue('eq4')

    self.obj998.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(440.0,660.0,self.obj998)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj998.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj998)
    self.globalAndLocalPostcondition(self.obj998, rootNode)
    self.obj998.postAction( rootNode.CREATE )

    self.obj999=Equation(self)
    self.obj999.isGraphObjectVisual = True

    if(hasattr(self.obj999, '_setHierarchicalLink')):
      self.obj999._setHierarchicalLink(False)

    # name
    self.obj999.name.setValue('eq5')

    self.obj999.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(640.0,680.0,self.obj999)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj999.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj999)
    self.globalAndLocalPostcondition(self.obj999, rootNode)
    self.obj999.postAction( rootNode.CREATE )

    self.obj1000=Equation(self)
    self.obj1000.isGraphObjectVisual = True

    if(hasattr(self.obj1000, '_setHierarchicalLink')):
      self.obj1000._setHierarchicalLink(False)

    # name
    self.obj1000.name.setValue('eq6')

    self.obj1000.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1180.0,320.0,self.obj1000)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1000.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1000)
    self.globalAndLocalPostcondition(self.obj1000, rootNode)
    self.obj1000.postAction( rootNode.CREATE )

    self.obj1001=Equation(self)
    self.obj1001.isGraphObjectVisual = True

    if(hasattr(self.obj1001, '_setHierarchicalLink')):
      self.obj1001._setHierarchicalLink(False)

    # name
    self.obj1001.name.setValue('eq7')

    self.obj1001.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,20.0,self.obj1001)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1001.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1001)
    self.globalAndLocalPostcondition(self.obj1001, rootNode)
    self.obj1001.postAction( rootNode.CREATE )

    self.obj1002=Equation(self)
    self.obj1002.isGraphObjectVisual = True

    if(hasattr(self.obj1002, '_setHierarchicalLink')):
      self.obj1002._setHierarchicalLink(False)

    # name
    self.obj1002.name.setValue('eq8')

    self.obj1002.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,120.0,self.obj1002)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1002.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1002)
    self.globalAndLocalPostcondition(self.obj1002, rootNode)
    self.obj1002.postAction( rootNode.CREATE )

    self.obj1003=Equation(self)
    self.obj1003.isGraphObjectVisual = True

    if(hasattr(self.obj1003, '_setHierarchicalLink')):
      self.obj1003._setHierarchicalLink(False)

    # name
    self.obj1003.name.setValue('eq9')

    self.obj1003.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,220.0,self.obj1003)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1003.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1003)
    self.globalAndLocalPostcondition(self.obj1003, rootNode)
    self.obj1003.postAction( rootNode.CREATE )

    self.obj1004=Equation(self)
    self.obj1004.isGraphObjectVisual = True

    if(hasattr(self.obj1004, '_setHierarchicalLink')):
      self.obj1004._setHierarchicalLink(False)

    # name
    self.obj1004.name.setValue('eq10')

    self.obj1004.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,320.0,self.obj1004)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1005.name.setValue('eq11')

    self.obj1005.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1180.0,580.0,self.obj1005)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1006.name.setValue('eq12')

    self.obj1006.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,440.0,self.obj1006)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1007.name.setValue('eq13')

    self.obj1007.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,540.0,self.obj1007)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1008.name.setValue('eq14')

    self.obj1008.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(1700.0,660.0,self.obj1008)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1009.name.setValue('eq15')

    self.obj1009.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(303.0,100.0,self.obj1009)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1010.name.setValue('eq16')

    self.obj1010.graphClass_= graph_Equation
    if self.genGraphics:
       new_obj = graph_Equation(740.0,80.0,self.obj1010)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1010.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1010)
    self.globalAndLocalPostcondition(self.obj1010, rootNode)
    self.obj1010.postAction( rootNode.CREATE )

    self.obj1011=Constant(self)
    self.obj1011.isGraphObjectVisual = True

    if(hasattr(self.obj1011, '_setHierarchicalLink')):
      self.obj1011._setHierarchicalLink(False)

    # Type
    self.obj1011.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 1) )
    self.obj1011.Type.config = 0

    # name
    self.obj1011.name.setValue('true')

    self.obj1011.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(800.0,7.0,self.obj1011)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1011.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1011)
    self.globalAndLocalPostcondition(self.obj1011, rootNode)
    self.obj1011.postAction( rootNode.CREATE )

    self.obj1012=Constant(self)
    self.obj1012.isGraphObjectVisual = True

    if(hasattr(self.obj1012, '_setHierarchicalLink')):
      self.obj1012._setHierarchicalLink(False)

    # Type
    self.obj1012.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1012.Type.config = 0

    # name
    self.obj1012.name.setValue('sh')

    self.obj1012.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(20.0,540.0,self.obj1012)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1012.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1012)
    self.globalAndLocalPostcondition(self.obj1012, rootNode)
    self.obj1012.postAction( rootNode.CREATE )

    self.obj1013=Constant(self)
    self.obj1013.isGraphObjectVisual = True

    if(hasattr(self.obj1013, '_setHierarchicalLink')):
      self.obj1013._setHierarchicalLink(False)

    # Type
    self.obj1013.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1013.Type.config = 0

    # name
    self.obj1013.name.setValue('exit_in')

    self.obj1013.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(260.0,760.0,self.obj1013)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1014.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1014.Type.config = 0

    # name
    self.obj1014.name.setValue('exack_in')

    self.obj1014.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(440.0,760.0,self.obj1014)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1015.name.setValue('sh_in')

    self.obj1015.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(640.0,760.0,self.obj1015)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1016.name.setValue('C')

    self.obj1016.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1040.0,360.0,self.obj1016)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1017.name.setValue('enp')

    self.obj1017.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,20.0,self.obj1017)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1018.name.setValue('exit_in')

    self.obj1018.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,120.0,self.obj1018)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1019.name.setValue('exack_in')

    self.obj1019.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,220.0,self.obj1019)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1020.name.setValue('sh_in')

    self.obj1020.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,320.0,self.obj1020)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj1021.name.setValue('H')

    self.obj1021.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1040.0,620.0,self.obj1021)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1021.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1021)
    self.globalAndLocalPostcondition(self.obj1021, rootNode)
    self.obj1021.postAction( rootNode.CREATE )

    self.obj1022=Constant(self)
    self.obj1022.isGraphObjectVisual = True

    if(hasattr(self.obj1022, '_setHierarchicalLink')):
      self.obj1022._setHierarchicalLink(False)

    # Type
    self.obj1022.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1022.Type.config = 0

    # name
    self.obj1022.name.setValue('exit_in')

    self.obj1022.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,440.0,self.obj1022)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1022.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1022)
    self.globalAndLocalPostcondition(self.obj1022, rootNode)
    self.obj1022.postAction( rootNode.CREATE )

    self.obj1023=Constant(self)
    self.obj1023.isGraphObjectVisual = True

    if(hasattr(self.obj1023, '_setHierarchicalLink')):
      self.obj1023._setHierarchicalLink(False)

    # Type
    self.obj1023.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1023.Type.config = 0

    # name
    self.obj1023.name.setValue('exack_in')

    self.obj1023.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,540.0,self.obj1023)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1023.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1023)
    self.globalAndLocalPostcondition(self.obj1023, rootNode)
    self.obj1023.postAction( rootNode.CREATE )

    self.obj1024=Constant(self)
    self.obj1024.isGraphObjectVisual = True

    if(hasattr(self.obj1024, '_setHierarchicalLink')):
      self.obj1024._setHierarchicalLink(False)

    # Type
    self.obj1024.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1024.Type.config = 0

    # name
    self.obj1024.name.setValue('sh_in')

    self.obj1024.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(1860.0,660.0,self.obj1024)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1024.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1024)
    self.globalAndLocalPostcondition(self.obj1024, rootNode)
    self.obj1024.postAction( rootNode.CREATE )

    self.obj1025=Constant(self)
    self.obj1025.isGraphObjectVisual = True

    if(hasattr(self.obj1025, '_setHierarchicalLink')):
      self.obj1025._setHierarchicalLink(False)

    # Type
    self.obj1025.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1025.Type.config = 0

    # name
    self.obj1025.name.setValue('procdef')

    self.obj1025.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(450.0,80.0,self.obj1025)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1025.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1025)
    self.globalAndLocalPostcondition(self.obj1025, rootNode)
    self.obj1025.postAction( rootNode.CREATE )

    self.obj1026=Constant(self)
    self.obj1026.isGraphObjectVisual = True

    if(hasattr(self.obj1026, '_setHierarchicalLink')):
      self.obj1026._setHierarchicalLink(False)

    # Type
    self.obj1026.Type.setValue( (['String', 'Bool', 'Integer', 'Float'], 0) )
    self.obj1026.Type.config = 0

    # name
    self.obj1026.name.setValue('localdefcompstate')

    self.obj1026.graphClass_= graph_Constant
    if self.genGraphics:
       new_obj = graph_Constant(889.0,80.0,self.obj1026)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.91
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1026.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1026)
    self.globalAndLocalPostcondition(self.obj1026, rootNode)
    self.obj1026.postAction( rootNode.CREATE )

    self.obj1027=paired_with(self)
    self.obj1027.isGraphObjectVisual = True

    if(hasattr(self.obj1027, '_setHierarchicalLink')):
      self.obj1027._setHierarchicalLink(False)

    self.obj1027.graphClass_= graph_paired_with
    if self.genGraphics:
       new_obj = graph_paired_with(140.5,112.0,self.obj1027)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1027.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1027)
    self.globalAndLocalPostcondition(self.obj1027, rootNode)
    self.obj1027.postAction( rootNode.CREATE )

    self.obj1028=match_contains(self)
    self.obj1028.isGraphObjectVisual = True

    if(hasattr(self.obj1028, '_setHierarchicalLink')):
      self.obj1028._setHierarchicalLink(False)

    self.obj1028.graphClass_= graph_match_contains
    if self.genGraphics:
       new_obj = graph_match_contains(264.0,57.0,self.obj1028)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
       new_obj = graph_apply_contains(267.5,202.0,self.obj1029)
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
       new_obj = graph_apply_contains(377.5,202.0,self.obj1030)
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
       new_obj = graph_apply_contains(477.5,202.0,self.obj1031)
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
       new_obj = graph_apply_contains(576.5,202.0,self.obj1032)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1032.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1032)
    self.globalAndLocalPostcondition(self.obj1032, rootNode)
    self.obj1032.postAction( rootNode.CREATE )

    self.obj1033=apply_contains(self)
    self.obj1033.isGraphObjectVisual = True

    if(hasattr(self.obj1033, '_setHierarchicalLink')):
      self.obj1033._setHierarchicalLink(False)

    self.obj1033.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(167.5,252.0,self.obj1033)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1033.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1033)
    self.globalAndLocalPostcondition(self.obj1033, rootNode)
    self.obj1033.postAction( rootNode.CREATE )

    self.obj1034=apply_contains(self)
    self.obj1034.isGraphObjectVisual = True

    if(hasattr(self.obj1034, '_setHierarchicalLink')):
      self.obj1034._setHierarchicalLink(False)

    self.obj1034.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(287.5,262.0,self.obj1034)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1034.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1034)
    self.globalAndLocalPostcondition(self.obj1034, rootNode)
    self.obj1034.postAction( rootNode.CREATE )

    self.obj1035=apply_contains(self)
    self.obj1035.isGraphObjectVisual = True

    if(hasattr(self.obj1035, '_setHierarchicalLink')):
      self.obj1035._setHierarchicalLink(False)

    self.obj1035.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(377.5,262.0,self.obj1035)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1035.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1035)
    self.globalAndLocalPostcondition(self.obj1035, rootNode)
    self.obj1035.postAction( rootNode.CREATE )

    self.obj1036=apply_contains(self)
    self.obj1036.isGraphObjectVisual = True

    if(hasattr(self.obj1036, '_setHierarchicalLink')):
      self.obj1036._setHierarchicalLink(False)

    self.obj1036.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(477.5,262.0,self.obj1036)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1036.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1036)
    self.globalAndLocalPostcondition(self.obj1036, rootNode)
    self.obj1036.postAction( rootNode.CREATE )

    self.obj1037=apply_contains(self)
    self.obj1037.isGraphObjectVisual = True

    if(hasattr(self.obj1037, '_setHierarchicalLink')):
      self.obj1037._setHierarchicalLink(False)

    self.obj1037.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(677.5,202.0,self.obj1037)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1037.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1037)
    self.globalAndLocalPostcondition(self.obj1037, rootNode)
    self.obj1037.postAction( rootNode.CREATE )

    self.obj1038=apply_contains(self)
    self.obj1038.isGraphObjectVisual = True

    if(hasattr(self.obj1038, '_setHierarchicalLink')):
      self.obj1038._setHierarchicalLink(False)

    self.obj1038.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(677.5,332.0,self.obj1038)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1038.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1038)
    self.globalAndLocalPostcondition(self.obj1038, rootNode)
    self.obj1038.postAction( rootNode.CREATE )

    self.obj1039=apply_contains(self)
    self.obj1039.isGraphObjectVisual = True

    if(hasattr(self.obj1039, '_setHierarchicalLink')):
      self.obj1039._setHierarchicalLink(False)

    self.obj1039.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(783.5,215.0,self.obj1039)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1039.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1039)
    self.globalAndLocalPostcondition(self.obj1039, rootNode)
    self.obj1039.postAction( rootNode.CREATE )

    self.obj1040=apply_contains(self)
    self.obj1040.isGraphObjectVisual = True

    if(hasattr(self.obj1040, '_setHierarchicalLink')):
      self.obj1040._setHierarchicalLink(False)

    self.obj1040.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(787.5,214.0,self.obj1040)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1040.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1040)
    self.globalAndLocalPostcondition(self.obj1040, rootNode)
    self.obj1040.postAction( rootNode.CREATE )

    self.obj1041=apply_contains(self)
    self.obj1041.isGraphObjectVisual = True

    if(hasattr(self.obj1041, '_setHierarchicalLink')):
      self.obj1041._setHierarchicalLink(False)

    self.obj1041.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(837.5,222.0,self.obj1041)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1041.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1041)
    self.globalAndLocalPostcondition(self.obj1041, rootNode)
    self.obj1041.postAction( rootNode.CREATE )

    self.obj1042=apply_contains(self)
    self.obj1042.isGraphObjectVisual = True

    if(hasattr(self.obj1042, '_setHierarchicalLink')):
      self.obj1042._setHierarchicalLink(False)

    self.obj1042.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(837.5,272.0,self.obj1042)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1042.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1042)
    self.globalAndLocalPostcondition(self.obj1042, rootNode)
    self.obj1042.postAction( rootNode.CREATE )

    self.obj1043=apply_contains(self)
    self.obj1043.isGraphObjectVisual = True

    if(hasattr(self.obj1043, '_setHierarchicalLink')):
      self.obj1043._setHierarchicalLink(False)

    self.obj1043.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(837.5,332.0,self.obj1043)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1043.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1043)
    self.globalAndLocalPostcondition(self.obj1043, rootNode)
    self.obj1043.postAction( rootNode.CREATE )

    self.obj1044=apply_contains(self)
    self.obj1044.isGraphObjectVisual = True

    if(hasattr(self.obj1044, '_setHierarchicalLink')):
      self.obj1044._setHierarchicalLink(False)

    self.obj1044.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(833.5,407.0,self.obj1044)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1044.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1044)
    self.globalAndLocalPostcondition(self.obj1044, rootNode)
    self.obj1044.postAction( rootNode.CREATE )

    self.obj1045=apply_contains(self)
    self.obj1045.isGraphObjectVisual = True

    if(hasattr(self.obj1045, '_setHierarchicalLink')):
      self.obj1045._setHierarchicalLink(False)

    self.obj1045.graphClass_= graph_apply_contains
    if self.genGraphics:
       new_obj = graph_apply_contains(837.5,442.0,self.obj1045)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1045.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1045)
    self.globalAndLocalPostcondition(self.obj1045, rootNode)
    self.obj1045.postAction( rootNode.CREATE )

    self.obj1046=directLink_T(self)
    self.obj1046.isGraphObjectVisual = True

    if(hasattr(self.obj1046, '_setHierarchicalLink')):
      self.obj1046._setHierarchicalLink(False)

    # associationType
    self.obj1046.associationType.setValue('p')

    self.obj1046.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(415.0,348.0,self.obj1046)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1046.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1046)
    self.globalAndLocalPostcondition(self.obj1046, rootNode)
    self.obj1046.postAction( rootNode.CREATE )

    self.obj1047=directLink_T(self)
    self.obj1047.isGraphObjectVisual = True

    if(hasattr(self.obj1047, '_setHierarchicalLink')):
      self.obj1047._setHierarchicalLink(False)

    # associationType
    self.obj1047.associationType.setValue('p')

    self.obj1047.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(663.0,351.0,self.obj1047)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1047.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1047)
    self.globalAndLocalPostcondition(self.obj1047, rootNode)
    self.obj1047.postAction( rootNode.CREATE )

    self.obj1048=directLink_T(self)
    self.obj1048.isGraphObjectVisual = True

    if(hasattr(self.obj1048, '_setHierarchicalLink')):
      self.obj1048._setHierarchicalLink(False)

    # associationType
    self.obj1048.associationType.setValue('p')

    self.obj1048.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(912.0,231.0,self.obj1048)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1048.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1048)
    self.globalAndLocalPostcondition(self.obj1048, rootNode)
    self.obj1048.postAction( rootNode.CREATE )

    self.obj1049=directLink_T(self)
    self.obj1049.isGraphObjectVisual = True

    if(hasattr(self.obj1049, '_setHierarchicalLink')):
      self.obj1049._setHierarchicalLink(False)

    # associationType
    self.obj1049.associationType.setValue('p')

    self.obj1049.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1122.0,231.0,self.obj1049)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1049.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1049)
    self.globalAndLocalPostcondition(self.obj1049, rootNode)
    self.obj1049.postAction( rootNode.CREATE )

    self.obj1050=directLink_T(self)
    self.obj1050.isGraphObjectVisual = True

    if(hasattr(self.obj1050, '_setHierarchicalLink')):
      self.obj1050._setHierarchicalLink(False)

    # associationType
    self.obj1050.associationType.setValue('channelNames')

    self.obj1050.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(190.0,249.0,self.obj1050)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1050.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1050)
    self.globalAndLocalPostcondition(self.obj1050, rootNode)
    self.obj1050.postAction( rootNode.CREATE )

    self.obj1051=directLink_T(self)
    self.obj1051.isGraphObjectVisual = True

    if(hasattr(self.obj1051, '_setHierarchicalLink')):
      self.obj1051._setHierarchicalLink(False)

    # associationType
    self.obj1051.associationType.setValue('channelNames')

    self.obj1051.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(608.0,368.0,self.obj1051)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1051.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1051)
    self.globalAndLocalPostcondition(self.obj1051, rootNode)
    self.obj1051.postAction( rootNode.CREATE )

    self.obj1052=directLink_T(self)
    self.obj1052.isGraphObjectVisual = True

    if(hasattr(self.obj1052, '_setHierarchicalLink')):
      self.obj1052._setHierarchicalLink(False)

    # associationType
    self.obj1052.associationType.setValue('channelNames')

    self.obj1052.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(694.0,373.0,self.obj1052)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1052.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1052)
    self.globalAndLocalPostcondition(self.obj1052, rootNode)
    self.obj1052.postAction( rootNode.CREATE )

    self.obj1053=directLink_T(self)
    self.obj1053.isGraphObjectVisual = True

    if(hasattr(self.obj1053, '_setHierarchicalLink')):
      self.obj1053._setHierarchicalLink(False)

    # associationType
    self.obj1053.associationType.setValue('channelNames')

    self.obj1053.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(812.0,291.0,self.obj1053)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1053.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1053)
    self.globalAndLocalPostcondition(self.obj1053, rootNode)
    self.obj1053.postAction( rootNode.CREATE )

    self.obj1054=directLink_T(self)
    self.obj1054.isGraphObjectVisual = True

    if(hasattr(self.obj1054, '_setHierarchicalLink')):
      self.obj1054._setHierarchicalLink(False)

    # associationType
    self.obj1054.associationType.setValue('channelNames')

    self.obj1054.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1310.0,102.0,self.obj1054)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1054.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1054)
    self.globalAndLocalPostcondition(self.obj1054, rootNode)
    self.obj1054.postAction( rootNode.CREATE )

    self.obj1055=directLink_T(self)
    self.obj1055.isGraphObjectVisual = True

    if(hasattr(self.obj1055, '_setHierarchicalLink')):
      self.obj1055._setHierarchicalLink(False)

    # associationType
    self.obj1055.associationType.setValue('channelNames')

    self.obj1055.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1314.0,166.0,self.obj1055)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1055.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1055)
    self.globalAndLocalPostcondition(self.obj1055, rootNode)
    self.obj1055.postAction( rootNode.CREATE )

    self.obj1056=directLink_T(self)
    self.obj1056.isGraphObjectVisual = True

    if(hasattr(self.obj1056, '_setHierarchicalLink')):
      self.obj1056._setHierarchicalLink(False)

    # associationType
    self.obj1056.associationType.setValue('channelNames')

    self.obj1056.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1311.0,266.0,self.obj1056)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1056.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1056)
    self.globalAndLocalPostcondition(self.obj1056, rootNode)
    self.obj1056.postAction( rootNode.CREATE )

    self.obj1057=directLink_T(self)
    self.obj1057.isGraphObjectVisual = True

    if(hasattr(self.obj1057, '_setHierarchicalLink')):
      self.obj1057._setHierarchicalLink(False)

    # associationType
    self.obj1057.associationType.setValue('channelNames')

    self.obj1057.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1335.0,330.0,self.obj1057)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1057.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1057)
    self.globalAndLocalPostcondition(self.obj1057, rootNode)
    self.obj1057.postAction( rootNode.CREATE )

    self.obj1058=directLink_T(self)
    self.obj1058.isGraphObjectVisual = True

    if(hasattr(self.obj1058, '_setHierarchicalLink')):
      self.obj1058._setHierarchicalLink(False)

    # associationType
    self.obj1058.associationType.setValue('p')

    self.obj1058.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1016.0,492.0,self.obj1058)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1058.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1058)
    self.globalAndLocalPostcondition(self.obj1058, rootNode)
    self.obj1058.postAction( rootNode.CREATE )

    self.obj1059=directLink_T(self)
    self.obj1059.isGraphObjectVisual = True

    if(hasattr(self.obj1059, '_setHierarchicalLink')):
      self.obj1059._setHierarchicalLink(False)

    # associationType
    self.obj1059.associationType.setValue('channelNames')

    self.obj1059.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1372.0,491.0,self.obj1059)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1059.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1059)
    self.globalAndLocalPostcondition(self.obj1059, rootNode)
    self.obj1059.postAction( rootNode.CREATE )

    self.obj1060=directLink_T(self)
    self.obj1060.isGraphObjectVisual = True

    if(hasattr(self.obj1060, '_setHierarchicalLink')):
      self.obj1060._setHierarchicalLink(False)

    # associationType
    self.obj1060.associationType.setValue('channelNames')

    self.obj1060.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1359.0,527.0,self.obj1060)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1060.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1060)
    self.globalAndLocalPostcondition(self.obj1060, rootNode)
    self.obj1060.postAction( rootNode.CREATE )

    self.obj1061=directLink_T(self)
    self.obj1061.isGraphObjectVisual = True

    if(hasattr(self.obj1061, '_setHierarchicalLink')):
      self.obj1061._setHierarchicalLink(False)

    # associationType
    self.obj1061.associationType.setValue('channelNames')

    self.obj1061.graphClass_= graph_directLink_T
    if self.genGraphics:
       new_obj = graph_directLink_T(1372.0,601.0,self.obj1061)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1061.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1061)
    self.globalAndLocalPostcondition(self.obj1061, rootNode)
    self.obj1061.postAction( rootNode.CREATE )

    self.obj1062=backward_link(self)
    self.obj1062.isGraphObjectVisual = True

    if(hasattr(self.obj1062, '_setHierarchicalLink')):
      self.obj1062._setHierarchicalLink(False)

    # type
    self.obj1062.type.setValue('ruleDef')

    self.obj1062.graphClass_= graph_backward_link
    if self.genGraphics:
       new_obj = graph_backward_link(391.0,147.0,self.obj1062)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1062.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1062)
    self.globalAndLocalPostcondition(self.obj1062, rootNode)
    self.obj1062.postAction( rootNode.CREATE )

    self.obj1063=hasAttribute_S(self)
    self.obj1063.isGraphObjectVisual = True

    if(hasattr(self.obj1063, '_setHierarchicalLink')):
      self.obj1063._setHierarchicalLink(False)

    self.obj1063.graphClass_= graph_hasAttribute_S
    if self.genGraphics:
       new_obj = graph_hasAttribute_S(476.0,40.5,self.obj1063)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1063.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1063)
    self.globalAndLocalPostcondition(self.obj1063, rootNode)
    self.obj1063.postAction( rootNode.CREATE )

    self.obj1064=hasAttribute_T(self)
    self.obj1064.isGraphObjectVisual = True

    if(hasattr(self.obj1064, '_setHierarchicalLink')):
      self.obj1064._setHierarchicalLink(False)

    self.obj1064.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(167.0,377.5,self.obj1064)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1064.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1064)
    self.globalAndLocalPostcondition(self.obj1064, rootNode)
    self.obj1064.postAction( rootNode.CREATE )

    self.obj1065=hasAttribute_T(self)
    self.obj1065.isGraphObjectVisual = True

    if(hasattr(self.obj1065, '_setHierarchicalLink')):
      self.obj1065._setHierarchicalLink(False)

    self.obj1065.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(413.0,559.5,self.obj1065)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1065.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1065)
    self.globalAndLocalPostcondition(self.obj1065, rootNode)
    self.obj1065.postAction( rootNode.CREATE )

    self.obj1066=hasAttribute_T(self)
    self.obj1066.isGraphObjectVisual = True

    if(hasattr(self.obj1066, '_setHierarchicalLink')):
      self.obj1066._setHierarchicalLink(False)

    self.obj1066.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(602.0,588.5,self.obj1066)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1066.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1066)
    self.globalAndLocalPostcondition(self.obj1066, rootNode)
    self.obj1066.postAction( rootNode.CREATE )

    self.obj1067=hasAttribute_T(self)
    self.obj1067.isGraphObjectVisual = True

    if(hasattr(self.obj1067, '_setHierarchicalLink')):
      self.obj1067._setHierarchicalLink(False)

    self.obj1067.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(796.0,606.5,self.obj1067)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1067.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1067)
    self.globalAndLocalPostcondition(self.obj1067, rootNode)
    self.obj1067.postAction( rootNode.CREATE )

    self.obj1068=hasAttribute_T(self)
    self.obj1068.isGraphObjectVisual = True

    if(hasattr(self.obj1068, '_setHierarchicalLink')):
      self.obj1068._setHierarchicalLink(False)

    self.obj1068.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1193.0,272.5,self.obj1068)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1068.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1068)
    self.globalAndLocalPostcondition(self.obj1068, rootNode)
    self.obj1068.postAction( rootNode.CREATE )

    self.obj1069=hasAttribute_T(self)
    self.obj1069.isGraphObjectVisual = True

    if(hasattr(self.obj1069, '_setHierarchicalLink')):
      self.obj1069._setHierarchicalLink(False)

    self.obj1069.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,62.5,self.obj1069)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1069.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1069)
    self.globalAndLocalPostcondition(self.obj1069, rootNode)
    self.obj1069.postAction( rootNode.CREATE )

    self.obj1070=hasAttribute_T(self)
    self.obj1070.isGraphObjectVisual = True

    if(hasattr(self.obj1070, '_setHierarchicalLink')):
      self.obj1070._setHierarchicalLink(False)

    self.obj1070.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,162.5,self.obj1070)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1070.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1070)
    self.globalAndLocalPostcondition(self.obj1070, rootNode)
    self.obj1070.postAction( rootNode.CREATE )

    self.obj1071=hasAttribute_T(self)
    self.obj1071.isGraphObjectVisual = True

    if(hasattr(self.obj1071, '_setHierarchicalLink')):
      self.obj1071._setHierarchicalLink(False)

    self.obj1071.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,262.5,self.obj1071)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1071.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1071)
    self.globalAndLocalPostcondition(self.obj1071, rootNode)
    self.obj1071.postAction( rootNode.CREATE )

    self.obj1072=hasAttribute_T(self)
    self.obj1072.isGraphObjectVisual = True

    if(hasattr(self.obj1072, '_setHierarchicalLink')):
      self.obj1072._setHierarchicalLink(False)

    self.obj1072.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,362.5,self.obj1072)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1072.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1072)
    self.globalAndLocalPostcondition(self.obj1072, rootNode)
    self.obj1072.postAction( rootNode.CREATE )

    self.obj1073=hasAttribute_T(self)
    self.obj1073.isGraphObjectVisual = True

    if(hasattr(self.obj1073, '_setHierarchicalLink')):
      self.obj1073._setHierarchicalLink(False)

    self.obj1073.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1193.0,532.5,self.obj1073)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1073.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1073)
    self.globalAndLocalPostcondition(self.obj1073, rootNode)
    self.obj1073.postAction( rootNode.CREATE )

    self.obj1074=hasAttribute_T(self)
    self.obj1074.isGraphObjectVisual = True

    if(hasattr(self.obj1074, '_setHierarchicalLink')):
      self.obj1074._setHierarchicalLink(False)

    self.obj1074.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,482.5,self.obj1074)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1074.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1074)
    self.globalAndLocalPostcondition(self.obj1074, rootNode)
    self.obj1074.postAction( rootNode.CREATE )

    self.obj1075=hasAttribute_T(self)
    self.obj1075.isGraphObjectVisual = True

    if(hasattr(self.obj1075, '_setHierarchicalLink')):
      self.obj1075._setHierarchicalLink(False)

    self.obj1075.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,582.5,self.obj1075)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1075.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1075)
    self.globalAndLocalPostcondition(self.obj1075, rootNode)
    self.obj1075.postAction( rootNode.CREATE )

    self.obj1076=hasAttribute_T(self)
    self.obj1076.isGraphObjectVisual = True

    if(hasattr(self.obj1076, '_setHierarchicalLink')):
      self.obj1076._setHierarchicalLink(False)

    self.obj1076.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(1603.0,702.5,self.obj1076)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1076.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1076)
    self.globalAndLocalPostcondition(self.obj1076, rootNode)
    self.obj1076.postAction( rootNode.CREATE )

    self.obj1077=hasAttribute_T(self)
    self.obj1077.isGraphObjectVisual = True

    if(hasattr(self.obj1077, '_setHierarchicalLink')):
      self.obj1077._setHierarchicalLink(False)

    self.obj1077.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(373.0,182.5,self.obj1077)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1077.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1077)
    self.globalAndLocalPostcondition(self.obj1077, rootNode)
    self.obj1077.postAction( rootNode.CREATE )

    self.obj1078=hasAttribute_T(self)
    self.obj1078.isGraphObjectVisual = True

    if(hasattr(self.obj1078, '_setHierarchicalLink')):
      self.obj1078._setHierarchicalLink(False)

    self.obj1078.graphClass_= graph_hasAttribute_T
    if self.genGraphics:
       new_obj = graph_hasAttribute_T(663.0,232.5,self.obj1078)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasAttribute_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1078.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1078)
    self.globalAndLocalPostcondition(self.obj1078, rootNode)
    self.obj1078.postAction( rootNode.CREATE )

    self.obj1079=leftExpr(self)
    self.obj1079.isGraphObjectVisual = True

    if(hasattr(self.obj1079, '_setHierarchicalLink')):
      self.obj1079._setHierarchicalLink(False)

    self.obj1079.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(646.0,45.5,self.obj1079)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1079.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1079)
    self.globalAndLocalPostcondition(self.obj1079, rootNode)
    self.obj1079.postAction( rootNode.CREATE )

    self.obj1080=leftExpr(self)
    self.obj1080.isGraphObjectVisual = True

    if(hasattr(self.obj1080, '_setHierarchicalLink')):
      self.obj1080._setHierarchicalLink(False)

    self.obj1080.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(153.0,457.0,self.obj1080)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1080.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1080)
    self.globalAndLocalPostcondition(self.obj1080, rootNode)
    self.obj1080.postAction( rootNode.CREATE )

    self.obj1081=leftExpr(self)
    self.obj1081.isGraphObjectVisual = True

    if(hasattr(self.obj1081, '_setHierarchicalLink')):
      self.obj1081._setHierarchicalLink(False)

    self.obj1081.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(408.0,647.5,self.obj1081)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1081.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1081)
    self.globalAndLocalPostcondition(self.obj1081, rootNode)
    self.obj1081.postAction( rootNode.CREATE )

    self.obj1082=leftExpr(self)
    self.obj1082.isGraphObjectVisual = True

    if(hasattr(self.obj1082, '_setHierarchicalLink')):
      self.obj1082._setHierarchicalLink(False)

    self.obj1082.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(585.0,660.5,self.obj1082)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1082.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1082)
    self.globalAndLocalPostcondition(self.obj1082, rootNode)
    self.obj1082.postAction( rootNode.CREATE )

    self.obj1083=leftExpr(self)
    self.obj1083.isGraphObjectVisual = True

    if(hasattr(self.obj1083, '_setHierarchicalLink')):
      self.obj1083._setHierarchicalLink(False)

    self.obj1083.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(782.0,665.5,self.obj1083)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1083.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1083)
    self.globalAndLocalPostcondition(self.obj1083, rootNode)
    self.obj1083.postAction( rootNode.CREATE )

    self.obj1084=leftExpr(self)
    self.obj1084.isGraphObjectVisual = True

    if(hasattr(self.obj1084, '_setHierarchicalLink')):
      self.obj1084._setHierarchicalLink(False)

    self.obj1084.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1246.0,336.5,self.obj1084)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1084.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1084)
    self.globalAndLocalPostcondition(self.obj1084, rootNode)
    self.obj1084.postAction( rootNode.CREATE )

    self.obj1085=leftExpr(self)
    self.obj1085.isGraphObjectVisual = True

    if(hasattr(self.obj1085, '_setHierarchicalLink')):
      self.obj1085._setHierarchicalLink(False)

    self.obj1085.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,56.5,self.obj1085)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1085.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1085)
    self.globalAndLocalPostcondition(self.obj1085, rootNode)
    self.obj1085.postAction( rootNode.CREATE )

    self.obj1086=leftExpr(self)
    self.obj1086.isGraphObjectVisual = True

    if(hasattr(self.obj1086, '_setHierarchicalLink')):
      self.obj1086._setHierarchicalLink(False)

    self.obj1086.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,156.5,self.obj1086)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1086.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1086)
    self.globalAndLocalPostcondition(self.obj1086, rootNode)
    self.obj1086.postAction( rootNode.CREATE )

    self.obj1087=leftExpr(self)
    self.obj1087.isGraphObjectVisual = True

    if(hasattr(self.obj1087, '_setHierarchicalLink')):
      self.obj1087._setHierarchicalLink(False)

    self.obj1087.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,256.5,self.obj1087)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1087.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1087)
    self.globalAndLocalPostcondition(self.obj1087, rootNode)
    self.obj1087.postAction( rootNode.CREATE )

    self.obj1088=leftExpr(self)
    self.obj1088.isGraphObjectVisual = True

    if(hasattr(self.obj1088, '_setHierarchicalLink')):
      self.obj1088._setHierarchicalLink(False)

    self.obj1088.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,356.5,self.obj1088)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1088.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1088)
    self.globalAndLocalPostcondition(self.obj1088, rootNode)
    self.obj1088.postAction( rootNode.CREATE )

    self.obj1089=leftExpr(self)
    self.obj1089.isGraphObjectVisual = True

    if(hasattr(self.obj1089, '_setHierarchicalLink')):
      self.obj1089._setHierarchicalLink(False)

    self.obj1089.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1246.0,596.5,self.obj1089)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1089.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1089)
    self.globalAndLocalPostcondition(self.obj1089, rootNode)
    self.obj1089.postAction( rootNode.CREATE )

    self.obj1090=leftExpr(self)
    self.obj1090.isGraphObjectVisual = True

    if(hasattr(self.obj1090, '_setHierarchicalLink')):
      self.obj1090._setHierarchicalLink(False)

    self.obj1090.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,476.5,self.obj1090)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1090.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1090)
    self.globalAndLocalPostcondition(self.obj1090, rootNode)
    self.obj1090.postAction( rootNode.CREATE )

    self.obj1091=leftExpr(self)
    self.obj1091.isGraphObjectVisual = True

    if(hasattr(self.obj1091, '_setHierarchicalLink')):
      self.obj1091._setHierarchicalLink(False)

    self.obj1091.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,576.5,self.obj1091)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1091.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1091)
    self.globalAndLocalPostcondition(self.obj1091, rootNode)
    self.obj1091.postAction( rootNode.CREATE )

    self.obj1092=leftExpr(self)
    self.obj1092.isGraphObjectVisual = True

    if(hasattr(self.obj1092, '_setHierarchicalLink')):
      self.obj1092._setHierarchicalLink(False)

    self.obj1092.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(1756.0,696.5,self.obj1092)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1092.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1092)
    self.globalAndLocalPostcondition(self.obj1092, rootNode)
    self.obj1092.postAction( rootNode.CREATE )

    self.obj1093=leftExpr(self)
    self.obj1093.isGraphObjectVisual = True

    if(hasattr(self.obj1093, '_setHierarchicalLink')):
      self.obj1093._setHierarchicalLink(False)

    self.obj1093.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(446.0,126.5,self.obj1093)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1093.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1093)
    self.globalAndLocalPostcondition(self.obj1093, rootNode)
    self.obj1093.postAction( rootNode.CREATE )

    self.obj1094=leftExpr(self)
    self.obj1094.isGraphObjectVisual = True

    if(hasattr(self.obj1094, '_setHierarchicalLink')):
      self.obj1094._setHierarchicalLink(False)

    self.obj1094.graphClass_= graph_leftExpr
    if self.genGraphics:
       new_obj = graph_leftExpr(806.0,116.5,self.obj1094)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1094.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1094)
    self.globalAndLocalPostcondition(self.obj1094, rootNode)
    self.obj1094.postAction( rootNode.CREATE )

    self.obj1095=rightExpr(self)
    self.obj1095.isGraphObjectVisual = True

    if(hasattr(self.obj1095, '_setHierarchicalLink')):
      self.obj1095._setHierarchicalLink(False)

    self.obj1095.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(809.0,43.5,self.obj1095)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1095.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1095)
    self.globalAndLocalPostcondition(self.obj1095, rootNode)
    self.obj1095.postAction( rootNode.CREATE )

    self.obj1096=rightExpr(self)
    self.obj1096.isGraphObjectVisual = True

    if(hasattr(self.obj1096, '_setHierarchicalLink')):
      self.obj1096._setHierarchicalLink(False)

    self.obj1096.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(154.0,532.0,self.obj1096)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1096.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1096)
    self.globalAndLocalPostcondition(self.obj1096, rootNode)
    self.obj1096.postAction( rootNode.CREATE )

    self.obj1097=rightExpr(self)
    self.obj1097.isGraphObjectVisual = True

    if(hasattr(self.obj1097, '_setHierarchicalLink')):
      self.obj1097._setHierarchicalLink(False)

    self.obj1097.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(401.0,748.5,self.obj1097)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1097.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1097)
    self.globalAndLocalPostcondition(self.obj1097, rootNode)
    self.obj1097.postAction( rootNode.CREATE )

    self.obj1098=rightExpr(self)
    self.obj1098.isGraphObjectVisual = True

    if(hasattr(self.obj1098, '_setHierarchicalLink')):
      self.obj1098._setHierarchicalLink(False)

    self.obj1098.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(584.0,736.5,self.obj1098)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1098.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1098)
    self.globalAndLocalPostcondition(self.obj1098, rootNode)
    self.obj1098.postAction( rootNode.CREATE )

    self.obj1099=rightExpr(self)
    self.obj1099.isGraphObjectVisual = True

    if(hasattr(self.obj1099, '_setHierarchicalLink')):
      self.obj1099._setHierarchicalLink(False)

    self.obj1099.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(788.0,763.5,self.obj1099)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1099.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1099)
    self.globalAndLocalPostcondition(self.obj1099, rootNode)
    self.obj1099.postAction( rootNode.CREATE )

    self.obj1100=rightExpr(self)
    self.obj1100.isGraphObjectVisual = True

    if(hasattr(self.obj1100, '_setHierarchicalLink')):
      self.obj1100._setHierarchicalLink(False)

    self.obj1100.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1246.0,376.5,self.obj1100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1100)
    self.globalAndLocalPostcondition(self.obj1100, rootNode)
    self.obj1100.postAction( rootNode.CREATE )

    self.obj1101=rightExpr(self)
    self.obj1101.isGraphObjectVisual = True

    if(hasattr(self.obj1101, '_setHierarchicalLink')):
      self.obj1101._setHierarchicalLink(False)

    self.obj1101.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,56.5,self.obj1101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1101)
    self.globalAndLocalPostcondition(self.obj1101, rootNode)
    self.obj1101.postAction( rootNode.CREATE )

    self.obj1102=rightExpr(self)
    self.obj1102.isGraphObjectVisual = True

    if(hasattr(self.obj1102, '_setHierarchicalLink')):
      self.obj1102._setHierarchicalLink(False)

    self.obj1102.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,156.5,self.obj1102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1102)
    self.globalAndLocalPostcondition(self.obj1102, rootNode)
    self.obj1102.postAction( rootNode.CREATE )

    self.obj1103=rightExpr(self)
    self.obj1103.isGraphObjectVisual = True

    if(hasattr(self.obj1103, '_setHierarchicalLink')):
      self.obj1103._setHierarchicalLink(False)

    self.obj1103.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,256.5,self.obj1103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1103)
    self.globalAndLocalPostcondition(self.obj1103, rootNode)
    self.obj1103.postAction( rootNode.CREATE )

    self.obj1104=rightExpr(self)
    self.obj1104.isGraphObjectVisual = True

    if(hasattr(self.obj1104, '_setHierarchicalLink')):
      self.obj1104._setHierarchicalLink(False)

    self.obj1104.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,356.5,self.obj1104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1104)
    self.globalAndLocalPostcondition(self.obj1104, rootNode)
    self.obj1104.postAction( rootNode.CREATE )

    self.obj1105=rightExpr(self)
    self.obj1105.isGraphObjectVisual = True

    if(hasattr(self.obj1105, '_setHierarchicalLink')):
      self.obj1105._setHierarchicalLink(False)

    self.obj1105.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1246.0,636.5,self.obj1105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1105)
    self.globalAndLocalPostcondition(self.obj1105, rootNode)
    self.obj1105.postAction( rootNode.CREATE )

    self.obj1106=rightExpr(self)
    self.obj1106.isGraphObjectVisual = True

    if(hasattr(self.obj1106, '_setHierarchicalLink')):
      self.obj1106._setHierarchicalLink(False)

    self.obj1106.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,476.5,self.obj1106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1106)
    self.globalAndLocalPostcondition(self.obj1106, rootNode)
    self.obj1106.postAction( rootNode.CREATE )

    self.obj1107=rightExpr(self)
    self.obj1107.isGraphObjectVisual = True

    if(hasattr(self.obj1107, '_setHierarchicalLink')):
      self.obj1107._setHierarchicalLink(False)

    self.obj1107.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,576.5,self.obj1107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1107)
    self.globalAndLocalPostcondition(self.obj1107, rootNode)
    self.obj1107.postAction( rootNode.CREATE )

    self.obj1108=rightExpr(self)
    self.obj1108.isGraphObjectVisual = True

    if(hasattr(self.obj1108, '_setHierarchicalLink')):
      self.obj1108._setHierarchicalLink(False)

    self.obj1108.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(1916.0,696.5,self.obj1108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1108)
    self.globalAndLocalPostcondition(self.obj1108, rootNode)
    self.obj1108.postAction( rootNode.CREATE )

    self.obj1109=rightExpr(self)
    self.obj1109.isGraphObjectVisual = True

    if(hasattr(self.obj1109, '_setHierarchicalLink')):
      self.obj1109._setHierarchicalLink(False)

    self.obj1109.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(538.0,116.5,self.obj1109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1109)
    self.globalAndLocalPostcondition(self.obj1109, rootNode)
    self.obj1109.postAction( rootNode.CREATE )

    self.obj1110=rightExpr(self)
    self.obj1110.isGraphObjectVisual = True

    if(hasattr(self.obj1110, '_setHierarchicalLink')):
      self.obj1110._setHierarchicalLink(False)

    self.obj1110.graphClass_= graph_rightExpr
    if self.genGraphics:
       new_obj = graph_rightExpr(950.5,116.5,self.obj1110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1110)
    self.globalAndLocalPostcondition(self.obj1110, rootNode)
    self.obj1110.postAction( rootNode.CREATE )

    # Connections for obj959 (graphObject_: Obj300) of type MatchModel
    self.drawConnections(
(self.obj959,self.obj1027,[138.0, 51.0, 140.5, 112.0],"true", 2),
(self.obj959,self.obj1028,[138.0, 51.0, 264.0, 57.0],"true", 2) )
    # Connections for obj960 (graphObject_: Obj301) of type ApplyModel
    self.drawConnections(
(self.obj960,self.obj1029,[143.0, 173.0, 267.5, 202.0],"true", 2),
(self.obj960,self.obj1030,[143.0, 173.0, 377.5, 202.0],"true", 2),
(self.obj960,self.obj1031,[143.0, 173.0, 477.5, 202.0],"true", 2),
(self.obj960,self.obj1032,[143.0, 173.0, 576.5, 202.0],"true", 2),
(self.obj960,self.obj1033,[143.0, 173.0, 167.5, 252.0],"true", 2),
(self.obj960,self.obj1034,[143.0, 173.0, 287.5, 262.0],"true", 2),
(self.obj960,self.obj1035,[143.0, 173.0, 377.5, 262.0],"true", 2),
(self.obj960,self.obj1036,[143.0, 173.0, 477.5, 262.0],"true", 2),
(self.obj960,self.obj1037,[143.0, 173.0, 677.5, 202.0],"true", 2),
(self.obj960,self.obj1038,[143.0, 173.0, 677.5, 332.0],"true", 2),
(self.obj960,self.obj1039,[143.0, 173.0, 783.5, 215.0],"true", 2),
(self.obj960,self.obj1040,[143.0, 173.0, 787.5, 214.0],"true", 2),
(self.obj960,self.obj1041,[143.0, 173.0, 837.5, 222.0],"true", 2),
(self.obj960,self.obj1042,[143.0, 173.0, 837.5, 272.0],"true", 2),
(self.obj960,self.obj1043,[143.0, 173.0, 837.5, 332.0],"true", 2),
(self.obj960,self.obj1044,[143.0, 173.0, 833.5, 407.0],"true", 2),
(self.obj960,self.obj1045,[143.0, 173.0, 837.5, 442.0],"true", 2) )
    # Connections for obj961 (graphObject_: Obj302) named state1
    self.drawConnections(
(self.obj961,self.obj1063,[390.0, 51.0, 476.0, 40.5],"true", 2) )
    # Connections for obj962 (graphObject_: Obj303) named procdef1
    self.drawConnections(
(self.obj962,self.obj1046,[392.0, 231.0, 415.0, 348.0],"true", 2),
(self.obj962,self.obj1050,[392.0, 231.0, 190.0, 249.0],"true", 2),
(self.obj962,self.obj1062,[392.0, 231.0, 391.0, 147.0],"true", 2),
(self.obj962,self.obj1077,[392.0, 231.0, 373.0, 182.5],"true", 2) )
    # Connections for obj963 (graphObject_: Obj304) named name1
    self.drawConnections(
(self.obj963,self.obj1064,[192.0, 331.0, 167.0, 377.5],"true", 2) )
    # Connections for obj964 (graphObject_: Obj305) named name2
    self.drawConnections(
(self.obj964,self.obj1065,[392.0, 511.0, 413.0, 559.5],"true", 2) )
    # Connections for obj965 (graphObject_: Obj306) named name3
    self.drawConnections(
(self.obj965,self.obj1066,[612.0, 511.0, 602.0, 588.5],"true", 2) )
    # Connections for obj966 (graphObject_: Obj307) named name4
    self.drawConnections(
(self.obj966,self.obj1067,[812.0, 511.0, 796.0, 606.5],"true", 2) )
    # Connections for obj967 (graphObject_: Obj308) named name5
    self.drawConnections(
(self.obj967,self.obj1069,[1532.0, 71.0, 1603.0, 62.5],"true", 2) )
    # Connections for obj968 (graphObject_: Obj309) named name6
    self.drawConnections(
(self.obj968,self.obj1070,[1532.0, 171.0, 1603.0, 162.5],"true", 2) )
    # Connections for obj969 (graphObject_: Obj310) named name7
    self.drawConnections(
(self.obj969,self.obj1071,[1532.0, 271.0, 1603.0, 262.5],"true", 2) )
    # Connections for obj970 (graphObject_: Obj311) named name8
    self.drawConnections(
(self.obj970,self.obj1072,[1532.0, 371.0, 1603.0, 362.5],"true", 2) )
    # Connections for obj971 (graphObject_: Obj312) named name9
    self.drawConnections(
(self.obj971,self.obj1074,[1532.0, 491.0, 1603.0, 482.5],"true", 2) )
    # Connections for obj972 (graphObject_: Obj313) named name10
    self.drawConnections(
(self.obj972,self.obj1075,[1532.0, 591.0, 1603.0, 582.5],"true", 2) )
    # Connections for obj973 (graphObject_: Obj314) named name11
    self.drawConnections(
(self.obj973,self.obj1076,[1532.0, 711.0, 1603.0, 702.5],"true", 2) )
    # Connections for obj974 (graphObject_: Obj315) named new1
    self.drawConnections(
(self.obj974,self.obj1048,[832.0, 351.0, 912.0, 231.0],"true", 2),
(self.obj974,self.obj1051,[832.0, 351.0, 608.0, 368.0],"true", 2),
(self.obj974,self.obj1052,[832.0, 351.0, 694.0, 373.0],"true", 2),
(self.obj974,self.obj1053,[832.0, 351.0, 812.0, 291.0],"true", 2) )
    # Connections for obj975 (graphObject_: Obj316) named par1
    self.drawConnections(
(self.obj975,self.obj1049,[1012.0, 231.0, 1122.0, 231.0],"true", 2),
(self.obj975,self.obj1058,[1012.0, 231.0, 1016.0, 492.0],"true", 2) )
    # Connections for obj976 (graphObject_: Obj317) named inst1
    self.drawConnections(
(self.obj976,self.obj1068,[1212.0, 231.0, 1193.0, 272.5],"true", 2),
(self.obj976,self.obj1054,[1212.0, 231.0, 1310.0, 102.0],"true", 2),
(self.obj976,self.obj1055,[1212.0, 231.0, 1314.0, 166.0],"true", 2),
(self.obj976,self.obj1056,[1212.0, 231.0, 1311.0, 266.0],"true", 2),
(self.obj976,self.obj1057,[1212.0, 231.0, 1335.0, 330.0],"true", 2) )
    # Connections for obj977 (graphObject_: Obj318) named inst2
    self.drawConnections(
(self.obj977,self.obj1073,[1212.0, 491.0, 1193.0, 532.5],"true", 2),
(self.obj977,self.obj1059,[1212.0, 491.0, 1372.0, 491.0],"true", 2),
(self.obj977,self.obj1060,[1212.0, 491.0, 1359.0, 527.0],"true", 2),
(self.obj977,self.obj1061,[1212.0, 491.0, 1372.0, 601.0],"true", 2) )
    # Connections for obj978 (graphObject_: Obj319) named localdef1
    self.drawConnections(
(self.obj978,self.obj1047,[592.0, 351.0, 663.0, 351.0],"true", 2),
(self.obj978,self.obj1078,[592.0, 351.0, 663.0, 232.5],"true", 2) )
    # Connections for obj979 (graphObject_: Obj320) named isComposite
    self.drawConnections(
 )
    # Connections for obj980 (graphObject_: Obj321) named literal
    self.drawConnections(
 )
    # Connections for obj981 (graphObject_: Obj322) named literal
    self.drawConnections(
 )
    # Connections for obj982 (graphObject_: Obj323) named literal
    self.drawConnections(
 )
    # Connections for obj983 (graphObject_: Obj324) named literal
    self.drawConnections(
 )
    # Connections for obj984 (graphObject_: Obj325) named name
    self.drawConnections(
 )
    # Connections for obj985 (graphObject_: Obj326) named literal
    self.drawConnections(
 )
    # Connections for obj986 (graphObject_: Obj327) named literal
    self.drawConnections(
 )
    # Connections for obj987 (graphObject_: Obj328) named literal
    self.drawConnections(
 )
    # Connections for obj988 (graphObject_: Obj329) named literal
    self.drawConnections(
 )
    # Connections for obj989 (graphObject_: Obj330) named name
    self.drawConnections(
 )
    # Connections for obj990 (graphObject_: Obj331) named literal
    self.drawConnections(
 )
    # Connections for obj991 (graphObject_: Obj332) named literal
    self.drawConnections(
 )
    # Connections for obj992 (graphObject_: Obj333) named literal
    self.drawConnections(
 )
    # Connections for obj993 (graphObject_: Obj334) named pivotin
    self.drawConnections(
 )
    # Connections for obj994 (graphObject_: Obj335) named pivotout
    self.drawConnections(
 )
    # Connections for obj995 (graphObject_: Obj336) named eq1
    self.drawConnections(
(self.obj995,self.obj1079,[758.0, 45.0, 646.0, 45.5],"true", 2),
(self.obj995,self.obj1095,[758.0, 45.0, 809.0, 43.5],"true", 2) )
    # Connections for obj996 (graphObject_: Obj337) named eq2
    self.drawConnections(
(self.obj996,self.obj1080,[158.0, 499.0, 153.0, 457.0],"true", 2),
(self.obj996,self.obj1096,[158.0, 499.0, 154.0, 532.0],"true", 2) )
    # Connections for obj997 (graphObject_: Obj338) named eq3
    self.drawConnections(
(self.obj997,self.obj1081,[398.0, 699.0, 408.0, 647.5],"true", 2),
(self.obj997,self.obj1097,[398.0, 699.0, 401.0, 748.5],"true", 2) )
    # Connections for obj998 (graphObject_: Obj339) named eq4
    self.drawConnections(
(self.obj998,self.obj1082,[578.0, 699.0, 585.0, 660.5],"true", 2),
(self.obj998,self.obj1098,[578.0, 699.0, 584.0, 736.5],"true", 2) )
    # Connections for obj999 (graphObject_: Obj340) named eq5
    self.drawConnections(
(self.obj999,self.obj1083,[778.0, 719.0, 782.0, 665.5],"true", 2),
(self.obj999,self.obj1099,[778.0, 719.0, 788.0, 763.5],"true", 2) )
    # Connections for obj1000 (graphObject_: Obj341) named eq6
    self.drawConnections(
(self.obj1000,self.obj1084,[1318.0, 359.0, 1246.0, 336.5],"true", 2),
(self.obj1000,self.obj1100,[1318.0, 359.0, 1246.0, 376.5],"true", 2) )
    # Connections for obj1001 (graphObject_: Obj342) named eq7
    self.drawConnections(
(self.obj1001,self.obj1085,[1838.0, 59.0, 1756.0, 56.5],"true", 2),
(self.obj1001,self.obj1101,[1838.0, 59.0, 1916.0, 56.5],"true", 2) )
    # Connections for obj1002 (graphObject_: Obj343) named eq8
    self.drawConnections(
(self.obj1002,self.obj1086,[1838.0, 159.0, 1756.0, 156.5],"true", 2),
(self.obj1002,self.obj1102,[1838.0, 159.0, 1916.0, 156.5],"true", 2) )
    # Connections for obj1003 (graphObject_: Obj344) named eq9
    self.drawConnections(
(self.obj1003,self.obj1103,[1838.0, 259.0, 1916.0, 256.5],"true", 2),
(self.obj1003,self.obj1087,[1838.0, 259.0, 1756.0, 256.5],"true", 2) )
    # Connections for obj1004 (graphObject_: Obj345) named eq10
    self.drawConnections(
(self.obj1004,self.obj1104,[1838.0, 359.0, 1916.0, 356.5],"true", 2),
(self.obj1004,self.obj1088,[1838.0, 359.0, 1756.0, 356.5],"true", 2) )
    # Connections for obj1005 (graphObject_: Obj346) named eq11
    self.drawConnections(
(self.obj1005,self.obj1089,[1318.0, 619.0, 1246.0, 596.5],"true", 2),
(self.obj1005,self.obj1105,[1318.0, 619.0, 1246.0, 636.5],"true", 2) )
    # Connections for obj1006 (graphObject_: Obj347) named eq12
    self.drawConnections(
(self.obj1006,self.obj1090,[1838.0, 479.0, 1756.0, 476.5],"true", 2),
(self.obj1006,self.obj1106,[1838.0, 479.0, 1916.0, 476.5],"true", 2) )
    # Connections for obj1007 (graphObject_: Obj348) named eq13
    self.drawConnections(
(self.obj1007,self.obj1091,[1838.0, 579.0, 1756.0, 576.5],"true", 2),
(self.obj1007,self.obj1107,[1838.0, 579.0, 1916.0, 576.5],"true", 2) )
    # Connections for obj1008 (graphObject_: Obj349) named eq14
    self.drawConnections(
(self.obj1008,self.obj1092,[1838.0, 699.0, 1756.0, 696.5],"true", 2),
(self.obj1008,self.obj1108,[1838.0, 699.0, 1916.0, 696.5],"true", 2) )
    # Connections for obj1009 (graphObject_: Obj350) named eq15
    self.drawConnections(
(self.obj1009,self.obj1109,[441.0, 139.0, 538.0, 116.5],"true", 2),
(self.obj1009,self.obj1093,[441.0, 139.0, 446.0, 126.5],"true", 2) )
    # Connections for obj1010 (graphObject_: Obj351) named eq16
    self.drawConnections(
(self.obj1010,self.obj1094,[878.0, 119.0, 806.0, 116.5],"true", 2),
(self.obj1010,self.obj1110,[878.0, 119.0, 950.5, 116.5],"true", 2) )
    # Connections for obj1011 (graphObject_: Obj352) named true
    self.drawConnections(
 )
    # Connections for obj1012 (graphObject_: Obj353) named sh
    self.drawConnections(
 )
    # Connections for obj1013 (graphObject_: Obj354) named exit_in
    self.drawConnections(
 )
    # Connections for obj1014 (graphObject_: Obj355) named exack_in
    self.drawConnections(
 )
    # Connections for obj1015 (graphObject_: Obj356) named sh_in
    self.drawConnections(
 )
    # Connections for obj1016 (graphObject_: Obj357) named C
    self.drawConnections(
 )
    # Connections for obj1017 (graphObject_: Obj358) named enp
    self.drawConnections(
 )
    # Connections for obj1018 (graphObject_: Obj359) named exit_in
    self.drawConnections(
 )
    # Connections for obj1019 (graphObject_: Obj360) named exack_in
    self.drawConnections(
 )
    # Connections for obj1020 (graphObject_: Obj361) named sh_in
    self.drawConnections(
 )
    # Connections for obj1021 (graphObject_: Obj362) named H
    self.drawConnections(
 )
    # Connections for obj1022 (graphObject_: Obj363) named exit_in
    self.drawConnections(
 )
    # Connections for obj1023 (graphObject_: Obj364) named exack_in
    self.drawConnections(
 )
    # Connections for obj1024 (graphObject_: Obj365) named sh_in
    self.drawConnections(
 )
    # Connections for obj1025 (graphObject_: Obj366) named procdef
    self.drawConnections(
 )
    # Connections for obj1026 (graphObject_: Obj367) named localdefcompstate
    self.drawConnections(
 )
    # Connections for obj1027 (graphObject_: Obj368) of type paired_with
    self.drawConnections(
(self.obj1027,self.obj960,[140.5, 112.0, 143.0, 173.0],"true", 2) )
    # Connections for obj1028 (graphObject_: Obj369) of type match_contains
    self.drawConnections(
(self.obj1028,self.obj961,[264.0, 57.0, 390.0, 51.0],"true", 2) )
    # Connections for obj1029 (graphObject_: Obj370) of type apply_contains
    self.drawConnections(
(self.obj1029,self.obj962,[267.5, 202.0, 392.0, 231.0],"true", 2) )
    # Connections for obj1030 (graphObject_: Obj371) of type apply_contains
    self.drawConnections(
(self.obj1030,self.obj978,[377.5, 202.0, 592.0, 351.0],"true", 2) )
    # Connections for obj1031 (graphObject_: Obj372) of type apply_contains
    self.drawConnections(
(self.obj1031,self.obj974,[477.5, 202.0, 832.0, 351.0],"true", 2) )
    # Connections for obj1032 (graphObject_: Obj373) of type apply_contains
    self.drawConnections(
(self.obj1032,self.obj975,[576.5, 202.0, 1012.0, 231.0],"true", 2) )
    # Connections for obj1033 (graphObject_: Obj374) of type apply_contains
    self.drawConnections(
(self.obj1033,self.obj963,[167.5, 252.0, 192.0, 331.0],"true", 2) )
    # Connections for obj1034 (graphObject_: Obj375) of type apply_contains
    self.drawConnections(
(self.obj1034,self.obj964,[287.5, 262.0, 392.0, 511.0],"true", 2) )
    # Connections for obj1035 (graphObject_: Obj376) of type apply_contains
    self.drawConnections(
(self.obj1035,self.obj965,[377.5, 262.0, 612.0, 511.0],"true", 2) )
    # Connections for obj1036 (graphObject_: Obj377) of type apply_contains
    self.drawConnections(
(self.obj1036,self.obj966,[477.5, 262.0, 812.0, 511.0],"true", 2) )
    # Connections for obj1037 (graphObject_: Obj378) of type apply_contains
    self.drawConnections(
(self.obj1037,self.obj976,[677.5, 202.0, 1212.0, 231.0],"true", 2) )
    # Connections for obj1038 (graphObject_: Obj379) of type apply_contains
    self.drawConnections(
(self.obj1038,self.obj977,[677.5, 332.0, 1212.0, 491.0],"true", 2) )
    # Connections for obj1039 (graphObject_: Obj380) of type apply_contains
    self.drawConnections(
(self.obj1039,self.obj967,[837.5, 122.0, 1532.0, 71.0],"true", 2) )
    # Connections for obj1040 (graphObject_: Obj381) of type apply_contains
    self.drawConnections(
(self.obj1040,self.obj968,[837.5, 172.0, 1532.0, 171.0],"true", 2) )
    # Connections for obj1041 (graphObject_: Obj382) of type apply_contains
    self.drawConnections(
(self.obj1041,self.obj969,[837.5, 222.0, 1532.0, 271.0],"true", 2) )
    # Connections for obj1042 (graphObject_: Obj383) of type apply_contains
    self.drawConnections(
(self.obj1042,self.obj970,[837.5, 272.0, 1532.0, 371.0],"true", 2) )
    # Connections for obj1043 (graphObject_: Obj384) of type apply_contains
    self.drawConnections(
(self.obj1043,self.obj971,[837.5, 332.0, 1532.0, 491.0],"true", 2) )
    # Connections for obj1044 (graphObject_: Obj385) of type apply_contains
    self.drawConnections(
(self.obj1044,self.obj972,[833.5, 407.0, 1532.0, 591.0],"true", 2) )
    # Connections for obj1045 (graphObject_: Obj386) of type apply_contains
    self.drawConnections(
(self.obj1045,self.obj973,[837.5, 442.0, 1532.0, 711.0],"true", 2) )
    # Connections for obj1046 (graphObject_: Obj387) of type directLink_T
    self.drawConnections(
(self.obj1046,self.obj978,[502.0, 231.0, 592.0, 351.0],"true", 2) )
    # Connections for obj1047 (graphObject_: Obj388) of type directLink_T
    self.drawConnections(
(self.obj1047,self.obj974,[712.0, 231.0, 832.0, 351.0],"true", 2) )
    # Connections for obj1048 (graphObject_: Obj389) of type directLink_T
    self.drawConnections(
(self.obj1048,self.obj975,[912.0, 231.0, 1012.0, 231.0],"true", 2) )
    # Connections for obj1049 (graphObject_: Obj390) of type directLink_T
    self.drawConnections(
(self.obj1049,self.obj976,[1122.0, 231.0, 1212.0, 231.0],"true", 2) )
    # Connections for obj1050 (graphObject_: Obj391) of type directLink_T
    self.drawConnections(
(self.obj1050,self.obj963,[190.0, 249.0, 192.0, 331.0],"true", 2) )
    # Connections for obj1051 (graphObject_: Obj392) of type directLink_T
    self.drawConnections(
(self.obj1051,self.obj964,[622.0, 291.0, 392.0, 511.0],"true", 2) )
    # Connections for obj1052 (graphObject_: Obj393) of type directLink_T
    self.drawConnections(
(self.obj1052,self.obj965,[712.0, 291.0, 612.0, 511.0],"true", 2) )
    # Connections for obj1053 (graphObject_: Obj394) of type directLink_T
    self.drawConnections(
(self.obj1053,self.obj966,[812.0, 291.0, 812.0, 511.0],"true", 2) )
    # Connections for obj1054 (graphObject_: Obj395) of type directLink_T
    self.drawConnections(
(self.obj1054,self.obj967,[1310.0, 102.0, 1532.0, 71.0],"true", 2) )
    # Connections for obj1055 (graphObject_: Obj396) of type directLink_T
    self.drawConnections(
(self.obj1055,self.obj968,[1314.0, 166.0, 1532.0, 171.0],"true", 2) )
    # Connections for obj1056 (graphObject_: Obj397) of type directLink_T
    self.drawConnections(
(self.obj1056,self.obj969,[1311.0, 266.0, 1532.0, 271.0],"true", 2) )
    # Connections for obj1057 (graphObject_: Obj398) of type directLink_T
    self.drawConnections(
(self.obj1057,self.obj970,[1335.0, 330.0, 1532.0, 371.0],"true", 2) )
    # Connections for obj1058 (graphObject_: Obj399) of type directLink_T
    self.drawConnections(
(self.obj1058,self.obj977,[1016.0, 492.0, 1212.0, 491.0],"true", 2) )
    # Connections for obj1059 (graphObject_: Obj400) of type directLink_T
    self.drawConnections(
(self.obj1059,self.obj971,[1372.0, 491.0, 1532.0, 491.0],"true", 2) )
    # Connections for obj1060 (graphObject_: Obj401) of type directLink_T
    self.drawConnections(
(self.obj1060,self.obj972,[1359.0, 527.0, 1532.0, 591.0],"true", 2) )
    # Connections for obj1061 (graphObject_: Obj402) of type directLink_T
    self.drawConnections(
(self.obj1061,self.obj973,[1372.0, 601.0, 1532.0, 711.0],"true", 2) )
    # Connections for obj1062 (graphObject_: Obj403) of type backward_link
    self.drawConnections(
(self.obj1062,self.obj961,[391.0, 147.0, 390.0, 51.0],"true", 2) )
    # Connections for obj1063 (graphObject_: Obj404) of type hasAttribute_S
    self.drawConnections(
(self.obj1063,self.obj979,[482.0, 68.5, 574.0, 40.0],"true", 2) )
    # Connections for obj1064 (graphObject_: Obj405) of type hasAttribute_T
    self.drawConnections(
(self.obj1064,self.obj980,[167.0, 377.5, 154.0, 414.0],"true", 2) )
    # Connections for obj1065 (graphObject_: Obj406) of type hasAttribute_T
    self.drawConnections(
(self.obj1065,self.obj981,[413.0, 392.5, 394.0, 614.0],"true", 2) )
    # Connections for obj1066 (graphObject_: Obj407) of type hasAttribute_T
    self.drawConnections(
(self.obj1066,self.obj982,[593.0, 392.5, 574.0, 614.0],"true", 2) )
    # Connections for obj1067 (graphObject_: Obj408) of type hasAttribute_T
    self.drawConnections(
(self.obj1067,self.obj983,[793.0, 392.5, 774.0, 634.0],"true", 2) )
    # Connections for obj1068 (graphObject_: Obj409) of type hasAttribute_T
    self.drawConnections(
(self.obj1068,self.obj984,[1193.0, 272.5, 1174.0, 314.0],"true", 2) )
    # Connections for obj1069 (graphObject_: Obj410) of type hasAttribute_T
    self.drawConnections(
(self.obj1069,self.obj985,[1603.0, 62.5, 1674.0, 54.0],"true", 2) )
    # Connections for obj1070 (graphObject_: Obj411) of type hasAttribute_T
    self.drawConnections(
(self.obj1070,self.obj986,[1603.0, 162.5, 1674.0, 154.0],"true", 2) )
    # Connections for obj1071 (graphObject_: Obj412) of type hasAttribute_T
    self.drawConnections(
(self.obj1071,self.obj987,[1603.0, 262.5, 1674.0, 254.0],"true", 2) )
    # Connections for obj1072 (graphObject_: Obj413) of type hasAttribute_T
    self.drawConnections(
(self.obj1072,self.obj988,[1603.0, 362.5, 1674.0, 354.0],"true", 2) )
    # Connections for obj1073 (graphObject_: Obj414) of type hasAttribute_T
    self.drawConnections(
(self.obj1073,self.obj989,[1193.0, 532.5, 1174.0, 574.0],"true", 2) )
    # Connections for obj1074 (graphObject_: Obj415) of type hasAttribute_T
    self.drawConnections(
(self.obj1074,self.obj990,[1603.0, 482.5, 1674.0, 474.0],"true", 2) )
    # Connections for obj1075 (graphObject_: Obj416) of type hasAttribute_T
    self.drawConnections(
(self.obj1075,self.obj991,[1603.0, 582.5, 1674.0, 574.0],"true", 2) )
    # Connections for obj1076 (graphObject_: Obj417) of type hasAttribute_T
    self.drawConnections(
(self.obj1076,self.obj992,[1603.0, 702.5, 1674.0, 694.0],"true", 2) )
    # Connections for obj1077 (graphObject_: Obj418) of type hasAttribute_T
    self.drawConnections(
(self.obj1077,self.obj993,[373.0, 182.5, 294.0, 134.0],"true", 2) )
    # Connections for obj1078 (graphObject_: Obj419) of type hasAttribute_T
    self.drawConnections(
(self.obj1078,self.obj994,[663.0, 232.5, 734.0, 114.0],"true", 2) )
    # Connections for obj1079 (graphObject_: Obj420) of type leftExpr
    self.drawConnections(
(self.obj1079,self.obj979,[666.0, 76.5, 574.0, 40.0],"true", 2) )
    # Connections for obj1080 (graphObject_: Obj421) of type leftExpr
    self.drawConnections(
(self.obj1080,self.obj980,[153.0, 457.0, 154.0, 414.0],"true", 2) )
    # Connections for obj1081 (graphObject_: Obj422) of type leftExpr
    self.drawConnections(
(self.obj1081,self.obj981,[396.0, 476.5, 394.0, 614.0],"true", 2) )
    # Connections for obj1082 (graphObject_: Obj423) of type leftExpr
    self.drawConnections(
(self.obj1082,self.obj982,[576.0, 476.5, 574.0, 614.0],"true", 2) )
    # Connections for obj1083 (graphObject_: Obj424) of type leftExpr
    self.drawConnections(
(self.obj1083,self.obj983,[776.0, 476.5, 774.0, 634.0],"true", 2) )
    # Connections for obj1084 (graphObject_: Obj425) of type leftExpr
    self.drawConnections(
(self.obj1084,self.obj984,[1246.0, 336.5, 1174.0, 314.0],"true", 2) )
    # Connections for obj1085 (graphObject_: Obj426) of type leftExpr
    self.drawConnections(
(self.obj1085,self.obj985,[1756.0, 56.5, 1674.0, 54.0],"true", 2) )
    # Connections for obj1086 (graphObject_: Obj427) of type leftExpr
    self.drawConnections(
(self.obj1086,self.obj986,[1756.0, 156.5, 1674.0, 154.0],"true", 2) )
    # Connections for obj1087 (graphObject_: Obj428) of type leftExpr
    self.drawConnections(
(self.obj1087,self.obj987,[1756.0, 256.5, 1674.0, 254.0],"true", 2) )
    # Connections for obj1088 (graphObject_: Obj429) of type leftExpr
    self.drawConnections(
(self.obj1088,self.obj988,[1756.0, 356.5, 1674.0, 354.0],"true", 2) )
    # Connections for obj1089 (graphObject_: Obj430) of type leftExpr
    self.drawConnections(
(self.obj1089,self.obj989,[1246.0, 596.5, 1174.0, 574.0],"true", 2) )
    # Connections for obj1090 (graphObject_: Obj431) of type leftExpr
    self.drawConnections(
(self.obj1090,self.obj990,[1756.0, 476.5, 1674.0, 474.0],"true", 2) )
    # Connections for obj1091 (graphObject_: Obj432) of type leftExpr
    self.drawConnections(
(self.obj1091,self.obj991,[1756.0, 576.5, 1674.0, 574.0],"true", 2) )
    # Connections for obj1092 (graphObject_: Obj433) of type leftExpr
    self.drawConnections(
(self.obj1092,self.obj992,[1756.0, 696.5, 1674.0, 694.0],"true", 2) )
    # Connections for obj1093 (graphObject_: Obj434) of type leftExpr
    self.drawConnections(
(self.obj1093,self.obj993,[446.0, 126.5, 294.0, 134.0],"true", 2) )
    # Connections for obj1094 (graphObject_: Obj435) of type leftExpr
    self.drawConnections(
(self.obj1094,self.obj994,[806.0, 116.5, 734.0, 114.0],"true", 2) )
    # Connections for obj1095 (graphObject_: Obj436) of type rightExpr
    self.drawConnections(
(self.obj1095,self.obj1011,[846.0, 76.5, 934.0, 41.0],"true", 2) )
    # Connections for obj1096 (graphObject_: Obj437) of type rightExpr
    self.drawConnections(
(self.obj1096,self.obj1012,[154.0, 532.0, 154.0, 574.0],"true", 2) )
    # Connections for obj1097 (graphObject_: Obj438) of type rightExpr
    self.drawConnections(
(self.obj1097,self.obj1013,[396.0, 556.5, 394.0, 794.0],"true", 2) )
    # Connections for obj1098 (graphObject_: Obj439) of type rightExpr
    self.drawConnections(
(self.obj1098,self.obj1014,[576.0, 556.5, 574.0, 794.0],"true", 2) )
    # Connections for obj1099 (graphObject_: Obj440) of type rightExpr
    self.drawConnections(
(self.obj1099,self.obj1015,[776.0, 556.5, 774.0, 794.0],"true", 2) )
    # Connections for obj1100 (graphObject_: Obj441) of type rightExpr
    self.drawConnections(
(self.obj1100,self.obj1016,[1246.0, 376.5, 1174.0, 394.0],"true", 2) )
    # Connections for obj1101 (graphObject_: Obj442) of type rightExpr
    self.drawConnections(
(self.obj1101,self.obj1017,[1916.0, 56.5, 1994.0, 54.0],"true", 2) )
    # Connections for obj1102 (graphObject_: Obj443) of type rightExpr
    self.drawConnections(
(self.obj1102,self.obj1018,[1916.0, 156.5, 1994.0, 154.0],"true", 2) )
    # Connections for obj1103 (graphObject_: Obj444) of type rightExpr
    self.drawConnections(
(self.obj1103,self.obj1019,[1916.0, 256.5, 1994.0, 254.0],"true", 2) )
    # Connections for obj1104 (graphObject_: Obj445) of type rightExpr
    self.drawConnections(
(self.obj1104,self.obj1020,[1916.0, 356.5, 1994.0, 354.0],"true", 2) )
    # Connections for obj1105 (graphObject_: Obj446) of type rightExpr
    self.drawConnections(
(self.obj1105,self.obj1021,[1246.0, 636.5, 1174.0, 654.0],"true", 2) )
    # Connections for obj1106 (graphObject_: Obj447) of type rightExpr
    self.drawConnections(
(self.obj1106,self.obj1022,[1916.0, 476.5, 1994.0, 474.0],"true", 2) )
    # Connections for obj1107 (graphObject_: Obj448) of type rightExpr
    self.drawConnections(
(self.obj1107,self.obj1023,[1916.0, 576.5, 1994.0, 574.0],"true", 2) )
    # Connections for obj1108 (graphObject_: Obj449) of type rightExpr
    self.drawConnections(
(self.obj1108,self.obj1024,[1916.0, 696.5, 1994.0, 694.0],"true", 2) )
    # Connections for obj1109 (graphObject_: Obj450) of type rightExpr
    self.drawConnections(
(self.obj1109,self.obj1025,[538.0, 116.5, 584.0, 114.0],"true", 2) )
    # Connections for obj1110 (graphObject_: Obj451) of type rightExpr
    self.drawConnections(
(self.obj1110,self.obj1026,[950.5, 116.5, 1023.0, 114.0],"true", 2) )

newfunction = CompositeState2ProcDef_MDL

loadedMMName = 'UMLRT2Kiltera_MM_META'

atom3version = '0.3'
