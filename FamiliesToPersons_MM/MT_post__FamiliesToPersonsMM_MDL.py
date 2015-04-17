"""
__MT_post__FamiliesToPersonsMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Apr 17 11:08:49 2015
__________________________________________________________________________________________
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

def MT_post__FamiliesToPersonsMM_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('MT_post__FamiliesToPersonsMM')

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


    self.obj69=CD_Class3(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # QOCA
    self.obj69.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj69.Graphical_Appearance.setValue( ('MT_post__MetaModelElement_S', self.obj69))

    # name
    self.obj69.name.setValue('MT_post__MetaModelElement_S')

    # attributes
    self.obj69.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj69.attributes.setValue(lcobj2)

    # Abstract
    self.obj69.Abstract.setValue((None, 0))
    self.obj69.Abstract.config = 0

    # cardinality
    self.obj69.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__match_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__backward_link', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__indirectLink_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__indirectLink_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__directLink_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__directLink_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__trace_link', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj69.cardinality.setValue(lcobj2)

    # display
    self.obj69.display.setValue('Attributes:\n  - cardinality :: String\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From match_contains: 0 to N\n  - From backward_link: 0 to N\n  - To indirectLink_S: 0 to N\n  - From indirectLink_S: 0 to N\n  - To directLink_S: 0 to N\n  - From directLink_S: 0 to N\n  - From trace_link: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj69.display.setHeight(15)

    # Actions
    self.obj69.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj69.Actions.setValue(lcobj2)

    # Constraints
    self.obj69.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.Constraints.setValue(lcobj2)

    self.obj69.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,120.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.7901639344262295]
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
    self.obj70.Graphical_Appearance.setValue( ('MT_post__HouseholdRoot', self.obj70))

    # name
    self.obj70.name.setValue('MT_post__HouseholdRoot')

    # attributes
    self.obj70.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj70.attributes.setValue(lcobj2)

    # Abstract
    self.obj70.Abstract.setValue((None, 0))
    self.obj70.Abstract.config = 0

    # cardinality
    self.obj70.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj70.cardinality.setValue(lcobj2)

    # display
    self.obj70.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj70.display.setHeight(15)

    # Actions
    self.obj70.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj70.Actions.setValue(lcobj2)

    # Constraints
    self.obj70.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj70.Constraints.setValue(lcobj2)

    self.obj70.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,340.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj71.Graphical_Appearance.setValue( ('MT_post__Family', self.obj71))

    # name
    self.obj71.name.setValue('MT_post__Family')

    # attributes
    self.obj71.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj71.attributes.setValue(lcobj2)

    # Abstract
    self.obj71.Abstract.setValue((None, 0))
    self.obj71.Abstract.config = 0

    # cardinality
    self.obj71.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj71.cardinality.setValue(lcobj2)

    # display
    self.obj71.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj71.display.setHeight(15)

    # Actions
    self.obj71.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj71.Actions.setValue(lcobj2)

    # Constraints
    self.obj71.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj71.Constraints.setValue(lcobj2)

    self.obj71.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(500.0,340.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj72.Graphical_Appearance.setValue( ('MT_post__Member', self.obj72))

    # name
    self.obj72.name.setValue('MT_post__Member')

    # attributes
    self.obj72.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj72.attributes.setValue(lcobj2)

    # Abstract
    self.obj72.Abstract.setValue((None, 0))
    self.obj72.Abstract.config = 0

    # cardinality
    self.obj72.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj72.cardinality.setValue(lcobj2)

    # display
    self.obj72.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj72.display.setHeight(15)

    # Actions
    self.obj72.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj72.Actions.setValue(lcobj2)

    # Constraints
    self.obj72.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj72.Constraints.setValue(lcobj2)

    self.obj72.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,340.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj73.Graphical_Appearance.setValue( ('MT_post__MatchModel', self.obj73))

    # name
    self.obj73.name.setValue('MT_post__MatchModel')

    # attributes
    self.obj73.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj73.attributes.setValue(lcobj2)

    # Abstract
    self.obj73.Abstract.setValue((None, 0))
    self.obj73.Abstract.config = 0

    # cardinality
    self.obj73.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__match_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__paired_with', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj73.cardinality.setValue(lcobj2)

    # display
    self.obj73.display.setValue('Multiplicities:\n  - To match_contains: 0 to N\n  - To paired_with: 1 to 1\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj73.display.setHeight(15)

    # Actions
    self.obj73.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj73.Actions.setValue(lcobj2)

    # Constraints
    self.obj73.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj73.Constraints.setValue(lcobj2)

    self.obj73.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,120.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj74.Graphical_Appearance.setValue( ('MT_post__ApplyModel', self.obj74))

    # name
    self.obj74.name.setValue('MT_post__ApplyModel')

    # attributes
    self.obj74.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj74.attributes.setValue(lcobj2)

    # Abstract
    self.obj74.Abstract.setValue((None, 0))
    self.obj74.Abstract.config = 0

    # cardinality
    self.obj74.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__apply_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__paired_with', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj74.cardinality.setValue(lcobj2)

    # display
    self.obj74.display.setValue('Multiplicities:\n  - To apply_contains: 0 to N\n  - From paired_with: 1 to 1\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj74.display.setHeight(15)

    # Actions
    self.obj74.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj74.Actions.setValue(lcobj2)

    # Constraints
    self.obj74.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj74.Constraints.setValue(lcobj2)

    self.obj74.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,540.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.752
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj75.Graphical_Appearance.setValue( ('MT_post__MetaModelElement_T', self.obj75))

    # name
    self.obj75.name.setValue('MT_post__MetaModelElement_T')

    # attributes
    self.obj75.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj75.attributes.setValue(lcobj2)

    # Abstract
    self.obj75.Abstract.setValue((None, 0))
    self.obj75.Abstract.config = 0

    # cardinality
    self.obj75.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__apply_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__backward_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__directLink_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__directLink_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__trace_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj75.cardinality.setValue(lcobj2)

    # display
    self.obj75.display.setValue('Attributes:\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From apply_contains: 0 to N\n  - To backward_link: 0 to N\n  - To directLink_T: 0 to N\n  - From directLink_T: 0 to N\n  - To trace_link: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj75.display.setHeight(15)

    # Actions
    self.obj75.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj75.Actions.setValue(lcobj2)

    # Constraints
    self.obj75.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj75.Constraints.setValue(lcobj2)

    self.obj75.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,540.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.672
       new_obj.layConstraints['scale'] = [1.3890624999999999, 1.290983606557377]
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
    self.obj76.Graphical_Appearance.setValue( ('MT_post__CommunityRoot', self.obj76))

    # name
    self.obj76.name.setValue('MT_post__CommunityRoot')

    # attributes
    self.obj76.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj76.attributes.setValue(lcobj2)

    # Abstract
    self.obj76.Abstract.setValue((None, 0))
    self.obj76.Abstract.config = 0

    # cardinality
    self.obj76.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj76.cardinality.setValue(lcobj2)

    # display
    self.obj76.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj76.display.setHeight(15)

    # Actions
    self.obj76.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj76.Actions.setValue(lcobj2)

    # Constraints
    self.obj76.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj76.Constraints.setValue(lcobj2)

    self.obj76.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(320.0,720.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj77.Graphical_Appearance.setValue( ('MT_post__Person', self.obj77))

    # name
    self.obj77.name.setValue('MT_post__Person')

    # attributes
    self.obj77.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj77.attributes.setValue(lcobj2)

    # Abstract
    self.obj77.Abstract.setValue((None, 0))
    self.obj77.Abstract.config = 0

    # cardinality
    self.obj77.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj77.cardinality.setValue(lcobj2)

    # display
    self.obj77.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj77.display.setHeight(15)

    # Actions
    self.obj77.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj77.Actions.setValue(lcobj2)

    # Constraints
    self.obj77.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj77.Constraints.setValue(lcobj2)

    self.obj77.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,720.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj78.Graphical_Appearance.setValue( ('MT_post__Man', self.obj78))

    # name
    self.obj78.name.setValue('MT_post__Man')

    # attributes
    self.obj78.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj78.attributes.setValue(lcobj2)

    # Abstract
    self.obj78.Abstract.setValue((None, 0))
    self.obj78.Abstract.config = 0

    # cardinality
    self.obj78.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj78.cardinality.setValue(lcobj2)

    # display
    self.obj78.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj78.display.setHeight(15)

    # Actions
    self.obj78.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj78.Actions.setValue(lcobj2)

    # Constraints
    self.obj78.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj78.Constraints.setValue(lcobj2)

    self.obj78.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(760.0,720.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj79.Graphical_Appearance.setValue( ('MT_post__Woman', self.obj79))

    # name
    self.obj79.name.setValue('MT_post__Woman')

    # attributes
    self.obj79.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj79.attributes.setValue(lcobj2)

    # Abstract
    self.obj79.Abstract.setValue((None, 0))
    self.obj79.Abstract.config = 0

    # cardinality
    self.obj79.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj79.cardinality.setValue(lcobj2)

    # display
    self.obj79.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj79.display.setHeight(15)

    # Actions
    self.obj79.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj79.Actions.setValue(lcobj2)

    # Constraints
    self.obj79.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj79.Constraints.setValue(lcobj2)

    self.obj79.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(560.0,920.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj95=CD_Class3(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # QOCA
    self.obj95.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj95.Graphical_Appearance.setValue( ('MT_post__GenericNode_FamiliesToPersonsMM', self.obj95))

    # name
    self.obj95.name.setValue('MT_post__GenericNode_FamiliesToPersonsMM')

    # attributes
    self.obj95.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj95.attributes.setValue(lcobj2)

    # Abstract
    self.obj95.Abstract.setValue((None, 0))
    self.obj95.Abstract.config = 0

    # cardinality
    self.obj95.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj95.cardinality.setValue(lcobj2)

    # display
    self.obj95.display.setValue('Multiplicities:\n  - To GenericEdge_FamiliesToPersonsMM: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj95.display.setHeight(15)

    # Actions
    self.obj95.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj95.Actions.setValue(lcobj2)

    # Constraints
    self.obj95.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj95.Constraints.setValue(lcobj2)

    self.obj95.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(0.0,0.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj80=CD_Association3(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # QOCA
    self.obj80.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj80.Graphical_Appearance.setValue( ('MT_post__match_contains', self.obj80))
    self.obj80.Graphical_Appearance.linkInfo=linkEditor(self,self.obj80.Graphical_Appearance.semObject, "match_contains")
    self.obj80.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('match_contains_1stLink', self.obj80.Graphical_Appearance.linkInfo.FirstLink))
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('match_contains_1stSegment', self.obj80.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj80.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj80.Graphical_Appearance.linkInfo.Center.setValue( ('match_contains_Center', self.obj80.Graphical_Appearance.linkInfo))
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('match_contains_2ndSegment', self.obj80.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj80.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('match_contains_2ndLink', self.obj80.Graphical_Appearance.linkInfo.SecondLink))
    self.obj80.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj80.Graphical_Appearance.semObject
    self.obj80.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj80.Graphical_Appearance.semObject
    self.obj80.Graphical_Appearance.linkInfo.Center.semObject=self.obj80.Graphical_Appearance.semObject
    self.obj80.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj80.Graphical_Appearance.semObject
    self.obj80.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj80.Graphical_Appearance.semObject

    # name
    self.obj80.name.setValue('MT_post__match_contains')

    # displaySelect
    self.obj80.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj80.displaySelect.config = 0

    # attributes
    self.obj80.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj80.attributes.setValue(lcobj2)

    # cardinality
    self.obj80.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj80.cardinality.setValue(lcobj2)

    # display
    self.obj80.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MatchModel: 0 to N\n')
    self.obj80.display.setHeight(15)

    # Actions
    self.obj80.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj80.Actions.setValue(lcobj2)

    # Constraints
    self.obj80.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj80.Constraints.setValue(lcobj2)

    self.obj80.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(361.8,199.8,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.3230000000000002, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=CD_Association3(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # QOCA
    self.obj81.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj81.Graphical_Appearance.setValue( ('MT_post__apply_contains', self.obj81))
    self.obj81.Graphical_Appearance.linkInfo=linkEditor(self,self.obj81.Graphical_Appearance.semObject, "apply_contains")
    self.obj81.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('apply_contains_1stLink', self.obj81.Graphical_Appearance.linkInfo.FirstLink))
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('apply_contains_1stSegment', self.obj81.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj81.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj81.Graphical_Appearance.linkInfo.Center.setValue( ('apply_contains_Center', self.obj81.Graphical_Appearance.linkInfo))
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('apply_contains_2ndSegment', self.obj81.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj81.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('apply_contains_2ndLink', self.obj81.Graphical_Appearance.linkInfo.SecondLink))
    self.obj81.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj81.Graphical_Appearance.semObject
    self.obj81.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj81.Graphical_Appearance.semObject
    self.obj81.Graphical_Appearance.linkInfo.Center.semObject=self.obj81.Graphical_Appearance.semObject
    self.obj81.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj81.Graphical_Appearance.semObject
    self.obj81.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj81.Graphical_Appearance.semObject

    # name
    self.obj81.name.setValue('MT_post__apply_contains')

    # displaySelect
    self.obj81.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj81.displaySelect.config = 0

    # attributes
    self.obj81.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj81.attributes.setValue(lcobj2)

    # cardinality
    self.obj81.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj81.cardinality.setValue(lcobj2)

    # display
    self.obj81.display.setValue('Multiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From ApplyModel: 0 to N\n')
    self.obj81.display.setHeight(15)

    # Actions
    self.obj81.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj81.Actions.setValue(lcobj2)

    # Constraints
    self.obj81.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj81.Constraints.setValue(lcobj2)

    self.obj81.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(362.491532278,586.86445,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.316, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=CD_Association3(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # QOCA
    self.obj82.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj82.Graphical_Appearance.setValue( ('MT_post__backward_link', self.obj82))
    self.obj82.Graphical_Appearance.linkInfo=linkEditor(self,self.obj82.Graphical_Appearance.semObject, "backward_link")
    self.obj82.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('backward_link_1stLink', self.obj82.Graphical_Appearance.linkInfo.FirstLink))
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('backward_link_1stSegment', self.obj82.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj82.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj82.Graphical_Appearance.linkInfo.Center.setValue( ('backward_link_Center', self.obj82.Graphical_Appearance.linkInfo))
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('backward_link_2ndSegment', self.obj82.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj82.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('backward_link_2ndLink', self.obj82.Graphical_Appearance.linkInfo.SecondLink))
    self.obj82.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj82.Graphical_Appearance.semObject
    self.obj82.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj82.Graphical_Appearance.semObject
    self.obj82.Graphical_Appearance.linkInfo.Center.semObject=self.obj82.Graphical_Appearance.semObject
    self.obj82.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj82.Graphical_Appearance.semObject
    self.obj82.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj82.Graphical_Appearance.semObject

    # name
    self.obj82.name.setValue('MT_post__backward_link')

    # displaySelect
    self.obj82.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj82.displaySelect.config = 0

    # attributes
    self.obj82.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj82.attributes.setValue(lcobj2)

    # cardinality
    self.obj82.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj82.cardinality.setValue(lcobj2)

    # display
    self.obj82.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj82.display.setHeight(15)

    # Actions
    self.obj82.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj82.Actions.setValue(lcobj2)

    # Constraints
    self.obj82.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj82.Constraints.setValue(lcobj2)

    self.obj82.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1245.0,339.5,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=CD_Association3(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # QOCA
    self.obj83.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj83.Graphical_Appearance.setValue( ('MT_post__indirectLink_S', self.obj83))
    self.obj83.Graphical_Appearance.linkInfo=linkEditor(self,self.obj83.Graphical_Appearance.semObject, "indirectLink_S")
    self.obj83.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('indirectLink_S_1stLink', self.obj83.Graphical_Appearance.linkInfo.FirstLink))
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('blue', 20)
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('indirectLink_S_1stSegment', self.obj83.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj83.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj83.Graphical_Appearance.linkInfo.Center.setValue( ('indirectLink_S_Center', self.obj83.Graphical_Appearance.linkInfo))
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('blue', 20)
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('indirectLink_S_2ndSegment', self.obj83.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj83.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('indirectLink_S_2ndLink', self.obj83.Graphical_Appearance.linkInfo.SecondLink))
    self.obj83.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj83.Graphical_Appearance.semObject
    self.obj83.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj83.Graphical_Appearance.semObject
    self.obj83.Graphical_Appearance.linkInfo.Center.semObject=self.obj83.Graphical_Appearance.semObject
    self.obj83.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj83.Graphical_Appearance.semObject
    self.obj83.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj83.Graphical_Appearance.semObject

    # name
    self.obj83.name.setValue('MT_post__indirectLink_S')

    # displaySelect
    self.obj83.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj83.displaySelect.config = 0

    # attributes
    self.obj83.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj83.attributes.setValue(lcobj2)

    # cardinality
    self.obj83.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj83.cardinality.setValue(lcobj2)

    # display
    self.obj83.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj83.display.setHeight(15)

    # Actions
    self.obj83.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj83.Actions.setValue(lcobj2)

    # Constraints
    self.obj83.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj83.Constraints.setValue(lcobj2)

    self.obj83.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1274.5,81.5,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.862, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=CD_Association3(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # QOCA
    self.obj84.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj84.Graphical_Appearance.setValue( ('MT_post__directLink_T', self.obj84))
    self.obj84.Graphical_Appearance.linkInfo=linkEditor(self,self.obj84.Graphical_Appearance.semObject, "directLink_T")
    self.obj84.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_T_1stLink', self.obj84.Graphical_Appearance.linkInfo.FirstLink))
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_T_1stSegment', self.obj84.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj84.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj84.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_T_Center', self.obj84.Graphical_Appearance.linkInfo))
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_T_2ndSegment', self.obj84.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj84.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_T_2ndLink', self.obj84.Graphical_Appearance.linkInfo.SecondLink))
    self.obj84.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj84.Graphical_Appearance.semObject
    self.obj84.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj84.Graphical_Appearance.semObject
    self.obj84.Graphical_Appearance.linkInfo.Center.semObject=self.obj84.Graphical_Appearance.semObject
    self.obj84.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj84.Graphical_Appearance.semObject
    self.obj84.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj84.Graphical_Appearance.semObject

    # name
    self.obj84.name.setValue('MT_post__directLink_T')

    # displaySelect
    self.obj84.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj84.displaySelect.config = 0

    # attributes
    self.obj84.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__associationType', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj84.attributes.setValue(lcobj2)

    # cardinality
    self.obj84.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj84.cardinality.setValue(lcobj2)

    # display
    self.obj84.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj84.display.setHeight(15)

    # Actions
    self.obj84.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj84.Actions.setValue(lcobj2)

    # Constraints
    self.obj84.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj84.Constraints.setValue(lcobj2)

    self.obj84.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1193.0,684.5,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.185483870967742]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=CD_Association3(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # QOCA
    self.obj85.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj85.Graphical_Appearance.setValue( ('MT_post__directLink_S', self.obj85))
    self.obj85.Graphical_Appearance.linkInfo=linkEditor(self,self.obj85.Graphical_Appearance.semObject, "directLink_S")
    self.obj85.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_S_1stLink', self.obj85.Graphical_Appearance.linkInfo.FirstLink))
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_S_1stSegment', self.obj85.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj85.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj85.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_S_Center', self.obj85.Graphical_Appearance.linkInfo))
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_S_2ndSegment', self.obj85.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj85.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_S_2ndLink', self.obj85.Graphical_Appearance.linkInfo.SecondLink))
    self.obj85.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj85.Graphical_Appearance.semObject
    self.obj85.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj85.Graphical_Appearance.semObject
    self.obj85.Graphical_Appearance.linkInfo.Center.semObject=self.obj85.Graphical_Appearance.semObject
    self.obj85.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj85.Graphical_Appearance.semObject
    self.obj85.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj85.Graphical_Appearance.semObject

    # name
    self.obj85.name.setValue('MT_post__directLink_S')

    # displaySelect
    self.obj85.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj85.displaySelect.config = 0

    # attributes
    self.obj85.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__associationType', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj85.attributes.setValue(lcobj2)

    # cardinality
    self.obj85.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj85.cardinality.setValue(lcobj2)

    # display
    self.obj85.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj85.display.setHeight(15)

    # Actions
    self.obj85.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj85.Actions.setValue(lcobj2)

    # Constraints
    self.obj85.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj85.Constraints.setValue(lcobj2)

    self.obj85.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(950.5,86.5,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.862, 1.185483870967742]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=CD_Association3(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # QOCA
    self.obj86.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj86.Graphical_Appearance.setValue( ('MT_post__paired_with', self.obj86))
    self.obj86.Graphical_Appearance.linkInfo=linkEditor(self,self.obj86.Graphical_Appearance.semObject, "paired_with")
    self.obj86.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('paired_with_1stLink', self.obj86.Graphical_Appearance.linkInfo.FirstLink))
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('paired_with_1stSegment', self.obj86.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj86.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj86.Graphical_Appearance.linkInfo.Center.setValue( ('paired_with_Center', self.obj86.Graphical_Appearance.linkInfo))
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('paired_with_2ndSegment', self.obj86.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj86.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('paired_with_2ndLink', self.obj86.Graphical_Appearance.linkInfo.SecondLink))
    self.obj86.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj86.Graphical_Appearance.semObject
    self.obj86.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj86.Graphical_Appearance.semObject
    self.obj86.Graphical_Appearance.linkInfo.Center.semObject=self.obj86.Graphical_Appearance.semObject
    self.obj86.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj86.Graphical_Appearance.semObject
    self.obj86.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj86.Graphical_Appearance.semObject

    # name
    self.obj86.name.setValue('MT_post__paired_with')

    # displaySelect
    self.obj86.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj86.displaySelect.config = 0

    # attributes
    self.obj86.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj86.attributes.setValue(lcobj2)

    # cardinality
    self.obj86.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj86.cardinality.setValue(lcobj2)

    # display
    self.obj86.display.setValue('Multiplicities:\n  - To ApplyModel: 1 to 1\n  - From MatchModel: 1 to 1\n')
    self.obj86.display.setHeight(15)

    # Actions
    self.obj86.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj86.Actions.setValue(lcobj2)

    # Constraints
    self.obj86.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj86.Constraints.setValue(lcobj2)

    self.obj86.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(136.0,401.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.344, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=CD_Association3(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # QOCA
    self.obj87.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj87.Graphical_Appearance.setValue( ('MT_post__trace_link', self.obj87))
    self.obj87.Graphical_Appearance.linkInfo=linkEditor(self,self.obj87.Graphical_Appearance.semObject, "trace_link")
    self.obj87.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('trace_link_1stLink', self.obj87.Graphical_Appearance.linkInfo.FirstLink))
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('trace_link_1stSegment', self.obj87.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj87.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj87.Graphical_Appearance.linkInfo.Center.setValue( ('trace_link_Center', self.obj87.Graphical_Appearance.linkInfo))
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('trace_link_2ndSegment', self.obj87.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj87.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('trace_link_2ndLink', self.obj87.Graphical_Appearance.linkInfo.SecondLink))
    self.obj87.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj87.Graphical_Appearance.semObject
    self.obj87.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj87.Graphical_Appearance.semObject
    self.obj87.Graphical_Appearance.linkInfo.Center.semObject=self.obj87.Graphical_Appearance.semObject
    self.obj87.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj87.Graphical_Appearance.semObject
    self.obj87.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj87.Graphical_Appearance.semObject

    # name
    self.obj87.name.setValue('MT_post__trace_link')

    # displaySelect
    self.obj87.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj87.displaySelect.config = 0

    # attributes
    self.obj87.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj87.attributes.setValue(lcobj2)

    # cardinality
    self.obj87.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj87.cardinality.setValue(lcobj2)

    # display
    self.obj87.display.setValue('Multiplicities:\n  - From MetaModelElement_T: 0 to N\n  - To MetaModelElement_S: 0 to N\n')
    self.obj87.display.setHeight(15)

    # Actions
    self.obj87.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj87.Actions.setValue(lcobj2)

    # Constraints
    self.obj87.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj87.Constraints.setValue(lcobj2)

    self.obj87.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1242.0,481.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj96=CD_Association3(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # QOCA
    self.obj96.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj96.Graphical_Appearance.setValue( ('MT_post__GenericEdge_FamiliesToPersonsMM', self.obj96))
    self.obj96.Graphical_Appearance.linkInfo=linkEditor(self,self.obj96.Graphical_Appearance.semObject, "GenericEdge_FamiliesToPersonsMM")
    self.obj96.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_1stLink', self.obj96.Graphical_Appearance.linkInfo.FirstLink))
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('purple', 20)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_1stSegment', self.obj96.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj96.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.Center.setValue( ('GenericEdge_FamiliesToPersonsMM_Center', self.obj96.Graphical_Appearance.linkInfo))
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('purple', 20)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_2ndSegment', self.obj96.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_2ndLink', self.obj96.Graphical_Appearance.linkInfo.SecondLink))
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.Center.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj96.Graphical_Appearance.semObject

    # name
    self.obj96.name.setValue('MT_post__GenericEdge_FamiliesToPersonsMM')

    # displaySelect
    self.obj96.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj96.displaySelect.config = 0

    # attributes
    self.obj96.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_label__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotOut__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj96.attributes.setValue(lcobj2)

    # cardinality
    self.obj96.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericNode_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericNode_FamiliesToPersonsMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__HouseholdRoot', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Family', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Member', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__CommunityRoot', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Person', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Man', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Woman', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj96.cardinality.setValue(lcobj2)

    # display
    self.obj96.display.setValue('Multiplicities:\n  - From GenericNode_FamiliesToPersonsMM: 0 to N\n  - To GenericNode_FamiliesToPersonsMM: 0 to N\n  - To MetaModelElement_S: 0 to N\n  - To HouseholdRoot: 0 to N\n  - To Family: 0 to N\n  - To Member: 0 to N\n  - To MatchModel: 0 to N\n  - To ApplyModel: 0 to N\n  - To MetaModelElement_T: 0 to N\n  - To CommunityRoot: 0 to N\n  - To Person: 0 to N\n  - To Man: 0 to N\n  - To Woman: 0 to N\n')
    self.obj96.display.setHeight(15)

    # Actions
    self.obj96.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj96.Actions.setValue(lcobj2)

    # Constraints
    self.obj96.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj96.Constraints.setValue(lcobj2)

    self.obj96.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(0.0,0.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.6390000000000002, 3.3193548387096774]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj88=CD_Inheritance3(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    self.obj88.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(641.4,303.6,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=CD_Inheritance3(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    self.obj89.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(754.6,277.8,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=CD_Inheritance3(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    self.obj90.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(468.4,303.6,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=CD_Inheritance3(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    self.obj91.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(609.891532278,704.0332,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=CD_Inheritance3(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    self.obj92.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(757.391532278,694.0332,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=CD_Inheritance3(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    self.obj93.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(502.391532278,694.0332,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=CD_Inheritance3(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    self.obj94.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(636.0,812.5,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    # Connections for obj69 (graphObject_: Obj44) named MT_post__MetaModelElement_S
    self.drawConnections(
(self.obj69,self.obj83,[711.0, 195.02295081967213, 1026.0, 203.0, 1274.5, 81.5, 1274.5, 81.5],"true", 4),
(self.obj69,self.obj85,[711.0, 148.75409836065572, 950.5, 86.5, 950.5, 86.5],"true", 3) )
    # Connections for obj70 (graphObject_: Obj45) named MT_post__HouseholdRoot
    self.drawConnections(
(self.obj70,self.obj90,[436.0, 341.0, 468.4, 303.6],"true", 2) )
    # Connections for obj71 (graphObject_: Obj46) named MT_post__Family
    self.drawConnections(
(self.obj71,self.obj88,[656.0, 341.0, 641.4, 303.6],"true", 2) )
    # Connections for obj72 (graphObject_: Obj47) named MT_post__Member
    self.drawConnections(
(self.obj72,self.obj89,[776.0, 341.0, 754.6, 277.8],"true", 2) )
    # Connections for obj73 (graphObject_: Obj48) named MT_post__MatchModel
    self.drawConnections(
(self.obj73,self.obj80,[211.0, 189.0, 361.8, 199.8],"true", 2),
(self.obj73,self.obj86,[136.0, 261.0, 136.0, 401.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj49) named MT_post__ApplyModel
    self.drawConnections(
(self.obj74,self.obj81,[211.0, 581.0, 362.491532278, 586.86445],"true", 2) )
    # Connections for obj75 (graphObject_: Obj50) named MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj75,self.obj82,[711.0, 569.811475409836, 1245.0, 424.5, 1245.0, 339.5],"true", 3),
(self.obj75,self.obj84,[711.0, 662.7622950819672, 1193.0, 684.5, 1193.0, 684.5],"true", 3),
(self.obj75,self.obj87,[711.0, 569.811475409836, 990.0, 584.0, 1242.0, 481.0],"true", 3) )
    # Connections for obj76 (graphObject_: Obj51) named MT_post__CommunityRoot
    self.drawConnections(
(self.obj76,self.obj93,[476.0, 721.0, 502.3915322780172, 694.0332000000001],"true", 2) )
    # Connections for obj77 (graphObject_: Obj52) named MT_post__Person
    self.drawConnections(
(self.obj77,self.obj91,[616.0, 721.0, 609.8915322780176, 704.0332],"true", 2) )
    # Connections for obj78 (graphObject_: Obj53) named MT_post__Man
    self.drawConnections(
(self.obj78,self.obj92,[796.0, 721.0, 757.3915322780169, 694.0332000000001],"true", 2) )
    # Connections for obj79 (graphObject_: Obj54) named MT_post__Woman
    self.drawConnections(
(self.obj79,self.obj94,[636.0, 921.0, 636.0, 812.5],"true", 2) )
    # Connections for obj95 (graphObject_: Obj85) named MT_post__GenericNode_FamiliesToPersonsMM
    self.drawConnections(
(self.obj95,self.obj96,[1.0, 41.0, -3.0, 5.0], 0, 2) )
    # Connections for obj80 (graphObject_: Obj55) named MT_post__match_contains
    self.drawConnections(
(self.obj80,self.obj69,[361.8, 199.8, 521.0, 214.85245901639345],"true", 2) )
    # Connections for obj81 (graphObject_: Obj57) named MT_post__apply_contains
    self.drawConnections(
(self.obj81,self.obj75,[362.491532278, 586.86445, 521.0, 602.344262295082],"true", 2) )
    # Connections for obj82 (graphObject_: Obj59) named MT_post__backward_link
    self.drawConnections(
(self.obj82,self.obj69,[1245.0, 339.5, 1245.0, 254.5, 711.0, 245.8360655737705],"true", 3) )
    # Connections for obj83 (graphObject_: Obj61) named MT_post__indirectLink_S
    self.drawConnections(
(self.obj83,self.obj69,[1274.5, 81.5, 1274.5, 81.5, 711.0, 148.75409836065572],"true", 3) )
    # Connections for obj84 (graphObject_: Obj63) named MT_post__directLink_T
    self.drawConnections(
(self.obj84,self.obj75,[1193.0, 684.5, 1193.0, 684.5, 711.0, 662.7622950819672],"true", 3) )
    # Connections for obj85 (graphObject_: Obj65) named MT_post__directLink_S
    self.drawConnections(
(self.obj85,self.obj69,[950.5, 86.5, 950.5, 86.5, 711.0, 148.75409836065572],"true", 3) )
    # Connections for obj86 (graphObject_: Obj67) named MT_post__paired_with
    self.drawConnections(
(self.obj86,self.obj74,[136.0, 401.0, 136.0, 541.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj69) named MT_post__trace_link
    self.drawConnections(
(self.obj87,self.obj69,[1242.0, 481.0, 937.0, 308.0, 711.0, 280.95081967213116],"true", 3) )
    # Connections for obj96 (graphObject_: Obj86) named MT_post__GenericEdge_FamiliesToPersonsMM
    self.drawConnections(
(self.obj96,self.obj95,[-2.0, 5.0, 192.625, 1.0], 0, 2),
(self.obj96,self.obj69,[-0.36099999999999977, 5.0, 521.0, 186.75409836065572], 0, 2),
(self.obj96,self.obj70,[-0.36099999999999977, 5.0, 316.0, 341.0], 0, 2),
(self.obj96,self.obj71,[-0.36099999999999977, 5.0, 536.0, 341.0], 0, 2),
(self.obj96,self.obj72,[-0.36099999999999977, 5.0, 741.0, 381.0], 0, 2),
(self.obj96,self.obj73,[-0.36099999999999977, 5.0, 176.0, 121.0], 0, 2),
(self.obj96,self.obj74,[-0.36099999999999977, 5.0, 176.0, 541.0], 0, 2),
(self.obj96,self.obj75,[-0.36099999999999977, 5.0, 556.0, 541.3360655737705], 0, 2),
(self.obj96,self.obj76,[-0.36099999999999977, 5.0, 356.0, 721.0], 0, 2),
(self.obj96,self.obj77,[-0.36099999999999977, 5.0, 576.0, 721.0], 0, 2),
(self.obj96,self.obj78,[-0.36099999999999977, 5.0, 796.0, 721.0], 0, 2),
(self.obj96,self.obj79,[-0.36099999999999977, 5.0, 596.0, 921.0], 0, 2),
(self.obj96,self.obj95,[-2.0, 5.0, 192.625, 1.0], 0, 2) )
    # Connections for obj88 (graphObject_: Obj71) of type CD_Inheritance3
    self.drawConnections(
(self.obj88,self.obj69,[641.4, 303.6, 636.0, 352.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj73) of type CD_Inheritance3
    self.drawConnections(
(self.obj89,self.obj69,[754.6, 277.8, 711.0, 277.6393442622951],"true", 2) )
    # Connections for obj90 (graphObject_: Obj75) of type CD_Inheritance3
    self.drawConnections(
(self.obj90,self.obj69,[468.4, 303.6, 521.0, 318.95081967213116],"true", 2) )
    # Connections for obj91 (graphObject_: Obj77) of type CD_Inheritance3
    self.drawConnections(
(self.obj91,self.obj75,[609.891532278, 704.0332, 596.0, 704.0],"true", 2) )
    # Connections for obj92 (graphObject_: Obj79) of type CD_Inheritance3
    self.drawConnections(
(self.obj92,self.obj75,[757.391532278, 694.0332, 711.0, 680.7622950819672],"true", 2) )
    # Connections for obj93 (graphObject_: Obj81) of type CD_Inheritance3
    self.drawConnections(
(self.obj93,self.obj75,[502.391532278, 694.0332, 521.0, 680.7622950819672],"true", 2) )
    # Connections for obj94 (graphObject_: Obj83) of type CD_Inheritance3
    self.drawConnections(
(self.obj94,self.obj75,[636.0, 812.5, 636.0, 704.0],"true", 2) )

newfunction = MT_post__FamiliesToPersonsMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
