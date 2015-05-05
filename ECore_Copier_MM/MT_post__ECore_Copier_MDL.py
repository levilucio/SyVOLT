"""
__MT_post__ECore_Copier_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Tue May  5 12:31:09 2015
___________________________________________________________________________________
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

def MT_post__ECore_Copier_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('MT_post__ECoreMM')

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


    self.obj78=CD_Class3(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # QOCA
    self.obj78.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj78.Graphical_Appearance.setValue( ('MT_post__MetaModelElement_S', self.obj78))

    # name
    self.obj78.name.setValue('MT_post__MetaModelElement_S')

    # attributes
    self.obj78.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj78.attributes.setValue(lcobj2)

    # Abstract
    self.obj78.Abstract.setValue((None, 0))
    self.obj78.Abstract.config = 0

    # cardinality
    self.obj78.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2.setValue(('MT_post__hasAttr_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj78.cardinality.setValue(lcobj2)

    # display
    self.obj78.display.setValue('Attributes:\n  - cardinality :: String\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From match_contains: 0 to N\n  - From backward_link: 0 to N\n  - To indirectLink_S: 0 to N\n  - From indirectLink_S: 0 to N\n  - To directLink_S: 0 to N\n  - From directLink_S: 0 to N\n  - From trace_link: 0 to N\n  - To hasAttr_S: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(520.0,120.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.9278688524590166]
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
    self.obj79.Graphical_Appearance.setValue( ('MT_post__EClass', self.obj79))

    # name
    self.obj79.name.setValue('MT_post__EClass')

    # attributes
    self.obj79.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj79.cardinality.setValue(lcobj2)

    # display
    self.obj79.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_ECoreMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(280.0,340.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.0]
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
    self.obj80.Graphical_Appearance.setValue( ('MT_post__EReference', self.obj80))

    # name
    self.obj80.name.setValue('MT_post__EReference')

    # attributes
    self.obj80.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj80.attributes.setValue(lcobj2)

    # Abstract
    self.obj80.Abstract.setValue((None, 0))
    self.obj80.Abstract.config = 0

    # cardinality
    self.obj80.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj80.cardinality.setValue(lcobj2)

    # display
    self.obj80.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj80.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(500.0,340.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.0]
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
    self.obj81.Graphical_Appearance.setValue( ('MT_post__EStructuralFeature', self.obj81))

    # name
    self.obj81.name.setValue('MT_post__EStructuralFeature')

    # attributes
    self.obj81.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj81.attributes.setValue(lcobj2)

    # Abstract
    self.obj81.Abstract.setValue((None, 0))
    self.obj81.Abstract.config = 0

    # cardinality
    self.obj81.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj81.cardinality.setValue(lcobj2)

    # display
    self.obj81.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj81.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,340.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.0]
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
    self.obj82.Graphical_Appearance.setValue( ('MT_post__MatchModel', self.obj82))

    # name
    self.obj82.name.setValue('MT_post__MatchModel')

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

    # Abstract
    self.obj82.Abstract.setValue((None, 0))
    self.obj82.Abstract.config = 0

    # cardinality
    self.obj82.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__match_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__paired_with', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj82.cardinality.setValue(lcobj2)

    # display
    self.obj82.display.setValue('Multiplicities:\n  - To match_contains: 0 to N\n  - To paired_with: 1 to 1\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj82.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,120.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.0]
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
    self.obj83.Graphical_Appearance.setValue( ('MT_post__ApplyModel', self.obj83))

    # name
    self.obj83.name.setValue('MT_post__ApplyModel')

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

    # Abstract
    self.obj83.Abstract.setValue((None, 0))
    self.obj83.Abstract.config = 0

    # cardinality
    self.obj83.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__apply_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__paired_with', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj83.cardinality.setValue(lcobj2)

    # display
    self.obj83.display.setValue('Multiplicities:\n  - To apply_contains: 0 to N\n  - From paired_with: 1 to 1\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj83.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,540.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.752
       new_obj.layConstraints['scale'] = [1.1812500000000001, 1.0]
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
    self.obj84.Graphical_Appearance.setValue( ('MT_post__MetaModelElement_T', self.obj84))

    # name
    self.obj84.name.setValue('MT_post__MetaModelElement_T')

    # attributes
    self.obj84.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj84.attributes.setValue(lcobj2)

    # Abstract
    self.obj84.Abstract.setValue((None, 0))
    self.obj84.Abstract.config = 0

    # cardinality
    self.obj84.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2.setValue(('MT_post__hasAttr_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj84.cardinality.setValue(lcobj2)

    # display
    self.obj84.display.setValue('Attributes:\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From apply_contains: 0 to N\n  - To backward_link: 0 to N\n  - To directLink_T: 0 to N\n  - From directLink_T: 0 to N\n  - To trace_link: 0 to N\n  - To hasAttr_T: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj84.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,540.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.672
       new_obj.layConstraints['scale'] = [1.0609375, 1.4200819672131149]
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
    self.obj85.Graphical_Appearance.setValue( ('MT_post__Attribute', self.obj85))

    # name
    self.obj85.name.setValue('MT_post__Attribute')

    # attributes
    self.obj85.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
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
    self.obj85.attributes.setValue(lcobj2)

    # Abstract
    self.obj85.Abstract.setValue((None, 0))
    self.obj85.Abstract.config = 0

    # cardinality
    self.obj85.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__hasAttr_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__hasAttr_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj85.cardinality.setValue(lcobj2)

    # display
    self.obj85.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From hasAttr_S: 0 to N\n  - From hasAttr_T: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj85.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1480.0,500.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.5476562500000002, 1.0844262295081968]
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
    self.obj86.Graphical_Appearance.setValue( ('MT_post__Equation', self.obj86))

    # name
    self.obj86.name.setValue('MT_post__Equation')

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

    # Abstract
    self.obj86.Abstract.setValue((None, 0))
    self.obj86.Abstract.config = 0

    # cardinality
    self.obj86.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__leftExpr', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__rightExpr', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj86.cardinality.setValue(lcobj2)

    # display
    self.obj86.display.setValue('Multiplicities:\n  - To leftExpr: 0 to N\n  - To rightExpr: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj86.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1640.0,0.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.5476562500000002, 1.0]
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
    self.obj87.Graphical_Appearance.setValue( ('MT_post__Expression', self.obj87))

    # name
    self.obj87.name.setValue('MT_post__Expression')

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

    # Abstract
    self.obj87.Abstract.setValue((None, 0))
    self.obj87.Abstract.config = 0

    # cardinality
    self.obj87.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__leftExpr', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__rightExpr', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__arg_1', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__arg_2', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj87.cardinality.setValue(lcobj2)

    # display
    self.obj87.display.setValue('Multiplicities:\n  - From leftExpr: 0 to N\n  - From rightExpr: 0 to N\n  - From arg_1: 0 to N\n  - From arg_2: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
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

    self.obj87.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1640.0,280.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.5476562500000002, 1.0844262295081968]
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
    self.obj88.Graphical_Appearance.setValue( ('MT_post__Constant', self.obj88))

    # name
    self.obj88.name.setValue('MT_post__Constant')

    # attributes
    self.obj88.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_post__value', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
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
    self.obj88.attributes.setValue(lcobj2)

    # Abstract
    self.obj88.Abstract.setValue((None, 0))
    self.obj88.Abstract.config = 0

    # cardinality
    self.obj88.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj88.cardinality.setValue(lcobj2)

    # display
    self.obj88.display.setValue('Attributes:\n  - value :: String\nMultiplicities:\n  - From GenericEdge_ECoreMM: 0 to N\n')
    self.obj88.display.setHeight(15)

    # Actions
    self.obj88.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj88.Actions.setValue(lcobj2)

    # Constraints
    self.obj88.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj88.Constraints.setValue(lcobj2)

    self.obj88.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2040.0,280.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.5476562500000002, 1.0]
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
    self.obj89.Graphical_Appearance.setValue( ('MT_post__Concat', self.obj89))

    # name
    self.obj89.name.setValue('MT_post__Concat')

    # attributes
    self.obj89.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj89.attributes.setValue(lcobj2)

    # Abstract
    self.obj89.Abstract.setValue((None, 0))
    self.obj89.Abstract.config = 0

    # cardinality
    self.obj89.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__arg_1', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__arg_2', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj89.cardinality.setValue(lcobj2)

    # display
    self.obj89.display.setValue('Multiplicities:\n  - To arg_1: 0 to N\n  - To arg_2: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
    self.obj89.display.setHeight(15)

    # Actions
    self.obj89.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj89.Actions.setValue(lcobj2)

    # Constraints
    self.obj89.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj89.Constraints.setValue(lcobj2)

    self.obj89.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1820.0,720.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.5476562500000002, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj113=CD_Class3(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # QOCA
    self.obj113.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj113.Graphical_Appearance.setValue( ('MT_post__GenericNode_ECoreMM', self.obj113))

    # name
    self.obj113.name.setValue('MT_post__GenericNode_ECoreMM')

    # attributes
    self.obj113.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj113.attributes.setValue(lcobj2)

    # Abstract
    self.obj113.Abstract.setValue((None, 0))
    self.obj113.Abstract.config = 0

    # cardinality
    self.obj113.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj113.cardinality.setValue(lcobj2)

    # display
    self.obj113.display.setValue('Multiplicities:\n  - To GenericEdge_ECoreMM: 0 to N\n  - From GenericEdge_ECoreMM: 0 to N\n')
    self.obj113.display.setHeight(15)

    # Actions
    self.obj113.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj113.Actions.setValue(lcobj2)

    # Constraints
    self.obj113.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj113.Constraints.setValue(lcobj2)

    self.obj113.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(0.0,0.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.5476562500000002, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj90=CD_Association3(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # QOCA
    self.obj90.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj90.Graphical_Appearance.setValue( ('MT_post__match_contains', self.obj90))
    self.obj90.Graphical_Appearance.linkInfo=linkEditor(self,self.obj90.Graphical_Appearance.semObject, "match_contains")
    self.obj90.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('match_contains_1stLink', self.obj90.Graphical_Appearance.linkInfo.FirstLink))
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('match_contains_1stSegment', self.obj90.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj90.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.Center.setValue( ('match_contains_Center', self.obj90.Graphical_Appearance.linkInfo))
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('match_contains_2ndSegment', self.obj90.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('match_contains_2ndLink', self.obj90.Graphical_Appearance.linkInfo.SecondLink))
    self.obj90.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.Center.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj90.Graphical_Appearance.semObject
    self.obj90.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj90.Graphical_Appearance.semObject

    # name
    self.obj90.name.setValue('MT_post__match_contains')

    # displaySelect
    self.obj90.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj90.displaySelect.config = 0

    # attributes
    self.obj90.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj90.attributes.setValue(lcobj2)

    # cardinality
    self.obj90.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj90.cardinality.setValue(lcobj2)

    # display
    self.obj90.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MatchModel: 0 to N\n')
    self.obj90.display.setHeight(15)

    # Actions
    self.obj90.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj90.Actions.setValue(lcobj2)

    # Constraints
    self.obj90.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj90.Constraints.setValue(lcobj2)

    self.obj90.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(361.8,199.8,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.3230000000000002, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=CD_Association3(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # QOCA
    self.obj91.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj91.Graphical_Appearance.setValue( ('MT_post__apply_contains', self.obj91))
    self.obj91.Graphical_Appearance.linkInfo=linkEditor(self,self.obj91.Graphical_Appearance.semObject, "apply_contains")
    self.obj91.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('apply_contains_1stLink', self.obj91.Graphical_Appearance.linkInfo.FirstLink))
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('apply_contains_1stSegment', self.obj91.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj91.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.Center.setValue( ('apply_contains_Center', self.obj91.Graphical_Appearance.linkInfo))
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('apply_contains_2ndSegment', self.obj91.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('apply_contains_2ndLink', self.obj91.Graphical_Appearance.linkInfo.SecondLink))
    self.obj91.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.Center.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj91.Graphical_Appearance.semObject
    self.obj91.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj91.Graphical_Appearance.semObject

    # name
    self.obj91.name.setValue('MT_post__apply_contains')

    # displaySelect
    self.obj91.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj91.displaySelect.config = 0

    # attributes
    self.obj91.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj91.attributes.setValue(lcobj2)

    # cardinality
    self.obj91.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj91.cardinality.setValue(lcobj2)

    # display
    self.obj91.display.setValue('Multiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From ApplyModel: 0 to N\n')
    self.obj91.display.setHeight(15)

    # Actions
    self.obj91.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj91.Actions.setValue(lcobj2)

    # Constraints
    self.obj91.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj91.Constraints.setValue(lcobj2)

    self.obj91.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(362.491532278,586.86445,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.316, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=CD_Association3(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # QOCA
    self.obj92.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj92.Graphical_Appearance.setValue( ('MT_post__backward_link', self.obj92))
    self.obj92.Graphical_Appearance.linkInfo=linkEditor(self,self.obj92.Graphical_Appearance.semObject, "backward_link")
    self.obj92.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('backward_link_1stLink', self.obj92.Graphical_Appearance.linkInfo.FirstLink))
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('backward_link_1stSegment', self.obj92.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj92.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj92.Graphical_Appearance.linkInfo.Center.setValue( ('backward_link_Center', self.obj92.Graphical_Appearance.linkInfo))
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('backward_link_2ndSegment', self.obj92.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj92.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('backward_link_2ndLink', self.obj92.Graphical_Appearance.linkInfo.SecondLink))
    self.obj92.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj92.Graphical_Appearance.semObject
    self.obj92.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj92.Graphical_Appearance.semObject
    self.obj92.Graphical_Appearance.linkInfo.Center.semObject=self.obj92.Graphical_Appearance.semObject
    self.obj92.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj92.Graphical_Appearance.semObject
    self.obj92.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj92.Graphical_Appearance.semObject

    # name
    self.obj92.name.setValue('MT_post__backward_link')

    # displaySelect
    self.obj92.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj92.displaySelect.config = 0

    # attributes
    self.obj92.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj92.attributes.setValue(lcobj2)

    # cardinality
    self.obj92.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj92.cardinality.setValue(lcobj2)

    # display
    self.obj92.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj92.display.setHeight(15)

    # Actions
    self.obj92.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj92.Actions.setValue(lcobj2)

    # Constraints
    self.obj92.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj92.Constraints.setValue(lcobj2)

    self.obj92.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1245.0,339.5,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=CD_Association3(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # QOCA
    self.obj93.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj93.Graphical_Appearance.setValue( ('MT_post__indirectLink_S', self.obj93))
    self.obj93.Graphical_Appearance.linkInfo=linkEditor(self,self.obj93.Graphical_Appearance.semObject, "indirectLink_S")
    self.obj93.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('indirectLink_S_1stLink', self.obj93.Graphical_Appearance.linkInfo.FirstLink))
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('blue', 20)
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('indirectLink_S_1stSegment', self.obj93.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj93.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj93.Graphical_Appearance.linkInfo.Center.setValue( ('indirectLink_S_Center', self.obj93.Graphical_Appearance.linkInfo))
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('blue', 20)
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('indirectLink_S_2ndSegment', self.obj93.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj93.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('indirectLink_S_2ndLink', self.obj93.Graphical_Appearance.linkInfo.SecondLink))
    self.obj93.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj93.Graphical_Appearance.semObject
    self.obj93.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj93.Graphical_Appearance.semObject
    self.obj93.Graphical_Appearance.linkInfo.Center.semObject=self.obj93.Graphical_Appearance.semObject
    self.obj93.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj93.Graphical_Appearance.semObject
    self.obj93.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj93.Graphical_Appearance.semObject

    # name
    self.obj93.name.setValue('MT_post__indirectLink_S')

    # displaySelect
    self.obj93.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj93.displaySelect.config = 0

    # attributes
    self.obj93.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj93.attributes.setValue(lcobj2)

    # cardinality
    self.obj93.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj93.cardinality.setValue(lcobj2)

    # display
    self.obj93.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj93.display.setHeight(15)

    # Actions
    self.obj93.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj93.Actions.setValue(lcobj2)

    # Constraints
    self.obj93.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj93.Constraints.setValue(lcobj2)

    self.obj93.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1274.5,81.5,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.862, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=CD_Association3(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # QOCA
    self.obj94.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj94.Graphical_Appearance.setValue( ('MT_post__directLink_T', self.obj94))
    self.obj94.Graphical_Appearance.linkInfo=linkEditor(self,self.obj94.Graphical_Appearance.semObject, "directLink_T")
    self.obj94.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_T_1stLink', self.obj94.Graphical_Appearance.linkInfo.FirstLink))
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_T_1stSegment', self.obj94.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj94.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj94.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_T_Center', self.obj94.Graphical_Appearance.linkInfo))
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_T_2ndSegment', self.obj94.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj94.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_T_2ndLink', self.obj94.Graphical_Appearance.linkInfo.SecondLink))
    self.obj94.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj94.Graphical_Appearance.semObject
    self.obj94.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj94.Graphical_Appearance.semObject
    self.obj94.Graphical_Appearance.linkInfo.Center.semObject=self.obj94.Graphical_Appearance.semObject
    self.obj94.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj94.Graphical_Appearance.semObject
    self.obj94.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj94.Graphical_Appearance.semObject

    # name
    self.obj94.name.setValue('MT_post__directLink_T')

    # displaySelect
    self.obj94.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj94.displaySelect.config = 0

    # attributes
    self.obj94.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj94.attributes.setValue(lcobj2)

    # cardinality
    self.obj94.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj94.cardinality.setValue(lcobj2)

    # display
    self.obj94.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj94.display.setHeight(15)

    # Actions
    self.obj94.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj94.Actions.setValue(lcobj2)

    # Constraints
    self.obj94.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj94.Constraints.setValue(lcobj2)

    self.obj94.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1193.0,684.5,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.185483870967742]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=CD_Association3(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # QOCA
    self.obj95.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj95.Graphical_Appearance.setValue( ('MT_post__directLink_S', self.obj95))
    self.obj95.Graphical_Appearance.linkInfo=linkEditor(self,self.obj95.Graphical_Appearance.semObject, "directLink_S")
    self.obj95.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_S_1stLink', self.obj95.Graphical_Appearance.linkInfo.FirstLink))
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_S_1stSegment', self.obj95.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj95.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj95.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_S_Center', self.obj95.Graphical_Appearance.linkInfo))
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_S_2ndSegment', self.obj95.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj95.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_S_2ndLink', self.obj95.Graphical_Appearance.linkInfo.SecondLink))
    self.obj95.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj95.Graphical_Appearance.semObject
    self.obj95.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj95.Graphical_Appearance.semObject
    self.obj95.Graphical_Appearance.linkInfo.Center.semObject=self.obj95.Graphical_Appearance.semObject
    self.obj95.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj95.Graphical_Appearance.semObject
    self.obj95.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj95.Graphical_Appearance.semObject

    # name
    self.obj95.name.setValue('MT_post__directLink_S')

    # displaySelect
    self.obj95.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj95.displaySelect.config = 0

    # attributes
    self.obj95.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj95.attributes.setValue(lcobj2)

    # cardinality
    self.obj95.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj95.cardinality.setValue(lcobj2)

    # display
    self.obj95.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
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

    self.obj95.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(950.5,86.5,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.862, 1.185483870967742]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=CD_Association3(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # QOCA
    self.obj96.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj96.Graphical_Appearance.setValue( ('MT_post__paired_with', self.obj96))
    self.obj96.Graphical_Appearance.linkInfo=linkEditor(self,self.obj96.Graphical_Appearance.semObject, "paired_with")
    self.obj96.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('paired_with_1stLink', self.obj96.Graphical_Appearance.linkInfo.FirstLink))
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('paired_with_1stSegment', self.obj96.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj96.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.Center.setValue( ('paired_with_Center', self.obj96.Graphical_Appearance.linkInfo))
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('paired_with_2ndSegment', self.obj96.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('paired_with_2ndLink', self.obj96.Graphical_Appearance.linkInfo.SecondLink))
    self.obj96.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.Center.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj96.Graphical_Appearance.semObject
    self.obj96.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj96.Graphical_Appearance.semObject

    # name
    self.obj96.name.setValue('MT_post__paired_with')

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
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj96.cardinality.setValue(lcobj2)

    # display
    self.obj96.display.setValue('Multiplicities:\n  - To ApplyModel: 1 to 1\n  - From MatchModel: 1 to 1\n')
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
       new_obj = graph_CD_Association3(136.0,401.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.344, 1.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=CD_Association3(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    # QOCA
    self.obj97.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj97.Graphical_Appearance.setValue( ('MT_post__trace_link', self.obj97))
    self.obj97.Graphical_Appearance.linkInfo=linkEditor(self,self.obj97.Graphical_Appearance.semObject, "trace_link")
    self.obj97.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('trace_link_1stLink', self.obj97.Graphical_Appearance.linkInfo.FirstLink))
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('trace_link_1stSegment', self.obj97.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj97.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj97.Graphical_Appearance.linkInfo.Center.setValue( ('trace_link_Center', self.obj97.Graphical_Appearance.linkInfo))
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('trace_link_2ndSegment', self.obj97.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj97.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('trace_link_2ndLink', self.obj97.Graphical_Appearance.linkInfo.SecondLink))
    self.obj97.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj97.Graphical_Appearance.semObject
    self.obj97.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj97.Graphical_Appearance.semObject
    self.obj97.Graphical_Appearance.linkInfo.Center.semObject=self.obj97.Graphical_Appearance.semObject
    self.obj97.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj97.Graphical_Appearance.semObject
    self.obj97.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj97.Graphical_Appearance.semObject

    # name
    self.obj97.name.setValue('MT_post__trace_link')

    # displaySelect
    self.obj97.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj97.displaySelect.config = 0

    # attributes
    self.obj97.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj97.attributes.setValue(lcobj2)

    # cardinality
    self.obj97.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj97.cardinality.setValue(lcobj2)

    # display
    self.obj97.display.setValue('Multiplicities:\n  - From MetaModelElement_T: 0 to N\n  - To MetaModelElement_S: 0 to N\n')
    self.obj97.display.setHeight(15)

    # Actions
    self.obj97.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj97.Actions.setValue(lcobj2)

    # Constraints
    self.obj97.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj97.Constraints.setValue(lcobj2)

    self.obj97.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1242.0,481.0,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=CD_Association3(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    # QOCA
    self.obj98.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj98.Graphical_Appearance.setValue( ('MT_post__hasAttr_S', self.obj98))
    self.obj98.Graphical_Appearance.linkInfo=linkEditor(self,self.obj98.Graphical_Appearance.semObject, "hasAttr_S")
    self.obj98.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasAttr_S_1stLink', self.obj98.Graphical_Appearance.linkInfo.FirstLink))
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasAttr_S_1stSegment', self.obj98.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj98.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj98.Graphical_Appearance.linkInfo.Center.setValue( ('hasAttr_S_Center', self.obj98.Graphical_Appearance.linkInfo))
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasAttr_S_2ndSegment', self.obj98.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj98.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasAttr_S_2ndLink', self.obj98.Graphical_Appearance.linkInfo.SecondLink))
    self.obj98.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj98.Graphical_Appearance.semObject
    self.obj98.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj98.Graphical_Appearance.semObject
    self.obj98.Graphical_Appearance.linkInfo.Center.semObject=self.obj98.Graphical_Appearance.semObject
    self.obj98.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj98.Graphical_Appearance.semObject
    self.obj98.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj98.Graphical_Appearance.semObject

    # name
    self.obj98.name.setValue('MT_post__hasAttr_S')

    # displaySelect
    self.obj98.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj98.displaySelect.config = 0

    # attributes
    self.obj98.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj98.attributes.setValue(lcobj2)

    # cardinality
    self.obj98.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj98.cardinality.setValue(lcobj2)

    # display
    self.obj98.display.setValue('Multiplicities:\n  - To Attribute: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj98.display.setHeight(15)

    # Actions
    self.obj98.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj98.Actions.setValue(lcobj2)

    # Constraints
    self.obj98.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj98.Constraints.setValue(lcobj2)

    self.obj98.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1346.0,240.975409836,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.862, 1.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=CD_Association3(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # QOCA
    self.obj99.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj99.Graphical_Appearance.setValue( ('MT_post__hasAttr_T', self.obj99))
    self.obj99.Graphical_Appearance.linkInfo=linkEditor(self,self.obj99.Graphical_Appearance.semObject, "hasAttr_T")
    self.obj99.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasAttr_T_1stLink', self.obj99.Graphical_Appearance.linkInfo.FirstLink))
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasAttr_T_1stSegment', self.obj99.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj99.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.Center.setValue( ('hasAttr_T_Center', self.obj99.Graphical_Appearance.linkInfo))
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasAttr_T_2ndSegment', self.obj99.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasAttr_T_2ndLink', self.obj99.Graphical_Appearance.linkInfo.SecondLink))
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.Center.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj99.Graphical_Appearance.semObject

    # name
    self.obj99.name.setValue('MT_post__hasAttr_T')

    # displaySelect
    self.obj99.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj99.displaySelect.config = 0

    # attributes
    self.obj99.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj99.attributes.setValue(lcobj2)

    # cardinality
    self.obj99.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj99.cardinality.setValue(lcobj2)

    # display
    self.obj99.display.setValue('Multiplicities:\n  - To Attribute: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj99.display.setHeight(15)

    # Actions
    self.obj99.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj99.Actions.setValue(lcobj2)

    # Constraints
    self.obj99.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj99.Constraints.setValue(lcobj2)

    self.obj99.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1292.49804688,838.905737705,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=CD_Association3(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    # QOCA
    self.obj100.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj100.Graphical_Appearance.setValue( ('MT_post__leftExpr', self.obj100))
    self.obj100.Graphical_Appearance.linkInfo=linkEditor(self,self.obj100.Graphical_Appearance.semObject, "leftExpr")
    self.obj100.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('leftExpr_1stLink', self.obj100.Graphical_Appearance.linkInfo.FirstLink))
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('leftExpr_1stSegment', self.obj100.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj100.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.Center.setValue( ('leftExpr_Center', self.obj100.Graphical_Appearance.linkInfo))
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('leftExpr_2ndSegment', self.obj100.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('leftExpr_2ndLink', self.obj100.Graphical_Appearance.linkInfo.SecondLink))
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.Center.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj100.Graphical_Appearance.semObject

    # name
    self.obj100.name.setValue('MT_post__leftExpr')

    # displaySelect
    self.obj100.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj100.displaySelect.config = 0

    # attributes
    self.obj100.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj100.attributes.setValue(lcobj2)

    # cardinality
    self.obj100.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Equation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj100.cardinality.setValue(lcobj2)

    # display
    self.obj100.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Equation: 0 to N\n')
    self.obj100.display.setHeight(15)

    # Actions
    self.obj100.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj100.Actions.setValue(lcobj2)

    # Constraints
    self.obj100.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj100.Constraints.setValue(lcobj2)

    self.obj100.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1618.0,211.0,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.204, 1.0]
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=CD_Association3(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # QOCA
    self.obj101.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj101.Graphical_Appearance.setValue( ('MT_post__rightExpr', self.obj101))
    self.obj101.Graphical_Appearance.linkInfo=linkEditor(self,self.obj101.Graphical_Appearance.semObject, "rightExpr")
    self.obj101.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('rightExpr_1stLink', self.obj101.Graphical_Appearance.linkInfo.FirstLink))
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('rightExpr_1stSegment', self.obj101.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj101.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.Center.setValue( ('rightExpr_Center', self.obj101.Graphical_Appearance.linkInfo))
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('rightExpr_2ndSegment', self.obj101.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('rightExpr_2ndLink', self.obj101.Graphical_Appearance.linkInfo.SecondLink))
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.Center.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj101.Graphical_Appearance.semObject

    # name
    self.obj101.name.setValue('MT_post__rightExpr')

    # displaySelect
    self.obj101.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj101.displaySelect.config = 0

    # attributes
    self.obj101.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj101.attributes.setValue(lcobj2)

    # cardinality
    self.obj101.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Equation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj101.cardinality.setValue(lcobj2)

    # display
    self.obj101.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Equation: 0 to N\n')
    self.obj101.display.setHeight(15)

    # Actions
    self.obj101.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj101.Actions.setValue(lcobj2)

    # Constraints
    self.obj101.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj101.Constraints.setValue(lcobj2)

    self.obj101.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1866.15625,208.0,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.204, 1.0]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=CD_Association3(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # QOCA
    self.obj102.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj102.Graphical_Appearance.setValue( ('MT_post__arg_1', self.obj102))
    self.obj102.Graphical_Appearance.linkInfo=linkEditor(self,self.obj102.Graphical_Appearance.semObject, "arg_1")
    self.obj102.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('arg_1_1stLink', self.obj102.Graphical_Appearance.linkInfo.FirstLink))
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('arg_1_1stSegment', self.obj102.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj102.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.Center.setValue( ('arg_1_Center', self.obj102.Graphical_Appearance.linkInfo))
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('arg_1_2ndSegment', self.obj102.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('arg_1_2ndLink', self.obj102.Graphical_Appearance.linkInfo.SecondLink))
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.Center.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj102.Graphical_Appearance.semObject

    # name
    self.obj102.name.setValue('MT_post__arg_1')

    # displaySelect
    self.obj102.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj102.displaySelect.config = 0

    # attributes
    self.obj102.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj102.attributes.setValue(lcobj2)

    # cardinality
    self.obj102.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Concat', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj102.cardinality.setValue(lcobj2)

    # display
    self.obj102.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Concat: 0 to N\n')
    self.obj102.display.setHeight(15)

    # Actions
    self.obj102.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj102.Actions.setValue(lcobj2)

    # Constraints
    self.obj102.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj102.Constraints.setValue(lcobj2)

    self.obj102.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1780.0,551.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.19, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=CD_Association3(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # QOCA
    self.obj103.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj103.Graphical_Appearance.setValue( ('MT_post__arg_2', self.obj103))
    self.obj103.Graphical_Appearance.linkInfo=linkEditor(self,self.obj103.Graphical_Appearance.semObject, "arg_2")
    self.obj103.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('arg_2_1stLink', self.obj103.Graphical_Appearance.linkInfo.FirstLink))
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('arg_2_1stSegment', self.obj103.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj103.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.Center.setValue( ('arg_2_Center', self.obj103.Graphical_Appearance.linkInfo))
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('arg_2_2ndSegment', self.obj103.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('arg_2_2ndLink', self.obj103.Graphical_Appearance.linkInfo.SecondLink))
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.Center.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj103.Graphical_Appearance.semObject

    # name
    self.obj103.name.setValue('MT_post__arg_2')

    # displaySelect
    self.obj103.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj103.displaySelect.config = 0

    # attributes
    self.obj103.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj103.attributes.setValue(lcobj2)

    # cardinality
    self.obj103.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Concat', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj103.cardinality.setValue(lcobj2)

    # display
    self.obj103.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Concat: 0 to N\n')
    self.obj103.display.setHeight(15)

    # Actions
    self.obj103.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj103.Actions.setValue(lcobj2)

    # Constraints
    self.obj103.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj103.Constraints.setValue(lcobj2)

    self.obj103.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1965.53125,535.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.19, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj114=CD_Association3(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # QOCA
    self.obj114.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj114.Graphical_Appearance.setValue( ('MT_post__GenericEdge_ECoreMM', self.obj114))
    self.obj114.Graphical_Appearance.linkInfo=linkEditor(self,self.obj114.Graphical_Appearance.semObject, "GenericEdge_ECoreMM")
    self.obj114.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('GenericEdge_ECoreMM_1stLink', self.obj114.Graphical_Appearance.linkInfo.FirstLink))
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('purple', 20)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('GenericEdge_ECoreMM_1stSegment', self.obj114.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj114.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.Center.setValue( ('GenericEdge_ECoreMM_Center', self.obj114.Graphical_Appearance.linkInfo))
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('purple', 20)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('GenericEdge_ECoreMM_2ndSegment', self.obj114.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('GenericEdge_ECoreMM_2ndLink', self.obj114.Graphical_Appearance.linkInfo.SecondLink))
    self.obj114.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.Center.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj114.Graphical_Appearance.semObject
    self.obj114.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj114.Graphical_Appearance.semObject

    # name
    self.obj114.name.setValue('MT_post__GenericEdge_ECoreMM')

    # displaySelect
    self.obj114.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj114.displaySelect.config = 0

    # attributes
    self.obj114.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj114.attributes.setValue(lcobj2)

    # cardinality
    self.obj114.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericNode_ECoreMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericNode_ECoreMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__EClass', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__EReference', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__EStructuralFeature', (('Source', 'Destination'), 0), '0', 'N'))
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
    cobj2.setValue(('MT_post__Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Equation', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Constant', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Concat', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj114.cardinality.setValue(lcobj2)

    # display
    self.obj114.display.setValue('Multiplicities:\n  - From GenericNode_ECoreMM: 0 to N\n  - To GenericNode_ECoreMM: 0 to N\n  - To MetaModelElement_S: 0 to N\n  - To EClass: 0 to N\n  - To EReference: 0 to N\n  - To EStructuralFeature: 0 to N\n  - To MatchModel: 0 to N\n  - To ApplyModel: 0 to N\n  - To MetaModelElement_T: 0 to N\n  - To Attribute: 0 to N\n  - To Equation: 0 to N\n  - To Expression: 0 to N\n  - To Constant: 0 to N\n  - To Concat: 0 to N\n')
    self.obj114.display.setHeight(15)

    # Actions
    self.obj114.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj114.Actions.setValue(lcobj2)

    # Constraints
    self.obj114.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj114.Constraints.setValue(lcobj2)

    self.obj114.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(0.0,0.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.988, 3.556451612903226]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj104=CD_Inheritance3(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    self.obj104.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(641.4,303.6,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=CD_Inheritance3(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    self.obj105.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(754.6,277.8,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=CD_Inheritance3(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    self.obj106.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(468.4,303.6,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=CD_Inheritance3(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    self.obj107.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1656.0,461.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=CD_Inheritance3(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    self.obj108.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1926.0,405.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=CD_Inheritance3(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    self.obj109.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1831.0,571.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=CD_Inheritance3(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    self.obj110.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(513.5,501.131147541,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=CD_Inheritance3(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    self.obj111.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(626.0,511.131147541,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=CD_Inheritance3(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    self.obj112.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(708.5,501.131147541,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    # Connections for obj78 (graphObject_: Obj61) named MT_post__MetaModelElement_S
    self.drawConnections(
(self.obj78,self.obj93,[711.0, 192.98360655737704, 1274.5, 81.5, 1026.0, 203.0, 1274.5, 81.5],"true", 4),
(self.obj78,self.obj95,[711.0, 192.98360655737704, 950.5, 86.5, 950.5, 86.5],"true", 3),
(self.obj78,self.obj98,[711.0, 243.1081967213115, 1346.0, 240.975409836],"true", 2) )
    # Connections for obj79 (graphObject_: Obj62) named MT_post__EClass
    self.drawConnections(
(self.obj79,self.obj106,[436.0, 341.0, 468.4, 303.6],"true", 2),
(self.obj79,self.obj110,[471.0, 461.0, 513.5, 501.1311475409836],"true", 2) )
    # Connections for obj80 (graphObject_: Obj63) named MT_post__EReference
    self.drawConnections(
(self.obj80,self.obj104,[656.0, 341.0, 641.4, 303.6],"true", 2),
(self.obj80,self.obj111,[616.0, 481.0, 626.0, 511.1311475409836],"true", 2) )
    # Connections for obj81 (graphObject_: Obj64) named MT_post__EStructuralFeature
    self.drawConnections(
(self.obj81,self.obj105,[776.0, 341.0, 754.6, 277.8],"true", 2),
(self.obj81,self.obj112,[741.0, 461.0, 708.5, 501.1311475409836],"true", 2) )
    # Connections for obj82 (graphObject_: Obj65) named MT_post__MatchModel
    self.drawConnections(
(self.obj82,self.obj90,[211.0, 189.0, 361.8, 199.8],"true", 2),
(self.obj82,self.obj96,[136.0, 261.0, 136.0, 401.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj66) named MT_post__ApplyModel
    self.drawConnections(
(self.obj83,self.obj91,[211.0, 581.0, 362.491532278, 586.86445],"true", 2) )
    # Connections for obj84 (graphObject_: Obj67) named MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj84,self.obj92,[711.0, 592.9016393442623, 1245.0, 424.5, 1245.0, 339.5],"true", 3),
(self.obj84,self.obj94,[711.0, 696.1803278688525, 1193.0, 684.5, 1193.0, 684.5],"true", 3),
(self.obj84,self.obj97,[711.0, 592.9016393442623, 990.0, 584.0, 1242.0, 481.0],"true", 3),
(self.obj84,self.obj99,[711.0, 696.1803278688525, 1292.49804688, 838.905737705],"true", 2) )
    # Connections for obj85 (graphObject_: Obj68) named MT_post__Attribute
    self.drawConnections(
(self.obj85,self.obj107,[1636.0, 501.0, 1656.0, 461.0],"true", 2) )
    # Connections for obj86 (graphObject_: Obj69) named MT_post__Equation
    self.drawConnections(
(self.obj86,self.obj100,[1676.0, 141.0, 1618.0, 211.0],"true", 2),
(self.obj86,self.obj101,[1831.0, 121.0, 1866.15625, 208.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj70) named MT_post__Expression
    self.drawConnections(
 )
    # Connections for obj88 (graphObject_: Obj71) named MT_post__Constant
    self.drawConnections(
(self.obj88,self.obj108,[2041.0, 401.0, 1926.0, 405.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj72) named MT_post__Concat
    self.drawConnections(
(self.obj89,self.obj102,[1859.0, 721.0, 1780.0, 551.0],"true", 2),
(self.obj89,self.obj103,[1979.0, 721.0, 1965.53125, 535.0],"true", 2),
(self.obj89,self.obj109,[1859.0, 721.0, 1831.0, 571.0],"true", 2) )
    # Connections for obj113 (graphObject_: Obj119) named MT_post__GenericNode_ECoreMM
    self.drawConnections(
(self.obj113,self.obj114,[1.0, 41.0, -3.0, 5.0], 0, 2) )
    # Connections for obj90 (graphObject_: Obj73) named MT_post__match_contains
    self.drawConnections(
(self.obj90,self.obj78,[361.8, 199.8, 521.0, 192.98360655737704],"true", 2) )
    # Connections for obj91 (graphObject_: Obj75) named MT_post__apply_contains
    self.drawConnections(
(self.obj91,self.obj84,[362.491532278, 586.86445, 521.0, 592.9016393442623],"true", 2) )
    # Connections for obj92 (graphObject_: Obj77) named MT_post__backward_link
    self.drawConnections(
(self.obj92,self.obj78,[1245.0, 339.5, 1245.0, 254.5, 711.0, 243.1081967213115],"true", 3) )
    # Connections for obj93 (graphObject_: Obj79) named MT_post__indirectLink_S
    self.drawConnections(
(self.obj93,self.obj78,[1274.5, 81.5, 1274.5, 81.5, 711.0, 192.98360655737704],"true", 3) )
    # Connections for obj94 (graphObject_: Obj81) named MT_post__directLink_T
    self.drawConnections(
(self.obj94,self.obj84,[1193.0, 684.5, 1193.0, 684.5, 711.0, 696.1803278688525],"true", 3) )
    # Connections for obj95 (graphObject_: Obj83) named MT_post__directLink_S
    self.drawConnections(
(self.obj95,self.obj78,[950.5, 86.5, 950.5, 86.5, 711.0, 192.98360655737704],"true", 3) )
    # Connections for obj96 (graphObject_: Obj85) named MT_post__paired_with
    self.drawConnections(
(self.obj96,self.obj83,[136.0, 401.0, 136.0, 541.0],"true", 2) )
    # Connections for obj97 (graphObject_: Obj87) named MT_post__trace_link
    self.drawConnections(
(self.obj97,self.obj78,[1242.0, 481.0, 937.0, 308.0, 711.0, 291.44262295081967],"true", 3) )
    # Connections for obj98 (graphObject_: Obj89) named MT_post__hasAttr_S
    self.drawConnections(
(self.obj98,self.obj85,[1346.0, 240.97540983606558, 1516.0, 501.0],"true", 2) )
    # Connections for obj99 (graphObject_: Obj91) named MT_post__hasAttr_T
    self.drawConnections(
(self.obj99,self.obj85,[1292.49804688, 838.905737705, 1481.0, 621.0],"true", 2) )
    # Connections for obj100 (graphObject_: Obj93) named MT_post__leftExpr
    self.drawConnections(
(self.obj100,self.obj87,[1618.0, 211.0, 1683.0, 281.0],"true", 2) )
    # Connections for obj101 (graphObject_: Obj95) named MT_post__rightExpr
    self.drawConnections(
(self.obj101,self.obj87,[1866.15625, 208.0, 1803.0, 281.0],"true", 2) )
    # Connections for obj102 (graphObject_: Obj97) named MT_post__arg_1
    self.drawConnections(
(self.obj102,self.obj87,[1780.0, 551.0, 1763.0, 421.0],"true", 2) )
    # Connections for obj103 (graphObject_: Obj99) named MT_post__arg_2
    self.drawConnections(
(self.obj103,self.obj87,[1965.53125, 535.0, 1838.0, 401.0],"true", 2) )
    # Connections for obj114 (graphObject_: Obj120) named MT_post__GenericEdge_ECoreMM
    self.drawConnections(
(self.obj114,self.obj113,[-2.0, 5.0, 151.9375, 1.0], 0, 2),
(self.obj114,self.obj78,[-1.012, 5.0, 521.0, 192.98360655737704], 0, 2),
(self.obj114,self.obj79,[-1.012, 5.0, 316.0, 341.0], 0, 2),
(self.obj114,self.obj80,[-1.012, 5.0, 536.0, 341.0], 0, 2),
(self.obj114,self.obj81,[-1.012, 5.0, 741.0, 381.0], 0, 2),
(self.obj114,self.obj82,[-1.012, 5.0, 176.0, 121.0], 0, 2),
(self.obj114,self.obj83,[-1.012, 5.0, 176.0, 541.0], 0, 2),
(self.obj114,self.obj84,[-1.012, 5.0, 556.0, 541.2622950819672], 0, 2),
(self.obj114,self.obj85,[-1.012, 5.0, 1481.0, 541.0], 0, 2),
(self.obj114,self.obj86,[-1.012, 5.0, 1641.0, 69.0], 0, 2),
(self.obj114,self.obj87,[-1.012, 5.0, 1641.0, 321.0], 0, 2),
(self.obj114,self.obj88,[-1.012, 5.0, 2041.0, 321.0], 0, 2),
(self.obj114,self.obj89,[-1.012, 5.0, 1821.0, 761.0], 0, 2),
(self.obj114,self.obj113,[-2.0, 5.0, 151.9375, 1.0], 0, 2) )
    # Connections for obj104 (graphObject_: Obj101) of type CD_Inheritance3
    self.drawConnections(
(self.obj104,self.obj78,[641.4, 303.6, 636.0, 372.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj103) of type CD_Inheritance3
    self.drawConnections(
(self.obj105,self.obj78,[754.6, 277.8, 711.0, 291.44262295081967],"true", 2) )
    # Connections for obj106 (graphObject_: Obj105) of type CD_Inheritance3
    self.drawConnections(
(self.obj106,self.obj78,[468.4, 303.6, 521.0, 291.44262295081967],"true", 2) )
    # Connections for obj107 (graphObject_: Obj107) of type CD_Inheritance3
    self.drawConnections(
(self.obj107,self.obj87,[1656.0, 461.0, 1683.0, 421.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj109) of type CD_Inheritance3
    self.drawConnections(
(self.obj108,self.obj87,[1926.0, 405.0, 1838.0, 401.0],"true", 2) )
    # Connections for obj109 (graphObject_: Obj111) of type CD_Inheritance3
    self.drawConnections(
(self.obj109,self.obj87,[1831.0, 571.0, 1803.0, 421.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj113) of type CD_Inheritance3
    self.drawConnections(
(self.obj110,self.obj84,[513.5, 501.1311475409836, 556.0, 541.2622950819672],"true", 2) )
    # Connections for obj111 (graphObject_: Obj115) of type CD_Inheritance3
    self.drawConnections(
(self.obj111,self.obj84,[626.0, 511.1311475409836, 636.0, 541.2622950819672],"true", 2) )
    # Connections for obj112 (graphObject_: Obj117) of type CD_Inheritance3
    self.drawConnections(
(self.obj112,self.obj84,[708.5, 501.1311475409836, 676.0, 541.2622950819672],"true", 2) )

newfunction = MT_post__ECore_Copier_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
