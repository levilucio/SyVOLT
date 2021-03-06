"""
__GM2AUTOSAR_MM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sun Aug  9 23:41:35 2015
___________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from CD_Class3 import *
from CD_Association3 import *
from CD_Inheritance3 import *
from graph_CD_Association3 import *
from graph_CD_Class3 import *
from graph_CD_Inheritance3 import *
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

def GM2AUTOSAR_MM_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('GM2AUTOSAR_MM')

        # author
        CD_ClassDiagramsV3RootNode.author.setValue('Annonymous')

        # showCardinalities
        CD_ClassDiagramsV3RootNode.showCardinalities.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showCardinalities.config = 0

        # showAssociationBox
        CD_ClassDiagramsV3RootNode.showAssociationBox.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAssociationBox.config = 0

        # description
        CD_ClassDiagramsV3RootNode.description.setValue('\n')
        CD_ClassDiagramsV3RootNode.description.setHeight(15)

        # showAttributes
        CD_ClassDiagramsV3RootNode.showAttributes.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAttributes.config = 0

        # showActions
        CD_ClassDiagramsV3RootNode.showActions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showActions.config = 0

        # showConditions
        CD_ClassDiagramsV3RootNode.showConditions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showConditions.config = 0

        # attributes
        CD_ClassDiagramsV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        CD_ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        CD_ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj28=CD_Class3(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # QOCA
    self.obj28.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj28.Graphical_Appearance.setValue( ('MatchModel', self.obj28))

    # name
    self.obj28.name.setValue('MatchModel')

    # attributes
    self.obj28.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.attributes.setValue(lcobj2)

    # Abstract
    self.obj28.Abstract.setValue((None, 0))
    self.obj28.Abstract.config = 0

    # cardinality
    self.obj28.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('paired_with', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('match_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj28.cardinality.setValue(lcobj2)

    # display
    self.obj28.display.setValue('Multiplicities:\n  - To paired_with: 1 to 1\n  - To match_contains: 0 to N\n')
    self.obj28.display.setHeight(15)

    # Actions
    self.obj28.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.Actions.setValue(lcobj2)

    # Constraints
    self.obj28.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.Constraints.setValue(lcobj2)

    self.obj28.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(46.0,50.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=CD_Class3(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # QOCA
    self.obj29.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj29.Graphical_Appearance.setValue( ('ApplyModel', self.obj29))

    # name
    self.obj29.name.setValue('ApplyModel')

    # attributes
    self.obj29.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.attributes.setValue(lcobj2)

    # Abstract
    self.obj29.Abstract.setValue((None, 0))
    self.obj29.Abstract.config = 0

    # cardinality
    self.obj29.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('paired_with', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('apply_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj29.cardinality.setValue(lcobj2)

    # display
    self.obj29.display.setValue('Multiplicities:\n  - From paired_with: 1 to 1\n  - To apply_contains: 0 to N\n')
    self.obj29.display.setHeight(15)

    # Actions
    self.obj29.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.Actions.setValue(lcobj2)

    # Constraints
    self.obj29.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.Constraints.setValue(lcobj2)

    self.obj29.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(68.0,621.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0828125, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=CD_Class3(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # QOCA
    self.obj30.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj30.Graphical_Appearance.setValue( ('MetaModelElement_S', self.obj30))

    # name
    self.obj30.name.setValue('MetaModelElement_S')

    # attributes
    self.obj30.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj30.attributes.setValue(lcobj2)

    # Abstract
    self.obj30.Abstract.setValue((None, 1))
    self.obj30.Abstract.config = 0

    # cardinality
    self.obj30.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('match_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('directLink_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('directLink_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('indirectLink_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('indirectLink_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('backward_link', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('trace_link', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj30.cardinality.setValue(lcobj2)

    # display
    self.obj30.display.setValue('Attributes:\n  - attr1 :: String\nMultiplicities:\n  - From match_contains: 0 to N\n  - To directLink_S: 0 to N\n  - From directLink_S: 0 to N\n  - To indirectLink_S: 0 to N\n  - From indirectLink_S: 0 to N\n  - From backward_link: 0 to N\n  - From trace_link: 0 to N\n')
    self.obj30.display.setHeight(15)

    # Actions
    self.obj30.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj30.Actions.setValue(lcobj2)

    # Constraints
    self.obj30.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj30.Constraints.setValue(lcobj2)

    self.obj30.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(599.0,46.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.9
       new_obj.layConstraints['scale'] = [1.0171875000000001, 1.4631147540983607]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=CD_Class3(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # QOCA
    self.obj31.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj31.Graphical_Appearance.setValue( ('MetaModelElement_T', self.obj31))

    # name
    self.obj31.name.setValue('MetaModelElement_T')

    # attributes
    self.obj31.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj31.attributes.setValue(lcobj2)

    # Abstract
    self.obj31.Abstract.setValue((None, 1))
    self.obj31.Abstract.config = 0

    # cardinality
    self.obj31.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('directLink_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('directLink_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('apply_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('backward_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('trace_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj31.cardinality.setValue(lcobj2)

    # display
    self.obj31.display.setValue('Attributes:\n  - attr1 :: String\nMultiplicities:\n  - To directLink_T: 0 to N\n  - From directLink_T: 0 to N\n  - From apply_contains: 0 to N\n  - To backward_link: 0 to N\n  - To trace_link: 0 to N\n')
    self.obj31.display.setHeight(15)

    # Actions
    self.obj31.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj31.Actions.setValue(lcobj2)

    # Constraints
    self.obj31.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj31.Constraints.setValue(lcobj2)

    self.obj31.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,592.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.91
       new_obj.layConstraints['scale'] = [1.0, 1.1704918032786886]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=CD_Class3(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # QOCA
    self.obj32.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj32.Graphical_Appearance.setValue( ('ECU', self.obj32))

    # name
    self.obj32.name.setValue('ECU')

    # attributes
    self.obj32.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj32.attributes.setValue(lcobj2)

    # Abstract
    self.obj32.Abstract.setValue((None, 0))
    self.obj32.Abstract.config = 0

    # cardinality
    self.obj32.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj32.cardinality.setValue(lcobj2)

    # display
    self.obj32.display.setValue('Attributes:\n')
    self.obj32.display.setHeight(15)

    # Actions
    self.obj32.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.Actions.setValue(lcobj2)

    # Constraints
    self.obj32.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.Constraints.setValue(lcobj2)

    self.obj32.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(314.0,210.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=CD_Class3(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # QOCA
    self.obj33.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj33.Graphical_Appearance.setValue( ('VirtualDevice', self.obj33))

    # name
    self.obj33.name.setValue('VirtualDevice')

    # attributes
    self.obj33.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj33.attributes.setValue(lcobj2)

    # Abstract
    self.obj33.Abstract.setValue((None, 0))
    self.obj33.Abstract.config = 0

    # cardinality
    self.obj33.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj33.cardinality.setValue(lcobj2)

    # display
    self.obj33.display.setValue('Attributes:\n')
    self.obj33.display.setHeight(15)

    # Actions
    self.obj33.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.Actions.setValue(lcobj2)

    # Constraints
    self.obj33.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.Constraints.setValue(lcobj2)

    self.obj33.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(300.0,380.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=CD_Class3(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # QOCA
    self.obj34.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj34.Graphical_Appearance.setValue( ('Distributable', self.obj34))

    # name
    self.obj34.name.setValue('Distributable')

    # attributes
    self.obj34.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj34.attributes.setValue(lcobj2)

    # Abstract
    self.obj34.Abstract.setValue((None, 0))
    self.obj34.Abstract.config = 0

    # cardinality
    self.obj34.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj34.cardinality.setValue(lcobj2)

    # display
    self.obj34.display.setValue('Attributes:\n')
    self.obj34.display.setHeight(15)

    # Actions
    self.obj34.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Actions.setValue(lcobj2)

    # Constraints
    self.obj34.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Constraints.setValue(lcobj2)

    self.obj34.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,380.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=CD_Class3(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # QOCA
    self.obj35.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj35.Graphical_Appearance.setValue( ('ExecFrame', self.obj35))

    # name
    self.obj35.name.setValue('ExecFrame')

    # attributes
    self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj35.attributes.setValue(lcobj2)

    # Abstract
    self.obj35.Abstract.setValue((None, 0))
    self.obj35.Abstract.config = 0

    # cardinality
    self.obj35.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj35.cardinality.setValue(lcobj2)

    # display
    self.obj35.display.setValue('Attributes:\n')
    self.obj35.display.setHeight(15)

    # Actions
    self.obj35.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Actions.setValue(lcobj2)

    # Constraints
    self.obj35.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Constraints.setValue(lcobj2)

    self.obj35.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,380.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.02
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=CD_Class3(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # QOCA
    self.obj36.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj36.Graphical_Appearance.setValue( ('Signal', self.obj36))

    # name
    self.obj36.name.setValue('Signal')

    # attributes
    self.obj36.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj36.attributes.setValue(lcobj2)

    # Abstract
    self.obj36.Abstract.setValue((None, 0))
    self.obj36.Abstract.config = 0

    # cardinality
    self.obj36.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj36.cardinality.setValue(lcobj2)

    # display
    self.obj36.display.setValue('Attributes:\n')
    self.obj36.display.setHeight(15)

    # Actions
    self.obj36.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Actions.setValue(lcobj2)

    # Constraints
    self.obj36.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Constraints.setValue(lcobj2)

    self.obj36.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(940.0,260.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=CD_Class3(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # QOCA
    self.obj37.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj37.Graphical_Appearance.setValue( ('System', self.obj37))

    # name
    self.obj37.name.setValue('System')

    # attributes
    self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj37.attributes.setValue(lcobj2)

    # Abstract
    self.obj37.Abstract.setValue((None, 0))
    self.obj37.Abstract.config = 0

    # cardinality
    self.obj37.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj37.cardinality.setValue(lcobj2)

    # display
    self.obj37.display.setValue('Attributes:\n')
    self.obj37.display.setHeight(15)

    # Actions
    self.obj37.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Actions.setValue(lcobj2)

    # Constraints
    self.obj37.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Constraints.setValue(lcobj2)

    self.obj37.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(31.0,819.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=CD_Class3(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # QOCA
    self.obj38.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj38.Graphical_Appearance.setValue( ('SystemMapping', self.obj38))

    # name
    self.obj38.name.setValue('SystemMapping')

    # attributes
    self.obj38.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj38.attributes.setValue(lcobj2)

    # Abstract
    self.obj38.Abstract.setValue((None, 0))
    self.obj38.Abstract.config = 0

    # cardinality
    self.obj38.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj38.cardinality.setValue(lcobj2)

    # display
    self.obj38.display.setValue('Attributes:\n')
    self.obj38.display.setHeight(15)

    # Actions
    self.obj38.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.Actions.setValue(lcobj2)

    # Constraints
    self.obj38.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.Constraints.setValue(lcobj2)

    self.obj38.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(236.0,818.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=CD_Class3(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # QOCA
    self.obj39.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj39.Graphical_Appearance.setValue( ('SoftwareComposition', self.obj39))

    # name
    self.obj39.name.setValue('SoftwareComposition')

    # attributes
    self.obj39.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj39.attributes.setValue(lcobj2)

    # Abstract
    self.obj39.Abstract.setValue((None, 0))
    self.obj39.Abstract.config = 0

    # cardinality
    self.obj39.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj39.cardinality.setValue(lcobj2)

    # display
    self.obj39.display.setValue('Attributes:\n')
    self.obj39.display.setHeight(15)

    # Actions
    self.obj39.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Actions.setValue(lcobj2)

    # Constraints
    self.obj39.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Constraints.setValue(lcobj2)

    self.obj39.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(293.0,1156.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.03125, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=CD_Class3(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # QOCA
    self.obj40.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj40.Graphical_Appearance.setValue( ('CompositionType', self.obj40))

    # name
    self.obj40.name.setValue('CompositionType')

    # attributes
    self.obj40.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj40.attributes.setValue(lcobj2)

    # Abstract
    self.obj40.Abstract.setValue((None, 0))
    self.obj40.Abstract.config = 0

    # cardinality
    self.obj40.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj40.cardinality.setValue(lcobj2)

    # display
    self.obj40.display.setValue('Attributes:\n')
    self.obj40.display.setHeight(15)

    # Actions
    self.obj40.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Actions.setValue(lcobj2)

    # Constraints
    self.obj40.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Constraints.setValue(lcobj2)

    self.obj40.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(498.0,1156.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=CD_Class3(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # QOCA
    self.obj41.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj41.Graphical_Appearance.setValue( ('ComponentPrototype', self.obj41))

    # name
    self.obj41.name.setValue('ComponentPrototype')

    # attributes
    self.obj41.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj41.attributes.setValue(lcobj2)

    # Abstract
    self.obj41.Abstract.setValue((None, 0))
    self.obj41.Abstract.config = 0

    # cardinality
    self.obj41.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj41.cardinality.setValue(lcobj2)

    # display
    self.obj41.display.setValue('Attributes:\n')
    self.obj41.display.setHeight(15)

    # Actions
    self.obj41.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Actions.setValue(lcobj2)

    # Constraints
    self.obj41.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Constraints.setValue(lcobj2)

    self.obj41.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(158.0,978.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.03125, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=CD_Class3(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # QOCA
    self.obj42.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj42.Graphical_Appearance.setValue( ('PPortPrototype', self.obj42))

    # name
    self.obj42.name.setValue('PPortPrototype')

    # attributes
    self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj42.attributes.setValue(lcobj2)

    # Abstract
    self.obj42.Abstract.setValue((None, 0))
    self.obj42.Abstract.config = 0

    # cardinality
    self.obj42.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj42.cardinality.setValue(lcobj2)

    # display
    self.obj42.display.setValue('Attributes:\n')
    self.obj42.display.setHeight(15)

    # Actions
    self.obj42.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj42.Actions.setValue(lcobj2)

    # Constraints
    self.obj42.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj42.Constraints.setValue(lcobj2)

    self.obj42.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(699.0,1157.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=CD_Class3(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # QOCA
    self.obj43.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj43.Graphical_Appearance.setValue( ('RPortPrototype', self.obj43))

    # name
    self.obj43.name.setValue('RPortPrototype')

    # attributes
    self.obj43.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj43.attributes.setValue(lcobj2)

    # Abstract
    self.obj43.Abstract.setValue((None, 0))
    self.obj43.Abstract.config = 0

    # cardinality
    self.obj43.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj43.cardinality.setValue(lcobj2)

    # display
    self.obj43.display.setValue('Attributes:\n')
    self.obj43.display.setHeight(15)

    # Actions
    self.obj43.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.Actions.setValue(lcobj2)

    # Constraints
    self.obj43.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.Constraints.setValue(lcobj2)

    self.obj43.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(900.0,1160.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=CD_Class3(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # QOCA
    self.obj44.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj44.Graphical_Appearance.setValue( ('EcuInstance', self.obj44))

    # name
    self.obj44.name.setValue('EcuInstance')

    # attributes
    self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj44.attributes.setValue(lcobj2)

    # Abstract
    self.obj44.Abstract.setValue((None, 0))
    self.obj44.Abstract.config = 0

    # cardinality
    self.obj44.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj44.cardinality.setValue(lcobj2)

    # display
    self.obj44.display.setValue('Attributes:\n')
    self.obj44.display.setHeight(15)

    # Actions
    self.obj44.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj44.Actions.setValue(lcobj2)

    # Constraints
    self.obj44.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj44.Constraints.setValue(lcobj2)

    self.obj44.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(414.0,977.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=CD_Class3(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # QOCA
    self.obj45.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj45.Graphical_Appearance.setValue( ('SwcToEcuMapping', self.obj45))

    # name
    self.obj45.name.setValue('SwcToEcuMapping')

    # attributes
    self.obj45.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj45.attributes.setValue(lcobj2)

    # Abstract
    self.obj45.Abstract.setValue((None, 0))
    self.obj45.Abstract.config = 0

    # cardinality
    self.obj45.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj45.cardinality.setValue(lcobj2)

    # display
    self.obj45.display.setValue('Attributes:\n')
    self.obj45.display.setHeight(15)

    # Actions
    self.obj45.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.Actions.setValue(lcobj2)

    # Constraints
    self.obj45.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.Constraints.setValue(lcobj2)

    self.obj45.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(455.0,817.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=CD_Class3(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # QOCA
    self.obj46.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj46.Graphical_Appearance.setValue( ('SwCompToEcuMapping_component', self.obj46))

    # name
    self.obj46.name.setValue('SwCompToEcuMapping_component')

    # attributes
    self.obj46.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj46.attributes.setValue(lcobj2)

    # Abstract
    self.obj46.Abstract.setValue((None, 0))
    self.obj46.Abstract.config = 0

    # cardinality
    self.obj46.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj46.cardinality.setValue(lcobj2)

    # display
    self.obj46.display.setValue('Attributes:\n')
    self.obj46.display.setHeight(15)

    # Actions
    self.obj46.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj46.Actions.setValue(lcobj2)

    # Constraints
    self.obj46.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj46.Constraints.setValue(lcobj2)

    self.obj46.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(985.0,817.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7562499999999999, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=CD_Class3(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # QOCA
    self.obj47.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj47.Graphical_Appearance.setValue( ('PortPrototype', self.obj47))

    # name
    self.obj47.name.setValue('PortPrototype')

    # attributes
    self.obj47.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj47.attributes.setValue(lcobj2)

    # Abstract
    self.obj47.Abstract.setValue((None, 0))
    self.obj47.Abstract.config = 0

    # cardinality
    self.obj47.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj47.cardinality.setValue(lcobj2)

    # display
    self.obj47.display.setValue('Attributes:\n')
    self.obj47.display.setHeight(15)

    # Actions
    self.obj47.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj47.Actions.setValue(lcobj2)

    # Constraints
    self.obj47.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj47.Constraints.setValue(lcobj2)

    self.obj47.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(920.0,977.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=CD_Class3(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # QOCA
    self.obj48.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj48.Graphical_Appearance.setValue( ('ComponentType', self.obj48))

    # name
    self.obj48.name.setValue('ComponentType')

    # attributes
    self.obj48.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj48.attributes.setValue(lcobj2)

    # Abstract
    self.obj48.Abstract.setValue((None, 0))
    self.obj48.Abstract.config = 0

    # cardinality
    self.obj48.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj48.cardinality.setValue(lcobj2)

    # display
    self.obj48.display.setValue('Attributes:\n')
    self.obj48.display.setHeight(15)

    # Actions
    self.obj48.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj48.Actions.setValue(lcobj2)

    # Constraints
    self.obj48.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj48.Constraints.setValue(lcobj2)

    self.obj48.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(672.0,977.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=CD_Association3(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # QOCA
    self.obj49.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj49.Graphical_Appearance.setValue( ('paired_with', self.obj49))
    self.obj49.Graphical_Appearance.linkInfo=linkEditor(self,self.obj49.Graphical_Appearance.semObject, "paired_with")
    self.obj49.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('paired_with_1stLink', self.obj49.Graphical_Appearance.linkInfo.FirstLink))
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('paired_with_1stSegment', self.obj49.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj49.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj49.Graphical_Appearance.linkInfo.Center.setValue( ('paired_with_Center', self.obj49.Graphical_Appearance.linkInfo))
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('paired_with_2ndSegment', self.obj49.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj49.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('paired_with_2ndLink', self.obj49.Graphical_Appearance.linkInfo.SecondLink))
    self.obj49.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj49.Graphical_Appearance.semObject
    self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj49.Graphical_Appearance.semObject
    self.obj49.Graphical_Appearance.linkInfo.Center.semObject=self.obj49.Graphical_Appearance.semObject
    self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj49.Graphical_Appearance.semObject
    self.obj49.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj49.Graphical_Appearance.semObject

    # name
    self.obj49.name.setValue('paired_with')

    # displaySelect
    self.obj49.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj49.displaySelect.config = 0

    # attributes
    self.obj49.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.attributes.setValue(lcobj2)

    # cardinality
    self.obj49.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('ApplyModel', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MatchModel', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj49.cardinality.setValue(lcobj2)

    # display
    self.obj49.display.setValue('Multiplicities:\n  - To ApplyModel: 1 to 1\n  - From MatchModel: 1 to 1\n')
    self.obj49.display.setHeight(15)

    # Actions
    self.obj49.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.Actions.setValue(lcobj2)

    # Constraints
    self.obj49.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.Constraints.setValue(lcobj2)

    self.obj49.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(153.0,394.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.84
       new_obj.layConstraints['scale'] = [1.134, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=CD_Association3(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # QOCA
    self.obj50.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj50.Graphical_Appearance.setValue( ('match_contains', self.obj50))
    self.obj50.Graphical_Appearance.linkInfo=linkEditor(self,self.obj50.Graphical_Appearance.semObject, "match_contains")
    self.obj50.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('match_contains_1stLink', self.obj50.Graphical_Appearance.linkInfo.FirstLink))
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('match_contains_1stSegment', self.obj50.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj50.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj50.Graphical_Appearance.linkInfo.Center.setValue( ('match_contains_Center', self.obj50.Graphical_Appearance.linkInfo))
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('match_contains_2ndSegment', self.obj50.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj50.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('match_contains_2ndLink', self.obj50.Graphical_Appearance.linkInfo.SecondLink))
    self.obj50.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj50.Graphical_Appearance.semObject
    self.obj50.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj50.Graphical_Appearance.semObject
    self.obj50.Graphical_Appearance.linkInfo.Center.semObject=self.obj50.Graphical_Appearance.semObject
    self.obj50.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj50.Graphical_Appearance.semObject
    self.obj50.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj50.Graphical_Appearance.semObject

    # name
    self.obj50.name.setValue('match_contains')

    # displaySelect
    self.obj50.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj50.displaySelect.config = 0

    # attributes
    self.obj50.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.attributes.setValue(lcobj2)

    # cardinality
    self.obj50.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MatchModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj50.cardinality.setValue(lcobj2)

    # display
    self.obj50.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MatchModel: 0 to N\n')
    self.obj50.display.setHeight(15)

    # Actions
    self.obj50.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.Actions.setValue(lcobj2)

    # Constraints
    self.obj50.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.Constraints.setValue(lcobj2)

    self.obj50.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(425.350433087,120.205,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.95
       new_obj.layConstraints['scale'] = [1.5890000000000002, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=CD_Association3(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # QOCA
    self.obj51.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj51.Graphical_Appearance.setValue( ('directLink_S', self.obj51))
    self.obj51.Graphical_Appearance.linkInfo=linkEditor(self,self.obj51.Graphical_Appearance.semObject, "directLink_S")
    self.obj51.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_S_1stLink', self.obj51.Graphical_Appearance.linkInfo.FirstLink))
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_S_1stSegment', self.obj51.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj51.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_S_Center', self.obj51.Graphical_Appearance.linkInfo))
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_S_2ndSegment', self.obj51.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_S_2ndLink', self.obj51.Graphical_Appearance.linkInfo.SecondLink))
    self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.Center.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj51.Graphical_Appearance.semObject
    self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj51.Graphical_Appearance.semObject

    # name
    self.obj51.name.setValue('directLink_S')

    # displaySelect
    self.obj51.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj51.displaySelect.config = 0

    # attributes
    self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attr1', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj51.attributes.setValue(lcobj2)

    # cardinality
    self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj51.cardinality.setValue(lcobj2)

    # display
    self.obj51.display.setValue('Attributes:\n  - attr1 :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj51.display.setHeight(15)

    # Actions
    self.obj51.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Actions.setValue(lcobj2)

    # Constraints
    self.obj51.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Constraints.setValue(lcobj2)

    self.obj51.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1018.35617001,75.74025,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.86
       new_obj.layConstraints['scale'] = [1.554, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=CD_Association3(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # QOCA
    self.obj52.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj52.Graphical_Appearance.setValue( ('directLink_T', self.obj52))
    self.obj52.Graphical_Appearance.linkInfo=linkEditor(self,self.obj52.Graphical_Appearance.semObject, "directLink_T")
    self.obj52.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_T_1stLink', self.obj52.Graphical_Appearance.linkInfo.FirstLink))
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_T_1stSegment', self.obj52.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj52.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_T_Center', self.obj52.Graphical_Appearance.linkInfo))
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_T_2ndSegment', self.obj52.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_T_2ndLink', self.obj52.Graphical_Appearance.linkInfo.SecondLink))
    self.obj52.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.Center.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj52.Graphical_Appearance.semObject
    self.obj52.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj52.Graphical_Appearance.semObject

    # name
    self.obj52.name.setValue('directLink_T')

    # displaySelect
    self.obj52.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj52.displaySelect.config = 0

    # attributes
    self.obj52.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('associationType', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj52.attributes.setValue(lcobj2)

    # cardinality
    self.obj52.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj52.cardinality.setValue(lcobj2)

    # display
    self.obj52.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj52.display.setHeight(15)

    # Actions
    self.obj52.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Actions.setValue(lcobj2)

    # Constraints
    self.obj52.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Constraints.setValue(lcobj2)

    self.obj52.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1316.36119942,658.741003922,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.95
       new_obj.layConstraints['scale'] = [1.701, 1.0725806451612903]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=CD_Association3(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # QOCA
    self.obj53.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj53.Graphical_Appearance.setValue( ('apply_contains', self.obj53))
    self.obj53.Graphical_Appearance.linkInfo=linkEditor(self,self.obj53.Graphical_Appearance.semObject, "apply_contains")
    self.obj53.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('apply_contains_1stLink', self.obj53.Graphical_Appearance.linkInfo.FirstLink))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('apply_contains_1stSegment', self.obj53.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj53.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.Center.setValue( ('apply_contains_Center', self.obj53.Graphical_Appearance.linkInfo))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('apply_contains_2ndSegment', self.obj53.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('apply_contains_2ndLink', self.obj53.Graphical_Appearance.linkInfo.SecondLink))
    self.obj53.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.Center.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj53.Graphical_Appearance.semObject
    self.obj53.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj53.Graphical_Appearance.semObject

    # name
    self.obj53.name.setValue('apply_contains')

    # displaySelect
    self.obj53.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj53.displaySelect.config = 0

    # attributes
    self.obj53.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.attributes.setValue(lcobj2)

    # cardinality
    self.obj53.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('ApplyModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj53.cardinality.setValue(lcobj2)

    # display
    self.obj53.display.setValue('Multiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From ApplyModel: 0 to N\n')
    self.obj53.display.setHeight(15)

    # Actions
    self.obj53.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.Actions.setValue(lcobj2)

    # Constraints
    self.obj53.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.Constraints.setValue(lcobj2)

    self.obj53.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(446.046746295,686.241003922,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.729, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=CD_Association3(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # QOCA
    self.obj54.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj54.Graphical_Appearance.setValue( ('indirectLink_S', self.obj54))
    self.obj54.Graphical_Appearance.linkInfo=linkEditor(self,self.obj54.Graphical_Appearance.semObject, "indirectLink_S")
    self.obj54.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('indirectLink_S_1stLink', self.obj54.Graphical_Appearance.linkInfo.FirstLink))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('indirectLink_S_1stSegment', self.obj54.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj54.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.Center.setValue( ('indirectLink_S_Center', self.obj54.Graphical_Appearance.linkInfo))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('indirectLink_S_2ndSegment', self.obj54.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('indirectLink_S_2ndLink', self.obj54.Graphical_Appearance.linkInfo.SecondLink))
    self.obj54.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.Center.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj54.Graphical_Appearance.semObject
    self.obj54.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj54.Graphical_Appearance.semObject

    # name
    self.obj54.name.setValue('indirectLink_S')

    # displaySelect
    self.obj54.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj54.displaySelect.config = 0

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.attributes.setValue(lcobj2)

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj54.cardinality.setValue(lcobj2)

    # display
    self.obj54.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj54.display.setHeight(15)

    # Actions
    self.obj54.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Actions.setValue(lcobj2)

    # Constraints
    self.obj54.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Constraints.setValue(lcobj2)

    self.obj54.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1273.35617001,158.998446721,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.91
       new_obj.layConstraints['scale'] = [1.554, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=CD_Association3(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # QOCA
    self.obj55.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj55.Graphical_Appearance.setValue( ('backward_link', self.obj55))
    self.obj55.Graphical_Appearance.linkInfo=linkEditor(self,self.obj55.Graphical_Appearance.semObject, "backward_link")
    self.obj55.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('backward_link_1stLink', self.obj55.Graphical_Appearance.linkInfo.FirstLink))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('backward_link_1stSegment', self.obj55.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj55.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.Center.setValue( ('backward_link_Center', self.obj55.Graphical_Appearance.linkInfo))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('backward_link_2ndSegment', self.obj55.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('backward_link_2ndLink', self.obj55.Graphical_Appearance.linkInfo.SecondLink))
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.Center.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj55.Graphical_Appearance.semObject

    # name
    self.obj55.name.setValue('backward_link')

    # displaySelect
    self.obj55.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj55.displaySelect.config = 0

    # attributes
    self.obj55.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.attributes.setValue(lcobj2)

    # cardinality
    self.obj55.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj55.cardinality.setValue(lcobj2)

    # display
    self.obj55.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj55.display.setHeight(15)

    # Actions
    self.obj55.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Actions.setValue(lcobj2)

    # Constraints
    self.obj55.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Constraints.setValue(lcobj2)

    self.obj55.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1335.6819269,322.343085977,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=CD_Association3(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # QOCA
    self.obj56.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj56.Graphical_Appearance.setValue( ('trace_link', self.obj56))
    self.obj56.Graphical_Appearance.linkInfo=linkEditor(self,self.obj56.Graphical_Appearance.semObject, "trace_link")
    self.obj56.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('trace_link_1stLink', self.obj56.Graphical_Appearance.linkInfo.FirstLink))
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('trace_link_1stSegment', self.obj56.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj56.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.Center.setValue( ('trace_link_Center', self.obj56.Graphical_Appearance.linkInfo))
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('trace_link_2ndSegment', self.obj56.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('trace_link_2ndLink', self.obj56.Graphical_Appearance.linkInfo.SecondLink))
    self.obj56.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.Center.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj56.Graphical_Appearance.semObject
    self.obj56.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj56.Graphical_Appearance.semObject

    # name
    self.obj56.name.setValue('trace_link')

    # displaySelect
    self.obj56.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj56.displaySelect.config = 0

    # attributes
    self.obj56.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.attributes.setValue(lcobj2)

    # cardinality
    self.obj56.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj56.cardinality.setValue(lcobj2)

    # display
    self.obj56.display.setValue('Multiplicities:\n  - From MetaModelElement_T: 0 to N\n  - To MetaModelElement_S: 0 to N\n')
    self.obj56.display.setHeight(15)

    # Actions
    self.obj56.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Actions.setValue(lcobj2)

    # Constraints
    self.obj56.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Constraints.setValue(lcobj2)

    self.obj56.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1334.0,485.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=CD_Inheritance3(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(545.94511815,232.933238441,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=CD_Inheritance3(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    self.obj58.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(581.0,302.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=CD_Inheritance3(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    self.obj59.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(712.1875,292.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=CD_Inheritance3(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(797.03125,316.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=CD_Inheritance3(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    self.obj61.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(907.33203125,291.868852459,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=CD_Inheritance3(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    self.obj62.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(494.910784314,787.069775845,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=CD_Inheritance3(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    self.obj63.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(599.0,787.515081967,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=CD_Inheritance3(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    self.obj64.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(668.0,779.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=CD_Inheritance3(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    self.obj65.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(803.765625,798.5,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=CD_Inheritance3(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    self.obj66.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(833.0,853.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=CD_Inheritance3(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    self.obj67.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(707.5,852.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=CD_Inheritance3(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    self.obj68.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(559.0,839.295081967,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=CD_Inheritance3(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    self.obj69.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(476.127935606,859.105081967,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=CD_Inheritance3(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    self.obj70.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(549.542878788,925.565,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=CD_Inheritance3(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    self.obj71.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(652.26,925.45,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=CD_Inheritance3(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    self.obj72.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(735.0,926.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=CD_Inheritance3(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    self.obj73.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(857.5,926.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named MatchModel
    self.drawConnections(
(self.obj28,self.obj49,[162.0, 191.0, 153.0, 394.0],"true", 2),
(self.obj28,self.obj50,[237.0, 119.0, 425.3504330872569, 120.20500000000001],"true", 2) )
    # Connections for obj29 (graphObject_: Obj1) named ApplyModel
    self.drawConnections(
(self.obj29,self.obj53,[274.8359375, 690.0, 446.046746295, 686.241003922],"true", 2) )
    # Connections for obj30 (graphObject_: Obj2) named MetaModelElement_S
    self.drawConnections(
(self.obj30,self.obj51,[793.6640625, 125.68852459016392, 1018.3561700079981, 75.74024999999999, 1018.35617001, 75.74025],"true", 3),
(self.obj30,self.obj54,[793.6640625, 166.65573770491804, 1273.3561700079981, 158.99844672131144, 1273.35617001, 158.998446721],"true", 3) )
    # Connections for obj31 (graphObject_: Obj3) named MetaModelElement_T
    self.drawConnections(
(self.obj31,self.obj52,[811.0, 659.9508196721312, 1316.3611994201624, 658.7410039215686, 1316.36119942, 658.741003922],"true", 3),
(self.obj31,self.obj55,[811.0, 659.9508196721312, 1334.0076837951624, 406.61395474124066, 1335.6819269, 322.343085977],"true", 3),
(self.obj31,self.obj56,[811.0, 659.9508196721312, 1132.0, 606.0, 1334.0, 485.0],"true", 3) )
    # Connections for obj32 (graphObject_: Obj4) named ECU
    self.drawConnections(
(self.obj32,self.obj57,[505.0, 251.0, 545.94511815, 232.933238441],"true", 2) )
    # Connections for obj33 (graphObject_: Obj5) named VirtualDevice
    self.drawConnections(
(self.obj33,self.obj58,[456.0, 381.0, 581.0, 302.0],"true", 2) )
    # Connections for obj34 (graphObject_: Obj6) named Distributable
    self.drawConnections(
(self.obj34,self.obj59,[676.0, 381.0, 712.1875, 292.5],"true", 2) )
    # Connections for obj35 (graphObject_: Obj7) named ExecFrame
    self.drawConnections(
(self.obj35,self.obj60,[816.0, 381.0, 797.03125, 316.5],"true", 2) )
    # Connections for obj36 (graphObject_: Obj8) named Signal
    self.drawConnections(
(self.obj36,self.obj61,[941.0, 301.0, 907.33203125, 291.868852459],"true", 2) )
    # Connections for obj37 (graphObject_: Obj9) named System
    self.drawConnections(
(self.obj37,self.obj62,[222.0, 860.0, 494.910784314, 787.069775845],"true", 2) )
    # Connections for obj38 (graphObject_: Obj10) named SystemMapping
    self.drawConnections(
(self.obj38,self.obj63,[427.0, 859.0, 599.0, 787.515081967],"true", 2) )
    # Connections for obj39 (graphObject_: Obj11) named SoftwareComposition
    self.drawConnections(
(self.obj39,self.obj70,[453.75, 1157.0, 549.542878788, 925.565],"true", 2) )
    # Connections for obj40 (graphObject_: Obj12) named CompositionType
    self.drawConnections(
(self.obj40,self.obj71,[654.0, 1157.0, 652.26, 925.45],"true", 2) )
    # Connections for obj41 (graphObject_: Obj13) named ComponentPrototype
    self.drawConnections(
(self.obj41,self.obj69,[318.75, 979.0, 476.127935606, 859.105081967],"true", 2) )
    # Connections for obj42 (graphObject_: Obj14) named PPortPrototype
    self.drawConnections(
(self.obj42,self.obj72,[735.0, 1158.0, 735.0, 926.0],"true", 2) )
    # Connections for obj43 (graphObject_: Obj15) named RPortPrototype
    self.drawConnections(
(self.obj43,self.obj73,[936.0, 1161.0, 857.5, 926.0],"true", 2) )
    # Connections for obj44 (graphObject_: Obj16) named EcuInstance
    self.drawConnections(
(self.obj44,self.obj68,[570.0, 978.0, 559.0, 839.295081967213],"true", 2) )
    # Connections for obj45 (graphObject_: Obj17) named SwcToEcuMapping
    self.drawConnections(
(self.obj45,self.obj64,[611.0, 818.0, 668.0, 779.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj18) named SwCompToEcuMapping_component
    self.drawConnections(
(self.obj46,self.obj65,[985.53125, 858.0, 803.765625, 798.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj19) named PortPrototype
    self.drawConnections(
(self.obj47,self.obj66,[956.0, 978.0, 833.0, 853.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj20) named ComponentType
    self.drawConnections(
(self.obj48,self.obj67,[708.0, 978.0, 707.5, 852.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj21) named paired_with
    self.drawConnections(
(self.obj49,self.obj29,[153.0, 394.0, 150.3125, 622.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj23) named match_contains
    self.drawConnections(
(self.obj50,self.obj30,[425.350433087, 120.205, 600.3984375, 125.68852459016392],"true", 2) )
    # Connections for obj51 (graphObject_: Obj25) named directLink_S
    self.drawConnections(
(self.obj51,self.obj30,[1018.35617001, 75.74025, 1018.3561700079981, 75.74024999999999, 793.6640625, 125.68852459016392],"true", 3) )
    # Connections for obj52 (graphObject_: Obj27) named directLink_T
    self.drawConnections(
(self.obj52,self.obj31,[1316.36119942, 658.741003922, 1316.3611994201624, 658.7410039215686, 811.0, 659.9508196721312],"true", 3) )
    # Connections for obj53 (graphObject_: Obj29) named apply_contains
    self.drawConnections(
(self.obj53,self.obj31,[446.046746295, 686.241003922, 621.0, 692.7245901639344],"true", 2) )
    # Connections for obj54 (graphObject_: Obj31) named indirectLink_S
    self.drawConnections(
(self.obj54,self.obj30,[1273.35617001, 158.998446721, 1273.3561700079981, 158.99844672131144, 793.6640625, 166.65573770491804],"true", 3) )
    # Connections for obj55 (graphObject_: Obj33) named backward_link
    self.drawConnections(
(self.obj55,self.obj30,[1335.6819269, 322.343085977, 1337.3561700079981, 238.0722172131147, 793.6640625, 222.7377049180328],"true", 3) )
    # Connections for obj56 (graphObject_: Obj35) named trace_link
    self.drawConnections(
(self.obj56,self.obj30,[1334.0, 485.0, 1154.0, 328.0, 793.6640625, 222.7377049180328],"true", 3) )
    # Connections for obj57 (graphObject_: Obj37) of type CD_Inheritance3
    self.drawConnections(
(self.obj57,self.obj30,[545.94511815, 232.933238441, 600.3984375, 242.7377049180328],"true", 2) )
    # Connections for obj58 (graphObject_: Obj39) of type CD_Inheritance3
    self.drawConnections(
(self.obj58,self.obj30,[581.0, 302.0, 600.3984375, 242.7377049180328],"true", 2) )
    # Connections for obj59 (graphObject_: Obj41) of type CD_Inheritance3
    self.drawConnections(
(self.obj59,self.obj30,[712.1875, 292.5, 717.375, 272.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj43) of type CD_Inheritance3
    self.drawConnections(
(self.obj60,self.obj30,[797.03125, 316.5, 758.0625, 272.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj45) of type CD_Inheritance3
    self.drawConnections(
(self.obj61,self.obj30,[907.33203125, 291.868852459, 793.6640625, 242.7377049180328],"true", 2) )
    # Connections for obj62 (graphObject_: Obj47) of type CD_Inheritance3
    self.drawConnections(
(self.obj62,self.obj31,[494.910784314, 787.069775845, 621.0, 753.5901639344262],"true", 2) )
    # Connections for obj63 (graphObject_: Obj49) of type CD_Inheritance3
    self.drawConnections(
(self.obj63,self.obj31,[599.0, 787.515081967, 621.0, 753.5901639344262],"true", 2) )
    # Connections for obj64 (graphObject_: Obj51) of type CD_Inheritance3
    self.drawConnections(
(self.obj64,self.obj31,[668.0, 779.0, 656.0, 777.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj53) of type CD_Inheritance3
    self.drawConnections(
(self.obj65,self.obj31,[803.765625, 798.5, 776.0, 777.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj55) of type CD_Inheritance3
    self.drawConnections(
(self.obj66,self.obj31,[833.0, 853.0, 776.0, 777.0],"true", 2) )
    # Connections for obj67 (graphObject_: Obj57) of type CD_Inheritance3
    self.drawConnections(
(self.obj67,self.obj31,[707.5, 852.0, 696.0, 777.0],"true", 2) )
    # Connections for obj68 (graphObject_: Obj59) of type CD_Inheritance3
    self.drawConnections(
(self.obj68,self.obj31,[559.0, 839.295081967, 621.0, 753.5901639344262],"true", 2) )
    # Connections for obj69 (graphObject_: Obj61) of type CD_Inheritance3
    self.drawConnections(
(self.obj69,self.obj31,[476.127935606, 859.105081967, 621.0, 753.5901639344262],"true", 2) )
    # Connections for obj70 (graphObject_: Obj63) of type CD_Inheritance3
    self.drawConnections(
(self.obj70,self.obj31,[549.542878788, 925.565, 656.0, 777.0],"true", 2) )
    # Connections for obj71 (graphObject_: Obj65) of type CD_Inheritance3
    self.drawConnections(
(self.obj71,self.obj31,[652.26, 925.45, 656.0, 777.0],"true", 2) )
    # Connections for obj72 (graphObject_: Obj67) of type CD_Inheritance3
    self.drawConnections(
(self.obj72,self.obj31,[735.0, 926.0, 736.0, 777.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj69) of type CD_Inheritance3
    self.drawConnections(
(self.obj73,self.obj31,[857.5, 926.0, 776.0, 777.0],"true", 2) )

newfunction = GM2AUTOSAR_MM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
