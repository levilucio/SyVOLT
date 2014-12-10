"""
__UMLRT2Kiltera_MM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Sat Aug 30 18:23:38 2014
______________________________________________________________________________
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

def UMLRT2Kiltera_MM_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('UMLRT2Kiltera_MM')

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
       new_obj = graph_CD_Class3(60.0,80.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.1046875, 1.0]
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
       new_obj = graph_CD_Class3(71.03125,1869.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasAttribute_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj30.cardinality.setValue(lcobj2)

    # display
    self.obj30.display.setValue('Attributes:\n  - cardinality :: String\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From match_contains: 0 to N\n  - To directLink_S: 0 to N\n  - From directLink_S: 0 to N\n  - To indirectLink_S: 0 to N\n  - From indirectLink_S: 0 to N\n  - From backward_link: 0 to N\n  - From trace_link: 0 to N\n  - To hasAttribute_S: 0 to N\n')
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
       new_obj = graph_CD_Class3(1400.90625,60.081045082,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.203125, 2.3495901639344265]
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
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
    cobj2.setValue(('apply_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('directLink_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('directLink_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('backward_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('trace_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasAttribute_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj31.cardinality.setValue(lcobj2)

    # display
    self.obj31.display.setValue('Attributes:\n  - cardinality :: String\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From apply_contains: 0 to N\n  - To directLink_T: 0 to N\n  - From directLink_T: 0 to N\n  - To backward_link: 0 to N\n  - To trace_link: 0 to N\n  - To hasAttribute_T: 0 to N\n')
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
       new_obj = graph_CD_Class3(1380.0,1780.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.9881147540983608]
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
    self.obj32.Graphical_Appearance.setValue( ('Element', self.obj32))

    # name
    self.obj32.name.setValue('Element')

    # attributes
    self.obj32.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(340.0,460.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj33.Graphical_Appearance.setValue( ('NamedElement', self.obj33))

    # name
    self.obj33.name.setValue('NamedElement')

    # attributes
    self.obj33.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj33.attributes.setValue(lcobj2)

    # Abstract
    self.obj33.Abstract.setValue((None, 1))
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
       new_obj = graph_CD_Class3(640.0,940.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj34.Graphical_Appearance.setValue( ('Trigger_S', self.obj34))

    # name
    self.obj34.name.setValue('Trigger_S')

    # attributes
    self.obj34.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(140.0,640.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj35.Graphical_Appearance.setValue( ('Action', self.obj35))

    # name
    self.obj35.name.setValue('Action')

    # attributes
    self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(140.0,800.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj36.Graphical_Appearance.setValue( ('PortRef', self.obj36))

    # name
    self.obj36.name.setValue('PortRef')

    # attributes
    self.obj36.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(380.0,660.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj37.Graphical_Appearance.setValue( ('PortConnectorRef', self.obj37))

    # name
    self.obj37.name.setValue('PortConnectorRef')

    # attributes
    self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(340.0,820.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj38.Graphical_Appearance.setValue( ('StateMachineElement', self.obj38))

    # name
    self.obj38.name.setValue('StateMachineElement')

    # attributes
    self.obj38.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj38.attributes.setValue(lcobj2)

    # Abstract
    self.obj38.Abstract.setValue((None, 1))
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
       new_obj = graph_CD_Class3(860.0,1120.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.03125, 1.0]
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
    self.obj39.Graphical_Appearance.setValue( ('Protocol', self.obj39))

    # name
    self.obj39.name.setValue('Protocol')

    # attributes
    self.obj39.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(400.0,1120.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj40.Graphical_Appearance.setValue( ('Signal', self.obj40))

    # name
    self.obj40.name.setValue('Signal')

    # attributes
    self.obj40.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(440.0,1300.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj41.Graphical_Appearance.setValue( ('Port', self.obj41))

    # name
    self.obj41.name.setValue('Port')

    # attributes
    self.obj41.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(640.0,1120.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj42.Graphical_Appearance.setValue( ('Vertex', self.obj42))

    # name
    self.obj42.name.setValue('Vertex')

    # attributes
    self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(720.0,1300.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj43.Graphical_Appearance.setValue( ('InitialPoint', self.obj43))

    # name
    self.obj43.name.setValue('InitialPoint')

    # attributes
    self.obj43.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(700.0,1460.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj44.Graphical_Appearance.setValue( ('EntryPoint', self.obj44))

    # name
    self.obj44.name.setValue('EntryPoint')

    # attributes
    self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(720.0,1640.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj45.Graphical_Appearance.setValue( ('ExitPoint', self.obj45))

    # name
    self.obj45.name.setValue('ExitPoint')

    # attributes
    self.obj45.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(940.0,1640.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj46.Graphical_Appearance.setValue( ('Transition', self.obj46))

    # name
    self.obj46.name.setValue('Transition')

    # attributes
    self.obj46.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(960.0,1300.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj47.Graphical_Appearance.setValue( ('StateMachine', self.obj47))

    # name
    self.obj47.name.setValue('StateMachine')

    # attributes
    self.obj47.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(1200.0,1300.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj48.Graphical_Appearance.setValue( ('State', self.obj48))

    # name
    self.obj48.name.setValue('State')

    # attributes
    self.obj48.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
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
       new_obj = graph_CD_Class3(1000.0,1480.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=CD_Class3(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # QOCA
    self.obj49.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj49.Graphical_Appearance.setValue( ('Capsule', self.obj49))

    # name
    self.obj49.name.setValue('Capsule')

    # attributes
    self.obj49.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj49.attributes.setValue(lcobj2)

    # Abstract
    self.obj49.Abstract.setValue((None, 0))
    self.obj49.Abstract.config = 0

    # cardinality
    self.obj49.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj49.cardinality.setValue(lcobj2)

    # display
    self.obj49.display.setValue('Attributes:\n')
    self.obj49.display.setHeight(15)

    # Actions
    self.obj49.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.Actions.setValue(lcobj2)

    # Constraints
    self.obj49.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.Constraints.setValue(lcobj2)

    self.obj49.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1620.0,1300.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=CD_Class3(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # QOCA
    self.obj50.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj50.Graphical_Appearance.setValue( ('PackageContainer', self.obj50))

    # name
    self.obj50.name.setValue('PackageContainer')

    # attributes
    self.obj50.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj50.attributes.setValue(lcobj2)

    # Abstract
    self.obj50.Abstract.setValue((None, 1))
    self.obj50.Abstract.config = 0

    # cardinality
    self.obj50.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj50.cardinality.setValue(lcobj2)

    # display
    self.obj50.display.setValue('Attributes:\n')
    self.obj50.display.setHeight(15)

    # Actions
    self.obj50.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.Actions.setValue(lcobj2)

    # Constraints
    self.obj50.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj50.Constraints.setValue(lcobj2)

    self.obj50.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1420.0,1300.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=CD_Class3(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # QOCA
    self.obj51.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj51.Graphical_Appearance.setValue( ('Model_S', self.obj51))

    # name
    self.obj51.name.setValue('Model_S')

    # attributes
    self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj51.attributes.setValue(lcobj2)

    # Abstract
    self.obj51.Abstract.setValue((None, 0))
    self.obj51.Abstract.config = 0

    # cardinality
    self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj51.cardinality.setValue(lcobj2)

    # display
    self.obj51.display.setValue('Attributes:\n')
    self.obj51.display.setHeight(15)

    # Actions
    self.obj51.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Actions.setValue(lcobj2)

    # Constraints
    self.obj51.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj51.Constraints.setValue(lcobj2)

    self.obj51.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1260.0,1480.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=CD_Class3(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # QOCA
    self.obj52.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj52.Graphical_Appearance.setValue( ('Package', self.obj52))

    # name
    self.obj52.name.setValue('Package')

    # attributes
    self.obj52.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj52.attributes.setValue(lcobj2)

    # Abstract
    self.obj52.Abstract.setValue((None, 0))
    self.obj52.Abstract.config = 0

    # cardinality
    self.obj52.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj52.cardinality.setValue(lcobj2)

    # display
    self.obj52.display.setValue('Attributes:\n')
    self.obj52.display.setHeight(15)

    # Actions
    self.obj52.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Actions.setValue(lcobj2)

    # Constraints
    self.obj52.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.Constraints.setValue(lcobj2)

    self.obj52.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1500.0,1480.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=CD_Class3(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # QOCA
    self.obj53.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj53.Graphical_Appearance.setValue( ('CapsuleRole', self.obj53))

    # name
    self.obj53.name.setValue('CapsuleRole')

    # attributes
    self.obj53.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj53.attributes.setValue(lcobj2)

    # Abstract
    self.obj53.Abstract.setValue((None, 0))
    self.obj53.Abstract.config = 0

    # cardinality
    self.obj53.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj53.cardinality.setValue(lcobj2)

    # display
    self.obj53.display.setValue('Attributes:\n')
    self.obj53.display.setHeight(15)

    # Actions
    self.obj53.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.Actions.setValue(lcobj2)

    # Constraints
    self.obj53.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.Constraints.setValue(lcobj2)

    self.obj53.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1820.0,1300.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=CD_Class3(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # QOCA
    self.obj54.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj54.Graphical_Appearance.setValue( ('PortConnector', self.obj54))

    # name
    self.obj54.name.setValue('PortConnector')

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj54.attributes.setValue(lcobj2)

    # Abstract
    self.obj54.Abstract.setValue((None, 0))
    self.obj54.Abstract.config = 0

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj54.cardinality.setValue(lcobj2)

    # display
    self.obj54.display.setValue('Attributes:\n')
    self.obj54.display.setHeight(15)

    # Actions
    self.obj54.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Actions.setValue(lcobj2)

    # Constraints
    self.obj54.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Constraints.setValue(lcobj2)

    self.obj54.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2020.0,1300.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=CD_Class3(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # QOCA
    self.obj55.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj55.Graphical_Appearance.setValue( ('Thread', self.obj55))

    # name
    self.obj55.name.setValue('Thread')

    # attributes
    self.obj55.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj55.attributes.setValue(lcobj2)

    # Abstract
    self.obj55.Abstract.setValue((None, 1))
    self.obj55.Abstract.config = 0

    # cardinality
    self.obj55.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj55.cardinality.setValue(lcobj2)

    # display
    self.obj55.display.setValue('Attributes:\n')
    self.obj55.display.setHeight(15)

    # Actions
    self.obj55.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Actions.setValue(lcobj2)

    # Constraints
    self.obj55.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Constraints.setValue(lcobj2)

    self.obj55.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2240.0,1300.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=CD_Class3(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # QOCA
    self.obj56.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj56.Graphical_Appearance.setValue( ('PhysicalThread', self.obj56))

    # name
    self.obj56.name.setValue('PhysicalThread')

    # attributes
    self.obj56.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj56.attributes.setValue(lcobj2)

    # Abstract
    self.obj56.Abstract.setValue((None, 0))
    self.obj56.Abstract.config = 0

    # cardinality
    self.obj56.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj56.cardinality.setValue(lcobj2)

    # display
    self.obj56.display.setValue('Attributes:\n')
    self.obj56.display.setHeight(15)

    # Actions
    self.obj56.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Actions.setValue(lcobj2)

    # Constraints
    self.obj56.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Constraints.setValue(lcobj2)

    self.obj56.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2020.0,1480.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=CD_Class3(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # QOCA
    self.obj57.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj57.Graphical_Appearance.setValue( ('LogicalThread', self.obj57))

    # name
    self.obj57.name.setValue('LogicalThread')

    # attributes
    self.obj57.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj57.attributes.setValue(lcobj2)

    # Abstract
    self.obj57.Abstract.setValue((None, 0))
    self.obj57.Abstract.config = 0

    # cardinality
    self.obj57.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj57.cardinality.setValue(lcobj2)

    # display
    self.obj57.display.setValue('Attributes:\n')
    self.obj57.display.setHeight(15)

    # Actions
    self.obj57.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj57.Actions.setValue(lcobj2)

    # Constraints
    self.obj57.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj57.Constraints.setValue(lcobj2)

    self.obj57.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2260.0,1480.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=CD_Class3(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # QOCA
    self.obj58.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj58.Graphical_Appearance.setValue( ('PortType', self.obj58))

    # name
    self.obj58.name.setValue('PortType')

    # attributes
    self.obj58.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj58.attributes.setValue(lcobj2)

    # Abstract
    self.obj58.Abstract.setValue((None, 1))
    self.obj58.Abstract.config = 0

    # cardinality
    self.obj58.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj58.cardinality.setValue(lcobj2)

    # display
    self.obj58.display.setValue('Attributes:\n')
    self.obj58.display.setHeight(15)

    # Actions
    self.obj58.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj58.Actions.setValue(lcobj2)

    # Constraints
    self.obj58.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj58.Constraints.setValue(lcobj2)

    self.obj58.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,360.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=CD_Class3(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # QOCA
    self.obj59.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj59.Graphical_Appearance.setValue( ('BASE0', self.obj59))

    # name
    self.obj59.name.setValue('BASE0')

    # attributes
    self.obj59.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj59.attributes.setValue(lcobj2)

    # Abstract
    self.obj59.Abstract.setValue((None, 0))
    self.obj59.Abstract.config = 0

    # cardinality
    self.obj59.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj59.cardinality.setValue(lcobj2)

    # display
    self.obj59.display.setValue('Attributes:\n')
    self.obj59.display.setHeight(15)

    # Actions
    self.obj59.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj59.Actions.setValue(lcobj2)

    # Constraints
    self.obj59.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj59.Constraints.setValue(lcobj2)

    self.obj59.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(580.0,520.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=CD_Class3(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # QOCA
    self.obj60.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj60.Graphical_Appearance.setValue( ('CONJUGATE1', self.obj60))

    # name
    self.obj60.name.setValue('CONJUGATE1')

    # attributes
    self.obj60.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj60.attributes.setValue(lcobj2)

    # Abstract
    self.obj60.Abstract.setValue((None, 0))
    self.obj60.Abstract.config = 0

    # cardinality
    self.obj60.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj60.cardinality.setValue(lcobj2)

    # display
    self.obj60.display.setValue('Attributes:\n')
    self.obj60.display.setHeight(15)

    # Actions
    self.obj60.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj60.Actions.setValue(lcobj2)

    # Constraints
    self.obj60.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj60.Constraints.setValue(lcobj2)

    self.obj60.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(613.0,680.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=CD_Class3(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # QOCA
    self.obj61.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj61.Graphical_Appearance.setValue( ('SignalType', self.obj61))

    # name
    self.obj61.name.setValue('SignalType')

    # attributes
    self.obj61.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj61.attributes.setValue(lcobj2)

    # Abstract
    self.obj61.Abstract.setValue((None, 1))
    self.obj61.Abstract.config = 0

    # cardinality
    self.obj61.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj61.cardinality.setValue(lcobj2)

    # display
    self.obj61.display.setValue('Attributes:\n')
    self.obj61.display.setHeight(15)

    # Actions
    self.obj61.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj61.Actions.setValue(lcobj2)

    # Constraints
    self.obj61.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj61.Constraints.setValue(lcobj2)

    self.obj61.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(860.0,360.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=CD_Class3(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # QOCA
    self.obj62.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj62.Graphical_Appearance.setValue( ('OUT1', self.obj62))

    # name
    self.obj62.name.setValue('OUT1')

    # attributes
    self.obj62.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj62.attributes.setValue(lcobj2)

    # Abstract
    self.obj62.Abstract.setValue((None, 0))
    self.obj62.Abstract.config = 0

    # cardinality
    self.obj62.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj62.cardinality.setValue(lcobj2)

    # display
    self.obj62.display.setValue('Attributes:\n')
    self.obj62.display.setHeight(15)

    # Actions
    self.obj62.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj62.Actions.setValue(lcobj2)

    # Constraints
    self.obj62.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj62.Constraints.setValue(lcobj2)

    self.obj62.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(860.0,680.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=CD_Class3(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # QOCA
    self.obj63.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj63.Graphical_Appearance.setValue( ('IN0', self.obj63))

    # name
    self.obj63.name.setValue('IN0')

    # attributes
    self.obj63.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj63.attributes.setValue(lcobj2)

    # Abstract
    self.obj63.Abstract.setValue((None, 0))
    self.obj63.Abstract.config = 0

    # cardinality
    self.obj63.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj63.cardinality.setValue(lcobj2)

    # display
    self.obj63.display.setValue('Attributes:\n')
    self.obj63.display.setHeight(15)

    # Actions
    self.obj63.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj63.Actions.setValue(lcobj2)

    # Constraints
    self.obj63.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj63.Constraints.setValue(lcobj2)

    self.obj63.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(820.0,520.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=CD_Class3(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # QOCA
    self.obj64.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj64.Graphical_Appearance.setValue( ('RoleType', self.obj64))

    # name
    self.obj64.name.setValue('RoleType')

    # attributes
    self.obj64.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj64.attributes.setValue(lcobj2)

    # Abstract
    self.obj64.Abstract.setValue((None, 1))
    self.obj64.Abstract.config = 0

    # cardinality
    self.obj64.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj64.cardinality.setValue(lcobj2)

    # display
    self.obj64.display.setValue('Attributes:\n')
    self.obj64.display.setHeight(15)

    # Actions
    self.obj64.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj64.Actions.setValue(lcobj2)

    # Constraints
    self.obj64.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj64.Constraints.setValue(lcobj2)

    self.obj64.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1080.0,360.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=CD_Class3(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # QOCA
    self.obj65.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj65.Graphical_Appearance.setValue( ('FIXED0', self.obj65))

    # name
    self.obj65.name.setValue('FIXED0')

    # attributes
    self.obj65.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj65.attributes.setValue(lcobj2)

    # Abstract
    self.obj65.Abstract.setValue((None, 0))
    self.obj65.Abstract.config = 0

    # cardinality
    self.obj65.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj65.cardinality.setValue(lcobj2)

    # display
    self.obj65.display.setValue('Attributes:\n')
    self.obj65.display.setHeight(15)

    # Actions
    self.obj65.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj65.Actions.setValue(lcobj2)

    # Constraints
    self.obj65.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj65.Constraints.setValue(lcobj2)

    self.obj65.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1040.0,520.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=CD_Class3(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # QOCA
    self.obj66.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj66.Graphical_Appearance.setValue( ('OPTIONAL1', self.obj66))

    # name
    self.obj66.name.setValue('OPTIONAL1')

    # attributes
    self.obj66.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj66.attributes.setValue(lcobj2)

    # Abstract
    self.obj66.Abstract.setValue((None, 0))
    self.obj66.Abstract.config = 0

    # cardinality
    self.obj66.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj66.cardinality.setValue(lcobj2)

    # display
    self.obj66.display.setValue('Attributes:\n')
    self.obj66.display.setHeight(15)

    # Actions
    self.obj66.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj66.Actions.setValue(lcobj2)

    # Constraints
    self.obj66.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj66.Constraints.setValue(lcobj2)

    self.obj66.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1080.0,680.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=CD_Class3(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # QOCA
    self.obj67.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj67.Graphical_Appearance.setValue( ('PLUGIN2', self.obj67))

    # name
    self.obj67.name.setValue('PLUGIN2')

    # attributes
    self.obj67.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj67.attributes.setValue(lcobj2)

    # Abstract
    self.obj67.Abstract.setValue((None, 0))
    self.obj67.Abstract.config = 0

    # cardinality
    self.obj67.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj67.cardinality.setValue(lcobj2)

    # display
    self.obj67.display.setValue('Attributes:\n')
    self.obj67.display.setHeight(15)

    # Actions
    self.obj67.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj67.Actions.setValue(lcobj2)

    # Constraints
    self.obj67.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj67.Constraints.setValue(lcobj2)

    self.obj67.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1100.0,840.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=CD_Class3(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # QOCA
    self.obj68.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj68.Graphical_Appearance.setValue( ('TransitionType', self.obj68))

    # name
    self.obj68.name.setValue('TransitionType')

    # attributes
    self.obj68.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj68.attributes.setValue(lcobj2)

    # Abstract
    self.obj68.Abstract.setValue((None, 1))
    self.obj68.Abstract.config = 0

    # cardinality
    self.obj68.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj68.cardinality.setValue(lcobj2)

    # display
    self.obj68.display.setValue('Attributes:\n')
    self.obj68.display.setHeight(15)

    # Actions
    self.obj68.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj68.Actions.setValue(lcobj2)

    # Constraints
    self.obj68.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj68.Constraints.setValue(lcobj2)

    self.obj68.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1380.0,400.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=CD_Class3(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # QOCA
    self.obj69.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj69.Graphical_Appearance.setValue( ('SIBLING0', self.obj69))

    # name
    self.obj69.name.setValue('SIBLING0')

    # attributes
    self.obj69.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj69.attributes.setValue(lcobj2)

    # Abstract
    self.obj69.Abstract.setValue((None, 0))
    self.obj69.Abstract.config = 0

    # cardinality
    self.obj69.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj69.cardinality.setValue(lcobj2)

    # display
    self.obj69.display.setValue('Attributes:\n')
    self.obj69.display.setHeight(15)

    # Actions
    self.obj69.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.Actions.setValue(lcobj2)

    # Constraints
    self.obj69.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.Constraints.setValue(lcobj2)

    self.obj69.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1300.0,560.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=CD_Class3(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # QOCA
    self.obj70.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj70.Graphical_Appearance.setValue( ('IN1', self.obj70))

    # name
    self.obj70.name.setValue('IN1')

    # attributes
    self.obj70.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj70.attributes.setValue(lcobj2)

    # Abstract
    self.obj70.Abstract.setValue((None, 0))
    self.obj70.Abstract.config = 0

    # cardinality
    self.obj70.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj70.cardinality.setValue(lcobj2)

    # display
    self.obj70.display.setValue('Attributes:\n')
    self.obj70.display.setHeight(15)

    # Actions
    self.obj70.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj70.Actions.setValue(lcobj2)

    # Constraints
    self.obj70.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj70.Constraints.setValue(lcobj2)

    self.obj70.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1340.0,720.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=CD_Class3(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # QOCA
    self.obj71.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj71.Graphical_Appearance.setValue( ('OUT2', self.obj71))

    # name
    self.obj71.name.setValue('OUT2')

    # attributes
    self.obj71.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj71.attributes.setValue(lcobj2)

    # Abstract
    self.obj71.Abstract.setValue((None, 0))
    self.obj71.Abstract.config = 0

    # cardinality
    self.obj71.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj71.cardinality.setValue(lcobj2)

    # display
    self.obj71.display.setValue('Attributes:\n')
    self.obj71.display.setHeight(15)

    # Actions
    self.obj71.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj71.Actions.setValue(lcobj2)

    # Constraints
    self.obj71.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj71.Constraints.setValue(lcobj2)

    self.obj71.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1400.0,880.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=CD_Class3(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # QOCA
    self.obj72.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj72.Graphical_Appearance.setValue( ('Def', self.obj72))

    # name
    self.obj72.name.setValue('Def')

    # attributes
    self.obj72.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj72.attributes.setValue(lcobj2)

    # Abstract
    self.obj72.Abstract.setValue((None, 1))
    self.obj72.Abstract.config = 0

    # cardinality
    self.obj72.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj72.cardinality.setValue(lcobj2)

    # display
    self.obj72.display.setValue('Attributes:\n')
    self.obj72.display.setHeight(15)

    # Actions
    self.obj72.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj72.Actions.setValue(lcobj2)

    # Constraints
    self.obj72.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj72.Constraints.setValue(lcobj2)

    self.obj72.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(100.0,2080.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=CD_Class3(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # QOCA
    self.obj73.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj73.Graphical_Appearance.setValue( ('Expr', self.obj73))

    # name
    self.obj73.name.setValue('Expr')

    # attributes
    self.obj73.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj73.attributes.setValue(lcobj2)

    # Abstract
    self.obj73.Abstract.setValue((None, 0))
    self.obj73.Abstract.config = 0

    # cardinality
    self.obj73.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj73.cardinality.setValue(lcobj2)

    # display
    self.obj73.display.setValue('Attributes:\n')
    self.obj73.display.setHeight(15)

    # Actions
    self.obj73.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj73.Actions.setValue(lcobj2)

    # Constraints
    self.obj73.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj73.Constraints.setValue(lcobj2)

    self.obj73.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(320.0,2080.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=CD_Class3(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # QOCA
    self.obj74.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj74.Graphical_Appearance.setValue( ('Pattern', self.obj74))

    # name
    self.obj74.name.setValue('Pattern')

    # attributes
    self.obj74.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj74.attributes.setValue(lcobj2)

    # Abstract
    self.obj74.Abstract.setValue((None, 0))
    self.obj74.Abstract.config = 0

    # cardinality
    self.obj74.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj74.cardinality.setValue(lcobj2)

    # display
    self.obj74.display.setValue('Attributes:\n')
    self.obj74.display.setHeight(15)

    # Actions
    self.obj74.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj74.Actions.setValue(lcobj2)

    # Constraints
    self.obj74.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj74.Constraints.setValue(lcobj2)

    self.obj74.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,2080.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=CD_Class3(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # QOCA
    self.obj75.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj75.Graphical_Appearance.setValue( ('Proc', self.obj75))

    # name
    self.obj75.name.setValue('Proc')

    # attributes
    self.obj75.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj75.attributes.setValue(lcobj2)

    # Abstract
    self.obj75.Abstract.setValue((None, 1))
    self.obj75.Abstract.config = 0

    # cardinality
    self.obj75.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj75.cardinality.setValue(lcobj2)

    # display
    self.obj75.display.setValue('Attributes:\n')
    self.obj75.display.setHeight(15)

    # Actions
    self.obj75.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj75.Actions.setValue(lcobj2)

    # Constraints
    self.obj75.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj75.Constraints.setValue(lcobj2)

    self.obj75.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1940.0,2080.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=CD_Class3(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # QOCA
    self.obj76.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj76.Graphical_Appearance.setValue( ('ProcDef', self.obj76))

    # name
    self.obj76.name.setValue('ProcDef')

    # attributes
    self.obj76.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj76.attributes.setValue(lcobj2)

    # Abstract
    self.obj76.Abstract.setValue((None, 0))
    self.obj76.Abstract.config = 0

    # cardinality
    self.obj76.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj76.cardinality.setValue(lcobj2)

    # display
    self.obj76.display.setValue('Attributes:\n')
    self.obj76.display.setHeight(15)

    # Actions
    self.obj76.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj76.Actions.setValue(lcobj2)

    # Constraints
    self.obj76.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj76.Constraints.setValue(lcobj2)

    self.obj76.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(15.0,2260.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=CD_Class3(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # QOCA
    self.obj77.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj77.Graphical_Appearance.setValue( ('FuncDef', self.obj77))

    # name
    self.obj77.name.setValue('FuncDef')

    # attributes
    self.obj77.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj77.attributes.setValue(lcobj2)

    # Abstract
    self.obj77.Abstract.setValue((None, 0))
    self.obj77.Abstract.config = 0

    # cardinality
    self.obj77.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj77.cardinality.setValue(lcobj2)

    # display
    self.obj77.display.setValue('Attributes:\n')
    self.obj77.display.setHeight(15)

    # Actions
    self.obj77.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj77.Actions.setValue(lcobj2)

    # Constraints
    self.obj77.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj77.Constraints.setValue(lcobj2)

    self.obj77.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(60.0,2600.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=CD_Class3(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # QOCA
    self.obj78.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj78.Graphical_Appearance.setValue( ('Name', self.obj78))

    # name
    self.obj78.name.setValue('Name')

    # attributes
    self.obj78.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj78.attributes.setValue(lcobj2)

    # Abstract
    self.obj78.Abstract.setValue((None, 0))
    self.obj78.Abstract.config = 0

    # cardinality
    self.obj78.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj78.cardinality.setValue(lcobj2)

    # display
    self.obj78.display.setValue('Attributes:\n')
    self.obj78.display.setHeight(15)

    # Actions
    self.obj78.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj78.Actions.setValue(lcobj2)

    # Constraints
    self.obj78.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj78.Constraints.setValue(lcobj2)

    self.obj78.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,2080.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=CD_Class3(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # QOCA
    self.obj79.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj79.Graphical_Appearance.setValue( ('PythonRef', self.obj79))

    # name
    self.obj79.name.setValue('PythonRef')

    # attributes
    self.obj79.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj79.attributes.setValue(lcobj2)

    # Abstract
    self.obj79.Abstract.setValue((None, 0))
    self.obj79.Abstract.config = 0

    # cardinality
    self.obj79.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj79.cardinality.setValue(lcobj2)

    # display
    self.obj79.display.setValue('Attributes:\n')
    self.obj79.display.setHeight(15)

    # Actions
    self.obj79.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj79.Actions.setValue(lcobj2)

    # Constraints
    self.obj79.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj79.Constraints.setValue(lcobj2)

    self.obj79.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,2260.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=CD_Class3(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # QOCA
    self.obj80.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj80.Graphical_Appearance.setValue( ('Module', self.obj80))

    # name
    self.obj80.name.setValue('Module')

    # attributes
    self.obj80.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj80.attributes.setValue(lcobj2)

    # Abstract
    self.obj80.Abstract.setValue((None, 0))
    self.obj80.Abstract.config = 0

    # cardinality
    self.obj80.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj80.cardinality.setValue(lcobj2)

    # display
    self.obj80.display.setValue('Attributes:\n')
    self.obj80.display.setHeight(15)

    # Actions
    self.obj80.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj80.Actions.setValue(lcobj2)

    # Constraints
    self.obj80.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj80.Constraints.setValue(lcobj2)

    self.obj80.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,2440.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=CD_Class3(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # QOCA
    self.obj81.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj81.Graphical_Appearance.setValue( ('Null', self.obj81))

    # name
    self.obj81.name.setValue('Null')

    # attributes
    self.obj81.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj81.attributes.setValue(lcobj2)

    # Abstract
    self.obj81.Abstract.setValue((None, 0))
    self.obj81.Abstract.config = 0

    # cardinality
    self.obj81.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj81.cardinality.setValue(lcobj2)

    # display
    self.obj81.display.setValue('Attributes:\n')
    self.obj81.display.setHeight(15)

    # Actions
    self.obj81.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj81.Actions.setValue(lcobj2)

    # Constraints
    self.obj81.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj81.Constraints.setValue(lcobj2)

    self.obj81.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1820.0,2260.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=CD_Class3(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # QOCA
    self.obj82.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj82.Graphical_Appearance.setValue( ('Trigger_T', self.obj82))

    # name
    self.obj82.name.setValue('Trigger_T')

    # attributes
    self.obj82.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj82.attributes.setValue(lcobj2)

    # Abstract
    self.obj82.Abstract.setValue((None, 0))
    self.obj82.Abstract.config = 0

    # cardinality
    self.obj82.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj82.cardinality.setValue(lcobj2)

    # display
    self.obj82.display.setValue('Attributes:\n')
    self.obj82.display.setHeight(15)

    # Actions
    self.obj82.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj82.Actions.setValue(lcobj2)

    # Constraints
    self.obj82.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj82.Constraints.setValue(lcobj2)

    self.obj82.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2040.0,2260.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=CD_Class3(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # QOCA
    self.obj83.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj83.Graphical_Appearance.setValue( ('Listen', self.obj83))

    # name
    self.obj83.name.setValue('Listen')

    # attributes
    self.obj83.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj83.attributes.setValue(lcobj2)

    # Abstract
    self.obj83.Abstract.setValue((None, 0))
    self.obj83.Abstract.config = 0

    # cardinality
    self.obj83.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj83.cardinality.setValue(lcobj2)

    # display
    self.obj83.display.setValue('Attributes:\n')
    self.obj83.display.setHeight(15)

    # Actions
    self.obj83.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj83.Actions.setValue(lcobj2)

    # Constraints
    self.obj83.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj83.Constraints.setValue(lcobj2)

    self.obj83.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2260.0,2260.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=CD_Class3(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # QOCA
    self.obj84.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj84.Graphical_Appearance.setValue( ('ConditionBranch', self.obj84))

    # name
    self.obj84.name.setValue('ConditionBranch')

    # attributes
    self.obj84.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj84.attributes.setValue(lcobj2)

    # Abstract
    self.obj84.Abstract.setValue((None, 0))
    self.obj84.Abstract.config = 0

    # cardinality
    self.obj84.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj84.cardinality.setValue(lcobj2)

    # display
    self.obj84.display.setValue('Attributes:\n')
    self.obj84.display.setHeight(15)

    # Actions
    self.obj84.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj84.Actions.setValue(lcobj2)

    # Constraints
    self.obj84.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj84.Constraints.setValue(lcobj2)

    self.obj84.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1740.0,2080.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=CD_Class3(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # QOCA
    self.obj85.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj85.Graphical_Appearance.setValue( ('ListenBranch', self.obj85))

    # name
    self.obj85.name.setValue('ListenBranch')

    # attributes
    self.obj85.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj85.attributes.setValue(lcobj2)

    # Abstract
    self.obj85.Abstract.setValue((None, 0))
    self.obj85.Abstract.config = 0

    # cardinality
    self.obj85.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj85.cardinality.setValue(lcobj2)

    # display
    self.obj85.display.setValue('Attributes:\n')
    self.obj85.display.setHeight(15)

    # Actions
    self.obj85.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj85.Actions.setValue(lcobj2)

    # Constraints
    self.obj85.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj85.Constraints.setValue(lcobj2)

    self.obj85.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(940.0,2080.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=CD_Class3(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # QOCA
    self.obj86.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj86.Graphical_Appearance.setValue( ('Site', self.obj86))

    # name
    self.obj86.name.setValue('Site')

    # attributes
    self.obj86.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj86.attributes.setValue(lcobj2)

    # Abstract
    self.obj86.Abstract.setValue((None, 0))
    self.obj86.Abstract.config = 0

    # cardinality
    self.obj86.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj86.cardinality.setValue(lcobj2)

    # display
    self.obj86.display.setValue('Attributes:\n')
    self.obj86.display.setHeight(15)

    # Actions
    self.obj86.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj86.Actions.setValue(lcobj2)

    # Constraints
    self.obj86.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj86.Constraints.setValue(lcobj2)

    self.obj86.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1140.0,2080.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=CD_Class3(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # QOCA
    self.obj87.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj87.Graphical_Appearance.setValue( ('Model_T', self.obj87))

    # name
    self.obj87.name.setValue('Model_T')

    # attributes
    self.obj87.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj87.attributes.setValue(lcobj2)

    # Abstract
    self.obj87.Abstract.setValue((None, 0))
    self.obj87.Abstract.config = 0

    # cardinality
    self.obj87.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj87.cardinality.setValue(lcobj2)

    # display
    self.obj87.display.setValue('Attributes:\n')
    self.obj87.display.setHeight(15)

    # Actions
    self.obj87.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj87.Actions.setValue(lcobj2)

    # Constraints
    self.obj87.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj87.Constraints.setValue(lcobj2)

    self.obj87.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1340.0,2080.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=CD_Class3(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # QOCA
    self.obj88.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj88.Graphical_Appearance.setValue( ('MatchCase', self.obj88))

    # name
    self.obj88.name.setValue('MatchCase')

    # attributes
    self.obj88.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj88.attributes.setValue(lcobj2)

    # Abstract
    self.obj88.Abstract.setValue((None, 0))
    self.obj88.Abstract.config = 0

    # cardinality
    self.obj88.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj88.cardinality.setValue(lcobj2)

    # display
    self.obj88.display.setValue('Attributes:\n')
    self.obj88.display.setHeight(15)

    # Actions
    self.obj88.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj88.Actions.setValue(lcobj2)

    # Constraints
    self.obj88.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj88.Constraints.setValue(lcobj2)

    self.obj88.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1540.0,2080.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=CD_Class3(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # QOCA
    self.obj89.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj89.Graphical_Appearance.setValue( ('Condition', self.obj89))

    # name
    self.obj89.name.setValue('Condition')

    # attributes
    self.obj89.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj89.attributes.setValue(lcobj2)

    # Abstract
    self.obj89.Abstract.setValue((None, 0))
    self.obj89.Abstract.config = 0

    # cardinality
    self.obj89.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj89.cardinality.setValue(lcobj2)

    # display
    self.obj89.display.setValue('Attributes:\n')
    self.obj89.display.setHeight(15)

    # Actions
    self.obj89.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj89.Actions.setValue(lcobj2)

    # Constraints
    self.obj89.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj89.Constraints.setValue(lcobj2)

    self.obj89.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1620.0,2260.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=CD_Class3(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # QOCA
    self.obj90.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj90.Graphical_Appearance.setValue( ('New', self.obj90))

    # name
    self.obj90.name.setValue('New')

    # attributes
    self.obj90.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj90.attributes.setValue(lcobj2)

    # Abstract
    self.obj90.Abstract.setValue((None, 0))
    self.obj90.Abstract.config = 0

    # cardinality
    self.obj90.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj90.cardinality.setValue(lcobj2)

    # display
    self.obj90.display.setValue('Attributes:\n')
    self.obj90.display.setHeight(15)

    # Actions
    self.obj90.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj90.Actions.setValue(lcobj2)

    # Constraints
    self.obj90.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj90.Constraints.setValue(lcobj2)

    self.obj90.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2480.0,2260.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=CD_Class3(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # QOCA
    self.obj91.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj91.Graphical_Appearance.setValue( ('Delay', self.obj91))

    # name
    self.obj91.name.setValue('Delay')

    # attributes
    self.obj91.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj91.attributes.setValue(lcobj2)

    # Abstract
    self.obj91.Abstract.setValue((None, 0))
    self.obj91.Abstract.config = 0

    # cardinality
    self.obj91.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj91.cardinality.setValue(lcobj2)

    # display
    self.obj91.display.setValue('Attributes:\n')
    self.obj91.display.setHeight(15)

    # Actions
    self.obj91.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj91.Actions.setValue(lcobj2)

    # Constraints
    self.obj91.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj91.Constraints.setValue(lcobj2)

    self.obj91.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2680.0,2260.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=CD_Class3(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # QOCA
    self.obj92.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj92.Graphical_Appearance.setValue( ('Par', self.obj92))

    # name
    self.obj92.name.setValue('Par')

    # attributes
    self.obj92.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj92.attributes.setValue(lcobj2)

    # Abstract
    self.obj92.Abstract.setValue((None, 0))
    self.obj92.Abstract.config = 0

    # cardinality
    self.obj92.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj92.cardinality.setValue(lcobj2)

    # display
    self.obj92.display.setValue('Attributes:\n')
    self.obj92.display.setHeight(15)

    # Actions
    self.obj92.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj92.Actions.setValue(lcobj2)

    # Constraints
    self.obj92.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj92.Constraints.setValue(lcobj2)

    self.obj92.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1820.0,2440.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=CD_Class3(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # QOCA
    self.obj93.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj93.Graphical_Appearance.setValue( ('ParIndexed', self.obj93))

    # name
    self.obj93.name.setValue('ParIndexed')

    # attributes
    self.obj93.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj93.attributes.setValue(lcobj2)

    # Abstract
    self.obj93.Abstract.setValue((None, 0))
    self.obj93.Abstract.config = 0

    # cardinality
    self.obj93.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj93.cardinality.setValue(lcobj2)

    # display
    self.obj93.display.setValue('Attributes:\n')
    self.obj93.display.setHeight(15)

    # Actions
    self.obj93.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj93.Actions.setValue(lcobj2)

    # Constraints
    self.obj93.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj93.Constraints.setValue(lcobj2)

    self.obj93.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2040.0,2440.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=CD_Class3(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # QOCA
    self.obj94.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj94.Graphical_Appearance.setValue( ('Inst', self.obj94))

    # name
    self.obj94.name.setValue('Inst')

    # attributes
    self.obj94.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj94.attributes.setValue(lcobj2)

    # Abstract
    self.obj94.Abstract.setValue((None, 0))
    self.obj94.Abstract.config = 0

    # cardinality
    self.obj94.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj94.cardinality.setValue(lcobj2)

    # display
    self.obj94.display.setValue('Attributes:\n')
    self.obj94.display.setHeight(15)

    # Actions
    self.obj94.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj94.Actions.setValue(lcobj2)

    # Constraints
    self.obj94.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj94.Constraints.setValue(lcobj2)

    self.obj94.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2240.0,2440.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=CD_Class3(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # QOCA
    self.obj95.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj95.Graphical_Appearance.setValue( ('LocalDef', self.obj95))

    # name
    self.obj95.name.setValue('LocalDef')

    # attributes
    self.obj95.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj95.attributes.setValue(lcobj2)

    # Abstract
    self.obj95.Abstract.setValue((None, 0))
    self.obj95.Abstract.config = 0

    # cardinality
    self.obj95.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj95.cardinality.setValue(lcobj2)

    # display
    self.obj95.display.setValue('Attributes:\n')
    self.obj95.display.setHeight(15)

    # Actions
    self.obj95.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj95.Actions.setValue(lcobj2)

    # Constraints
    self.obj95.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj95.Constraints.setValue(lcobj2)

    self.obj95.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2440.0,2440.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=CD_Class3(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # QOCA
    self.obj96.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj96.Graphical_Appearance.setValue( ('Seq', self.obj96))

    # name
    self.obj96.name.setValue('Seq')

    # attributes
    self.obj96.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj96.attributes.setValue(lcobj2)

    # Abstract
    self.obj96.Abstract.setValue((None, 0))
    self.obj96.Abstract.config = 0

    # cardinality
    self.obj96.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj96.cardinality.setValue(lcobj2)

    # display
    self.obj96.display.setValue('Attributes:\n')
    self.obj96.display.setHeight(15)

    # Actions
    self.obj96.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj96.Actions.setValue(lcobj2)

    # Constraints
    self.obj96.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj96.Constraints.setValue(lcobj2)

    self.obj96.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1820.0,2620.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=CD_Class3(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    # QOCA
    self.obj97.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj97.Graphical_Appearance.setValue( ('ConditionSet', self.obj97))

    # name
    self.obj97.name.setValue('ConditionSet')

    # attributes
    self.obj97.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj97.attributes.setValue(lcobj2)

    # Abstract
    self.obj97.Abstract.setValue((None, 0))
    self.obj97.Abstract.config = 0

    # cardinality
    self.obj97.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj97.cardinality.setValue(lcobj2)

    # display
    self.obj97.display.setValue('Attributes:\n')
    self.obj97.display.setHeight(15)

    # Actions
    self.obj97.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj97.Actions.setValue(lcobj2)

    # Constraints
    self.obj97.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj97.Constraints.setValue(lcobj2)

    self.obj97.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2640.0,2440.0,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=CD_Class3(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    # QOCA
    self.obj98.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj98.Graphical_Appearance.setValue( ('Match', self.obj98))

    # name
    self.obj98.name.setValue('Match')

    # attributes
    self.obj98.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj98.attributes.setValue(lcobj2)

    # Abstract
    self.obj98.Abstract.setValue((None, 0))
    self.obj98.Abstract.config = 0

    # cardinality
    self.obj98.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj98.cardinality.setValue(lcobj2)

    # display
    self.obj98.display.setValue('Attributes:\n')
    self.obj98.display.setHeight(15)

    # Actions
    self.obj98.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj98.Actions.setValue(lcobj2)

    # Constraints
    self.obj98.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj98.Constraints.setValue(lcobj2)

    self.obj98.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2886.0,2260.0,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=CD_Class3(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # QOCA
    self.obj99.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj99.Graphical_Appearance.setValue( ('Print', self.obj99))

    # name
    self.obj99.name.setValue('Print')

    # attributes
    self.obj99.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('classtype', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('s_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj99.attributes.setValue(lcobj2)

    # Abstract
    self.obj99.Abstract.setValue((None, 0))
    self.obj99.Abstract.config = 0

    # cardinality
    self.obj99.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj99.cardinality.setValue(lcobj2)

    # display
    self.obj99.display.setValue('Attributes:\n')
    self.obj99.display.setHeight(15)

    # Actions
    self.obj99.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj99.Actions.setValue(lcobj2)

    # Constraints
    self.obj99.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj99.Constraints.setValue(lcobj2)

    self.obj99.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2840.0,2440.0,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=CD_Class3(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    # QOCA
    self.obj100.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj100.Graphical_Appearance.setValue( ('Attribute', self.obj100))

    # name
    self.obj100.name.setValue('Attribute')

    # attributes
    self.obj100.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj100.attributes.setValue(lcobj2)

    # Abstract
    self.obj100.Abstract.setValue((None, 0))
    self.obj100.Abstract.config = 0

    # cardinality
    self.obj100.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasAttribute_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasAttribute_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj100.cardinality.setValue(lcobj2)

    # display
    self.obj100.display.setValue('Attributes:\nMultiplicities:\n  - From hasAttribute_S: 0 to N\n  - From hasAttribute_T: 0 to N\n')
    self.obj100.display.setHeight(15)

    # Actions
    self.obj100.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj100.Actions.setValue(lcobj2)

    # Constraints
    self.obj100.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj100.Constraints.setValue(lcobj2)

    self.obj100.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2700.0,660.0,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.16484375, 1.0]
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=CD_Class3(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # QOCA
    self.obj101.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj101.Graphical_Appearance.setValue( ('Expression', self.obj101))

    # name
    self.obj101.name.setValue('Expression')

    # attributes
    self.obj101.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj101.attributes.setValue(lcobj2)

    # Abstract
    self.obj101.Abstract.setValue((None, 1))
    self.obj101.Abstract.config = 0

    # cardinality
    self.obj101.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('leftExpr', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('rightExpr', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasArgs', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj101.cardinality.setValue(lcobj2)

    # display
    self.obj101.display.setValue('Attributes:\n  - Type :: Enum\n  - name :: String\nMultiplicities:\n  - From leftExpr: 0 to N\n  - From rightExpr: 0 to N\n  - From hasArgs: 0 to N\n')
    self.obj101.display.setHeight(15)

    # Actions
    self.obj101.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj101.Actions.setValue(lcobj2)

    # Constraints
    self.obj101.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj101.Constraints.setValue(lcobj2)

    self.obj101.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2700.0,420.0,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.2651639344262295]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=CD_Class3(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # QOCA
    self.obj102.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj102.Graphical_Appearance.setValue( ('Equation', self.obj102))

    # name
    self.obj102.name.setValue('Equation')

    # attributes
    self.obj102.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('eq_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj102.attributes.setValue(lcobj2)

    # Abstract
    self.obj102.Abstract.setValue((None, 0))
    self.obj102.Abstract.config = 0

    # cardinality
    self.obj102.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('leftExpr', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('rightExpr', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj102.cardinality.setValue(lcobj2)

    # display
    self.obj102.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - To leftExpr: 0 to N\n  - To rightExpr: 0 to N\n')
    self.obj102.display.setHeight(15)

    # Actions
    self.obj102.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj102.Actions.setValue(lcobj2)

    # Constraints
    self.obj102.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj102.Constraints.setValue(lcobj2)

    self.obj102.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2740.0,80.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=CD_Class3(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # QOCA
    self.obj103.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj103.Graphical_Appearance.setValue( ('Operation', self.obj103))

    # name
    self.obj103.name.setValue('Operation')

    # attributes
    self.obj103.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj103.attributes.setValue(lcobj2)

    # Abstract
    self.obj103.Abstract.setValue((None, 1))
    self.obj103.Abstract.config = 0

    # cardinality
    self.obj103.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasArgs', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj103.cardinality.setValue(lcobj2)

    # display
    self.obj103.display.setValue('Attributes:\nMultiplicities:\n  - To hasArgs: 0 to N\n')
    self.obj103.display.setHeight(15)

    # Actions
    self.obj103.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj103.Actions.setValue(lcobj2)

    # Constraints
    self.obj103.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj103.Constraints.setValue(lcobj2)

    self.obj103.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(3000.0,960.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj108=CD_Class3(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # QOCA
    self.obj108.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj108.Graphical_Appearance.setValue( ('Add', self.obj108))

    # name
    self.obj108.name.setValue('Add')

    # attributes
    self.obj108.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj108.attributes.setValue(lcobj2)

    # Abstract
    self.obj108.Abstract.setValue((None, 0))
    self.obj108.Abstract.config = 0

    # cardinality
    self.obj108.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj108.cardinality.setValue(lcobj2)

    # display
    self.obj108.display.setValue('Attributes:\n')
    self.obj108.display.setHeight(15)

    # Actions
    self.obj108.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj108.Actions.setValue(lcobj2)

    # Constraints
    self.obj108.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj108.Constraints.setValue(lcobj2)

    self.obj108.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2820.0,1140.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=CD_Class3(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # QOCA
    self.obj109.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj109.Graphical_Appearance.setValue( ('Subtract', self.obj109))

    # name
    self.obj109.name.setValue('Subtract')

    # attributes
    self.obj109.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj109.attributes.setValue(lcobj2)

    # Abstract
    self.obj109.Abstract.setValue((None, 0))
    self.obj109.Abstract.config = 0

    # cardinality
    self.obj109.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj109.cardinality.setValue(lcobj2)

    # display
    self.obj109.display.setValue('Attributes:\n')
    self.obj109.display.setHeight(15)

    # Actions
    self.obj109.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj109.Actions.setValue(lcobj2)

    # Constraints
    self.obj109.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj109.Constraints.setValue(lcobj2)

    self.obj109.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(3080.0,1140.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=CD_Class3(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # QOCA
    self.obj110.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj110.Graphical_Appearance.setValue( ('Concat', self.obj110))

    # name
    self.obj110.name.setValue('Concat')

    # attributes
    self.obj110.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj110.attributes.setValue(lcobj2)

    # Abstract
    self.obj110.Abstract.setValue((None, 0))
    self.obj110.Abstract.config = 0

    # cardinality
    self.obj110.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj110.cardinality.setValue(lcobj2)

    # display
    self.obj110.display.setValue('Attributes:\n')
    self.obj110.display.setHeight(15)

    # Actions
    self.obj110.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj110.Actions.setValue(lcobj2)

    # Constraints
    self.obj110.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj110.Constraints.setValue(lcobj2)

    self.obj110.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2960.0,1300.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=CD_Class3(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # QOCA
    self.obj111.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj111.Graphical_Appearance.setValue( ('Constant', self.obj111))

    # name
    self.obj111.name.setValue('Constant')

    # attributes
    self.obj111.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['String', 'Bool', 'Integer', 'Float'],None,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('String', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Bool', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Integer', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('Float', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('exp_', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj111.attributes.setValue(lcobj2)

    # Abstract
    self.obj111.Abstract.setValue((None, 0))
    self.obj111.Abstract.config = 0

    # cardinality
    self.obj111.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj111.cardinality.setValue(lcobj2)

    # display
    self.obj111.display.setValue('Attributes:\n')
    self.obj111.display.setHeight(15)

    # Actions
    self.obj111.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj111.Actions.setValue(lcobj2)

    # Constraints
    self.obj111.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj111.Constraints.setValue(lcobj2)

    self.obj111.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(3180.0,660.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=CD_Association3(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # QOCA
    self.obj112.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj112.Graphical_Appearance.setValue( ('paired_with', self.obj112))
    self.obj112.Graphical_Appearance.linkInfo=linkEditor(self,self.obj112.Graphical_Appearance.semObject, "paired_with")
    self.obj112.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('paired_with_1stLink', self.obj112.Graphical_Appearance.linkInfo.FirstLink))
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('paired_with_1stSegment', self.obj112.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj112.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.Center.setValue( ('paired_with_Center', self.obj112.Graphical_Appearance.linkInfo))
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('paired_with_2ndSegment', self.obj112.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('paired_with_2ndLink', self.obj112.Graphical_Appearance.linkInfo.SecondLink))
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.Center.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj112.Graphical_Appearance.semObject

    # name
    self.obj112.name.setValue('paired_with')

    # displaySelect
    self.obj112.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj112.displaySelect.config = 0

    # attributes
    self.obj112.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj112.attributes.setValue(lcobj2)

    # cardinality
    self.obj112.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('ApplyModel', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MatchModel', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj112.cardinality.setValue(lcobj2)

    # display
    self.obj112.display.setValue('Multiplicities:\n  - To ApplyModel: 1 to 1\n  - From MatchModel: 1 to 1\n')
    self.obj112.display.setHeight(15)

    # Actions
    self.obj112.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj112.Actions.setValue(lcobj2)

    # Constraints
    self.obj112.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj112.Constraints.setValue(lcobj2)

    self.obj112.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(121.0,395.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.09
       new_obj.layConstraints['scale'] = [1.526, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=CD_Association3(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # QOCA
    self.obj113.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj113.Graphical_Appearance.setValue( ('match_contains', self.obj113))
    self.obj113.Graphical_Appearance.linkInfo=linkEditor(self,self.obj113.Graphical_Appearance.semObject, "match_contains")
    self.obj113.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('match_contains_1stLink', self.obj113.Graphical_Appearance.linkInfo.FirstLink))
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('match_contains_1stSegment', self.obj113.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj113.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj113.Graphical_Appearance.linkInfo.Center.setValue( ('match_contains_Center', self.obj113.Graphical_Appearance.linkInfo))
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('match_contains_2ndSegment', self.obj113.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj113.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('match_contains_2ndLink', self.obj113.Graphical_Appearance.linkInfo.SecondLink))
    self.obj113.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj113.Graphical_Appearance.semObject
    self.obj113.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj113.Graphical_Appearance.semObject
    self.obj113.Graphical_Appearance.linkInfo.Center.semObject=self.obj113.Graphical_Appearance.semObject
    self.obj113.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj113.Graphical_Appearance.semObject
    self.obj113.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj113.Graphical_Appearance.semObject

    # name
    self.obj113.name.setValue('match_contains')

    # displaySelect
    self.obj113.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj113.displaySelect.config = 0

    # attributes
    self.obj113.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj113.attributes.setValue(lcobj2)

    # cardinality
    self.obj113.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MatchModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj113.cardinality.setValue(lcobj2)

    # display
    self.obj113.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MatchModel: 0 to N\n')
    self.obj113.display.setHeight(15)

    # Actions
    self.obj113.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj113.Actions.setValue(lcobj2)

    # Constraints
    self.obj113.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj113.Constraints.setValue(lcobj2)

    self.obj113.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(745.5625,123.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.7360000000000002, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=CD_Association3(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # QOCA
    self.obj114.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj114.Graphical_Appearance.setValue( ('apply_contains', self.obj114))
    self.obj114.Graphical_Appearance.linkInfo=linkEditor(self,self.obj114.Graphical_Appearance.semObject, "apply_contains")
    self.obj114.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('apply_contains_1stLink', self.obj114.Graphical_Appearance.linkInfo.FirstLink))
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('apply_contains_1stSegment', self.obj114.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj114.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.Center.setValue( ('apply_contains_Center', self.obj114.Graphical_Appearance.linkInfo))
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('apply_contains_2ndSegment', self.obj114.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('apply_contains_2ndLink', self.obj114.Graphical_Appearance.linkInfo.SecondLink))
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.Center.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj114.Graphical_Appearance.semObject

    # name
    self.obj114.name.setValue('apply_contains')

    # displaySelect
    self.obj114.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj114.displaySelect.config = 0

    # attributes
    self.obj114.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj114.attributes.setValue(lcobj2)

    # cardinality
    self.obj114.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('ApplyModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj114.cardinality.setValue(lcobj2)

    # display
    self.obj114.display.setValue('Multiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From ApplyModel: 0 to N\n')
    self.obj114.display.setHeight(15)

    # Actions
    self.obj114.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj114.Actions.setValue(lcobj2)

    # Constraints
    self.obj114.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj114.Constraints.setValue(lcobj2)

    self.obj114.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(572.123046875,1947.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.7290000000000001, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=CD_Association3(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # QOCA
    self.obj115.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj115.Graphical_Appearance.setValue( ('directLink_T', self.obj115))
    self.obj115.Graphical_Appearance.linkInfo=linkEditor(self,self.obj115.Graphical_Appearance.semObject, "directLink_T")
    self.obj115.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_T_1stLink', self.obj115.Graphical_Appearance.linkInfo.FirstLink))
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_T_1stSegment', self.obj115.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj115.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj115.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_T_Center', self.obj115.Graphical_Appearance.linkInfo))
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_T_2ndSegment', self.obj115.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj115.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_T_2ndLink', self.obj115.Graphical_Appearance.linkInfo.SecondLink))
    self.obj115.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj115.Graphical_Appearance.semObject
    self.obj115.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj115.Graphical_Appearance.semObject
    self.obj115.Graphical_Appearance.linkInfo.Center.semObject=self.obj115.Graphical_Appearance.semObject
    self.obj115.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj115.Graphical_Appearance.semObject
    self.obj115.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj115.Graphical_Appearance.semObject

    # name
    self.obj115.name.setValue('directLink_T')

    # displaySelect
    self.obj115.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj115.displaySelect.config = 0

    # attributes
    self.obj115.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('associationType', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj115.attributes.setValue(lcobj2)

    # cardinality
    self.obj115.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj115.cardinality.setValue(lcobj2)

    # display
    self.obj115.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj115.display.setHeight(15)

    # Actions
    self.obj115.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj115.Actions.setValue(lcobj2)

    # Constraints
    self.obj115.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj115.Constraints.setValue(lcobj2)

    self.obj115.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1969.58007812,1860.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.185483870967742]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=CD_Association3(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # QOCA
    self.obj116.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj116.Graphical_Appearance.setValue( ('directLink_S', self.obj116))
    self.obj116.Graphical_Appearance.linkInfo=linkEditor(self,self.obj116.Graphical_Appearance.semObject, "directLink_S")
    self.obj116.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_S_1stLink', self.obj116.Graphical_Appearance.linkInfo.FirstLink))
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_S_1stSegment', self.obj116.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj116.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj116.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_S_Center', self.obj116.Graphical_Appearance.linkInfo))
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_S_2ndSegment', self.obj116.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj116.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_S_2ndLink', self.obj116.Graphical_Appearance.linkInfo.SecondLink))
    self.obj116.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj116.Graphical_Appearance.semObject
    self.obj116.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj116.Graphical_Appearance.semObject
    self.obj116.Graphical_Appearance.linkInfo.Center.semObject=self.obj116.Graphical_Appearance.semObject
    self.obj116.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj116.Graphical_Appearance.semObject
    self.obj116.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj116.Graphical_Appearance.semObject

    # name
    self.obj116.name.setValue('directLink_S')

    # displaySelect
    self.obj116.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj116.displaySelect.config = 0

    # attributes
    self.obj116.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('associationType', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('t_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj116.attributes.setValue(lcobj2)

    # cardinality
    self.obj116.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj116.cardinality.setValue(lcobj2)

    # display
    self.obj116.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj116.display.setHeight(15)

    # Actions
    self.obj116.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj116.Actions.setValue(lcobj2)

    # Constraints
    self.obj116.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj116.Constraints.setValue(lcobj2)

    self.obj116.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1853.2421875,89.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.8620000000000001, 1.185483870967742]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=CD_Association3(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # QOCA
    self.obj117.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj117.Graphical_Appearance.setValue( ('indirectLink_S', self.obj117))
    self.obj117.Graphical_Appearance.linkInfo=linkEditor(self,self.obj117.Graphical_Appearance.semObject, "indirectLink_S")
    self.obj117.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('indirectLink_S_1stLink', self.obj117.Graphical_Appearance.linkInfo.FirstLink))
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('indirectLink_S_1stSegment', self.obj117.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj117.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj117.Graphical_Appearance.linkInfo.Center.setValue( ('indirectLink_S_Center', self.obj117.Graphical_Appearance.linkInfo))
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('indirectLink_S_2ndSegment', self.obj117.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj117.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('indirectLink_S_2ndLink', self.obj117.Graphical_Appearance.linkInfo.SecondLink))
    self.obj117.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj117.Graphical_Appearance.semObject
    self.obj117.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj117.Graphical_Appearance.semObject
    self.obj117.Graphical_Appearance.linkInfo.Center.semObject=self.obj117.Graphical_Appearance.semObject
    self.obj117.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj117.Graphical_Appearance.semObject
    self.obj117.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj117.Graphical_Appearance.semObject

    # name
    self.obj117.name.setValue('indirectLink_S')

    # displaySelect
    self.obj117.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj117.displaySelect.config = 0

    # attributes
    self.obj117.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj117.attributes.setValue(lcobj2)

    # cardinality
    self.obj117.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj117.cardinality.setValue(lcobj2)

    # display
    self.obj117.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj117.display.setHeight(15)

    # Actions
    self.obj117.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj117.Actions.setValue(lcobj2)

    # Constraints
    self.obj117.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj117.Constraints.setValue(lcobj2)

    self.obj117.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1846.7421875,223.5,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.8620000000000001, 1.0]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=CD_Association3(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # QOCA
    self.obj118.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj118.Graphical_Appearance.setValue( ('backward_link', self.obj118))
    self.obj118.Graphical_Appearance.linkInfo=linkEditor(self,self.obj118.Graphical_Appearance.semObject, "backward_link")
    self.obj118.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('backward_link_1stLink', self.obj118.Graphical_Appearance.linkInfo.FirstLink))
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('backward_link_1stSegment', self.obj118.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj118.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.Center.setValue( ('backward_link_Center', self.obj118.Graphical_Appearance.linkInfo))
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('backward_link_2ndSegment', self.obj118.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('backward_link_2ndLink', self.obj118.Graphical_Appearance.linkInfo.SecondLink))
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.Center.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj118.Graphical_Appearance.semObject

    # name
    self.obj118.name.setValue('backward_link')

    # displaySelect
    self.obj118.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj118.displaySelect.config = 0

    # attributes
    self.obj118.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('type', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('ruleDef', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj118.attributes.setValue(lcobj2)

    # cardinality
    self.obj118.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj118.cardinality.setValue(lcobj2)

    # display
    self.obj118.display.setValue('Attributes:\n  - type :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj118.display.setHeight(15)

    # Actions
    self.obj118.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj118.Actions.setValue(lcobj2)

    # Constraints
    self.obj118.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj118.Constraints.setValue(lcobj2)

    self.obj118.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1991.5,1063.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.185483870967742]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=CD_Association3(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # QOCA
    self.obj119.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj119.Graphical_Appearance.setValue( ('trace_link', self.obj119))
    self.obj119.Graphical_Appearance.linkInfo=linkEditor(self,self.obj119.Graphical_Appearance.semObject, "trace_link")
    self.obj119.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('trace_link_1stLink', self.obj119.Graphical_Appearance.linkInfo.FirstLink))
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('trace_link_1stSegment', self.obj119.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj119.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.Center.setValue( ('trace_link_Center', self.obj119.Graphical_Appearance.linkInfo))
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('trace_link_2ndSegment', self.obj119.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('trace_link_2ndLink', self.obj119.Graphical_Appearance.linkInfo.SecondLink))
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.Center.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj119.Graphical_Appearance.semObject

    # name
    self.obj119.name.setValue('trace_link')

    # displaySelect
    self.obj119.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj119.displaySelect.config = 0

    # attributes
    self.obj119.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.attributes.setValue(lcobj2)

    # cardinality
    self.obj119.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj119.cardinality.setValue(lcobj2)

    # display
    self.obj119.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj119.display.setHeight(15)

    # Actions
    self.obj119.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.Actions.setValue(lcobj2)

    # Constraints
    self.obj119.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.Constraints.setValue(lcobj2)

    self.obj119.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(2290.0,1056.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=CD_Association3(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # QOCA
    self.obj120.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj120.Graphical_Appearance.setValue( ('hasAttribute_S', self.obj120))
    self.obj120.Graphical_Appearance.linkInfo=linkEditor(self,self.obj120.Graphical_Appearance.semObject, "hasAttribute_S")
    self.obj120.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasAttribute_S_1stLink', self.obj120.Graphical_Appearance.linkInfo.FirstLink))
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasAttribute_S_1stSegment', self.obj120.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj120.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.Center.setValue( ('hasAttribute_S_Center', self.obj120.Graphical_Appearance.linkInfo))
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasAttribute_S_2ndSegment', self.obj120.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasAttribute_S_2ndLink', self.obj120.Graphical_Appearance.linkInfo.SecondLink))
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.Center.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj120.Graphical_Appearance.semObject

    # name
    self.obj120.name.setValue('hasAttribute_S')

    # displaySelect
    self.obj120.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj120.displaySelect.config = 0

    # attributes
    self.obj120.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.attributes.setValue(lcobj2)

    # cardinality
    self.obj120.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj120.cardinality.setValue(lcobj2)

    # display
    self.obj120.display.setValue('Multiplicities:\n  - To Attribute: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj120.display.setHeight(15)

    # Actions
    self.obj120.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.Actions.setValue(lcobj2)

    # Constraints
    self.obj120.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.Constraints.setValue(lcobj2)

    self.obj120.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(2291.32421875,496.446260246,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.8620000000000001, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=CD_Association3(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # QOCA
    self.obj121.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj121.Graphical_Appearance.setValue( ('hasAttribute_T', self.obj121))
    self.obj121.Graphical_Appearance.linkInfo=linkEditor(self,self.obj121.Graphical_Appearance.semObject, "hasAttribute_T")
    self.obj121.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasAttribute_T_1stLink', self.obj121.Graphical_Appearance.linkInfo.FirstLink))
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasAttribute_T_1stSegment', self.obj121.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj121.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.Center.setValue( ('hasAttribute_T_Center', self.obj121.Graphical_Appearance.linkInfo))
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasAttribute_T_2ndSegment', self.obj121.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasAttribute_T_2ndLink', self.obj121.Graphical_Appearance.linkInfo.SecondLink))
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.Center.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj121.Graphical_Appearance.semObject

    # name
    self.obj121.name.setValue('hasAttribute_T')

    # displaySelect
    self.obj121.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj121.displaySelect.config = 0

    # attributes
    self.obj121.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.attributes.setValue(lcobj2)

    # cardinality
    self.obj121.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj121.cardinality.setValue(lcobj2)

    # display
    self.obj121.display.setValue('Multiplicities:\n  - To Attribute: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj121.display.setHeight(15)

    # Actions
    self.obj121.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.Actions.setValue(lcobj2)

    # Constraints
    self.obj121.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.Constraints.setValue(lcobj2)

    self.obj121.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(2412.7734375,1464.06557377,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=CD_Association3(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # QOCA
    self.obj122.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj122.Graphical_Appearance.setValue( ('leftExpr', self.obj122))
    self.obj122.Graphical_Appearance.linkInfo=linkEditor(self,self.obj122.Graphical_Appearance.semObject, "leftExpr")
    self.obj122.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('leftExpr_1stLink', self.obj122.Graphical_Appearance.linkInfo.FirstLink))
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('leftExpr_1stSegment', self.obj122.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj122.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.Center.setValue( ('leftExpr_Center', self.obj122.Graphical_Appearance.linkInfo))
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('leftExpr_2ndSegment', self.obj122.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('leftExpr_2ndLink', self.obj122.Graphical_Appearance.linkInfo.SecondLink))
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.Center.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj122.Graphical_Appearance.semObject

    # name
    self.obj122.name.setValue('leftExpr')

    # displaySelect
    self.obj122.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj122.displaySelect.config = 0

    # attributes
    self.obj122.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.attributes.setValue(lcobj2)

    # cardinality
    self.obj122.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Equation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj122.cardinality.setValue(lcobj2)

    # display
    self.obj122.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Equation: 0 to N\n')
    self.obj122.display.setHeight(15)

    # Actions
    self.obj122.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.Actions.setValue(lcobj2)

    # Constraints
    self.obj122.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.Constraints.setValue(lcobj2)

    self.obj122.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(2715.0,299.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.204, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=CD_Association3(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # QOCA
    self.obj123.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj123.Graphical_Appearance.setValue( ('rightExpr', self.obj123))
    self.obj123.Graphical_Appearance.linkInfo=linkEditor(self,self.obj123.Graphical_Appearance.semObject, "rightExpr")
    self.obj123.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('rightExpr_1stLink', self.obj123.Graphical_Appearance.linkInfo.FirstLink))
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('rightExpr_1stSegment', self.obj123.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj123.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.Center.setValue( ('rightExpr_Center', self.obj123.Graphical_Appearance.linkInfo))
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('rightExpr_2ndSegment', self.obj123.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('rightExpr_2ndLink', self.obj123.Graphical_Appearance.linkInfo.SecondLink))
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.Center.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj123.Graphical_Appearance.semObject

    # name
    self.obj123.name.setValue('rightExpr')

    # displaySelect
    self.obj123.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj123.displaySelect.config = 0

    # attributes
    self.obj123.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.attributes.setValue(lcobj2)

    # cardinality
    self.obj123.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Equation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj123.cardinality.setValue(lcobj2)

    # display
    self.obj123.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Equation: 0 to N\n')
    self.obj123.display.setHeight(15)

    # Actions
    self.obj123.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Actions.setValue(lcobj2)

    # Constraints
    self.obj123.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Constraints.setValue(lcobj2)

    self.obj123.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(2930.15625,299.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.204, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=CD_Association3(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # QOCA
    self.obj124.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj124.Graphical_Appearance.setValue( ('hasArgs', self.obj124))
    self.obj124.Graphical_Appearance.linkInfo=linkEditor(self,self.obj124.Graphical_Appearance.semObject, "hasArgs")
    self.obj124.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasArgs_1stLink', self.obj124.Graphical_Appearance.linkInfo.FirstLink))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasArgs_1stSegment', self.obj124.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj124.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.Center.setValue( ('hasArgs_Center', self.obj124.Graphical_Appearance.linkInfo))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasArgs_2ndSegment', self.obj124.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasArgs_2ndLink', self.obj124.Graphical_Appearance.linkInfo.SecondLink))
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.Center.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj124.Graphical_Appearance.semObject

    # name
    self.obj124.name.setValue('hasArgs')

    # displaySelect
    self.obj124.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj124.displaySelect.config = 0

    # attributes
    self.obj124.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.attributes.setValue(lcobj2)

    # cardinality
    self.obj124.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Operation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj124.cardinality.setValue(lcobj2)

    # display
    self.obj124.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Operation: 0 to N\n')
    self.obj124.display.setHeight(15)

    # Actions
    self.obj124.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Actions.setValue(lcobj2)

    # Constraints
    self.obj124.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Constraints.setValue(lcobj2)

    self.obj124.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(3067.5,791.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.246, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj126=CD_Inheritance3(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    self.obj126.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(460.953125,310.040522541,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=CD_Inheritance3(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    self.obj127.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(668.0,934.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=CD_Inheritance3(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    self.obj128.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(308.0,622.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=CD_Inheritance3(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    self.obj129.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(349.0,783.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=CD_Inheritance3(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    self.obj130.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(372.0,809.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=CD_Inheritance3(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    self.obj131.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(468.0,645.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=CD_Inheritance3(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    self.obj132.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(929.875,1107.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=CD_Inheritance3(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    self.obj133.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(618.0,1074.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=CD_Inheritance3(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    self.obj134.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(801.0,1104.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=CD_Inheritance3(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    self.obj135.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(638.0,1081.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=CD_Inheritance3(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    self.obj136.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(899.0,1275.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=CD_Inheritance3(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    self.obj137.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(855.0,1451.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=CD_Inheritance3(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    self.obj138.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(898.0,1621.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=CD_Inheritance3(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    self.obj139.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(930.0,1522.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=CD_Inheritance3(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    self.obj140.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1032.875,1278.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=CD_Inheritance3(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    self.obj141.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1246.0,1144.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=CD_Inheritance3(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(961.0,1487.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=CD_Inheritance3(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    self.obj143.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1208.0,1461.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=CD_Inheritance3(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    self.obj144.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1311.0,1118.5,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=CD_Inheritance3(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    self.obj145.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1302.0,1129.0,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=CD_Inheritance3(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    self.obj146.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1430.0,1475.0,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=CD_Inheritance3(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    self.obj147.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1510.0,1455.0,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=CD_Inheritance3(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    self.obj148.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1328.0,1095.0,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj149=CD_Inheritance3(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    self.obj149.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1334.0,1089.0,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=CD_Inheritance3(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    self.obj150.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1329.0,1078.0,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=CD_Inheritance3(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    self.obj151.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2232.0,1488.0,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=CD_Inheritance3(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    self.obj152.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2365.0,1456.0,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj153=CD_Inheritance3(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    self.obj153.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(742.3984375,330.851997951,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=CD_Inheritance3(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    self.obj154.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(736.0,511.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=CD_Inheritance3(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    self.obj155.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(779.0,671.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=CD_Inheritance3(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    self.obj156.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(936.0,511.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=CD_Inheritance3(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    self.obj157.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1020.6875,661.957746479,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=CD_Inheritance3(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    self.obj158.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(976.3984375,337.466752049,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=CD_Inheritance3(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    self.obj159.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1242.3984375,350.466752049,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=CD_Inheritance3(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    self.obj160.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1156.0,511.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=CD_Inheritance3(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    self.obj161.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1236.0,591.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=CD_Inheritance3(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    self.obj162.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1302.0,812.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj163=CD_Inheritance3(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    self.obj163.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1538.078125,385.540522541,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=CD_Inheritance3(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    self.obj164.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1456.0,551.0,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=CD_Inheritance3(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    self.obj165.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1506.0,631.0,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=CD_Inheritance3(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    self.obj166.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1550.0,771.0,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=CD_Inheritance3(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    self.obj167.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(264.828125,2024.42622951,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=CD_Inheritance3(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    self.obj168.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(451.828125,2034.42622951,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=CD_Inheritance3(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    self.obj169.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(594.828125,2052.42622951,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=CD_Inheritance3(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    self.obj170.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1972.828125,2057.42622951,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj171=CD_Inheritance3(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    self.obj171.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(176.0,2241.0,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=CD_Inheritance3(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(False)

    self.obj172.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(225.0,2586.0,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=CD_Inheritance3(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(False)

    self.obj173.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(794.828125,2061.42622951,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=CD_Inheritance3(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    self.obj174.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(826.0,2245.0,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=CD_Inheritance3(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    self.obj175.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(133.5,2421.0,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=CD_Inheritance3(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    self.obj176.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1953.5,2252.0,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    self.obj177=CD_Inheritance3(self)
    self.obj177.isGraphObjectVisual = True

    if(hasattr(self.obj177, '_setHierarchicalLink')):
      self.obj177._setHierarchicalLink(False)

    self.obj177.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2067.0,2246.0,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)
    self.obj177.postAction( rootNode.CREATE )

    self.obj178=CD_Inheritance3(self)
    self.obj178.isGraphObjectVisual = True

    if(hasattr(self.obj178, '_setHierarchicalLink')):
      self.obj178._setHierarchicalLink(False)

    self.obj178.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2338.5,2248.0,self.obj178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj178)
    self.globalAndLocalPostcondition(self.obj178, rootNode)
    self.obj178.postAction( rootNode.CREATE )

    self.obj179=CD_Inheritance3(self)
    self.obj179.isGraphObjectVisual = True

    if(hasattr(self.obj179, '_setHierarchicalLink')):
      self.obj179._setHierarchicalLink(False)

    self.obj179.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1776.046875,2063.42622951,self.obj179)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj179.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj179)
    self.globalAndLocalPostcondition(self.obj179, rootNode)
    self.obj179.postAction( rootNode.CREATE )

    self.obj180=CD_Inheritance3(self)
    self.obj180.isGraphObjectVisual = True

    if(hasattr(self.obj180, '_setHierarchicalLink')):
      self.obj180._setHierarchicalLink(False)

    self.obj180.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1057.828125,2058.42622951,self.obj180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj180)
    self.globalAndLocalPostcondition(self.obj180, rootNode)
    self.obj180.postAction( rootNode.CREATE )

    self.obj181=CD_Inheritance3(self)
    self.obj181.isGraphObjectVisual = True

    if(hasattr(self.obj181, '_setHierarchicalLink')):
      self.obj181._setHierarchicalLink(False)

    self.obj181.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1176.328125,2056.42622951,self.obj181)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj181.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj181)
    self.globalAndLocalPostcondition(self.obj181, rootNode)
    self.obj181.postAction( rootNode.CREATE )

    self.obj182=CD_Inheritance3(self)
    self.obj182.isGraphObjectVisual = True

    if(hasattr(self.obj182, '_setHierarchicalLink')):
      self.obj182._setHierarchicalLink(False)

    self.obj182.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1462.625,2057.5,self.obj182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj182)
    self.globalAndLocalPostcondition(self.obj182, rootNode)
    self.obj182.postAction( rootNode.CREATE )

    self.obj183=CD_Inheritance3(self)
    self.obj183.isGraphObjectVisual = True

    if(hasattr(self.obj183, '_setHierarchicalLink')):
      self.obj183._setHierarchicalLink(False)

    self.obj183.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1569.875,2057.5,self.obj183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj183)
    self.globalAndLocalPostcondition(self.obj183, rootNode)
    self.obj183.postAction( rootNode.CREATE )

    self.obj184=CD_Inheritance3(self)
    self.obj184.isGraphObjectVisual = True

    if(hasattr(self.obj184, '_setHierarchicalLink')):
      self.obj184._setHierarchicalLink(False)

    self.obj184.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1776.5,2265.0,self.obj184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj184)
    self.globalAndLocalPostcondition(self.obj184, rootNode)
    self.obj184.postAction( rootNode.CREATE )

    self.obj185=CD_Inheritance3(self)
    self.obj185.isGraphObjectVisual = True

    if(hasattr(self.obj185, '_setHierarchicalLink')):
      self.obj185._setHierarchicalLink(False)

    self.obj185.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1778.0,2251.0,self.obj185)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj185.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj185)
    self.globalAndLocalPostcondition(self.obj185, rootNode)
    self.obj185.postAction( rootNode.CREATE )

    self.obj186=CD_Inheritance3(self)
    self.obj186.isGraphObjectVisual = True

    if(hasattr(self.obj186, '_setHierarchicalLink')):
      self.obj186._setHierarchicalLink(False)

    self.obj186.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2483.0,2243.0,self.obj186)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj186.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj186)
    self.globalAndLocalPostcondition(self.obj186, rootNode)
    self.obj186.postAction( rootNode.CREATE )

    self.obj187=CD_Inheritance3(self)
    self.obj187.isGraphObjectVisual = True

    if(hasattr(self.obj187, '_setHierarchicalLink')):
      self.obj187._setHierarchicalLink(False)

    self.obj187.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2700.0,2239.0,self.obj187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj187)
    self.globalAndLocalPostcondition(self.obj187, rootNode)
    self.obj187.postAction( rootNode.CREATE )

    self.obj188=CD_Inheritance3(self)
    self.obj188.isGraphObjectVisual = True

    if(hasattr(self.obj188, '_setHierarchicalLink')):
      self.obj188._setHierarchicalLink(False)

    self.obj188.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2021.0,2479.0,self.obj188)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj188.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj188)
    self.globalAndLocalPostcondition(self.obj188, rootNode)
    self.obj188.postAction( rootNode.CREATE )

    self.obj189=CD_Inheritance3(self)
    self.obj189.isGraphObjectVisual = True

    if(hasattr(self.obj189, '_setHierarchicalLink')):
      self.obj189._setHierarchicalLink(False)

    self.obj189.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2031.0,2479.0,self.obj189)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj189.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj189)
    self.globalAndLocalPostcondition(self.obj189, rootNode)
    self.obj189.postAction( rootNode.CREATE )

    self.obj190=CD_Inheritance3(self)
    self.obj190.isGraphObjectVisual = True

    if(hasattr(self.obj190, '_setHierarchicalLink')):
      self.obj190._setHierarchicalLink(False)

    self.obj190.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2230.5,2240.0,self.obj190)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj190.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj190)
    self.globalAndLocalPostcondition(self.obj190, rootNode)
    self.obj190.postAction( rootNode.CREATE )

    self.obj191=CD_Inheritance3(self)
    self.obj191.isGraphObjectVisual = True

    if(hasattr(self.obj191, '_setHierarchicalLink')):
      self.obj191._setHierarchicalLink(False)

    self.obj191.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2467.5,2256.0,self.obj191)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj191.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj191)
    self.globalAndLocalPostcondition(self.obj191, rootNode)
    self.obj191.postAction( rootNode.CREATE )

    self.obj192=CD_Inheritance3(self)
    self.obj192.isGraphObjectVisual = True

    if(hasattr(self.obj192, '_setHierarchicalLink')):
      self.obj192._setHierarchicalLink(False)

    self.obj192.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1896.0,2601.0,self.obj192)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj192.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj192)
    self.globalAndLocalPostcondition(self.obj192, rootNode)
    self.obj192.postAction( rootNode.CREATE )

    self.obj193=CD_Inheritance3(self)
    self.obj193.isGraphObjectVisual = True

    if(hasattr(self.obj193, '_setHierarchicalLink')):
      self.obj193._setHierarchicalLink(False)

    self.obj193.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2675.0,2249.0,self.obj193)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj193.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj193)
    self.globalAndLocalPostcondition(self.obj193, rootNode)
    self.obj193.postAction( rootNode.CREATE )

    self.obj194=CD_Inheritance3(self)
    self.obj194.isGraphObjectVisual = True

    if(hasattr(self.obj194, '_setHierarchicalLink')):
      self.obj194._setHierarchicalLink(False)

    self.obj194.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2876.0,2237.0,self.obj194)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj194.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj194)
    self.globalAndLocalPostcondition(self.obj194, rootNode)
    self.obj194.postAction( rootNode.CREATE )

    self.obj195=CD_Inheritance3(self)
    self.obj195.isGraphObjectVisual = True

    if(hasattr(self.obj195, '_setHierarchicalLink')):
      self.obj195._setHierarchicalLink(False)

    self.obj195.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2900.0,2225.0,self.obj195)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj195.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj195)
    self.globalAndLocalPostcondition(self.obj195, rootNode)
    self.obj195.postAction( rootNode.CREATE )

    self.obj196=CD_Inheritance3(self)
    self.obj196.isGraphObjectVisual = True

    if(hasattr(self.obj196, '_setHierarchicalLink')):
      self.obj196._setHierarchicalLink(False)

    self.obj196.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(798.328125,2158.42622951,self.obj196)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj196.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj196)
    self.globalAndLocalPostcondition(self.obj196, rootNode)
    self.obj196.postAction( rootNode.CREATE )

    self.obj197=CD_Inheritance3(self)
    self.obj197.isGraphObjectVisual = True

    if(hasattr(self.obj197, '_setHierarchicalLink')):
      self.obj197._setHierarchicalLink(False)

    self.obj197.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(795.828125,2239.42622951,self.obj197)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj197.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj197)
    self.globalAndLocalPostcondition(self.obj197, rootNode)
    self.obj197.postAction( rootNode.CREATE )

    self.obj198=CD_Inheritance3(self)
    self.obj198.isGraphObjectVisual = True

    if(hasattr(self.obj198, '_setHierarchicalLink')):
      self.obj198._setHierarchicalLink(False)

    self.obj198.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(815.828125,2319.42622951,self.obj198)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj198.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj198)
    self.globalAndLocalPostcondition(self.obj198, rootNode)
    self.obj198.postAction( rootNode.CREATE )

    self.obj199=CD_Inheritance3(self)
    self.obj199.isGraphObjectVisual = True

    if(hasattr(self.obj199, '_setHierarchicalLink')):
      self.obj199._setHierarchicalLink(False)

    self.obj199.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1155.828125,2149.42622951,self.obj199)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj199.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj199)
    self.globalAndLocalPostcondition(self.obj199, rootNode)
    self.obj199.postAction( rootNode.CREATE )

    self.obj200=CD_Inheritance3(self)
    self.obj200.isGraphObjectVisual = True

    if(hasattr(self.obj200, '_setHierarchicalLink')):
      self.obj200._setHierarchicalLink(False)

    self.obj200.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1609.875,2147.5,self.obj200)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj200.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj200)
    self.globalAndLocalPostcondition(self.obj200, rootNode)
    self.obj200.postAction( rootNode.CREATE )

    self.obj201=CD_Inheritance3(self)
    self.obj201.isGraphObjectVisual = True

    if(hasattr(self.obj201, '_setHierarchicalLink')):
      self.obj201._setHierarchicalLink(False)

    self.obj201.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1730.546875,2129.42622951,self.obj201)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj201.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj201)
    self.globalAndLocalPostcondition(self.obj201, rootNode)
    self.obj201.postAction( rootNode.CREATE )

    self.obj202=CD_Inheritance3(self)
    self.obj202.isGraphObjectVisual = True

    if(hasattr(self.obj202, '_setHierarchicalLink')):
      self.obj202._setHierarchicalLink(False)

    self.obj202.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1823.046875,2149.42622951,self.obj202)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj202.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj202)
    self.globalAndLocalPostcondition(self.obj202, rootNode)
    self.obj202.postAction( rootNode.CREATE )

    self.obj203=CD_Inheritance3(self)
    self.obj203.isGraphObjectVisual = True

    if(hasattr(self.obj203, '_setHierarchicalLink')):
      self.obj203._setHierarchicalLink(False)

    self.obj203.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1933.046875,2149.42622951,self.obj203)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj203.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj203)
    self.globalAndLocalPostcondition(self.obj203, rootNode)
    self.obj203.postAction( rootNode.CREATE )

    self.obj204=CD_Inheritance3(self)
    self.obj204.isGraphObjectVisual = True

    if(hasattr(self.obj204, '_setHierarchicalLink')):
      self.obj204._setHierarchicalLink(False)

    self.obj204.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2043.046875,2149.42622951,self.obj204)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj204.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj204)
    self.globalAndLocalPostcondition(self.obj204, rootNode)
    self.obj204.postAction( rootNode.CREATE )

    self.obj205=CD_Inheritance3(self)
    self.obj205.isGraphObjectVisual = True

    if(hasattr(self.obj205, '_setHierarchicalLink')):
      self.obj205._setHierarchicalLink(False)

    self.obj205.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2143.046875,2149.42622951,self.obj205)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj205.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj205)
    self.globalAndLocalPostcondition(self.obj205, rootNode)
    self.obj205.postAction( rootNode.CREATE )

    self.obj206=CD_Inheritance3(self)
    self.obj206.isGraphObjectVisual = True

    if(hasattr(self.obj206, '_setHierarchicalLink')):
      self.obj206._setHierarchicalLink(False)

    self.obj206.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2246.046875,2149.42622951,self.obj206)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj206.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj206)
    self.globalAndLocalPostcondition(self.obj206, rootNode)
    self.obj206.postAction( rootNode.CREATE )

    self.obj207=CD_Inheritance3(self)
    self.obj207.isGraphObjectVisual = True

    if(hasattr(self.obj207, '_setHierarchicalLink')):
      self.obj207._setHierarchicalLink(False)

    self.obj207.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2223.046875,2239.42622951,self.obj207)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj207.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj207)
    self.globalAndLocalPostcondition(self.obj207, rootNode)
    self.obj207.postAction( rootNode.CREATE )

    self.obj208=CD_Inheritance3(self)
    self.obj208.isGraphObjectVisual = True

    if(hasattr(self.obj208, '_setHierarchicalLink')):
      self.obj208._setHierarchicalLink(False)

    self.obj208.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2124.046875,2255.42622951,self.obj208)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj208.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj208)
    self.globalAndLocalPostcondition(self.obj208, rootNode)
    self.obj208.postAction( rootNode.CREATE )

    self.obj209=CD_Inheritance3(self)
    self.obj209.isGraphObjectVisual = True

    if(hasattr(self.obj209, '_setHierarchicalLink')):
      self.obj209._setHierarchicalLink(False)

    self.obj209.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2023.046875,2239.42622951,self.obj209)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj209.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj209)
    self.globalAndLocalPostcondition(self.obj209, rootNode)
    self.obj209.postAction( rootNode.CREATE )

    self.obj210=CD_Inheritance3(self)
    self.obj210.isGraphObjectVisual = True

    if(hasattr(self.obj210, '_setHierarchicalLink')):
      self.obj210._setHierarchicalLink(False)

    self.obj210.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1923.046875,2239.42622951,self.obj210)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj210.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj210)
    self.globalAndLocalPostcondition(self.obj210, rootNode)
    self.obj210.postAction( rootNode.CREATE )

    self.obj211=CD_Inheritance3(self)
    self.obj211.isGraphObjectVisual = True

    if(hasattr(self.obj211, '_setHierarchicalLink')):
      self.obj211._setHierarchicalLink(False)

    self.obj211.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1840.546875,2219.42622951,self.obj211)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj211.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj211)
    self.globalAndLocalPostcondition(self.obj211, rootNode)
    self.obj211.postAction( rootNode.CREATE )

    self.obj212=CD_Inheritance3(self)
    self.obj212.isGraphObjectVisual = True

    if(hasattr(self.obj212, '_setHierarchicalLink')):
      self.obj212._setHierarchicalLink(False)

    self.obj212.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1709.875,2237.5,self.obj212)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj212.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj212)
    self.globalAndLocalPostcondition(self.obj212, rootNode)
    self.obj212.postAction( rootNode.CREATE )

    self.obj213=CD_Inheritance3(self)
    self.obj213.isGraphObjectVisual = True

    if(hasattr(self.obj213, '_setHierarchicalLink')):
      self.obj213._setHierarchicalLink(False)

    self.obj213.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1709.875,2327.5,self.obj213)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj213.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj213)
    self.globalAndLocalPostcondition(self.obj213, rootNode)
    self.obj213.postAction( rootNode.CREATE )

    self.obj214=CD_Inheritance3(self)
    self.obj214.isGraphObjectVisual = True

    if(hasattr(self.obj214, '_setHierarchicalLink')):
      self.obj214._setHierarchicalLink(False)

    self.obj214.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1591.90625,560.581045082,self.obj214)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj214.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj214)
    self.globalAndLocalPostcondition(self.obj214, rootNode)
    self.obj214.postAction( rootNode.CREATE )

    self.obj215=CD_Inheritance3(self)
    self.obj215.isGraphObjectVisual = True

    if(hasattr(self.obj215, '_setHierarchicalLink')):
      self.obj215._setHierarchicalLink(False)

    self.obj215.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1604.96875,567.581045082,self.obj215)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj215.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj215)
    self.globalAndLocalPostcondition(self.obj215, rootNode)
    self.obj215.postAction( rootNode.CREATE )

    self.obj216=CD_Inheritance3(self)
    self.obj216.isGraphObjectVisual = True

    if(hasattr(self.obj216, '_setHierarchicalLink')):
      self.obj216._setHierarchicalLink(False)

    self.obj216.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1617.03125,604.581045082,self.obj216)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj216.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj216)
    self.globalAndLocalPostcondition(self.obj216, rootNode)
    self.obj216.postAction( rootNode.CREATE )

    self.obj217=CD_Inheritance3(self)
    self.obj217.isGraphObjectVisual = True

    if(hasattr(self.obj217, '_setHierarchicalLink')):
      self.obj217._setHierarchicalLink(False)

    self.obj217.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1345.8515625,365.892520492,self.obj217)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj217.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj217)
    self.globalAndLocalPostcondition(self.obj217, rootNode)
    self.obj217.postAction( rootNode.CREATE )

    self.obj218=CD_Inheritance3(self)
    self.obj218.isGraphObjectVisual = True

    if(hasattr(self.obj218, '_setHierarchicalLink')):
      self.obj218._setHierarchicalLink(False)

    self.obj218.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1319.90625,427.581045082,self.obj218)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj218.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj218)
    self.globalAndLocalPostcondition(self.obj218, rootNode)
    self.obj218.postAction( rootNode.CREATE )

    self.obj219=CD_Inheritance3(self)
    self.obj219.isGraphObjectVisual = True

    if(hasattr(self.obj219, '_setHierarchicalLink')):
      self.obj219._setHierarchicalLink(False)

    self.obj219.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1325.90625,435.581045082,self.obj219)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj219.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj219)
    self.globalAndLocalPostcondition(self.obj219, rootNode)
    self.obj219.postAction( rootNode.CREATE )

    self.obj220=CD_Inheritance3(self)
    self.obj220.isGraphObjectVisual = True

    if(hasattr(self.obj220, '_setHierarchicalLink')):
      self.obj220._setHierarchicalLink(False)

    self.obj220.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1206.3515625,443.892520492,self.obj220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj220)
    self.globalAndLocalPostcondition(self.obj220, rootNode)
    self.obj220.postAction( rootNode.CREATE )

    self.obj221=CD_Inheritance3(self)
    self.obj221.isGraphObjectVisual = True

    if(hasattr(self.obj221, '_setHierarchicalLink')):
      self.obj221._setHierarchicalLink(False)

    self.obj221.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1226.40625,478.581045082,self.obj221)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj221.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj221)
    self.globalAndLocalPostcondition(self.obj221, rootNode)
    self.obj221.postAction( rootNode.CREATE )

    self.obj222=CD_Inheritance3(self)
    self.obj222.isGraphObjectVisual = True

    if(hasattr(self.obj222, '_setHierarchicalLink')):
      self.obj222._setHierarchicalLink(False)

    self.obj222.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1086.3515625,443.892520492,self.obj222)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj222.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj222)
    self.globalAndLocalPostcondition(self.obj222, rootNode)
    self.obj222.postAction( rootNode.CREATE )

    self.obj223=CD_Inheritance3(self)
    self.obj223.isGraphObjectVisual = True

    if(hasattr(self.obj223, '_setHierarchicalLink')):
      self.obj223._setHierarchicalLink(False)

    self.obj223.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1102.8515625,523.892520492,self.obj223)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj223.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj223)
    self.globalAndLocalPostcondition(self.obj223, rootNode)
    self.obj223.postAction( rootNode.CREATE )

    self.obj224=CD_Inheritance3(self)
    self.obj224.isGraphObjectVisual = True

    if(hasattr(self.obj224, '_setHierarchicalLink')):
      self.obj224._setHierarchicalLink(False)

    self.obj224.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(866.3515625,503.892520492,self.obj224)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj224.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj224)
    self.globalAndLocalPostcondition(self.obj224, rootNode)
    self.obj224.postAction( rootNode.CREATE )

    self.obj225=CD_Inheritance3(self)
    self.obj225.isGraphObjectVisual = True

    if(hasattr(self.obj225, '_setHierarchicalLink')):
      self.obj225._setHierarchicalLink(False)

    self.obj225.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(986.3515625,513.892520492,self.obj225)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj225.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj225)
    self.globalAndLocalPostcondition(self.obj225, rootNode)
    self.obj225.postAction( rootNode.CREATE )

    self.obj226=CD_Inheritance3(self)
    self.obj226.isGraphObjectVisual = True

    if(hasattr(self.obj226, '_setHierarchicalLink')):
      self.obj226._setHierarchicalLink(False)

    self.obj226.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(866.3515625,583.892520492,self.obj226)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj226.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj226)
    self.globalAndLocalPostcondition(self.obj226, rootNode)
    self.obj226.postAction( rootNode.CREATE )

    self.obj227=CD_Inheritance3(self)
    self.obj227.isGraphObjectVisual = True

    if(hasattr(self.obj227, '_setHierarchicalLink')):
      self.obj227._setHierarchicalLink(False)

    self.obj227.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(966.3515625,593.892520492,self.obj227)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj227.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj227)
    self.globalAndLocalPostcondition(self.obj227, rootNode)
    self.obj227.postAction( rootNode.CREATE )

    self.obj228=CD_Inheritance3(self)
    self.obj228.isGraphObjectVisual = True

    if(hasattr(self.obj228, '_setHierarchicalLink')):
      self.obj228._setHierarchicalLink(False)

    self.obj228.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1098.8515625,633.892520492,self.obj228)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj228.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj228)
    self.globalAndLocalPostcondition(self.obj228, rootNode)
    self.obj228.postAction( rootNode.CREATE )

    self.obj229=CD_Inheritance3(self)
    self.obj229.isGraphObjectVisual = True

    if(hasattr(self.obj229, '_setHierarchicalLink')):
      self.obj229._setHierarchicalLink(False)

    self.obj229.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(954.8515625,705.892520492,self.obj229)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj229.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj229)
    self.globalAndLocalPostcondition(self.obj229, rootNode)
    self.obj229.postAction( rootNode.CREATE )

    self.obj230=CD_Inheritance3(self)
    self.obj230.isGraphObjectVisual = True

    if(hasattr(self.obj230, '_setHierarchicalLink')):
      self.obj230._setHierarchicalLink(False)

    self.obj230.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1230.90625,529.581045082,self.obj230)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj230.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj230)
    self.globalAndLocalPostcondition(self.obj230, rootNode)
    self.obj230.postAction( rootNode.CREATE )

    self.obj231=CD_Inheritance3(self)
    self.obj231.isGraphObjectVisual = True

    if(hasattr(self.obj231, '_setHierarchicalLink')):
      self.obj231._setHierarchicalLink(False)

    self.obj231.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1272.28125,668.581045082,self.obj231)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj231.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj231)
    self.globalAndLocalPostcondition(self.obj231, rootNode)
    self.obj231.postAction( rootNode.CREATE )

    self.obj232=CD_Inheritance3(self)
    self.obj232.isGraphObjectVisual = True

    if(hasattr(self.obj232, '_setHierarchicalLink')):
      self.obj232._setHierarchicalLink(False)

    self.obj232.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1019.90625,835.581045082,self.obj232)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj232.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj232)
    self.globalAndLocalPostcondition(self.obj232, rootNode)
    self.obj232.postAction( rootNode.CREATE )

    self.obj233=CD_Inheritance3(self)
    self.obj233.isGraphObjectVisual = True

    if(hasattr(self.obj233, '_setHierarchicalLink')):
      self.obj233._setHierarchicalLink(False)

    self.obj233.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1159.90625,835.581045082,self.obj233)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj233.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj233)
    self.globalAndLocalPostcondition(self.obj233, rootNode)
    self.obj233.postAction( rootNode.CREATE )

    self.obj234=CD_Inheritance3(self)
    self.obj234.isGraphObjectVisual = True

    if(hasattr(self.obj234, '_setHierarchicalLink')):
      self.obj234._setHierarchicalLink(False)

    self.obj234.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1279.90625,835.581045082,self.obj234)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj234.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj234)
    self.globalAndLocalPostcondition(self.obj234, rootNode)
    self.obj234.postAction( rootNode.CREATE )

    self.obj235=CD_Inheritance3(self)
    self.obj235.isGraphObjectVisual = True

    if(hasattr(self.obj235, '_setHierarchicalLink')):
      self.obj235._setHierarchicalLink(False)

    self.obj235.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1399.90625,835.581045082,self.obj235)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj235.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj235)
    self.globalAndLocalPostcondition(self.obj235, rootNode)
    self.obj235.postAction( rootNode.CREATE )

    self.obj236=CD_Inheritance3(self)
    self.obj236.isGraphObjectVisual = True

    if(hasattr(self.obj236, '_setHierarchicalLink')):
      self.obj236._setHierarchicalLink(False)

    self.obj236.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1449.90625,835.581045082,self.obj236)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj236.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj236)
    self.globalAndLocalPostcondition(self.obj236, rootNode)
    self.obj236.postAction( rootNode.CREATE )

    self.obj237=CD_Inheritance3(self)
    self.obj237.isGraphObjectVisual = True

    if(hasattr(self.obj237, '_setHierarchicalLink')):
      self.obj237._setHierarchicalLink(False)

    self.obj237.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1622.09375,835.581045082,self.obj237)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj237.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj237)
    self.globalAndLocalPostcondition(self.obj237, rootNode)
    self.obj237.postAction( rootNode.CREATE )

    self.obj238=CD_Inheritance3(self)
    self.obj238.isGraphObjectVisual = True

    if(hasattr(self.obj238, '_setHierarchicalLink')):
      self.obj238._setHierarchicalLink(False)

    self.obj238.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1722.09375,835.581045082,self.obj238)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj238.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj238)
    self.globalAndLocalPostcondition(self.obj238, rootNode)
    self.obj238.postAction( rootNode.CREATE )

    self.obj239=CD_Inheritance3(self)
    self.obj239.isGraphObjectVisual = True

    if(hasattr(self.obj239, '_setHierarchicalLink')):
      self.obj239._setHierarchicalLink(False)

    self.obj239.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1822.09375,835.581045082,self.obj239)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj239.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj239)
    self.globalAndLocalPostcondition(self.obj239, rootNode)
    self.obj239.postAction( rootNode.CREATE )

    self.obj240=CD_Inheritance3(self)
    self.obj240.isGraphObjectVisual = True

    if(hasattr(self.obj240, '_setHierarchicalLink')):
      self.obj240._setHierarchicalLink(False)

    self.obj240.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1932.09375,835.581045082,self.obj240)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj240.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj240)
    self.globalAndLocalPostcondition(self.obj240, rootNode)
    self.obj240.postAction( rootNode.CREATE )

    self.obj241=CD_Inheritance3(self)
    self.obj241.isGraphObjectVisual = True

    if(hasattr(self.obj241, '_setHierarchicalLink')):
      self.obj241._setHierarchicalLink(False)

    self.obj241.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1149.90625,915.581045082,self.obj241)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj241.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj241)
    self.globalAndLocalPostcondition(self.obj241, rootNode)
    self.obj241.postAction( rootNode.CREATE )

    self.obj242=CD_Inheritance3(self)
    self.obj242.isGraphObjectVisual = True

    if(hasattr(self.obj242, '_setHierarchicalLink')):
      self.obj242._setHierarchicalLink(False)

    self.obj242.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1299.90625,925.581045082,self.obj242)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj242.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj242)
    self.globalAndLocalPostcondition(self.obj242, rootNode)
    self.obj242.postAction( rootNode.CREATE )

    self.obj243=CD_Inheritance3(self)
    self.obj243.isGraphObjectVisual = True

    if(hasattr(self.obj243, '_setHierarchicalLink')):
      self.obj243._setHierarchicalLink(False)

    self.obj243.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1429.90625,925.581045082,self.obj243)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj243.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj243)
    self.globalAndLocalPostcondition(self.obj243, rootNode)
    self.obj243.postAction( rootNode.CREATE )

    self.obj244=CD_Inheritance3(self)
    self.obj244.isGraphObjectVisual = True

    if(hasattr(self.obj244, '_setHierarchicalLink')):
      self.obj244._setHierarchicalLink(False)

    self.obj244.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1538.03125,925.581045082,self.obj244)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj244.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj244)
    self.globalAndLocalPostcondition(self.obj244, rootNode)
    self.obj244.postAction( rootNode.CREATE )

    self.obj245=CD_Inheritance3(self)
    self.obj245.isGraphObjectVisual = True

    if(hasattr(self.obj245, '_setHierarchicalLink')):
      self.obj245._setHierarchicalLink(False)

    self.obj245.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1822.09375,925.581045082,self.obj245)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj245.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj245)
    self.globalAndLocalPostcondition(self.obj245, rootNode)
    self.obj245.postAction( rootNode.CREATE )

    self.obj246=CD_Inheritance3(self)
    self.obj246.isGraphObjectVisual = True

    if(hasattr(self.obj246, '_setHierarchicalLink')):
      self.obj246._setHierarchicalLink(False)

    self.obj246.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1942.09375,925.581045082,self.obj246)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj246.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj246)
    self.globalAndLocalPostcondition(self.obj246, rootNode)
    self.obj246.postAction( rootNode.CREATE )

    self.obj247=CD_Inheritance3(self)
    self.obj247.isGraphObjectVisual = True

    if(hasattr(self.obj247, '_setHierarchicalLink')):
      self.obj247._setHierarchicalLink(False)

    self.obj247.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1159.90625,1005.58104508,self.obj247)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj247.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj247)
    self.globalAndLocalPostcondition(self.obj247, rootNode)
    self.obj247.postAction( rootNode.CREATE )

    self.obj248=CD_Inheritance3(self)
    self.obj248.isGraphObjectVisual = True

    if(hasattr(self.obj248, '_setHierarchicalLink')):
      self.obj248._setHierarchicalLink(False)

    self.obj248.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1269.90625,1005.58104508,self.obj248)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj248.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj248)
    self.globalAndLocalPostcondition(self.obj248, rootNode)
    self.obj248.postAction( rootNode.CREATE )

    self.obj249=CD_Inheritance3(self)
    self.obj249.isGraphObjectVisual = True

    if(hasattr(self.obj249, '_setHierarchicalLink')):
      self.obj249._setHierarchicalLink(False)

    self.obj249.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2776.0,621.0,self.obj249)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj249.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj249)
    self.globalAndLocalPostcondition(self.obj249, rootNode)
    self.obj249.postAction( rootNode.CREATE )

    self.obj250=CD_Inheritance3(self)
    self.obj250.isGraphObjectVisual = True

    if(hasattr(self.obj250, '_setHierarchicalLink')):
      self.obj250._setHierarchicalLink(False)

    self.obj250.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2894.0,689.0,self.obj250)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj250.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj250)
    self.globalAndLocalPostcondition(self.obj250, rootNode)
    self.obj250.postAction( rootNode.CREATE )

    self.obj254=CD_Inheritance3(self)
    self.obj254.isGraphObjectVisual = True

    if(hasattr(self.obj254, '_setHierarchicalLink')):
      self.obj254._setHierarchicalLink(False)

    self.obj254.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(3041.0,1141.0,self.obj254)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj254.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj254)
    self.globalAndLocalPostcondition(self.obj254, rootNode)
    self.obj254.postAction( rootNode.CREATE )

    self.obj255=CD_Inheritance3(self)
    self.obj255.isGraphObjectVisual = True

    if(hasattr(self.obj255, '_setHierarchicalLink')):
      self.obj255._setHierarchicalLink(False)

    self.obj255.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(3125.0,1119.0,self.obj255)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj255.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj255)
    self.globalAndLocalPostcondition(self.obj255, rootNode)
    self.obj255.postAction( rootNode.CREATE )

    self.obj256=CD_Inheritance3(self)
    self.obj256.isGraphObjectVisual = True

    if(hasattr(self.obj256, '_setHierarchicalLink')):
      self.obj256._setHierarchicalLink(False)

    self.obj256.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(3177.0,1132.0,self.obj256)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj256.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj256)
    self.globalAndLocalPostcondition(self.obj256, rootNode)
    self.obj256.postAction( rootNode.CREATE )

    self.obj257=CD_Inheritance3(self)
    self.obj257.isGraphObjectVisual = True

    if(hasattr(self.obj257, '_setHierarchicalLink')):
      self.obj257._setHierarchicalLink(False)

    self.obj257.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2950.5,825.848360656,self.obj257)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj257.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj257)
    self.globalAndLocalPostcondition(self.obj257, rootNode)
    self.obj257.postAction( rootNode.CREATE )

    self.obj258=CD_Inheritance3(self)
    self.obj258.isGraphObjectVisual = True

    if(hasattr(self.obj258, '_setHierarchicalLink')):
      self.obj258._setHierarchicalLink(False)

    self.obj258.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2866.0,749.5,self.obj258)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj258.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj258)
    self.globalAndLocalPostcondition(self.obj258, rootNode)
    self.obj258.postAction( rootNode.CREATE )

    self.obj259=CD_Inheritance3(self)
    self.obj259.isGraphObjectVisual = True

    if(hasattr(self.obj259, '_setHierarchicalLink')):
      self.obj259._setHierarchicalLink(False)

    self.obj259.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(2913.0,841.5,self.obj259)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj259.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj259)
    self.globalAndLocalPostcondition(self.obj259, rootNode)
    self.obj259.postAction( rootNode.CREATE )

    self.obj260=CD_Inheritance3(self)
    self.obj260.isGraphObjectVisual = True

    if(hasattr(self.obj260, '_setHierarchicalLink')):
      self.obj260._setHierarchicalLink(False)

    self.obj260.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(3036.0,646.848360656,self.obj260)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj260.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj260)
    self.globalAndLocalPostcondition(self.obj260, rootNode)
    self.obj260.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named MatchModel
    self.drawConnections(
(self.obj28,self.obj112,[100.0, 221.0, 121.0, 395.0],"true", 2),
(self.obj28,self.obj113,[271.2265625, 121.0, 745.5625, 123.0],"true", 2) )
    # Connections for obj29 (graphObject_: Obj1) named ApplyModel
    self.drawConnections(
(self.obj29,self.obj114,[277.8984375, 1938.0, 572.123046875, 1947.0],"true", 2) )
    # Connections for obj30 (graphObject_: Obj2) named MetaModelElement_S
    self.drawConnections(
(self.obj30,self.obj116,[1630.296875, 155.20307377055735, 1853.2421875, 89.0, 1853.2421875, 89.0],"true", 3),
(self.obj30,self.obj117,[1630.296875, 220.9915983607213, 1846.7421875, 223.5, 1846.7421875, 223.5],"true", 3),
(self.obj30,self.obj120,[1630.296875, 343.1702868853115, 2023.6484375, 402.89252049183608, 2291.32421875, 496.44626024600001],"true", 3) )
    # Connections for obj31 (graphObject_: Obj3) named MetaModelElement_T
    self.drawConnections(
(self.obj31,self.obj115,[1605.09375, 1860.188524590164, 1969.5800781249995, 1860.0, 1969.5800781200001, 1860.0],"true", 3),
(self.obj31,self.obj118,[1605.09375, 1860.188524590164, 1988.0, 1743.0, 1991.5, 1063.0],"true", 3),
(self.obj31,self.obj119,[1605.09375, 1860.188524590164, 2280.0, 1735.0, 2290.0, 1056.0],"true", 3),
(self.obj31,self.obj121,[1605.09375, 1860.188524590164, 2130.046875, 1727.1311475409836, 2412.7734375, 1464.0655737699999],"true", 3) )
    # Connections for obj32 (graphObject_: Obj4) named Element
    self.drawConnections(
(self.obj32,self.obj126,[456.0, 461.0, 460.953125, 310.04052254099997],"true", 2) )
    # Connections for obj33 (graphObject_: Obj5) named NamedElement
    self.drawConnections(
(self.obj33,self.obj127,[676.0, 941.0, 668.0, 934.0],"true", 2),
(self.obj33,self.obj228,[796.0, 941.0, 1098.8515625, 633.89252049183608],"true", 2) )
    # Connections for obj34 (graphObject_: Obj6) named Trigger_S
    self.drawConnections(
(self.obj34,self.obj128,[296.0, 641.0, 308.0, 622.0],"true", 2),
(self.obj34,self.obj224,[331.0, 681.0, 866.3515625, 503.89252049183608],"true", 2) )
    # Connections for obj35 (graphObject_: Obj7) named Action
    self.drawConnections(
(self.obj35,self.obj129,[296.0, 801.0, 349.0, 783.0],"true", 2),
(self.obj35,self.obj226,[331.0, 841.0, 866.3515625, 583.89252049183608],"true", 2) )
    # Connections for obj36 (graphObject_: Obj8) named PortRef
    self.drawConnections(
(self.obj36,self.obj131,[456.0, 661.0, 468.0, 645.0],"true", 2),
(self.obj36,self.obj225,[571.0, 701.0, 986.3515625, 513.89252049183608],"true", 2) )
    # Connections for obj37 (graphObject_: Obj9) named PortConnectorRef
    self.drawConnections(
(self.obj37,self.obj130,[376.0, 821.0, 372.0, 809.0],"true", 2),
(self.obj37,self.obj227,[531.0, 861.0, 966.3515625, 593.89252049183608],"true", 2) )
    # Connections for obj38 (graphObject_: Obj10) named StateMachineElement
    self.drawConnections(
(self.obj38,self.obj132,[938.25, 1121.0, 929.875, 1107.0],"true", 2),
(self.obj38,self.obj231,[1020.75, 1121.0, 1272.28125, 668.58104508199995],"true", 2) )
    # Connections for obj39 (graphObject_: Obj11) named Protocol
    self.drawConnections(
(self.obj39,self.obj133,[556.0, 1121.0, 618.0, 1074.0],"true", 2),
(self.obj39,self.obj229,[556.0, 1121.0, 954.8515625, 705.89252049183608],"true", 2) )
    # Connections for obj40 (graphObject_: Obj12) named Signal
    self.drawConnections(
(self.obj40,self.obj135,[596.0, 1301.0, 638.0, 1081.0],"true", 2),
(self.obj40,self.obj232,[596.0, 1301.0, 1019.90625, 835.58104508199995],"true", 2) )
    # Connections for obj41 (graphObject_: Obj13) named Port
    self.drawConnections(
(self.obj41,self.obj134,[796.0, 1121.0, 801.0, 1104.0],"true", 2),
(self.obj41,self.obj230,[796.0, 1121.0, 1230.90625, 529.58104508199995],"true", 2) )
    # Connections for obj42 (graphObject_: Obj14) named Vertex
    self.drawConnections(
(self.obj42,self.obj136,[876.0, 1301.0, 899.0, 1275.0],"true", 2),
(self.obj42,self.obj233,[876.0, 1301.0, 1159.90625, 835.58104508199995],"true", 2) )
    # Connections for obj43 (graphObject_: Obj15) named InitialPoint
    self.drawConnections(
(self.obj43,self.obj137,[856.0, 1461.0, 855.0, 1451.0],"true", 2),
(self.obj43,self.obj241,[856.0, 1461.0, 1149.90625, 915.58104508199995],"true", 2) )
    # Connections for obj44 (graphObject_: Obj16) named EntryPoint
    self.drawConnections(
(self.obj44,self.obj138,[876.0, 1641.0, 898.0, 1621.0],"true", 2),
(self.obj44,self.obj247,[876.0, 1641.0, 1159.90625, 1005.5810450819999],"true", 2) )
    # Connections for obj45 (graphObject_: Obj17) named ExitPoint
    self.drawConnections(
(self.obj45,self.obj139,[976.0, 1641.0, 930.0, 1522.0],"true", 2),
(self.obj45,self.obj248,[1096.0, 1641.0, 1269.90625, 1005.5810450819999],"true", 2) )
    # Connections for obj46 (graphObject_: Obj18) named Transition
    self.drawConnections(
(self.obj46,self.obj140,[1036.0, 1301.0, 1032.875, 1278.0],"true", 2),
(self.obj46,self.obj234,[1116.0, 1301.0, 1279.90625, 835.58104508199995],"true", 2) )
    # Connections for obj47 (graphObject_: Obj19) named StateMachine
    self.drawConnections(
(self.obj47,self.obj141,[1236.0, 1301.0, 1246.0, 1144.0],"true", 2),
(self.obj47,self.obj235,[1356.0, 1301.0, 1399.90625, 835.58104508199995],"true", 2) )
    # Connections for obj48 (graphObject_: Obj20) named State
    self.drawConnections(
(self.obj48,self.obj142,[1001.0, 1521.0, 961.0, 1487.0],"true", 2),
(self.obj48,self.obj143,[1156.0, 1481.0, 1208.0, 1461.0],"true", 2),
(self.obj48,self.obj242,[1156.0, 1481.0, 1299.90625, 925.58104508199995],"true", 2) )
    # Connections for obj49 (graphObject_: Obj21) named Capsule
    self.drawConnections(
(self.obj49,self.obj144,[1621.0, 1341.0, 1311.0, 1118.5],"true", 2),
(self.obj49,self.obj237,[1656.0, 1301.0, 1622.09375, 835.58104508199995],"true", 2) )
    # Connections for obj50 (graphObject_: Obj22) named PackageContainer
    self.drawConnections(
(self.obj50,self.obj145,[1456.0, 1301.0, 1302.0, 1129.0],"true", 2),
(self.obj50,self.obj236,[1456.0, 1301.0, 1449.90625, 835.58104508199995],"true", 2) )
    # Connections for obj51 (graphObject_: Obj23) named Model_S
    self.drawConnections(
(self.obj51,self.obj146,[1416.0, 1481.0, 1430.0, 1475.0],"true", 2),
(self.obj51,self.obj243,[1416.0, 1481.0, 1429.90625, 925.58104508199995],"true", 2) )
    # Connections for obj52 (graphObject_: Obj24) named Package
    self.drawConnections(
(self.obj52,self.obj147,[1536.0, 1481.0, 1510.0, 1455.0],"true", 2),
(self.obj52,self.obj244,[1536.0, 1481.0, 1538.03125, 925.58104508199995],"true", 2) )
    # Connections for obj53 (graphObject_: Obj25) named CapsuleRole
    self.drawConnections(
(self.obj53,self.obj148,[1821.0, 1341.0, 1328.0, 1095.0],"true", 2),
(self.obj53,self.obj238,[1856.0, 1301.0, 1722.09375, 835.58104508199995],"true", 2) )
    # Connections for obj54 (graphObject_: Obj26) named PortConnector
    self.drawConnections(
(self.obj54,self.obj149,[2021.0, 1341.0, 1334.0, 1089.0],"true", 2),
(self.obj54,self.obj239,[2056.0, 1301.0, 1822.09375, 835.58104508199995],"true", 2) )
    # Connections for obj55 (graphObject_: Obj27) named Thread
    self.drawConnections(
(self.obj55,self.obj150,[2241.0, 1341.0, 1329.0, 1078.0],"true", 2),
(self.obj55,self.obj240,[2276.0, 1301.0, 1932.09375, 835.58104508199995],"true", 2) )
    # Connections for obj56 (graphObject_: Obj28) named PhysicalThread
    self.drawConnections(
(self.obj56,self.obj151,[2211.0, 1521.0, 2232.0, 1488.0],"true", 2),
(self.obj56,self.obj245,[2056.0, 1481.0, 1822.09375, 925.58104508199995],"true", 2) )
    # Connections for obj57 (graphObject_: Obj29) named LogicalThread
    self.drawConnections(
(self.obj57,self.obj152,[2376.0, 1481.0, 2365.0, 1456.0],"true", 2),
(self.obj57,self.obj246,[2296.0, 1481.0, 1942.09375, 925.58104508199995],"true", 2) )
    # Connections for obj58 (graphObject_: Obj30) named PortType
    self.drawConnections(
(self.obj58,self.obj153,[736.0, 361.0, 742.3984375, 330.85199795084969],"true", 2) )
    # Connections for obj59 (graphObject_: Obj31) named BASE0
    self.drawConnections(
(self.obj59,self.obj154,[736.0, 521.0, 736.0, 511.0],"true", 2),
(self.obj59,self.obj222,[771.0, 561.0, 1086.3515625, 443.89252049183608],"true", 2) )
    # Connections for obj60 (graphObject_: Obj32) named CONJUGATE1
    self.drawConnections(
(self.obj60,self.obj155,[769.0, 681.0, 779.0, 671.0],"true", 2),
(self.obj60,self.obj223,[804.0, 721.0, 1102.8515625, 523.89252049183608],"true", 2) )
    # Connections for obj61 (graphObject_: Obj33) named SignalType
    self.drawConnections(
(self.obj61,self.obj158,[976.0, 361.0, 976.3984375, 337.4667520492103],"true", 2) )
    # Connections for obj62 (graphObject_: Obj34) named OUT1
    self.drawConnections(
(self.obj62,self.obj157,[1016.0, 681.0, 1020.6875, 661.95774647899998],"true", 2),
(self.obj62,self.obj221,[1016.0, 681.0, 1226.40625, 478.58104508199995],"true", 2) )
    # Connections for obj63 (graphObject_: Obj35) named IN0
    self.drawConnections(
(self.obj63,self.obj156,[936.0, 521.0, 936.0, 511.0],"true", 2),
(self.obj63,self.obj220,[1011.0, 561.0, 1206.3515625, 443.89252049183608],"true", 2) )
    # Connections for obj64 (graphObject_: Obj36) named RoleType
    self.drawConnections(
(self.obj64,self.obj159,[1236.0, 361.0, 1242.3984375, 350.4667520492103],"true", 2) )
    # Connections for obj65 (graphObject_: Obj37) named FIXED0
    self.drawConnections(
(self.obj65,self.obj160,[1156.0, 521.0, 1156.0, 511.0],"true", 2),
(self.obj65,self.obj217,[1196.0, 521.0, 1345.8515625, 365.89252049183608],"true", 2) )
    # Connections for obj66 (graphObject_: Obj38) named OPTIONAL1
    self.drawConnections(
(self.obj66,self.obj161,[1236.0, 681.0, 1236.0, 591.0],"true", 2),
(self.obj66,self.obj218,[1236.0, 681.0, 1319.90625, 427.58104508199995],"true", 2) )
    # Connections for obj67 (graphObject_: Obj39) named PLUGIN2
    self.drawConnections(
(self.obj67,self.obj162,[1256.0, 841.0, 1302.0, 812.0],"true", 2),
(self.obj67,self.obj219,[1256.0, 841.0, 1325.90625, 435.58104508199995],"true", 2) )
    # Connections for obj68 (graphObject_: Obj40) named TransitionType
    self.drawConnections(
(self.obj68,self.obj163,[1536.0, 401.0, 1538.078125, 385.54052254101362],"true", 2) )
    # Connections for obj69 (graphObject_: Obj41) named SIBLING0
    self.drawConnections(
(self.obj69,self.obj164,[1456.0, 561.0, 1456.0, 551.0],"true", 2),
(self.obj69,self.obj214,[1491.0, 601.0, 1591.90625, 560.58104508199995],"true", 2) )
    # Connections for obj70 (graphObject_: Obj42) named IN1
    self.drawConnections(
(self.obj70,self.obj165,[1496.0, 721.0, 1506.0, 631.0],"true", 2),
(self.obj70,self.obj215,[1496.0, 721.0, 1604.96875, 567.58104508199995],"true", 2) )
    # Connections for obj71 (graphObject_: Obj43) named OUT2
    self.drawConnections(
(self.obj71,self.obj166,[1556.0, 881.0, 1550.0, 771.0],"true", 2),
(self.obj71,self.obj216,[1556.0, 881.0, 1617.03125, 604.58104508199995],"true", 2) )
    # Connections for obj72 (graphObject_: Obj44) named Def
    self.drawConnections(
(self.obj72,self.obj167,[256.0, 2081.0, 264.828125, 2024.4262295081967],"true", 2) )
    # Connections for obj73 (graphObject_: Obj45) named Expr
    self.drawConnections(
(self.obj73,self.obj168,[436.0, 2081.0, 451.828125, 2034.4262295081967],"true", 2) )
    # Connections for obj74 (graphObject_: Obj46) named Pattern
    self.drawConnections(
(self.obj74,self.obj169,[576.0, 2081.0, 594.828125, 2052.4262295081967],"true", 2) )
    # Connections for obj75 (graphObject_: Obj47) named Proc
    self.drawConnections(
(self.obj75,self.obj170,[1976.0, 2081.0, 1972.828125, 2057.4262295081967],"true", 2) )
    # Connections for obj76 (graphObject_: Obj48) named ProcDef
    self.drawConnections(
(self.obj76,self.obj171,[171.0, 2261.0, 176.0, 2241.0],"true", 2),
(self.obj76,self.obj196,[206.0, 2301.0, 798.328125, 2158.4262295081967],"true", 2) )
    # Connections for obj77 (graphObject_: Obj49) named FuncDef
    self.drawConnections(
(self.obj77,self.obj172,[216.0, 2601.0, 225.0, 2586.0],"true", 2),
(self.obj77,self.obj198,[251.0, 2641.0, 815.828125, 2319.4262295081967],"true", 2) )
    # Connections for obj78 (graphObject_: Obj50) named Name
    self.drawConnections(
(self.obj78,self.obj173,[776.0, 2081.0, 794.828125, 2061.4262295081967],"true", 2) )
    # Connections for obj79 (graphObject_: Obj51) named PythonRef
    self.drawConnections(
(self.obj79,self.obj174,[816.0, 2261.0, 826.0, 2245.0],"true", 2),
(self.obj79,self.obj199,[931.0, 2301.0, 1155.828125, 2149.4262295081967],"true", 2) )
    # Connections for obj80 (graphObject_: Obj52) named Module
    self.drawConnections(
(self.obj80,self.obj175,[136.0, 2441.0, 133.5, 2421.0],"true", 2),
(self.obj80,self.obj197,[211.0, 2481.0, 795.828125, 2239.4262295081967],"true", 2) )
    # Connections for obj81 (graphObject_: Obj53) named Null
    self.drawConnections(
(self.obj81,self.obj176,[1936.0, 2261.0, 1953.5, 2252.0],"true", 2),
(self.obj81,self.obj201,[1856.0, 2261.0, 1730.546875, 2129.4262295081967],"true", 2) )
    # Connections for obj82 (graphObject_: Obj54) named Trigger_T
    self.drawConnections(
(self.obj82,self.obj177,[2076.0, 2261.0, 2067.0, 2246.0],"true", 2),
(self.obj82,self.obj202,[2041.0, 2301.0, 1823.046875, 2149.4262295081967],"true", 2) )
    # Connections for obj83 (graphObject_: Obj55) named Listen
    self.drawConnections(
(self.obj83,self.obj178,[2336.0, 2261.0, 2338.5, 2248.0],"true", 2),
(self.obj83,self.obj203,[2261.0, 2301.0, 1933.046875, 2149.4262295081967],"true", 2) )
    # Connections for obj84 (graphObject_: Obj56) named ConditionBranch
    self.drawConnections(
(self.obj84,self.obj179,[1776.0, 2081.0, 1776.046875, 2063.4262295081967],"true", 2) )
    # Connections for obj85 (graphObject_: Obj57) named ListenBranch
    self.drawConnections(
(self.obj85,self.obj180,[1056.0, 2081.0, 1057.828125, 2058.4262295081967],"true", 2) )
    # Connections for obj86 (graphObject_: Obj58) named Site
    self.drawConnections(
(self.obj86,self.obj181,[1176.0, 2081.0, 1176.328125, 2056.4262295081967],"true", 2) )
    # Connections for obj87 (graphObject_: Obj59) named Model_T
    self.drawConnections(
(self.obj87,self.obj182,[1456.0, 2081.0, 1462.625, 2057.5],"true", 2) )
    # Connections for obj88 (graphObject_: Obj60) named MatchCase
    self.drawConnections(
(self.obj88,self.obj183,[1576.0, 2081.0, 1569.875, 2057.5],"true", 2) )
    # Connections for obj89 (graphObject_: Obj61) named Condition
    self.drawConnections(
(self.obj89,self.obj184,[1776.0, 2261.0, 1776.5, 2265.0],"true", 2),
(self.obj89,self.obj185,[1776.0, 2261.0, 1778.0, 2251.0],"true", 2),
(self.obj89,self.obj200,[1656.0, 2261.0, 1609.875, 2147.5],"true", 2) )
    # Connections for obj90 (graphObject_: Obj62) named New
    self.drawConnections(
(self.obj90,self.obj186,[2516.0, 2261.0, 2483.0, 2243.0],"true", 2),
(self.obj90,self.obj204,[2481.0, 2301.0, 2043.046875, 2149.4262295081967],"true", 2) )
    # Connections for obj91 (graphObject_: Obj63) named Delay
    self.drawConnections(
(self.obj91,self.obj187,[2716.0, 2261.0, 2700.0, 2239.0],"true", 2),
(self.obj91,self.obj205,[2681.0, 2301.0, 2143.046875, 2149.4262295081967],"true", 2) )
    # Connections for obj92 (graphObject_: Obj64) named Par
    self.drawConnections(
(self.obj92,self.obj188,[2011.0, 2481.0, 2021.0, 2479.0],"true", 2),
(self.obj92,self.obj212,[1856.0, 2441.0, 1709.875, 2237.5],"true", 2) )
    # Connections for obj93 (graphObject_: Obj65) named ParIndexed
    self.drawConnections(
(self.obj93,self.obj189,[2041.0, 2481.0, 2031.0, 2479.0],"true", 2),
(self.obj93,self.obj211,[2076.0, 2441.0, 1840.546875, 2219.4262295081967],"true", 2) )
    # Connections for obj94 (graphObject_: Obj66) named Inst
    self.drawConnections(
(self.obj94,self.obj190,[2276.0, 2441.0, 2230.5, 2240.0],"true", 2),
(self.obj94,self.obj210,[2241.0, 2481.0, 1923.046875, 2239.4262295081967],"true", 2) )
    # Connections for obj95 (graphObject_: Obj67) named LocalDef
    self.drawConnections(
(self.obj95,self.obj191,[2476.0, 2441.0, 2467.5, 2256.0],"true", 2),
(self.obj95,self.obj209,[2441.0, 2481.0, 2023.046875, 2239.4262295081967],"true", 2) )
    # Connections for obj96 (graphObject_: Obj68) named Seq
    self.drawConnections(
(self.obj96,self.obj192,[1896.0, 2621.0, 1896.0, 2601.0],"true", 2),
(self.obj96,self.obj213,[1856.0, 2621.0, 1709.875, 2327.5],"true", 2) )
    # Connections for obj97 (graphObject_: Obj69) named ConditionSet
    self.drawConnections(
(self.obj97,self.obj193,[2676.0, 2441.0, 2675.0, 2249.0],"true", 2),
(self.obj97,self.obj208,[2641.0, 2481.0, 2124.046875, 2255.4262295081967],"true", 2) )
    # Connections for obj98 (graphObject_: Obj70) named Match
    self.drawConnections(
(self.obj98,self.obj195,[2922.0, 2261.0, 2900.0, 2225.0],"true", 2),
(self.obj98,self.obj206,[2887.0, 2301.0, 2246.046875, 2149.4262295081967],"true", 2) )
    # Connections for obj99 (graphObject_: Obj71) named Print
    self.drawConnections(
(self.obj99,self.obj194,[2876.0, 2441.0, 2876.0, 2237.0],"true", 2),
(self.obj99,self.obj207,[2841.0, 2481.0, 2223.046875, 2239.4262295081967],"true", 2) )
    # Connections for obj100 (graphObject_: Obj72) named Attribute
    self.drawConnections(
(self.obj100,self.obj249,[2788.59375, 661.0, 2776.0, 621.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj73) named Expression
    self.drawConnections(
 )
    # Connections for obj102 (graphObject_: Obj74) named Equation
    self.drawConnections(
(self.obj102,self.obj122,[2776.0, 221.0, 2715.0, 299.0],"true", 2),
(self.obj102,self.obj123,[2896.0, 221.0, 2930.15625, 299.0],"true", 2) )
    # Connections for obj103 (graphObject_: Obj75) named Operation
    self.drawConnections(
(self.obj103,self.obj250,[3036.0, 961.0, 2894.0, 689.0],"true", 2),
(self.obj103,self.obj124,[3076.0, 961.0, 3067.5, 791.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj80) named Add
    self.drawConnections(
(self.obj108,self.obj254,[3011.0, 1181.0, 3041.0, 1141.0],"true", 2),
(self.obj108,self.obj258,[2856.0, 1141.0, 2866.0, 749.5],"true", 2) )
    # Connections for obj109 (graphObject_: Obj81) named Subtract
    self.drawConnections(
(self.obj109,self.obj255,[3116.0, 1141.0, 3125.0, 1119.0],"true", 2),
(self.obj109,self.obj257,[3116.0, 1141.0, 2950.5, 825.84836065573768],"true", 2) )
    # Connections for obj110 (graphObject_: Obj82) named Concat
    self.drawConnections(
(self.obj110,self.obj256,[3116.0, 1301.0, 3177.0, 1132.0],"true", 2),
(self.obj110,self.obj259,[2996.0, 1301.0, 2913.0, 841.5],"true", 2) )
    # Connections for obj111 (graphObject_: Obj83) named Constant
    self.drawConnections(
(self.obj111,self.obj260,[3181.0, 701.0, 3036.0, 646.84836065573768],"true", 2) )
    # Connections for obj112 (graphObject_: Obj84) named paired_with
    self.drawConnections(
(self.obj112,self.obj29,[121.0, 395.0, 110.0625, 1870.0],"true", 2) )
    # Connections for obj113 (graphObject_: Obj86) named match_contains
    self.drawConnections(
(self.obj113,self.obj30,[745.5625, 123.0, 1401.703125, 155.20307377055735],"true", 2) )
    # Connections for obj114 (graphObject_: Obj88) named apply_contains
    self.drawConnections(
(self.obj114,self.obj31,[572.123046875, 1947.0, 1380.65625, 1969.5348360655737],"true", 2) )
    # Connections for obj115 (graphObject_: Obj90) named directLink_T
    self.drawConnections(
(self.obj115,self.obj31,[1969.5800781200001, 1860.0, 1969.5800781249995, 1860.0, 1605.09375, 1860.188524590164],"true", 3) )
    # Connections for obj116 (graphObject_: Obj92) named directLink_S
    self.drawConnections(
(self.obj116,self.obj30,[1853.2421875, 89.0, 1675.2421875, 130.0, 1630.296875, 155.20307377055735],"true", 3) )
    # Connections for obj117 (graphObject_: Obj94) named indirectLink_S
    self.drawConnections(
(self.obj117,self.obj30,[1846.7421875, 223.5, 1868.7421875, 299.5, 1630.296875, 284.43053278695083],"true", 3) )
    # Connections for obj118 (graphObject_: Obj96) named backward_link
    self.drawConnections(
(self.obj118,self.obj30,[1991.5, 1063.0, 1995.0, 383.0, 1630.296875, 343.1702868853115],"true", 3) )
    # Connections for obj119 (graphObject_: Obj98) named trace_link
    self.drawConnections(
(self.obj119,self.obj30,[2290.0, 1056.0, 2300.0, 377.0, 1630.296875, 343.1702868853115],"true", 3) )
    # Connections for obj120 (graphObject_: Obj100) named hasAttribute_S
    self.drawConnections(
(self.obj120,self.obj100,[2291.32421875, 496.44626024600001, 2559.0, 590.0, 2701.23046875, 701.0],"true", 3) )
    # Connections for obj121 (graphObject_: Obj102) named hasAttribute_T
    self.drawConnections(
(self.obj121,self.obj100,[2412.7734375, 1464.0655737699999, 2695.5, 1201.0, 2742.0, 801.0],"true", 3) )
    # Connections for obj122 (graphObject_: Obj104) named leftExpr
    self.drawConnections(
(self.obj122,self.obj101,[2715.0, 299.0, 2736.0, 420.87704918032784],"true", 2) )
    # Connections for obj123 (graphObject_: Obj106) named rightExpr
    self.drawConnections(
(self.obj123,self.obj101,[2930.15625, 299.0, 2856.0, 420.87704918032784],"true", 2) )
    # Connections for obj124 (graphObject_: Obj108) named hasArgs
    self.drawConnections(
(self.obj124,self.obj101,[3067.5, 791.0, 2891.0, 572.69672131147536],"true", 2) )
    # Connections for obj126 (graphObject_: Obj112) of type CD_Inheritance3
    self.drawConnections(
(self.obj126,self.obj30,[460.953125, 310.04052254099997, 1401.703125, 284.43053278695083],"true", 2) )
    # Connections for obj127 (graphObject_: Obj114) of type CD_Inheritance3
    self.drawConnections(
(self.obj127,self.obj32,[668.0, 934.0, 496.0, 601.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj116) of type CD_Inheritance3
    self.drawConnections(
(self.obj128,self.obj32,[308.0, 622.0, 341.0, 581.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj118) of type CD_Inheritance3
    self.drawConnections(
(self.obj129,self.obj32,[349.0, 783.0, 376.0, 601.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj120) of type CD_Inheritance3
    self.drawConnections(
(self.obj130,self.obj32,[372.0, 809.0, 376.0, 601.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj122) of type CD_Inheritance3
    self.drawConnections(
(self.obj131,self.obj32,[468.0, 645.0, 456.0, 601.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj124) of type CD_Inheritance3
    self.drawConnections(
(self.obj132,self.obj33,[929.875, 1107.0, 831.0, 1061.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj126) of type CD_Inheritance3
    self.drawConnections(
(self.obj133,self.obj33,[618.0, 1074.0, 641.0, 1061.0],"true", 2) )
    # Connections for obj134 (graphObject_: Obj128) of type CD_Inheritance3
    self.drawConnections(
(self.obj134,self.obj33,[801.0, 1104.0, 796.0, 1081.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj130) of type CD_Inheritance3
    self.drawConnections(
(self.obj135,self.obj33,[638.0, 1081.0, 641.0, 1061.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj132) of type CD_Inheritance3
    self.drawConnections(
(self.obj136,self.obj38,[899.0, 1275.0, 897.0, 1261.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj134) of type CD_Inheritance3
    self.drawConnections(
(self.obj137,self.obj42,[855.0, 1451.0, 836.0, 1441.0],"true", 2) )
    # Connections for obj138 (graphObject_: Obj136) of type CD_Inheritance3
    self.drawConnections(
(self.obj138,self.obj42,[898.0, 1621.0, 876.0, 1441.0],"true", 2) )
    # Connections for obj139 (graphObject_: Obj138) of type CD_Inheritance3
    self.drawConnections(
(self.obj139,self.obj42,[930.0, 1522.0, 876.0, 1441.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj140) of type CD_Inheritance3
    self.drawConnections(
(self.obj140,self.obj38,[1032.875, 1278.0, 1020.75, 1261.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj142) of type CD_Inheritance3
    self.drawConnections(
(self.obj141,self.obj33,[1246.0, 1144.0, 831.0, 1061.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj144) of type CD_Inheritance3
    self.drawConnections(
(self.obj142,self.obj42,[961.0, 1487.0, 911.0, 1421.0],"true", 2) )
    # Connections for obj143 (graphObject_: Obj146) of type CD_Inheritance3
    self.drawConnections(
(self.obj143,self.obj47,[1208.0, 1461.0, 1236.0, 1441.0],"true", 2) )
    # Connections for obj144 (graphObject_: Obj148) of type CD_Inheritance3
    self.drawConnections(
(self.obj144,self.obj33,[1311.0, 1118.5, 831.0, 1061.0],"true", 2) )
    # Connections for obj145 (graphObject_: Obj150) of type CD_Inheritance3
    self.drawConnections(
(self.obj145,self.obj33,[1302.0, 1129.0, 831.0, 1061.0],"true", 2) )
    # Connections for obj146 (graphObject_: Obj152) of type CD_Inheritance3
    self.drawConnections(
(self.obj146,self.obj50,[1430.0, 1475.0, 1456.0, 1441.0],"true", 2) )
    # Connections for obj147 (graphObject_: Obj154) of type CD_Inheritance3
    self.drawConnections(
(self.obj147,self.obj50,[1510.0, 1455.0, 1496.0, 1441.0],"true", 2) )
    # Connections for obj148 (graphObject_: Obj156) of type CD_Inheritance3
    self.drawConnections(
(self.obj148,self.obj33,[1328.0, 1095.0, 831.0, 1061.0],"true", 2) )
    # Connections for obj149 (graphObject_: Obj158) of type CD_Inheritance3
    self.drawConnections(
(self.obj149,self.obj33,[1334.0, 1089.0, 831.0, 1061.0],"true", 2) )
    # Connections for obj150 (graphObject_: Obj160) of type CD_Inheritance3
    self.drawConnections(
(self.obj150,self.obj33,[1329.0, 1078.0, 831.0, 1061.0],"true", 2) )
    # Connections for obj151 (graphObject_: Obj162) of type CD_Inheritance3
    self.drawConnections(
(self.obj151,self.obj55,[2232.0, 1488.0, 2276.0, 1441.0],"true", 2) )
    # Connections for obj152 (graphObject_: Obj164) of type CD_Inheritance3
    self.drawConnections(
(self.obj152,self.obj55,[2365.0, 1456.0, 2356.0, 1441.0],"true", 2) )
    # Connections for obj153 (graphObject_: Obj166) of type CD_Inheritance3
    self.drawConnections(
(self.obj153,self.obj30,[742.3984375, 330.85199795099999, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj154 (graphObject_: Obj168) of type CD_Inheritance3
    self.drawConnections(
(self.obj154,self.obj58,[736.0, 511.0, 736.0, 501.0],"true", 2) )
    # Connections for obj155 (graphObject_: Obj170) of type CD_Inheritance3
    self.drawConnections(
(self.obj155,self.obj58,[779.0, 671.0, 776.0, 501.0],"true", 2) )
    # Connections for obj156 (graphObject_: Obj172) of type CD_Inheritance3
    self.drawConnections(
(self.obj156,self.obj61,[936.0, 511.0, 936.0, 501.0],"true", 2) )
    # Connections for obj157 (graphObject_: Obj174) of type CD_Inheritance3
    self.drawConnections(
(self.obj157,self.obj61,[1020.6875, 661.95774647887322, 1016.0, 501.0],"true", 2) )
    # Connections for obj158 (graphObject_: Obj176) of type CD_Inheritance3
    self.drawConnections(
(self.obj158,self.obj30,[976.3984375, 337.46675204899998, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj159 (graphObject_: Obj178) of type CD_Inheritance3
    self.drawConnections(
(self.obj159,self.obj30,[1242.3984375, 350.46675204899998, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj160 (graphObject_: Obj180) of type CD_Inheritance3
    self.drawConnections(
(self.obj160,self.obj64,[1156.0, 511.0, 1156.0, 501.0],"true", 2) )
    # Connections for obj161 (graphObject_: Obj182) of type CD_Inheritance3
    self.drawConnections(
(self.obj161,self.obj64,[1236.0, 591.0, 1236.0, 501.0],"true", 2) )
    # Connections for obj162 (graphObject_: Obj184) of type CD_Inheritance3
    self.drawConnections(
(self.obj162,self.obj64,[1302.0, 812.0, 1236.0, 501.0],"true", 2) )
    # Connections for obj163 (graphObject_: Obj186) of type CD_Inheritance3
    self.drawConnections(
(self.obj163,self.obj30,[1538.078125, 385.54052254099997, 1540.0625, 390.16209016400001],"true", 2) )
    # Connections for obj164 (graphObject_: Obj188) of type CD_Inheritance3
    self.drawConnections(
(self.obj164,self.obj68,[1456.0, 551.0, 1456.0, 541.0],"true", 2) )
    # Connections for obj165 (graphObject_: Obj190) of type CD_Inheritance3
    self.drawConnections(
(self.obj165,self.obj68,[1506.0, 631.0, 1496.0, 541.0],"true", 2) )
    # Connections for obj166 (graphObject_: Obj192) of type CD_Inheritance3
    self.drawConnections(
(self.obj166,self.obj68,[1550.0, 771.0, 1536.0, 541.0],"true", 2) )
    # Connections for obj167 (graphObject_: Obj194) of type CD_Inheritance3
    self.drawConnections(
(self.obj167,self.obj31,[264.828125, 2024.42622951, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj168 (graphObject_: Obj196) of type CD_Inheritance3
    self.drawConnections(
(self.obj168,self.obj31,[451.828125, 2034.42622951, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj169 (graphObject_: Obj198) of type CD_Inheritance3
    self.drawConnections(
(self.obj169,self.obj31,[594.828125, 2052.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj170 (graphObject_: Obj200) of type CD_Inheritance3
    self.drawConnections(
(self.obj170,self.obj31,[1972.828125, 2057.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj171 (graphObject_: Obj202) of type CD_Inheritance3
    self.drawConnections(
(self.obj171,self.obj72,[176.0, 2241.0, 176.0, 2221.0],"true", 2) )
    # Connections for obj172 (graphObject_: Obj204) of type CD_Inheritance3
    self.drawConnections(
(self.obj172,self.obj72,[225.0, 2586.0, 216.0, 2221.0],"true", 2) )
    # Connections for obj173 (graphObject_: Obj206) of type CD_Inheritance3
    self.drawConnections(
(self.obj173,self.obj31,[794.828125, 2061.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj174 (graphObject_: Obj208) of type CD_Inheritance3
    self.drawConnections(
(self.obj174,self.obj78,[826.0, 2245.0, 816.0, 2221.0],"true", 2) )
    # Connections for obj175 (graphObject_: Obj210) of type CD_Inheritance3
    self.drawConnections(
(self.obj175,self.obj76,[133.5, 2421.0, 131.0, 2401.0],"true", 2) )
    # Connections for obj176 (graphObject_: Obj212) of type CD_Inheritance3
    self.drawConnections(
(self.obj176,self.obj75,[1953.5, 2252.0, 1976.0, 2221.0],"true", 2) )
    # Connections for obj177 (graphObject_: Obj214) of type CD_Inheritance3
    self.drawConnections(
(self.obj177,self.obj75,[2067.0, 2246.0, 2056.0, 2221.0],"true", 2) )
    # Connections for obj178 (graphObject_: Obj216) of type CD_Inheritance3
    self.drawConnections(
(self.obj178,self.obj75,[2338.5, 2248.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj179 (graphObject_: Obj218) of type CD_Inheritance3
    self.drawConnections(
(self.obj179,self.obj31,[1776.046875, 2063.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj180 (graphObject_: Obj220) of type CD_Inheritance3
    self.drawConnections(
(self.obj180,self.obj31,[1057.828125, 2058.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj181 (graphObject_: Obj222) of type CD_Inheritance3
    self.drawConnections(
(self.obj181,self.obj31,[1176.328125, 2056.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj182 (graphObject_: Obj224) of type CD_Inheritance3
    self.drawConnections(
(self.obj182,self.obj31,[1462.625, 2057.5, 1469.25, 2059.0],"true", 2) )
    # Connections for obj183 (graphObject_: Obj226) of type CD_Inheritance3
    self.drawConnections(
(self.obj183,self.obj31,[1569.875, 2057.5, 1563.75, 2059.0],"true", 2) )
    # Connections for obj184 (graphObject_: Obj228) of type CD_Inheritance3
    self.drawConnections(
(self.obj184,self.obj75,[1776.5, 2265.0, 1941.0, 2201.0],"true", 2) )
    # Connections for obj185 (graphObject_: Obj230) of type CD_Inheritance3
    self.drawConnections(
(self.obj185,self.obj84,[1778.0, 2251.0, 1776.0, 2221.0],"true", 2) )
    # Connections for obj186 (graphObject_: Obj232) of type CD_Inheritance3
    self.drawConnections(
(self.obj186,self.obj75,[2483.0, 2243.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj187 (graphObject_: Obj234) of type CD_Inheritance3
    self.drawConnections(
(self.obj187,self.obj75,[2700.0, 2239.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj188 (graphObject_: Obj236) of type CD_Inheritance3
    self.drawConnections(
(self.obj188,self.obj75,[2021.0, 2479.0, 2016.0, 2221.0],"true", 2) )
    # Connections for obj189 (graphObject_: Obj238) of type CD_Inheritance3
    self.drawConnections(
(self.obj189,self.obj75,[2031.0, 2479.0, 2016.0, 2221.0],"true", 2) )
    # Connections for obj190 (graphObject_: Obj240) of type CD_Inheritance3
    self.drawConnections(
(self.obj190,self.obj75,[2230.5, 2240.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj191 (graphObject_: Obj242) of type CD_Inheritance3
    self.drawConnections(
(self.obj191,self.obj75,[2467.5, 2256.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj192 (graphObject_: Obj244) of type CD_Inheritance3
    self.drawConnections(
(self.obj192,self.obj92,[1896.0, 2601.0, 1896.0, 2581.0],"true", 2) )
    # Connections for obj193 (graphObject_: Obj246) of type CD_Inheritance3
    self.drawConnections(
(self.obj193,self.obj75,[2675.0, 2249.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj194 (graphObject_: Obj248) of type CD_Inheritance3
    self.drawConnections(
(self.obj194,self.obj75,[2876.0, 2237.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj195 (graphObject_: Obj250) of type CD_Inheritance3
    self.drawConnections(
(self.obj195,self.obj75,[2900.0, 2225.0, 2131.0, 2201.0],"true", 2) )
    # Connections for obj196 (graphObject_: Obj252) of type CD_Inheritance3
    self.drawConnections(
(self.obj196,self.obj31,[798.328125, 2158.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj197 (graphObject_: Obj254) of type CD_Inheritance3
    self.drawConnections(
(self.obj197,self.obj31,[795.828125, 2239.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj198 (graphObject_: Obj256) of type CD_Inheritance3
    self.drawConnections(
(self.obj198,self.obj31,[815.828125, 2319.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj199 (graphObject_: Obj258) of type CD_Inheritance3
    self.drawConnections(
(self.obj199,self.obj31,[1155.828125, 2149.4262295100002, 1380.65625, 2019.2377049180327],"true", 2) )
    # Connections for obj200 (graphObject_: Obj260) of type CD_Inheritance3
    self.drawConnections(
(self.obj200,self.obj31,[1609.875, 2147.5, 1563.75, 2059.0],"true", 2) )
    # Connections for obj201 (graphObject_: Obj262) of type CD_Inheritance3
    self.drawConnections(
(self.obj201,self.obj31,[1730.546875, 2129.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj202 (graphObject_: Obj264) of type CD_Inheritance3
    self.drawConnections(
(self.obj202,self.obj31,[1823.046875, 2149.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj203 (graphObject_: Obj266) of type CD_Inheritance3
    self.drawConnections(
(self.obj203,self.obj31,[1933.046875, 2149.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj204 (graphObject_: Obj268) of type CD_Inheritance3
    self.drawConnections(
(self.obj204,self.obj31,[2043.046875, 2149.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj205 (graphObject_: Obj270) of type CD_Inheritance3
    self.drawConnections(
(self.obj205,self.obj31,[2143.046875, 2149.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj206 (graphObject_: Obj272) of type CD_Inheritance3
    self.drawConnections(
(self.obj206,self.obj31,[2246.046875, 2149.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj207 (graphObject_: Obj274) of type CD_Inheritance3
    self.drawConnections(
(self.obj207,self.obj31,[2223.046875, 2239.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj208 (graphObject_: Obj276) of type CD_Inheritance3
    self.drawConnections(
(self.obj208,self.obj31,[2124.046875, 2255.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj209 (graphObject_: Obj278) of type CD_Inheritance3
    self.drawConnections(
(self.obj209,self.obj31,[2023.046875, 2239.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj210 (graphObject_: Obj280) of type CD_Inheritance3
    self.drawConnections(
(self.obj210,self.obj31,[1923.046875, 2239.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj211 (graphObject_: Obj282) of type CD_Inheritance3
    self.drawConnections(
(self.obj211,self.obj31,[1840.546875, 2219.4262295100002, 1605.09375, 2019.2377049180327],"true", 2) )
    # Connections for obj212 (graphObject_: Obj284) of type CD_Inheritance3
    self.drawConnections(
(self.obj212,self.obj31,[1709.875, 2237.5, 1563.75, 2059.0],"true", 2) )
    # Connections for obj213 (graphObject_: Obj286) of type CD_Inheritance3
    self.drawConnections(
(self.obj213,self.obj31,[1709.875, 2327.5, 1563.75, 2059.0],"true", 2) )
    # Connections for obj214 (graphObject_: Obj288) of type CD_Inheritance3
    self.drawConnections(
(self.obj214,self.obj30,[1591.90625, 560.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj215 (graphObject_: Obj290) of type CD_Inheritance3
    self.drawConnections(
(self.obj215,self.obj30,[1604.96875, 567.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj216 (graphObject_: Obj292) of type CD_Inheritance3
    self.drawConnections(
(self.obj216,self.obj30,[1617.03125, 604.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj217 (graphObject_: Obj294) of type CD_Inheritance3
    self.drawConnections(
(self.obj217,self.obj30,[1345.8515625, 365.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj218 (graphObject_: Obj296) of type CD_Inheritance3
    self.drawConnections(
(self.obj218,self.obj30,[1319.90625, 427.581045082, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj219 (graphObject_: Obj298) of type CD_Inheritance3
    self.drawConnections(
(self.obj219,self.obj30,[1325.90625, 435.581045082, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj220 (graphObject_: Obj300) of type CD_Inheritance3
    self.drawConnections(
(self.obj220,self.obj30,[1206.3515625, 443.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj221 (graphObject_: Obj302) of type CD_Inheritance3
    self.drawConnections(
(self.obj221,self.obj30,[1226.40625, 478.581045082, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj222 (graphObject_: Obj304) of type CD_Inheritance3
    self.drawConnections(
(self.obj222,self.obj30,[1086.3515625, 443.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj223 (graphObject_: Obj306) of type CD_Inheritance3
    self.drawConnections(
(self.obj223,self.obj30,[1102.8515625, 523.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj224 (graphObject_: Obj308) of type CD_Inheritance3
    self.drawConnections(
(self.obj224,self.obj30,[866.3515625, 503.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj225 (graphObject_: Obj310) of type CD_Inheritance3
    self.drawConnections(
(self.obj225,self.obj30,[986.3515625, 513.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj226 (graphObject_: Obj312) of type CD_Inheritance3
    self.drawConnections(
(self.obj226,self.obj30,[866.3515625, 583.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj227 (graphObject_: Obj314) of type CD_Inheritance3
    self.drawConnections(
(self.obj227,self.obj30,[966.3515625, 593.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj228 (graphObject_: Obj316) of type CD_Inheritance3
    self.drawConnections(
(self.obj228,self.obj30,[1098.8515625, 633.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj229 (graphObject_: Obj318) of type CD_Inheritance3
    self.drawConnections(
(self.obj229,self.obj30,[954.8515625, 705.89252049200002, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj230 (graphObject_: Obj320) of type CD_Inheritance3
    self.drawConnections(
(self.obj230,self.obj30,[1230.90625, 529.58104508199995, 1401.703125, 343.1702868853115],"true", 2) )
    # Connections for obj231 (graphObject_: Obj322) of type CD_Inheritance3
    self.drawConnections(
(self.obj231,self.obj30,[1272.28125, 668.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj232 (graphObject_: Obj324) of type CD_Inheritance3
    self.drawConnections(
(self.obj232,self.obj30,[1019.90625, 835.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj233 (graphObject_: Obj326) of type CD_Inheritance3
    self.drawConnections(
(self.obj233,self.obj30,[1159.90625, 835.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj234 (graphObject_: Obj328) of type CD_Inheritance3
    self.drawConnections(
(self.obj234,self.obj30,[1279.90625, 835.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj235 (graphObject_: Obj330) of type CD_Inheritance3
    self.drawConnections(
(self.obj235,self.obj30,[1399.90625, 835.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj236 (graphObject_: Obj332) of type CD_Inheritance3
    self.drawConnections(
(self.obj236,self.obj30,[1449.90625, 835.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj237 (graphObject_: Obj334) of type CD_Inheritance3
    self.drawConnections(
(self.obj237,self.obj30,[1622.09375, 835.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj238 (graphObject_: Obj336) of type CD_Inheritance3
    self.drawConnections(
(self.obj238,self.obj30,[1722.09375, 835.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj239 (graphObject_: Obj338) of type CD_Inheritance3
    self.drawConnections(
(self.obj239,self.obj30,[1822.09375, 835.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj240 (graphObject_: Obj340) of type CD_Inheritance3
    self.drawConnections(
(self.obj240,self.obj30,[1932.09375, 835.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj241 (graphObject_: Obj342) of type CD_Inheritance3
    self.drawConnections(
(self.obj241,self.obj30,[1149.90625, 915.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj242 (graphObject_: Obj344) of type CD_Inheritance3
    self.drawConnections(
(self.obj242,self.obj30,[1299.90625, 925.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj243 (graphObject_: Obj346) of type CD_Inheritance3
    self.drawConnections(
(self.obj243,self.obj30,[1429.90625, 925.58104508199995, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj244 (graphObject_: Obj348) of type CD_Inheritance3
    self.drawConnections(
(self.obj244,self.obj30,[1538.03125, 925.58104508199995, 1540.0625, 390.16209016400001],"true", 2) )
    # Connections for obj245 (graphObject_: Obj350) of type CD_Inheritance3
    self.drawConnections(
(self.obj245,self.obj30,[1822.09375, 925.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj246 (graphObject_: Obj352) of type CD_Inheritance3
    self.drawConnections(
(self.obj246,self.obj30,[1942.09375, 925.58104508199995, 1588.1875, 390.16209016400001],"true", 2) )
    # Connections for obj247 (graphObject_: Obj354) of type CD_Inheritance3
    self.drawConnections(
(self.obj247,self.obj30,[1159.90625, 1005.58104508, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj248 (graphObject_: Obj356) of type CD_Inheritance3
    self.drawConnections(
(self.obj248,self.obj30,[1269.90625, 1005.58104508, 1443.8125, 390.16209016400001],"true", 2) )
    # Connections for obj249 (graphObject_: Obj358) of type CD_Inheritance3
    self.drawConnections(
(self.obj249,self.obj101,[2776.0, 621.0, 2776.0, 598.0],"true", 2) )
    # Connections for obj250 (graphObject_: Obj360) of type CD_Inheritance3
    self.drawConnections(
(self.obj250,self.obj101,[2894.0, 689.0, 2856.0, 598.0],"true", 2) )
    # Connections for obj254 (graphObject_: Obj368) of type CD_Inheritance3
    self.drawConnections(
(self.obj254,self.obj103,[3041.0, 1141.0, 3036.0, 1101.0],"true", 2) )
    # Connections for obj255 (graphObject_: Obj370) of type CD_Inheritance3
    self.drawConnections(
(self.obj255,self.obj103,[3125.0, 1119.0, 3116.0, 1101.0],"true", 2) )
    # Connections for obj256 (graphObject_: Obj372) of type CD_Inheritance3
    self.drawConnections(
(self.obj256,self.obj103,[3177.0, 1132.0, 3156.0, 1101.0],"true", 2) )
    # Connections for obj257 (graphObject_: Obj374) of type CD_Inheritance3
    self.drawConnections(
(self.obj257,self.obj101,[2950.5, 825.84836065573768, 2856.0, 598.0],"true", 2) )
    # Connections for obj258 (graphObject_: Obj376) of type CD_Inheritance3
    self.drawConnections(
(self.obj258,self.obj101,[2866.0, 749.5, 2856.0, 598.0],"true", 2) )
    # Connections for obj259 (graphObject_: Obj378) of type CD_Inheritance3
    self.drawConnections(
(self.obj259,self.obj101,[2913.0, 841.5, 2856.0, 598.0],"true", 2) )
    # Connections for obj260 (graphObject_: Obj380) of type CD_Inheritance3
    self.drawConnections(
(self.obj260,self.obj101,[3036.0, 646.84836065599995, 2891.0, 572.69672131147536],"true", 2) )

newfunction = UMLRT2Kiltera_MM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
